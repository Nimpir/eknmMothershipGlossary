"""
scripts/add_space_station_layout.py
Add C342 Space Station Layout — a d10 dice table linked from C341.
Each entry carries an "image" path used by the bot to send the layout diagram.
Run: python scripts/add_space_station_layout.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

CONTENT_ID = 342
PARENT_CONTENT_ID = 341  # Space Station Noteworthy Locations

DICE = {
    "die": "d10",
    "entries": [
        {"min":  1, "max":  1, "text": "1 establishment — self-contained ring", "image": "images/A Pound of Flesh/Space Station Layouts/1.png"},
        {"min":  2, "max":  2, "text": "2 establishments — single corridor link", "image": "images/A Pound of Flesh/Space Station Layouts/2.png"},
        {"min":  3, "max":  3, "text": "3 establishments — central hub with 2 branches", "image": "images/A Pound of Flesh/Space Station Layouts/3.png"},
        {"min":  4, "max":  4, "text": "4 establishments — cross-linked mesh", "image": "images/A Pound of Flesh/Space Station Layouts/4.png"},
        {"min":  5, "max":  5, "text": "5 establishments — hub & outer ring", "image": "images/A Pound of Flesh/Space Station Layouts/5.png"},
        {"min":  6, "max":  6, "text": "6 establishments — branching hub, two tiers", "image": "images/A Pound of Flesh/Space Station Layouts/6.png"},
        {"min":  7, "max":  7, "text": "7 establishments — tree structure", "image": "images/A Pound of Flesh/Space Station Layouts/7.png"},
        {"min":  8, "max":  8, "text": "8 establishments — dual hub with branches", "image": "images/A Pound of Flesh/Space Station Layouts/8.png"},
        {"min":  9, "max":  9, "text": "9 establishments — large hub with surrounding ring", "image": "images/A Pound of Flesh/Space Station Layouts/9.png"},
        {"min": 10, "max": 10, "text": "10 establishments — cross-linked web", "image": "images/A Pound of Flesh/Space Station Layouts/10.png"},
    ],
}

I18N = [
    ("en", "Space Station Layout",   "Roll 1d10 to determine how many Noteworthy Establishments the station has and roughly how they are connected. There may be many more establishments — these are just the most important."),
    ("ru", "Планировка Станции",     "Бросьте 1d10, чтобы определить количество Примечательных Объектов на станции и примерную схему их соединения. Объектов может быть и больше — это лишь самые важные."),
    ("ua", "Планування Станції",     "Киньте 1d10, щоб визначити кількість Визначних Закладів на станції та приблизну схему їх з'єднання. Закладів може бути більше — це лише найважливіші."),
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — C342 Space Station Layout added, linked from C341.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    # 1. Insert content row
    conn.execute(
        """INSERT OR IGNORE INTO contents (id, icon, dice, source_slug, source_page)
           VALUES (?, ?, ?, 'apof', 38)""",
        (CONTENT_ID, "🗺️", json.dumps(DICE)),
    )
    # Idempotent update in case the row already existed with stale data
    conn.execute(
        "UPDATE contents SET icon=?, dice=?, source_slug='apof', source_page=38 WHERE id=?",
        ("🗺️", json.dumps(DICE), CONTENT_ID),
    )

    # 2. Insert i18n rows for all three languages
    for lang, name, desc in I18N:
        conn.execute(
            """INSERT INTO content_i18n (content_id, lang, name, desc)
               VALUES (?, ?, ?, ?)
               ON CONFLICT(content_id, lang) DO UPDATE SET name=excluded.name, desc=excluded.desc""",
            (CONTENT_ID, lang, name, desc),
        )

    # 3. Link C341 → C342 (see_also)
    conn.execute(
        """INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key)
           VALUES (?, ?, 'see_also')""",
        (PARENT_CONTENT_ID, CONTENT_ID),
    )


if __name__ == "__main__":
    run()
