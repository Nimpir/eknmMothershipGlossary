"""
scripts/update_p35_add_deep_locations.py
Move C245 (Doptown) and C247 (The Choke) from P36 to P35.
Add image_url column to pages; set ProsperosDream.png on P35.
Update P35 and P36 descriptions; remove empty P36 from P31 navigation.
Run: python scripts/update_p35_add_deep_locations.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

P35_IMAGE = "images/A Pound of Flesh/ProsperosDream.png"

P35_DESCS = {
    "en": "All ten major locations of Prospero's Dream — eight station sections, Doptown, and The Choke.",
    "ru": "Все десять ключевых локаций Мечты Просперо — восемь зон станции, Доптаун и Удавка.",
    "ua": "Всі десять ключових локацій Мрії Просперо — вісім зон станції, Доптаун і Задуша.",
}

P36_DESCS = {
    "en": "Previously housed Doptown and The Choke — both now accessible from The Station (P35).",
    "ru": "Ранее содержал Доптаун и Удавку — обе локации теперь доступны через Станцию (P35).",
    "ua": "Раніше містив Доптаун і Задушу — обидві локації тепер доступні через Станцію (P35).",
}


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — C245/C247 moved to P35; P35 image set; P36 removed from P31 nav.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    # 1. Add image_url column to pages (idempotent)
    try:
        conn.execute("ALTER TABLE pages ADD COLUMN image_url TEXT")
    except Exception:
        pass  # Column already exists

    # 2. Set ProsperosDream.png on P35
    conn.execute(
        "UPDATE pages SET image_url = ? WHERE id = 35",
        (P35_IMAGE,),
    )

    # 3. Remove C245, C247 from P36
    conn.execute(
        "DELETE FROM page_contents WHERE page_id = 36 AND content_id IN (245, 247)"
    )

    # 4. Add C245, C247 to P35
    conn.execute(
        "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (35, 245, 22)"
    )
    conn.execute(
        "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (35, 247, 23)"
    )

    # 5. Update P35 descriptions
    for lang, desc in P35_DESCS.items():
        conn.execute(
            "UPDATE page_i18n SET desc = ? WHERE page_id = 35 AND lang = ?",
            (desc, lang),
        )

    # 6. Update P36 descriptions (now empty)
    for lang, desc in P36_DESCS.items():
        conn.execute(
            "UPDATE page_i18n SET desc = ? WHERE page_id = 36 AND lang = ?",
            (desc, lang),
        )

    # 7. Remove P36 from P31's linked_pages
    row = conn.execute("SELECT linked_pages FROM pages WHERE id = 31").fetchone()
    if row:
        linked = json.loads(row[0]) if row[0] else []
        linked = [pid for pid in linked if pid != 36]
        conn.execute(
            "UPDATE pages SET linked_pages = ? WHERE id = 31",
            (json.dumps(linked),),
        )


if __name__ == "__main__":
    run()
