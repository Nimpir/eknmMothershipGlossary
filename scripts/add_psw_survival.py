"""
scripts/add_psw_survival.py
Seed Survival (P14) from PSG pg 32–33.
Creates P14 under P11 with C150–C157.
Run after add_psw_skills.py: python scripts/add_psw_survival.py
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
    (14, "🌍", 32, "Survival", "Выживание", "Виживання"),
]

CONTENTS = [
    {
        "id": 150, "icon": "🌫️", "source_page": 32,
        "name": ("Atmospheres", "Атмосферы", "Атмосфери"),
        "desc": (
            "Toxic Atmosphere: The planet's atmosphere is not fit to breathe but is otherwise safe. "
            "A rebreather or armor with its own oxygen supply is required. Without these, characters "
            "take 1d10 DMG per round, Body Save for half.\n\n"
            "Corrosive Atmosphere: The planet's atmosphere is deadly and destructive. It deals Damage "
            "every round while on it. This ranges from 1 DMG/round (Mildly Corrosive) to 10 DMG/round "
            "(Highly Corrosive). Anything higher is simply impossible to safely traverse without "
            "specialized equipment and armor.",

            "Токсичная атмосфера: Атмосфера планеты непригодна для дыхания, но в остальном безопасна. "
            "Требуется респиратор или броня с собственным запасом кислорода. Без них персонажи получают "
            "1d10 урона в раунд, Спасбросок Тела для половины урона.\n\n"
            "Разъедающая атмосфера: Атмосфера планеты смертоносна и разрушительна. Она наносит урон "
            "каждый раунд нахождения на ней. От 1 урона/раунд (Слегка разъедающая) до 10 урона/раунд "
            "(Сильно разъедающая). Всё, что выше, невозможно безопасно пройти без специального "
            "снаряжения и брони.",

            "Токсична атмосфера: Атмосфера планети непридатна для дихання, але в іншому безпечна. "
            "Потрібен респіратор або броня з власним запасом кисню. Без них персонажі отримують "
            "1d10 шкоди за раунд, Порятунок Тіла для половини шкоди.\n\n"
            "Роз'їдаюча атмосфера: Атмосфера планети смертоносна і руйнівна. Вона завдає шкоди "
            "кожен раунд перебування на ній. Від 1 шкоди/раунд (Злегка роз'їдаюча) до 10 шкоди/раунд "
            "(Сильно роз'їдаюча). Все, що вище, неможливо безпечно пройти без спеціального "
            "спорядження та броні.",
        ),
    },
    {
        "id": 151, "icon": "🩸", "source_page": 32,
        "name": ("Bleeding", "Кровотечение", "Кровотеча"),
        "desc": (
            "Some weapons or Wounds cause characters to Bleed. This means they take 1 Damage every "
            "round until the bleeding is stopped. Bleeding is cumulative — if a character is Bleeding "
            "1 DMG/round and gains Bleeding +1, they now take 2 DMG/round.\n\n"
            "Bleeding damage ignores armor and damage reduction.",

            "Некоторое оружие или Раны заставляют персонажей Истекать кровью. Это означает, что они "
            "получают 1 урон каждый раунд, пока кровотечение не остановлено. Кровотечение суммируется — "
            "если персонаж получает 1 урон/раунд от кровотечения и получает Кровотечение +1, теперь он "
            "получает 2 урона/раунд.\n\n"
            "Урон от кровотечения игнорирует броню и снижение урона.",

            "Деяка зброя або Рани змушують персонажів Кровоточити. Це означає, що вони отримують "
            "1 шкоди щороку, поки кровотечу не зупинено. Кровотеча сумується — якщо персонаж отримує "
            "1 шкоди/раунд від кровотечі та отримує Кровотеча +1, тепер він отримує 2 шкоди/раунд.\n\n"
            "Шкода від кровотечі ігнорує броню та зниження шкоди.",
        ),
    },
    {
        "id": 152, "icon": "🧊", "source_page": 32,
        "name": ("Cryosickness", "Криозаморозка", "Кріохвороба"),
        "desc": (
            "To endure long space journeys or hyperspace jumps, crews use cryopods — coffin-like "
            "capsules that freeze them in suspended animation called cryosleep. While in cryosleep, "
            "vitals are preserved and aging slows down.\n\n"
            "However, upon awakening, you experience a hangover-like feeling called cryosickness, which "
            "causes sluggishness and slow reflexes. While cryosick you suffer [-] on all rolls for "
            "1 week. Upgraded cryochambers can help mitigate these effects, and a Stimpak can cure "
            "them instantly.",

            "Для длительных космических путешествий или прыжков сквозь гиперпространство экипажи "
            "используют криокапсулы — гробоподобные камеры, замораживающие их в состоянии "
            "криосна. Во время криосна жизненные показатели сохраняются, а старение замедляется.\n\n"
            "Однако при пробуждении ощущается похмельеподобное состояние — криобользнь, вызывающая "
            "вялость и замедленные рефлексы. При криоболезни вы страдаете [-] на все броски в течение "
            "1 недели. Улучшенные криокамеры помогают смягчить эти эффекты, а Стимпак излечивает "
            "их мгновенно.",

            "Для тривалих космічних подорожей або стрибків крізь гіперпростір екіпажі використовують "
            "кріокапсули — гробоподібні камери, що заморожують їх у стані кріосну. Під час кріосну "
            "життєві показники зберігаються, а старіння сповільнюється.\n\n"
            "Однак при пробудженні відчувається схожий на похмілля стан — кріохвороба, що спричиняє "
            "млявість і сповільнені рефлекси. При кріохворобі ви страждаєте [-] на всі кидки протягом "
            "1 тижня. Покращені кріокамери допомагають пом'якшити ці ефекти, а Стимпак лікує "
            "їх миттєво.",
        ),
    },
    {
        "id": 153, "icon": "🍱", "source_page": 32,
        "name": ("Food & Water", "Еда и Вода", "Їжа та Вода"),
        "desc": (
            "Humans can survive roughly 3 weeks without food. After 24 hours without food, roll at "
            "Disadvantage on all rolls.\n\n"
            "For the bare minimum of survival you need 1 liter of water a day. However, at this level, "
            "any strenuous activity (e.g., running, combat, making mechanical repairs) forces you to "
            "make a Body Save or pass out. When water is scarce and you're tracking it this closely, "
            "you're at Disadvantage on all rolls.",

            "Люди могут прожить примерно 3 недели без еды. После 24 часов без еды бросайте с "
            "Помехой на все броски.\n\n"
            "Для минимального выживания вам нужен 1 литр воды в день. Однако на этом уровне любая "
            "напряжённая деятельность (например, бег, бой, механические ремонты) вынуждает делать "
            "Спасбросок Тела или потерять сознание. Когда воды мало и вы тщательно её отслеживаете, "
            "вы бросаете с Помехой на все броски.",

            "Люди можуть прожити приблизно 3 тижні без їжі. Після 24 годин без їжі кидайте з "
            "Перешкодою на всі кидки.\n\n"
            "Для мінімального виживання вам потрібен 1 літр води на день. Однак на цьому рівні будь-яка "
            "напружена діяльність (наприклад, біг, бій, механічні ремонти) змушує робити Порятунок Тіла "
            "або знепритомніти. Коли води мало і ви ретельно її відстежуєте, ви кидаєте з Перешкодою "
            "на всі кидки.",
        ),
    },
    {
        "id": 154, "icon": "💨", "source_page": 33,
        "name": ("Oxygen", "Кислород", "Кисень"),
        "desc": (
            "In space you can last 15 seconds without oxygen before falling unconscious. After passing "
            "out, you can survive for 1d5 minutes before dying.\n\n"
            "If all of a ship's Life Support System goes offline, roll 1d10 and multiply it by the "
            "maximum crew capacity. This is the remaining oxygen supply.\n\n"
            "Every 24 hours, subtract the total number of breathing crewmembers from the remaining "
            "oxygen supply. Crewmembers engaging in strenuous activity further reduce the supply by 2 each.\n\n"
            "• When oxygen supply < 2× breathing passengers: all rolls at Disadvantage (headaches, fatigue, "
            "anxiety, clumsiness).\n"
            "• When oxygen supply < total breathing passengers: every breathing passenger must make a Body "
            "Save or make a Death Save.\n"
            "• When oxygen runs out: 15 seconds before unconscious, then 1d5 minutes before death.\n\n"
            "Androids do not consume oxygen. Those in cryosleep do not reduce the oxygen supply.",

            "В космосе без кислорода можно продержаться 15 секунд до потери сознания. После потери "
            "сознания можно прожить 1d5 минут.\n\n"
            "Если вся система жизнеобеспечения корабля отключится, бросьте 1d10 и умножьте на "
            "максимальную вместимость экипажа. Это оставшийся запас кислорода.\n\n"
            "Каждые 24 часа вычитайте из запаса кислорода общее число дышащих членов экипажа. "
            "Члены экипажа, занятые напряжённой деятельностью, дополнительно сокращают запас на 2 каждый.\n\n"
            "• Когда запас < 2× дышащих пассажиров: все броски с Помехой.\n"
            "• Когда запас < числа дышащих пассажиров: каждый делает Спасбросок Тела или Спасбросок "
            "от Смерти.\n"
            "• Когда кислород заканчивается: 15 секунд до потери сознания, затем 1d5 минут до смерти.\n\n"
            "Андроиды не потребляют кислород. Те, кто в криосне, не сокращают запас кислорода.",

            "У космосі без кисню можна протриматися 15 секунд до втрати свідомості. Після втрати "
            "свідомості можна прожити 1d5 хвилин.\n\n"
            "Якщо вся система життєзабезпечення корабля відключиться, киньте 1d10 і помножте на "
            "максимальну місткість екіпажу. Це залишковий запас кисню.\n\n"
            "Кожні 24 години віднімайте від запасу кисню загальну кількість дихаючих членів екіпажу. "
            "Члени екіпажу, зайняті напруженою діяльністю, додатково скорочують запас на 2 кожен.\n\n"
            "• Коли запас < 2× дихаючих пасажирів: всі кидки з Перешкодою.\n"
            "• Коли запас < кількості дихаючих пасажирів: кожен робить Порятунок Тіла або Порятунок "
            "від Смерті.\n"
            "• Коли кисень закінчується: 15 секунд до втрати свідомості, потім 1d5 хвилин до смерті.\n\n"
            "Андроїди не споживають кисень. Ті, хто у кріосні, не скорочують запас кисню.",
        ),
    },
    {
        "id": 155, "icon": "☢️", "source_page": 33,
        "name": ("Radiation", "Радиация", "Радіація"),
        "desc": (
            "Whether it's cosmic rays, an engine leak, or some previously undiscovered asteroid ore, "
            "radiation can kill you if you're not careful.\n\n"
            "Armor with Radiation Shielding (e.g., the Hazard Suit) blocks all three levels of radiation.",

            "Будь то космические лучи, утечка двигателя или неизвестная asteroiдная руда, "
            "радиация может убить вас, если вы не будете осторожны.\n\n"
            "Броня с радиационной защитой (например, Защитный Костюм) блокирует все три уровня радиации.",

            "Будь то космічні промені, витік двигуна або невідома астероїдна руда, "
            "радіація може вбити вас, якщо ви не будете обережні.\n\n"
            "Броня з радіаційним захистом (наприклад, Захисний Костюм) блокує всі три рівні радіації.",
        ),
        "dice": {
            "die": "d3",
            "entries": [
                {
                    "min": 1, "max": 1,
                    "text": "Level 1 – Trace: Normal everyday radiation, cosmic rays. No immediate damage. Possible long-term side effects (cancer, etc.).",
                },
                {
                    "min": 2, "max": 2,
                    "text": "Level 2 – Acute: Unshielded reactors, warp cores. Reduce all Stats and Saves by 1 every round.",
                },
                {
                    "min": 3, "max": 3,
                    "text": "Level 3 – Lethal: Atomic weapons, direct handling of warp cores. Every round: Body Save or lethal dose (death in 1d5 days).",
                },
            ],
        },
    },
    {
        "id": 156, "icon": "💊", "source_page": 33,
        "name": ("Stimpak Overdose", "Передозировка Стимпака", "Передозування Стімпака"),
        "desc": (
            "Excessive use of stimpaks (and other dangerous drugs) carries a risk of overdose. Whenever "
            "a character takes more than one stimpak in a day, roll 1d10. If you roll under the amount "
            "of doses taken in the past 24 hours, make a Death Save.",

            "Чрезмерное использование стимпаков (и других опасных препаратов) несёт риск передозировки. "
            "Когда персонаж принимает более одного стимпака в день, бросьте 1d10. Если результат меньше "
            "количества доз, принятых за последние 24 часа, сделайте Спасбросок от Смерти.",

            "Надмірне використання стімпаків (та інших небезпечних препаратів) несе ризик передозування. "
            "Коли персонаж приймає більше одного стімпака на день, киньте 1d10. Якщо результат менше "
            "кількості доз, прийнятих за останні 24 години, зробіть Порятунок від Смерті.",
        ),
    },
    {
        "id": 157, "icon": "🌡️", "source_page": 33,
        "name": ("Temperature", "Температура", "Температура"),
        "desc": (
            "In most cases, a hot or cold climate has no notable effects. However, in places of extreme "
            "cold or heat, make Body Saves every hour or succumb to Extreme Cold/Heat.\n\n"
            "Extreme Cold: In sub-zero temperatures, hypothermia and frostbite can set in within 10–30 "
            "minutes for those not dressed appropriately. To survive you must bring your body up to its "
            "normal temperature. Hypothermia can kill within 30 minutes to 6 hours.\n\n"
            "Extreme Heat: Extreme heat over 100°F/40°C can cause heat stroke and kill within hours. "
            "Victims must move to a cooler location immediately to get their temperature down.",

            "В большинстве случаев жаркий или холодный климат не имеет заметных эффектов. Однако "
            "в местах с экстремальным холодом или жарой делайте Спасброски Тела каждый час или "
            "поддайтесь Экстремальному Холоду/Жаре.\n\n"
            "Экстремальный холод: При температурах ниже нуля гипотермия и обморожение могут наступить "
            "в течение 10–30 минут у тех, кто не одет соответствующим образом. Для выживания нужно "
            "поднять температуру тела до нормы. Гипотермия может убить в течение 30 минут – 6 часов.\n\n"
            "Экстремальная жара: Жара выше 40°C может вызвать тепловой удар и убить в течение часов. "
            "Пострадавшие должны немедленно перейти в более прохладное место.",

            "У більшості випадків спекотний або холодний клімат не має помітних ефектів. Однак "
            "у місцях з екстремальним холодом або спекою робіть Порятунки Тіла щогодини або "
            "піддайтеся Екстремальному Холоду/Спеці.\n\n"
            "Екстремальний холод: При температурах нижче нуля гіпотермія та обмороження можуть "
            "настати протягом 10–30 хвилин у тих, хто не одягнений відповідно. Для виживання потрібно "
            "підняти температуру тіла до норми. Гіпотермія може вбити протягом 30 хвилин – 6 годин.\n\n"
            "Екстремальна спека: Спека вище 40°C може спричинити тепловий удар і вбити протягом годин. "
            "Постраждалі повинні негайно перейти в більш прохолодне місце.",
        ),
    },
]

# ── page_contents order ────────────────────────────────────────────────────────
# P14: Atmospheres(150), Bleeding(151), Cryosickness(152), Food&Water(153),
#      Oxygen(154), Radiation(155), StimpakOD(156), Temperature(157)
P14_CONTENT_ORDER = [150, 151, 152, 153, 154, 155, 156, 157]


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

    # ── Attach P14 to P11 ─────────────────────────────────────────────────────
    cur.execute("SELECT linked_pages FROM pages WHERE id=11")
    row = cur.fetchone()
    linked = json.loads(row[0]) if row and row[0] else []
    if 14 not in linked:
        linked.append(14)
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
    cur.execute("DELETE FROM page_contents WHERE page_id=14")
    for sort_order, cid in enumerate(P14_CONTENT_ORDER):
        cur.execute(
            "INSERT INTO page_contents (page_id, content_id, sort_order) VALUES (?,?,?)",
            (14, cid, sort_order),
        )

    conn.commit()
    conn.close()
    print("Done ✓ Survival (P14) + C150–C157 seeded into", repr(db_path))


if __name__ == "__main__":
    seed(DB_PATH)
