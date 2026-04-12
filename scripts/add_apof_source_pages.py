"""
scripts/add_apof_source_pages.py
A Pound of Flesh — source record, pages P31-P40, and nav wiring update.
Creates P41 (Modules) if absent, links P31 under P41, and links P41 to P1.
Run first before any other add_apof_*.py scripts.
Run: python scripts/add_apof_source_pages.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── Source ─────────────────────────────────────────────────────────────────────
SOURCE = (3, "apof", "A Pound of Flesh", "module")

# ── Pages ──────────────────────────────────────────────────────────────────────
# (id, icon, source_slug, source_page, linked_pages_json,
#  name_en, name_ru, name_ua,
#  desc_en, desc_ru, desc_ua)
PAGES = [
    (
        31, "🏙️", "apof", None, json.dumps([32, 33, 34, 35, 37, 38]),
        "A Pound of Flesh",
        "Фунт плоти",
        "Фунт плоті",
        "Prospero's Dream — a massive space station teeming with crime, corruption, and cosmic horror.",
        "Мечта Просперо — огромная космическая станция, кишащая преступностью, коррупцией и космическим ужасом.",
        "Мрія Просперо — величезна космічна станція, що кишить злочинністю, корупцією та космічним жахом.",
    ),
    (
        32, "ℹ️", "apof", 4, json.dumps([]),
        "The Dream",
        "Мечта",
        "Мрія",
        "Station overview, how to board, laws, fees, and the ACMD infection rules.",
        "Обзор станции, правила посадки, законы, сборы и правила заражения ACMD.",
        "Огляд станції, правила посадки, закони, збори та правила зараження ACMD.",
    ),
    (
        33, "👥", "apof", 8, json.dumps([]),
        "Power Brokers",
        "Власть имущие",
        "Владні особи",
        "The six major NPCs who run Prospero's Dream — stats, jobs, and where to find them.",
        "Шесть ключевых персонажей, управляющих Мечтой Просперо — характеристики, задания и местонахождение.",
        "Шість ключових персонажів, що керують Мрією Просперо — характеристики, завдання та місцезнаходження.",
    ),
    (
        34, "📊", "apof", 6, json.dumps([]),
        "Storylines",
        "Сюжетные линии",
        "Сюжетні лінії",
        "Three escalating crises — the Teamster Strike, Unrest in The Choke, and the ACMD Outbreak.",
        "Три нарастающих кризиса — забастовка Тимстеров, Восстание в Удавке и вспышка ACMD.",
        "Три кризи, що наростають — страйк Тімстерів, Заворушення в Задусі та спалах ACMD.",
    ),
    (
        35, "🏢", "apof", 10, json.dumps([]),
        "The Station",
        "Станция",
        "Станція",
        "All ten major locations of Prospero's Dream — eight station sections, Doptown, and The Choke.",
        "Все десять ключевых локаций Мечты Просперо — восемь зон станции, Доптаун и Удавка.",
        "Всі десять ключових локацій Мрії Просперо — вісім зон станції, Доптаун і Задуша.",
    ),
    (
        36, "☠️", "apof", 30, json.dumps([]),
        "The Deep",
        "Глубина",
        "Глибина",
        "Previously housed Doptown and The Choke — both now accessible from The Station (P35).",
        "Ранее содержал Доптаун и Удавку — обе локации теперь доступны через Станцию (P35).",
        "Раніше містив Доптаун і Задушу — обидві локації тепер доступні через Станцію (P35).",
    ),
    (
        37, "🔧", "apof", 16, json.dumps([39, 40]),
        "Cybermods",
        "Киберимпланты",
        "Кіберімпланти",
        "Installation rules, malfunctions, overclocking, reaping, and the full cyberware and slickware lists.",
        "Правила установки, неисправности, разгон, извлечение и полные списки киберимплантов и слик-ПО.",
        "Правила встановлення, несправності, оверклокінг, вилучення та повні списки кіберімплантів і слік-ПЗ.",
    ),
    (
        38, "🎲", "apof", 40, json.dumps([]),
        "Tables",
        "Таблицы",
        "Таблиці",
        "Random encounter tables, establishments, denizens, and space station generators.",
        "Таблицы случайных встреч, заведений, жителей и генераторы космических станций.",
        "Таблиці випадкових зустрічей, закладів, мешканців та генератори космічних станцій.",
    ),
    (
        39, "🦾", "apof", 18, json.dumps([]),
        "Cyberware",
        "Кибернетика",
        "Кібернетика",
        "Hardware cybermods — physical implants that augment the body.",
        "Аппаратные киберимпланты — физические имплантаты для улучшения тела.",
        "Апаратні кіберімпланти — фізичні імплантати для покращення тіла.",
    ),
    (
        40, "💻", "apof", 21, json.dumps([]),
        "Slickware",
        "Слик-ПО",
        "Слік-ПЗ",
        "Software cybermods installed in the brain via a Slicksocket.",
        "Программные киберимпланты, устанавливаемые в мозг через разъём Слика.",
        "Програмні кіберімпланти, що встановлюються в мозок через роз'єм Сліка.",
    ),
]


def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


def _seed(conn: sqlite3.Connection) -> None:
    # Source
    sid, slug, title, stype = SOURCE
    conn.execute(
        "INSERT OR IGNORE INTO sources (id, slug, title, type) VALUES (?,?,?,?)",
        (sid, slug, title, stype),
    )

    for (pid, icon, src_slug, src_page, linked_pages,
         name_en, name_ru, name_ua,
         desc_en, desc_ru, desc_ua) in PAGES:

        conn.execute("""
            INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
            VALUES (?, ?, ?, ?, ?)
        """, (pid, icon, src_slug, src_page, linked_pages))

        for lang, name, desc in [
            ("en", name_en, desc_en),
            ("ru", name_ru, desc_ru),
            ("ua", name_ua, desc_ua),
        ]:
            conn.execute("""
                INSERT OR IGNORE INTO page_i18n (page_id, lang, name, desc)
                VALUES (?, ?, ?, ?)
            """, (pid, lang, name, desc))

    # Ensure P41 (Modules) exists and wire nav: P1 → P41 → P31
    conn.execute(
        """
        INSERT INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (41, '📦', NULL, NULL, json('[]'))
        ON CONFLICT(id) DO NOTHING
        """
    )
    for lang, name in [("en", "Modules"), ("ru", "Модули"), ("ua", "Модулі")]:
        conn.execute(
            """
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
            VALUES (41, ?, ?)
            """,
            (lang, name),
        )
    _add_linked_page(conn, parent_id=41, child_id=31)
    _add_linked_page(conn, parent_id=1, child_id=41)

    # Set P35 overview image (idempotent UPDATE — safe to re-run)
    try:
        conn.execute("ALTER TABLE pages ADD COLUMN image_url TEXT")
    except Exception:
        pass  # Column already exists
    conn.execute(
        "UPDATE pages SET image_url = 'images/A Pound of Flesh/ProsperosDream.png' WHERE id = 35"
    )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — 1 source, {len(PAGES)} pages added; P41 (Modules) ensured, P31 linked under P41, P41 linked to P1.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
