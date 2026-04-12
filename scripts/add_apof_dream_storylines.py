"""
scripts/add_apof_dream_storylines.py
A Pound of Flesh — P32 "The Dream" (C212-C217) and P34 "Storylines" (C224-C228).
Run after add_apof_source_pages.py.
Run: python scripts/add_apof_dream_storylines.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ─────────────────────────────────────────────────────────────────────────────
# P32 THE DREAM  (C212–C217)
# ─────────────────────────────────────────────────────────────────────────────

P32_CONTENTS = [
    {
        "id": 212, "icon": "🚀", "source_page": 4, "sort_order": 1,
        "name": ("Station Overview", "Обзор станции", "Огляд станції"),
        "desc": (
            "Prospero's Dream is a massive space station with a population of over 8 million. "
            "It's haphazard, disorganized, overcrowded and teeming with hustlers and criminals of all stripes.\n\n"
            "Population (City Level): 5.6m | Diameter: 12.98km | Decks (Outer Ring): 23\n"
            "Population (Choke): 3.1m | Circumference: 40.77km | Decks (Ring Structures Avg.): 78\n"
            "Ships Currently Docked: 1d100 | Decks (Center Spire): 430\n\n"
            "The Dream is operated by the Golyonova II Bratva (AKA the Novos, or 'Yandee's People'), "
            "a powerful criminal syndicate headed by a meticulous (secret) android named Yandee, "
            "backed by the elite Tempest Mercenary Company. Together they sell the lucrative drug "
            "Sycorax, which is supplied by The Solarian Church and distributed by Teamsters Local 32819L.",

            "Мечта Просперо — огромная космическая станция с населением более 8 миллионов человек. "
            "Здесь царит беспорядок, перенаселённость и разгул преступности всех мастей.\n\n"
            "Население (городской уровень): 5,6м | Диаметр: 12,98 км | Палубы (внешнее кольцо): 23\n"
            "Население (Удавка): 3,1м | Окружность: 40,77 км | Палубы (кольцевые структуры, ср.): 78\n"
            "Кораблей пришвартовано сейчас: 1d100 | Палубы (центральный шпиль): 430\n\n"
            "Мечтой управляет братва Голяново II (она же «Новосы» или «Люди Яндея») — мощный "
            "преступный синдикат во главе с педантичным (тайным) андроидом Яндеем, "
            "которому помогает элитная наёмная компания Tempest. Вместе они торгуют "
            "прибыльным наркотиком Сикорах, который поставляет Солярианская церковь, "
            "а распространяет Местная 32819L Тимстеров.",

            "Мрія Просперо — величезна космічна станція з населенням понад 8 мільйонів. "
            "Тут панує хаос, перенаселеність і розгул злочинності всіх мастей.\n\n"
            "Населення (міський рівень): 5,6м | Діаметр: 12,98 км | Палуби (зовнішнє кільце): 23\n"
            "Населення (Задуша): 3,1м | Окружність: 40,77 км | Палуби (кільцеві структури, сер.): 78\n"
            "Кораблів зараз пришвартовано: 1d100 | Палуби (центральний шпиль): 430\n\n"
            "Мрією керує братва Голяново II (вона ж «Новоси» або «Люди Яндея») — потужний "
            "злочинний синдикат на чолі з педантичним (таємним) андроїдом Яндеєм, "
            "якому допомагає елітна найманська компанія Tempest. Разом вони торгують "
            "прибутковим наркотиком Сикорах, який постачає Соляріанська церква, "
            "а розповсюджує Місцева 32819L Тімстерів.",
        ),
    },
    {
        "id": 213, "icon": "🚪", "source_page": 4, "sort_order": 2,
        "name": ("Boarding The Dream", "Посадка на Мечту", "Посадка на Мрію"),
        "desc": (
            "Ships of Hull 70 or lower enter through the dry dock (locked into the station via crane). "
            "Ships of Hull 71+ must moor to the station's piers — a shuttle retrieves passengers.\n\n"
            "Every ship requires an up-to-date manifest (captain, crew, cargo). IDs are checked on entry. "
            "Discrepancies can lead to invasive searches, an impounded vehicle, or arrest.\n\n"
            "Upon disembarking you're directed to a Clean Room where a Q-Team (hazmat-clad brutes) "
            "strip searches you and sprays you with disinfectant foam (4 Stress, Fear Save for half).\n\n"
            "You're then issued an O2 credstick — your wallet, passport, and locator aboard the station. "
            "It must be pre-loaded with credits; taxes and fees are automatically withdrawn daily.\n\n"
            "Q-TEAM: COMBAT 25 (Disinfectant Foam Gun — Body Save or knocked down; or Pulse Rifles 5d10 DMG) "
            "SPEED 35 | INSTINCT 25 | HITS 2 (20)",

            "Корабли с корпусом 70 и ниже входят через сухой dok (блокируются краном). "
            "Корабли с корпусом 71+ пришвартовываются к пирсам — шаттл забирает пассажиров.\n\n"
            "Каждый корабль должен иметь актуальный манифест (капитан, экипаж, груз). "
            "Удостоверения проверяются при входе. Несоответствия грозят обыском, конфискацией или арестом.\n\n"
            "При высадке вас направляют в Дезинфекционную комнату, где Команда-Q (брутальные парни "
            "в защитных костюмах) обыскивает и обрабатывает дезинфицирующей пеной "
            "(4 Стресса, Спасбросок Страха для половины).\n\n"
            "Вам выдают кредитный стик О2 — ваш кошелёк, паспорт и маяк на станции. "
            "Нужно пополнить кредитами; налоги и сборы снимаются автоматически каждый день.\n\n"
            "КОМАНДА-Q: БОЙ 25 (Пеногаситель — Спасбросок Тела или сбит с ног; Импульсные винтовки 5d10 урона) "
            "СКОРОСТЬ 35 | ИНСТИНКТ 25 | ОЧКИ ЗДОРОВЬЯ 2 (20)",

            "Кораблі з корпусом 70 і нижче входять через сухий dok (блокуються краном). "
            "Кораблі з корпусом 71+ пришвартовуються до пірсів — шаттл забирає пасажирів.\n\n"
            "Кожен корабель повинен мати актуальний маніфест (капітан, екіпаж, вантаж). "
            "Посвідчення перевіряються при вході. Невідповідності загрожують обшуком, конфіскацією або арештом.\n\n"
            "При висадці вас направляють до Дезінфекційної кімнати, де Команда-Q (брутальні хлопці "
            "у захисних костюмах) обшукує та обробляє дезінфікуючою піною "
            "(4 Стреси, Порятунок Страху для половини).\n\n"
            "Вам видають кредитний стік О2 — ваш гаманець, паспорт і маяк на станції. "
            "Потрібно поповнити кредитами; податки та збори знімаються автоматично щодня.\n\n"
            "КОМАНДА-Q: БІЙ 25 (Піногасник — Порятунок Тіла або збитий з ніг; Імпульсні гвинтівки 5d10 шкоди) "
            "ШВИДКІСТЬ 35 | ІНСТИНКТ 25 | ОЧКИ ЗДОРОВ'Я 2 (20)",
        ),
    },
    {
        "id": 214, "icon": "⚖️", "source_page": 4, "sort_order": 3,
        "name": ("Laws & Contraband", "Законы и контрабанда", "Закони та контрабанда"),
        "desc": (
            "The rules of The Dream:\n"
            "» Have your O2 credstick on you at all times. Your movements are tracked.\n"
            "» Contraband: Laser Cutters, Explosives, Signal Jammers, Contagious Bioweapons, EMP tech.\n"
            "» Non-hull-piercing weapons can be kept; other weapons must be stowed in a rented locker "
            "(1cr/day/weapon). Key is tagged to the renter's fingerprint.\n"
            "» Don't enter unauthorized areas, particularly The Choke (pg. 32).\n\n"
            "Everything else is left to the parties involved. Street justice is pervasive. "
            "More substantial breaches are handled by Tempest Company and The Court.",

            "Правила Мечты:\n"
            "» Всегда держите при себе кредитный стик О2. Ваши перемещения отслеживаются.\n"
            "» Контрабанда: Лазерные резаки, Взрывчатка, Глушители сигналов, Заразное биооружие, ЭМИ-техника.\n"
            "» Оружие, не пробивающее корпус, можно оставить; остальное сдаётся в арендованный шкафчик "
            "(1 кр/день/единица). Ключ привязан к отпечатку пальца арендатора.\n"
            "» Не заходите в запрещённые зоны, особенно в Удавку.\n\n"
            "Всё остальное остаётся на усмотрение сторон. Уличное правосудие повсеместно. "
            "Более серьёзные нарушения рассматривают Tempest Company и Суд.",

            "Правила Мрії:\n"
            "» Завжди майте при собі кредитний стік О2. Ваші пересування відстежуються.\n"
            "» Контрабанда: Лазерні різаки, Вибухівка, Глушники сигналів, Заразна біозброя, ЕМІ-техніка.\n"
            "» Зброю, що не пробиває корпус, можна залишити; іншу здають у орендовану шафу "
            "(1 кр/день/одиниця). Ключ прив'язаний до відбитку пальця орендаря.\n"
            "» Не заходьте в заборонені зони, особливо в Задушу.\n\n"
            "Все інше залишається на розсуд сторін. Вуличне правосуддя повсюдне. "
            "Серйозніші порушення розглядають Tempest Company та Суд.",
        ),
    },
    {
        "id": 215, "icon": "💳", "source_page": 4, "sort_order": 4,
        "name": ("Fees & Costs", "Сборы и стоимость", "Збори та вартість"),
        "desc": (
            "Docking Fee: 1,000cr + 100cr/day. Impounded vehicle fine: Hull × 100cr (+200cr/day impounded).\n"
            "Oxygen Tax: 10cr/day/person. 50cr/day/person during major events (e.g. at The Court).\n"
            "Seller's License: 2,000cr. Allows selling goods aboard The Dream; without it you can only buy.\n"
            "Weapon Locker: 1cr/day/weapon. All hull-breachable weapons must be placed in a locker.\n"
            "Bribe: 2d10cr for minor manifest issues; 5d10cr for major manifest issues.\n"
            "Re-fueling: 2d10×1,000cr/fuel unit. Reroll monthly as prices fluctuate.\n\n"
            "Repairs: 75kcr/Hull. Upgrades: 12mcr/Hull. 50% downpayment required.\n"
            "Turnaround: 1d10 days (repairs) / 1d10 weeks (upgrades). 10% chance cargo stolen.",

            "Плата за стоянку: 1 000 кр + 100 кр/день. Штраф за конфискацию: Корпус × 100 кр (+200 кр/день).\n"
            "Налог на кислород: 10 кр/день/чел. 50 кр/день/чел. во время крупных событий (напр. в Суде).\n"
            "Лицензия продавца: 2 000 кр. Позволяет продавать товары на Мечте; без неё — только покупка.\n"
            "Оружейный шкафчик: 1 кр/день/единица. Всё пробивающее корпус оружие сдаётся в шкафчик.\n"
            "Взятка: 2d10 кр за незначительные проблемы с манифестом; 5d10 кр за серьёзные.\n"
            "Дозаправка: 2d10×1 000 кр/единица топлива. Цены пересматриваются ежемесячно.\n\n"
            "Ремонт: 75 ккр/Корпус. Модернизация: 12 мкр/Корпус. Требуется аванс 50%.\n"
            "Срок: 1d10 дней (ремонт) / 1d10 недель (модернизация). 10% шанс кражи груза.",

            "Плата за стоянку: 1 000 кр + 100 кр/день. Штраф за конфіскацію: Корпус × 100 кр (+200 кр/день).\n"
            "Податок на кисень: 10 кр/день/особа. 50 кр/день/особа під час великих подій (напр. у Суді).\n"
            "Ліцензія продавця: 2 000 кр. Дозволяє продавати товари на Мрії; без неї — лише купівля.\n"
            "Зброярський шафа: 1 кр/день/одиниця. Вся зброя, що пробиває корпус, здається в шафу.\n"
            "Хабар: 2d10 кр за незначні проблеми з маніфестом; 5d10 кр за серйозні.\n"
            "Дозаправка: 2d10×1 000 кр/одиниця палива. Ціни переглядаються щомісяця.\n\n"
            "Ремонт: 75 ккр/Корпус. Модернізація: 12 мкр/Корпус. Потрібна передоплата 50%.\n"
            "Термін: 1d10 днів (ремонт) / 1d10 тижнів (модернізація). 10% шанс крадіжки вантажу.",
        ),
    },
    {
        "id": 216, "icon": "💬", "source_page": 10, "sort_order": 5,
        "name": ("Rumors", "Слухи", "Чутки"),
        "desc": (
            "1 rumor costs 1kcr (ask Loshe at the Dry Dock, or Sem at the Stellar Burn).",
            "1 слух стоит 1 ккр (спросите Лоше в сухом доке или Сема в Звёздном ожоге).",
            "1 чутка коштує 1 ккр (запитайте Лоше в сухому доку або Сема у Зоряному опіку).",
        ),
        "dice": {
            "die": "d10",
            "entries": [
                {"min": 1,  "max": 1,  "text": "There are creatures growing in The Choke."},
                {"min": 2,  "max": 2,  "text": "Yandee is secretly an android."},
                {"min": 3,  "max": 3,  "text": "Cutter is looking to overthrow Yandee."},
                {"min": 4,  "max": 4,  "text": "Ukko/Ukka is a Hunglung sympathizer."},
                {"min": 5,  "max": 5,  "text": "Imogene Kane is planning an uprising."},
                {"min": 6,  "max": 6,  "text": "Sycorax makes installing cybermods easy."},
                {"min": 7,  "max": 7,  "text": "Angus knows everything about everyone."},
                {"min": 8,  "max": 8,  "text": "Brunhildh keeps a pet monster in the cells."},
                {"min": 9,  "max": 9,  "text": "Something called 'Caliban' is infecting the terminals."},
                {"min": 10, "max": 10, "text": "The Aarnivalkea can heal any disease."},
            ],
        },
        "dice_ru": [
            "В Удавке растут какие-то существа.",
            "Яндей — тайный андроид.",
            "Каттер хочет свергнуть Яндея.",
            "Укко/Укка симпатизирует Хунглунгам.",
            "Имоджен Кейн планирует восстание.",
            "Сикорах облегчает установку киберимплантов.",
            "Ангус знает всё обо всех.",
            "Брунхильд держит монстра в камерах.",
            "Нечто под названием «Калибан» заражает терминалы.",
            "Аарнивалкеа способна вылечить любую болезнь.",
        ],
        "dice_ua": [
            "У Задуші ростуть якісь істоти.",
            "Яндей — таємний андроїд.",
            "Каттер хоче скинути Яндея.",
            "Укко/Укка симпатизує Хунглунгам.",
            "Імоджен Кейн планує повстання.",
            "Сикорах полегшує встановлення кіберімплантів.",
            "Ангус знає все про всіх.",
            "Брунхільд тримає монстра у камерах.",
            "Щось під назвою «Калібан» заражає термінали.",
            "Аарнівалкеа здатна вилікувати будь-яку хворобу.",
        ],
    },
    {
        "id": 217, "icon": "🦠", "source_page": 6, "sort_order": 6,
        "name": ("Infection Rules (ACMD)", "Правила заражения (ACMD)", "Правила зараження (ACMD)"),
        "desc": (
            "ACMD (Acute Cybernetic Mutagenetic Disorder) infects individuals with cybermods, "
            "slowly transforming them into fully cybernetic beings that then merge into 'Caliban.'\n\n"
            "Infection Check: When triggered (contact with infected, puncturing a hazard suit in The Choke, etc.) "
            "make a Body Save. On failure you become Infected and your Infection Level increases by 1.\n\n"
            "Once per day you may make a Body Save instead of Resting to reduce Infection by 1 "
            "(1d5 on a Critical Success). On failure the Infection increases by 1 (1d5 on a Critical Failure).\n\n"
            "Infection Level effects (cumulative):\n"
            "1 — Weak Immune System. All Body Saves at [-].\n"
            "2 — Once/day Body Save or coughing fit for 1d5 rounds. Anyone within 10m makes Infection Check.\n"
            "3 — Fever & Chills. Take 1d10 DMG per day.\n"
            "4 — Random Mutation (Back Cover).\n"
            "5 — Frailty. All Strength & Speed Checks at [-]. Mutation.\n"
            "6 — 2d10 DMG per day. Random Malfunction.\n"
            "7 — Panic Check. [+] on Reaping Checks until cured. Mutation.\n"
            "8 — Install 1 cybermod per week or gain 2d10 Stress. Mutation.\n"
            "9 — Once/day Body Save or spew Nanoswarm (all in 20m make Infection Check at [-]). Mutation.\n"
            "10 — Lose control of PC and transform into Chokespawn.",

            "ACMD (Острое кибернетическое мутагенетическое расстройство) заражает носителей "
            "киберимплантов, постепенно превращая их в полностью кибернетических существ, "
            "которые затем сливаются с «Калибаном».\n\n"
            "Проверка заражения: При контакте с заражёнными, пробитии защитного костюма в Удавке и т.д. "
            "сделайте Спасбросок Тела. При провале вы заражаетесь, Уровень заражения +1.\n\n"
            "Раз в день вместо отдыха можно сделать Спасбросок Тела для снижения заражения на 1 "
            "(1d5 при критическом успехе). При провале уровень растёт на 1 (1d5 при критическом провале).\n\n"
            "Эффекты уровней заражения (накопительно):\n"
            "1 — Слабый иммунитет. Все Спасброски Тела на [-].\n"
            "2 — Раз в день Спасбросок Тела или приступ кашля на 1d5 раундов. Все в 10м делают Проверку заражения.\n"
            "3 — Жар и озноб. 1d10 урона в день.\n"
            "4 — Случайная мутация.\n"
            "5 — Слабость. Все Проверки Силы и Скорости на [-]. Мутация.\n"
            "6 — 2d10 урона в день. Случайный сбой.\n"
            "7 — Проверка паники. [+] на Проверки извлечения до лечения. Мутация.\n"
            "8 — Устанавливайте 1 имплант в неделю или получайте 2d10 Стресса. Мутация.\n"
            "9 — Раз в день Спасбросок Тела или выброс нанороя (все в 20м делают Проверку заражения на [-]). Мутация.\n"
            "10 — Потеря контроля над персонажем, превращение в Чокспауна.",

            "ACMD (Гостре кібернетичне мутагенетичне розлад) заражає носіїв "
            "кіберімплантів, поступово перетворюючи їх на повністю кібернетичних істот, "
            "які потім зливаються з «Калібаном».\n\n"
            "Перевірка зараження: При контакті із зараженими, пробитті захисного костюма в Задуші тощо "
            "зробіть Порятунок Тіла. При провалі ви заражаєтеся, Рівень зараження +1.\n\n"
            "Раз на день замість відпочинку можна зробити Порятунок Тіла для зниження зараження на 1 "
            "(1d5 при критичному успіху). При провалі рівень зростає на 1 (1d5 при критичному провалі).\n\n"
            "Ефекти рівнів зараження (накопично):\n"
            "1 — Слабкий імунітет. Всі Порятунки Тіла на [-].\n"
            "2 — Раз на день Порятунок Тіла або напад кашлю на 1d5 раундів. Всі в 10м роблять Перевірку зараження.\n"
            "3 — Жар та озноб. 1d10 шкоди на день.\n"
            "4 — Випадкова мутація.\n"
            "5 — Слабкість. Всі Перевірки Сили та Швидкості на [-]. Мутація.\n"
            "6 — 2d10 шкоди на день. Випадкова несправність.\n"
            "7 — Перевірка паніки. [+] на Перевірки вилучення до лікування. Мутація.\n"
            "8 — Встановлюйте 1 імплант на тиждень або отримуйте 2d10 Стресу. Мутація.\n"
            "9 — Раз на день Порятунок Тіла або викид нанорою (всі в 20м роблять Перевірку зараження на [-]). Мутація.\n"
            "10 — Втрата контролю над персонажем, перетворення на Чокспауна.",
        ),
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# P34 STORYLINES  (C224–C228)
# ─────────────────────────────────────────────────────────────────────────────

P34_CONTENTS = [
    {
        "id": 224, "icon": "📖", "source_page": 5, "sort_order": 1,
        "name": ("How to Use This Module", "Как использовать этот модуль", "Як використовувати цей модуль"),
        "desc": (
            "Prospero's Dream works as a base of operations for an ongoing campaign or a pick-up-and-play one-shot.\n\n"
            "THREE STORYLINES: Each has three escalating Phases. Use them as:\n"
            "» Current Events — news and rumors each time players visit.\n"
            "» Seeds for play — players can investigate and prevent crises.\n"
            "» Session fodder — build missions around the power brokers involved.\n"
            "» Ignored entirely — you don't need them.\n\n"
            "PHASE ALTERATIONS: Boxes throughout the module note how each location changes by Phase and Storyline. "
            "E.g. 'Strike 1' = Phase 1 of the Teamster Strike. 'Unrest/Outbreak 2' = Phase 2 of either "
            "the Unrest or Outbreak storylines.\n\n"
            "ONE-SHOT IDEAS:\n"
            "» Pick a Major NPC job and run just that.\n"
            "» Build a session around a Timeline event.\n"
            "» Run Life Support 01 or The Burrows as a standalone.\n"
            "» Start players in Phase 3 and have them ESCAPE FROM PROSPERO'S DREAM.\n\n"
            "\"In a campaign, make them fall in love with The Dream. In a one-shot, make them hate it.\"",

            "Мечта Просперо работает как база для многосессионной кампании или быстрого one-shot.\n\n"
            "ТРИ СЮЖЕТНЫХ ЛИНИИ: У каждой три нарастающих фазы. Используйте их как:\n"
            "» Текущие события — новости и слухи при каждом посещении.\n"
            "» Завязки для игры — игроки расследуют и предотвращают кризисы.\n"
            "» Материал для сессий — стройте миссии вокруг власть имущих.\n"
            "» Игнорируйте полностью — они не обязательны.\n\n"
            "ИЗМЕНЕНИЯ ПО ФАЗАМ: Вставки по всему модулю показывают, как меняется локация. "
            "«Забастовка 1» = Фаза 1 забастовки Тимстеров. «Волнения/Вспышка 2» = Фаза 2 одной из двух линий.\n\n"
            "ИДЕИ ДЛЯ ONE-SHOT:\n"
            "» Возьмите задание одного из ключевых НПС.\n"
            "» Постройте сессию вокруг события Временной шкалы.\n"
            "» Проведите Систему жизнеобеспечения 01 или Норы как самостоятельное приключение.\n"
            "» Начните в Фазе 3 и попытайтесь СБЕЖАТЬ С МЕЧТЫ ПРОСПЕРО.\n\n"
            "«В кампании — влюбите их в Мечту. В one-shot — заставьте ненавидеть.»",

            "Мрія Просперо працює як база для тривалої кампанії або швидкого one-shot.\n\n"
            "ТРИ СЮЖЕТНІ ЛІНІЇ: Кожна має три фази, що наростають. Використовуйте їх як:\n"
            "» Поточні події — новини та чутки при кожному відвідуванні.\n"
            "» Завязки для гри — гравці розслідують і запобігають кризам.\n"
            "» Матеріал для сесій — будуйте місії навколо владних осіб.\n"
            "» Ігноруйте повністю — вони не обов'язкові.\n\n"
            "ЗМІНИ ЗА ФАЗАМИ: Вставки по всьому модулю показують, як змінюється локація. "
            "«Страйк 1» = Фаза 1 страйку Тімстерів. «Заворушення/Спалах 2» = Фаза 2 однієї з двох ліній.\n\n"
            "ІДЕЇ ДЛЯ ONE-SHOT:\n"
            "» Візьміть завдання одного з ключових НПС.\n"
            "» Побудуйте сесію навколо події Часової шкали.\n"
            "» Проведіть Систему життєзабезпечення 01 або Нори як самостійну пригоду.\n"
            "» Почніть у Фазі 3 і спробуйте ВТЕКТИ З МРІЇ ПРОСПЕРО.\n\n"
            "«У кампанії — закохайте їх у Мрію. У one-shot — змусьте ненавидіти.»",
        ),
    },
    {
        "id": 225, "icon": "🚚", "source_page": 6, "sort_order": 2,
        "name": ("Teamster Strike", "Забастовка Тимстеров", "Страйк Тімстерів"),
        "desc": (
            "Ex-pilot Reidmar runs Teamsters Local 32819L, which distributes Sycorax for Yandee. "
            "Tensions peaked after the Stratemeyer Syndicate captured a fleet of Reidmar's freighters. "
            "Yandee refuses to pay ransom; Local 32819L can't afford Tempest Co. to rescue them. "
            "If unresolved, the Teamsters will strike and steal the remaining Sycorax stock.\n\n"
            "PHASE 1: Reidmar's fleet captured. Demands Yandee send Tempest Co.\n"
            "→ Stratemeyer executes Teamsters on footage. Reidmar threatens general strike.\n\n"
            "PHASE 2: Strike! No ships enter or leave. Tempest overworked. Fuel/repairs ×5.\n"
            "→ Tempest strikebreakers arrest union leaders. Scabs allow some ships out for 30kcr.\n\n"
            "PHASE 3: Brutal violence. Teamsters vs. Novo Droogs and Tempest operators. Massive looting.\n"
            "→ If unresolved: The Dream is consumed by civil war.",

            "Бывший пилот Рейдмар возглавляет Местную 32819L Тимстеров, распространяющую Сикорах для Яндея. "
            "Напряжённость достигла пика, когда Синдикат Стратемейера захватил флот грузовиков Рейдмара. "
            "Яндей отказывается платить выкуп; Местная не может нанять Tempest Co. для спасения. "
            "Без решения Тимстеры объявят забастовку и уведут оставшийся Сикорах.\n\n"
            "ФАЗА 1: Флот захвачен. Рейдмар требует прислать Tempest Co.\n"
            "→ Синдикат казнит Тимстеров на видео. Рейдмар грозит общей забастовкой.\n\n"
            "ФАЗА 2: Забастовка! Корабли не входят и не выходят. Tempest перегружены. Топливо/ремонт ×5.\n"
            "→ Штрейкбрехеры Tempest арестовывают лидеров профсоюза. Скэбы выпускают часть судов за 30 ккр.\n\n"
            "ФАЗА 3: Жестокое насилие. Тимстеры против Дружинников и операторов Tempest. Массовый грабёж.\n"
            "→ Если не разрешить: Мечта погружается в гражданскую войну.",

            "Колишній пілот Рейдмар очолює Місцеву 32819L Тімстерів, що розповсюджує Сикорах для Яндея. "
            "Напруженість досягла піку, коли Синдикат Стратемейера захопив флот вантажівок Рейдмара. "
            "Яндей відмовляється платити викуп; Місцева не може найняти Tempest Co. для порятунку. "
            "Без вирішення Тімстери оголосять страйк і заберуть залишки Сикораху.\n\n"
            "ФАЗА 1: Флот захоплено. Рейдмар вимагає надіслати Tempest Co.\n"
            "→ Синдикат страчує Тімстерів на відео. Рейдмар загрожує загальним страйком.\n\n"
            "ФАЗА 2: Страйк! Кораблі не входять і не виходять. Tempest перевантажені. Паливо/ремонт ×5.\n"
            "→ Штрейкбрехери Tempest арештовують лідерів профспілки. Скеби випускають частину суден за 30 ккр.\n\n"
            "ФАЗА 3: Жорстоке насильство. Тімстери проти Дружинників та операторів Tempest. Масовий грабіж.\n"
            "→ Якщо не вирішити: Мрія занурюється в громадянську війну.",
        ),
    },
    {
        "id": 226, "icon": "🔥", "source_page": 6, "sort_order": 3,
        "name": ("Unrest in The Choke", "Волнения в Удавке", "Заворушення в Задуші"),
        "desc": (
            "Those who can't pay the O2 tax are sent to The Choke — a brutal debtors prison housing "
            "millions in destitute squalor. Revolution is coming: Imogene Kane and her insurgent "
            "resistance, the Hunglungs, plan to overthrow their Tempest Co. guards.\n\n"
            "PHASE 1: Hunglung footage demands all O2 debt paid off in 24hrs or bombings begin. "
            "Body Saves against infection at [+]. Mysterious figure in Slickbays. 2d10 die in Slickbay accident.\n"
            "→ Bombings in a random module. 2d100 dead. Tempest begins 'Search & Seize' at random.\n\n"
            "PHASE 2: Ukko/Ukka unmasked as Doptown rebel sympathizer. Standoff at The Farm between Tempest and the Church.\n"
            "→ The Choke quarantined. No one out. O2 debts doubled until leaders surrender.\n\n"
            "PHASE 3: Citizens from Doptown overrun the Airlock guards. War erupts in the corridors. "
            "Tempest Armored Troopers butcher civilians.\n"
            "→ If unresolved: The Dream falls to insurgency and martial law.",

            "Те, кто не может платить налог на кислород, оказываются в Удавке — жестокой долговой тюрьме "
            "для миллионов. Революция надвигается: Имоджен Кейн и её повстанцы — Хунглунги — "
            "планируют свергнуть охрану Tempest Co.\n\n"
            "ФАЗА 1: Хунглунги требуют погасить все долги за О2 за 24 часа или начнутся взрывы. "
            "Спасброски от заражения на [+]. Таинственная фигура в слик-боксах. 2d10 погибших в аварии.\n"
            "→ Взрывы в случайном модуле. 2d100 погибших. Tempest начинает «Обыск и изъятие».\n\n"
            "ФАЗА 2: Укко/Укка разоблачён как сочувствующий повстанцам. Противостояние на Ферме.\n"
            "→ Удавка на карантине. Никто не выходит. Долги за О2 удвоены до сдачи лидеров.\n\n"
            "ФАЗА 3: Жители Доптауна прорываются через ворота. Война в коридорах. "
            "Бронепехота Tempest уничтожает мирных жителей.\n"
            "→ Если не разрешить: Мечта падает под власть повстанцев и военного положения.",

            "Ті, хто не може платити податок на кисень, потрапляють до Задуші — жорсткої боргової тюрми "
            "для мільйонів. Революція наближається: Імоджен Кейн та її повстанці — Хунглунги — "
            "планують скинути охорону Tempest Co.\n\n"
            "ФАЗА 1: Хунглунги вимагають погасити всі борги за О2 за 24 години або почнуться вибухи. "
            "Порятунки від зараження на [+]. Таємна фігура в слік-боксах. 2d10 загиблих в аварії.\n"
            "→ Вибухи в випадковому модулі. 2d100 загиблих. Tempest починає «Обшук і вилучення».\n\n"
            "ФАЗА 2: Укко/Укка викритий як симпатик повстанців. Протистояння на Фермі.\n"
            "→ Задуша на карантині. Ніхто не виходить. Борги за О2 подвоєні до здачі лідерів.\n\n"
            "ФАЗА 3: Мешканці Доптауну прориваються через ворота. Війна в коридорах. "
            "Бронепіхота Tempest знищує мирних жителів.\n"
            "→ Якщо не вирішити: Мрія падає під владу повстанців і воєнного стану.",
        ),
    },
    {
        "id": 227, "icon": "🦠", "source_page": 6, "sort_order": 4,
        "name": ("ACMD Outbreak", "Вспышка ACMD", "Спалах ACMD"),
        "desc": (
            "Two decades ago Dr. Emil Bancali brought his dying daughter Ariel to The Dream to cure her "
            "rare disease through cybermods. The treatments failed; his inhumane experiments birthed ACMD "
            "(Acute Cybernetic Mutagenetic Disorder). Bancali was the first to succumb — he merged with the "
            "station itself and is now Caliban. As more people are infected Caliban gains power over The Dream "
            "until it becomes one singular grotesque organism.\n\n"
            "PHASE 1: First Chokespawn caught on station. Rumors ACMD plague comes through air filters.\n"
            "→ Packs of Chokespawn roam the corridors. Sycorax becomes scarce. Q-teams extort newcomers.\n\n"
            "PHASE 2: Every 24hrs a random module is taken over by Caliban. Husks and Chokespawn run rampant.\n"
            "→ Every inch of The Dream begins to morph. Metallic eyes appear. Corridors become throats.\n\n"
            "PHASE 3: Caliban takes over the entire station.\n"
            "→ Only solution: kill Caliban at his Heart (pg. 38). Then the station self-destructs in 1d10hrs.",

            "Двадцать лет назад доктор Эмиль Банкали привёз умирающую дочь Ариэль на Мечту, "
            "надеясь вылечить её редкую болезнь с помощью киберимплантов. Лечение провалилось; "
            "бесчеловечные эксперименты породили ACMD. Банкали стал первой жертвой — он слился "
            "со станцией и теперь он Калибан. Чем больше людей заражается, тем сильнее становится "
            "Калибан, пока Мечта не превратится в единый гротескный организм.\n\n"
            "ФАЗА 1: Первый Чокспаун пойман на станции. Слухи об ACMD через воздушные фильтры.\n"
            "→ Стаи Чокспаунов бродят по коридорам. Сикорах иссякает. Команды-Q вымогают у новичков.\n\n"
            "ФАЗА 2: Каждые 24 часа случайный модуль захватывает Калибан. Хаски и Чокспауны повсюду.\n"
            "→ Вся Мечта начинает мутировать. Появляются металлические глаза. Коридоры становятся глотками.\n\n"
            "ФАЗА 3: Калибан захватывает всю станцию.\n"
            "→ Единственное решение: убить Калибана в его Сердце. Затем станция самоуничтожится за 1d10 ч.",

            "Двадцять років тому доктор Еміль Банкалі привіз вмираючу доньку Аріель на Мрію, "
            "сподіваючись вилікувати її рідкісну хворобу кіберімплантами. Лікування провалилося; "
            "нелюдські експерименти породили ACMD. Банкалі став першою жертвою — він злився "
            "зі станцією і тепер він Калібан. Чим більше людей заражається, тим сильніше стає "
            "Калібан, поки Мрія не перетвориться на єдиний гротескний організм.\n\n"
            "ФАЗА 1: Перший Чокспаун спійманий на станції. Чутки про ACMD через повітряні фільтри.\n"
            "→ Зграї Чокспаунів бродять коридорами. Сикорах вичерпується. Команди-Q вимагають хабарів.\n\n"
            "ФАЗА 2: Кожні 24 год випадковий модуль захоплює Калібан. Хаски та Чокспауни скрізь.\n"
            "→ Вся Мрія починає мутувати. З'являються металеві очі. Коридори стають глотками.\n\n"
            "ФАЗА 3: Калібан захоплює всю станцію.\n"
            "→ Єдине рішення: вбити Калібана в його Серці. Потім станція самознищиться за 1d10 год.",
        ),
    },
    {
        "id": 228, "icon": "📅", "source_page": 7, "sort_order": 5,
        "name": ("Event Timeline", "Временная шкала событий", "Часова шкала подій"),
        "desc": (
            "If the PCs do nothing, these events unfold automatically across the three storylines. "
            "Each row is a Phase; move to the next when all events in the current Phase have occurred.\n\n"
            "TEAMSTER STRIKE:\n"
            "P1: Fleet captured — Syndicate sends execution footage — Reidmar threatens strike\n"
            "P2: Strike declared — Strikebreakers called in, scabs run ships at 30kcr\n"
            "P3: Brutal street warfare — Looting and rioting across The Dream\n\n"
            "UNREST IN THE CHOKE:\n"
            "P1: Bombing ultimatum footage — Bombings in random module (2d100 dead), Search & Seize begins\n"
            "P2: Ukko/Ukka unmasked — Choke quarantined, O2 debts doubled\n"
            "P3: Doptown overruns Airlock — Tempest Armored Troopers massacre civilians\n\n"
            "ACMD OUTBREAK:\n"
            "P1: First Chokespawn caught — Packs roam corridors, Sycorax scarce, Q-teams extort\n"
            "P2: Random module taken every 24hrs — Dream begins to morph, corridors become throats\n"
            "P3: Caliban takes over entirely",

            "Если персонажи ничего не предпринимают, события разворачиваются автоматически. "
            "Каждая строка — одна Фаза; переходите к следующей, когда все события фазы произошли.\n\n"
            "ЗАБАСТОВКА ТИМСТЕРОВ:\n"
            "Ф1: Флот захвачен — Синдикат рассылает видео казней — Рейдмар угрожает забастовкой\n"
            "Ф2: Забастовка объявлена — Штрейкбрехеры вызваны, скэбы гоняют суда за 30 ккр\n"
            "Ф3: Уличные бои — Грабёж и мародёрство по всей Мечте\n\n"
            "ВОЛНЕНИЯ В УДАВКЕ:\n"
            "Ф1: Видео с угрозой взрыва — Взрывы в случайном модуле (2d100 погибших), «Обыск и изъятие»\n"
            "Ф2: Укко/Укка разоблачён — Удавка на карантине, долги за О2 удвоены\n"
            "Ф3: Доптаун прорывает ворота — Бронепехота Tempest уничтожает мирных\n\n"
            "ВСПЫШКА ACMD:\n"
            "Ф1: Первый Чокспаун пойман — Стаи бродят по коридорам, Сикорах иссякает\n"
            "Ф2: Каждые 24 ч случайный модуль захватывает Калибан — Мечта мутирует\n"
            "Ф3: Калибан полностью захватывает станцию",

            "Якщо персонажі нічого не роблять, події розгортаються автоматично. "
            "Кожен рядок — одна Фаза; переходьте до наступної, коли всі події фази відбулися.\n\n"
            "СТРАЙК ТІМСТЕРІВ:\n"
            "Ф1: Флот захоплено — Синдикат розсилає відео страт — Рейдмар загрожує страйком\n"
            "Ф2: Страйк оголошено — Штрейкбрехери викликані, скеби гасають судна за 30 ккр\n"
            "Ф3: Вуличні бої — Грабіж та мародерство по всій Мрії\n\n"
            "ЗАВОРУШЕННЯ В ЗАДУШІ:\n"
            "Ф1: Відео з погрозою вибуху — Вибухи в випадковому модулі (2d100 загиблих), «Обшук і вилучення»\n"
            "Ф2: Укко/Укка викритий — Задуша на карантині, борги за О2 подвоєні\n"
            "Ф3: Доптаун прориває ворота — Бронепіхота Tempest знищує мирних\n\n"
            "СПАЛАХ ACMD:\n"
            "Ф1: Перший Чокспаун спійманий — Зграї бродять коридорами, Сикорах вичерпується\n"
            "Ф2: Кожні 24 год випадковий модуль захоплює Калібан — Мрія мутує\n"
            "Ф3: Калібан повністю захоплює станцію",
        ),
    },
]


def _insert_contents(conn: sqlite3.Connection, page_id: int, items: list[dict]) -> None:
    for item in items:
        cid        = item["id"]
        icon       = item["icon"]
        src_page   = item.get("source_page")
        sort_order = item.get("sort_order", cid)
        desc       = item.get("desc", ("", "", ""))
        dice_data  = item.get("dice")
        dice_ru    = item.get("dice_ru")
        dice_ua    = item.get("dice_ua")

        dice_json = json.dumps(dice_data) if dice_data else None

        conn.execute("""
            INSERT OR IGNORE INTO contents
                (id, icon, source_slug, source_page, dice, sort_order)
            VALUES (?, ?, 'apof', ?, ?, ?)
        """, (cid, icon, src_page, dice_json, sort_order))

        names = item["name"]
        descs = desc if desc else ("", "", "")

        for i, (lang, di) in enumerate([("en", None), ("ru", dice_ru), ("ua", dice_ua)]):
            name_text = names[i]
            desc_text = descs[i] if descs else ""

            # Build dice_entries JSON for this lang
            if dice_data and di:
                # Override text in entries
                entries = []
                for j, entry in enumerate(dice_data["entries"]):
                    entries.append({**entry, "text": di[j]})
                de_json = json.dumps(entries)
            else:
                de_json = None

            conn.execute("""
                INSERT OR IGNORE INTO content_i18n
                    (content_id, lang, name, desc, dice_entries)
                VALUES (?, ?, ?, ?, ?)
            """, (cid, lang, name_text, desc_text or None, de_json))

        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (?, ?, ?)
        """, (page_id, cid, sort_order))


def _seed(conn: sqlite3.Connection) -> None:
    _insert_contents(conn, page_id=32, items=P32_CONTENTS)
    _insert_contents(conn, page_id=34, items=P34_CONTENTS)


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        total = len(P32_CONTENTS) + len(P34_CONTENTS)
        print(f"Done — {total} content items added to P32 and P34.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
