"""
scripts/add_character_page.py
Create P22 Character — a hub page grouping Character Creation (P7),
Weapons & Damage (P2), Armour (P6), and Ports & Shore Leave (P20).

Also:
  - Removes P2, P4, P6, P7, P20 from P1's linked_pages and adds P22.
  - Adds P4 (Wounds & Death) to P3 (Combat) as a linked sub-page.

Run: python scripts/add_character_page.py
"""

import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── P22 data ──────────────────────────────────────────────────────────────────

P22 = {
    "id":   22,
    "icon": "👤",
    "linked_pages": [7, 2, 6, 20],   # Character Creation, Weapons & Damage, Armour, Ports
    "i18n": [
        (
            "en",
            "Character",
            "Everything about your character: who they are, what they carry, and "
            "how they survive. Covers character creation, weapons & damage, "
            "armour, and ports.",
        ),
        (
            "ru",
            "Персонаж",
            "Всё о вашем персонаже: кто он, что несёт и как выживает. "
            "Включает создание персонажа, оружие и урон, броню и порты.",
        ),
        (
            "ua",
            "Персонаж",
            "Все про вашого персонажа: хто він, що несе і як виживає. "
            "Включає створення персонажа, зброю та пошкодження, броню і порти.",
        ),
    ],
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _set_linked_pages(conn: sqlite3.Connection, page_id: int, pages: list[int]) -> None:
    conn.execute(
        "UPDATE pages SET linked_pages=? WHERE id=?",
        (json.dumps(pages), page_id),
    )


def _get_linked_pages(conn: sqlite3.Connection, page_id: int) -> list[int]:
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (page_id,)).fetchone()
    return json.loads(row[0]) if row else []


# ── Seed ──────────────────────────────────────────────────────────────────────

def _seed(conn: sqlite3.Connection) -> None:
    # ── Create P22 ────────────────────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, linked_pages)
        VALUES (?, ?, NULL, ?)
    """, (P22["id"], P22["icon"], json.dumps(P22["linked_pages"])))

    # Update linked_pages in case the row already existed
    _set_linked_pages(conn, P22["id"], P22["linked_pages"])

    for lang, name, desc in P22["i18n"]:
        conn.execute("""
            INSERT INTO page_i18n (page_id, lang, name, desc)
            VALUES (?, ?, ?, ?)
            ON CONFLICT (page_id, lang) DO UPDATE SET name=excluded.name, desc=excluded.desc
        """, (P22["id"], lang, name, desc))

    # ── Update P1: remove P2,P4,P6,P7,P20 and add P22 ────────────────────────
    p1_pages = _get_linked_pages(conn, 1)
    remove = {2, 4, 6, 7, 20}
    p1_pages = [p for p in p1_pages if p not in remove]
    if P22["id"] not in p1_pages:
        p1_pages.append(P22["id"])
    _set_linked_pages(conn, 1, p1_pages)

    # ── Update P3 (Combat): add P4 (Wounds & Death) as a sub-page ─────────────
    p3_pages = _get_linked_pages(conn, 3)
    if 4 not in p3_pages:
        p3_pages.append(4)
    _set_linked_pages(conn, 3, p3_pages)


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — P22 Character created; P1 and P3 updated in '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
