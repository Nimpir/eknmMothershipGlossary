"""
seed.py — Initialize the database schema and create the root page (P1).
Run once before starting the bot for the first time, or after a schema change.

Usage:
    python seed.py
"""

import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")


def init_db() -> None:
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        schema = f.read()

    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(schema)
        _seed_main_page(conn)
        conn.commit()
        print(f"Database initialized: {DB_PATH}")
    finally:
        conn.close()


def _seed_main_page(conn: sqlite3.Connection) -> None:
    """Create P1 — the root navigation page."""
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, linked_pages)
        VALUES (1, '🚀', NULL, '[]')
    """)
    for lang, name, desc in [
        ("en", "Mothership RPG",  "Quick reference for the Mothership RPG."),
        ("ru", "Mothership RPG",  "Справочник по Mothership RPG."),
        ("ua", "Mothership RPG",  "Довідник по Mothership RPG."),
    ]:
        conn.execute("""
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name, desc)
            VALUES (1, ?, ?, ?)
        """, (lang, name, desc))


if __name__ == "__main__":
    init_db()
