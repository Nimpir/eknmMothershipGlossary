"""
db.py — All database query functions for the Mothership bot.
"""

import json
import os
import sqlite3
import time
from typing import Any

DB_PATH = os.getenv("DB_PATH", "mothership.db")


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
# LOCALISATION HELPER
# ─────────────────────────────────────────────

def _localize(row: dict, lang: str, fields: list[str]) -> dict:
    """
    For each field, replace its value with the translated version when available.
    Falls back to the base English value if the translation is missing or empty.

    Example: _localize(row, "ua", ["name", "body"])
      → row["name"] = row["name_ua"] if non-empty, else keeps row["name"]
    """
    if lang == "en":
        return row
    for field in fields:
        translated = row.get(f"{field}_{lang}")
        if translated:
            row[field] = translated
    return row


def _localize_many(rows: list[dict], lang: str, fields: list[str]) -> list[dict]:
    return [_localize(r, lang, fields) for r in rows]


# ─────────────────────────────────────────────
# CATEGORIES
# ─────────────────────────────────────────────

def get_top_level_categories(lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            "SELECT * FROM categories WHERE parent_id IS NULL ORDER BY sort_order, name"
        ).fetchall())
    return _localize_many(rows, lang, ["name"])


def get_subcategories(parent_id: int, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            "SELECT * FROM categories WHERE parent_id = ? ORDER BY sort_order, name",
            (parent_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["name"])


def get_category(cat_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            "SELECT * FROM categories WHERE id = ?", (cat_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "description"])
    return row


def get_term_tables_for_category(cat_id: int, lang: str = "en") -> list[dict]:
    """Return [{term_name, table_id, table_name, dice_notation}] for terms linked to a category
    that each have exactly one roll table — used to build a 'generate all' action."""
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT t.id AS term_id, t.name AS term_name, t.name_ua AS term_name_ua,
                      t.name_ru AS term_name_ru,
                      rt.id AS table_id, rt.name AS table_name, rt.dice_notation
               FROM content_term_links ctl_cat
               JOIN terms t ON t.id = ctl_cat.term_id
               JOIN content_term_links ctl_table ON ctl_table.term_id = t.id
                    AND ctl_table.content_type = 'roll_table'
               JOIN roll_tables rt ON rt.id = ctl_table.content_id
               WHERE ctl_cat.content_type = 'category' AND ctl_cat.content_id = ?
               ORDER BY ctl_cat.sort_order, t.name""",
            (cat_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["term_name"])


def get_category_breadcrumb(cat_id: int, lang: str = "en") -> list[dict]:
    """Returns list from root → given category."""
    breadcrumb = []
    with _conn() as conn:
        current = cat_id
        while current:
            row = conn.execute(
                "SELECT * FROM categories WHERE id = ?", (current,)
            ).fetchone()
            if not row:
                break
            d = dict(row)
            _localize(d, lang, ["name"])
            breadcrumb.insert(0, d)
            current = row["parent_id"]
    return breadcrumb


def category_has_children(cat_id: int) -> bool:
    with _conn() as conn:
        row = conn.execute(
            "SELECT COUNT(*) FROM categories WHERE parent_id = ?", (cat_id,)
        ).fetchone()
        return row[0] > 0


# ─────────────────────────────────────────────
# RULES
# ─────────────────────────────────────────────

def get_rules_by_category(cat_id: int, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT r.*, s.short_code AS book_code
               FROM rules r
               LEFT JOIN source_books s ON s.id = r.source_book_id
               WHERE r.category_id = ?
               ORDER BY r.sort_order, r.title""",
            (cat_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["title", "body"])


def get_rule(rule_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT r.*, s.short_code AS book_code
               FROM rules r
               LEFT JOIN source_books s ON s.id = r.source_book_id
               WHERE r.id = ?""",
            (rule_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["title", "body"])
    return row


# ─────────────────────────────────────────────
# TERMS (GLOSSARY)
# ─────────────────────────────────────────────

def get_all_terms(lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT t.*, s.short_code AS book_code
               FROM terms t
               LEFT JOIN source_books s ON s.id = t.source_book_id
               ORDER BY t.name""",
        ).fetchall())
    return _localize_many(rows, lang, ["name", "body"])


def get_term(term_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT t.*, s.short_code AS book_code
               FROM terms t
               LEFT JOIN source_books s ON s.id = t.source_book_id
               WHERE t.id = ?""",
            (term_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "body"])
    return row


def get_term_by_name(name: str, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT t.*, s.short_code AS book_code
               FROM terms t
               LEFT JOIN source_books s ON s.id = t.source_book_id
               WHERE LOWER(t.name) = LOWER(?)""",
            (name,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "body"])
    return row


def get_linked_terms(content_type: str, content_id: int, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT t.id, t.name, t.name_ua, t.name_ru
               FROM content_term_links ctl
               JOIN terms t ON t.id = ctl.term_id
               WHERE ctl.content_type = ? AND ctl.content_id = ?
               ORDER BY ctl.sort_order, t.name""",
            (content_type, content_id)
        ).fetchall())
    return _localize_many(rows, lang, ["name"])


def get_roll_tables_for_rule(rule_id: int, lang: str = "en") -> list[dict]:
    """Return roll tables linked directly to a rule via content_term_links (content_type='rule_table')."""
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT rt.id, rt.name, rt.name_ua, rt.name_ru, rt.dice_notation, ctl.sort_order
               FROM content_term_links ctl
               JOIN roll_tables rt ON rt.id = ctl.content_id
               WHERE ctl.content_type = 'rule_table' AND ctl.term_id = ?
               ORDER BY ctl.sort_order, rt.name""",
            (rule_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["name"])


def get_term_tables_for_rule(rule_id: int, lang: str = "en") -> list[dict]:
    """Return [{term_name, table_id, table_name, dice_notation}] for terms linked to a rule
    that each have exactly one roll table — used to build a 'generate all' action."""
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT t.id AS term_id, t.name AS term_name, t.name_ua AS term_name_ua,
                      t.name_ru AS term_name_ru,
                      rt.id AS table_id, rt.name AS table_name, rt.dice_notation
               FROM content_term_links ctl_rule
               JOIN terms t ON t.id = ctl_rule.term_id
               JOIN content_term_links ctl_table ON ctl_table.term_id = t.id
                    AND ctl_table.content_type = 'roll_table'
               JOIN roll_tables rt ON rt.id = ctl_table.content_id
               WHERE ctl_rule.content_type = 'rule' AND ctl_rule.content_id = ?
               ORDER BY ctl_rule.sort_order, t.name""",
            (rule_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["term_name"])


def roll_random_entry(table_id: int, lang: str = "en") -> dict | None:
    """Pick a random entry from a roll table by simulating a dice roll."""
    import random
    with _conn() as conn:
        entries = _rows(conn.execute(
            "SELECT * FROM roll_table_entries WHERE table_id = ? ORDER BY roll_min",
            (table_id,)
        ).fetchall())
    if not entries:
        return None
    max_roll = entries[-1]["roll_max"]
    roll = random.randint(entries[0]["roll_min"], max_roll)
    for entry in entries:
        if entry["roll_min"] <= roll <= entry["roll_max"]:
            return _localize(entry, lang, ["result_text", "label"])
    return _localize(entries[-1], lang, ["result_text", "label"])


def get_roll_tables_for_term(term_id: int, lang: str = "en") -> list[dict]:
    """Return roll tables linked to a term via content_term_links."""
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT rt.id, rt.name, rt.name_ua, rt.name_ru, rt.dice_notation
               FROM content_term_links ctl
               JOIN roll_tables rt ON rt.id = ctl.content_id
               WHERE ctl.content_type = 'roll_table' AND ctl.term_id = ?
               ORDER BY rt.name""",
            (term_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["name"])


# ─────────────────────────────────────────────
# ROLL TABLES
# ─────────────────────────────────────────────

def get_roll_tables_by_category(cat_id: int, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT rt.*, s.short_code AS book_code
               FROM roll_tables rt
               LEFT JOIN source_books s ON s.id = rt.source_book_id
               WHERE rt.category_id = ?
               ORDER BY rt.sort_order, rt.name""",
            (cat_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["name", "description"])


def get_all_roll_tables(lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT rt.*, s.short_code AS book_code, c.name AS category_name
               FROM roll_tables rt
               LEFT JOIN source_books s ON s.id = rt.source_book_id
               LEFT JOIN categories c ON c.id = rt.category_id
               ORDER BY rt.name"""
        ).fetchall())
    return _localize_many(rows, lang, ["name", "description"])


def get_roll_table(table_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT rt.*, s.short_code AS book_code
               FROM roll_tables rt
               LEFT JOIN source_books s ON s.id = rt.source_book_id
               WHERE rt.id = ?""",
            (table_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "description"])
    return row


def get_table_entries(table_id: int, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            "SELECT * FROM roll_table_entries WHERE table_id = ? ORDER BY roll_min",
            (table_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["result_text"])


def get_entry(entry_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            "SELECT * FROM roll_table_entries WHERE id = ?",
            (entry_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["result_text"])
    return row


def get_entry_for_roll(table_id: int, roll: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT * FROM roll_table_entries
               WHERE table_id = ? AND roll_min <= ? AND roll_max >= ?""",
            (table_id, roll, roll)
        ).fetchone())
    if row:
        _localize(row, lang, ["result_text"])
    return row


# ─────────────────────────────────────────────
# ITEMS (EQUIPMENT)
# ─────────────────────────────────────────────

def get_items_by_type(item_type: str, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT i.*, s.short_code AS book_code
               FROM items i
               LEFT JOIN source_books s ON s.id = i.source_book_id
               WHERE i.item_type = ?
               ORDER BY i.name""",
            (item_type,)
        ).fetchall())
    return _localize_many(rows, lang, ["name", "description", "special_rules"])


def get_item(item_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT i.*, s.short_code AS book_code
               FROM items i
               LEFT JOIN source_books s ON s.id = i.source_book_id
               WHERE i.id = ?""",
            (item_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "description", "special_rules"])
    return row


def find_items_in_text(text: str, lang: str = "en") -> list[dict]:
    """Return items whose name appears (case-insensitive) in the given text."""
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT i.*, s.short_code AS book_code
               FROM items i
               LEFT JOIN source_books s ON s.id = i.source_book_id
               WHERE INSTR(LOWER(?), LOWER(i.name)) > 0
               ORDER BY i.name""",
            (text,)
        ).fetchall())
    return _localize_many(rows, lang, ["name", "description", "special_rules"])


# ─────────────────────────────────────────────
# SKILLS
# ─────────────────────────────────────────────

def get_all_skills(lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            "SELECT * FROM skills ORDER BY tier, name"
        ).fetchall())
    return _localize_many(rows, lang, ["name", "description"])


def get_skill(skill_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = conn.execute("SELECT * FROM skills WHERE id = ?", (skill_id,)).fetchone()
        if not row:
            return None
        skill = dict(row)
        _localize(skill, lang, ["name", "description"])
        # Prerequisite names — use translated name if available
        name_col = f"name_{lang}" if lang != "en" else "name"
        prereqs = conn.execute(
            f"""SELECT COALESCE(s.{name_col}, s.name) AS prereq_name
               FROM skill_prerequisites sp
               JOIN skills s ON s.id = sp.prerequisite_id
               WHERE sp.skill_id = ?
               ORDER BY s.name""",
            (skill_id,)
        ).fetchall()
        skill["prerequisite_names"] = [r["prereq_name"] for r in prereqs]
    return skill


def get_skill_tree(lang: str = "en") -> list[dict]:
    """Returns all skills with their full prerequisite structure."""
    name_col = f"name_{lang}" if lang != "en" else "name"
    with _conn() as conn:
        skills = _rows(conn.execute(
            "SELECT * FROM skills ORDER BY tier, name"
        ).fetchall())
        prereq_rows = _rows(conn.execute(
            f"""SELECT sp.skill_id, COALESCE(s.{name_col}, s.name) AS prereq_name
               FROM skill_prerequisites sp
               JOIN skills s ON s.id = sp.prerequisite_id"""
        ).fetchall())
    prereq_map: dict[int, list[str]] = {}
    for r in prereq_rows:
        prereq_map.setdefault(r["skill_id"], []).append(r["prereq_name"])
    for skill in skills:
        _localize(skill, lang, ["name", "description"])
        skill["prerequisite_names"] = prereq_map.get(skill["id"], [])
    return skills


# ─────────────────────────────────────────────
# CLASSES
# ─────────────────────────────────────────────

def get_all_classes(lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            "SELECT * FROM classes ORDER BY name"
        ).fetchall())
    return _localize_many(rows, lang, ["name", "description", "special_abilities", "trauma_response"])


def get_class(class_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            "SELECT * FROM classes WHERE id = ?", (class_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "description", "special_abilities", "trauma_response"])
    return row


# ─────────────────────────────────────────────
# SHIPS
# ─────────────────────────────────────────────

def get_all_ships(lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT sh.*, s.short_code AS book_code
               FROM ships sh
               LEFT JOIN source_books s ON s.id = sh.source_book_id
               ORDER BY sh.class, sh.name"""
        ).fetchall())
    return _localize_many(rows, lang, ["name", "description"])


def get_ship(ship_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT sh.*, s.short_code AS book_code
               FROM ships sh
               LEFT JOIN source_books s ON s.id = sh.source_book_id
               WHERE sh.id = ?""",
            (ship_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "description"])
    return row


# ─────────────────────────────────────────────
# LOCATIONS
# ─────────────────────────────────────────────

def get_locations_by_book(source_book_id: int, parent_id: int | None = None, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        if parent_id is None:
            rows = conn.execute(
                """SELECT * FROM locations
                   WHERE source_book_id = ? AND parent_id IS NULL
                   ORDER BY name""",
                (source_book_id,)
            ).fetchall()
        else:
            rows = conn.execute(
                """SELECT * FROM locations
                   WHERE source_book_id = ? AND parent_id = ?
                   ORDER BY name""",
                (source_book_id, parent_id)
            ).fetchall()
    return _localize_many(_rows(rows), lang, ["name", "description"])


def get_child_locations(parent_id: int, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            "SELECT * FROM locations WHERE parent_id = ? ORDER BY name",
            (parent_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["name", "description"])


def get_location(loc_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT l.*, s.short_code AS book_code, p.name AS parent_name
               FROM locations l
               LEFT JOIN source_books s ON s.id = l.source_book_id
               LEFT JOIN locations p ON p.id = l.parent_id
               WHERE l.id = ?""",
            (loc_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "description"])
    return row


# ─────────────────────────────────────────────
# NPCs
# ─────────────────────────────────────────────

def get_npcs_by_book(source_book_id: int, lang: str = "en") -> list[dict]:
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT n.*, s.short_code AS book_code, l.name AS location_name
               FROM npcs n
               LEFT JOIN source_books s ON s.id = n.source_book_id
               LEFT JOIN locations l ON l.id = n.location_id
               WHERE n.source_book_id = ?
               ORDER BY n.name""",
            (source_book_id,)
        ).fetchall())
    return _localize_many(rows, lang, ["name", "role", "description", "special_rules"])


def get_npc(npc_id: int, lang: str = "en") -> dict | None:
    with _conn() as conn:
        row = _row(conn.execute(
            """SELECT n.*, s.short_code AS book_code, l.name AS location_name
               FROM npcs n
               LEFT JOIN source_books s ON s.id = n.source_book_id
               LEFT JOIN locations l ON l.id = n.location_id
               WHERE n.id = ?""",
            (npc_id,)
        ).fetchone())
    if row:
        _localize(row, lang, ["name", "role", "description", "special_rules"])
    return row


# ─────────────────────────────────────────────
# SEARCH
# ─────────────────────────────────────────────

def search_all(query: str) -> dict[str, list[dict]]:
    """Full-text search across all content types. Returns dict of results."""
    q = f"%{query.lower()}%"
    results: dict[str, list[dict]] = {}

    with _conn() as conn:
        rules = _rows(conn.execute(
            "SELECT id, title, 'rule' AS type FROM rules WHERE LOWER(title) LIKE ? OR LOWER(body) LIKE ?",
            (q, q)
        ).fetchall())
        if rules:
            results["Rules"] = rules

        terms = _rows(conn.execute(
            "SELECT id, name AS title, 'term' AS type FROM terms WHERE LOWER(name) LIKE ? OR LOWER(body) LIKE ? OR LOWER(aliases) LIKE ?",
            (q, q, q)
        ).fetchall())
        if terms:
            results["Glossary"] = terms

        items = _rows(conn.execute(
            "SELECT id, name AS title, item_type AS type FROM items WHERE LOWER(name) LIKE ? OR LOWER(description) LIKE ?",
            (q, q)
        ).fetchall())
        if items:
            results["Equipment"] = items

        npcs = _rows(conn.execute(
            "SELECT id, name AS title, 'npc' AS type FROM npcs WHERE LOWER(name) LIKE ? OR LOWER(description) LIKE ?",
            (q, q)
        ).fetchall())
        if npcs:
            results["NPCs"] = npcs

        locations = _rows(conn.execute(
            "SELECT id, name AS title, 'location' AS type FROM locations WHERE LOWER(name) LIKE ? OR LOWER(description) LIKE ?",
            (q, q)
        ).fetchall())
        if locations:
            results["Locations"] = locations

        tables = _rows(conn.execute(
            "SELECT id, name AS title, 'table' AS type FROM roll_tables WHERE LOWER(name) LIKE ? OR LOWER(description) LIKE ?",
            (q, q)
        ).fetchall())
        if tables:
            results["Roll Tables"] = tables

    return results


# ─────────────────────────────────────────────
# USER NAV STATE + LANGUAGE
# ─────────────────────────────────────────────

def save_nav_state(user_id: int, nav_current: str | None, nav_stack: list, language: str = "en") -> None:
    """Persist a user's nav stack and language preference to the database."""
    with _conn() as conn:
        conn.execute(
            """INSERT INTO user_nav_state (user_id, nav_current, nav_stack, language, saved_at)
               VALUES (?, ?, ?, ?, ?)
               ON CONFLICT(user_id) DO UPDATE SET
                   nav_current = excluded.nav_current,
                   nav_stack   = excluded.nav_stack,
                   language    = excluded.language,
                   saved_at    = excluded.saved_at""",
            (user_id, nav_current, json.dumps(nav_stack), language, int(time.time())),
        )


def load_nav_state(user_id: int) -> dict | None:
    """Load a user's persisted nav stack and language. Returns None if no saved state."""
    with _conn() as conn:
        row = conn.execute(
            "SELECT nav_current, nav_stack, language FROM user_nav_state WHERE user_id = ?",
            (user_id,),
        ).fetchone()
    if not row:
        return None
    return {
        "nav_current": row["nav_current"],
        "nav_stack": json.loads(row["nav_stack"]),
        "language": row["language"] or "en",
    }


def set_user_language(user_id: int, language: str) -> None:
    """Upsert only the language field for a user."""
    with _conn() as conn:
        conn.execute(
            """INSERT INTO user_nav_state (user_id, nav_current, nav_stack, language, saved_at)
               VALUES (?, NULL, '[]', ?, ?)
               ON CONFLICT(user_id) DO UPDATE SET
                   language = excluded.language,
                   saved_at = excluded.saved_at""",
            (user_id, language, int(time.time())),
        )
