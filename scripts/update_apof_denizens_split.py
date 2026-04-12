"""
scripts/update_apof_denizens_split.py
Split C300 "Denizens of The Dream" (one big table) into a page (P50) containing
three separate dice tables: Names (C307), Who Are They? (C308), What do they want? (C309).
Run AFTER: update_apof_dice_format.py (which must fix C300 before this script deletes it).
Run: python scripts/update_apof_denizens_split.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

P38_ID = 38
NEW_PAGE_ID = 50

C_NAMES = 307
C_WHO = 308
C_WANT = 309

DESC_EN = (
    "Feel free to use these random NPCs as proprietors, victims, patrons or anything "
    "else that is not provided in this module. They can be used as is, mixed up or as "
    "a jumping off point for your own NPCs. They all want something and are flawed "
    "humans. Breathe life into them."
)
DESC_RU = DESC_EN  # placeholder
DESC_UA = DESC_EN  # placeholder


def _parse_roll(roll_str: str) -> tuple[int, int]:
    """Parse "00-02" → (0, 2), "07" → (7, 7)."""
    roll_str = roll_str.strip()
    if "-" in roll_str:
        a, b = roll_str.split("-", 1)
        return int(a), int(b)
    return int(roll_str), int(roll_str)


def _split_entries(
    entries: list[str],
) -> tuple[list[str], list[str], list[str], list[tuple[int, int]]]:
    """
    Each entry: "{roll}: {Name} — {Role} — {Quote}"
    Returns (names, roles, quotes, roll_ranges) as parallel lists.
    roll_ranges is a list of (min, max) int tuples.
    """
    names, roles, quotes, ranges = [], [], [], []
    for entry in entries:
        colon_idx = entry.index(": ")
        roll_str = entry[:colon_idx]
        roll_prefix = entry[: colon_idx + 2]     # "00-02: "
        rest = entry[colon_idx + 2:]

        parts = rest.split(" \u2014 ", maxsplit=2)  # split on " — "
        name = parts[0].strip()
        role = parts[1].strip() if len(parts) > 1 else ""
        quote = parts[2].strip() if len(parts) > 2 else ""

        names.append(f"{roll_prefix}{name}")
        roles.append(f"{roll_prefix}{role}")
        quotes.append(f"{roll_prefix}{quote}")
        ranges.append(_parse_roll(roll_str))

    return names, roles, quotes, ranges


def _build_dice_json(entries_text: list[str], ranges: list[tuple[int, int]]) -> str:
    """Build the dice JSON expected by the bot: {"die": "d100", "entries": [...]}."""
    return json.dumps({
        "die": "d100",
        "entries": [
            {"min": lo, "max": hi, "text": text}
            for text, (lo, hi) in zip(entries_text, ranges)
        ],
    })


def _seed(conn: sqlite3.Connection) -> None:
    # ── Read existing C300 dice entries ──────────────────────────────────────
    row = conn.execute(
        "SELECT dice_entries FROM content_i18n WHERE content_id = 300 AND lang = 'en'"
    ).fetchone()
    if not row or not row[0]:
        raise RuntimeError("C300 en dice_entries not found — already migrated?")

    raw_entries = json.loads(row[0])
    names_en, roles_en, quotes_en, ranges = _split_entries(raw_entries)

    # ru/ua entries are the same as en (untranslated placeholders)
    names_ru, roles_ru, quotes_ru = names_en, roles_en, quotes_en
    names_ua, roles_ua, quotes_ua = names_en, roles_en, quotes_en

    dice_names = _build_dice_json(names_en, ranges)
    dice_who   = _build_dice_json(roles_en, ranges)
    dice_want  = _build_dice_json(quotes_en, ranges)

    # ── Create P50 "Denizens of The Dream" ───────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (?, '👤', 'apof', NULL, '[]')
    """, (NEW_PAGE_ID,))
    conn.execute("""
        UPDATE pages SET workflow_steps = '[307,308,309]' WHERE id = ?
    """, (NEW_PAGE_ID,))

    for lang, name, desc in [
        ("en", "Denizens of The Dream", DESC_EN),
        ("ru", "Обитатели Мечты", DESC_RU),
        ("ua", "Мешканці Мрії", DESC_UA),
    ]:
        conn.execute("""
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name, desc)
            VALUES (?, ?, ?, ?)
        """, (NEW_PAGE_ID, lang, name, desc))

    # ── Add P50 to P38 linked_pages ──────────────────────────────────────────
    lp_raw = conn.execute("SELECT linked_pages FROM pages WHERE id = ?", (P38_ID,)).fetchone()[0]
    lp = json.loads(lp_raw)
    if NEW_PAGE_ID not in lp:
        lp.append(NEW_PAGE_ID)
        conn.execute("UPDATE pages SET linked_pages = ? WHERE id = ?", (json.dumps(lp), P38_ID))

    # ── Create C307 Names ─────────────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (?, '🎲', 'apof', NULL, ?, 1)
    ON CONFLICT(id) DO UPDATE SET dice = excluded.dice
    """, (C_NAMES, dice_names))
    for lang, name, entries in [
        ("en", "Names",   names_en),
        ("ru", "Имена",   names_ru),
        ("ua", "Імена",   names_ua),
    ]:
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (?, ?, ?, ?, ?)
        """, (C_NAMES, lang, name, None, json.dumps(entries)))
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (?, ?, 1)
    """, (NEW_PAGE_ID, C_NAMES))

    # ── Create C308 Who Are They? ─────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (?, '👤', 'apof', NULL, ?, 2)
    ON CONFLICT(id) DO UPDATE SET dice = excluded.dice
    """, (C_WHO, dice_who))
    for lang, name, entries in [
        ("en", "Who Are They?", roles_en),
        ("ru", "Кто они?",      roles_ru),
        ("ua", "Хто вони?",     roles_ua),
    ]:
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (?, ?, ?, ?, ?)
        """, (C_WHO, lang, name, None, json.dumps(entries)))
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (?, ?, 2)
    """, (NEW_PAGE_ID, C_WHO))

    # ── Create C309 What do they want? ────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (?, '💬', 'apof', NULL, ?, 3)
    ON CONFLICT(id) DO UPDATE SET dice = excluded.dice
    """, (C_WANT, dice_want))
    for lang, name, entries in [
        ("en", "What do they want?",   quotes_en),
        ("ru", "Чего они хотят?",      quotes_ru),
        ("ua", "Чого вони хочуть?",    quotes_ua),
    ]:
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (?, ?, ?, ?, ?)
        """, (C_WANT, lang, name, None, json.dumps(entries)))
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (?, ?, 3)
    """, (NEW_PAGE_ID, C_WANT))

    # ── Remove C300 from P38 page_contents ───────────────────────────────────
    conn.execute(
        "DELETE FROM page_contents WHERE page_id = ? AND content_id = 300", (P38_ID,)
    )

    # ── Delete C300 content_i18n and contents ─────────────────────────────────
    conn.execute("DELETE FROM content_i18n WHERE content_id = 300")
    conn.execute("DELETE FROM contents WHERE id = 300")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(
            "Done — P50 'Denizens of The Dream' created; "
            "C307 Names, C308 Who Are They?, C309 What do they want? added; "
            "C300 deleted."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
