"""
scripts/add_psw_character.py
Seed Character Creation overview (P7) and Classes (P8) from the PSG.
Run after schema init: python scripts/add_psw_character.py
"""

import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── Pages ─────────────────────────────────────────────────────────────────────

PAGES = [
    # (id, icon, source_page, name_en, name_ru, name_ua)
    (7,  "📋", 4,  "Character Creation", "Создание Персонажа",  "Створення Персонажа"),
    (8,  "🎭", 5,  "Classes",            "Классы",              "Класи"),
]

# ── C46: Character Creation Steps ─────────────────────────────────────────────

CHAR_CREATION = {
    "id": 46, "page": 7, "icon": "📝", "source_page": 4,
    "name": (
        "Character Creation",
        "Создание Персонажа",
        "Створення Персонажа",
    ),
    "desc": (
        "9 steps to build your character:\n\n"
        "1. Roll 2d10+25 for each Stat: Strength, Speed, Intellect, Combat.\n"
        "2. Roll 2d10+10 for each Save: Sanity, Fear, Body.\n"
        "3. Select your Class and apply its Stat/Save adjustments.\n"
        "4. Roll 1d10+10 for Maximum Health. Start at max with 0 Wounds.\n"
        "5. Gain Stress — Current and Minimum both start at 2.\n"
        "6. Note your class's Trauma Response.\n"
        "7. Note class skills and choose bonus skills.\n"
        "8. Roll for Equipment Loadout (pg 7), Trinket (pg 8), and Patch (pg 9).\n"
        "9. Write your name and pronouns. Mark zero above High Score.\n\n"
        "Starting Credits: 2d10×10cr. (Forgo loadout for 2d10×100cr instead.)",

        "9 шагов создания персонажа:\n\n"
        "1. Бросьте 2d10+25 для каждого Параметра: Сила, Скорость, Интеллект, Бой.\n"
        "2. Бросьте 2d10+10 для каждого Спасброска: Рассудок, Страх, Тело.\n"
        "3. Выберите Класс и примените изменения к Параметрам/Спасброскам.\n"
        "4. Бросьте 1d10+10 для Максимального Здоровья. Начинайте с максимума и 0 Ранений.\n"
        "5. Получите Стресс — Текущий и Минимальный начинаются с 2.\n"
        "6. Запишите Реакцию на Травму своего класса.\n"
        "7. Запишите навыки класса и выберите бонусные навыки.\n"
        "8. Бросьте на Снаряжение (стр. 7), Безделушку (стр. 8) и Нашивку (стр. 9).\n"
        "9. Запишите имя и местоимения. Отметьте ноль над Рекордом.\n\n"
        "Начальные Кредиты: 2d10×10кр. (Или откажитесь от снаряжения для 2d10×100кр.)",

        "9 кроків створення персонажа:\n\n"
        "1. Киньте 2d10+25 для кожного Параметра: Сила, Швидкість, Інтелект, Бій.\n"
        "2. Киньте 2d10+10 для кожного Порятунку: Розум, Страх, Тіло.\n"
        "3. Оберіть Клас та застосуйте зміни до Параметрів/Порятунків.\n"
        "4. Киньте 1d10+10 для Максимального Здоров'я. Починайте з максимуму і 0 Поранень.\n"
        "5. Отримайте Стрес — Поточний і Мінімальний починаються з 2.\n"
        "6. Запишіть Реакцію на Травму свого класу.\n"
        "7. Запишіть навички класу та оберіть бонусні навички.\n"
        "8. Киньте на Спорядження (стор. 7), Дрібничку (стор. 8) та Нашивку (стор. 9).\n"
        "9. Запишіть ім'я та займенники. Відмітьте нуль над Рекордом.\n\n"
        "Початкові Кредити: 2d10×10кр. (Або відмовтеся від спорядження для 2d10×100кр.)",
    ),
    "subinfo": None,
}

# ── C47–C50: Classes ───────────────────────────────────────────────────────────

CLASSES = [
    {
        "id": 47, "page": 8, "icon": "🪖", "source_page": 5,
        "name": ("Marine", "Морской Пехотинец", "Морський Піхотинець"),
        "subinfo": [
            {"label_key": "combat",    "value": "+10 Combat",    "type": "stat"},
            {"label_key": "body_save", "value": "+10 Body Save", "type": "stat"},
            {"label_key": "fear_save", "value": "+20 Fear Save", "type": "stat"},
            {"label_key": "wounds",    "value": "+1 Max Wounds", "type": "stat"},
        ],
        "desc": (
            "Handy in a fight, but whenever they Panic it may cause problems for the rest of the crew.\n\n"
            "Trauma Response: Whenever you Panic, every Close friendly player must make a Fear Save.\n\n"
            "Starting skills: Military Training, Athletics\n"
            "Bonus: 1 Expert Skill OR 2 Trained Skills",

            "Умелый боец, но когда они Паникуют, это может создать проблемы для всего экипажа.\n\n"
            "Реакция на Травму: Когда вы Паникуете, каждый ближайший дружественный игрок "
            "обязан совершить Спасбросок Страха.\n\n"
            "Начальные навыки: Военная Подготовка, Атлетика\n"
            "Бонус: 1 Экспертный Навык ИЛИ 2 Начальных Навыка",

            "Умілий у бою, але коли вони Панікують, це може створити проблеми для решти екіпажу.\n\n"
            "Реакція на Травму: Коли ви Панікуєте, кожен близький дружній гравець "
            "зобов'язаний зробити Порятунок від Страху.\n\n"
            "Початкові навички: Військова Підготовка, Атлетика\n"
            "Бонус: 1 Експертний Навик АБО 2 Початкових Навики",
        ),
    },
    {
        "id": 48, "page": 8, "icon": "🤖", "source_page": 5,
        "name": ("Android", "Андроид", "Андроїд"),
        "subinfo": [
            {"label_key": "intellect", "value": "+20 Intellect",  "type": "stat"},
            {"label_key": "any_stat",  "value": "-10 to 1 Stat",  "type": "stat"},
            {"label_key": "fear_save", "value": "+60 Fear Save",  "type": "stat"},
            {"label_key": "wounds",    "value": "+1 Max Wounds",  "type": "stat"},
        ],
        "desc": (
            "A terrifying and exciting addition to any crew. They tend to unnerve other "
            "crewmembers with their cold inhumanity.\n\n"
            "Trauma Response: Fear Saves made by Close friendly players are at Disadvantage.\n\n"
            "Starting skills: Linguistics, Computers, Mathematics\n"
            "Bonus: 1 Expert Skill OR 2 Trained Skills",

            "Пугающее и захватывающее дополнение к любому экипажу. Своей холодной "
            "бесчеловечностью они вызывают дискомфорт у других членов экипажа.\n\n"
            "Реакция на Травму: Спасброски Страха ближайших дружественных игроков "
            "совершаются с Помехой.\n\n"
            "Начальные навыки: Лингвистика, Компьютеры, Математика\n"
            "Бонус: 1 Экспертный Навык ИЛИ 2 Начальных Навыка",

            "Лякаюче й захопливе доповнення до будь-якого екіпажу. Своєю холодною "
            "нелюдяністю вони викликають дискомфорт у інших членів екіпажу.\n\n"
            "Реакція на Травму: Порятунки від Страху близьких дружніх гравців "
            "здійснюються з Перешкодою.\n\n"
            "Початкові навички: Лінгвістика, Комп'ютери, Математика\n"
            "Бонус: 1 Експертний Навик АБО 2 Початкових Навики",
        ),
    },
    {
        "id": 49, "page": 8, "icon": "🔬", "source_page": 5,
        "name": ("Scientist", "Учёный", "Вчений"),
        "subinfo": [
            {"label_key": "intellect",   "value": "+10 Intellect",  "type": "stat"},
            {"label_key": "any_stat",    "value": "+5 to 1 Stat",   "type": "stat"},
            {"label_key": "sanity_save", "value": "+30 Sanity Save","type": "stat"},
        ],
        "desc": (
            "Doctors, researchers, or anyone who wants to slice open creatures "
            "(or infected crewmembers) with a scalpel.\n\n"
            "Trauma Response: Whenever you fail a Sanity Save, all Close friendly players gain 1 Stress.\n\n"
            "Starting skills: 1 Master Skill, plus its Expert and Trained prerequisites\n"
            "Bonus: 1 Trained Skill",

            "Врачи, исследователи или все, кто хочет вскрывать скальпелем существ "
            "(или заражённых членов экипажа).\n\n"
            "Реакция на Травму: Когда вы проваливаете Спасбросок Рассудка, "
            "все ближайшие дружественные игроки получают 1 Стресс.\n\n"
            "Начальные навыки: 1 Мастерский Навык, плюс необходимые Экспертный и Начальный\n"
            "Бонус: 1 Начальный Навык",

            "Лікарі, дослідники або всі, хто хоче розрізати скальпелем істот "
            "(або заражених членів екіпажу).\n\n"
            "Реакція на Травму: Коли ви провалюєте Порятунок Розуму, "
            "всі близькі дружні гравці отримують 1 Стрес.\n\n"
            "Початкові навички: 1 Майстерний Навик, плюс необхідні Експертний і Початковий\n"
            "Бонус: 1 Початковий Навик",
        ),
    },
    {
        "id": 50, "page": 8, "icon": "🔧", "source_page": 5,
        "name": ("Teamster", "Рабочий", "Робітник"),
        "subinfo": [
            {"label_key": "all_stats", "value": "+5 to all Stats", "type": "stat"},
            {"label_key": "all_saves", "value": "+10 to all Saves","type": "stat"},
        ],
        "desc": (
            "Rough and tumble blue-collar space workers: mechanics, engineers, miners, and pilots.\n\n"
            "Trauma Response: Once per session, you may take Advantage on a Panic Check.\n\n"
            "Starting skills: Industrial Equipment, Zero-G\n"
            "Bonus: 1 Trained Skill and 1 Expert Skill",

            "Грубоватые синие воротнички: механики, инженеры, шахтёры и пилоты.\n\n"
            "Реакция на Травму: Один раз за сессию вы можете совершить Проверку Паники "
            "с Преимуществом.\n\n"
            "Начальные навыки: Промышленное Оборудование, Невесомость\n"
            "Бонус: 1 Начальный Навык и 1 Экспертный Навык",

            "Грубуваті робітники: механіки, інженери, шахтарі та пілоти.\n\n"
            "Реакція на Травму: Один раз за сесію ви можете здійснити Перевірку Паніки "
            "з Перевагою.\n\n"
            "Початкові навички: Промислове Обладнання, Невагомість\n"
            "Бонус: 1 Початковий Навик і 1 Експертний Навик",
        ),
    },
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


# ── Seed ──────────────────────────────────────────────────────────────────────

def _seed(conn: sqlite3.Connection) -> None:
    conn.execute("""
        INSERT OR IGNORE INTO sources (id, slug, title, type)
        VALUES (1, 'psg', 'Player''s Survival Guide', 'core')
    """)

    # Create pages P7 and P8
    for (pid, icon, src_page, name_en, name_ru, name_ua) in PAGES:
        conn.execute("""
            INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
            VALUES (?, ?, 'psg', ?, '[]')
        """, (pid, icon, src_page))
        for lang, name in [("en", name_en), ("ru", name_ru), ("ua", name_ua)]:
            conn.execute("""
                INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
                VALUES (?, ?, ?)
            """, (pid, lang, name))

    # P7 linked_pages: [P8, P9, P10] — P9 and P10 added by their own scripts
    _add_linked_page(conn, parent_id=7, child_id=8)

    # Add P7 to P1's linked_pages
    _add_linked_page(conn, parent_id=1, child_id=7)

    # ── C46: Character Creation Steps ─────────────────────────────────────────
    conn.execute("DELETE FROM contents WHERE id = 46")
    conn.execute("""
        INSERT INTO contents (id, icon, source_slug, source_page, subinfo_fixed, sort_order)
        VALUES (46, '📝', 'psg', 4, NULL, 46)
    """)
    for lang, name, desc in zip(
        ("en", "ru", "ua"),
        CHAR_CREATION["name"],
        CHAR_CREATION["desc"],
    ):
        conn.execute("""
            INSERT INTO content_i18n (content_id, lang, name, desc, subinfo_text)
            VALUES (46, ?, ?, ?, NULL)
        """, (lang, name, desc))
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (7, 46, 46)
    """)

    # ── C47–C50: Classes ──────────────────────────────────────────────────────
    for cls in CLASSES:
        cid = cls["id"]
        conn.execute("DELETE FROM contents WHERE id = ?", (cid,))
        conn.execute("""
            INSERT INTO contents (id, icon, source_slug, source_page, subinfo_fixed, sort_order)
            VALUES (?, ?, 'psg', ?, ?, ?)
        """, (cid, cls["icon"], cls["source_page"],
              json.dumps(cls["subinfo"]), cid))
        for lang, name, desc in zip(("en", "ru", "ua"), cls["name"], cls["desc"]):
            conn.execute("""
                INSERT INTO content_i18n (content_id, lang, name, desc, subinfo_text)
                VALUES (?, ?, ?, ?, NULL)
            """, (cid, lang, name, desc))
        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (?, ?, ?)
        """, (cls["page"], cid, cid))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — Character Creation (P7, P8) + C46–C50 seeded into '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
