"""
scripts/update_p54_sort_order.py
Reorder page_contents on P54 (Space Stations):
  C305, C341, C299, C298, C304, C306
Run: python scripts/update_p54_sort_order.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

ORDER = [305, 341, 299, 298, 304, 306]

def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — P54 page_contents reordered.")
    finally:
        conn.close()

def _seed(conn: sqlite3.Connection) -> None:
    for i, content_id in enumerate(ORDER, start=1):
        conn.execute(
            "UPDATE page_contents SET sort_order = ? WHERE page_id = 54 AND content_id = ?",
            (i, content_id),
        )

if __name__ == "__main__":
    run()
