"""
scripts/update_p50_merge_denizen_tables.py
Merge C307 (Names), C308 (Who Are They?), C309 (What do they want?) on P50
into a single C307 table named "Denizens of The Dream".
Each entry becomes: "XX-XX: <name> | <who> | <want>"
C308 and C309 are deleted.
NOTE: Superseded by update_apof_denizens_split.py which now handles this inline.
      Keep for historical reference — already applied to production DB.
Run: python scripts/update_p50_merge_denizen_tables.py
"""
import json, os, re, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# New names for the merged content item per language
NAMES = {
    "en": "Denizens of The Dream",
    "ru": "Обитатели Мечты",
    "ua": "Мешканці Мрії",
}


def strip_range_prefix(text: str) -> str:
    """Remove leading 'XX-XX: ' or 'XX: ' range prefix from entry text."""
    return re.sub(r"^\d{2}(?:-\d{2})?: ", "", text, count=1)


def merge_str_entries(e307: list, e308: list, e309: list) -> list:
    """Merge three lists of plain-string dice_entries."""
    merged = []
    for a, b, c in zip(e307, e308, e309):
        merged.append(f"{a} | {strip_range_prefix(b)} | {strip_range_prefix(c)}")
    return merged


def merge_obj_entries(e307: list, e308: list, e309: list) -> list:
    """Merge three lists of dict dice entries (contents.dice.entries)."""
    merged = []
    for a, b, c in zip(e307, e308, e309):
        merged.append({
            "min":  a["min"],
            "max":  a["max"],
            "text": f"{a['text']} | {strip_range_prefix(b['text'])} | {strip_range_prefix(c['text'])}",
        })
    return merged


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — C307 updated with merged entries; C308 and C309 deleted.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    # ── 1. Load dice_entries for all 3 tables (use 'en' as canonical) ──────
    def get_entries(cid: int, lang: str) -> list:
        row = conn.execute(
            "SELECT dice_entries FROM content_i18n WHERE content_id=? AND lang=?",
            (cid, lang),
        ).fetchone()
        return json.loads(row[0]) if row and row[0] else []

    # ── 2. Build merged entries for each language ───────────────────────────
    for lang in ("en", "ru", "ua"):
        e307 = get_entries(307, lang)
        e308 = get_entries(308, lang)
        e309 = get_entries(309, lang)
        merged = merge_str_entries(e307, e308, e309)
        merged_json = json.dumps(merged, ensure_ascii=False)

        conn.execute(
            "UPDATE content_i18n SET name=?, dice_entries=? WHERE content_id=307 AND lang=?",
            (NAMES[lang], merged_json, lang),
        )

    # ── 3. Update contents.dice (canonical / non-localised) ────────────────
    def get_obj_entries(cid: int) -> list:
        row = conn.execute("SELECT dice FROM contents WHERE id=?", (cid,)).fetchone()
        d = json.loads(row[0]) if row and row[0] else {}
        return d.get("entries", [])

    e307_en = get_obj_entries(307)
    e308_en = get_obj_entries(308)
    e309_en = get_obj_entries(309)
    merged_en = merge_obj_entries(e307_en, e308_en, e309_en)

    dice_field = json.loads(
        conn.execute("SELECT dice FROM contents WHERE id=307").fetchone()[0]
    )
    dice_field["entries"] = merged_en
    conn.execute(
        "UPDATE contents SET dice=? WHERE id=307",
        (json.dumps(dice_field, ensure_ascii=False),),
    )

    # ── 4. Remove C308 and C309 from page_contents ─────────────────────────
    conn.execute("DELETE FROM page_contents WHERE content_id IN (308, 309)")

    # ── 5. Delete content_i18n rows for C308 and C309 ──────────────────────
    conn.execute("DELETE FROM content_i18n WHERE content_id IN (308, 309)")

    # ── 6. Delete C308 and C309 from contents ──────────────────────────────
    conn.execute("DELETE FROM contents WHERE id IN (308, 309)")

    # ── 7. Remove any content_links involving C308 / C309 ──────────────────
    conn.execute(
        "DELETE FROM content_links WHERE from_content_id IN (308, 309) OR to_content_id IN (308, 309)"
    )


if __name__ == "__main__":
    run()
