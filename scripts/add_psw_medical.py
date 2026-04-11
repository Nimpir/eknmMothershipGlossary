"""
scripts/add_psw_medical.py
Seed Medical Care (P15) from PSG pg 34–35.
Creates P15 under P11 with C158–C166.
Run after add_psw_survival.py: python scripts/add_psw_medical.py
"""

import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")

SOURCE_SLUG = "psg"

PAGES = [
    # (id, icon, source_page, name_en, name_ru, name_ua)
    (15, "🏥", 34, "Medical Care", "Медицинская Помощь", "Медична Допомога"),
]

CONTENTS = [
    {
        "id": 158, "icon": "🩹", "source_page": 34,
        "name": ("Short-Term Recovery", "Краткосрочное Восстановление", "Короткострокове Відновлення"),
        "desc": (
            "Once per day, whenever resting, a character's body attempts to heal itself naturally. "
            "After 6+ hours of rest make a Body Save. If successful, reset Health to its Maximum. "
            "Wounds, however, remain the same.",

            "Один раз в день, при отдыхе, тело персонажа пытается восстановиться естественным образом. "
            "После 6+ часов отдыха сделайте Спасбросок Тела. При успехе сбросьте Здоровье до максимума. "
            "Однако Раны остаются прежними.",

            "Один раз на день, під час відпочинку, тіло персонажа намагається відновитися природним чином. "
            "Після 6+ годин відпочинку зробіть Порятунок Тіла. При успіху скиньте Здоров'я до максимуму. "
            "Однак Рани залишаються незмінними.",
        ),
    },
    {
        "id": 159, "icon": "📋", "source_page": 34,
        "name": ("Long-Term Recovery", "Долгосрочное Восстановление", "Довгострокове Відновлення"),
        "desc": (
            "Recovering Wounds, Conditions, or losses to Stats and Saves takes a longer time. "
            "See the Medical Treatments table for available treatments — these require professional "
            "facilities at a Port.",

            "Восстановление Ран, Состояний или потерь Параметров и Спасбросков занимает больше времени. "
            "Смотрите таблицу Медицинских Процедур для доступных методов лечения — они требуют "
            "профессиональных учреждений в Порту.",

            "Відновлення Ран, Станів або втрат Параметрів та Порятунків займає більше часу. "
            "Дивіться таблицю Медичних Процедур для доступних методів лікування — вони вимагають "
            "професійних закладів у Порту.",
        ),
    },
    {
        "id": 160, "icon": "🤝", "source_page": 35,
        "name": (
            "Artificial Wellness Counselor",
            "Искусственный Консультант по Благополучию",
            "Штучний Консультант з Добробуту",
        ),
        "desc": (
            "1 hour session (max 1 per week). Restores 1 Sanity Save. "
            "1% chance you gain a random Condition.",

            "Сеанс 1 час (максимум 1 в неделю). Восстанавливает 1 Спасбросок Рассудка. "
            "1% шанс получить случайное Состояние.",

            "Сеанс 1 годину (максимум 1 на тиждень). Відновлює 1 Порятунок Розуму. "
            "1% шанс отримати випадковий Стан.",
        ),
        "subinfo_fixed": [{"label_key": "cost", "value": "~150cr", "type": "cost"}],
    },
    {
        "id": 161, "icon": "🧠", "source_page": 35,
        "name": (
            "Cognitive Defragmentation",
            "Когнитивная Дефрагментация",
            "Когнітивна Дефрагментація",
        ),
        "desc": (
            "24 hour surgical treatment. Removes 1 Condition. "
            "1% chance of total amnesia. [-] on Intellect Checks, Sanity Saves, and Fear Saves for 4 weeks.",

            "24-часовая хирургическая процедура. Убирает 1 Состояние. "
            "1% шанс полной амнезии. [-] на Проверки Интеллекта, Спасброски Рассудка и Страха на 4 недели.",

            "24-годинна хірургічна процедура. Прибирає 1 Стан. "
            "1% шанс повної амнезії. [-] на Перевірки Інтелекту, Порятунки Розуму та Страху на 4 тижні.",
        ),
        "subinfo_fixed": [{"label_key": "cost", "value": "100kcr", "type": "cost"}],
    },
    {
        "id": 162, "icon": "💆", "source_page": 35,
        "name": (
            "Deep Tissue Nanogel Massage",
            "Глубокотканный Наногелевый Массаж",
            "Глибокотканинний Наногелевий Масаж",
        ),
        "desc": (
            "1 hour session (max 1 per week). Reduces Minimum Stress by 1. "
            "[-] on all actions for 24 hours.",

            "Сеанс 1 час (максимум 1 в неделю). Уменьшает Минимальный Стресс на 1. "
            "[-] на все действия в течение 24 часов.",

            "Сеанс 1 годину (максимум 1 на тиждень). Зменшує Мінімальний Стрес на 1. "
            "[-] на всі дії протягом 24 годин.",
        ),
        "subinfo_fixed": [{"label_key": "cost", "value": "24kcr", "type": "cost"}],
    },
    {
        "id": 163, "icon": "🎮", "source_page": 35,
        "name": (
            "Immersive Slicksim Therapy",
            "Иммерсивная Слик-Сим Терапия",
            "Іммерсивна Слік-Сім Терапія",
        ),
        "desc": (
            "4 hour virtual treatment. Restores either 1d10 Combat or 1d10 Fear Save. "
            "1% chance the character is stuck in the immersion for 1d10 days and loses 1d5 Sanity Save.",

            "4-часовая виртуальная процедура. Восстанавливает либо 1d10 Бой, либо 1d10 Спасбросок Страха. "
            "1% шанс, что персонаж застрянет в иммерсии на 1d10 дней и потеряет 1d5 Спасброска Рассудка.",

            "4-годинна віртуальна процедура. Відновлює або 1d10 Бій, або 1d10 Порятунок Страху. "
            "1% шанс, що персонаж застрягне в іммерсії на 1d10 днів і втратить 1d5 Порятунку Розуму.",
        ),
        "subinfo_fixed": [{"label_key": "cost", "value": "1kcr", "type": "cost"}],
    },
    {
        "id": 164, "icon": "🛏️", "source_page": 35,
        "name": ("Medpod", "Медкапсула", "Медкапсула"),
        "desc": (
            "Week long treatment spent in the pod. Restores 1 Wound. "
            "Does not restore lost limbs or digits.",

            "Недельное лечение в капсуле. Восстанавливает 1 Рану. "
            "Не восстанавливает утраченные конечности или пальцы.",

            "Тижневе лікування в капсулі. Відновлює 1 Рану. "
            "Не відновлює втрачені кінцівки або пальці.",
        ),
        "subinfo_fixed": [{"label_key": "cost", "value": "6kcr", "type": "cost"}],
    },
    {
        "id": 165, "icon": "💉", "source_page": 35,
        "name": ("Pseudoflesh Injection", "Инъекция Псевдоплоти", "Ін'єкція Псевдоплоті"),
        "desc": (
            "8 hour surgical treatment. Restores either 2d10 Speed, 2d10 Strength, 2d10 Body Save, "
            "or all Wounds. At [-] on all rolls for 2 weeks, plus an additional 4 weeks of "
            "convalescent recovery required.",

            "8-часовая хирургическая операция. Восстанавливает либо 2d10 Скорость, 2d10 Силу, "
            "2d10 Спасбросок Тела, либо все Раны. [-] на все броски в течение 2 недель, плюс "
            "дополнительные 4 недели реабилитации.",

            "8-годинна хірургічна операція. Відновлює або 2d10 Швидкість, 2d10 Силу, "
            "2d10 Порятунок Тіла, або всі Рани. [-] на всі кидки протягом 2 тижнів, плюс "
            "додаткові 4 тижні реабілітації.",
        ),
        "subinfo_fixed": [{"label_key": "cost", "value": "18kcr", "type": "cost"}],
    },
    {
        "id": 166, "icon": "✂️", "source_page": 35,
        "name": ("Psychosurgery", "Психохирургия", "Психохірургія"),
        "desc": (
            "8 hour surgical treatment. Restores either Intellect, Sanity Save, or Fear Save to their "
            "maximum, or reduces Minimum Stress to 2. At [-] on all rolls for 4 weeks.",

            "8-часовая хирургическая операция. Восстанавливает Интеллект, Спасбросок Рассудка или "
            "Страха до максимума, либо снижает Минимальный Стресс до 2. [-] на все броски "
            "в течение 4 недель.",

            "8-годинна хірургічна операція. Відновлює Інтелект, Порятунок Розуму або Страху до "
            "максимуму, або зменшує Мінімальний Стрес до 2. [-] на всі кидки протягом 4 тижнів.",
        ),
        "subinfo_fixed": [{"label_key": "cost", "value": "28kcr", "type": "cost"}],
    },
]

# P15: Short-Term(158), Long-Term(159), AWC(160), CogDefrag(161), Massage(162),
#      Slicksim(163), Medpod(164), Pseudoflesh(165), Psychosurgery(166)
P15_CONTENT_ORDER = [158, 159, 160, 161, 162, 163, 164, 165, 166]


def seed(db_path: str) -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # ── Pages ─────────────────────────────────────────────────────────────────
    for pid, icon, src_pg, name_en, name_ru, name_ua in PAGES:
        cur.execute(
            "INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)"
            " VALUES (?,?,?,?,?)",
            (pid, icon, SOURCE_SLUG, src_pg, json.dumps([])),
        )
        for lang, name in [("en", name_en), ("ru", name_ru), ("ua", name_ua)]:
            cur.execute(
                "INSERT OR IGNORE INTO page_i18n (page_id, lang, name) VALUES (?,?,?)",
                (pid, lang, name),
            )

    # ── Attach P15 to P11 ─────────────────────────────────────────────────────
    cur.execute("SELECT linked_pages FROM pages WHERE id=11")
    row = cur.fetchone()
    linked = json.loads(row[0]) if row and row[0] else []
    if 15 not in linked:
        linked.append(15)
        cur.execute("UPDATE pages SET linked_pages=? WHERE id=11", (json.dumps(linked),))

    # ── Contents ──────────────────────────────────────────────────────────────
    for item in CONTENTS:
        dice_json = json.dumps(item["dice"]) if "dice" in item else None
        subinfo = json.dumps(item.get("subinfo_fixed", [])) if item.get("subinfo_fixed") else None
        cur.execute(
            "INSERT OR IGNORE INTO contents"
            " (id, icon, source_slug, source_page, dice, subinfo_fixed)"
            " VALUES (?,?,?,?,?,?)",
            (item["id"], item["icon"], SOURCE_SLUG, item["source_page"], dice_json, subinfo),
        )
        name_en, name_ru, name_ua = item["name"]
        desc_en, desc_ru, desc_ua = item["desc"]
        for lang, name, desc in [
            ("en", name_en, desc_en),
            ("ru", name_ru, desc_ru),
            ("ua", name_ua, desc_ua),
        ]:
            cur.execute(
                "INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc)"
                " VALUES (?,?,?,?)",
                (item["id"], lang, name, desc),
            )

    # ── page_contents ──────────────────────────────────────────────────────────
    cur.execute("DELETE FROM page_contents WHERE page_id=15")
    for sort_order, cid in enumerate(P15_CONTENT_ORDER):
        cur.execute(
            "INSERT INTO page_contents (page_id, content_id, sort_order) VALUES (?,?,?)",
            (15, cid, sort_order),
        )

    conn.commit()
    conn.close()
    print("Done: Medical Care (P15) + C158-C166 seeded into", repr(db_path))


if __name__ == "__main__":
    seed(DB_PATH)
