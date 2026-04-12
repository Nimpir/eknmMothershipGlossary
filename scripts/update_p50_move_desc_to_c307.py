"""
scripts/update_p50_move_desc_to_c307.py
Move P50 (Denizens of The Dream) page description into C307 content desc,
then clear the page-level desc.
NOTE: Superseded by update_apof_denizens_split.py which now handles this inline.
      Keep for historical reference — already applied to production DB.
Run: python scripts/update_p50_move_desc_to_c307.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

EN_DESC = (
    "Feel free to use these random NPCs as proprietors, victims, patrons or anything else "
    "that is not provided in this module. They can be used as is, mixed up or as a jumping "
    "off point for your own NPCs. They all want something and are flawed humans. "
    "Breathe life into them."
)

def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — P50 desc moved to C307, P50 desc cleared.")
    finally:
        conn.close()

def _migrate(conn: sqlite3.Connection) -> None:
    # Set C307 desc for all languages (ru/ua keep English as placeholder)
    for lang, text in [("en", EN_DESC), ("ru", EN_DESC), ("ua", EN_DESC)]:
        conn.execute(
            "UPDATE content_i18n SET desc = ? WHERE content_id = 307 AND lang = ?",
            (text, lang),
        )

    # Clear P50 desc for all languages
    conn.execute(
        "UPDATE page_i18n SET desc = NULL WHERE page_id = 50",
    )

if __name__ == "__main__":
    run()
