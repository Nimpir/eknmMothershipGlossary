"""
scripts/update_choke_sublinking.py
Move C248–C253 from P36 direct buttons to sub-items under C247 (The Choke).
Add 5 missing Choke/Sink sub-locations: The Falls (C343), The Doctor (C344),
The Old City (C345), Mass Grave (C346), The Veins (C347).
Run: python scripts/update_choke_sublinking.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# Items to remove from P36 direct buttons
REMOVE_FROM_P36 = [248, 249, 250, 251, 252, 253]

# Forward links from C247 to existing sub-items: (from, to, sort_order)
CHOKE_EXISTING_LINKS = [
    (247, 248, 0),   # The Choke → The Sink
    (247, 249, 1),   # The Choke → Life Support 01
    (247, 250, 2),   # The Choke → The Burrows
    (247, 251, 3),   # The Choke → Caliban's Heart
    (247, 252, 4),   # The Choke → Chokespawn
    (247, 253, 5),   # The Choke → Encounters
]

# New sub-locations
NEW_CONTENTS = [
    # (id, icon, source_slug)
    (343, "💧", "apof"),   # The Falls
    (344, "🩺", "apof"),   # The Doctor
    (345, "🏚️", "apof"),  # The Old City
    (346, "⚰️", "apof"),   # Mass Grave
    (347, "🩸", "apof"),   # The Veins
]

NEW_I18N = {
    343: {
        "en": (
            "The Falls",
            "Twenty story toxic sludge waterfall descending from Doptown into The Sink. "
            "Strength Check to climb down unassisted by gear. An old Hunglung named Otto sells "
            "scavenged climbing gear for a full O2 tank per set or 2kcr. For 500cr Otto will "
            "sketch a map of directions to The Doctor. 5% chance the gear is faulty.",
        ),
        "ru": (
            "Водопад",
            "Двадцатиэтажный токсический водопад из зловонной жижи, спускающийся из Доптауна "
            "в Раковину. Проверка Силы для спуска без снаряжения. Старый Хунглун по имени Отто "
            "продаёт найденное снаряжение за полный баллон О2 или 2 ккр. За 500 кр Отто "
            "нарисует карту пути к Доктору. 5% шанс, что снаряжение неисправно.",
        ),
        "ua": (
            "Водоспад",
            "Двадцятиповерховий токсичний водоспад із смердючого бруду, що спускається з "
            "Доптауна до Раковини. Перевірка Сили для спуску без спорядження. Старий Хунглун "
            "на ім'я Отто продає знайдене спорядження за повний балон О2 або 2 ккр. За 500 кр "
            "Отто намалює карту шляху до Лікаря. 5% шанс, що спорядження несправне.",
        ),
    },
    344: {
        "en": (
            "The Doctor",
            "Hidden beneath the toxic sludge falls runs a pulsating tunnel with walls ridged "
            "like a metal gullet. At the far end is a disquieting makeshift operating theater "
            "built entirely from reaped limbs. Dr. Bancali, a young and driven surgeon, works "
            "feverishly here.\n\n"
            "DR. BANCALI: COMBAT 65 (Scalpel 1d10dmg + Infection Save) | SPEED 75 | INSTINCT 65 | HITS 2 (20)\n"
            "Singly devoted to curing Ariel of her terminal illness. The last scrap of Caliban's "
            "sanity. Unaware of the ACMD outbreak he is causing.\n\n"
            "Bancali will install cybernetic \"gills\" that remove the need to breathe oxygen if "
            "asked. If Bancali is killed, Caliban loses control — advance to Outbreak Phase 3.",
        ),
        "ru": (
            "Доктор",
            "За токсическим водопадом из зловонной жижи тянется пульсирующий тоннель со стенами, "
            "изрытыми, словно металлическое горло. В конце — жутковатый самодельный операционный "
            "зал, построенный целиком из ампутированных конечностей. Здесь лихорадочно работает "
            "доктор Банкали — молодой и целеустремлённый хирург.\n\n"
            "ДОКТОР БАНКАЛИ: БОЙ 65 (Скальпель 1d10 урона + Проверка заражения) | СКОРОСТЬ 75 | "
            "ИНСТИНКТ 65 | ОЗ 2 (20)\n"
            "Целиком посвящён лечению Ариэль. Последняя крупица разума Калибана. Не знает о "
            "вспышке ACMD, которую сам же вызывает.\n\n"
            "Банкали вживит кибернетические «жабры», избавляющие от необходимости дышать "
            "кислородом. Если Банкали погибнет, Калибан потеряет контроль — Вспышка, Фаза 3.",
        ),
        "ua": (
            "Лікар",
            "За токсичним водоспадом бруду тягнеться пульсуючий тунель зі стінами, схожими на "
            "металеве горло. В кінці — моторошний саморобний операційний зал, збудований "
            "повністю з ампутованих кінцівок. Тут лихоманково працює доктор Банкалі — молодий "
            "і цілеспрямований хірург.\n\n"
            "ДОКТОР БАНКАЛІ: БІЙ 65 (Скальпель 1d10 шкоди + Перевірка зараження) | ШВИДКІСТЬ 75 | "
            "ІНСТИНКТ 65 | ОЗ 2 (20)\n"
            "Цілком присвячений лікуванню Аріель. Остання крупиця розуму Калібана. Не знає про "
            "спалах ACMD, який сам же спричиняє.\n\n"
            "Банкалі вживить кібернетичні «зябра», що знімають потребу дихати киснем. "
            "Якщо Банкалі загине, Калібан втратить контроль — Спалах, Фаза 3.",
        ),
    },
    345: {
        "en": (
            "The Old City",
            "Massive, sunken and abandoned city. Collapsing buildings (1d5×10 stories). Raw "
            "sewage. Chokespawn stalk the darkness. Dimly lit through cracks in the ceiling a "
            "hundred stories above. Notable landmarks, each about an hour apart:\n\n"
            "» JUNO TOWER. Former corporate HQ. 34 floors above the waste, 4 sunken below. "
            "Sadistic Tempest Co. Sniper [C:75 Smart Rifle 1d10dmg S:25 I:55 H:2] perched near "
            "the top, picking off travelers for sport.\n"
            "» THE METRO. Dark descent down three creaking stairwells into abandoned Metro tunnels. "
            "Power can be temporarily restored with a Jury Rigging or Engineering Check — opens "
            "fast travel to The Veins or Mass Grave.\n"
            "» THE OUTPOST. Tempest Co. Forward Operating Base in a crumbling apartment building. "
            "1d5 Paranoid Operators [C:25 SMG 4d10dmg I:25 H:2].\n"
            "» THE SEWERS. 100' drop in cracked pavement. Leads to Mass Grave and The Burrows. "
            "Roll for encounters twice per hour.\n"
            "» (HARD TO FIND) THE ARCHIVES. Decayed corporate research facility. Patient records "
            "reveal that Dr. Bancali and his daughter Ariel came to The Dream 23 years ago to "
            "cure her terminal cancer.",
        ),
        "ru": (
            "Старый Город",
            "Огромный затопленный и заброшенный город. Рушащиеся здания (1d5×10 этажей). "
            "Нечистоты. В темноте рыщут Споры Удавки. Скудное освещение сквозь трещины в "
            "потолке в сотне этажей над головой. Важные ориентиры, каждый в часе ходьбы:\n\n"
            "» БАШНЯ ЮНОНЫ. Бывший корпоративный штаб. 34 этажа над отходами, 4 под землёй. "
            "Садистский снайпер Tempest Co. [Б:75 Умная Винтовка 1d10 урона С:25 И:55 ОЗ:2] "
            "засел у верхушки — снимает путников ради забавы.\n"
            "» МЕТРО. Тёмный спуск по трём скрипучим лестничным пролётам в заброшенные тоннели. "
            "Питание можно временно восстановить проверкой Самоделки или Инженерного дела — "
            "открывает быстрый маршрут к Венам или Братской Могиле.\n"
            "» АВАНПОСТ. Передовая база Tempest Co. в рушащемся жилом доме. "
            "1d5 Параноидальных Операторов [Б:25 ПП 4d10 урона И:25 ОЗ:2].\n"
            "» КАНАЛИЗАЦИЯ. 30-метровый провал в растрескавшемся асфальте. Ведёт к Братской "
            "Могиле и Норам. Проверять встречи дважды в час.\n"
            "» (ТРУДНО НАЙТИ) АРХИВЫ. Обветшалый корпоративный исследовательский центр. Записи "
            "пациентов раскрывают: доктор Банкали и его дочь Ариэль прибыли на «Мечту» 23 года "
            "назад, чтобы вылечить её терминальный рак.",
        ),
        "ua": (
            "Старе Місто",
            "Величезне затоплене й покинуте місто. Будівлі, що руйнуються (1d5×10 поверхів). "
            "Нечистоти. У темряві рискають Споки Задуші. Тьмяне освітлення крізь тріщини в "
            "стелі за сто поверхів нагорі. Важливі орієнтири, кожен за годину ходьби:\n\n"
            "» ВЕЖА ЮНОНИ. Колишній корпоративний штаб. 34 поверхи над відходами, 4 під землею. "
            "Садистський снайпер Tempest Co. [Б:75 Розумна Гвинтівка 1d10 шкоди Ш:25 І:55 ОЗ:2] "
            "засів біля верхівки — знімає мандрівників заради забави.\n"
            "» МЕТРО. Темний спуск трьома скрипучими сходовими прольотами в покинуті тунелі. "
            "Живлення можна тимчасово відновити перевіркою Саморобки або Інженерної справи — "
            "відкриває швидкий маршрут до Вен або Братської Могили.\n"
            "» АВАНПОСТ. Передова база Tempest Co. у будинку, що розвалюється. "
            "1d5 Параноїдальних Операторів [Б:25 ПП 4d10 шкоди І:25 ОЗ:2].\n"
            "» КАНАЛІЗАЦІЯ. 30-метровий провал у розтрісканому асфальті. Веде до Братської "
            "Могили та Нір. Перевіряти зустрічі двічі на годину.\n"
            "» (ВАЖКО ЗНАЙТИ) АРХІВИ. Занедбаний корпоративний дослідницький центр. Записи "
            "пацієнтів розкривають: доктор Банкалі та його донька Аріель прибули на «Мрію» "
            "23 роки тому, щоб вилікувати її термінальний рак.",
        ),
    },
    346: {
        "en": (
            "Mass Grave",
            "A lonely sign reads: \"Even if you cannot breathe, you don't deserve to die here. "
            "Come back home.\" Beyond it: a one-story-high pile of corpses, reaped limbs, and "
            "discarded Husks. What remains of more than a decade of Caliban's monstrous "
            "experiments. Fear Save or gain 1d5 Stress upon locating the Grave.\n\n"
            "25% chance that if an hour is spent searching, one random cybermod is found "
            "discarded here. Installing it incurs two rolls on the Mutation Table and gives "
            "permanent [-] on Saves to resist Caliban if he awakens.",
        ),
        "ru": (
            "Братская Могила",
            "У одинокой таблички написано: «Даже если ты не можешь дышать, ты не заслуживаешь "
            "умереть здесь. Возвращайся домой.» За ней — куча трупов, ампутированных конечностей "
            "и выброшенных Оболочек ростом в этаж. Всё, что осталось от более чем десяти лет "
            "чудовищных экспериментов Калибана. Проверка Страха или 1d5 Стресса при обнаружении "
            "Могилы.\n\n"
            "25% шанс, что при часовом обыске найдётся один случайный кибермод. Его установка "
            "влечёт два броска по Таблице Мутаций и постоянный штраф [-] на Спасброски против "
            "пробуждения Калибана.",
        ),
        "ua": (
            "Братська Могила",
            "Самотній напис: «Навіть якщо ти не можеш дихати, ти не заслуговуєш вмирати тут. "
            "Повернись додому.» За ним — купа трупів, відрізаних кінцівок та викинутих Оболонок "
            "заввишки з поверх. Все, що залишилось від понад десяти років моторошних "
            "експериментів Калібана. Перевірка Страху або 1d5 Стресу при виявленні Могили.\n\n"
            "25% шанс, що при годинному обшуку знайдеться один випадковий кіберімплант. "
            "Його встановлення призводить до двох кидків по Таблиці Мутацій і постійного "
            "штрафу [-] на Рятівні кидки проти пробудження Калібана.",
        ),
    },
    347: {
        "en": (
            "The Veins",
            "A series of drainage pipes, ventilation shafts, and maintenance tunnels leading "
            "all over The Dream. Any module can be accessed if you know the way. The tunnels "
            "are marked by symbols that Imogene Kane and the Hunglungs can easily decipher, "
            "allowing them to strike any part of The Dream and retreat to the relative safety "
            "of The Choke. They are unaware that Caliban is the originator of these symbols.\n\n"
            "It takes 2d10 hours to follow any of these veins back to a module (roll randomly "
            "on the Inside Front Cover to see where you appear). Once a route is established "
            "it can be traversed again if detailed notes are kept.",
        ),
        "ru": (
            "Вены",
            "Сеть дренажных труб, вентиляционных шахт и технических тоннелей, ведущих по всей "
            "«Мечте». Можно добраться до любого модуля, если знаешь путь. Тоннели помечены "
            "символами, которые Имоджен Кейн и Хунглуны легко разбирают — это позволяет им "
            "наносить удары по любой части «Мечты» и отступать в относительную безопасность "
            "Удавки. Они не знают, что символы созданы Калибаном.\n\n"
            "Добраться по Венам до любого модуля занимает 2d10 часов (бросьте кубик по "
            "Внутренней Обложке для определения места появления). Если маршрут уже проложен "
            "и записан, по нему можно пройти снова.",
        ),
        "ua": (
            "Вени",
            "Мережа дренажних труб, вентиляційних шахт і технічних тунелів, що ведуть по всій "
            "«Мрії». До будь-якого модуля можна дістатися, якщо знаєш шлях. Тунелі позначені "
            "символами, які Імоджен Кейн і Хунглуни легко розшифровують — це дозволяє їм "
            "завдавати удари по будь-якій частині «Мрії» та відступати у відносну безпеку "
            "Задуші. Вони не знають, що символи створив Калібан.\n\n"
            "Добратися по Венах до будь-якого модуля займає 2d10 годин (кидайте кубик по "
            "Внутрішній Обкладинці для визначення місця появи). Якщо маршрут уже прокладено "
            "і записано, ним можна скористатися знову.",
        ),
    },
}

# Forward links for new items: (from, to, sort_order)
NEW_CHOKE_LINKS = [
    (247, 343, 6),   # The Choke → The Falls
    (247, 344, 7),   # The Choke → The Doctor
    (247, 346, 8),   # The Choke → Mass Grave
    (247, 347, 9),   # The Choke → The Veins
]

NEW_SINK_LINKS = [
    (248, 343, 0),   # The Sink → The Falls
    (248, 344, 1),   # The Sink → The Doctor
    (248, 345, 2),   # The Sink → The Old City
    (248, 346, 3),   # The Sink → Mass Grave
    (248, 347, 4),   # The Sink → The Veins
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — C248–C253 moved under C247; 5 new Choke/Sink sub-locations added (C343–C347).")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    # 1. Remove C248–C253 from P36 direct page_contents
    ph = ",".join("?" * len(REMOVE_FROM_P36))
    conn.execute(
        f"DELETE FROM page_contents WHERE page_id = 36 AND content_id IN ({ph})",
        REMOVE_FROM_P36,
    )

    # 2. Add forward links from C247 to existing sub-items
    for from_id, to_id, sort in CHOKE_EXISTING_LINKS:
        conn.execute(
            "INSERT OR IGNORE INTO content_links "
            "(from_content_id, to_content_id, label_key, sort_order) VALUES (?, ?, 'related', ?)",
            (from_id, to_id, sort),
        )
    # C247 → C248 is see_also (the main sub-zone)
    conn.execute(
        "UPDATE content_links SET label_key = 'see_also' "
        "WHERE from_content_id = 247 AND to_content_id = 248"
    )

    # 3. Insert new content items
    for cid, icon, source_slug in NEW_CONTENTS:
        conn.execute(
            "INSERT OR IGNORE INTO contents (id, icon, source_slug) VALUES (?, ?, ?)",
            (cid, icon, source_slug),
        )

    # 4. Insert i18n for new items
    for cid, langs in NEW_I18N.items():
        for lang, (name, desc) in langs.items():
            conn.execute(
                "INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc) "
                "VALUES (?, ?, ?, ?)",
                (cid, lang, name, desc),
            )

    # 5. Forward links from C247 to new items
    for from_id, to_id, sort in NEW_CHOKE_LINKS:
        conn.execute(
            "INSERT OR IGNORE INTO content_links "
            "(from_content_id, to_content_id, label_key, sort_order) VALUES (?, ?, 'related', ?)",
            (from_id, to_id, sort),
        )

    # 6. Forward links from C248 (The Sink) to its sub-locations
    for from_id, to_id, sort in NEW_SINK_LINKS:
        conn.execute(
            "INSERT OR IGNORE INTO content_links "
            "(from_content_id, to_content_id, label_key, sort_order) VALUES (?, ?, 'related', ?)",
            (from_id, to_id, sort),
        )


if __name__ == "__main__":
    run()
