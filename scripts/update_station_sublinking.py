"""
scripts/update_station_sublinking.py
Move secondary content items off P35 and link them as sub-items under their
parent location content. Also removes inline job tables from C232 desc.

Changes:
  C231 → sub of C230 (The Stellar Burn)
  C331 → sub of C232 (The Chop Shop)  — removes Babushka Jobs inline text
  C234 → sub of C233 (The Ice Box)
  C236 → sub of C235 (The Farm)
  C238, C239 → sub of C237 (CANYONHEAVY.market)
  C241, C332, C333 → sub of C240 (The Court)
  C243, C244 → sub of C242 (Tempest Company HQ)

Run: python scripts/update_station_sublinking.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# Items to remove from P35 direct buttons
REMOVE_FROM_P35 = [231, 331, 234, 236, 238, 239, 241, 332, 333, 243, 244]

# Forward content_links to add: (from_id, to_id, sort_order)
NEW_LINKS = [
    (230, 231, 0),   # The Stellar Burn → Heaven/Ecstasy
    (232, 331, 0),   # The Chop Shop → Jobs for The Babushka
    (233, 234, 0),   # The Ice Box → Ice Box Services
    (235, 236, 0),   # The Farm → Sycorax
    (237, 238, 0),   # CANYONHEAVY.market → CANYONHEAVY Missions
    (237, 239, 1),   # CANYONHEAVY.market → CANYONHEAVY Stock
    (240, 241, 0),   # The Court → Pit Fighters
    (240, 332, 1),   # The Court → The Docket
    (240, 333, 2),   # The Court → Accused & What They Can Pay
    (242, 243, 0),   # Tempest Company HQ → Tempest Missions
    (242, 244, 1),   # Tempest Company HQ → Tempest Roster
]

C232_DESC_EN = (
    "Overflowing with trash and grime. Run by the legendary cybersurgeon THE BABUSHKA and her holographic AI child ZHENYA. "
    "Access requires background check — must be on good terms with Yandee.\n\n"
    "1. ENTRANCE — Crowded. Zhenya greets visitors. 3 Augmented Toys hidden as guards [COMBAT 55, SMG+ 4d10[+] DMG + Frag Grenades, HITS 2 (10)].\n"
    "2. RECOVERY ROOM — 6 dingy bunks. One contains a melted horrific cybermod mutant. (Fear Save or 1d10 Stress.) 100cr/day.\n"
    "3. SYCORAX STASH — Babushka's anaesthetic. 1d10 barrels, guarded by Augmented Toy.\n"
    "4–7. OPERATING THEATERS — Babushka works ~20hrs/day in surgery. Room 7 quarantined for ACMD patients.\n"
    "8. BABUSHKA'S ROOM — Photo of Zhenya as a real boy. Note: 'Vera — one more trip and Y will let me home.'\n"
    "9. CYBERMOD STORAGE & REAPER BARN — Back tunnel to The Choke. 2d10 of each cybermod in stock.\n\n"
    "THE BABUSHKA: COMBAT 25 (Sawed-Off 2d10 DMG or MegaTranq) | INSTINCT 90 | HITS 2 (45)\n"
    "Cyber Savant: On any hit, may shut down one cybermod of target for the encounter."
)

C232_DESC_RU = (
    "Завалена мусором и грязью. Управляется легендарным кибернетическим хирургом БАБУШКОЙ и её голографическим ИИ-ребёнком ЖЕНЕЙ. "
    "Нужен допуск — не должен быть на плохом счету у Яндея.\n\n"
    "1. ВХОД — Захламлён. Женя встречает посетителей. 3 Дополненных игрушки-охранника.\n"
    "2. КОМНАТА ВОССТАНОВЛЕНИЯ — 6 коек. Одна занята расплавленным мутантом-имплантатом. 100 кр/день.\n"
    "3. ЗАПАС СИКОРАХА — Анестетик Бабушки. 1d10 бочек, охраняется Дополненной игрушкой.\n"
    "4–7. ОПЕРАЦИОННЫЕ — Бабушка работает ~20 ч/день. Палата 7 — на карантине для ACMD.\n"
    "8. КОМНАТА БАБУШКИ — Фото Жени маленьким. Записка: «Вера — ещё один рейс, и Я отпустит домой».\n"
    "9. ХРАНЕНИЕ ИМПЛАНТОВ — Тоннель в Удавку. 2d10 каждого кибермода в запасе.\n\n"
    "БАБУШКА: БОЙ 25 (Обрез 2d10 / МегаТранк) | ИНСТИНКТ 90 | ОЗ 2 (45)\n"
    "Кибер-Мастер: При любом попадании отключает один имплант цели на время боя."
)

C232_DESC_UA = (
    "Завалена сміттям і брудом. Керується легендарним кібернетичним хірургом БАБУСЕЮ та її голографічним ШІ-дитям ЖЕНЕЮ. "
    "Потрібен допуск — не повинен бути на поганому рахунку у Яндея.\n\n"
    "1. ВХІД — Захаращений. Женя зустрічає відвідувачів. 3 Доповнені іграшки-охоронці.\n"
    "2. КІМНАТА ВІДНОВЛЕННЯ — 6 ліжок. Одне зайняте розплавленим мутантом-імплантатом. 100 кр/день.\n"
    "3. ЗАПАС СИКОРАХУ — Анестетик Бабусі. 1d10 бочок, охороняється Доповненою іграшкою.\n"
    "4–7. ОПЕРАЦІЙНІ — Бабуся працює ~20 год/день. Палата 7 — на карантині для ACMD.\n"
    "8. КІМНАТА БАБУСІ — Фото Жені маленьким. Записка: «Віра — ще один рейс, і Я відпустить додому».\n"
    "9. ЗБЕРІГАННЯ ІМПЛАНТІВ — Тунель до Задуші. 2d10 кожного кіберімпланта в запасі.\n\n"
    "БАБУСЯ: БІЙ 25 (Обріз 2d10 / МегаТранк) | ІНСТИНКТ 90 | ОЗ 2 (45)\n"
    "Кібер-Майстер: При будь-якому влученні вимикає один імплант цілі на час бою."
)


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — 11 sub-items unlinked from P35; forward links added; C232 desc updated.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    ph = ",".join("?" * len(REMOVE_FROM_P35))
    conn.execute(
        f"DELETE FROM page_contents WHERE page_id = 35 AND content_id IN ({ph})",
        REMOVE_FROM_P35,
    )

    for from_id, to_id, sort in NEW_LINKS:
        conn.execute(
            "INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key, sort_order) VALUES (?, ?, 'related', ?)",
            (from_id, to_id, sort),
        )

    for lang, desc in [("en", C232_DESC_EN), ("ru", C232_DESC_RU), ("ua", C232_DESC_UA)]:
        conn.execute(
            "UPDATE content_i18n SET desc = ? WHERE content_id = 232 AND lang = ?",
            (desc, lang),
        )


if __name__ == "__main__":
    run()
