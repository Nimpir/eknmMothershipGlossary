"""
scripts/add_space_stations_page.py
Create P54 Space Stations under P38 Tables.
Move station-related sub-pages (P52, P53) and content items
(C298, C299, C304, C305, C306, C341) from P38 to P54.
Run: python scripts/add_space_stations_page.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

NEW_PAGE_ID   = 54
PARENT_PAGE   = 38

# Sub-pages moving from P38 → P54
MOVED_SUBPAGES = [52, 53]

# Content items moving from P38 → P54 (in display order)
MOVED_CONTENTS = [298, 299, 304, 305, 306, 341]

I18N = [
    ("en", "Space Stations",        None),
    ("ru", "Космические Станции",   None),
    ("ua", "Космічні Станції",      None),
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — P54 Space Stations created; P52, P53, C298, C299, C304, C305, C306, C341 moved from P38.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    # 1. Create P54
    conn.execute(
        """INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
           VALUES (?, '🛰️', 'apof', 38, ?)""",
        (NEW_PAGE_ID, json.dumps(MOVED_SUBPAGES)),
    )
    conn.execute(
        "UPDATE pages SET icon='🛰️', linked_pages=? WHERE id=?",
        (json.dumps(MOVED_SUBPAGES), NEW_PAGE_ID),
    )

    # 2. P54 i18n
    for lang, name, desc in I18N:
        conn.execute(
            """INSERT INTO page_i18n (page_id, lang, name, desc)
               VALUES (?, ?, ?, ?)
               ON CONFLICT(page_id, lang) DO UPDATE SET name=excluded.name, desc=excluded.desc""",
            (NEW_PAGE_ID, lang, name, desc),
        )

    # 3. Move content items: delete from P38, insert into P54
    conn.execute(
        "DELETE FROM page_contents WHERE page_id=? AND content_id IN ({})".format(
            ",".join("?" * len(MOVED_CONTENTS))
        ),
        [PARENT_PAGE] + MOVED_CONTENTS,
    )
    for sort_order, content_id in enumerate(MOVED_CONTENTS, start=1):
        conn.execute(
            "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (?, ?, ?)",
            (NEW_PAGE_ID, content_id, sort_order),
        )

    # 4. Update P38 linked_pages: remove P52/P53, add P54
    p38 = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (PARENT_PAGE,)).fetchone()
    current = json.loads(p38["linked_pages"]) if p38["linked_pages"] else []
    updated = [pid for pid in current if pid not in MOVED_SUBPAGES] + [NEW_PAGE_ID]
    conn.execute("UPDATE pages SET linked_pages=? WHERE id=?", (json.dumps(updated), PARENT_PAGE))

    # Re-sequence remaining P38 page_contents sort_order
    remaining = conn.execute(
        "SELECT content_id FROM page_contents WHERE page_id=? ORDER BY sort_order",
        (PARENT_PAGE,),
    ).fetchall()
    for i, row in enumerate(remaining, start=1):
        conn.execute(
            "UPDATE page_contents SET sort_order=? WHERE page_id=? AND content_id=?",
            (i, PARENT_PAGE, row["content_id"]),
        )


if __name__ == "__main__":
    run()
