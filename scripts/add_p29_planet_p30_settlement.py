"""
scripts/add_p29_planet_p30_settlement.py
Create P29 (Planet) and P30 (Settlement) as sub-pages of P28 (Random Generators).
Moves planet contents (C199, C207, C208, C209) to P29 and
settlement contents (C200, C201, C202, C203, C204, C205, C210, C211) to P30.
C206 (Random Lore) remains on P28.
Run: python scripts/add_p29_planet_p30_settlement.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

PLANET_CONTENTS     = [199, 207, 208, 209]
SETTLEMENT_CONTENTS = [200, 201, 202, 203, 204, 205, 210, 211]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — P29 (Planet) and P30 (Settlement) created under P28; 12 contents moved.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    # ── Insert P29 Planet ─────────────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (29, '🪐', 'wom', 58, '[]')
    """)
    conn.execute("""
        UPDATE pages SET workflow_steps = '[199,207,208,209]' WHERE id = 29
    """)
    for lang, name in (("en", "Planet"), ("ru", "Планета"), ("ua", "Планета")):
        conn.execute("""
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
            VALUES (29, ?, ?)
        """, (lang, name))

    # ── Insert P30 Settlement ─────────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (30, '🏘️', 'wom', 58, '[]')
    """)
    conn.execute("""
        UPDATE pages SET workflow_steps = '[200,201,202,203,204,205,210,211]' WHERE id = 30
    """)
    for lang, name in (("en", "Settlement"), ("ru", "Поселение"), ("ua", "Поселення")):
        conn.execute("""
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
            VALUES (30, ?, ?)
        """, (lang, name))

    # ── Update P28 linked_pages → [29, 30] ────────────────────────────────────
    row = conn.execute("SELECT linked_pages FROM pages WHERE id = 28").fetchone()
    current = json.loads(row[0]) if row and row[0] else []
    new_linked = current[:]
    for pid in (29, 30):
        if pid not in new_linked:
            new_linked.append(pid)
    conn.execute("UPDATE pages SET linked_pages = ? WHERE id = 28", (json.dumps(new_linked),))

    # ── Move planet contents: remove from P28, add to P29 ────────────────────
    for sort, cid in enumerate(PLANET_CONTENTS, start=1):
        conn.execute("DELETE FROM page_contents WHERE page_id = 28 AND content_id = ?", (cid,))
        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (29, ?, ?)
        """, (cid, sort))

    # ── Move settlement contents: remove from P28, add to P30 ─────────────────
    for sort, cid in enumerate(SETTLEMENT_CONTENTS, start=1):
        conn.execute("DELETE FROM page_contents WHERE page_id = 28 AND content_id = ?", (cid,))
        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (30, ?, ?)
        """, (cid, sort))


if __name__ == "__main__":
    run()
