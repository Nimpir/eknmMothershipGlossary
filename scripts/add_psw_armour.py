"""
scripts/add_psw_armour.py
Seed Armour from the Player's Survival Guide quick-reference table.
Run after add_psw_combat.py (C28 Armor rule must exist for content links).
"""

import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── C28 = "Armor" combat rule (seeded by add_psw_combat.py) ──────────────────
ARMOR_RULE_CONTENT_ID = 28

# ── Armour data ───────────────────────────────────────────────────────────────
# Each entry: (id, icon, cost, ap, o2, speed,
#              name_en, name_ru, name_ua,
#              desc_en, desc_ru, desc_ua)
ARMOUR = [
    (41, "👕", "100cr",  "1",  "—",      "Normal",
     "Standard Crew Attire",
     "Стандартная Одежда Экипажа",
     "Стандартний Одяг Екіпажу",
     "Basic clothing.",
     "Базовая одежда.",
     "Базовий одяг."),

    (42, "🔵", "10kcr",  "3",  "12 hrs", "[-]",
     "Vaccsuit",
     "Вакуумный Костюм",
     "Вакуумний Костюм",
     "Includes short-range comms, headlamp, and radiation shielding. "
     "Decompression within 1d5 rounds if punctured.",
     "Включает ближнюю связь, фонарь и защиту от радиации. "
     "Разгерметизация за 1d5 раундов при пробитии.",
     "Включає ближній зв'язок, ліхтар і захист від радіації. "
     "Розгерметизація за 1d5 раундів при пробитті."),

    (43, "☢️", "4kcr",   "5",  "1 hr",   "Normal",
     "Hazard Suit",
     "Защитный Костюм",
     "Захисний Костюм",
     "Includes air filter, extreme heat/cold protection, hydration reclamation "
     "(1L of water lasts 4 days), short-range comms, headlamp, and radiation shielding.",
     "Включает воздушный фильтр, защиту от экстремального жара/холода, рекуперацию влаги "
     "(1 л воды хватает на 4 дня), ближнюю связь, фонарь и защиту от радиации.",
     "Включає повітряний фільтр, захист від екстремальних температур, рекуперацію вологи "
     "(1 л води вистачає на 4 дні), ближній зв'язок, ліхтар і захист від радіації."),

    (44, "🪖", "2kcr",   "7",  "—",      "Normal",
     "Standard Battle Dress",
     "Стандартный Боевой Костюм",
     "Стандартний Бойовий Костюм",
     "Includes short-range comms.",
     "Включает ближнюю связь.",
     "Включає ближній зв'язок."),

    (45, "🤖", "12kcr",  "10", "1 hr",   "[-]",
     "Advanced Battle Dress",
     "Улучшенный Боевой Костюм",
     "Покращений Бойовий Костюм",
     "Includes short-range comms, body cam, headlamp, HUD, exoskeletal weave "
     "(Strength Checks [+]), and radiation shielding. Damage Reduction: 3.",
     "Включает ближнюю связь, нагрудную камеру, фонарь, HUD, экзоскелетное плетение "
     "(Проверки Силы [+]) и защиту от радиации. Снижение урона: 3.",
     "Включає ближній зв'язок, нагрудну камеру, ліхтар, HUD, екзоскелетне плетіння "
     "(Перевірки Сили [+]) і захист від радіації. Зменшення шкоди: 3."),
]


def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    """Append child_id to parent's linked_pages if not already present."""
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(ARMOUR)} armour items seeded into '{DB_PATH}'.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    conn.execute("""
        INSERT OR IGNORE INTO sources (id, slug, title, type)
        VALUES (1, 'psg', 'Player''s Survival Guide', 'core')
    """)

    # Page P6 — Armour
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, linked_pages)
        VALUES (6, '🛡️', 'psg', '[]')
    """)
    for lang, name in [("en", "Armour"),
                        ("ru", "Броня"),
                        ("ua", "Броня")]:
        conn.execute("""
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
            VALUES (?, ?, ?)
        """, (6, lang, name))

    _add_linked_page(conn, parent_id=1, child_id=6)

    # Delete and re-seed armour content items
    armour_ids = [a[0] for a in ARMOUR]
    conn.execute(
        f"DELETE FROM contents WHERE id IN ({','.join('?'*len(armour_ids))})",
        armour_ids,
    )

    for (cid, icon, cost, ap, o2, speed,
         name_en, name_ru, name_ua,
         desc_en, desc_ru, desc_ua) in ARMOUR:

        subinfo = json.dumps([
            {"label_key": "cost",  "value": cost,  "type": "cost"},
            {"label_key": "ap",    "value": ap,    "type": "stat"},
            {"label_key": "o2",    "value": o2,    "type": "stat"},
            {"label_key": "speed", "value": speed, "type": "stat"},
        ])

        conn.execute("""
            INSERT INTO contents (id, icon, source_slug, subinfo_fixed, sort_order)
            VALUES (?, ?, 'psg', ?, ?)
        """, (cid, icon, subinfo, cid))

        names = {"en": name_en, "ru": name_ru, "ua": name_ua}
        descs = {"en": desc_en, "ru": desc_ru, "ua": desc_ua}
        for lang in ("en", "ru", "ua"):
            conn.execute("""
                INSERT INTO content_i18n (content_id, lang, name, desc, subinfo_text)
                VALUES (?, ?, ?, ?, NULL)
            """, (cid, lang, names[lang], descs[lang]))

        conn.execute("""
            INSERT INTO page_contents (page_id, content_id, sort_order)
            VALUES (6, ?, ?)
        """, (cid, cid))

    # Content links: each armour item → C28 (Armor combat rule)
    existing = {r[0] for r in conn.execute("SELECT id FROM contents")}
    if ARMOR_RULE_CONTENT_ID in existing:
        for (cid, *_rest) in ARMOUR:
            conn.execute("""
                INSERT OR IGNORE INTO content_links
                    (from_content_id, to_content_id, label_key, sort_order)
                VALUES (?, ?, 'related', 0)
            """, (cid, ARMOR_RULE_CONTENT_ID))


if __name__ == "__main__":
    run()
