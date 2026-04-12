"""
scripts/update_c341_links_order.py
Move C342 to first position in C341's content_links (sort_order = -1).
Run: python scripts/update_c341_links_order.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done -- C341->C342 link moved to sort_order=-1 (first).")
    finally:
        conn.close()

def _seed(conn: sqlite3.Connection) -> None:
    conn.execute(
        "UPDATE content_links SET sort_order = -1 WHERE from_content_id = 341 AND to_content_id = 342",
    )

if __name__ == "__main__":
    run()
