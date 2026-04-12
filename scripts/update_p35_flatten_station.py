"""
scripts/update_p35_flatten_station.py
Flatten P35 The Station: remove sub-pages P42-P49 and move their content
items directly under P35. Deletes the now-empty intermediate pages.
Run: python scripts/update_p35_flatten_station.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# Content items per former sub-page, in original sort order
SUBPAGE_CONTENTS = [
    (42, [229, 329, 330]),
    (43, [230, 231]),
    (44, [232, 331]),
    (45, [233, 234]),
    (46, [235, 236]),
    (47, [237, 238, 239]),
    (48, [240, 241, 332, 333]),
    (49, [242, 243, 244]),
]
SUB_PAGE_IDS = [sp[0] for sp in SUBPAGE_CONTENTS]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — P35 flattened; P42-P49 deleted.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    # 1. Clear P35 linked_pages
    conn.execute("UPDATE pages SET linked_pages = '[]' WHERE id = 35")

    # 2. Move all content items to P35 with sequential sort_order
    # Remove any existing page_contents for P35 first (idempotent)
    conn.execute("DELETE FROM page_contents WHERE page_id = 35")

    sort = 1
    for _page_id, contents in SUBPAGE_CONTENTS:
        for cid in contents:
            conn.execute(
                "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (?, ?, ?)",
                (35, cid, sort),
            )
            sort += 1

    # 3. Delete page_contents for the sub-pages
    conn.execute(
        f"DELETE FROM page_contents WHERE page_id IN ({','.join('?'*len(SUB_PAGE_IDS))})",
        SUB_PAGE_IDS,
    )

    # 4. Delete page_i18n for the sub-pages
    conn.execute(
        f"DELETE FROM page_i18n WHERE page_id IN ({','.join('?'*len(SUB_PAGE_IDS))})",
        SUB_PAGE_IDS,
    )

    # 5. Delete the sub-pages themselves
    conn.execute(
        f"DELETE FROM pages WHERE id IN ({','.join('?'*len(SUB_PAGE_IDS))})",
        SUB_PAGE_IDS,
    )


if __name__ == "__main__":
    run()
