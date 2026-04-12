"""
scripts/update_c229_remove_ships_docked_inline.py
Remove the inline "SHIPS DOCKED (d10): ..." table from C229 (01 Dry Dock)
description — that data now lives in C330 (Ships Currently Docked).
Run: python scripts/update_c229_remove_ships_docked_inline.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

DESC_EN = (
    "The Dry Dock is hundreds of small ports. Sparks fly; shipbuilders scurry on scaffolding above massive ships.\n\n"
    "KEY AREAS:\n"
    "1. CLEAN ROOM — Q-Team strip search & disinfect. 1d5+1 Q-Team members.\n"
    "2. LOSHE'S OFFICE — Cramped, greasy. Safe contains plans for an experimental Jump-8 drive (4 Fuel).\n"
    "3. REPAIR BAY — Giant robotic limbs. Mechanics on watch.\n"
    "4. HANGAR BAY — Where your ship docks. 10% chance cargo stolen unless guards hired from Tempest.\n\n"
    "LOSHE (Dockmaster): COMBAT 55 (Exoskeleton bash 4d10 DMG) | INSTINCT 60 | HITS 3 (40)\n"
    "Exoskeleton: 4 arms, each capable of attacking or firing a weapon in one round. Reapable. Worth 40kcr.\n"
    "Personally oversees every ship. Hub of station information. Calm voice, always smoking. Wants to keep "
    "the dock running smoothly and get his 1-year sobriety chip."
)

DESC_RU = (
    "Сухой Dok — сотни маленьких портов. Искры летят; судостроители снуют по лесам над кораблями.\n\n"
    "КЛЮЧЕВЫЕ ЗОНЫ:\n"
    "1. ДЕЗИНФЕКЦИОННАЯ КОМНАТА — Команда-Q обыскивает и обрабатывает. 1d5+1 членов.\n"
    "2. КАБИНЕТ ЛОШЕ — Тесный, жирный. Сейф содержит планы экспериментального прыжкового двигателя Jump-8 (4 топлива).\n"
    "3. РЕМОНТНЫЙ ЦЕХ — Гигантские роботизированные конечности. Механики наблюдают.\n"
    "4. АНГАРНЫЙ ОТСЕК — Стоянка вашего корабля. 10% шанс кражи груза без охраны Tempest.\n\n"
    "ЛОШЕ (Начальник дока): БОЙ 55 (Удар экзоскелета 4d10 урона) | ИНСТИНКТ 60 | ОЗ 3 (40)\n"
    "Экзоскелет: 4 руки, каждая может атаковать или стрелять за раунд. Можно изъять. Стоит 40 ккр.\n"
    "Лично проверяет каждый корабль. Источник информации о станции. Спокойный голос, всегда курит сигары."
)

DESC_UA = (
    "Сухий Dok — сотні маленьких портів. Іскри летять; суднобудівники снують по риштуванню над кораблями.\n\n"
    "КЛЮЧОВІ ЗОНИ:\n"
    "1. ДЕЗІНФЕКЦІЙНА КІМНАТА — Команда-Q обшукує та обробляє. 1d5+1 членів.\n"
    "2. КАБІНЕТ ЛОШЕ — Тісний, жирний. Сейф містить плани експериментального двигуна Jump-8 (4 палива).\n"
    "3. РЕМОНТНИЙ ЦЕХ — Гігантські роботизовані кінцівки. Механіки спостерігають.\n"
    "4. АНГАРНИЙ ВІДСІК — Стоянка вашого корабля. 10% шанс крадіжки вантажу без охорони Tempest.\n\n"
    "ЛОШЕ (Начальник дока): БІЙ 55 (Удар екзоскелета 4d10 шкоди) | ІНСТИНКТ 60 | ОЗ 3 (40)\n"
    "Екзоскелет: 4 руки, кожна може атакувати або стріляти за раунд. Можна вилучити. Вартість 40 ккр.\n"
    "Особисто перевіряє кожен корабель. Джерело інформації про станцію. Спокійний голос, завжди курить сигари."
)


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        for lang, desc in [("en", DESC_EN), ("ru", DESC_RU), ("ua", DESC_UA)]:
            conn.execute(
                "UPDATE content_i18n SET desc = ? WHERE content_id = 229 AND lang = ?",
                (desc, lang),
            )
        conn.commit()
        print("Done — SHIPS DOCKED inline text removed from C229 desc (all 3 languages).")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
