"""
scripts/update_dry_dock_sublinking.py
Move C329 (Dry Dock Rumors) and C330 (Ships Currently Docked) from being
direct buttons on P35 to being sub-items accessible from C229 (01 Dry Dock).
Adds content_links C229→C329 and C229→C330; removes C329/C330 from page_contents.
Run: python scripts/update_dry_dock_sublinking.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — C329/C330 removed from P35; linked under C229.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    # Remove C329/C330 from P35 direct contents
    conn.execute(
        "DELETE FROM page_contents WHERE page_id = 35 AND content_id IN (329, 330)"
    )

    # Add forward links from C229 to its dice tables
    conn.execute(
        "INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key, sort_order) VALUES (229, 329, 'related', 0)"
    )
    conn.execute(
        "INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key, sort_order) VALUES (229, 330, 'related', 1)"
    )


if __name__ == "__main__":
    run()
