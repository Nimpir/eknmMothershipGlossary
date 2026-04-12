"""
scripts/update_station_structure.py
Flatten P35 The Station: remove sub-pages P42-P49 if they exist and place
all 8 location content items directly on P35 (no intermediate pages).
Idempotent — safe to re-run on any DB state.
Run: python scripts/update_station_structure.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

STATION_PAGE_ID = 35
SUB_PAGE_IDS = [42, 43, 44, 45, 46, 47, 48, 49]

# Direct P35 buttons — one per location (8 total).
# Sub-items (C231, C234, C236, C238, C239, C241, C243, C244) and dice tables
# (C329–C333) are accessible only via content_links from their parent location.
P35_CONTENT_ORDER = [
    (229,  1),
    (230,  4),
    (232,  6),
    (233,  8),
    (235, 10),
    (237, 12),
    (240, 15),
    (242, 19),
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — P35 flat structure ensured; P42-P49 removed if present.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    placeholders = ",".join("?" * len(SUB_PAGE_IDS))

    # Remove sub-pages if they still exist
    conn.execute(f"DELETE FROM page_contents WHERE page_id IN ({placeholders})", SUB_PAGE_IDS)
    conn.execute(f"DELETE FROM page_i18n WHERE page_id IN ({placeholders})", SUB_PAGE_IDS)
    conn.execute(f"DELETE FROM pages WHERE id IN ({placeholders})", SUB_PAGE_IDS)

    # Clear P35 linked_pages
    conn.execute("UPDATE pages SET linked_pages = '[]' WHERE id = ?", (STATION_PAGE_ID,))

    # Place content directly on P35
    for content_id, sort_order in P35_CONTENT_ORDER:
        conn.execute(
            "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (?, ?, ?)",
            (STATION_PAGE_ID, content_id, sort_order),
        )


if __name__ == "__main__":
    run()
