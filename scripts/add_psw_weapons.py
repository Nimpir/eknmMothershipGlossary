"""
scripts/add_psw_weapons.py
Seed Weapons & Damage from the Player's Survival Guide quick-reference table.
Run after add_psw_combat.py (range/wound content IDs C31-C40 must exist for related links).
Run: python scripts/add_psw_weapons.py
"""

import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── Range → content-item ID (C37–C40, seeded by add_psw_combat.py) ───────────
RANGE_CONTENT: dict[str, int] = {
    "Adjacent": 37,
    "Close":    38,
    "Long":     39,
    "Extreme":  40,
}

# ── Wound key → content-item ID(s) (C31–C35, seeded by add_psw_combat.py) ────
WOUND_CONTENT: dict[str, list[int]] = {
    "Gore [+]":                 [35],
    "Gunshot":                  [33],
    "Gunshot [+]":              [33],
    "Blunt Force":              [31],
    "Blunt Force [+]":          [31],
    "Fire/Explosives":          [34],
    "Fire/Explosives [+]":      [34],
    "Fire/Explosives [-]":      [34],
    "Bleeding":                 [32],
    "Bleeding [+]":             [32],
    "Bleeding [+] or Gore [+]": [32, 35],
    "Bleeding + Gore":          [32, 35],
}

# ── Weapon data ───────────────────────────────────────────────────────────────
# Each entry: (id, icon, cost, range_key, damage, shots, wound_key,
#              name_en, name_ru, name_ua,
#              special_en, special_ru, special_ua)
# special = None → rendered as "—" in all languages
WEAPONS = [
    (1, "🔫", "50cr",     "N/A",      "—",                          "N/A", "N/A",
     "Ammo",                        "Патроны",                        "Набої",
     "Per magazine/container.",
     "За магазин/контейнер.",
     "За магазин/контейнер."),

    (2, "⚔️", "150cr",    "Adjacent", "2d10 DMG",                   "N/A", "Gore [+]",
     "Boarding Axe",                "Абордажный Топор",               "Абордажна Сокира",
     None, None, None),

    (3, "🔫", "1,400cr",  "Close",    "4d10 DMG",                   "4",   "Gunshot",
     "Combat Shotgun",              "Боевой Дробовик",                "Бойовий Дробовик",
     "1d10 DMG at Long Range or greater.",
     "1d10 урона на Дальней дистанции и дальше.",
     "1d10 шкоди на Далекій дистанції і далі."),

    (4, "🔧", "25cr",     "Adjacent", "1d5 DMG",                    "N/A", "Blunt Force [+]",
     "Crowbar",                     "Монтировка",                     "Монтажний Лом",
     "Grants [+] on Strength Checks to open jammed airlocks, lift heavy objects, etc.",
     "Даёт [+] на Проверки Силы для вскрытия заклинивших шлюзов, подъёма тяжёлых предметов и т.д.",
     "Дає [+] на Перевірки Сили для відкривання заклинених шлюзів, підняття важких предметів тощо."),

    (5, "🔫", "4kcr",     "Close",    "2d10 DMG",                   "4",   "Fire/Explosives [+]",
     "Flamethrower",                "Огнемёт",                        "Вогнемет",
     "Body Save [-] or be set on fire (2d10 DMG / round).",
     "Спасбросок Тела [-] или загораетесь (2d10 урона / раунд).",
     "Порятунок Тіла [-] або загоряєтеся (2d10 шкоди / раунд)."),

    (6, "🔫", "25cr",     "Long",     "1d5 DMG",                    "2",   "Fire/Explosives [-]",
     "Flare Gun",                   "Сигнальный Пистолет",            "Сигнальний Пістолет",
     "High intensity flare visible day and night from Long Range.",
     "Яркая ракета, видимая днём и ночью на Дальней дистанции.",
     "Яскрава ракета, видима вдень і вночі на Далекій дистанції."),

    (7, "🔫", "500cr",    "Close",    "1 DMG",                      "3",   "Blunt Force",
     "Foam Gun",                    "Пеногаситель",                   "Піногасник",
     "Body Save or become stuck. Strength Check [-] to escape.",
     "Спасбросок Тела или застрять. Проверка Силы [-] для побега.",
     "Порятунок Тіла або застрягнути. Перевірка Сили [-] для втечі."),

    (8, "💣", "400cr ea.","Close",    "3d10 DMG",                   "1",   "Fire/Explosives",
     "Frag Grenade",                "Осколочная Граната",             "Осколкова Граната",
     "On a hit, damages all Adjacent to enemy.",
     "При попадании наносит урон всем Рядом с противником.",
     "При влученні завдає шкоди всім Поруч з ворогом."),

    (9, "🔫", "4.5kcr",   "Long",     "4d10 DMG",                   "5",   "Gunshot [+]",
     "General-Purpose Machine Gun", "Пулемёт Общего Назначения",      "Кулемет Загального Призначення",
     "Two-handed. Heavy. Barrel can be maneuvered to fire around corners.",
     "Двуручное. Тяжёлое. Ствол можно повернуть для стрельбы из-за угла.",
     "Дворучна. Важка. Ствол можна повернути для стрільби з-за кута."),

    (10, "🔧", "250cr",   "Adjacent", "1d10 DMG",                   "N/A", "Bleeding",
     "Hand Welder",                 "Ручной Сварочник",               "Ручний Зварювальник",
     "Can cut through airlock doors.",
     "Может прорезать двери шлюза.",
     "Може прорізати двері шлюзу."),

    (11, "🔫", "1,200cr", "Long",     "1d100 DMG",                  "6",   "Bleeding [+] or Gore [+]",
     "Laser Cutter",                "Лазерный Резак",                 "Лазерний Різак",
     "Two-handed. Heavy. 1 round recharge between shots.",
     "Двуручное. Тяжёлое. 1 раунд перезарядки между выстрелами.",
     "Дворучний. Важкий. 1 раунд перезарядки між пострілами."),

    (12, "🔫", "150cr",   "Close",    "1d5 DMG",                    "32",  "Bleeding",
     "Nail Gun",                    "Гвоздезабивной Пистолет",        "Цвяховий Пістолет",
     None, None, None),

    (13, "🔫", "2.4kcr",  "Long",     "3d10 DMG",                   "5",   "Gunshot",
     "Pulse Rifle",                 "Импульсная Винтовка",            "Імпульсна Гвинтівка",
     None, None, None),

    (14, "🔫", "750cr",   "Close",    "1d10+1 DMG",                 "6",   "Gunshot",
     "Revolver",                    "Револьвер",                      "Револьвер",
     None, None, None),

    (15, "🔫", "350cr",   "Close",    "1d10 DMG + 2d10 when removed","1",  "Bleeding [+]",
     "Rigging Gun",                 "Такелажный Пистолет",            "Такелажний Пістолет",
     "100m micro-filament. Body Save or become entangled.",
     "100м микрофиламент. Спасбросок Тела или запутаться.",
     "100м мікрофіламент. Порятунок Тіла або заплутатися."),

    (16, "⚔️", "50cr",    "Adjacent", "1d5 DMG",                    "N/A", "Bleeding [+]",
     "Scalpel",                     "Скальпель",                      "Скальпель",
     None, None, None),

    (17, "🔫", "5kcr",    "Extreme",  "4d10 DMG (AA)",               "3",  "Gunshot [+]",
     "Smart Rifle",                 "Умная Винтовка",                 "Розумна Гвинтівка",
     "[-] on Combat Check when fired at Close Range.",
     "[-] на Проверку Боя при стрельбе на Ближней дистанции.",
     "[-] на Перевірку Бою при стрільбі на Близькій дистанції."),

    (18, "🔫", "1kcr",    "Long",     "2d10 DMG",                   "5",   "Gunshot",
     "SMG",                         "Пистолет-Пулемёт",               "Пістолет-Кулемет",
     "Can be fired one-handed.",
     "Можно стрелять одной рукой.",
     "Можна стріляти однією рукою."),

    (19, "⚔️", "150cr",   "Adjacent", "1d5 DMG",                    "N/A", "Blunt Force",
     "Stun Baton",                  "Электрошокер",                   "Електрошокер",
     "Body Save or stunned 1 round.",
     "Спасбросок Тела или оглушён 1 раунд.",
     "Порятунок Тіла або приголомшений 1 раунд."),

    (20, "🔫", "250cr",   "Close",    "1d5 DMG",                    "6",   "Blunt Force",
     "Tranq Pistol",                "Транквилизаторный Пистолет",     "Транквілізаторний Пістолет",
     "If DMG dealt: enemy must Body Save or be unconscious 1d10 rounds.",
     "При нанесении урона: враг должен пройти Спасбросок Тела или потерять сознание на 1d10 раундов.",
     "При нанесенні шкоди: ворог має пройти Порятунок Тіла або втратити свідомість на 1d10 раундів."),

    (21, "👊", "Free",    "Adjacent", "Str/10 DMG",                 "N/A", "Blunt Force",
     "Unarmed",                     "Безоружный Бой",                 "Беззбройний Бій",
     None, None, None),

    (22, "⚔️", "1kcr",    "Adjacent", "3d10 DMG (AA)",              "N/A", "Bleeding + Gore",
     "Vibechete",                   "Вибромачете",                    "Вібромачете",
     "When dealing a Wound, roll on BOTH the Bleeding AND Gore columns.",
     "При нанесении Раны бросайте на ОБОИХ столбцах: Кровотечение И Расчленение.",
     "При нанесенні Рани кидайте на ОБОХ стовпцях: Кровотеча І Масивний урон."),
]


def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    """Add child_id to parent's linked_pages JSON array if not already present."""
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


def _make_desc(special: str | None) -> str | None:
    """desc = special rules text only. subinfo_fixed handles the stat display."""
    return special or None


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(WEAPONS)} weapons seeded into '{DB_PATH}'.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    conn.execute("""
        INSERT OR IGNORE INTO sources (id, slug, title, type)
        VALUES (1, 'psg', 'Player''s Survival Guide', 'core')
    """)

    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, linked_pages)
        VALUES (2, '🔫', 'psg', '[]')
    """)
    for lang, name in [("en", "Weapons & Damage"),
                        ("ru", "Оружие и Урон"),
                        ("ua", "Зброя та Шкода")]:
        conn.execute("""
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
            VALUES (?, ?, ?)
        """, (2, lang, name))

    _add_linked_page(conn, parent_id=1, child_id=2)

    weapon_ids = [w[0] for w in WEAPONS]
    conn.execute(
        f"DELETE FROM contents WHERE id IN ({','.join('?'*len(weapon_ids))})",
        weapon_ids,
    )

    for (cid, icon, cost, range_key, damage, shots, wound_key,
         name_en, name_ru, name_ua,
         special_en, special_ru, special_ua) in WEAPONS:

        subinfo = json.dumps([
            {"label_key": "cost",       "value": cost,      "type": "cost"},
            {"label_key": "range",      "value": range_key, "type": "stat"},
            {"label_key": "damage",     "value": damage,    "type": "roll"},
            {"label_key": "shots",      "value": shots,     "type": "stat"},
            {"label_key": "wound_type", "value": wound_key, "type": "stat"},
        ])

        conn.execute("""
            INSERT INTO contents (id, icon, source_slug, subinfo_fixed, sort_order)
            VALUES (?, ?, 'psg', ?, ?)
        """, (cid, icon, subinfo, cid))

        specials = {"en": special_en, "ru": special_ru, "ua": special_ua}
        names    = {"en": name_en,    "ru": name_ru,    "ua": name_ua}
        for lang in ("en", "ru", "ua"):
            conn.execute("""
                INSERT INTO content_i18n (content_id, lang, name, desc, subinfo_text)
                VALUES (?, ?, ?, ?, NULL)
            """, (cid, lang, names[lang], _make_desc(specials[lang])))

        conn.execute("""
            INSERT INTO page_contents (page_id, content_id, sort_order)
            VALUES (2, ?, ?)
        """, (cid, cid))

    # ── Content links: weapon → range band / wound type (requires combat script run first) ──
    existing = {r[0] for r in conn.execute("SELECT id FROM contents")}
    for (cid, _icon, _cost, range_key, _damage, _shots, wound_key,
         *_rest) in WEAPONS:
        sort = 0
        # Link to range band content
        if range_key in RANGE_CONTENT:
            target = RANGE_CONTENT[range_key]
            if target in existing:
                conn.execute("""
                    INSERT OR IGNORE INTO content_links
                        (from_content_id, to_content_id, label_key, sort_order)
                    VALUES (?, ?, 'related', ?)
                """, (cid, target, sort))
                sort += 1
        # Link to wound type table(s)
        for target in WOUND_CONTENT.get(wound_key, []):
            if target in existing:
                conn.execute("""
                    INSERT OR IGNORE INTO content_links
                        (from_content_id, to_content_id, label_key, sort_order)
                    VALUES (?, ?, 'related', ?)
                """, (cid, target, sort))
                sort += 1


if __name__ == "__main__":
    run()
