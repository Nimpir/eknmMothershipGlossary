"""
scripts/add_apof_cybermods.py
A Pound of Flesh — P37 Cybermod Rules (C254-C258), P39 Cyberware (C259-C286),
P40 Slickware (C287-C295).
Run after add_apof_source_pages.py.
Run: python scripts/add_apof_cybermods.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── Helper ─────────────────────────────────────────────────────────────────────

def _ins(conn, page_id, cid, icon, slug, sort_order,
         name_en, name_ru, name_ua,
         desc_en, desc_ru, desc_ua,
         dice_sides=None, dice_en=None, dice_ru=None, dice_ua=None,
         subinfo=None):
    dice_json = json.dumps({"sides": dice_sides}) if dice_sides else None
    subinfo_json = json.dumps(subinfo) if subinfo else None
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, subinfo_fixed, sort_order)
        VALUES (?, ?, 'apof', NULL, ?, ?, ?)
    """, (cid, icon, dice_json, subinfo_json, sort_order))
    for lang, name, desc, entries in [
        ("en", name_en, desc_en, dice_en),
        ("ru", name_ru, desc_ru, dice_ru),
        ("ua", name_ua, desc_ua, dice_ua),
    ]:
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (?, ?, ?, ?, ?)
        """, (cid, lang, name, desc, json.dumps(entries) if entries else None))
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (?, ?, ?)
    """, (page_id, cid, sort_order))


# ── P37 CYBERMOD RULES ─────────────────────────────────────────────────────────

def _seed_p37_rules(conn):
    P = 37

    # C254 — Installation Rules
    _ins(conn, P, 254, "📋", "apof_cybermod_install", 1,
        "Installation Rules",
        "Правила установки",
        "Правила встановлення",
        (
            "CYBERWARE: Install at a professional cybersurgeon (e.g. The Chop Shop). "
            "Body Save at [+]. Failure: mod installed but Xd10dmg (X = slots) + 1 Malfunction. "
            "Critical Failure: body rejects implant + roll Mutation + Panic Check. "
            "Critical Success: –1d10 Stress.\n\n"
            "SLICKWARE: Install at a professional Slickbay (e.g. The Ice Box). "
            "Sanity Save at [+]. Failure: installed but Intellect –X (X = slots). "
            "Critical Failure: Sanity –X + Malfunction + Panic Check. "
            "Critical Success: –1d10 Stress.\n\n"
            "AMATEUR: [-] on Save; add installer's relevant Skill to patient's Save.\n\n"
            "RECOVERY: 1 day/slot installed (×2 for amateur). All actions at [-] during recovery.\n\n"
            "SLOTS: Cyberware = 1 slot per 10 STR (rounded down). "
            "Slickware = 1 slot per 10 INT (rounded down; requires Slicksocket).\n\n"
            "CUSTOM MODS: Any weapon, armor, or equipment at 10× base cost. "
            "Armor: 1 slot per 5 Armor Save (rounded up). Handgun: 1 slot. Rifle: 2 slots. Larger: 3+."
        ),
        (
            "КИБЕРНЕТИКА: Установка у профессионального хирурга (напр. Чоп-шоп). "
            "Спасбросок Тела [+]. Провал: мод установлен, но Xd10 урона (X = слоты) + 1 Неисправность. "
            "Критический провал: тело отвергает имплант + Мутация + Паника-чек. "
            "Критический успех: –1d10 Стресса.\n\n"
            "СЛИК-ПО: Установка в профессиональном Слик-бэе (напр. Ледяной ящик). "
            "Спасбросок Рассудка [+]. Провал: установлен, но Интеллект –X (X = слоты). "
            "Критический провал: Рассудок –X + Неисправность + Паника-чек. "
            "Критический успех: –1d10 Стресса.\n\n"
            "ЛЮБИТЕЛЬСКАЯ УСТАНОВКА: [-] на Спасбросок; добавить навык установщика.\n\n"
            "ВОССТАНОВЛЕНИЕ: 1 день/слот (×2 для любителей). Все действия с [-].\n\n"
            "СЛОТЫ: Кибернетика = 1 слот на каждые 10 СИЛ. "
            "Слик-ПО = 1 слот на каждые 10 ИНТ (требуется Слик-разъём).\n\n"
            "КАСТОМНЫЕ МОДЫ: Любое оружие/броня/снаряжение за 10× базовую стоимость. "
            "Броня: 1 слот на 5 Брони (округл. вверх). Пистолет: 1 слот. Винтовка: 2. Крупнее: 3+."
        ),
        (
            "КІБЕРНІКА: Встановлення у професійного кіберхірурга (напр. Чоп-шоп). "
            "Рятівний кидок Тіла [+]. Провал: мод встановлено, але Xd10 шкоди (X = слоти) + 1 Несправність. "
            "Критичний провал: тіло відкидає імплант + Мутація + Перевірка Паніки. "
            "Критичний успіх: –1d10 Стресу.\n\n"
            "СЛІК-ПЗ: Встановлення у професійному Слік-бей (напр. Крижаний ящик). "
            "Рятівний кидок Розуму [+]. Провал: встановлено, але Інтелект –X (X = слоти). "
            "Критичний провал: Розум –X + Несправність + Перевірка Паніки. "
            "Критичний успіх: –1d10 Стресу.\n\n"
            "АМАТОРСЬКА УСТАНОВКА: [-] на Рятівний кидок; додати навик установника.\n\n"
            "ВІДНОВЛЕННЯ: 1 день/слот (×2 для аматорів). Усі дії з [-].\n\n"
            "СЛОТИ: Кібернетика = 1 слот на кожні 10 СИЛ. "
            "Слік-ПЗ = 1 слот на кожні 10 ІНТ (потрібен Слік-роз'єм).\n\n"
            "КАСТОМНІ МОДИ: Будь-яка зброя/броня/спорядження за 10× базову вартість. "
            "Броня: 1 слот на 5 Броні (округл. вгору). Пістолет: 1 слот. Гвинтівка: 2. Більше: 3+."
        ),
    )

    # C255 — Malfunctions (d100, 12 range entries)
    _ins(conn, P, 255, "⚠️", "apof_cybermod_malfunctions", 2,
        "Cybermod Malfunctions",
        "Неисправности кибермодов",
        "Несправності кібермодів",
        "Roll d100 when a malfunction occurs.",
        "Бросьте d100 при возникновении неисправности.",
        "Киньте d100 при виникненні несправності.",
        100,
        [
            "00-14: Loud. Squeaks, rings or hums near-constantly. Stealth difficult. +1 min. Stress.",
            "15-29: Ghastly. People are unnerved to have you around and stare. +2 min. Stress.",
            "30-44: Irritating. Itches, twitches, chills. Stress reduction halved.",
            "45-59: Painful. Constant chronic pain. All Healing halved.",
            "60-74: Sickly. Body doesn't play well with the mod. Body Save –1d10.",
            "75-89: Fragile. On Critical Fail Armor Save the mod breaks. Costs 10% base to repair.",
            "90: Knockoff. Effect of the mod is halved.",
            "91: Complicated. Come back for another session; pay 25% base price to finish.",
            "92: Finicky. Requires monthly repairs. 1d100cr.",
            "93: Poor Fit. The mod takes up one more slot than it should.",
            "94: Traumatizing. Overwhelms mental capacity. Forget a random Skill.",
            "95: Interference. Causes static with electronics within 10m.",
            "96: Underpowered. Requires a permanent 1-slot battery pack (2kcr).",
            "97: Poorly Designed. Permanently breaks in 2d10 days.",
            "98: Mutation. Roll a Random Mutation (Back Cover).",
            "99: Lemon. Roll twice and combine.",
        ],
        [
            "00-14: Громкий. Постоянно пищит, звенит или гудит. Стелс затруднён. +1 мин. Стресс.",
            "15-29: Жуткий. Люди нервничают рядом и смотрят на вас. +2 мин. Стресс.",
            "30-44: Раздражающий. Зуд, подёргивания, мурашки. Снижение Стресса вдвое.",
            "45-59: Болезненный. Хроническая боль. Всё лечение вдвое медленнее.",
            "60-74: Болезненный. Тело плохо принимает мод. Спасбросок Тела –1d10.",
            "75-89: Хрупкий. При крит. провале Броска Брони мод ломается. Ремонт 10% от стоимости.",
            "90: Подделка. Эффект мода вдвое слабее.",
            "91: Сложный. Нужен ещё один сеанс; заплатить 25% базовой цены.",
            "92: Капризный. Требует ежемесячного ремонта. 1d100кр.",
            "93: Неудобный. Мод занимает на 1 слот больше.",
            "94: Травматичный. Перегружает разум. Забыть случайный Навык.",
            "95: Помехи. Создаёт помехи электронике в радиусе 10м.",
            "96: Слабопитающийся. Требует постоянный 1-слотный аккумулятор (2 ккр).",
            "97: Плохой дизайн. Навсегда сломается через 2d10 дней.",
            "98: Мутация. Бросить кубик на Случайную Мутацию.",
            "99: Лимон. Бросить дважды и совместить результаты.",
        ],
        [
            "00-14: Гучний. Постійно скрипить, дзвонить або гуде. Стелс утруднений. +1 хв. Стрес.",
            "15-29: Моторошний. Люди нервують поруч і дивляться на вас. +2 хв. Стрес.",
            "30-44: Дратівливий. Свербіж, посмикування, мурашки. Зниження Стресу вдвічі.",
            "45-59: Болісний. Хронічний біль. Все лікування вдвічі повільніше.",
            "60-74: Хворобливий. Тіло погано приймає мод. Рятівний кидок Тіла –1d10.",
            "75-89: Крихкий. При крит. провалі Кидка Броні мод ламається. Ремонт 10% від вартості.",
            "90: Підробка. Ефект мода вдвічі слабший.",
            "91: Складний. Потрібен ще один сеанс; заплатити 25% базової ціни.",
            "92: Примхливий. Потребує щомісячного ремонту. 1d100 кр.",
            "93: Незручний. Мод займає на 1 слот більше.",
            "94: Травматичний. Перевантажує розум. Забути випадковий Навик.",
            "95: Завади. Створює завади електроніці в радіусі 10м.",
            "96: Маломіцний. Потребує постійний 1-слотний акумулятор (2 ккр).",
            "97: Поганий дизайн. Назавжди зламається через 2d10 днів.",
            "98: Мутація. Кинути кубик на Випадкову Мутацію.",
            "99: Лимон. Кинути двічі і поєднати результати.",
        ],
    )

    # C256 — Cybermod Panic Table
    _ins(conn, P, 256, "😱", "apof_cybermod_panic", 3,
        "Cybermod Panic Table",
        "Таблица паники кибермодов",
        "Таблиця паніки кібермодів",
        "Roll when a Cybermod Panic Check is triggered.",
        "Бросайте при срабатывании Паника-чека кибермода.",
        "Кидайте при спрацюванні Перевірки Паніки кіберімпланту.",
        30,
        [
            "2-3: Endorphin Flood. Reduce 1d5 Stress.",
            "4-5: Biofeedback. Regain 3d10 Health.",
            "6-7: Uplift. Gain a random Skill for 1d10 days.",
            "8-9: Glitch. Pass a Sanity Save or gain 1d5 Stress.",
            "10-11: Out of Batteries. All mods stop working unless hooked to a power source.",
            "12-13: Power Surge. Take Xd10dmg where X = number of slots installed.",
            "14-15: Shutdown. A random mod stops working until repaired.",
            "16-18: Reboot. Forget the last 1d10 days.",
            "19-21: Immune Response. Reduce slots available for mods by 1.",
            "22-24: Overload. Random mod explodes, dealing Xd10dmg (X = mod's slots).",
            "25-27: Mindwipe. Forget a random Skill.",
            "28-29: Loss of Humanity. Fear Saves made in your presence are at [-].",
            "30: I, Robot. In 1d10 rounds the mod takes over; become a machine controlled by the Warden.",
        ],
        [
            "2-3: Поток эндорфинов. Снизить 1d5 Стресса.",
            "4-5: Биообратная связь. Восстановить 3d10 Здоровья.",
            "6-7: Подъём. Получить случайный Навык на 1d10 дней.",
            "8-9: Сбой. Спасбросок Рассудка или +1d5 Стресса.",
            "10-11: Разряд батареи. Все моды отключаются без источника питания.",
            "12-13: Перегрузка мощности. Xd10 урона (X = количество слотов).",
            "14-15: Отключение. Случайный мод перестаёт работать до ремонта.",
            "16-18: Перезагрузка. Забыть последние 1d10 дней.",
            "19-21: Иммунный ответ. Уменьшить доступные слоты для модов на 1.",
            "22-24: Перегрев. Случайный мод взрывается, Xd10 урона (X = слоты мода).",
            "25-27: Стирание памяти. Забыть случайный Навык.",
            "28-29: Утрата человечности. Спасброски Страха в вашем присутствии с [-].",
            "30: Я-Робот. Через 1d10 раундов мод берёт управление; персонаж переходит под контроль Ведущего.",
        ],
        [
            "2-3: Потік ендорфінів. Знизити 1d5 Стресу.",
            "4-5: Біозворотний зв'язок. Відновити 3d10 Здоров'я.",
            "6-7: Підйом. Отримати випадковий Навик на 1d10 днів.",
            "8-9: Збій. Рятівний кидок Розуму або +1d5 Стресу.",
            "10-11: Розряд батареї. Всі моди відключаються без джерела живлення.",
            "12-13: Перевантаження потужності. Xd10 шкоди (X = кількість слотів).",
            "14-15: Вимкнення. Випадковий мод перестає працювати до ремонту.",
            "16-18: Перезавантаження. Забути останні 1d10 днів.",
            "19-21: Імунна відповідь. Зменшити доступні слоти для модів на 1.",
            "22-24: Перегрів. Випадковий мод вибухає, Xd10 шкоди (X = слоти мода).",
            "25-27: Стирання пам'яті. Забути випадковий Навик.",
            "28-29: Втрата людяності. Рятівні кидки Страху у вашій присутності з [-].",
            "30: Я-Робот. Через 1d10 раундів мод бере керування; персонаж переходить під контроль Провідника.",
        ],
    )

    # C257 — Overclocking
    _ins(conn, P, 257, "🔀", "apof_overclocking", 4,
        "Overclocking",
        "Оверклокинг",
        "Оверклокінг",
        (
            "Install more mods than available slots → become Overclocked. "
            "Each mod beyond limit = +1 Overclock Level (cumulative effects below). "
            "Overclocked mods cost 2× and Body Saves during install are at [-].\n\n"
            "OCL 1 — Minimum Stress +2.\n"
            "OCL 2 — Unnerving: gain Android's Panic ability (others get [-] on Fear Saves nearby). "
            "Androids cause +1 Stress whenever they make a Fear Save.\n"
            "OCL 3 — Minimum Stress +6.\n"
            "OCL 4 — Removed: no longer make Fear Saves for deaths, ship crits, others panicking, hopelessness.\n"
            "OCL 5 — Less than Human: the machine is in control. Warden takes over your character."
        ),
        (
            "Установить модов больше, чем есть слотов → стать Оверклокированным. "
            "Каждый мод сверх лимита = +1 Уровень Оверклока (накопительные эффекты ниже). "
            "Оверклокированные моды стоят 2× и Спасброски Тела при установке с [-].\n\n"
            "УО 1 — Минимальный Стресс +2.\n"
            "УО 2 — Пугающий: получить Паническую способность Андроида ([-] на Спасброски Страха рядом). "
            "Андроиды вызывают +1 Стресс при каждом своём Спасброске Страха.\n"
            "УО 3 — Минимальный Стресс +6.\n"
            "УО 4 — Удалено: больше нет Спасбросков Страха за смерти, крит. попадания в корабль, панику других, безнадёжность.\n"
            "УО 5 — Меньше человека: машина в управлении. Ведущий берёт под контроль персонажа."
        ),
        (
            "Встановити модів більше, ніж є слотів → стати Оверклокованим. "
            "Кожен мод понад ліміт = +1 Рівень Оверклоку (накопичувальні ефекти нижче). "
            "Оверклоковані моди коштують 2× і Рятівні кидки Тіла при встановленні з [-].\n\n"
            "РО 1 — Мінімальний Стрес +2.\n"
            "РО 2 — Моторошний: отримати Панічну здатність Андроїда ([-] на Рятівні кидки Страху поруч). "
            "Андроїди спричиняють +1 Стрес при кожному своєму Рятівному кидку Страху.\n"
            "РО 3 — Мінімальний Стрес +6.\n"
            "РО 4 — Видалено: більше немає Рятівних кидків Страху за смерті, крит. влучання у корабель, паніку інших, безнадійність.\n"
            "РО 5 — Менше людини: машина в управлінні. Провідник бере під контроль персонажа."
        ),
    )

    # C258 — Reaping
    _ins(conn, P, 258, "✂️", "apof_reaping", 5,
        "Reaping",
        "Изъятие",
        "Вилучення",
        (
            "Mods can be bought, sold and stolen. Removing ('reaping') a mod from a living, "
            "willing host requires:\n"
            "• Intellect Check (Surgery, Jury Rigging, or Cybernetics) from the reaper.\n"
            "• Body Save from the host.\n\n"
            "Failure of ONE roll: Xd10dmg to host (X = mod's slots) but mod is removed.\n"
            "Failure of BOTH rolls: Xd10dmg and the mod remains attached.\n"
            "Critical Failure on EITHER: Cybermod Panic Check.\n\n"
            "Unless extreme care is taken, only 15% chance that a combat-killed person "
            "has reapable mods."
        ),
        (
            "Моды можно купить, продать и украсть. Изъять мод из живого согласного хозяина требует:\n"
            "• Проверки Интеллекта (Хирургия, Импровизация, Кибернетика) изымающего.\n"
            "• Спасброска Тела от носителя.\n\n"
            "Провал ОДНОГО броска: Xd10 урона носителю (X = слоты мода), мод изъят.\n"
            "Провал ОБОИХ: Xd10 урона, мод остаётся.\n"
            "Критический провал ЛЮБОГО: Паника-чек кибермода.\n\n"
            "Без особых мер предосторожности только 15% шанс найти реапабельные моды у убитого в бою."
        ),
        (
            "Моди можна купити, продати і вкрасти. Вилучити мод із живого згодного господаря потребує:\n"
            "• Перевірки Інтелекту (Хірургія, Імпровізація, Кібернетика) того, хто вилучає.\n"
            "• Рятівного кидка Тіла від носія.\n\n"
            "Провал ОДНОГО кидка: Xd10 шкоди носію (X = слоти мода), мод вилучено.\n"
            "Провал ОБОХ: Xd10 шкоди, мод залишається.\n"
            "Критичний провал БУДЬ-ЯКОГО: Перевірка Паніки кіберімпланту.\n\n"
            "Без особливих заходів лише 15% шанс знайти придатні для вилучення моди у вбитого в бою."
        ),
    )


# ── P39 CYBERWARE ──────────────────────────────────────────────────────────────

# (cid, icon, slug, sort_order, name_en, name_ru, name_ua, desc_en, desc_ru, desc_ua, cost, slots, requires)
CYBERWARE = [
    (259, "🔄", "apof_cw_big_switch", 1,
     "Big Switch", "Большой переключатель", "Великий перемикач",
     "Allows the user to change their primary sexual characteristics. Takes 1 week and a mental trigger.",
     "Позволяет изменить первичные половые признаки. Занимает 1 неделю и ментальный триггер.",
     "Дозволяє змінити первинні статеві ознаки. Займає 1 тиждень і ментальний тригер.",
     "18,000cr", "1", ""),
    (260, "🧠", "apof_cw_black_box", 2,
     "Black Box", "Чёрный ящик", "Чорна скринька",
     "Eidetic memory backup. Memories watchable via OGRE or projected with Holoprojector. "
     "Only saves memories from installation onward. Also stores uploaded data and Slickware.",
     "Резервная копия эйдетической памяти. Можно просматривать через ОГРЭ или Голопроектор. "
     "Сохраняет воспоминания с момента установки. Также хранит загруженные данные и Слик-ПО.",
     "Резервна копія ейдетичної пам'яті. Можна переглядати через ОГРЕ або Голопроектор. "
     "Зберігає спогади з моменту встановлення. Також зберігає завантажені дані та Слік-ПЗ.",
     "10,000cr", "3", "Slicksocket"),
    (261, "👻", "apof_cw_cloakskin", 3,
     "Cloakskin", "Маскировочная кожа", "Маскувальна шкіра",
     "Near-invisibility for 5 minutes once per day. If Critically Hit during use, 30% chance condition becomes permanent.",
     "Почти невидимость на 5 минут раз в день. При крит. попадании во время использования — 30% шанс постоянного эффекта.",
     "Майже невидимість на 5 хвилин раз на день. При крит. влученні під час використання — 30% шанс постійного ефекту.",
     "200,000cr", "2", ""),
    (262, "💀", "apof_cw_deadswitch", 4,
     "Deadswitch", "Дэдсвитч", "Дедсвітч",
     "Feigns death for 2 weeks. Each use adds cumulative 5% chance the condition is permanent.",
     "Симулирует смерть на 2 недели. Каждое использование добавляет накопительный 5% шанс постоянства.",
     "Симулює смерть на 2 тижні. Кожне використання додає накопичувальний 5% шанс постійності.",
     "1,000cr", "1", "Black Box"),
    (263, "🦷", "apof_cw_fangs", 5,
     "Fangs", "Клыки", "Ікла",
     "Hollow cybernetic fangs. 2d10dmg. Can store up to 3 doses of poison, medicine or any other drug.",
     "Полые кибернетические клыки. 2d10 урона. Хранят до 3 доз яда, лекарства или другого препарата.",
     "Порожні кібернетичні ікла. 2d10 шкоди. Зберігають до 3 доз отрути, ліків або іншого препарату.",
     "30,000cr", "1", ""),
    (264, "🔫", "apof_cw_handcannon", 6,
     "Handcannon", "Пушка-рука", "Рука-гармата",
     "Conceals a weapon inside a prosthetic limb. Slots and cost based on weapon used.",
     "Прячет оружие внутри протеза конечности. Слоты и стоимость зависят от оружия.",
     "Ховає зброю всередині протеза кінцівки. Слоти та вартість залежать від зброї.",
     "55,000cr+weapon", "Varies*", "Prosthetic"),
    (265, "📽️", "apof_cw_holoprojector", 7,
     "Holoprojector", "Голопроектор", "Голопроектор",
     "Holographically project stored data (from OGRE, Body Cam, Black Box, Slicksocket, etc.).",
     "Голографически проецирует сохранённые данные (из ОГРЭ, камеры тела, Чёрного ящика, Слик-разъёма и т.д.).",
     "Голографічно проектує збережені дані (з ОГРЕ, камери тіла, Чорної скриньки, Слік-роз'єму тощо).",
     "750cr", "1", "OGRE"),
    (266, "🔀", "apof_cw_hotswap", 8,
     "Hotswap", "Хотсвап", "Хотсвап",
     "Allows 1-turn changing of cyberware.",
     "Позволяет менять кибернетику за 1 раунд.",
     "Дозволяє змінювати кібернетику за 1 раунд.",
     "1,000cr", "0", ""),
    (267, "🎯", "apof_cw_huntershot", 9,
     "Huntershot", "Хантершот", "Хантершот",
     "Holds 1 dart which can be fired on command, upon death or unconsciousness. 1d10dmg.",
     "Хранит 1 дротик, который стреляет по команде, при смерти или потере сознания. 1d10 урона.",
     "Зберігає 1 дротик, що стріляє за командою, при смерті або непритомності. 1d10 шкоди.",
     "4,500cr", "1", "OGRE"),
    (268, "💄", "apof_cw_little_switch", 10,
     "Little Switch", "Малый переключатель", "Малий перемикач",
     "Allows the user to smooth or roughen their appearance. Takes 1 day and a mental trigger.",
     "Позволяет сгладить или огрубить внешность. Занимает 1 день и ментальный триггер.",
     "Дозволяє згладити або погрубити зовнішність. Займає 1 день і ментальний тригер.",
     "8,000cr", "1", ""),
    (269, "📢", "apof_cw_loudmouth", 11,
     "Loudmouth", "Громкоговоритель", "Гучномовець",
     "Records and plays back audio. Maximum volume equivalent to a flashbang.",
     "Записывает и воспроизводит звук. Максимальная громкость — как у флэшбэнга.",
     "Записує і відтворює звук. Максимальна гучність — як у флешбенга.",
     "5,500cr", "1", ""),
    (270, "🎨", "apof_cw_lumatat", 12,
     "Lumatat", "Люматат", "Люматат",
     "Cosmetic, color-changing, animated or luminescent tattoos.",
     "Косметические, меняющие цвет, анимированные или светящиеся татуировки.",
     "Косметичні, кольоромінні, анімовані або люмінесцентні татуювання.",
     "200cr+", "0", ""),
    (271, "👁️", "apof_cw_ogre", 13,
     "OGRE", "ОГРЭ", "ОГРЕ",
     "Ocular Graphic Rendering Engine. A Heads-Up Display implanted in your optical nerve, "
     "projecting directly into your field of vision.",
     "Оптический графический движок рендеринга. Дисплей HUD, имплантированный в зрительный нерв.",
     "Оптичний графічний двигун рендеринга. HUD-дисплей, вживлений у зоровий нерв.",
     "32,000cr", "2", ""),
    (272, "💣", "apof_cw_panic_button", 14,
     "Panic Button", "Кнопка паники", "Кнопка паніки",
     "On trigger (or upon death) violently detonates hidden explosives: 1d10dmg to all within 20m "
     "who fail a Body Save. 5% auto-trigger chance on unconsciousness.",
     "При активации (или смерти) взрывает скрытую взрывчатку: 1d10 урона всем в 20м при провале Спасброска Тела. "
     "5% шанс автоматического срабатывания при потере сознания.",
     "При активації (або смерті) підриває приховану вибухівку: 1d10 шкоди всім у 20м при провалі Рятівного кидка Тіла. "
     "5% шанс автоматичного спрацювання при непритомності.",
     "10,000cr", "1", ""),
    (273, "🚀", "apof_cw_panzerfist", 15,
     "Panzerfist", "Панцерфист", "Панцерфіст",
     "Ship's autocannon hidden inside a prosthetic. 2d10 MDMG. Holds 2 shots. "
     "Range: Short 50m, Med 100m, Long 400m. Without a Spinal Rig: Body Save [-] or flung 2d10m back. "
     "Takes 2 rounds to fire.",
     "Автопушка корабля в протезе. 2d10 МУРОНА. 2 выстрела. "
     "Дальность: ближняя 50м, средняя 100м, дальняя 400м. Без Спинального Крепежа: Спасбросок Тела [-] или отброс на 2d10м.",
     "Автогармата корабля у протезі. 2d10 МШКОДА. 2 постріли. "
     "Дальність: ближня 50м, середня 100м, далека 400м. Без Хребтового Кріплення: Рятівний кидок Тіла [-] або відкидання на 2d10м.",
     "15,000,000cr", "4", "Prosthetic"),
    (274, "🦾", "apof_cw_prosthetic", 16,
     "Prosthetic", "Протез", "Протез",
     "Artificial hand, foot, arm or leg. Prosthetic organs can replace any damaged organ (10× cost).",
     "Искусственная рука, нога, ступня или ступня. Протезные органы заменяют повреждённые (×10 стоимость).",
     "Штучна рука, нога, ступня або кінцівка. Протезні органи замінюють пошкоджені (×10 вартість).",
     "1,000cr", "1", ""),
    (275, "📡", "apof_cw_remote_uplink", 17,
     "Remote Uplink", "Удалённый аплинк", "Дистанційний аплінк",
     "Once per day sends a PDGP-encrypted broadcast of Black Box data to a secure backup site "
     "for future retrieval or re-sleeving. Many services require authorized next-of-kin.",
     "Раз в день отправляет зашифрованный PDGP-бэкап Чёрного ящика на защищённый сервер. "
     "Многие сервисы требуют авторизованного следующего родственника.",
     "Раз на день надсилає зашифрований PDGP-бекап Чорної скриньки на захищений сервер. "
     "Багато сервісів вимагають авторизованого найближчого родича.",
     "550,000cr", "2", "Black Box"),
    (276, "🗡️", "apof_cw_nanoblade", 18,
     "Retractable Nanoblade", "Втяжное наноклинок", "Висувний нанолезо",
     "Retractable 9\" blade which can cut through almost anything. 4d10dmg.",
     "Выдвижной 9\" клинок, режущий почти всё. 4d10 урона.",
     "Висувне 9\" лезо, що ріже майже все. 4d10 шкоди.",
     "105,000cr", "1", "Prosthetic"),
    (277, "⚡", "apof_cw_revenant", 19,
     "Revenant Protocol", "Протокол Ревенант", "Протокол Ревенант",
     "If triggered within 2 rounds of death, allows the user to continue fighting for 2d10 rounds. "
     "If no enemies remain, user attacks random targets.",
     "При активации в течение 2 раундов после смерти позволяет сражаться ещё 2d10 раундов. "
     "Без врагов — атакует случайные цели.",
     "При активації протягом 2 раундів після смерті дозволяє битися ще 2d10 раундів. "
     "Без ворогів — атакує випадкові цілі.",
     "280,000cr", "2", "Black Box"),
    (278, "🛡️", "apof_cw_scapegoat", 20,
     "Scapegoat System", "Система Козла отпущения", "Система Цапа відпущення",
     "Stores kinetic energy (bullets, CQC dmg, etc.) up to 30dmg, which must be redirected via touch "
     "within 2d10 turns or the damage is tripled on the user. 1 week to recharge.",
     "Накапливает кинетическую энергию (пули, ближний бой и т.д.) до 30 урона, которую нужно перенаправить "
     "прикосновением в течение 2d10 ходов. Иначе — тройной урон носителю. Перезарядка 1 неделя.",
     "Накопичує кінетичну енергію (кулі, ближній бій тощо) до 30 шкоди, яку потрібно перенаправити "
     "дотиком протягом 2d10 ходів. Інакше — потрійна шкода носію. Перезарядка 1 тиждень.",
     "130,000cr", "3", ""),
    (279, "🔌", "apof_cw_slicksocket", 21,
     "Slicksocket", "Слик-разъём", "Слік-роз'єм",
     "Cranial input jack which allows Slickware to be installed.",
     "Черепной входной разъём для установки Слик-ПО.",
     "Черепний вхідний роз'єм для встановлення Слік-ПЗ.",
     "1,000cr", "1", ""),
    (280, "🤖", "apof_cw_sockpuppet", 22,
     "Sockpuppet", "Марионетка", "Маріонетка",
     "Allows a weapon installed in the user to fire on its own once per turn at half the user's Combat score.",
     "Позволяет вмонтированному оружию стрелять самостоятельно раз в раунд на половину боевого показателя.",
     "Дозволяє вмонтованій зброї стріляти самостійно раз на раунд на половину бойового показника.",
     "1,000,000cr+weapon", "Varies*", "Spinal Rig, OGRE"),
    (281, "🕷️", "apof_cw_spider_mount", 23,
     "Spider Mount", "Паучье крепление", "Павуче кріплення",
     "Allows up to 2 extra Prosthetics or Hardware to be attached. Can only be installed once.",
     "Позволяет прикрепить до 2 дополнительных Протезов или Оборудования. Устанавливается только один раз.",
     "Дозволяє прикріпити до 2 додаткових Протезів або Обладнання. Встановлюється лише один раз.",
     "250,000cr", "1", "Spinal Rig"),
    (282, "💪", "apof_cw_spinal_rig", 24,
     "Spinal Rig", "Спинальный каркас", "Хребтове кріплення",
     "Mechanical rig for assisted heavy-lifting. +10 Strength (no extra Health). May only be installed once.",
     "Механический каркас для подъёма тяжестей. +10 Силы (без доп. здоровья). Устанавливается только один раз.",
     "Механічний каркас для підйому важкого. +10 Сили (без доп. здоров'я). Встановлюється лише один раз.",
     "150,000cr", "1", ""),
    (283, "🎒", "apof_cw_subdermal_bandolier", 25,
     "Subdermal Bandolier", "Подкожная бандольера", "Підшкірна бандольєра",
     "Internal ammo cavity feeding installed weapons. Capacity: 10 full magazines. "
     "1 Bandolier per ammo type. On Critical Hit: 5% chance it detonates (2d10dmg to user + all within 20m, Body Save).",
     "Внутренняя полость для патронов. Ёмкость: 10 полных магазинов. 1 Бандольера на тип боеприпасов. "
     "При крит. попадании: 5% шанс детонации (2d10 урона носителю и всем в 20м, Спасбросок Тела).",
     "Внутрішня порожнина для патронів. Ємність: 10 повних магазинів. 1 Бандольєра на тип боєприпасів. "
     "При крит. влученні: 5% шанс детонації (2d10 шкоди носію і всім у 20м, Рятівний кидок Тіла).",
     "500cr", "1", ""),
    (284, "🐛", "apof_cw_tattletale", 26,
     "Tattletale", "Стукач", "Стукач",
     "Detachable audio surveillance bug. Traceable up to 100km within a 100m area.",
     "Отсоединяемый аудио-жучок. Отслеживается до 100 км в радиусе 100 м.",
     "Від'ємний аудіо-жучок. Відстежується до 100 км у радіусі 100 м.",
     "2,000cr", "1", "Slicksocket, OGRE"),
    (285, "🖥️", "apof_cw_terminal_jack", 27,
     "Terminal Jack", "Терминальный джек", "Термінальний джек",
     "Port for interfacing with terminals, smartlink weapons and vehicles. "
     "Can download data from linked systems or upload from a Black Box.",
     "Порт для подключения к терминалам, умным оружиям и транспорту. "
     "Скачивает данные или загружает из Чёрного ящика.",
     "Порт для підключення до терміналів, розумної зброї та транспорту. "
     "Завантажує дані або вивантажує з Чорної скриньки.",
     "750cr", "1", ""),
    (286, "💉", "apof_cw_whiplash", 28,
     "Whiplash Injector", "Инжектор Вихлясь", "Ін'єктор Хльост",
     "Automatically heals 1d10 after user hits 0 Health. Takes 1 week to recharge. "
     "Body Save permanently reduced by 1d10 after use.",
     "Автоматически лечит 1d10 при достижении 0 здоровья. Перезарядка 1 неделя. "
     "Спасбросок Тела навсегда снижается на 1d10 после использования.",
     "Автоматично лікує 1d10 при досягненні 0 здоров'я. Перезарядка 1 тиждень. "
     "Рятівний кидок Тіла назавжди знижується на 1d10 після використання.",
     "10,000,000cr", "2", ""),
]


def _make_subinfo(cost: str, slots: str, requires: str) -> list[dict]:
    """Build subinfo_fixed in the canonical list-of-objects format."""
    entries = [
        {"label_key": "cost",  "value": cost,  "type": "cost"},
        {"label_key": "slots", "value": slots, "type": "stat"},
    ]
    if requires:
        entries.append({"label_key": "requires", "value": requires, "type": "stat"})
    return entries


def _seed_p39_cyberware(conn):
    P = 39
    for row in CYBERWARE:
        (cid, icon, slug, sort_order,
         name_en, name_ru, name_ua,
         desc_en, desc_ru, desc_ua,
         cost, slots, requires) = row
        _ins(conn, P, cid, icon, slug, sort_order,
             name_en, name_ru, name_ua,
             desc_en, desc_ru, desc_ua,
             subinfo=_make_subinfo(cost, slots, requires))


# ── P40 SLICKWARE ──────────────────────────────────────────────────────────────

SLICKWARE = [
    (287, "⚡", "apof_sw_god_mode", 1,
     "God Mode", "Режим бога", "Режим бога",
     "[+] on Hacking Checks when jacked into a terminal. Gain 1d5 Stress per use.",
     "[+] на Проверки Взлома при подключении к терминалу. Получить 1d5 Стресса за использование.",
     "[+] на Перевірки Зламу при підключенні до термінала. Отримати 1d5 Стресу за використання.",
     "85,000cr", "2", "Slicksocket, Terminal Jack"),
    (288, "🧨", "apof_sw_espernetic", 2,
     "Espernetic Feedback Loop", "Эспернетическая петля обратной связи", "Еспернетична петля зворотного зв'язку",
     "Psionic attack overloading targeted electronics (Androids, cybernetics, etc.). "
     "Sanity Save [+]: success → deal damage equal to roll; fail → take half damage + 1d5 Stress.",
     "Псионическая атака, перегружающая электронику цели (Андроиды, кибернетика и т.д.). "
     "Спасбросок Рассудка [+]: успех → урон = результат броска; провал → половина урона + 1d5 Стресса.",
     "Псіонічна атака, що перевантажує електроніку цілі (Андроїди, кібернетика тощо). "
     "Рятівний кидок Розуму [+]: успіх → шкода = результат кидка; провал → половина шкоди + 1d5 Стресу.",
     "3,000,000cr", "5", "Slicksocket"),
    (289, "🐾", "apof_sw_holopet", 3,
     "Holopet", "Голопитомец", "Голопет",
     "Projects a medium holographic AI pet within 30m radius. Auto-heal 1 Stress when resting. "
     "Panic Check [-] if the Holopet slickware is ever destroyed.",
     "Проецирует среднего голографического ИИ-питомца в радиусе 30м. "
     "Автолечение 1 Стресса при отдыхе. Паника-чек [-] при уничтожении Голопитомца.",
     "Проектує середнього голографічного ШІ-вихованця у радіусі 30м. "
     "Автолікування 1 Стресу при відпочинку. Перевірка Паніки [-] при знищенні Голопета.",
     "75,000cr", "2", "Slicksocket, Holoprojector"),
    (290, "📻", "apof_sw_looky_loo", 4,
     "Looky-loo", "Подглядыватель", "Підглядач",
     "Picks up transmissions on all non-encrypted bands. Allows audio recording if you have a Black Box.",
     "Перехватывает передачи на всех незашифрованных частотах. Позволяет записывать звук при наличии Чёрного ящика.",
     "Перехоплює передачі на всіх незашифрованих частотах. Дозволяє записувати звук за наявності Чорної скриньки.",
     "550cr", "1", "Slicksocket, Loudmouth"),
    (291, "🤖", "apof_sw_machine_code", 5,
     "Machine Code", "Машинный код", "Машинний код",
     "Converse with powerful AI at a level it finds comfortable. Sanity Save: success → 1 Stress/hour; "
     "fail → 1 Stress/minute.",
     "Общение с мощным ИИ на понятном ему уровне. Спасбросок Рассудка: успех → 1 Стресс/час; провал → 1 Стресс/мин.",
     "Спілкування з потужним ШІ на зрозумілому йому рівні. Рятівний кидок Розуму: успіх → 1 Стрес/год; провал → 1 Стрес/хв.",
     "350,000cr", "4", "Slicksocket, Black Box, Terminal Jack"),
    (292, "💊", "apof_sw_sentinel", 6,
     "Sentinel System", "Система Страж", "Система Вартовий",
     "Doubles effectiveness of Stimpaks, rest and healing. Body Saves for Addiction now at [-].",
     "Удваивает эффективность Стимпаков, отдыха и лечения. Спасброски Тела на Зависимость с [-].",
     "Подвоює ефективність Стимпаків, відпочинку і лікування. Рятівні кидки Тіла на Залежність з [-].",
     "8,500cr", "3", "Slicksocket"),
    (293, "📚", "apof_sw_skillslick", 7,
     "Skillslick", "Скиллслик", "Скіллслік",
     "User gains the purchased Skill for as long as the Skillslick remains installed. "
     "Supply is very limited and closely guarded.\n"
     "• Trained: 50,000cr / 1 slot\n"
     "• Expert: 550,000cr / 2 slots\n"
     "• Master: 4,000,000cr / 3 slots",
     "Пользователь получает купленный Навык, пока Скиллслик установлен. "
     "Ассортимент и запас очень ограничены.\n"
     "• Обученный: 50 000 кр / 1 слот\n"
     "• Эксперт: 550 000 кр / 2 слота\n"
     "• Мастер: 4 000 000 кр / 3 слота",
     "Користувач отримує куплений Навик, поки Скіллслік встановлений. "
     "Асортимент і запас дуже обмежені.\n"
     "• Навчений: 50 000 кр / 1 слот\n"
     "• Експерт: 550 000 кр / 2 слоти\n"
     "• Майстер: 4 000 000 кр / 3 слоти",
     "50,000–4,000,000cr", "1–3", "Slicksocket, OGRE"),
    (294, "🏃", "apof_sw_twitch_booster", 8,
     "Twitch Booster", "Ускоритель рефлексов", "Прискорювач рефлексів",
     "On activation: [+] on Speed Checks for 3 rounds. Deals 2d10dmg to user as nerve endings burn.",
     "При активации: [+] на Броски Скорости 3 раунда. 2d10 урона пользователю — нервы горят.",
     "При активації: [+] на Кидки Швидкості 3 раунди. 2d10 шкоди користувачу — нерви горять.",
     "125,000cr", "3", "Slicksocket"),
    (295, "🎙️", "apof_sw_vox_box", 9,
     "Vox Box", "Голосовой имитатор", "Голосовий імітатор",
     "Perfectly mimics any voice after 10 minutes of speaking to the target. Stores up to 3 voices.",
     "Идеально имитирует любой голос после 10 минут разговора с целью. Хранит до 3 голосов.",
     "Ідеально імітує будь-який голос після 10 хвилин розмови з ціллю. Зберігає до 3 голосів.",
     "25,000cr", "1", "Loudmouth"),
]


def _seed_p40_slickware(conn):
    P = 40
    for row in SLICKWARE:
        (cid, icon, slug, sort_order,
         name_en, name_ru, name_ua,
         desc_en, desc_ru, desc_ua,
         cost, slots, requires) = row
        _ins(conn, P, cid, icon, slug, sort_order,
             name_en, name_ru, name_ua,
             desc_en, desc_ru, desc_ua,
             subinfo=_make_subinfo(cost, slots, requires))


# ── Main ───────────────────────────────────────────────────────────────────────

def _seed(conn: sqlite3.Connection) -> None:
    _seed_p37_rules(conn)
    _seed_p39_cyberware(conn)
    _seed_p40_slickware(conn)


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        n_rules = 5
        n_cw = len(CYBERWARE)
        n_sw = len(SLICKWARE)
        total = n_rules + n_cw + n_sw
        print(
            f"Done — {total} contents added: "
            f"{n_rules} rule pages (P37), "
            f"{n_cw} cyberware items (P39), "
            f"{n_sw} slickware items (P40)."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
