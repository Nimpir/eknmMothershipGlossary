"""
scripts/add_psw_rules.py
Seed Core Rules (P11) and Stress & Panic (P12) from PSG pg 18-21.
Creates P11 (Core Rules) linked from P1, and P12 (Stress & Panic) under P11.
Run after add_psw_equipment.py: python scripts/add_psw_rules.py
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
    (11, "📖", 18, "Core Rules",     "Основные Правила", "Основні Правила"),
    (12, "😰", 20, "Stress & Panic", "Стресс и Паника",  "Стрес та Паніка"),
]


# ── P11 content: Stat Checks, Saves, Advantage, Criticals ─────────────────────

P11_CONTENTS = [
    {
        "id": 100, "icon": "🎯", "source_page": 18,
        "name": ("Stat Checks", "Проверки Параметров", "Перевірки Параметрів"),
        "desc": (
            "Roll 1d100 and try to roll lower than your most relevant Stat. "
            "Success if you roll under your Stat. Failure: you gain 1 Stress. "
            "A roll of 90–99 is always a failure.\n\n"
            "Your four Stats:\n"
            "• Strength — holding airlocks closed, carrying fallen comrades, climbing, pushing, jumping.\n"
            "• Speed — escaping before blast doors close, acting before others, running away.\n"
            "• Intellect — recalling training under duress, thinking through difficult problems, fixing things.\n"
            "• Combat — fighting for your life.\n\n"
            "If you have a relevant Skill, add its bonus to your Stat before rolling.",

            "Бросьте 1d100 и постарайтесь выбросить меньше наиболее подходящего Параметра. "
            "Успех — если бросок меньше Параметра. Провал — получаете 1 Стресс. "
            "Результат 90–99 всегда является провалом.\n\n"
            "Четыре Параметра:\n"
            "• Сила — удерживать шлюзы, нести упавших товарищей, карабкаться, толкать, прыгать.\n"
            "• Скорость — бежать до закрытия переборок, действовать быстрее других, убегать.\n"
            "• Интеллект — вспоминать тренировки под давлением, решать сложные задачи, чинить вещи.\n"
            "• Бой — сражаться за свою жизнь.\n\n"
            "Если у вас есть подходящий Навык, прибавьте его бонус к Параметру перед броском.",

            "Киньте 1d100 і намагайтеся кинути нижче найбільш відповідного Параметра. "
            "Успіх — якщо кидок нижче Параметра. Провал — отримуєте 1 Стрес. "
            "Результат 90–99 завжди є провалом.\n\n"
            "Чотири Параметри:\n"
            "• Сила — утримувати шлюзи, нести поранених товаришів, лізти, штовхати, стрибати.\n"
            "• Швидкість — тікати до закриття переборок, діяти швидше інших, тікати.\n"
            "• Інтелект — згадувати тренування під тиском, вирішувати складні завдання, лагодити речі.\n"
            "• Бій — боротися за своє життя.\n\n"
            "Якщо у вас є відповідний Навик, додайте його бонус до Параметра перед кидком.",
        ),
    },
    {
        "id": 101, "icon": "🛟", "source_page": 18,
        "name": ("Saves", "Спасброски", "Порятунки"),
        "desc": (
            "Roll 1d100 and try to roll lower than your most relevant Save to avoid certain "
            "dangers or trauma. Success if you roll under your Save. Failure: you gain 1 Stress. "
            "A roll of 90–99 is always a failure.\n\n"
            "Your three Saves:\n"
            "• Sanity — rationalize logical inconsistencies, make sense of chaos, detect illusions and "
            "mimicry, cope with Stress.\n"
            "• Fear — maintain a level head while struggling with fear, loneliness, depression, and "
            "other emotional surges.\n"
            "• Body — employ quick reflexes and resist hunger, disease, or organisms trying to invade "
            "your insides.",

            "Бросьте 1d100 и постарайтесь выбросить меньше наиболее подходящего Спасброска, "
            "чтобы избежать определённых опасностей или травм. Успех — если бросок меньше Спасброска. "
            "Провал — получаете 1 Стресс. Результат 90–99 всегда является провалом.\n\n"
            "Три Спасброска:\n"
            "• Рассудок — рационализировать логические противоречия, разобраться в хаосе, "
            "обнаружить иллюзии и мимикрию, справляться со Стрессом.\n"
            "• Страх — сохранять хладнокровие перед лицом страха, одиночества, депрессии и "
            "других эмоциональных всплесков.\n"
            "• Тело — быстрые рефлексы и сопротивление голоду, болезням или организмам, "
            "пытающимся проникнуть внутрь.",

            "Киньте 1d100 і намагайтеся кинути нижче найбільш відповідного Порятунку, "
            "щоб уникнути певних небезпек або травм. Успіх — якщо кидок нижче Порятунку. "
            "Провал — отримуєте 1 Стрес. Результат 90–99 завжди є провалом.\n\n"
            "Три Порятунки:\n"
            "• Розум — раціоналізувати логічні суперечності, розібратися в хаосі, "
            "виявити ілюзії та мімікрію, справлятися зі Стресом.\n"
            "• Страх — зберігати холоднокровність перед обличчям страху, самотності, депресії та "
            "інших емоційних сплесків.\n"
            "• Тіло — швидкі рефлекси і опір голоду, хворобам або організмам, "
            "що намагаються проникнути всередину.",
        ),
    },
    {
        "id": 102, "icon": "⚖️", "source_page": 19,
        "name": (
            "Advantage & Disadvantage",
            "Преимущество и Помеха",
            "Перевага та Перешкода",
        ),
        "desc": (
            "Advantage [+]: Roll twice, take the better result. Granted by helpful circumstances "
            "(assistance from others, good positioning, relevant Skill, etc.).\n\n"
            "Disadvantage [-]: Roll twice, take the worse result. Imposed by poor circumstances "
            "(bad weather, poor visibility, injury, etc.).\n\n"
            "If a character has both Advantage and Disadvantage, they cancel each other out.\n\n"
            "Critical Successes & Failures: Rolling doubles (00, 11, 22 … 99) on a Stat Check or "
            "Save is a Critical. Succeeding doubles = Critical Success (something very good happens). "
            "Failing doubles = Critical Failure (something bad happens AND you must make a Panic Check). "
            "00 is always a Critical Success. 99 is always a Critical Failure.",

            "Преимущество [+]: Бросайте дважды, берите лучший результат. Предоставляется "
            "благоприятными обстоятельствами (помощь, хорошая позиция, Навык и т.д.).\n\n"
            "Помеха [-]: Бросайте дважды, берите худший результат. Накладывается "
            "неблагоприятными обстоятельствами (плохая погода, плохая видимость, травма и т.д.).\n\n"
            "Если у персонажа есть и Преимущество, и Помеха, они нейтрализуют друг друга.\n\n"
            "Критические Успехи и Провалы: Выпадение дублей (00, 11, 22 … 99) на Проверке или "
            "Спасброске — Критический результат. Успешные дубли = Критический Успех (происходит "
            "что-то очень хорошее). Провальные дубли = Критический Провал (происходит что-то плохое "
            "И необходимо совершить Проверку Паники). 00 — всегда Критический Успех. "
            "99 — всегда Критический Провал.",

            "Перевага [+]: Кидайте двічі, беріть кращий результат. Надається "
            "сприятливими обставинами (допомога, гарна позиція, Навик тощо).\n\n"
            "Перешкода [-]: Кидайте двічі, беріть гірший результат. Накладається "
            "несприятливими обставинами (погана погода, погана видимість, травма тощо).\n\n"
            "Якщо у персонажа є і Перевага, і Перешкода, вони нейтралізують одна одну.\n\n"
            "Критичні Успіхи та Провали: Випадання дублів (00, 11, 22 … 99) на Перевірці або "
            "Порятунку — Критичний результат. Успішні дубли = Критичний Успіх (відбувається "
            "щось дуже хороше). Провальні дубли = Критичний Провал (відбувається щось погане "
            "І необхідно зробити Перевірку Паніки). 00 — завжди Критичний Успіх. "
            "99 — завжди Критичний Провал.",
        ),
    },
]


# ── P12 content: Stress, Panic Table, Conditions ──────────────────────────────

STRESS = {
    "id": 103, "icon": "😤", "source_page": 20,
    "name": ("Stress", "Стресс", "Стрес"),
    "desc": (
        "Stress measures the toll the cosmos takes on a person. Higher Stress means higher "
        "chance to Panic, and more Stress when you Panic means worse results.\n\n"
        "Gaining Stress: Gain 1 Stress every time you fail a Stat Check or Save. "
        "Some locations or entities grant Stress automatically. Maximum Stress is 20; "
        "any Stress over 20 reduces the most relevant Stat or Save by that amount.\n\n"
        "Minimum Stress starts at 2 and can be raised or lowered by Panic Check results.\n\n"
        "Relieving Stress (Rest): In a relatively safe place, make a Rest Save using your "
        "worst Save. Success: reduce Stress by the ones digit of your roll "
        "(e.g., rolling 24 under Save of 30 reduces Stress by 4). Failure: gain 1 Stress. "
        "Gain Advantage on Rest Saves through consensual sex, recreational drug use, a night "
        "of heavy drinking, prayer, or other leisure activities.\n\n"
        "Relieving Stress (Shore Leave): Convert Stress into improved Saves at a Port.",

        "Стресс измеряет тяжесть последствий космоса для человека. Чем выше Стресс — "
        "тем больше шанс Паники и тем хуже её результаты.\n\n"
        "Получение Стресса: Получайте 1 Стресс каждый раз, когда проваливаете Проверку "
        "Параметра или Спасбросок. Некоторые места или существа дают Стресс автоматически. "
        "Максимальный Стресс — 20; любой Стресс сверх 20 снижает наиболее релевантный "
        "Параметр или Спасбросок на это значение.\n\n"
        "Минимальный Стресс начинается с 2 и может меняться по результатам Проверки Паники.\n\n"
        "Снятие Стресса (Отдых): В относительно безопасном месте совершите Бросок Отдыха "
        "с использованием худшего Спасброска. Успех: снизьте Стресс на цифру единиц "
        "выпавшего результата. Провал: получите 1 Стресс. Преимущество на Броске Отдыха "
        "дают секс по согласию, наркотики для отдыха, ночная пьянка, молитва и т.д.\n\n"
        "Снятие Стресса (Увольнение): Конвертируйте Стресс в улучшенные Спасброски в Порту.",

        "Стрес вимірює тягар наслідків космосу для людини. Вищий Стрес — більший шанс "
        "Паніки і гірші її результати.\n\n"
        "Отримання Стресу: Отримуйте 1 Стрес кожного разу, коли провалюєте Перевірку "
        "Параметра або Порятунок. Деякі місця або істоти дають Стрес автоматично. "
        "Максимальний Стрес — 20; будь-який Стрес понад 20 знижує найбільш релевантний "
        "Параметр або Порятунок на цю величину.\n\n"
        "Мінімальний Стрес починається з 2 і може змінюватися за результатами Перевірки Паніки.\n\n"
        "Зняття Стресу (Відпочинок): У відносно безпечному місці зробіть Кидок Відпочинку "
        "з використанням найгіршого Порятунку. Успіх: знизьте Стрес на цифру одиниць "
        "результату. Провал: отримайте 1 Стрес. Перевагу на Кидку Відпочинку дають секс за "
        "згодою, рекреаційні наркотики, нічне пияцтво, молитва тощо.\n\n"
        "Зняття Стресу (Відпустка): Конвертуйте Стрес у покращені Порятунки в Порту.",
    ),
    "subinfo": None,
    "dice": None,
}

PANIC_TABLE = {
    "id": 104, "icon": "🎲", "source_page": 21,
    "name": ("Panic Checks", "Проверки Паники", "Перевірки Паніки"),
    "desc": (
        "Roll the Panic Die (1d20) and try to roll greater than your current Stress. "
        "On failure (roll ≤ Stress), look up your result below.\n\n"
        "When to make a Panic Check: On any Critical Failure on a Stat Check or Save; "
        "watching another crewmember die; witnessing 2+ crewmembers Panic simultaneously; "
        "ship rolls a Critical Failure (all on board Panic); encountering a horrifying entity "
        "for the first time; when all hope is lost; whenever you want.",

        "Бросьте Кубик Паники (1d20) и постарайтесь выбросить больше текущего Стресса. "
        "При провале (результат ≤ Стресс) смотрите результат ниже.\n\n"
        "Когда делать Проверку Паники: при Критическом Провале Проверки или Спасброска; "
        "при гибели другого члена экипажа; при виде 2+ паникующих одновременно; "
        "при Критическом Провале корабля (паникуют все на борту); при первой встрече с "
        "ужасающей сущностью; когда всё потеряно; в любой момент по желанию.",

        "Киньте Кубик Паніки (1d20) і намагайтеся кинути більше поточного Стресу. "
        "При провалі (результат ≤ Стрес) дивіться результат нижче.\n\n"
        "Коли робити Перевірку Паніки: при Критичному Провалі Перевірки або Порятунку; "
        "при загибелі іншого члена екіпажу; при вигляді 2+ тих, хто панікує одночасно; "
        "при Критичному Провалі корабля (панікують усі на борту); при першій зустрічі з "
        "жахливою істотою; коли все втрачено; в будь-який момент за бажанням.",
    ),
    "dice": {"die": "d20", "entries": [
        {"min": 1,  "max": 1,  "text": "ADRENALINE RUSH. [+] on all rolls for 2d10 minutes. Reduce Stress by 1d5."},
        {"min": 2,  "max": 2,  "text": "NERVOUS. Gain 1 Stress."},
        {"min": 3,  "max": 3,  "text": "JUMPY. Gain 1 Stress. All Close crewmembers gain 2 Stress."},
        {"min": 4,  "max": 4,  "text": "OVERWHELMED. [-] on all rolls for 1d10 minutes. Increase Minimum Stress by 1."},
        {"min": 5,  "max": 5,  "text": "COWARD. New Condition: You must make a Fear Save to engage in violence, otherwise you flee."},
        {"min": 6,  "max": 6,  "text": "FRIGHTENED. New Condition: When encountering what frightened you, make a Fear Save [-] or gain 1d5 Stress."},
        {"min": 7,  "max": 7,  "text": "NIGHTMARES. New Condition: Sleep is difficult, gain [-] on Rest Saves."},
        {"min": 8,  "max": 8,  "text": "LOSS OF CONFIDENCE. New Condition: Choose one Skill and lose that Skill's bonus."},
        {"min": 9,  "max": 9,  "text": "DEFLATED. New Condition: Whenever a Close crewmember fails a Save, gain 1 Stress."},
        {"min": 10, "max": 10, "text": "DOOMED. New Condition: You feel cursed and unlucky. All Critical Successes are instead Critical Failures."},
        {"min": 11, "max": 11, "text": "SUSPICIOUS. For the next week, whenever someone joins the crew (even briefly), make a Fear Save or gain 1 Stress."},
        {"min": 12, "max": 12, "text": "HAUNTED. New Condition: Something starts visiting the character at night. In their dreams. Out of the corner of their eye. And soon it will start making demands."},
        {"min": 13, "max": 13, "text": "DEATH WISH. For the next 24 hours, whenever encountering a stranger or known enemy, make a Sanity Save or immediately attack them."},
        {"min": 14, "max": 14, "text": "PROPHETIC VISION. Character immediately experiences an intense hallucination or vision of an impending terror or horrific event. Increase Minimum Stress by 2."},
        {"min": 15, "max": 15, "text": "CATATONIC. Become unresponsive and unmoving for 2d10 minutes. Reduce Stress by 1d10."},
        {"min": 16, "max": 16, "text": "RAGE. [+] on all Damage rolls for 1d10 hours. All crewmembers gain 1 Stress."},
        {"min": 17, "max": 17, "text": "SPIRALING. New Condition: Panic Checks are at [-]."},
        {"min": 18, "max": 18, "text": "COMPOUNDING PROBLEMS. Roll twice on this table. Increase Minimum Stress by 1."},
        {"min": 19, "max": 19, "text": "HEART ATTACK / SHORT CIRCUIT (ANDROIDS). Reduce Maximum Wounds by 1. [-] on all rolls for 1d10 hours. Increase Minimum Stress by 1."},
        {"min": 20, "max": 20, "text": "RETIRE. Roll up a new character to play."},
    ]},
}

CONDITIONS = {
    "id": 105, "icon": "😵", "source_page": 21,
    "name": ("Conditions", "Состояния", "Стани"),
    "desc": (
        "Some Panic Table results leave a lasting impression. These are called Conditions, "
        "and they affect you until treated.\n\n"
        "Conditions from the Panic Table:\n"
        "• Coward (5) — Fear Save to engage in violence, otherwise flee.\n"
        "• Frightened (6) — Fear Save [-] or 1d5 Stress when encountering the trigger.\n"
        "• Nightmares (7) — [-] on Rest Saves.\n"
        "• Loss of Confidence (8) — One chosen Skill loses its bonus.\n"
        "• Deflated (9) — Gain 1 Stress when a Close crewmember fails a Save.\n"
        "• Doomed (10) — All Critical Successes become Critical Failures.\n"
        "• Haunted (12) — Something is watching. It will start making demands.\n"
        "• Spiraling (17) — Panic Checks at [-].\n\n"
        "Conditions require professional medical treatment to remove.",

        "Некоторые результаты Таблицы Паники оставляют глубокий след. "
        "Они называются Состояниями и действуют до получения лечения.\n\n"
        "Состояния из Таблицы Паники:\n"
        "• Трус (5) — Спасбросок Страха для участия в насилии, иначе бегство.\n"
        "• Напуган (6) — Спасбросок Страха [-] или 1d5 Стресса при встрече с триггером.\n"
        "• Кошмары (7) — [-] на Броски Отдыха.\n"
        "• Потеря уверенности (8) — Выбранный Навык теряет бонус.\n"
        "• Сломлен (9) — 1 Стресс при провале Спасброска близким товарищем.\n"
        "• Проклят (10) — Все Критические Успехи становятся Критическими Провалами.\n"
        "• Одержим (12) — Что-то наблюдает. Скоро начнёт требовать.\n"
        "• Штопор (17) — Проверки Паники с Помехой [-].\n\n"
        "Для снятия Состояния требуется профессиональная медицинская помощь.",

        "Деякі результати Таблиці Паніки залишають глибокий слід. "
        "Вони називаються Станами і діють до отримання лікування.\n\n"
        "Стани з Таблиці Паніки:\n"
        "• Боягуз (5) — Порятунок від Страху для участі у насильстві, інакше втеча.\n"
        "• Наляканий (6) — Порятунок від Страху [-] або 1d5 Стресу при зустрічі з тригером.\n"
        "• Кошмари (7) — [-] на Кидки Відпочинку.\n"
        "• Втрата впевненості (8) — Обраний Навик втрачає бонус.\n"
        "• Зламаний (9) — 1 Стрес при провалі Порятунку близьким товаришем.\n"
        "• Проклятий (10) — Усі Критичні Успіхи стають Критичними Провалами.\n"
        "• Переслідуваний (12) — Щось спостерігає. Незабаром почне вимагати.\n"
        "• Штопор (17) — Перевірки Паніки з Перешкодою [-].\n\n"
        "Для зняття Стану потрібна професійна медична допомога.",
    ),
    "subinfo": None,
    "dice": None,
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


def _seed_content(conn: sqlite3.Connection, item: dict, page_id: int) -> None:
    cid = item["id"]
    conn.execute("DELETE FROM contents WHERE id = ?", (cid,))
    conn.execute("""
        INSERT INTO contents (id, icon, source_slug, source_page, subinfo_fixed, dice, sort_order)
        VALUES (?, ?, 'psg', ?, ?, ?, ?)
    """, (cid, item["icon"], item["source_page"],
          json.dumps(item.get("subinfo")) if item.get("subinfo") else None,
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

    # Create pages P11 and P12
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

    # P12 is a sub-page of P11; P11 also links to P13 and P14 (added by their scripts)
    _add_linked_page(conn, parent_id=11, child_id=12)

    # P11 is a top-level page linked from P1
    _add_linked_page(conn, parent_id=1, child_id=11)

    # Seed P11 content
    for item in P11_CONTENTS:
        _seed_content(conn, item, page_id=11)

    # Seed P12 content
    _seed_content(conn, STRESS,       page_id=12)
    _seed_content(conn, PANIC_TABLE,  page_id=12)
    _seed_content(conn, CONDITIONS,   page_id=12)

    # Content links
    existing = {r[0] for r in conn.execute("SELECT id FROM contents")}
    links = [
        (103, 104, "related", 0),   # Stress → Panic Checks
        (104, 105, "related", 0),   # Panic Checks → Conditions
        (105, 104, "see_also", 0),  # Conditions → Panic Checks
    ]
    for from_id, to_id, label, sort in links:
        if from_id in existing and to_id in existing:
            conn.execute("""
                INSERT OR IGNORE INTO content_links
                    (from_content_id, to_content_id, label_key, sort_order)
                VALUES (?, ?, ?, ?)
            """, (from_id, to_id, label, sort))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        total = len(P11_CONTENTS) + 3
        print(f"Done — Core Rules (P11) + Stress & Panic (P12) + C100–C105 ({total} items) seeded into '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
