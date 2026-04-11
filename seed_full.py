"""
seed_full.py — Initialize the database from the canonical data snapshot.

Creates the schema (schema.sql) and inserts all content (data.sql).
Idempotent: safe to re-run; existing rows are left unchanged.

Usage:
    python seed_full.py
"""

import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")
BASE_DIR = os.path.dirname(__file__)


def init_db() -> None:
    schema = open(os.path.join(BASE_DIR, "schema.sql"), encoding="utf-8").read()
    data   = open(os.path.join(BASE_DIR, "data.sql"),   encoding="utf-8").read()

    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(schema)
        conn.executescript(data)
        conn.commit()
        print(f"Database initialized: {DB_PATH}")
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
