"""
scripts/add_psw_skills.py
Seed Skills (P13 hub → P16 Trained / P17 Expert / P18 Master) and
Skill Training (P19) from PSG pg 22-25.
Also seeds full prerequisite DAG as content_links.
Run after add_psw_rules.py: python scripts/add_psw_skills.py
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
    (13, "🧠", 22, "Skills",          "Навыки",              "Навички"),
    (16, "📚", 22, "Trained Skills",  "Начальные Навыки",    "Початкові Навички"),
    (17, "🎓", 23, "Expert Skills",   "Экспертные Навыки",   "Експертні Навички"),
    (18, "🏆", 23, "Master Skills",   "Мастерские Навыки",   "Майстерні Навички"),
    (19, "⏳", 24, "Skill Training",  "Обучение Навыкам",    "Навчання Навичкам"),
]


# ── Trained Skills (+10, C106–C121) ───────────────────────────────────────────

TRAINED = [
    (106, "🗣️", "Linguistics",        "Лингвистика",          "Лінгвістика",
     "The study of languages (alive, dead, and undiscovered).",
     "Изучение языков (живых, мёртвых и неоткрытых).",
     "Вивчення мов (живих, мертвих та нерозкритих)."),

    (107, "🦎", "Zoology",             "Зоология",             "Зоологія",
     "The study of animal life.",
     "Изучение животной жизни.",
     "Вивчення тваринного життя."),

    (108, "🌱", "Botany",              "Ботаника",             "Ботаніка",
     "The study of plant life.",
     "Изучение растительной жизни.",
     "Вивчення рослинного життя."),

    (109, "🪨", "Geology",             "Геология",             "Геологія",
     "The study of the solid features of any terrestrial planet or its satellites.",
     "Изучение твёрдых пород любой планеты земного типа или её спутников.",
     "Вивчення твердих порід будь-якої планети земного типу або її супутників."),

    (110, "⚙️", "Industrial Equipment","Промышленное Оборудование","Промислове Обладнання",
     "The safe and proper use of heavy machinery and tools (exosuits, forklifts, drills, breakers, laser cutters, etc.).",
     "Безопасное и правильное использование тяжёлой техники и инструментов (экзоскелеты, погрузчики, дрели, отбойники, лазерные резаки и т.д.).",
     "Безпечне та правильне використання важкої техніки та інструментів (екзоскелети, навантажувачі, дрилі, відбійники, лазерні різаки тощо)."),

    (111, "🪛", "Jury-Rigging",        "Самоделки",            "Саморобки",
     "Makeshift repair using only the tools and materials at hand.",
     "Кустарный ремонт с использованием только подручных инструментов и материалов.",
     "Кустарний ремонт з використанням лише підручних інструментів і матеріалів."),

    (112, "⚗️", "Chemistry",           "Химия",                "Хімія",
     "The study of matter and its chemical elements and compounds.",
     "Изучение материи, её химических элементов и соединений.",
     "Вивчення матерії, її хімічних елементів і сполук."),

    (113, "💻", "Computers",           "Компьютеры",           "Комп'ютери",
     "Fluent use of computers and their networks.",
     "Свободное владение компьютерами и их сетями.",
     "Вільне використання комп'ютерів та їх мереж."),

    (114, "🌌", "Zero-G",              "Невесомость",          "Невагомість",
     "Practice and know-how of working in a vacuum, orientation, vaccsuit operation, etc.",
     "Практика и навыки работы в вакууме, ориентирование, использование вакуумного костюма и т.д.",
     "Практика та навички роботи у вакуумі, орієнтування, використання вакуумного костюма тощо."),

    (115, "➕", "Mathematics",          "Математика",           "Математика",
     "The study of numbers, quantity, and space.",
     "Изучение чисел, количества и пространства.",
     "Вивчення чисел, кількості та простору."),

    (116, "🎨", "Art",                 "Искусство",            "Мистецтво",
     "The expression or application of a species' creative ability and imagination.",
     "Выражение или применение творческих способностей и воображения биологического вида.",
     "Вираження або застосування творчих здібностей та уяви біологічного виду."),

    (117, "🏺", "Archaeology",         "Археология",           "Археологія",
     "Ancient cultures and artifacts.",
     "Древние культуры и артефакты.",
     "Давні культури та артефакти."),

    (118, "✝️", "Theology",            "Теология",             "Теологія",
     "The study of the divine or devotion to a religion.",
     "Изучение божественного или преданность религии.",
     "Вивчення божественного або відданість релігії."),

    (119, "🎖️", "Military Training",   "Военная Подготовка",   "Військова Підготовка",
     "Basic training provided to all military personnel.",
     "Базовая подготовка, предоставляемая всему военному персоналу.",
     "Базова підготовка, що надається всьому військовому персоналу."),

    (120, "🌃", "Rimwise",             "Окраины",              "Окраїни",
     "Practical knowledge and know-how regarding outer Rim colonies, their customs, and the seedier parts of the galaxy.",
     "Практические знания об окраинных колониях, их обычаях и более тёмных уголках галактики.",
     "Практичні знання про окраїнні колонії, їх звичаї та темніші куточки галактики."),

    (121, "🏃", "Athletics",           "Атлетика",             "Атлетика",
     "Physical fitness, sports, and games.",
     "Физическая подготовка, спорт и игры.",
     "Фізична підготовка, спорт та ігри."),
]


# ── Expert Skills (+15, C122–C136) ────────────────────────────────────────────

EXPERT = [
    (122, "🧠", "Psychology",          "Психология",           "Психологія",
     "The study of behavior and the human mind.",
     "Изучение поведения и человеческого разума.",
     "Вивчення поведінки та людського розуму."),

    (123, "🦠", "Pathology",           "Патология",            "Патологія",
     "Study of the causes and effects of diseases.",
     "Изучение причин и последствий заболеваний.",
     "Вивчення причин та наслідків захворювань."),

    (124, "🩺", "Field Medicine",      "Полевая Медицина",     "Польова Медицина",
     "Emergency medical care and treatment.",
     "Экстренная медицинская помощь и лечение.",
     "Екстрена медична допомога та лікування."),

    (125, "🌿", "Ecology",             "Экология",             "Екологія",
     "The study of organisms and how they relate to their environment.",
     "Изучение организмов и их связи с окружающей средой.",
     "Вивчення організмів та їх зв'язку з навколишнім середовищем."),

    (126, "⛏️", "Asteroid Mining",     "Добыча Астероидов",    "Видобуток Астероїдів",
     "Training in the tools and procedures used for mining asteroids.",
     "Подготовка к использованию инструментов и процедур добычи астероидов.",
     "Підготовка до використання інструментів та процедур видобутку астероїдів."),

    (127, "🔨", "Mechanical Repair",   "Механический Ремонт",  "Механічний Ремонт",
     "Fixing broken machines.",
     "Ремонт неисправных машин.",
     "Ремонт несправних машин."),

    (128, "💥", "Explosives",          "Взрывчатые Вещества",  "Вибухові Речовини",
     "Design and effective use of explosive devices (bombs, grenades, shells, land mines, etc.).",
     "Проектирование и эффективное применение взрывных устройств (бомбы, гранаты, снаряды, мины и т.д.).",
     "Проєктування та ефективне застосування вибухових пристроїв (бомби, гранати, снаряди, міни тощо)."),

    (129, "💊", "Pharmacology",        "Фармакология",         "Фармакологія",
     "Study of drugs and medication.",
     "Изучение лекарственных препаратов и медикаментов.",
     "Вивчення лікарських препаратів та медикаментів."),

    (130, "🖥️", "Hacking",             "Взлом",                "Злом",
     "Unauthorized access to computer systems and networks.",
     "Несанкционированный доступ к компьютерным системам и сетям.",
     "Несанкціонований доступ до комп'ютерних систем і мереж."),

    (131, "✈️", "Piloting",            "Пилотирование",        "Пілотування",
     "Operation and control of aircraft, spacecraft, and other vehicles.",
     "Управление и контроль самолётов, космических кораблей и других транспортных средств.",
     "Управління та контроль літаків, космічних кораблів та інших транспортних засобів."),

    (132, "⚛️", "Physics",             "Физика",               "Фізика",
     "Study of matter, motion, energy, and their effects in space and time.",
     "Изучение материи, движения, энергии и их воздействия в пространстве и времени.",
     "Вивчення матерії, руху, енергії та їх впливу в просторі та часі."),

    (133, "🔮", "Mysticism",           "Мистика",              "Містика",
     "Spiritual apprehension of hidden knowledge.",
     "Духовное постижение скрытого знания.",
     "Духовне осягнення прихованого знання."),

    (134, "🔫", "Firearms",            "Огнестрельное Оружие", "Вогнепальна Зброя",
     "Safe and effective use of guns.",
     "Безопасное и эффективное использование огнестрельного оружия.",
     "Безпечне та ефективне використання вогнепальної зброї."),

    (135, "🥊", "Hand-to-Hand Combat", "Рукопашный Бой",       "Рукопашний Бій",
     "Melee fighting, brawling, martial arts, etc.",
     "Ближний бой, драки, боевые искусства и т.д.",
     "Ближній бій, бійки, бойові мистецтва тощо."),

    (136, "🏕️", "Wilderness Survival", "Выживание в Природе",  "Виживання на Природі",
     "Applicable know-how regarding the basic necessities of life (food, water, shelter) in a natural environment.",
     "Применимые знания об основных потребностях жизни (еда, вода, укрытие) в природных условиях.",
     "Застосовувані знання про основні потреби для виживання (їжа, вода, укриття) в природних умовах."),
]


# ── Master Skills (+20, C137–C147) ────────────────────────────────────────────

MASTER = [
    (137, "👽", "Sophontology",        "Софонтология",         "Софонтологія",
     "The study of the behavior and mind of inhuman entities.",
     "Изучение поведения и разума нечеловеческих существ.",
     "Вивчення поведінки та розуму нелюдських істот."),

    (138, "🧬", "Exobiology",          "Экзобиология",         "Екзобіологія",
     "The study of and search for intelligent alien life.",
     "Изучение и поиск разумной инопланетной жизни.",
     "Вивчення та пошук розумного інопланетного життя."),

    (139, "✂️", "Surgery",             "Хирургия",             "Хірургія",
     "Manually operating on living or dead biological subjects.",
     "Ручное оперирование живых или мёртвых биологических объектов.",
     "Ручне оперування живих або мертвих біологічних об'єктів."),

    (140, "🪐", "Planetology",         "Планетология",         "Планетологія",
     "Study of planets and other celestial bodies.",
     "Изучение планет и других небесных тел.",
     "Вивчення планет та інших небесних тіл."),

    (141, "🤖", "Robotics",            "Робототехника",        "Робототехніка",
     "Design, maintenance, and operation of robots, drones, and androids.",
     "Проектирование, обслуживание и управление роботами, дронами и андроидами.",
     "Проєктування, обслуговування та управління роботами, дронами та андроїдами."),

    (142, "🏗️", "Engineering",         "Инженерия",            "Інженерія",
     "The design, building, and use of engines, machines, and structures.",
     "Проектирование, строительство и использование двигателей, машин и конструкций.",
     "Проєктування, будівництво та використання двигунів, машин і конструкцій."),

    (143, "🦿", "Cybernetics",         "Кибернетика",          "Кібернетика",
     "The physical and neural interfaces between organisms and machines.",
     "Физические и нейронные интерфейсы между организмами и машинами.",
     "Фізичні та нейронні інтерфейси між організмами та машинами."),

    (144, "🧮", "Artificial Intelligence","Искусственный Интеллект","Штучний Інтелект",
     "The study of intelligence as demonstrated by machines.",
     "Изучение интеллекта, демонстрируемого машинами.",
     "Вивчення інтелекту, що демонструється машинами."),

    (145, "🌀", "Hyperspace",          "Гиперпространство",    "Гіперпростір",
     "Faster-than-light travel.",
     "Путешествие быстрее скорости света.",
     "Подорож швидше швидкості світла."),

    (146, "🔯", "Xenoesotericism",     "Ксенотерика",          "Ксенотерика",
     "Obscure beliefs, mysticism, and religion regarding non-human entities.",
     "Малоизвестные верования, мистика и религия, касающиеся нечеловеческих существ.",
     "Маловідомі вірування, містика та релігія щодо нелюдських істот."),

    (147, "⭐", "Command",             "Командование",         "Командування",
     "Leadership, management, and authority.",
     "Лидерство, управление и авторитет.",
     "Лідерство, управління та авторитет."),
]


# ── Skill Training (C148–C149) ────────────────────────────────────────────────

TRAINING_ITEMS = [
    {
        "id": 148, "icon": "📅", "source_page": 24,
        "name": ("Train a Skill", "Обучение Навыку", "Навчання Навику"),
        "desc": (
            "To learn a new Skill you need time and credits:\n\n"
            "• Trained Skill (+10): 2 years + 10kcr in materials.\n"
            "• Expert Skill (+15): 4 years + 50kcr in materials.\n"
            "• Master Skill (+20): 6 years + 200kcr in materials.\n\n"
            "Expert Skills require one Trained Skill prerequisite. "
            "Master Skills require one Expert Skill prerequisite.\n\n"
            "Training assumes working full-time on missions and living life. "
            "Studying full-time (e.g., school) halves the time. "
            "The Warden may allow other resources (tutoring, AI assistance, cybermods) "
            "to decrease the time required.",

            "Для освоения нового Навыка необходимы время и кредиты:\n\n"
            "• Начальный Навык (+10): 2 года + 10ккр в материалах.\n"
            "• Экспертный Навык (+15): 4 года + 50ккр в материалах.\n"
            "• Мастерский Навык (+20): 6 лет + 200ккр в материалах.\n\n"
            "Для Экспертного Навыка требуется один Начальный предпосылочный Навык. "
            "Для Мастерского — один Экспертный.\n\n"
            "Обучение предполагает работу на полную ставку с миссиями. "
            "Полноценная учёба (например, в школе) вдвое сокращает время. "
            "Надзиратель может разрешить другие ресурсы (репетиторство, ИИ, кибермоды) "
            "для сокращения необходимого времени.",

            "Для освоєння нового Навику необхідні час і кредити:\n\n"
            "• Початковий Навик (+10): 2 роки + 10ккр у матеріалах.\n"
            "• Експертний Навик (+15): 4 роки + 50ккр у матеріалах.\n"
            "• Майстерний Навик (+20): 6 років + 200ккр у матеріалах.\n\n"
            "Для Експертного Навику потрібен один Початковий передумовний Навик. "
            "Для Майстерного — один Експертний.\n\n"
            "Навчання передбачає роботу на повну ставку з місіями. "
            "Повноцінне навчання (наприклад, у школі) вдвічі скорочує час. "
            "Охоронець може дозволити інші ресурси (репетиторство, ШІ, кіберзасоби) "
            "для скорочення необхідного часу.",
        ),
        "subinfo": None,
        "dice": None,
    },
    {
        "id": 149, "icon": "🎖️", "source_page": 25,
        "name": (
            "Military Training Enlistment",
            "Запись на Военную Службу",
            "Запис на Військову Службу",
        ),
        "desc": (
            "Military Training is free but requires signing a 6-year contract with the local "
            "Colonial Marine regiment. Make a Combat Check to find out what happened during service:\n\n"
            "• Success: Gain Military Training, Athletics, and 2 Trained Skills. "
            "+10 Combat, -10 to another Stat. Gain the Marine's Trauma Response.\n"
            "• Critical Success: As Success, but take an Expert Skill instead of 2 Trained Skills.\n"
            "• Failure: Gain Military Training, Athletics, and 1 Trained Skill. "
            "Gain the Marine's Trauma Response.\n"
            "• Critical Failure: You were killed in action.",

            "Военная Подготовка бесплатна, но требует подписания 6-летнего контракта с местным "
            "полком Колониальных Морских Пехотинцев. Совершите Проверку Боя, чтобы узнать, "
            "что произошло во время службы:\n\n"
            "• Успех: Получите Военную Подготовку, Атлетику и 2 Начальных Навыка. "
            "+10 к Бою, -10 к другому Параметру. Приобретите Реакцию на Травму Морпеха.\n"
            "• Критический Успех: Как Успех, но вместо 2 Начальных Навыков можно взять Экспертный.\n"
            "• Провал: Получите Военную Подготовку, Атлетику и 1 Начальный Навык. "
            "Приобретите Реакцию на Травму Морпеха.\n"
            "• Критический Провал: Убиты в бою.",

            "Військова Підготовка безкоштовна, але вимагає підписання 6-річного контракту з місцевим "
            "полком Колоніальних Морських Піхотинців. Зробіть Перевірку Бою, щоб дізнатися, "
            "що відбулося під час служби:\n\n"
            "• Успіх: Отримайте Військову Підготовку, Атлетику та 2 Початкових Навики. "
            "+10 до Бою, -10 до іншого Параметра. Отримайте Реакцію на Травму Морського Піхотинця.\n"
            "• Критичний Успіх: Як Успіх, але замість 2 Початкових Навиків можна взяти Експертний.\n"
            "• Провал: Отримайте Військову Підготовку, Атлетику та 1 Початковий Навик. "
            "Отримайте Реакцію на Травму Морського Піхотинця.\n"
            "• Критичний Провал: Загинули у бою.",
        ),
        "subinfo": None,
        "dice": None,
    },
]


# ── Prerequisite DAG: (from_id, to_id) pairs ──────────────────────────────────
# Direction: prerequisite skill → skill that requires it

PREREQ_LINKS = [
    # Trained → Expert
    (106, 122),  # Linguistics → Psychology
    (107, 122),  # Zoology → Psychology
    (107, 123),  # Zoology → Pathology
    (107, 124),  # Zoology → Field Medicine
    (108, 123),  # Botany → Pathology
    (108, 125),  # Botany → Ecology
    (108, 136),  # Botany → Wilderness Survival
    (109, 125),  # Geology → Ecology
    (109, 126),  # Geology → Asteroid Mining
    (110, 126),  # Industrial Equipment → Asteroid Mining
    (110, 127),  # Industrial Equipment → Mechanical Repair
    (111, 127),  # Jury-Rigging → Mechanical Repair
    (111, 128),  # Jury-Rigging → Explosives
    (112, 128),  # Chemistry → Explosives
    (112, 129),  # Chemistry → Pharmacology
    (113, 130),  # Computers → Hacking
    (114, 131),  # Zero-G → Piloting
    (115, 132),  # Mathematics → Physics
    (116, 133),  # Art → Mysticism
    (117, 133),  # Archaeology → Mysticism
    (118, 133),  # Theology → Mysticism
    (119, 128),  # Military Training → Explosives
    (119, 134),  # Military Training → Firearms
    (119, 135),  # Military Training → Hand-to-Hand Combat
    (120, 134),  # Rimwise → Firearms
    (120, 135),  # Rimwise → Hand-to-Hand Combat
    (121, 135),  # Athletics → Hand-to-Hand Combat

    # Expert → Master
    (122, 137),  # Psychology → Sophontology
    (123, 138),  # Pathology → Exobiology
    (123, 139),  # Pathology → Surgery
    (124, 139),  # Field Medicine → Surgery
    (125, 140),  # Ecology → Planetology
    (126, 140),  # Asteroid Mining → Planetology
    (127, 141),  # Mechanical Repair → Robotics
    (127, 142),  # Mechanical Repair → Engineering
    (127, 143),  # Mechanical Repair → Cybernetics
    (130, 144),  # Hacking → Artificial Intelligence
    (131, 145),  # Piloting → Hyperspace
    (131, 147),  # Piloting → Command
    (132, 145),  # Physics → Hyperspace
    (133, 145),  # Mysticism → Hyperspace
    (133, 146),  # Mysticism → Xenoesotericism
    (134, 147),  # Firearms → Command
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


def _seed_skill(conn: sqlite3.Connection, row: tuple, page_id: int, tier: str, bonus: str) -> None:
    cid, icon, name_en, name_ru, name_ua, desc_en, desc_ru, desc_ua = row
    conn.execute("DELETE FROM contents WHERE id = ?", (cid,))
    subinfo = json.dumps([{"label_key": "tier", "value": f"{tier} {bonus}", "type": "stat"}])
    conn.execute("""
        INSERT INTO contents (id, icon, source_slug, source_page, subinfo_fixed, sort_order)
        VALUES (?, ?, 'psg', 22, ?, ?)
    """, (cid, icon, subinfo, cid))
    for lang, name, desc in [
        ("en", name_en, desc_en),
        ("ru", name_ru, desc_ru),
        ("ua", name_ua, desc_ua),
    ]:
        conn.execute("""
            INSERT INTO content_i18n (content_id, lang, name, desc, subinfo_text)
            VALUES (?, ?, ?, ?, NULL)
        """, (cid, lang, name, desc))
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (?, ?, ?)
    """, (page_id, cid, cid))


def _seed_content(conn: sqlite3.Connection, item: dict, page_id: int) -> None:
    cid = item["id"]
    conn.execute("DELETE FROM contents WHERE id = ?", (cid,))
    conn.execute("""
        INSERT INTO contents (id, icon, source_slug, source_page, subinfo_fixed, dice, sort_order)
        VALUES (?, ?, 'psg', ?, ?, ?, ?)
    """, (cid, item["icon"], item["source_page"],
          json.dumps(item["subinfo"]) if item.get("subinfo") else None,
          json.dumps(item["dice"]) if item.get("dice") else None,
          cid))
    for lang, name, desc in zip(("en", "ru", "ua"), item["name"], item["desc"]):
        conn.execute("""
            INSERT INTO content_i18n (content_id, lang, name, desc, subinfo_text)
            VALUES (?, ?, ?, ?, NULL)
        """, (cid, lang, name, desc))
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (?, ?, ?)
    """, (page_id, cid, cid))


# ── Seed ──────────────────────────────────────────────────────────────────────

def _seed(conn: sqlite3.Connection) -> None:
    conn.execute("""
        INSERT OR IGNORE INTO sources (id, slug, title, type)
        VALUES (1, 'psg', 'Player''s Survival Guide', 'core')
    """)

    # Create pages P13, P16, P17, P18, P19
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

    # P13 (Skills hub) links to P16, P17, P18, P19
    for child in (16, 17, 18, 19):
        _add_linked_page(conn, parent_id=13, child_id=child)

    # P11 (Core Rules) links to P13
    _add_linked_page(conn, parent_id=11, child_id=13)

    # Seed skills
    for row in TRAINED:
        _seed_skill(conn, row, page_id=16, tier="Trained", bonus="+10")
    for row in EXPERT:
        _seed_skill(conn, row, page_id=17, tier="Expert", bonus="+15")
    for row in MASTER:
        _seed_skill(conn, row, page_id=18, tier="Master", bonus="+20")

    # Seed skill training items
    for item in TRAINING_ITEMS:
        _seed_content(conn, item, page_id=19)

    # Seed prerequisite content_links
    all_ids = {r[0] for r in conn.execute("SELECT id FROM contents")}
    for sort, (from_id, to_id) in enumerate(PREREQ_LINKS):
        if from_id in all_ids and to_id in all_ids:
            conn.execute("""
                INSERT OR IGNORE INTO content_links
                    (from_content_id, to_content_id, label_key, sort_order)
                VALUES (?, ?, 'prerequisite', ?)
            """, (from_id, to_id, sort))

    # Also link Skill Training items to each other
    conn.execute("""
        INSERT OR IGNORE INTO content_links
            (from_content_id, to_content_id, label_key, sort_order)
        VALUES (148, 149, 'see_also', 0)
    """)


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        total_skills = len(TRAINED) + len(EXPERT) + len(MASTER)
        print(
            f"Done — Skills (P13, P16, P17, P18) + Skill Training (P19) + "
            f"C106–C149 ({total_skills + len(TRAINING_ITEMS)} items, "
            f"{len(PREREQ_LINKS)} prerequisite links) seeded into '{DB_PATH}'."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
