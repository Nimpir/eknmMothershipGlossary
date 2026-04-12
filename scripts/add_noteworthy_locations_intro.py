"""
scripts/add_noteworthy_locations_intro.py
Creates C341 (Space Station Noteworthy Locations intro) on P38 at sort 14,
removes C328/C334-C340 from P38 page_contents, and links C341 → all 8 tables.

Run: python scripts/add_noteworthy_locations_intro.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

C341_EN = (
    "To find out what modules and establishments are on your space station "
    "roll 1d100 for each location (for example: if you used the Space Station "
    "Layout Chart and rolled a 4 you'd roll 1d100 four times) and mark it down "
    "on your map. This creates pretty small space stations (with a maximum of "
    "ten modules), but another way to interpret this is that the modules you "
    "roll up are the major noteworthy locations on your space station. You may "
    "have any other number of small establishments but these are the ones the "
    "station is known for."
)

C341_RU = (
    "Чтобы определить модули и объекты на вашей космической станции, бросайте "
    "1d100 за каждую локацию (например: если вы использовали Таблицу Планировки "
    "Станции и выбросили 4 — бросайте 1d100 четыре раза) и отмечайте на карте. "
    "Станции получаются небольшими (не более десяти модулей), но можно "
    "воспринимать это так: выбрасываемые модули — главные примечательные места "
    "вашей станции. Любые другие мелкие объекты могут существовать, но именно "
    "эти прославили станцию."
)

C341_UA = (
    "Щоб визначити модулі та заклади вашої космічної станції, кидайте 1d100 "
    "за кожну локацію (наприклад: якщо ви використали Таблицю Планування Станції "
    "і випало 4 — кидайте 1d100 чотири рази) і позначайте на карті. Станції "
    "виходять невеликими (максимум десять модулів), але можна трактувати це так: "
    "модулі, що випали, — це головні примітні місця вашої станції. Будь-яка "
    "кількість дрібних закладів може існувати, але саме ці уславили станцію."
)

# Tables linked from C341 in display order
NOTEWORTHY_TABLE_IDS = [328, 334, 335, 336, 337, 338, 339, 340]


def _seed(conn: sqlite3.Connection) -> None:
    # 1. Create C341
    conn.execute(
        "INSERT OR IGNORE INTO contents (id, icon, source_slug) VALUES (341, '📋', 'apof')",
    )
    conn.execute("UPDATE contents SET icon='📋', dice=NULL WHERE id=341")

    for lang, name, desc in [
        ("en", "Space Station Noteworthy Locations", C341_EN),
        ("ru", "Примечательные локации станции", C341_RU),
        ("ua", "Визначні локації станції", C341_UA),
    ]:
        conn.execute(
            """INSERT INTO content_i18n (content_id, lang, name, desc)
               VALUES (341, ?, ?, ?)
               ON CONFLICT (content_id, lang)
               DO UPDATE SET name=excluded.name, desc=excluded.desc""",
            (lang, name, desc),
        )

    # 2. Place C341 on P38 at sort 14
    conn.execute(
        "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (38, 341, 14)",
    )
    conn.execute(
        "UPDATE page_contents SET sort_order=14 WHERE page_id=38 AND content_id=341",
    )

    # 3. Remove C328 and C334-C340 from P38
    placeholders = ",".join("?" * len(NOTEWORTHY_TABLE_IDS))
    conn.execute(
        f"DELETE FROM page_contents WHERE page_id=38 AND content_id IN ({placeholders})",
        NOTEWORTHY_TABLE_IDS,
    )

    # 4. Link C341 → each of the 8 tables (see_also)
    for sort, cid in enumerate(NOTEWORTHY_TABLE_IDS):
        conn.execute(
            """INSERT OR IGNORE INTO content_links
               (from_content_id, to_content_id, label_key, sort_order)
               VALUES (341, ?, 'see_also', ?)""",
            (cid, sort),
        )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(
            "Done — C341 (Space Station Noteworthy Locations) created on P38; "
            "C328/C334-C340 removed from P38; 8 content links C341->tables added."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
