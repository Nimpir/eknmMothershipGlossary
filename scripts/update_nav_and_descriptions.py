# -*- coding: utf-8 -*-
"""
scripts/update_nav_and_descriptions.py

1. P22 Character linked_pages: [P7, P10, P2, P6, P20]  (Equipment before Weapons)
2. P7  Character Creation linked_pages: [P8, P9]         (remove P10, now on P22)
3. Move C55 (Trinkets) and C56 (Patches) from P9 to P7 page_contents
4. Add descriptions to all pages that have none (P2-P4, P6-P21)

Run: python scripts/update_nav_and_descriptions.py
"""

import json
import os
import sqlite3

DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── Page descriptions (id → {lang: (name, desc)}) ────────────────────────────
# P1, P5, P22 already have descriptions — skipped here.

PAGE_DESCS = {
    2: {
        "en": ("Weapons & Damage",
               "All weapons available to the crew — firearms, melee, and special. "
               "Includes ammo types and damage ratings."),
        "ru": ("Оружие и Урон",
               "Всё оружие экипажа — огнестрельное, рукопашное и специальное. "
               "Включает типы боеприпасов и показатели урона."),
        "ua": ("Зброя та Пошкодження",
               "Вся зброя екіпажу — вогнепальна, рукопашна та спеціальна. "
               "Включає типи боєприпасів та показники пошкодження."),
    },
    3: {
        "en": ("Combat",
               "How fights work — turn order, actions, attacking, dealing damage, and using cover."),
        "ru": ("Бой",
               "Как работают бои — очерёдность ходов, действия, атаки, нанесение урона и укрытия."),
        "ua": ("Бій",
               "Як працюють бої — черговість ходів, дії, атаки, нанесення пошкодження та укриття."),
    },
    4: {
        "en": ("Wounds & Death",
               "What happens to your body — wound tables by damage type and the Death Table."),
        "ru": ("Ранения и Смерть",
               "Что происходит с вашим телом — таблицы ранений по типу урона и таблица смерти."),
        "ua": ("Поранення та Смерть",
               "Що відбувається з вашим тілом — таблиці поранень за типом пошкодження та таблиця смерті."),
    },
    6: {
        "en": ("Armour",
               "Five armour types that protect the crew — from basic crew attire to Advanced Battle Dress."),
        "ru": ("Броня",
               "Пять типов брони для защиты экипажа — от стандартной одежды до продвинутого боевого снаряжения."),
        "ua": ("Броня",
               "П'ять типів броні для захисту екіпажу — від стандартного одягу до просунутого бойового спорядження."),
    },
    7: {
        "en": ("Character Creation",
               "The 9-step process to build your character, choose a class, and roll your starting loadout."),
        "ru": ("Создание Персонажа",
               "9 шагов для создания персонажа, выбора класса и броска начального снаряжения."),
        "ua": ("Створення Персонажа",
               "9 кроків для створення персонажа, вибору класу та кидка початкового спорядження."),
    },
    8: {
        "en": ("Classes",
               "Four playable classes — Marine, Android, Scientist, and Teamster — each with unique "
               "stat bonuses and a Trauma Response."),
        "ru": ("Классы",
               "Четыре играбельных класса — Морпех, Андроид, Учёный и Рабочий — каждый с уникальными "
               "бонусами и реакцией на травму."),
        "ua": ("Класи",
               "Чотири відіграваних класи — Морпіх, Андроїд, Вчений і Робітник — кожен з унікальними "
               "бонусами та реакцією на травму."),
    },
    9: {
        "en": ("Loadouts & Tables",
               "Starting equipment loadouts rolled randomly by class."),
        "ru": ("Снаряжение и Таблицы",
               "Начальное снаряжение, случайно разыгрываемое для каждого класса."),
        "ua": ("Спорядження та Таблиці",
               "Початкове спорядження, що випадково розігрується для кожного класу."),
    },
    10: {
        "en": ("Equipment",
               "All purchasable gear, tools, and supplies available to the crew."),
        "ru": ("Снаряжение",
               "Всё покупное снаряжение, инструменты и расходники для экипажа."),
        "ua": ("Спорядження",
               "Все купівельне спорядження, інструменти та витратники для екіпажу."),
    },
    11: {
        "en": ("Core Rules",
               "The core mechanics — stat checks, saves, and advantage & disadvantage."),
        "ru": ("Основные Правила",
               "Основные механики — проверки параметров, спасброски и преимущество с помехой."),
        "ua": ("Основні Правила",
               "Основні механіки — перевірки параметрів, порятунки та перевага і перешкода."),
    },
    12: {
        "en": ("Stress & Panic",
               "How stress builds, when to roll Panic Checks, and the conditions that result from breaking down."),
        "ru": ("Стресс и Паника",
               "Как накапливается стресс, когда делать броски на панику и какие состояния возникают при срыве."),
        "ua": ("Стрес та Паніка",
               "Як накопичується стрес, коли робити кидки на паніку та які стани виникають при зриві."),
    },
    13: {
        "en": ("Skills",
               "Three tiers of skills — Trained, Expert, and Master — with prerequisite chains and training rules."),
        "ru": ("Навыки",
               "Три уровня навыков — Начальный, Экспертный и Мастерский — с цепочками требований и правилами обучения."),
        "ua": ("Навички",
               "Три рівні навичок — Початковий, Експертний та Майстерний — з ланцюжками вимог та правилами навчання."),
    },
    14: {
        "en": ("Survival",
               "Environmental hazards that threaten the crew — atmosphere, oxygen, radiation, temperature, and more."),
        "ru": ("Выживание",
               "Опасности окружающей среды — атмосфера, кислород, радиация, температура и другое."),
        "ua": ("Виживання",
               "Екологічні загрози для екіпажу — атмосфера, кисень, радіація, температура та інше."),
    },
    15: {
        "en": ("Medical Care",
               "Recovery and treatment — from short-term first aid to long-term therapy and specialized procedures."),
        "ru": ("Медицинская Помощь",
               "Восстановление и лечение — от неотложной помощи до долгосрочной терапии и специализированных процедур."),
        "ua": ("Медична Допомога",
               "Відновлення та лікування — від першої допомоги до довгострокової терапії та спеціалізованих процедур."),
    },
    16: {
        "en": ("Trained Skills",
               "The foundational skill tier — sixteen skills available to any character."),
        "ru": ("Начальные Навыки",
               "Базовый уровень навыков — шестнадцать навыков, доступных любому персонажу."),
        "ua": ("Початкові Навички",
               "Базовий рівень навичок — шістнадцять навичок, доступних будь-якому персонажу."),
    },
    17: {
        "en": ("Expert Skills",
               "Advanced skills requiring a Trained prerequisite — available after basic training."),
        "ru": ("Экспертные Навыки",
               "Продвинутые навыки, требующие базового навыка в качестве условия."),
        "ua": ("Експертні Навички",
               "Просунуті навички, що потребують базового навику як умови."),
    },
    18: {
        "en": ("Master Skills",
               "The highest tier of skills, each requiring an Expert prerequisite."),
        "ru": ("Мастерские Навыки",
               "Высший уровень навыков, каждый из которых требует экспертного навыка."),
        "ua": ("Майстерні Навички",
               "Найвищий рівень навичок, кожен з яких вимагає експертного навику."),
    },
    19: {
        "en": ("Skill Training",
               "How to train new skills between sessions and how to enlist in Military Training."),
        "ru": ("Обучение Навыкам",
               "Как осваивать новые навыки между сессиями и как записаться на военную подготовку."),
        "ua": ("Навчання Навичкам",
               "Як освоювати нові навички між сесіями та як записатися на військову підготовку."),
    },
    20: {
        "en": ("Ports & Shore Leave",
               "What happens when the crew makes port — shore leave activities, spending credits, and port classes."),
        "ru": ("Порты и Берег",
               "Что происходит, когда экипаж прибывает в порт — береговой отпуск, трата кредитов и классы портов."),
        "ua": ("Порти та Берег",
               "Що відбувається, коли екіпаж прибуває до порту — берегова відпустка, витрата кредитів та класи портів."),
    },
    21: {
        "en": ("Contractors",
               "Hiring and managing contractor NPCs — their stats, costs, and the Contractors Table."),
        "ru": ("Подрядчики",
               "Найм и управление НПС-подрядчиками — параметры, стоимость и таблица подрядчиков."),
        "ua": ("Підрядники",
               "Найм та управління НПС-підрядниками — параметри, вартість та таблиця підрядників."),
    },
}


def _seed(conn: sqlite3.Connection) -> None:
    # ── 1. P22 linked_pages: Equipment (P10) before Weapons (P2) ─────────────
    conn.execute(
        "UPDATE pages SET linked_pages=? WHERE id=22",
        (json.dumps([7, 10, 2, 6, 20]),),
    )

    # ── 2. P7 linked_pages: remove P10 ───────────────────────────────────────
    conn.execute(
        "UPDATE pages SET linked_pages=? WHERE id=7",
        (json.dumps([8, 9]),),
    )

    # ── 3. Move C55 and C56 from P9 to P7 ────────────────────────────────────
    conn.execute("DELETE FROM page_contents WHERE page_id=9 AND content_id IN (55, 56)")
    conn.execute(
        "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (7, 55, 55)"
    )
    conn.execute(
        "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (7, 56, 56)"
    )

    # ── 4. Add descriptions to pages that have none ───────────────────────────
    for page_id, langs in PAGE_DESCS.items():
        for lang, (name, desc) in langs.items():
            conn.execute("""
                UPDATE page_i18n SET desc=?
                WHERE page_id=? AND lang=? AND (desc IS NULL OR desc='')
            """, (desc, page_id, lang))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
