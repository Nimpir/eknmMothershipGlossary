"""
scripts/regenerate_data_sql.py
Regenerate data.sql from the current live DB.

Run this after every migration script to keep the Docker seed in sync:
    python scripts/regenerate_data_sql.py

Output: data.sql (project root)
"""

import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH   = os.getenv("DB_PATH", "mothership.db")
BASE_DIR  = os.path.dirname(os.path.dirname(__file__))
OUT_PATH  = os.path.join(BASE_DIR, "data.sql")

TABLES = [
    "sources",
    "pages",
    "page_i18n",
    "contents",
    "content_i18n",
    "page_contents",
    "content_links",
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    lines: list[str] = []

    for table in TABLES:
        lines.append(f"-- {table}")
        for stmt in conn.iterdump():
            if stmt.startswith(f'INSERT INTO "{table}"'):
                lines.append(
                    stmt.replace(f'INSERT INTO "{table}"',
                                 f'INSERT OR IGNORE INTO "{table}"', 1)
                )

    conn.close()

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    counts = {t: sum(1 for l in lines if f'INTO "{t}"' in l) for t in TABLES}
    print(f"data.sql regenerated ({DB_PATH}):")
    for t, n in counts.items():
        print(f"  {t}: {n} rows")


if __name__ == "__main__":
    run()
