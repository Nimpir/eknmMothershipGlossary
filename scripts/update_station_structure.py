"""
scripts/update_station_structure.py
Restructure P35 The Station: create 8 location sub-pages (P42-P49),
move each location's content items to its sub-page, and replace
P35's page_contents with linked_pages pointing to the new pages.
Run: python scripts/update_station_structure.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# New pages: (page_id, icon, en_name, ru_name, ua_name, content_ids)
LOCATION_PAGES = [
    (42, "🛸", "01 Dry Dock",               "01 Сухой Dok",                "01 Сухий Dok",                [229]),
    (43, "🍹", "02 The Stellar Burn",        "02 Звёздный Ожог",            "02 Зоряний Опік",             [230, 231]),
    (44, "🔪", "03 The Chop Shop",           "03 Мастерская",               "03 Майстерня",                [232]),
    (45, "❄️", "04 The Ice Box",             "04 Морозильник",              "04 Морозильник",              [233, 234]),
    (46, "🌿", "05 The Farm",               "05 Ферма",                    "05 Ферма",                    [235, 236]),
    (47, "🖥️", "06 CANYONHEAVY.market",     "06 CANYONHEAVY.market",       "06 CANYONHEAVY.market",       [237, 238, 239]),
    (48, "⚔️", "07 The Court",              "07 Суд",                      "07 Суд",                      [240, 241]),
    (49, "🏛️", "08 Tempest Company HQ",     "08 Штаб Tempest Company",     "08 Штаб Tempest Company",     [242, 243, 244]),
]

STATION_PAGE_ID = 35
NEW_LINKED_PAGES = [p[0] for p in LOCATION_PAGES]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — 8 location pages created (P42–P49), P35 restructured.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    # 1. Create new location pages with i18n
    for page_id, icon, en, ru, ua, _ in LOCATION_PAGES:
        conn.execute(
            "INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages) VALUES (?, ?, 'apof', 35, '[]')",
            (page_id, icon),
        )
        for lang, name in [("en", en), ("ru", ru), ("ua", ua)]:
            conn.execute(
                "INSERT OR IGNORE INTO page_i18n (page_id, lang, name) VALUES (?, ?, ?)",
                (page_id, lang, name),
            )

    # 2. Remove all existing page_contents for P35
    conn.execute("DELETE FROM page_contents WHERE page_id = ?", (STATION_PAGE_ID,))

    # 3. Add page_contents for each new location page
    for page_id, _, _, _, _, content_ids in LOCATION_PAGES:
        for sort_order, content_id in enumerate(content_ids, start=1):
            conn.execute(
                "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (?, ?, ?)",
                (page_id, content_id, sort_order),
            )

    # 4. Update P35 linked_pages
    conn.execute(
        "UPDATE pages SET linked_pages = ? WHERE id = ?",
        (json.dumps(NEW_LINKED_PAGES), STATION_PAGE_ID),
    )


if __name__ == "__main__":
    run()
