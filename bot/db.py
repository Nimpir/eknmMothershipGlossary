"""
db.py — Database access layer for the Mothership bot.
Queries for the pages / contents schema.
"""

import json
import logging
import os
import sqlite3
import time

DB_PATH = os.getenv("DB_PATH", "mothership.db")
logger  = logging.getLogger(__name__)


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _row(row: sqlite3.Row | None) -> dict | None:
    return dict(row) if row else None


def _rows(rows: list[sqlite3.Row]) -> list[dict]:
    return [dict(r) for r in rows]


# ─────────────────────────────────────────────
# PAGES
# ─────────────────────────────────────────────

def get_page(page_id: int, lang: str = "en") -> dict | None:
    """Fetch a page with i18n fields. Falls back to 'en' when translation is missing."""
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT p.id, p.icon, p.source_slug, p.source_page, p.linked_pages,
                      p.workflow_steps,
                      COALESCE(i18n.name, en.name) AS name,
                      COALESCE(i18n.desc, en.desc)  AS desc
               FROM pages p
               LEFT JOIN page_i18n i18n ON i18n.page_id = p.id AND i18n.lang = ?
               LEFT JOIN page_i18n en   ON en.page_id   = p.id AND en.lang   = 'en'
               WHERE p.id = ?""",
            (lang, page_id)
        ).fetchone())
    if row:
        row["linked_pages"]   = json.loads(row["linked_pages"])   if row["linked_pages"]   else []
        row["workflow_steps"] = json.loads(row["workflow_steps"]) if row["workflow_steps"] else None
    return row


def get_workflow_contents(page_id: int, lang: str = "en") -> list[dict] | None:
    """Return ordered list of full content dicts for a workflow page, or None if no workflow."""
    page = get_page(page_id, lang)
    if not page or not page.get("workflow_steps"):
        return None
    return [c for cid in page["workflow_steps"] if (c := get_content(cid, lang)) is not None]


def get_pages_by_ids(page_ids: list[int], lang: str = "en") -> list[dict]:
    """Fetch multiple pages by ID list, preserving the given order."""
    if not page_ids:
        return []
    placeholders = ",".join("?" * len(page_ids))
    with _conn() as conn:
        rows = _rows(conn.execute(
            f"""SELECT p.id, p.icon,
                       COALESCE(i18n.name, en.name) AS name
                FROM pages p
                LEFT JOIN page_i18n i18n ON i18n.page_id = p.id AND i18n.lang = ?
                LEFT JOIN page_i18n en   ON en.page_id   = p.id AND en.lang   = 'en'
                WHERE p.id IN ({placeholders})""",
            [lang] + list(page_ids)
        ).fetchall())
    by_id = {r["id"]: r for r in rows}
    return [by_id[pid] for pid in page_ids if pid in by_id]


# ─────────────────────────────────────────────
# CONTENTS
# ─────────────────────────────────────────────

def get_content(content_id: int, lang: str = "en") -> dict | None:
    """Fetch a content item with i18n. Falls back to 'en'."""
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT c.id, c.icon, c.image_url, c.tg_file_id,
                      c.subinfo_fixed, c.dice, c.source_slug, c.source_page,
                      COALESCE(i18n.name, en.name)                    AS name,
                      COALESCE(i18n.desc, en.desc)                     AS desc,
                      COALESCE(i18n.subinfo_text, en.subinfo_text)     AS subinfo_text,
                      COALESCE(i18n.dice_entries, en.dice_entries)     AS dice_entries
               FROM contents c
               LEFT JOIN content_i18n i18n ON i18n.content_id = c.id AND i18n.lang = ?
               LEFT JOIN content_i18n en   ON en.content_id   = c.id AND en.lang   = 'en'
               WHERE c.id = ?""",
            (lang, content_id)
        ).fetchone())
    if row:
        cid = row.get("id")
        try:
            row["subinfo_fixed"] = json.loads(row["subinfo_fixed"]) if row["subinfo_fixed"] else []
        except json.JSONDecodeError:
            logger.warning("Bad JSON in subinfo_fixed for content %s", cid)
            row["subinfo_fixed"] = []
        try:
            row["dice"] = json.loads(row["dice"]) if row["dice"] else None
        except json.JSONDecodeError:
            logger.warning("Bad JSON in dice for content %s", cid)
            row["dice"] = None
        try:
            row["subinfo_text"] = json.loads(row["subinfo_text"]) if row["subinfo_text"] else []
        except json.JSONDecodeError:
            logger.warning("Bad JSON in subinfo_text for content %s", cid)
            row["subinfo_text"] = []
        try:
            dice_entries = json.loads(row.pop("dice_entries")) if row.get("dice_entries") else None
        except json.JSONDecodeError:
            logger.warning("Bad JSON in dice_entries for content %s", cid)
            dice_entries = None
            row.pop("dice_entries", None)
        if row["dice"] and dice_entries:
            for i, entry in enumerate(row["dice"]["entries"]):
                if i < len(dice_entries) and dice_entries[i]:
                    raw = dice_entries[i]
                    entry["text"] = raw["text"] if isinstance(raw, dict) else raw
    return row


def get_page_contents(page_id: int, lang: str = "en") -> list[dict]:
    """Fetch all contents on a page ordered by sort_order."""
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT c.id, c.icon,
                      COALESCE(i18n.name, en.name) AS name,
                      pc.sort_order
               FROM page_contents pc
               JOIN contents c ON c.id = pc.content_id
               LEFT JOIN content_i18n i18n ON i18n.content_id = c.id AND i18n.lang = ?
               LEFT JOIN content_i18n en   ON en.content_id   = c.id AND en.lang   = 'en'
               WHERE pc.page_id = ?
               ORDER BY pc.sort_order, c.id""",
            (lang, page_id)
        ).fetchall())
    return rows


def get_content_links(content_id: int, lang: str = "en") -> list[dict]:
    """Fetch outgoing content links for a content item."""
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT cl.to_content_id AS id, cl.label_key,
                      COALESCE(i18n.name, en.name) AS name,
                      c.icon
               FROM content_links cl
               JOIN contents c ON c.id = cl.to_content_id
               LEFT JOIN content_i18n i18n ON i18n.content_id = c.id AND i18n.lang = ?
               LEFT JOIN content_i18n en   ON en.content_id   = c.id AND en.lang   = 'en'
               WHERE cl.from_content_id = ?
               ORDER BY cl.sort_order""",
            (lang, content_id)
        ).fetchall())
    return rows


def update_tg_file_id(content_id: int, file_id: str) -> None:
    """Cache Telegram file_id after first successful image send."""
    with _conn() as conn:
        conn.execute(
            "UPDATE contents SET tg_file_id = ? WHERE id = ?",
            (file_id, content_id)
        )


# ─────────────────────────────────────────────
# SEARCH
# ─────────────────────────────────────────────

def search(query: str, lang: str = "en") -> list[dict]:
    """FTS5 search across pages and contents in the user's language."""
    safe = query.replace('"', '""').strip()
    if not safe:
        return []
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT entity_type, entity_id, name,
                      snippet(search_fts, 4, '<b>', '</b>', '…', 10) AS snippet
               FROM search_fts
               WHERE search_fts MATCH ? AND lang = ?
               ORDER BY rank
               LIMIT 20""",
            (f'"{safe}"*', lang)
        ).fetchall())
    return rows


# ─────────────────────────────────────────────
# USER STATE
# ─────────────────────────────────────────────

def get_user_state(user_id: int) -> dict | None:
    """Load persisted user state. Returns None if no record."""
    with _conn() as conn:
        row = _row(conn.execute(
            "SELECT lang, nav_stack, last_msg_id, last_query FROM user_state WHERE user_id = ?",
            (user_id,)
        ).fetchone())
    if not row:
        return None
    try:
        row["nav_stack"] = json.loads(row["nav_stack"]) if row["nav_stack"] else []
    except json.JSONDecodeError:
        logger.warning("Bad JSON in nav_stack for user %s", user_id)
        row["nav_stack"] = []
    return row


def save_user_state(
    user_id: int,
    lang: str,
    nav_stack: list,
    last_msg_id: int | None = None,
    last_query: str | None = None,
) -> None:
    with _conn() as conn:
        conn.execute(
            """INSERT INTO user_state (user_id, lang, nav_stack, last_msg_id, last_query, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(user_id) DO UPDATE SET
                   lang        = excluded.lang,
                   nav_stack   = excluded.nav_stack,
                   last_msg_id = excluded.last_msg_id,
                   last_query  = excluded.last_query,
                   updated_at  = excluded.updated_at""",
            (user_id, lang, json.dumps(nav_stack), last_msg_id, last_query, int(time.time()))
        )


def cleanup_user_state(days: int = 90) -> int:
    """Delete user_state rows not updated within the given number of days."""
    cutoff = int(time.time()) - days * 86400
    with _conn() as conn:
        cursor = conn.execute(
            "DELETE FROM user_state WHERE updated_at < ?", (cutoff,)
        )
    return cursor.rowcount


def set_user_lang(user_id: int, lang: str) -> None:
    with _conn() as conn:
        conn.execute(
            """INSERT INTO user_state (user_id, lang, nav_stack, updated_at)
               VALUES (?, ?, '[]', ?)
               ON CONFLICT(user_id) DO UPDATE SET
                   lang       = excluded.lang,
                   updated_at = excluded.updated_at""",
            (user_id, lang, int(time.time()))
        )
