"""
scripts/update_pages_add_image_url.py
Add image_url column to the pages table (idempotent).
Backfills P35 with the ProsperosDream.png image path.
Run: python scripts/update_pages_add_image_url.py
"""
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — pages.image_url column ensured; P35 image path set.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    # Add column if it doesn't already exist (idempotent)
    existing = {row[1] for row in conn.execute("PRAGMA table_info(pages)").fetchall()}
    if "image_url" not in existing:
        conn.execute("ALTER TABLE pages ADD COLUMN image_url TEXT")

    # Backfill P35 with the station overview image
    conn.execute(
        "UPDATE pages SET image_url = ? WHERE id = 35",
        ("images/A Pound of Flesh/ProsperosDream.png",),
    )


if __name__ == "__main__":
    run()
