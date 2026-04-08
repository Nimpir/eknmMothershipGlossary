"""
seed.py — Drop all tables, recreate schema, load all seed JSON files.
Run: python seed.py
"""

import json
import os
import sqlite3
from pathlib import Path

DB_PATH = os.getenv("DB_PATH", "mothership.db")
SCHEMA_FILE = Path(__file__).parent / "schema.sql"
SEEDS_DIR = Path(__file__).parent / "seeds"

# Load order respects FK dependencies
SEED_ORDER = [
    "source_books",
    "categories",
    "terms",
    "rules",
    "roll_tables",
    "roll_table_entries",
    "items",
    "skills",
    "skill_prerequisites",
    "classes",
    "ships",
    "locations",
    "npcs",
    "content_term_links",
]


def drop_tables(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    # Disable FK checks during drop so order doesn't matter
    cur.execute("PRAGMA foreign_keys = OFF")
    tables = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()
    for (name,) in tables:
        cur.execute(f"DROP TABLE IF EXISTS [{name}]")
    cur.execute("PRAGMA foreign_keys = ON")
    conn.commit()
    print("  Dropped all existing tables.")


def create_schema(conn: sqlite3.Connection) -> None:
    sql = SCHEMA_FILE.read_text(encoding="utf-8")
    conn.executescript(sql)
    conn.commit()
    print("  Schema created.")


def load_seed(conn: sqlite3.Connection, table: str) -> None:
    seed_file = SEEDS_DIR / f"{table}.json"
    if not seed_file.exists():
        print(f"  [SKIP] {table}.json not found")
        return

    rows = json.loads(seed_file.read_text(encoding="utf-8"))
    if not rows:
        print(f"  [EMPTY] {table}.json")
        return

    columns = list(rows[0].keys())
    placeholders = ", ".join("?" for _ in columns)
    col_str = ", ".join(f"[{c}]" for c in columns)
    sql = f"INSERT INTO [{table}] ({col_str}) VALUES ({placeholders})"

    values = [tuple(row.get(c) for c in columns) for row in rows]
    conn.executemany(sql, values)
    conn.commit()
    print(f"  Loaded {len(rows):>4} rows -> {table}")


def main() -> None:
    print(f"\nSeeding database: {DB_PATH}\n")

    # Remove old DB so we start clean
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"  Removed old {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    print("\n[1] Recreating schema...")
    create_schema(conn)

    print("\n[2] Loading seed data...")
    for table in SEED_ORDER:
        load_seed(conn, table)

    conn.close()
    print(f"\nDone. Database written to: {DB_PATH}\n")


if __name__ == "__main__":
    main()
