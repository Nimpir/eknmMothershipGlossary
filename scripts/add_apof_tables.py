"""
scripts/add_apof_tables.py
A Pound of Flesh — P38 Tables: encounter tables, establishments, denizens,
living expenses, space station generators (C296-C306).
Run after add_apof_source_pages.py.
Run: python scripts/add_apof_tables.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

PAGE_ID = 38


def _ins(conn, page_id, cid, icon, slug, sort_order,
         name_en, name_ru, name_ua,
         desc_en, desc_ru, desc_ua,
         dice_sides=None, dice_en=None, dice_ru=None, dice_ua=None):
    dice_json = json.dumps({"sides": dice_sides}) if dice_sides else None
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (?, ?, 'apof', NULL, ?, ?)
    """, (cid, icon, dice_json, sort_order))
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


def _seed(conn):

    # ── C296 Encounter Frequency ──────────────────────────────────────────────
    _ins(conn, PAGE_ID, 296, "📊", "apof_encounter_freq", 1,
        "Encounter Frequency",
        "Частота встреч",
        "Частота зустрічей",
        (
            "When passing through a map slice, roll 1d10 and check by Phase.\n"
            "If violence breaks out: 10% chance Tempest Operators [H:2 C:35 Pulse Rifle 5d10dmg I:25] "
            "arrive in 1d10 rounds. Otherwise no help is coming.\n\n"
            "d10  | Phase 1           | Phase 2           | Phase 3\n"
            "1-2  | No encounter      | No encounter      | No encounter\n"
            "3    | No encounter      | No encounter      | Station Encounter\n"
            "4    | No encounter      | Station Encounter | Station Encounter\n"
            "5-6  | Station Encounter | Station Encounter | Deadly Encounter\n"
            "7    | Station Encounter | Deadly Encounter  | Deadly Encounter\n"
            "8-9  | Station Encounter | Deadly Encounter  | Deadly Encounter\n"
            "10   | Deadly Encounter  | Deadly Encounter  | Deadly Encounter\n\n"
            "If the Deadly Encounter doesn't fit with Phase Events completed, "
            "move down the list until you find one that matches."
        ),
        (
            "При переходе через участок карты бросайте 1d10 и проверяйте по Фазе.\n"
            "При вспышке насилия: 10% шанс прибытия Операторов Tempest [H:2 C:35 Пульсовая винтовка 5d10 I:25] "
            "через 1d10 раундов. Иначе помощи не будет.\n\n"
            "d10  | Фаза 1              | Фаза 2              | Фаза 3\n"
            "1-2  | Нет встречи         | Нет встречи         | Нет встречи\n"
            "3    | Нет встречи         | Нет встречи         | Встреча на станции\n"
            "4    | Нет встречи         | Встреча на станции  | Встреча на станции\n"
            "5-6  | Встреча на станции  | Встреча на станции  | Смертельная встреча\n"
            "7    | Встреча на станции  | Смертельная встреча | Смертельная встреча\n"
            "8-9  | Встреча на станции  | Смертельная встреча | Смертельная встреча\n"
            "10   | Смертельная встреча | Смертельная встреча | Смертельная встреча"
        ),
        (
            "При переході через ділянку карти кидайте 1d10 і перевіряйте за Фазою.\n"
            "При спалаху насильства: 10% шанс прибуття Операторів Tempest [H:2 C:35 Імпульсна гвинтівка 5d10 I:25] "
            "через 1d10 раундів. Інакше допомоги не буде.\n\n"
            "d10  | Фаза 1              | Фаза 2              | Фаза 3\n"
            "1-2  | Без зустрічі        | Без зустрічі        | Без зустрічі\n"
            "3    | Без зустрічі        | Без зустрічі        | Зустріч на станції\n"
            "4    | Без зустрічі        | Зустріч на станції  | Зустріч на станції\n"
            "5-6  | Зустріч на станції  | Зустріч на станції  | Смертельна зустріч\n"
            "7    | Зустріч на станції  | Смертельна зустріч  | Смертельна зустріч\n"
            "8-9  | Зустріч на станції  | Смертельна зустріч  | Смертельна зустріч\n"
            "10   | Смертельна зустріч  | Смертельна зустріч  | Смертельна зустріч"
        ),
    )

    # ── C297 Deadly Encounters (d20) ──────────────────────────────────────────
    _ins(conn, PAGE_ID, 297, "💀", "apof_deadly_encounters", 2,
        "Deadly Encounters",
        "Смертельные встречи",
        "Смертельні зустрічі",
        "Phase 1: 1d10. Phase 2: 1d10+5. Phase 3: 1d10+10.",
        "Фаза 1: 1d10. Фаза 2: 1d10+5. Фаза 3: 1d10+10.",
        "Фаза 1: 1d10. Фаза 2: 1d10+5. Фаза 3: 1d10+10.",
        20,
        [
            "Escaped Pit Creature (pg.27). 1d10 Executioners [C:55 Electrolash 4d10dmg H:3] attempting to subdue it.",
            "1d10 Reapers [C:45 S:35 I:35 H:2] looking for parts. Will attempt to capture androids and cybermodded crewmembers.",
            "Fight between 2d10 Teamsters [C:35 Unarmed H:1] and 1d5 Novo Droogs [C:55 Knives 1d10dmg H:1].",
            "Body Save or get pickpocketed for 2d100cr. 1d10 Urchins [C:35 H:1] waiting in ambush if things go wrong.",
            "Ticking in the bulkhead. 2d10 seconds later a pipe bomb explodes. Body Save or 1d10dmg. Armor Save for half.",
            "Aug [C:40 5d10dmg S:30 I:20 H:3] screaming 'Help! It's not me, it's Caliban!' Can't stop attacking.",
            "Sycorax Dealer and 1d10 Novo Droogs [C:55 Shotgun 2d10dmg S:25 I:25 H:2].",
            "Floor warps and swallows you whole. Body Save or fall into The Sink (pg.34). Floor morphs back. If you see it: Sanity Save or 1d5 Stress.",
            "Q-Team [C:25 5d10dmg H:2] escorting 2d10 Infected to The Court (pg.26). Infection Check.",
            "A single confused Husk (pg.21). Doesn't attack unless interfered with.",
            "2d10+10 Teamsters [C:35 Improvised Weapons 1d10 H:1] rioting. Burning down a Novo Front Establishment.",
            "Mandatory Q-Team [C:25 5d10dmg H:2] inspection. Forcibly take your blood and test for Infection.",
            "A fleshy mouth opens in the bulkhead revealing 2 Cybernetic Tongues [Body[-] Save or 5d10dmg/round H:1(30)]. Sanity Save or 1d5 Stress.",
            "Firefight between 2d10 Tempest Operators [C:35 SMG 4d10dmg H:2] and 3d10 Hunglungs [C:35 SMG[-] 4d10dmg[-] H:1].",
            "5d10+10 Teamsters burning and looting. In 1d10 rounds Armored Troopers arrive with tear gas (Body Save or fall prone coughing).",
            "Giant eyeball opens in the wall and follows your movements. Sanity Save or trapped in gaze: 1 Stress/round until Sanity Save succeeds. Closes after 50dmg.",
            "A gnashing mouth opens in the bulkhead and 2d10 Husks (pg.21) stream out.",
            "Massive battle: 1d5 Tempest Squads vs 2d10 Hunglung Insurgent squads. Massive civilian casualties. Area impassable without running the battlefield.",
            "1d5 Tempest Squads fighting 4d10 Chokespawn (pg.35). The Chokespawn are winning.",
            "The Avatar of Caliban (pg.39) marches through corridors flanked by Husks. All with cybermods/slickware: Sanity Save or bow. Fight only if fired upon. Behind them: darkness and static. Fear Save or 1d10 Stress.",
        ],
        [
            "Сбежавшее существо из Ямы (стр.27). 1d10 Палачей [C:55 Электроплеть 4d10 H:3] пытаются усмирить его.",
            "1d10 Мародёров [C:45 S:35 I:35 H:2] в поисках запчастей. Попытаются захватить андроидов и кибермодифицированных.",
            "Драка между 2d10 Тимстерами [C:35 Без оружия H:1] и 1d5 Ново-Дроогами [C:55 Ножи 1d10 H:1].",
            "Спасбросок Тела или ограбят на 2d100 кр. 1d10 Оборванцев [C:35 H:1] в засаде при сопротивлении.",
            "Тиканье в переборке. Через 2d10 секунд взрывается трубная бомба. Спасбросок Тела или 1d10 урона. Броня вдвое.",
            "Авг [C:40 5d10 S:30 I:20 H:3] кричит 'Помогите! Это не я, это Калибан!' Не может прекратить нападать.",
            "Дилер Сикоракса и 1d10 Ново-Дроогов [C:55 Дробовик 2d10 S:25 I:25 H:2].",
            "Пол деформируется и поглощает вас. Спасбросок Тела или упасть в Провал (стр.34). Пол возвращается в норму. Если видели: Спасбросок Рассудка или 1d5 Стресса.",
            "Команда-Q [C:25 5d10 H:2] сопровождает 2d10 Заражённых в Суд (стр.26). Проверка на Заражение.",
            "Одинокий растерянный Хаск (стр.21). Не нападает, если не тревожить.",
            "2d10+10 Тимстеров [C:35 Импровизированное оружие 1d10 H:1] бунтуют. Поджигают заведение Ново Фронт.",
            "Обязательная проверка командой-Q [C:25 5d10 H:2]. Принудительно берут кровь и проверяют на Заражение.",
            "Мясистый рот в переборке — 2 Кибернетических языка [Тело[-] Спасбросок или 5d10/раунд H:1(30)]. Спасбросок Рассудка или 1d5 Стресса.",
            "Перестрелка между 2d10 Операторами Tempest [C:35 SMG 4d10 H:2] и 3d10 Хунглунгами [C:35 SMG[-] 4d10[-] H:1].",
            "5d10+10 Тимстеров грабят и поджигают. Через 1d10 раундов Бронетрупперы со слезоточивым газом.",
            "Гигантский глаз открывается в стене и следит за вами. Спасбросок Рассудка или в оцепенении: 1 Стресс/раунд до успешного броска. Закрывается после 50 урона.",
            "Зубастый рот в переборке — 2d10 Хасков (стр.21) вырываются наружу.",
            "Массовая битва: 1d5 отрядов Tempest против 2d10 отрядов Хунглунгов. Огромные потери среди гражданских.",
            "1d5 отрядов Tempest бьются против 4d10 Чокеспаунов (стр.35). Чокеспауны побеждают.",
            "Аватар Калибана (стр.39) шествует по коридорам в окружении Хасков. Все с кибермодами/слик-ПО: Спасбросок Рассудка или поклонятся. Атакуют только если по ним открыли огонь. Позади: темнота и статика. Спасбросок Страха или 1d10 Стресса.",
        ],
        [
            "Втекла Істота з Ями (стор.27). 1d10 Катів [C:55 Електроплеть 4d10 H:3] намагаються її приборкати.",
            "1d10 Мародерів [C:45 S:35 I:35 H:2] шукають запчастини. Спробують захопити андроїдів і кібермодифікованих.",
            "Бійка між 2d10 Тімстерами [C:35 Без зброї H:1] і 1d5 Ново-Другами [C:55 Ножі 1d10 H:1].",
            "Рятівний кидок Тіла або пограбують на 2d100 кр. 1d10 Безпритульних [C:35 H:1] у засідці при опорі.",
            "Цокання в переборці. Через 2d10 секунд вибухає трубна бомба. Рятівний кидок Тіла або 1d10 шкоди. Броня вдвічі.",
            "Авг [C:40 5d10 S:30 I:20 H:3] кричить 'Допоможіть! Це не я, це Калібан!' Не може зупинитись нападати.",
            "Дилер Сикоракса і 1d10 Ново-Другів [C:55 Дробовик 2d10 S:25 I:25 H:2].",
            "Підлога деформується і поглинає вас. Рятівний кидок Тіла або впасти в Провал (стор.34). Підлога відновлюється. Якщо бачили: Рятівний кидок Розуму або 1d5 Стресу.",
            "Команда-Q [C:25 5d10 H:2] супроводжує 2d10 Заражених до Суду (стор.26). Перевірка на Зараження.",
            "Самотній розгублений Хаск (стор.21). Не нападає, якщо не чіпати.",
            "2d10+10 Тімстерів [C:35 Імпровізована зброя 1d10 H:1] бунтують. Підпалюють заклад Ново Фронт.",
            "Обов'язкова перевірка командою-Q [C:25 5d10 H:2]. Примусово беруть кров і перевіряють на Зараження.",
            "М'ясистий рот у переборці — 2 Кібернетичних язики [Тіло[-] Рятівний кидок або 5d10/раунд H:1(30)]. Рятівний кидок Розуму або 1d5 Стресу.",
            "Перестрілка між 2d10 Операторами Tempest [C:35 SMG 4d10 H:2] і 3d10 Хунглунгами [C:35 SMG[-] 4d10[-] H:1].",
            "5d10+10 Тімстерів грабують і підпалюють. Через 1d10 раундів Бронетрупери зі сльозогінним газом.",
            "Гігантське око відкривається у стіні й стежить за вами. Рятівний кидок Розуму або в заціпенінні: 1 Стрес/раунд до успішного кидка. Закривається після 50 шкоди.",
            "Зубастий рот у переборці — 2d10 Хасків (стор.21) вириваються назовні.",
            "Масова битва: 1d5 загонів Tempest проти 2d10 загонів Хунглунгів. Величезні втрати серед цивільних.",
            "1d5 загонів Tempest б'ються проти 4d10 Чокеспаунів (стор.35). Чокеспауни перемагають.",
            "Аватар Калібана (стор.39) марширує коридорами в оточенні Хасків. Усі з кіберімплантами/слік-ПЗ: Рятівний кидок Розуму або вклоняються. Атакують лише якщо по них відкрили вогонь. Позаду: темрява і статика. Рятівний кидок Страху або 1d10 Стресу.",
        ],
    )

    # ── C298 Station Encounters (d100) ────────────────────────────────────────
    station_en = [
        "Crit (doubles): Roll again and combine two results.",
        "00: Roll Deadly Encounter and combine with another Station Encounter.",
        "01-09: Cryer for random nearby establishment. 10% off if you go right now.",
        "10-19: O2 beggar from The Choke. They need d100 credits or they'll be sent back today. Reduce Stress by 1 if you give.",
        "20-24: Hawker pawning [d10: (1-5) equipment, (6-9) drug, (10) cybermod] for 50% off.",
        "25-29: 1d5 Solarian Missionaries proselytizing. Unbaptized who follow get 1hr in The Solarium.",
        "30-34: Infected denizen [d10: (1-5) coughing, (6-9) vomiting, (10) violently overtaken by cybermods].",
        "35-39: Sex worker from The Ecstasy offering overnights at 75% off.",
        "40-44: Recently let-go Tempest Merc (roll 1d10 for Rank) looking for work at 50% off.",
        "45-49: 1d10 Tempest Recruits [d10: (1-5) on patrol, (6-9) on leave, (10) arresting someone].",
        "50-54: (No entry — reroll.)",
        "55-57: Gamblers playing Sej. d100×1kcr at stake. A crowd is drawing near.",
        "58-60: Q-Team quarantining the area. Go around: adds 1d100[-] minutes to your trip.",
        "61-63: First mate of a ship looking for a crew. Ship leaves in 1d10 hours.",
        "64-66: Backpacker tagging the bulkhead [d10: (1-5) CALIBAN LIVES, (6-9) TAKE MY BREATH AWAY, (10) YAN DEEZ NUTS].",
        "67-69: Gang of 2d10 Novo Droogs squatting at an abandoned establishment.",
        "70-71: Chief Adjudicator Brunhildh and Executioners. All must stop and let them pass or get electrolashed.",
        "72-73: Novo Droogs [C:55 Knives 1d10dmg H:1] beating up 1d10 O2 beggars.",
        "74-75: Android with damaged legs lies in viscous fluids and reaches out for help.",
        "76-77: Dancers from The Stellar Burn gracefully slide by with large holosnakes.",
        "78-79: 1d10 Socialites returning from a Big Switch installation heading to a cybermod showing party.",
        "80-81: Sycorax dealer offering tester vials. 200cr/hit. Body Save or take double damage.",
        "82-83: 2d10 Queer Folx on milkcrates outside a local haunt. Suspicious of strangers and tourists.",
        "84-85: Group of 1d10 dirty urchins tugging on legs and begging for food scraps.",
        "85: 1d5+1 Novo Droogs, drunk and getting kicked out of a nearby establishment.",
        "86: Suspicious group: 1d10 Hunglungs setting a pipe bomb at a nearby establishment.",
        "87: Solarian Gardener offering 1hr in The Solarium in exchange for a 1d100cr donation to The Choke.",
        "88: Victim of a recent reaping attempt bleeding out. Get them to The Chop Shop in 30 min or they die.",
        "89: Flirts in flashing holosuits handing out fliers for the Psychoromp in The Stellar Burn tonight.",
        "90: A Sleeve with a featureless face passing out invitations to The Runway.",
        "91: Accused being escorted to The Court. They can pay 1d10kcr. Fight in 1d10 hours.",
        "92: Slickbay star and entourage mobbed by fans. Packed corridor. 10% chance of being pickpocketed.",
        "93: 1d10+2 fugitive Hunglungs looking for somewhere to hide.",
        "94: Tempest Co. raid on nearby establishment. Move along.",
        "95: 2d10 Teamsters looking to ambush Novo Droogs at a nearby Novo Bar.",
        "96: An empty, discarded Sleeve. Will rot in 1d10[-] hours. Still salvageable.",
        "97: All lights flicker and turn off. Sound of a heartbeat. Heavy, labored breathing.",
        "98: All nearby screens turn to static. Volume increases until you can't hear anything else. Then it's gone.",
        "99: Hologram of Ariel (pg.6) wandering alone. 'Please, help me. I don't want to die.' Disappears in 1d10min.",
    ]
    station_ru = [
        "Крит (дубли): Бросить снова и объединить два результата.",
        "00: Бросить Смертельную Встречу и объединить с другой Встречей на Станции.",
        "01-09: Зазывала ближайшего заведения. Скидка 10% прямо сейчас.",
        "10-19: Попрошайка O2 из Удавки. Нужно d100 кредитов, иначе сегодня отправят обратно. Дать — Стресс –1.",
        "20-24: Торговец продаёт [d10: (1-5) снаряжение, (6-9) наркотик, (10) кибермод] за 50% от цены.",
        "25-29: 1d5 Солярианских Миссионеров. Незрещённые, последовавшие за ними, получают час в Солярии.",
        "30-34: Заражённый житель [d10: (1-5) кашляет, (6-9) рвёт, (10) кибермоды вышли из-под контроля].",
        "35-39: Секс-работник из Экстаза предлагает ночь за 75% скидки.",
        "40-44: Уволенный наёмник Tempest (1d10 для ранга) ищет работу за 50%.",
        "45-49: 1d10 Новобранцев Tempest [d10: (1-5) патруль, (6-9) отпуск, (10) кого-то арестовывают].",
        "50-54: (Нет результата — перебросить.)",
        "55-57: Игроки играют в Сей. Ставка d100×1 ккр. Собирается толпа.",
        "58-60: Команда-Q карантинит зону. Обход: +1d100[-] минут к поездке.",
        "61-63: Первый помощник корабля ищет экипаж. Отход через 1d10 часов.",
        "64-66: Тэггер на переборке [d10: (1-5) КАЛИБАН ЖИВЁТ, (6-9) ОТНИМИ МОЁ ДЫХАНИЕ, (10) ЯН ДЕЕЕЗ НАТС].",
        "67-69: Банда 2d10 Ново-Дроогов оккупирует заброшенное заведение.",
        "70-71: Главный Адъюдикатор Брунхильд и Палачи. Все должны посторониться или получить плетью.",
        "72-73: Ново-Други [C:55 Ножи 1d10 H:1] избивают 1d10 попрошаек O2.",
        "74-75: Андроид с повреждёнными ногами лежит в вязкой жидкости и тянет руки за помощью.",
        "76-77: Танцоры из Звёздного Ожога скользят мимо с огромными голозмеями на плечах.",
        "78-79: 1d10 Светских персон возвращаются с установки Большого Переключателя на вечеринку кибермодов.",
        "80-81: Дилер Сикоракса предлагает пробные дозы. 200 кр/доза. Спасбросок Тела или двойной урон.",
        "82-83: 2d10 Квир-Народцев на ящиках снаружи местного заведения. Подозрительны к чужакам.",
        "84-85: Группа 1d10 грязных оборванцев хватается за ноги и просит объедки.",
        "85: 1d5+1 Ново-Дроогов, пьяных и выкинутых из заведения.",
        "86: Подозрительная группа: 1d10 Хунглунгов закладывают трубную бомбу в заведении.",
        "87: Солярианский Садовник предлагает час в Солярии за пожертвование 1d100 кр в Удавку.",
        "88: Жертва недавнего мародёрства истекает кровью. Доставить в Чоп-шоп за 30 мин или умрёт.",
        "89: Флиртующие в мигающих голокостюмах раздают флаеры на Психоромп в Звёздном Ожоге сегодня.",
        "90: Рукав с безликим лицом раздаёт приглашения на Подиум.",
        "91: Обвиняемого ведут в Суд. Может заплатить 1d10 ккр. Бой через 1d10 часов.",
        "92: Звезда Слик-бэя в окружении фанатов. Толпа. 10% шанс кражи.",
        "93: 1d10+2 беглых Хунглунгов ищут укрытие.",
        "94: Рейд Tempest на ближайшее заведение. Проходим мимо.",
        "95: 2d10 Тимстеров собираются устроить засаду на Ново-Дроогов в ближайшем Ново-Баре.",
        "96: Пустой выброшенный Рукав. Сгниёт через 1d10[-] часов. Ещё в пригодном состоянии.",
        "97: Все огни мигают и гаснут. Звук сердцебиения. Тяжёлое, хриплое дыхание.",
        "98: Все ближайшие экраны переходят в статику. Громкость нарастает до невыносимого. Потом тишина.",
        "99: Голограмма Ариэль (стр.6) бродит в одиночестве. 'Пожалуйста, помогите мне. Я не хочу умирать.' Исчезает через 1d10 мин.",
    ]
    station_ua = [
        "Крит (дублі): Кинути знову і об'єднати два результати.",
        "00: Кинути Смертельну Зустріч і об'єднати з іншою Зустріччю на Станції.",
        "01-09: Зазивала найближчого закладу. Знижка 10% прямо зараз.",
        "10-19: Жебрак O2 з Задуші. Потрібно d100 кредитів, інакше сьогодні відправлять назад. Дати — Стрес –1.",
        "20-24: Торговець продає [d10: (1-5) спорядження, (6-9) наркотик, (10) кіберімплант] за 50% від ціни.",
        "25-29: 1d5 Соляріанських Місіонерів. Нехрещені, що підуть за ними, отримають годину в Солярії.",
        "30-34: Заражений мешканець [d10: (1-5) кашляє, (6-9) блює, (10) кіберімпланти вийшли з-під контролю].",
        "35-39: Секс-працівник з Екстазу пропонує ніч за 75% знижки.",
        "40-44: Звільнений найманець Tempest (1d10 для рангу) шукає роботу за 50%.",
        "45-49: 1d10 Новобранців Tempest [d10: (1-5) патруль, (6-9) відпустка, (10) когось арештовують].",
        "50-54: (Немає результату — перекинути.)",
        "55-57: Гравці грають у Сей. Ставка d100×1 ккр. Збирається натовп.",
        "58-60: Команда-Q карантинить зону. Обхід: +1d100[-] хвилин до поїздки.",
        "61-63: Перший помічник корабля шукає екіпаж. Відхід через 1d10 годин.",
        "64-66: Теггер на переборці [d10: (1-5) КАЛІБАН ЖИВЕ, (6-9) ЗАБЕРИ МОЄ ДИХАННЯ, (10) ЯН ДЕЕЕЗ НАТС].",
        "67-69: Банда 2d10 Ново-Друзів окупує занедбаний заклад.",
        "70-71: Головний Ад'юдикатор Брунхільд і Кати. Усі мають посторонитись або отримати плетю.",
        "72-73: Ново-Друзі [C:55 Ножі 1d10 H:1] б'ють 1d10 жебраків O2.",
        "74-75: Андроїд з пошкодженими ногами лежить у в'язкій рідині і тягне руки за допомогою.",
        "76-77: Танцівники зі Зоряного Горіння ковзають повз з великими голозміями на плечах.",
        "78-79: 1d10 Світських персон повертаються з встановлення Великого Перемикача на вечірку кіберімплантів.",
        "80-81: Дилер Сикоракса пропонує пробні дози. 200 кр/доза. Рятівний кидок Тіла або подвійна шкода.",
        "82-83: 2d10 Квір-Людей на ящиках зовні місцевого закладу. Підозріливі до чужинців.",
        "84-85: Група 1d10 брудних безпритульних чіпляється за ноги і просить об'їдки.",
        "85: 1d5+1 Ново-Друзів, п'яних і вигнаних із закладу.",
        "86: Підозріла група: 1d10 Хунглунгів закладають трубну бомбу в закладі.",
        "87: Соляріанський Садівник пропонує годину в Солярії за пожертву 1d100 кр у Задушу.",
        "88: Жертва недавнього мародерства втрачає кров. Доставити до Чоп-шопу за 30 хв або помре.",
        "89: Фліртівники в мигаючих голокостюмах роздають флаєри на Психоромп у Зоряному Горінні сьогодні.",
        "90: Рукав із безликим обличчям роздає запрошення на Подіум.",
        "91: Обвинуваченого ведуть до Суду. Може заплатити 1d10 ккр. Бій через 1d10 годин.",
        "92: Зірка Слік-бею в оточенні фанатів. Натовп. 10% шанс крадіжки.",
        "93: 1d10+2 утіклих Хунглунгів шукають притулок.",
        "94: Рейд Tempest на найближчий заклад. Проходимо мимо.",
        "95: 2d10 Тімстерів збираються влаштувати засідку на Ново-Друзів у найближчому Ново-Барі.",
        "96: Порожній викинутий Рукав. Згниє через 1d10[-] годин. Ще у придатному стані.",
        "97: Усі вогні мигають і гаснуть. Звук серцебиття. Важке, хрипле дихання.",
        "98: Усі найближчі екрани переходять у статику. Гучність наростає до нестерпного. Потім тиша.",
        "99: Голограма Аріель (стор.6) бродить самотньо. 'Будь ласка, допоможіть мені. Я не хочу вмирати.' Зникає через 1d10 хв.",
    ]
    _ins(conn, PAGE_ID, 298, "🎲", "apof_station_encounters", 3,
        "Station Encounters", "Встречи на станции", "Зустрічі на станції",
        "Roll d100 when passing through a map slice (see Encounter Frequency table).",
        "Бросайте d100 при переходе через участок карты (см. таблицу частоты встреч).",
        "Кидайте d100 при переході через ділянку карти (див. таблицю частоти зустрічей).",
        100, station_en, station_ru, station_ua,
    )

    # ── C299 Establishments (d100) ────────────────────────────────────────────
    estab_en = [
        "00-02: Biovend — 1cr/dose. Body Save or take 1dmg.",
        "03-04: Ramen House — 2cr/bowl. Open 24hrs.",
        "05-06: Chai Room — 5cr/cup. +50cr for hallucinogenic tea (Body Save[-]).",
        "07: Teamster Bar — 1cr draft. Must present Union Card.",
        "08: Burger Joint — 20cr combo. Only real meat on the station.",
        "09: Gay Bar — 30cr cover. Body[-] Save or hangover.",
        "10-12: Cabaret — 200cr cover + drinks. Shows 1-2 hours.",
        "13-14: Mahjong Club — 500cr buy-in. No androids.",
        "15-16: Holocade — 10cr/hour. Win tickets for prizes.",
        "17: Solarian Garden — 10cr donation. Reduce 1 Stress/day.",
        "18: Drag Show — 35cr cover. 2d100cr in tips.",
        "19: Slickbooth — 10cr/min, 50cr/hr. Install Slicks, visit Slickworlds.",
        "20-22: Street Surgeon — [+] on Healing checks; failure causes 2d10dmg.",
        "23-24: Mod Repair — Minor 10% of list, Major 25%.",
        "25-26: Plastic Surgeon — Most surgeries 5kcr. Body Save or 1d5 Stress.",
        "27: Acupuncturist — 100cr first, 50cr recurring. Reduces 1 Stress/visit.",
        "28: Reaper Fence — Buys reaped mods for 25% of list price.",
        "29: Sleeve Storage — 500cr/month. 5% Infection Check chance.",
        "30-32: Ration Line — 1 ration/day free. Line takes 1d5 hours.",
        "33-34: Pawn Shop — Buys at 1d10-10% of list price.",
        "35-36: Outfitter — Clothing and standard equipment.",
        "37: Armory — 30% chance of a given weapon in stock.",
        "38: Mining Supplies — Laser Cutters, Survey Kits. 20% Union discount.",
        "39: Android Rental — 500cr/wk. [H:1 C:20 I:25 Loyalty:20 One trained Skill].",
        "40-42: Hostel — 1cr/night. Roll Station Encounter.",
        "43-44: Capsule Hotel — 100cr/night. Rest rolls at [-].",
        "45-46: Arco-op — 500cr/month + 20hrs co-op work/week.",
        "47-48: Apartment — 2d10×100cr/month. 1d100kcr to buy.",
        "49: Penthouse — 10kcr/month. 1d10mcr to buy. Rest rolls at [+].",
        "50-52: I-Ching Oracle — 90cr. Sanity Save success: 2× XP this session.",
        "53-54: Lumatat Shop — 500cr/hr. Spot 1d10hrs, Full Sleeve 50hrs, Back 90hrs.",
        "55-56: Palm Reader — 25cr. Sanity Save success: 1 reroll this session.",
        "57-58: Bathhouse — 100cr/month membership. Reduce 1d5 Stress.",
        "59: Solarian Shrine — 1cr offering. 1% chance [+] on one roll in next 24hrs.",
        "60-62: Novo Bar — Golyanovo II Bratva hangout. Droogs only.",
        "63-64: Strip Club — 50cr cover, 20cr lapdance. Reduce Stress by 1.",
        "65-66: Opium Den — 1kcr/hit. Reduce 2d10 Stress. Highly addictive.",
        "67: Fight Club — 10cr cover. 200cr/month. Must fight on first night. Body Save or 2d10dmg.",
        "68: BDSM Dungeon — 75cr cover. Dress code enforced.",
        "69: Freak Show — 100cr cover. Rare cybernetic mutations on display.",
        "70-72: Shooting Range — 200cr/month. Success: [+] on 1d5 future Combat Checks.",
        "73-74: Piloting Slicksim — 200cr/hr. 120hrs: Piloting. 500hrs: Vehicle Spec. 2khrs: Command.",
        "75-76: Boxing Gym — 50cr/month. Success: [+] on 1d5 future Strength Checks.",
        "77: Teamster Cert. — 100cr/hr. 40hrs: Union card. 100hrs: Asteroid Mining.",
        "78: Meditation Ctr. — 10cr donation. 1d10 Stress first visit, 1 Stress after.",
        "79: Shinken-Ri Dojo — 50cr/hr. 100hrs: Weapon Specialization (Unarmed).",
        "80-82: Tempest Outpost — 1d10 R0 Recruits being trained.",
        "83: Shuttle Dock — 50cr for a quick ride across the station.",
        "84-85: Engineering — Local 32819L facility keeping The Dream running.",
        "86: Holding Cells — Awaiting transfer to The Court.",
        "87: Fuel Depot — 20% discount for Teamsters.",
        "88: Power Plant — Destroying it destroys the current module.",
        "89: Waste Disposal — Disgusting smell. Body Save or vomit. Leads to The Veins.",
        "90: Warp Core Vault — 50kcr per warp core; each fuels a single Jump.",
        "91: Slaughterfactory — Provides meat for 85% of The Dream.",
        "92: Hunglung Base — Secret insurgent cell. Roll again for 'front' operation.",
        "93: Black Site — Tempest Co. off-the-books interrogation center.",
        "94: Hidden Corridor — Decreases travel time to a random module by half.",
        "95: Quarantine Area — Secretly quarantined by Tempest Co. No one in or out.",
        "96: Husk Brood Pit — Dark corridor leads to a pit of silent waiting Husks.",
        "97: Syndicate Hideout — Front operation (roll d100) for Syndicate spies.",
        "98: Nest of Caliban — Infested machinorganic mush; spews Chokespawn.",
        "99: Yandee's Penthouse — One of many fortified villas. 3d10 Armored Troopers.",
    ]
    estab_ru = [e.replace("Body Save", "Спасбросок Тела").replace("Sanity Save", "Спасбросок Рассудка")
                  .replace("Stress", "Стресс").replace("Healing", "Лечение") for e in estab_en]
    estab_ua = [e.replace("Body Save", "Рятівний кидок Тіла").replace("Sanity Save", "Рятівний кидок Розуму")
                  .replace("Stress", "Стрес").replace("Healing", "Лікування") for e in estab_en]
    _ins(conn, PAGE_ID, 299, "🏪", "apof_establishments", 4,
        "Establishments", "Заведения", "Заклади",
        "Roll d100 for a random establishment on Prospero's Dream.",
        "Бросайте d100 для случайного заведения на Мечте Просперо.",
        "Кидайте d100 для випадкового закладу на Мрії Просперо.",
        100, estab_en, estab_ru, estab_ua,
    )

    # ── C300 Denizens (d100) ──────────────────────────────────────────────────
    denizens_en = [
        "00-02: Caprico — Solarian Missionary — 'Invictus Sol, brother. Come and take the dawn with me.'",
        "03-04: Legato — Union Organizer — 'The teamsters are overworked. Reidmar is organizing a strike.'",
        "05-06: Denter — Spaceflight Controller — 'You fly close enough and you'll see a ship fused to the bottom of The Dream.'",
        "07: Ungar — Tempest Operator — 'Brunhild and her Executioners are androids and can't be bribed.'",
        "08: Yoshitaka — Overmodded Freak — 'They threw him into The Choke! For nothing! You have to get him back!'",
        "09: Tresch — Spice Smuggler — 'The Choke spawns monstrosities that run through the halls of The Dream.'",
        "10-12: Ramanan — Corporate Strikebreaker — 'Looking for undercover infiltrators into Reidmar's Union. Pays 300kcr.'",
        "13-14: Gatsby — Chokespawn Keeper — 'Some people's cybermods are failing, turning against their host body.'",
        "15-16: Advik — Novo Droog — 'Don't let them know I told you this, but Yandee's a synthetic.'",
        "17: Hansh — Rim War Refugee — 'In The Choke a massive ancient machine awakens every 130 days.'",
        "18: Krish — Lifesupport Engineer — Secret Saboteur. Wants to overthrow The Court.",
        "19: Rohan — Cybermod Reaper — 'Have you dreamed of the metal laughing face yet?'",
        "20-22: Eiko — Ultimó Player — 'Sometimes people get sick here. Like, vomiting blood and liquid metal sick.'",
        "23-24: Skeeve — Pinkerton Unit — 'Have you seen this individual?' (roll d100 for fugitive description)",
        "25-26: Wince — Android in Hiding — 'Looking for a way off the station. Any ship. Anywhere.'",
        "27: Govender — Sycorax Addict — 'They're serving Hunglungs from The Choke at long-pork dinner parties.'",
        "28: Engström — Off-duty Sex Worker — 'I don't do no mods. They go blank sometimes and get rough.'",
        "29: Renton — Sycorax Dealer — 'Weird fruits grow deep in The Choke. The Solarians will pay for them.'",
        "30-32: Roskam — Clan Hologamer — 'This girl named Ariel shows up in all my games. She says she's dying.'",
        "33-34: Akane — Rim Space Astrogator — 'Have you seen the glory of raw space?'",
        "35-36: Fedorov — Snake Dancer — 'Tempest is breeding hybrids in The Choke.'",
        "37: Sokolov — Holopet Designer — 'Sometimes the AI code seems to write itself.'",
        "38: Aradhya — O2 Beggar — 'I can't go back to The Choke... I CAN'T!'",
        "39: Nowak — Court Advocate — 'If you ever get in trouble at The Court and need a hand, ask for me.'",
        "40-42: Cheng — Q-Team Cleaner — 'Tempest is on a secret mission from Rosalind Bio & Weaponization.'",
        "43-44: Enzo — Court High Patron — 'If those Chokers don't like it down there they should get a job.'",
        "45-46: Otomo — Court Executioner — 'It's too bad she won't live. But then again, who does?'",
        "47-48: Kowalski — Holoslick Producer — 'Love your look! Do you wanna be famous?'",
        "49: Yannik — Cybermod Hacker — 'You gotta overclock. You only get one body right? Well, one first body.'",
        "50-52: Bennett — Nomadic Cleromancer — 'There are games of skill and games of chance. Life is both.'",
        "53-54: Kask — Corporate Bodyguard — 'My boss is looking for a crew with some Tempest training. You in?'",
        "55-56: Tamm — Vault Cracker — 'I can crack it. How many creds we talkin'? Half. I want half.'",
        "57-58: Moreau — Bounty Hunter — 'Two thousand credits and a name.'",
        "59: Westbay — Android Serial Killer — 'Someone hacked my holopet! It just ran down that dark corridor!'",
        "60-62: Ivanov — Yakuza Lumatat Artist — 'I need creds bad. Half off, today only.'",
        "63-64: Trantis — Ragrunner — 'I can do any job on a ship. Just looking to get off this shithole station.'",
        "65-66: Yuvenko — Sleevejacker — 'You haven't lived until you've lived twice.'",
        "67: Kruger — Street Doctor — 'A stitch in time saves nine. I can get anywhere in The Dream in 30 minutes.'",
        "68: Brunekta — Licensed Privateer — 'I'm looking to score off a ship in the docks tonight, you want a piece?'",
        "69: Vasiliev — Holoslick Star — 'Please, my girl is stuck in The Choke. I've got the credits...'",
        "70-72: Ellywhen — Knockoff Mod Dealer — 'Watch my back tonight. Yandee's crew is gunning for me.'",
        "73-74: Stein — Colony Recruiter — 'Need a team to scout terrain and install terraformers. 100k sound good?'",
        "75-76: Kotze — Tea Brewer — 'I need this new tea leaf. Only 2 Jumps away. 25kcr if you're interested.'",
        "77: Octrev — Desperate Hacker — 'Boyfriend is a Slug addict. I'll do anything if you drop Slug and find him.'",
        "78: Leikfenn — Runway Model — 'There's an android stalking me, trying to kill me. It looks exactly like me.'",
        "79: Sang — Hyperspace Raider — 'You think I'm psycho, don't you, Mama? You'd better let 'em lock me up!'",
        "80-82: Kramm — Hunglung Sympathizer — 'The Choke is a death camp for poor people. Stop lying to yourself.'",
        "83: Astrid — Hunglung Terrorist — 'The breath you steal from us will be your last.'",
        "84-85: Eleanor — Seed Geneticist — Looking for unhatched Chokespawn egg. Pays 30kcr.",
        "86: Linus — Block Captain — 'Tempest has gone too far. We have to band together to keep safe.'",
        "87: Altmann — Conscript Dodger — 'You never saw me, okay? Keep my name out of any Tempest Co. reports.'",
        "88: Roux — Prison Marshall — 'Guard duty don't pay so well, but there are side benefits. 2kcr starting.'",
        "89: Sloane — Armored Ship Robber — 'Got these hand welders that cut twice as fast and far. 300cr?'",
        "90: Petrov — Customs Inspector — 'I could use a little muscle later for an inspection. Interested?'",
        "91: Ozu — Infected Citizen — 'I ain't feel so good... [pukes blood and nanites on your feet].'",
        "92: Motoko — Solarian Caretaker — 'I see your light. Come with me to The Garden. You will feel lighter.'",
        "93: Loeb — Hydroponic Farmer — 'It's all about nutrients, maaaaan.'",
        "94: Grendel — Undercover Thinkpol — 'Tell me a little bit about yourself.'",
        "95: Amano — Political Prisoner — 'I know people that can pay big. Be my Advocate and I'll change your life.'",
        "96: Kleyman — Novo Informant — 'Lookin' for scabs. If Reidmar orders a strike we'll need loyal people.'",
        "97: Orlov — Core World Fugitive — 'You can't go anywhere in the Core without signing their Terms of Service.'",
        "98: McCabe — Warp Core Mechanic — 'Jumping is a form of prayer. You gotta be devout and you gotta be crazy.'",
        "99: Stintz — Syndicate Spy — 'Show me where Yandee rests their head. I can get you out safely. 500kcr.'",
    ]
    _ins(conn, PAGE_ID, 300, "👤", "apof_denizens", 5,
        "Denizens of The Dream",
        "Обитатели Мечты",
        "Мешканці Мрії",
        "Roll d100 for a random NPC on Prospero's Dream.",
        "Бросайте d100 для случайного НИП на Мечте Просперо.",
        "Кидайте d100 для випадкового НГП на Мрії Просперо.",
        100, denizens_en, denizens_en, denizens_en,
    )

    # ── C301 Living Expenses ──────────────────────────────────────────────────
    _ins(conn, PAGE_ID, 301, "💸", "apof_living_expenses", 6,
        "Living Expenses",
        "Расходы на проживание",
        "Витрати на проживання",
        (
            "• Squalor: 1cr/day. Tempest Co. will throw you in The Choke if they find you.\n"
            "• Borderline: 20cr/day. Can eat, breathe, sleep.\n"
            "• Citizen: 50cr/day. Move about comfortably.\n"
            "• Decadent: 200cr/day. Go wherever you want, do whatever you want.\n\n"
            "Directions from strangers to any establishment cost 10cr (a day of oxygen)."
        ),
        (
            "• Нищета: 1 кр/день. Tempest Co. выбросит вас в Удавку при обнаружении.\n"
            "• Прожиточный минимум: 20 кр/день. Можно есть, дышать, спать.\n"
            "• Гражданин: 50 кр/день. Свободно передвигаться.\n"
            "• Декаданс: 200 кр/день. Куда угодно, что угодно.\n\n"
            "Направления к любому заведению у незнакомца стоят 10 кр (день кислорода)."
        ),
        (
            "• Злидні: 1 кр/день. Tempest Co. викине вас у Задушу при виявленні.\n"
            "• Прожитковий мінімум: 20 кр/день. Можна їсти, дихати, спати.\n"
            "• Громадянин: 50 кр/день. Вільно пересуватись.\n"
            "• Декаданс: 200 кр/день. Куди завгодно, що завгодно.\n\n"
            "Вказівки до будь-якого закладу від незнайомця коштують 10 кр (день кисню)."
        ),
    )

    # ── C302 Corespace Station Generator ──────────────────────────────────────
    _ins(conn, PAGE_ID, 302, "🌐", "apof_corespace_gen", 7,
        "Corespace Station Generator",
        "Генератор станций Ядра",
        "Генератор станцій Ядра",
        (
            "[STATION NAME] is a(n) [CORE STATION] orbiting a(n) [CELESTIAL BODY]. "
            "Run by a(n) [CORE LEADER] backed by [GROUP]. "
            "Docking: 1d10×100cr. Cheap room: 2d100cr/night. "
            "5% chance station is undergoing a [CRISIS]. "
            "Markup: 2d100%. Buys [GOODS] at 1d100-10% off. "
            "Free-traders have a line on [RESOURCE].\n\n"
            "d10 | Station Name | Core Station | Celestial Body | Core Leader | Group\n"
            "01 | Azrael's Price | Overcrowded Habitat Colony | Still Terraforming Planet | First-Colony Descendant | Radical Colonial Separatists\n"
            "02 | Dumah's Sorrow | Palatial Estate | Overpopulated Slumworld | Asteroid Mining Oligarch | Valecore Mining Consortium\n"
            "03 | Marut's Redemption | Secret Corporate Research Facility | Resource Rich Planet | Reclusive Intellectual | Exo-Credit Federated Union\n"
            "04 | Gorgon's Revenge | Marine Battle School | Desolate Planetoid | Scheming Marine General | 91st Colonial Dragoons\n"
            "05 | Soter's Ring | Bustling Trading Port | White Dwarf Star | Teamster Union Rep | Teamster's Local 101977L\n"
            "06 | Pontian's Crown | Sprawling Megatropolis | Moon of an Inhabited Planet | Sadistic Decadent | Yamguchi-gumi Clan\n"
            "07 | Vitalian's Sword | High Security Corporate Vault | Unpopulated Paradise World | Decorated Regional Governor | Crashlander Titan 2nd Fleet\n"
            "08 | Iblis's Shield | Semi-Autonomous Shipyard | Giant Asteroid Cluster | Rimwar Veteran Commander | Principality of Christian XII\n"
            "09 | Al-'Uzzá's Cross | Solitary Monastery | Red Supergiant | Reformed Criminal Outcast | Decanon Caliphate\n"
            "10 | Vanth's Herald | Ancient Jump Gate | Black Hole (past Event Horizon) | Dynastic Child-Heir | House of Tarkhan"
        ),
        (
            "[НАЗВАНИЕ СТАНЦИИ] — это [ТИП СТАНЦИИ] на орбите [НЕБЕСНОГО ТЕЛА]. "
            "Управляет [ЛИДЕР ЯДРА] при поддержке [ГРУППЫ]. "
            "Стоянка: 1d10×100 кр. Дешёвый номер: 2d100 кр/ночь. "
            "5% шанс кризиса [КРИЗИС]. Наценка: 2d100%. "
            "Покупает [ТОВАР] за -1d100+10%. Свободные торговцы знают про [РЕСУРС].\n\n"
            "d10 | Название | Тип | Небесное тело | Лидер | Группа\n"
            "01 | Цена Азраэля | Переполненная Колония-Жильё | Ещё Терраформируемая Планета | Потомок Первой Колонии | Радикальные Колониальные Сепаратисты\n"
            "02 | Горе Думаха | Роскошное Поместье | Перенаселённый Трущобный Мир | Олигарх Горнодобычи | Горный Консорциум Вейлкор\n"
            "03 | Искупление Марута | Тайный Корпоративный Исследовательский Центр | Планета Богатая Ресурсами | Затворник-Интеллектуал | Федеральный Союз Экзо-Кредит\n"
            "04 | Месть Горгоны | Морская Боевая Школа | Безлюдный Планетоид | Интригующий Морской Генерал | 91-е Колониальные Драгуны\n"
            "05 | Кольцо Сотера | Оживлённый Торговый Порт | Белый Карлик | Представитель Профсоюза | Местный 101977L Тимстеров\n"
            "06 | Корона Понтиана | Разросшийся Мегаполис | Спутник Обитаемой Планеты | Садистский Декадент | Клан Ямгучи-гуми\n"
            "07 | Меч Виталиана | Высокозащищённый Корпоративный Сейф | Необитаемый Рай | Заслуженный Региональный Губернатор | Флот Краш-лендеров Титан 2й\n"
            "08 | Щит Иблиса | Полуавтономная Верфь | Кластер Гигантских Астероидов | Ветеран Войны на Краю | Принципат Кристиана XII\n"
            "09 | Крест Аль-Уззы | Уединённый Монастырь | Красный Сверхгигант | Реформированный Преступник-Изгой | Деканский Халифат\n"
            "10 | Вестник Ванта | Древние Прыжковые Врата | Чёрная Дыра | Наследник Династии | Дом Тархан"
        ),
        (
            "[НАЗВА СТАНЦІЇ] — це [ТИП СТАНЦІЇ] на орбіті [НЕБЕСНОГО ТІЛА]. "
            "Керує [ЛІДЕР ЯДРА] за підтримки [ГРУПИ]. "
            "Стоянка: 1d10×100 кр. Дешевий номер: 2d100 кр/ніч. "
            "5% шанс кризи [КРИЗА]. Націнка: 2d100%. "
            "Купує [ТОВАР] за -1d100+10%. Вільні торговці знають про [РЕСУРС].\n\n"
            "d10 | Назва | Тип | Небесне тіло | Лідер | Група\n"
            "01 | Ціна Азраеля | Переповнена Колонія-Житло | Ще Тераформована Планета | Нащадок Першої Колонії | Радикальні Колоніальні Сепаратисти\n"
            "02 | Горе Думаха | Розкішна Садиба | Перенаселений Трущобний Світ | Олігарх Видобувної Промисловості | Гірничодобувний Консорціум Вейлкор\n"
            "03 | Спокута Марута | Таємний Корпоративний Дослідницький Центр | Планета Багата на Ресурси | Відлюдник-Інтелектуал | Федеральний Союз Екзо-Кредит\n"
            "04 | Помста Горгони | Морська Бойова Школа | Безлюдний Планетоїд | Підступний Морський Генерал | 91-й Колоніальний Драгунський\n"
            "05 | Кільце Сотера | Жвавий Торговий Порт | Білий Карлик | Представник Профспілки | Місцева 101977L Тімстерів\n"
            "06 | Корона Понтіана | Розросле Мегамісто | Супутник Населеної Планети | Садистський Декадент | Клан Ямгуті-гумі\n"
            "07 | Меч Віталіана | Сильнозахищений Корпоративний Сейф | Ненаселений Рай | Заслужений Регіональний Губернатор | Флот Краш-лендерів Титан 2й\n"
            "08 | Щит Ібліса | Напівавтономна Верф | Кластер Гігантських Астероїдів | Ветеран Війни на Краю | Принципат Крістіана XII\n"
            "09 | Хрест Аль-Уззи | Відокремлений Монастир | Червоний Надгігант | Реформований Злочинець-Вигнанець | Деканський Халіфат\n"
            "10 | Вісник Ванта | Стародавні Стрибкові Ворота | Чорна Діра | Спадкоємець Династії | Дім Тархан"
        ),
    )

    # ── C303 Rimspace Station Generator ───────────────────────────────────────
    _ins(conn, PAGE_ID, 303, "🌌", "apof_rimspace_gen", 8,
        "Rimspace Station Generator",
        "Генератор станций Края",
        "Генератор станцій Краю",
        (
            "Near a(n) [RIM LANDMARK], a(n) [STATION NAME] station (call-sign [CALL-SIGN]) spins. "
            "Controlled by [CONTROL FACTION], undermined by [RIVAL FACTION] led by a(n) [RIVAL LEADER]. "
            "20% chance of a [CRISIS]. Otherwise: fuel as normal, only [GOODS] for sale, "
            "station in dire need of [RESOURCE].\n\n"
            "d10 | Rim Landmark | Station | Call-Sign | Control | Rival | Rival Leader\n"
            "01 | Heavily Guarded Corporate DMZ | Independent Colony | Remote Site-[d100]-[Letter] | Anders-Klimt Mining Corp | Synthetic Liberation Front | Renegade Android\n"
            "02 | Battered Asteroid Field | Run Down Factory | [d100]-[d10] | Gaff Android Labor Syndicate | Altruistic Scientists | Powerful Rogue AI\n"
            "03 | Uninhabitable Desert Planet | Military Base | Forward Base-[d10]-[Letter] | 601st Colonial Marine Regiment | Neo-Haram Anarchists | Ruthless Criminal Despot\n"
            "04 | Strip-Mined Ice World | Lighthouse | Rimward-Post [d10]-[d10] | Salo-Mercury Biomotors Inc. | Violent Return-Earthers | Charismatic Revivalist\n"
            "05 | First Generation Pioneer Colony | Asteroid Mining | [Letter]-[d100] | Apostles Gate Church | Carter Tactical Concerns Ltd. | Perverse Corp. Warden\n"
            "06 | Resource Rich Asteroid Cluster | Maximum Sec. Prison | Supervisor-[Letter]-[d10] | Confederated Systems Inc. | Armadyne Weapons Inc. | Highly Intelligent Merc. Captain\n"
            "07 | Disputed Territory Border | Scrap Processing | Control-[d100] | 'Opera' Fleet of Mercenary Raiders | House Sivaranjan | Cunning Corporate Spy\n"
            "08 | Massive Jump-5 Derelict Hulk | Rest & Refuel | Command-[d10]-[d10] | Sindec Alloyed Metals Corp | Secret Union Instigators | Merciless Slaver\n"
            "09 | Burgeoning Off-World Colony | Black Market | Outpost [d100]-[Letter]-[d10] | SEBACO Mining Ltd. | Black Dawn Mercenaries | Stalwart Union Organizer\n"
            "10 | Ship Graveyard | Abandoned Derelict | Bridle-[d10] | Limited Colonial Government | Family of Eleven | Relentless Warrant Officer"
        ),
        (
            "У [ОРИЕНТИРА КРАЯ] вращается станция [НАЗВАНИЕ] (позывной [ПОЗЫВНОЙ]). "
            "Контролируется [ФРАКЦИЕЙ], подрывается [СОПЕРНИКОМ] под руководством [ЛИДЕРА СОПЕРНИКА]. "
            "20% шанс [КРИЗИСА]. Иначе: топливо как обычно, продаётся только [ТОВАР], "
            "острая нужда в [РЕСУРСЕ].\n\n"
            "(см. английскую версию для полных таблиц d10)"
        ),
        (
            "Біля [ОРІЄНТИРА КРАЮ] обертається станція [НАЗВА] (позивний [ПОЗИВНИЙ]). "
            "Контролюється [ФРАКЦІЄЮ], підривається [СУПЕРНИКОМ] під керівництвом [ЛІДЕРА СУПЕРНИКА]. "
            "20% шанс [КРИЗИ]. Інакше: пальне як зазвичай, продається лише [ТОВАР], "
            "гостра потреба в [РЕСУРСІ].\n\n"
            "(див. англійську версію для повних таблиць d10)"
        ),
    )

    # ── C304 Crisis Table (d10) ────────────────────────────────────────────────
    _ins(conn, PAGE_ID, 304, "🚨", "apof_crisis_table", 9,
        "Station Crisis Table",
        "Таблица кризисов станции",
        "Таблиця криз станції",
        "Roll d10 to determine the crisis a space station is facing.",
        "Бросайте d10 для определения кризиса на космической станции.",
        "Кидайте d10 для визначення кризи на космічній станції.",
        10,
        [
            "Hostage Situation. Command taken by a rival faction who demand 1d10kcr ransom.",
            "Refugee Crisis. Station overrun with refugees. Everything 1d10+1× more expensive.",
            "Food Shortage. Station pays 1d10+1kcr for food and another random resource. Theft rampant.",
            "Quarantine. After boarding you learn it's quarantined. No one allowed to leave.",
            "Bout of Civil Unrest. Rioting and looting. Mercenary death squads execute collaborators.",
            "Disaster. Crash landing, mass explosion or sabotage. Full alert and going down without repairs.",
            "General Strike. Unions organized. Protests, picket lines, riots. Commerce shut down.",
            "Uncanny Abandonment. Aftermath of some bloody, haunted or mysterious happening.",
            "Martial Law Edict. All ships boarded and inspected, visas issued, curfew in effect.",
            "Blockade. Station under siege by rival faction. Access cut off. Your ship will be boarded.",
        ],
        [
            "Захват заложников. Командование захвачено соперничающей фракцией, требующей 1d10 ккр выкупа.",
            "Кризис беженцев. Станция переполнена беженцами. Всё в 1d10+1× дороже обычного.",
            "Нехватка продовольствия. Станция платит 1d10+1 ккр за еду и случайный ресурс. Кражи повсюду.",
            "Карантин. Уже на борту выясняется карантин. Никому нельзя покинуть станцию.",
            "Гражданские волнения. Грабежи и беспорядки. Наёмные отряды смерти расстреливают коллаборационистов.",
            "Катастрофа. Аварийная посадка, взрыв или диверсия. Полная тревога — станция падает без ремонта.",
            "Всеобщая забастовка. Профсоюзы организовались. Протесты, пикеты, бунты. Торговля остановлена.",
            "Зловещее запустение. Последствия кровавого, проклятого или загадочного события.",
            "Военное положение. Все корабли досматриваются, выдаются визы, введён комендантский час.",
            "Блокада. Станция осаждена соперничающей фракцией. Доступ заблокирован. Ваш корабль будет захвачен.",
        ],
        [
            "Захоплення заручників. Командування захоплено суперничаючою фракцією, що вимагає 1d10 ккр викупу.",
            "Криза біженців. Станція переповнена біженцями. Все в 1d10+1× дорожче.",
            "Нестача продовольства. Станція платить 1d10+1 ккр за їжу і випадковий ресурс. Злодійство повсюди.",
            "Карантин. Вже на борту з'ясовується карантин. Нікому не можна залишати станцію.",
            "Громадянські заворушення. Грабунки та безлад. Найманські загони смерті розстрілюють колаборантів.",
            "Катастрофа. Аварійна посадка, вибух або диверсія. Повна тривога — станція падає без ремонту.",
            "Загальний страйк. Профспілки організувались. Протести, пікети, бунти. Торгівля зупинена.",
            "Зловісне запустіння. Наслідки кривавої, прокляттєвої або загадкової події.",
            "Воєнний стан. Усі кораблі оглядаються, видаються візи, запроваджено комендантську годину.",
            "Блокада. Станція в облозі суперничаючої фракції. Доступ заблокований. Ваш корабель буде захоплений.",
        ],
    )

    # ── C305 Structure Table (d10) ─────────────────────────────────────────────
    _ins(conn, PAGE_ID, 305, "🏗️", "apof_structure_table", 10,
        "Space Station Structure",
        "Структура космической станции",
        "Структура космічної станції",
        "Roll d10 to determine the physical structure of a space station.",
        "Бросайте d10 для определения физической структуры космической станции.",
        "Кидайте d10 для визначення фізичної структури космічної станції.",
        10,
        [
            "Asteroid Surface. Built on the outside surface of an asteroid.",
            "Asteroid Interior. Station exists underground as tunnels, caves, or similar structures.",
            "Spindle. Common design shaped like a spinning top with towers rising from top and/or bottom.",
            "Cylinder. Rotation provides artificial gravity. Can be quite large, like an O'Neill Cylinder.",
            "Sphere. Can be as big as a Dyson/Bernal Sphere or as small as a single pod-station.",
            "Torus/Ring. Most common design. Outer ring could provide centrifugal artificial gravity.",
            "Tower. Angular or blocky design, like a skyscraper flung into space.",
            "Modular. Built from discrete modules or 'beads' that can be removed or added on to.",
            "Platform. Design based on a large ship. Clearly defined levels/decks.",
            "Amalgamation. Roll twice and combine two of the other designs.",
        ],
        [
            "Поверхность астероида. Построена на внешней поверхности астероида.",
            "Недра астероида. Станция существует под землёй как тоннели, пещеры и подобные структуры.",
            "Веретено. Распространённый дизайн в форме юлы с башнями снизу и/или сверху.",
            "Цилиндр. Вращение обеспечивает искусственную гравитацию. Может быть очень большим, как цилиндр О'Нейла.",
            "Сфера. Может быть как сферой Дайсона/Бернала, так и маленьким одноместным подом.",
            "Тор/Кольцо. Самый распространённый дизайн. Внешнее кольцо создаёт центробежную гравитацию.",
            "Башня. Угловатый или блочный дизайн, как небоскрёб в космосе.",
            "Модульная. Построена из отдельных модулей, которые можно добавлять или убирать.",
            "Платформа. Дизайн основан на большом корабле. Чётко выраженные уровни/палубы.",
            "Гибрид. Бросить дважды и объединить два других дизайна.",
        ],
        [
            "Поверхня астероїда. Побудована на зовнішній поверхні астероїда.",
            "Надра астероїда. Станція існує під землею як тунелі, печери та подібні структури.",
            "Веретено. Поширений дизайн у формі дзиги з вежами знизу та/або зверху.",
            "Циліндр. Обертання забезпечує штучну гравітацію. Може бути дуже великим, як циліндр О'Ніла.",
            "Сфера. Може бути як сферою Дайсона/Бернала, так і маленькою однопосадковою станцією.",
            "Тор/Кільце. Найпоширеніший дизайн. Зовнішнє кільце створює відцентрову гравітацію.",
            "Вежа. Кутастий або блоковий дизайн, як хмарочос у космосі.",
            "Модульна. Побудована з окремих модулів, які можна додавати або прибирати.",
            "Платформа. Дизайн заснований на великому кораблі. Чітко виражені рівні/палуби.",
            "Гібрид. Кинути двічі і поєднати два інших дизайни.",
        ],
    )

    # ── C306 Common Space Station Issues (d10) ─────────────────────────────────
    _ins(conn, PAGE_ID, 306, "⚙️", "apof_station_issues", 11,
        "Space Station Issues",
        "Проблемы космической станции",
        "Проблеми космічної станції",
        "Roll d10 for a common issue affecting a space station.",
        "Бросайте d10 для случайной проблемы космической станции.",
        "Кидайте d10 для випадкової проблеми космічної станції.",
        10,
        [
            "No Artificial Gravity. Zero-G Skill Check for complex maneuvers.",
            "Resource Scarcity. Food, water, oxygen, shelter is hard to find.",
            "Trade Good Scarcity. Lack of fuel, warp cores, ammunition.",
            "Oxygen Poor. Strenuous activities at [-]. O2 taxation.",
            "Non-standard Day/Night Cycle. Resting at [-].",
            "Poor Water Treatment Facilities. Healing at [-].",
            "Low Security. High risk of theft, threat of violence, piracy.",
            "High Security. High risk of authoritarian police, taxation, prison.",
            "Xenophobic Population. Suspicious/hostile to strangers/outsiders.",
            "Poor Maintenance. Minimum Stress +1. Resting and Healing at [-]. High risk of damage during combat.",
        ],
        [
            "Нет искусственной гравитации. Нулевая-G — Проверка Навыка для сложных манёвров.",
            "Нехватка ресурсов. Еда, вода, кислород, жильё труднодоступны.",
            "Нехватка товаров. Отсутствие топлива, варп-ядер, боеприпасов.",
            "Недостаток кислорода. Тяжёлые действия с [-]. Налогообложение O2.",
            "Нестандартный цикл день/ночь. Отдых с [-].",
            "Плохие водоочистные сооружения. Лечение с [-].",
            "Низкая безопасность. Высокий риск краж, угрозы насилия, пиратства.",
            "Высокая безопасность. Высокий риск авторитарной полиции, налогов, тюрьмы.",
            "Ксенофобное население. Подозрительно/враждебно к чужакам.",
            "Плохое обслуживание. Мин. Стресс +1. Отдых и Лечение с [-]. Высокий риск повреждений в бою.",
        ],
        [
            "Немає штучної гравітації. Нульова-G — Перевірка Навику для складних маневрів.",
            "Нестача ресурсів. Їжа, вода, кисень, житло важкодоступні.",
            "Нестача торгових товарів. Відсутність пального, варп-ядер, боєприпасів.",
            "Низький вміст кисню. Важкі дії з [-]. Оподаткування O2.",
            "Нестандартний цикл день/ніч. Відпочинок з [-].",
            "Погані водоочисні споруди. Лікування з [-].",
            "Низька безпека. Високий ризик крадіжок, загрози насильства, піратства.",
            "Висока безпека. Високий ризик авторитарної поліції, податків, в'язниці.",
            "Ксенофобне населення. Підозріливе/вороже до чужинців.",
            "Погане обслуговування. Мін. Стрес +1. Відпочинок і Лікування з [-]. Високий ризик пошкоджень у бою.",
        ],
    )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — 11 contents added to P38 (Tables): C296-C306.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
