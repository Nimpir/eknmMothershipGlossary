"""
scripts/add_modules_page.py
Create the Modules page (P41) under P1 and move A Pound of Flesh (P31) under it.
Run: python scripts/add_modules_page.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — 1 page added (P41 Modules), P1 linked_pages updated.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    # Insert Modules page (P41) with P31 as child
    conn.execute(
        """
        INSERT INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (41, '📦', NULL, NULL, json('[31]'))
        ON CONFLICT(id) DO UPDATE SET
            icon = excluded.icon,
            source_slug = excluded.source_slug,
            source_page = excluded.source_page,
            linked_pages = excluded.linked_pages
        """
    )

    # i18n for Modules page — all three languages
    for lang, name in [("en", "Modules"), ("ru", "Модули"), ("ua", "Модулі")]:
        conn.execute(
            """
            INSERT INTO page_i18n (page_id, lang, name)
            VALUES (?, ?, ?)
            ON CONFLICT(page_id, lang) DO UPDATE SET name = excluded.name
            """,
            (41, lang, name),
        )

    # Update P1: replace 31 with 41 in linked_pages
    conn.execute(
        """
        UPDATE pages
        SET linked_pages = json('[22, 3, 11, 23, 41]')
        WHERE id = 1
        """
    )


if __name__ == "__main__":
    run()
