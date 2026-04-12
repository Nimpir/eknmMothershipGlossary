"""
scripts/update_apof_denizens_split.py
Replace C300 "Denizens of The Dream" (one big table) with a single merged C307
placed directly on P38. Each entry combines Name, Role and Quote into one row:
  "XX-XX: <Name> | <Role> | <Quote>"
C300 is deleted. No sub-page (P50) is created.
Run AFTER: update_apof_dice_format.py (which must fix C300 before this script deletes it).
Run: python scripts/update_apof_denizens_split.py
"""
import json
import os
import re
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

P38_ID = 38
C_DENIZENS = 307

DESC_EN = (
    "Feel free to use these random NPCs as proprietors, victims, patrons or anything "
    "else that is not provided in this module. They can be used as is, mixed up or as "
    "a jumping off point for your own NPCs. They all want something and are flawed "
    "humans. Breathe life into them."
)
DESC_RU = DESC_EN  # placeholder
DESC_UA = DESC_EN  # placeholder

NAMES = {
    "en": "Denizens of The Dream",
    "ru": "Обитатели Мечты",
    "ua": "Мешканці Мрії",
}


def _parse_roll(roll_str: str) -> tuple[int, int]:
    """Parse "00-02" → (0, 2), "07" → (7, 7)."""
    roll_str = roll_str.strip()
    if "-" in roll_str:
        a, b = roll_str.split("-", 1)
        return int(a), int(b)
    return int(roll_str), int(roll_str)


def _strip_range_prefix(text: str) -> str:
    return re.sub(r"^\d{2}(?:-\d{2})?: ", "", text, count=1)


def _merge_entries(
    entries: list[str],
) -> tuple[list[str], list[dict], list[tuple[int, int]]]:
    """
    Each C300 entry: "{roll}: {Name} — {Role} — {Quote}"
    Returns:
      str_entries  — plain strings for content_i18n.dice_entries
      obj_entries  — dicts for contents.dice
      ranges       — (min, max) pairs
    """
    str_entries, obj_entries, ranges = [], [], []
    for entry in entries:
        colon_idx = entry.index(": ")
        roll_str   = entry[:colon_idx]
        roll_prefix = entry[: colon_idx + 2]
        rest = entry[colon_idx + 2:]

        parts = rest.split(" \u2014 ", maxsplit=2)
        name  = parts[0].strip()
        role  = parts[1].strip() if len(parts) > 1 else ""
        quote = parts[2].strip() if len(parts) > 2 else ""

        merged_text = f"{roll_prefix}{name} | {role} | {quote}"
        lo, hi = _parse_roll(roll_str)

        str_entries.append(merged_text)
        obj_entries.append({"min": lo, "max": hi, "text": merged_text})
        ranges.append((lo, hi))

    return str_entries, obj_entries, ranges


def _seed(conn: sqlite3.Connection) -> None:
    # ── Read existing C300 dice entries ──────────────────────────────────────
    row = conn.execute(
        "SELECT dice_entries FROM content_i18n WHERE content_id = 300 AND lang = 'en'"
    ).fetchone()
    if not row or not row[0]:
        raise RuntimeError("C300 en dice_entries not found — already migrated?")

    raw_entries = json.loads(row[0])
    str_entries, obj_entries, _ = _merge_entries(raw_entries)

    dice_json = json.dumps({"die": "d100", "entries": obj_entries}, ensure_ascii=False)
    str_json  = json.dumps(str_entries, ensure_ascii=False)

    # ── Create C307 ───────────────────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (?, '🎲', 'apof', NULL, ?, 1)
        ON CONFLICT(id) DO UPDATE SET dice = excluded.dice
    """, (C_DENIZENS, dice_json))

    for lang, name, desc in [
        ("en", NAMES["en"], DESC_EN),
        ("ru", NAMES["ru"], DESC_RU),
        ("ua", NAMES["ua"], DESC_UA),
    ]:
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(content_id, lang) DO UPDATE SET
                name        = excluded.name,
                desc        = excluded.desc,
                dice_entries = excluded.dice_entries
        """, (C_DENIZENS, lang, name, desc, str_json))

    # ── Add C307 to P38 page_contents ─────────────────────────────────────────
    # Determine next sort_order after existing P38 contents
    max_order = conn.execute(
        "SELECT COALESCE(MAX(sort_order), 0) FROM page_contents WHERE page_id = ?",
        (P38_ID,),
    ).fetchone()[0]
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (?, ?, ?)
    """, (P38_ID, C_DENIZENS, max_order + 1))

    # ── Remove C300 from P38 page_contents ───────────────────────────────────
    conn.execute(
        "DELETE FROM page_contents WHERE page_id = ? AND content_id = 300", (P38_ID,)
    )

    # ── Delete C300 ───────────────────────────────────────────────────────────
    conn.execute("DELETE FROM content_i18n WHERE content_id = 300")
    conn.execute("DELETE FROM contents WHERE id = 300")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — C307 'Denizens of The Dream' created on P38; C300 deleted.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
