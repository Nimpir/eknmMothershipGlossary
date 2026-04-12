"""
scripts/add_corespace_generator_page.py
Restructures the Corespace Station Generator:

- Deletes C302 (plain-text generator card)
- Creates P52 "Corespace Station Generator" with intro desc and Roll All workflow
- Creates C315 Station Name, C316 Core Station, C317 Celestial Body,
  C318 Core Leader, C319 Group — each a d10 dice table on P52
- Adds P52 to P38 linked_pages

Run: python scripts/add_corespace_generator_page.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── P52 page i18n ─────────────────────────────────────────────────────────────
PAGE_52 = {
    "icon": "🌐",
    "source_slug": "apof",
    "workflow_steps": [315, 316, 317, 318, 319],
    "i18n": {
        "en": {
            "name": "Corespace Station Generator",
            "desc": (
                "[STATION NAME] is a(n) [CORE STATION] orbiting a(n) [CELESTIAL BODY]. "
                "Run by a(n) [CORE LEADER] backed by [GROUP]. "
                "Docking: 1d10×100cr. Cheap room: 2d100cr/night. "
                "5% chance station is undergoing a [CRISIS]. "
                "Markup: 2d100%. Buys [GOODS] at 1d100-10% off. "
                "Free-traders have a line on [RESOURCE]."
            ),
        },
        "ru": {
            "name": "Генератор станций Ядра",
            "desc": (
                "[НАЗВАНИЕ СТАНЦИИ] — это [ТИП СТАНЦИИ] на орбите [НЕБЕСНОГО ТЕЛА]. "
                "Управляет [ЛИДЕР ЯДРА] при поддержке [ГРУППЫ]. "
                "Стоянка: 1d10×100 кр. Дешёвый номер: 2d100 кр/ночь. "
                "5% шанс кризиса [КРИЗИС]. Наценка: 2d100%. "
                "Покупает [ТОВАР] за -1d100+10%. Свободные торговцы знают про [РЕСУРС]."
            ),
        },
        "ua": {
            "name": "Генератор станцій Ядра",
            "desc": (
                "[НАЗВА СТАНЦІЇ] — це [ТИП СТАНЦІЇ] на орбіті [НЕБЕСНОГО ТІЛА]. "
                "Керує [ЛІДЕР ЯДРА] за підтримки [ГРУПИ]. "
                "Стоянка: 1d10×100 кр. Дешевий номер: 2d100 кр/ніч. "
                "5% шанс кризи [КРИЗА]. Націнка: 2d100%. "
                "Купує [ТОВАР] за -1d100+10%. Вільні торговці знають про [РЕСУРС]."
            ),
        },
    },
}

# ── 5 dice tables (id, icon, {lang: name}, {lang: [10 entries]}) ──────────────
DICE_TABLES = [
    (
        315, "🏷️",
        {"en": "Station Name", "ru": "Название станции", "ua": "Назва станції"},
        {
            "en": [
                "Azrael's Price", "Dumah's Sorrow", "Marut's Redemption",
                "Gorgon's Revenge", "Soter's Ring", "Pontian's Crown",
                "Vitalian's Sword", "Iblis's Shield", "Al-'Uzzá's Cross",
                "Vanth's Herald",
            ],
            "ru": [
                "Цена Азраэля", "Горе Думаха", "Искупление Марута",
                "Месть Горгоны", "Кольцо Сотера", "Корона Понтиана",
                "Меч Виталиана", "Щит Иблиса", "Крест Аль-Уззы",
                "Вестник Ванта",
            ],
            "ua": [
                "Ціна Азраеля", "Горе Думаха", "Спокута Марута",
                "Помста Горгони", "Кільце Сотера", "Корона Понтіана",
                "Меч Віталіана", "Щит Ібліса", "Хрест Аль-Уззи",
                "Вісник Ванта",
            ],
        },
    ),
    (
        316, "🛰️",
        {"en": "Core Station", "ru": "Тип станции", "ua": "Тип станції"},
        {
            "en": [
                "Overcrowded Habitat Colony", "Palatial Estate",
                "Secret Corporate Research Facility", "Marine Battle School",
                "Bustling Trading Port", "Sprawling Megatropolis",
                "High Security Corporate Vault", "Semi-Autonomous Shipyard",
                "Solitary Monastery", "Ancient Jump Gate",
            ],
            "ru": [
                "Переполненная Колония-Жильё", "Роскошное Поместье",
                "Тайный Корпоративный Исследовательский Центр", "Морская Боевая Школа",
                "Оживлённый Торговый Порт", "Разросшийся Мегаполис",
                "Высокозащищённый Корпоративный Сейф", "Полуавтономная Верфь",
                "Уединённый Монастырь", "Древние Прыжковые Врата",
            ],
            "ua": [
                "Переповнена Колонія-Житло", "Розкішна Садиба",
                "Таємний Корпоративний Дослідницький Центр", "Морська Бойова Школа",
                "Жвавий Торговий Порт", "Розросле Мегамісто",
                "Сильнозахищений Корпоративний Сейф", "Напівавтономна Верф",
                "Відокремлений Монастир", "Стародавні Стрибкові Ворота",
            ],
        },
    ),
    (
        317, "⭐",
        {"en": "Celestial Body", "ru": "Небесное тело", "ua": "Небесне тіло"},
        {
            "en": [
                "Still Terraforming Planet", "Overpopulated Slumworld",
                "Resource Rich Planet", "Desolate Planetoid",
                "White Dwarf Star", "Moon of an Inhabited Planet",
                "Unpopulated Paradise World", "Giant Asteroid Cluster",
                "Red Supergiant", "Black Hole (past Event Horizon)",
            ],
            "ru": [
                "Ещё Терраформируемая Планета", "Перенаселённый Трущобный Мир",
                "Планета Богатая Ресурсами", "Безлюдный Планетоид",
                "Белый Карлик", "Спутник Обитаемой Планеты",
                "Необитаемый Рай", "Кластер Гигантских Астероидов",
                "Красный Сверхгигант", "Чёрная Дыра",
            ],
            "ua": [
                "Ще Тераформована Планета", "Перенаселений Трущобний Світ",
                "Планета Багата на Ресурси", "Безлюдний Планетоїд",
                "Білий Карлик", "Супутник Населеної Планети",
                "Ненаселений Рай", "Кластер Гігантських Астероїдів",
                "Червоний Надгігант", "Чорна Діра",
            ],
        },
    ),
    (
        318, "👤",
        {"en": "Core Leader", "ru": "Лидер Ядра", "ua": "Лідер Ядра"},
        {
            "en": [
                "First-Colony Descendant", "Asteroid Mining Oligarch",
                "Reclusive Intellectual", "Scheming Marine General",
                "Teamster Union Rep", "Sadistic Decadent",
                "Decorated Regional Governor", "Rimwar Veteran Commander",
                "Reformed Criminal Outcast", "Dynastic Child-Heir",
            ],
            "ru": [
                "Потомок Первой Колонии", "Олигарх Горнодобычи",
                "Затворник-Интеллектуал", "Интригующий Морской Генерал",
                "Представитель Профсоюза", "Садистский Декадент",
                "Заслуженный Региональный Губернатор", "Ветеран Войны на Краю",
                "Реформированный Преступник-Изгой", "Наследник Династии",
            ],
            "ua": [
                "Нащадок Першої Колонії", "Олігарх Видобувної Промисловості",
                "Відлюдник-Інтелектуал", "Підступний Морський Генерал",
                "Представник Профспілки", "Садистський Декадент",
                "Заслужений Регіональний Губернатор", "Ветеран Війни на Краю",
                "Реформований Злочинець-Вигнанець", "Спадкоємець Династії",
            ],
        },
    ),
    (
        319, "🤝",
        {"en": "Group", "ru": "Группа", "ua": "Група"},
        {
            "en": [
                "Radical Colonial Separatists", "Valecore Mining Consortium",
                "Exo-Credit Federated Union", "91st Colonial Dragoons",
                "Teamster's Local 101977L", "Yamguchi-gumi Clan",
                "Crashlander Titan 2nd Fleet", "Principality of Christian XII",
                "Decanon Caliphate", "House of Tarkhan",
            ],
            "ru": [
                "Радикальные Колониальные Сепаратисты", "Горный Консорциум Вейлкор",
                "Федеральный Союз Экзо-Кредит", "91-е Колониальные Драгуны",
                "Местный 101977L Тимстеров", "Клан Ямгучи-гуми",
                "Флот Краш-лендеров Титан 2й", "Принципат Кристиана XII",
                "Деканский Халифат", "Дом Тархан",
            ],
            "ua": [
                "Радикальні Колоніальні Сепаратисти", "Гірничодобувний Консорціум Вейлкор",
                "Федеральний Союз Екзо-Кредит", "91-й Колоніальний Драгунський",
                "Місцева 101977L Тімстерів", "Клан Ямгуті-гумі",
                "Флот Краш-лендерів Титан 2й", "Принципат Крістіана XII",
                "Деканський Халіфат", "Дім Тархан",
            ],
        },
    ),
]


def _entries(texts: list[str]) -> list[dict]:
    return [{"min": i + 1, "max": i + 1, "text": t} for i, t in enumerate(texts)]


def _seed(conn: sqlite3.Connection) -> None:
    # 1. Delete C302 (cascades content_i18n and page_contents rows)
    conn.execute("DELETE FROM contents WHERE id = 302")

    # 2. Create P52
    conn.execute(
        """INSERT OR IGNORE INTO pages (id, icon, source_slug, linked_pages, workflow_steps)
           VALUES (52, ?, ?, '[]', ?)""",
        (
            PAGE_52["icon"],
            PAGE_52["source_slug"],
            json.dumps(PAGE_52["workflow_steps"]),
        ),
    )
    # Ensure workflow_steps is set even if the row already existed
    conn.execute(
        "UPDATE pages SET workflow_steps = ? WHERE id = 52",
        (json.dumps(PAGE_52["workflow_steps"]),),
    )
    for lang, strings in PAGE_52["i18n"].items():
        conn.execute(
            """INSERT INTO page_i18n (page_id, lang, name, desc) VALUES (52, ?, ?, ?)
               ON CONFLICT (page_id, lang) DO UPDATE SET name=excluded.name, desc=excluded.desc""",
            (lang, strings["name"], strings["desc"]),
        )

    # 3. Add P52 to P38 linked_pages
    row = conn.execute("SELECT linked_pages FROM pages WHERE id = 38").fetchone()
    lp: list = json.loads(row[0]) if row and row[0] else []
    if 52 not in lp:
        lp.append(52)
        conn.execute(
            "UPDATE pages SET linked_pages = ? WHERE id = 38",
            (json.dumps(lp),),
        )

    # 4. Create C315–C319 and place on P52
    for sort, (cid, icon, names, entries_by_lang) in enumerate(DICE_TABLES, start=1):
        en_entries = _entries(entries_by_lang["en"])
        dice_json = json.dumps({"die": "d10", "entries": en_entries}, ensure_ascii=False)

        conn.execute(
            "INSERT OR IGNORE INTO contents (id, icon, dice, source_slug) VALUES (?, ?, ?, 'apof')",
            (cid, icon, dice_json),
        )
        # Ensure dice is updated if row existed
        conn.execute(
            "UPDATE contents SET icon = ?, dice = ? WHERE id = ?",
            (icon, dice_json, cid),
        )

        for lang, name in names.items():
            de_json = json.dumps(_entries(entries_by_lang[lang]), ensure_ascii=False)
            conn.execute(
                """INSERT INTO content_i18n (content_id, lang, name, dice_entries)
                   VALUES (?, ?, ?, ?)
                   ON CONFLICT (content_id, lang) DO UPDATE
                   SET name=excluded.name, dice_entries=excluded.dice_entries""",
                (cid, lang, name, de_json),
            )

        conn.execute(
            "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (52, ?, ?)",
            (cid, sort),
        )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(
            "Done — C302 deleted, P52 created with workflow, "
            "C315–C319 (Station Name, Core Station, Celestial Body, Core Leader, Group) added."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
