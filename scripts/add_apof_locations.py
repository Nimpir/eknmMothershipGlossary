"""
scripts/add_apof_locations.py
A Pound of Flesh — P35 "The Station" with 8 locations as content items
placed directly on P35 (flat structure, no sub-pages).
Run after add_apof_source_pages.py.
Run: python scripts/add_apof_locations.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

CONTENTS = [
    {
        "id": 229, "icon": "🛸", "source_page": 10, "sort_order": 1,
        "name": ("01 Dry Dock", "01 Сухой Dok", "01 Сухий Dok"),
        "desc": (
            "The Dry Dock is hundreds of small ports. Sparks fly; shipbuilders scurry on scaffolding above massive ships.\n\n"
            "KEY AREAS:\n"
            "1. CLEAN ROOM — Q-Team strip search & disinfect. 1d5+1 Q-Team members.\n"
            "2. LOSHE'S OFFICE — Cramped, greasy. Safe contains plans for an experimental Jump-8 drive (4 Fuel).\n"
            "3. REPAIR BAY — Giant robotic limbs. Mechanics on watch.\n"
            "4. HANGAR BAY — Where your ship docks. 10% chance cargo stolen unless guards hired from Tempest.\n\n"
            "LOSHE (Dockmaster): COMBAT 55 (Exoskeleton bash 4d10 DMG) | INSTINCT 60 | HITS 3 (40)\n"
            "Exoskeleton: 4 arms, each capable of attacking or firing a weapon in one round. Reapable. Worth 40kcr.\n"
            "Personally oversees every ship. Hub of station information. Calm voice, always smoking. Wants to keep "
            "the dock running smoothly and get his 1-year sobriety chip.",

            "Сухой Dok — сотни маленьких портов. Искры летят; судостроители снуют по лесам над кораблями.\n\n"
            "КЛЮЧЕВЫЕ ЗОНЫ:\n"
            "1. ДЕЗИНФЕКЦИОННАЯ КОМНАТА — Команда-Q обыскивает и обрабатывает. 1d5+1 членов.\n"
            "2. КАБИНЕТ ЛОШЕ — Тесный, жирный. Сейф содержит планы экспериментального прыжкового двигателя Jump-8 (4 топлива).\n"
            "3. РЕМОНТНЫЙ ЦЕХ — Гигантские роботизированные конечности. Механики наблюдают.\n"
            "4. АНГАРНЫЙ ОТСЕК — Стоянка вашего корабля. 10% шанс кражи груза без охраны Tempest.\n\n"
            "ЛОШЕ (Начальник дока): БОЙ 55 (Удар экзоскелета 4d10 урона) | ИНСТИНКТ 60 | ОЗ 3 (40)\n"
            "Экзоскелет: 4 руки, каждая может атаковать или стрелять за раунд. Можно изъять. Стоит 40 ккр.\n"
            "Лично проверяет каждый корабль. Источник информации о станции. Спокойный голос, всегда курит сигары.",

            "Сухий Dok — сотні маленьких портів. Іскри летять; суднобудівники снують по риштуванню над кораблями.\n\n"
            "КЛЮЧОВІ ЗОНИ:\n"
            "1. ДЕЗІНФЕКЦІЙНА КІМНАТА — Команда-Q обшукує та обробляє. 1d5+1 членів.\n"
            "2. КАБІНЕТ ЛОШЕ — Тісний, жирний. Сейф містить плани експериментального двигуна Jump-8 (4 палива).\n"
            "3. РЕМОНТНИЙ ЦЕХ — Гігантські роботизовані кінцівки. Механіки спостерігають.\n"
            "4. АНГАРНИЙ ВІДСІК — Стоянка вашого корабля. 10% шанс крадіжки вантажу без охорони Tempest.\n\n"
            "ЛОШЕ (Начальник дока): БІЙ 55 (Удар екзоскелета 4d10 шкоди) | ІНСТИНКТ 60 | ОЗ 3 (40)\n"
            "Екзоскелет: 4 руки, кожна може атакувати або стріляти за раунд. Можна вилучити. Вартість 40 ккр.\n"
            "Особисто перевіряє кожен корабель. Джерело інформації про станцію. Спокійний голос, завжди курить сигари.",
        ),
    },
    {
        "id": 230, "icon": "🍹", "source_page": 12, "sort_order": 2,
        "name": ("02 The Stellar Burn", "02 Звёздный Ожог", "02 Зоряний Опік"),
        "desc": (
            "Dark, smoky, strobing lights and flashing lasers. The place to unwind and do 'business.' "
            "Security: Gundrones and Tempest Probies.\n\n"
            "1. SEM'S BAR (Club Level) — Jury 'Sem' Semenov runs the bar. Retina scan required for upper level. "
            "Dispenses a Rumor if you've bought a drink (see Rumors table).\n"
            "2. HEAVEN (Upper Level) — Private booths with sonic muting. VIP area. Yandee holds court here.\n"
            "3. THE ECSTACY (Lower Level) — Indyl's domain. Companionship for hire. 100cr cover.\n\n"
            "GUNDRONE: COMBAT 60 (SMG 4d10 DMG) | SPEED 75 | INSTINCT 25 | HITS 1 (15) | Flying\n"
            "TEMPEST PROBIE: COMBAT 25 (SMG 4d10 DMG) | SPEED 35 | INSTINCT 25 | HITS 2 (35)\n\n"
            "INDYL (Procurer): COMBAT 35 (Nanoblade 4d10 DMG or Laser pistol) | SPEED 65 | INSTINCT 85 | HITS 5 (15)\n"
            "Pheromone Transmitter: Body Save or [-] against Indyl. Poison Tongue: Body Save [-] or paralysed 1d10hrs.\n"
            "Indyl's bodyguards: Seraphs of Virtue (COMBAT 70, Electrified Lash 5d10 DMG, 85% clearance rate, 2mcr/target).",

            "Тёмный, дымный, мигающие огни и лазеры. Место для отдыха и 'дел'. "
            "Безопасность: Оружейные дроны и пробники Tempest.\n\n"
            "1. БАР СЕМА (Клубный уровень) — Джури «Сем» Семёнов за стойкой. Сканирование сетчатки для верхнего уровня.\n"
            "2. НЕБЕСА (Верхний уровень) — Приватные кабинки со звуковым заглушением. VIP-зона.\n"
            "3. ЭКСТАЗ (Нижний уровень) — Владения Индыл. Компания за деньги. 100 кр за вход.\n\n"
            "ОРУЖЕЙНЫЙ ДРОН: БОЙ 60 (ПП 4d10 урона) | СКР 75 | ИНС 25 | ОЗ 1 (15) | Летает\n"
            "ПРОБНИК TEMPEST: БОЙ 25 (ПП 4d10 урона) | СКР 35 | ИНС 25 | ОЗ 2 (35)\n\n"
            "ИНДЫЛ (Сводник/сводница): БОЙ 35 (Нанолезвие 4d10 / лазерный пистолет) | СКР 65 | ИНС 85 | ОЗ 5 (15)\n"
            "Феромонный передатчик: Спасбросок Тела или [-] против Индыл. Ядовитый язык: Тело [-] или парализован 1d10 ч.\n"
            "Телохранители Индыл: Серафимы Добродетели (БОЙ 70, Электрокнут 5d10 урона, 85% успеха, 2 мкр/цель).",

            "Темний, димний, миготливі вогні та лазери. Місце для відпочинку та 'справ'. "
            "Безпека: Зброярські дрони та пробники Tempest.\n\n"
            "1. БАР СЕМА (Клубний рівень) — Джурі «Сем» Семенов за стійкою. Сканування сітківки для верхнього рівня.\n"
            "2. НЕБЕСА (Верхній рівень) — Приватні кабінки зі звуковим заглушенням. VIP-зона.\n"
            "3. ЕКСТАЗ (Нижній рівень) — Владіння Індил. Компанія за гроші. 100 кр за вхід.\n\n"
            "ЗБРОЯРСЬКИЙ ДРОН: БІЙ 60 (ПП 4d10 шкоди) | ШВД 75 | ІНС 25 | ОЗ 1 (15) | Літає\n"
            "ПРОБНИК TEMPEST: БІЙ 25 (ПП 4d10 шкоди) | ШВД 35 | ІНС 25 | ОЗ 2 (35)\n\n"
            "ІНДИЛ (Звідник/звідниця): БІЙ 35 (Нанолезо 4d10 / лазерний пістолет) | ШВД 65 | ІНС 85 | ОЗ 5 (15)\n"
            "Феромонний передавач: Порятунок Тіла або [-] проти Індил. Отруйний язик: Тіло [-] або паралізований 1d10 год.\n"
            "Охоронці Індил: Серафими Чесноти (БІЙ 70, Електробатіг 5d10 шкоди, 85% успіху, 2 мкр/ціль).",
        ),
    },
    {
        "id": 231, "icon": "🥂", "source_page": 13, "sort_order": 3,
        "name": ("What's on the Menu", "Меню заведений", "Меню закладів"),
        "desc": (
            "SEM'S BAR:\n"
            "Chatter (beans, grubs, corn) 15cr | Moloko+ (milk, synthemesc, hallucinogen) 25cr | "
            "Ambrosia (midori, blue curacao, lime) 20cr | Victory Gin 12cr | Vesper 30cr | "
            "Cadre Cola 1cr | Smokey (mescal margarita) 15cr | Well Drink 10cr | Call Drink 20–75cr | Beer 5cr\n"
            "Sycorax (neon pink pill, +20 to cybermod install saves) 750cr/pill\n"
            "Body Saves for Drunkenness: [+] for a few drinks / normal for casual / [-] for a long night.\n\n"
            "HEAVEN (Upper Level):\n"
            "Private VIP Booth (sonic muting) 250cr | Balcony Access 50cr\n\n"
            "THE ECSTACY (Lower Level, 100cr cover):\n"
            "Private Dance (reduce 1d5 Stress [-]) 20cr | Hourly Rate (reduce 1d5 Stress [+]) 100cr | "
            "Overnight (reduce 1d10 Stress) 1,500cr | XP Slick recording 40cr/hr (your own) or 5kcr/hr (someone else's)",

            "БАР СЕМА:\n"
            "Болтовня (бобы, жучки, кукуруза) 15 кр | Молоко+ (молоко, синтемеск, галлюциноген) 25 кр | "
            "Амброзия (мидори, блю-кюрасао, лайм) 20 кр | Победный Джин 12 кр | Веспер 30 кр | "
            "Кадр-Кола 1 кр | Дымный (маргарита с мескалем) 15 кр | Обычный коктейль 10 кр | "
            "Фирменный коктейль 20–75 кр | Пиво 5 кр\n"
            "Сикорах (неоново-розовая таблетка, +20 к спасброскам при установке импланта) 750 кр/таб\n"
            "Спасброски от опьянения: [+] после нескольких / обычный для спокойного вечера / [-] для долгой ночи.\n\n"
            "НЕБЕСА (Верхний уровень):\n"
            "VIP-кабинка (звуковое заглушение) 250 кр | Доступ к балкону 50 кр\n\n"
            "ЭКСТАЗ (100 кр вход):\n"
            "Приватный танец (−1d5 Стресса [-]) 20 кр | Почасовая ставка (−1d5 Стресса [+]) 100 кр | "
            "На ночь (−1d10 Стресса) 1 500 кр | XP-слик 40 кр/ч (своё) / 5 ккр/ч (чужое)",

            "БАР СЕМА:\n"
            "Балачки (боби, жучки, кукурудза) 15 кр | Молоко+ (молоко, синтемеск, галюциноген) 25 кр | "
            "Амброзія (мідорі, блю-кюрасао, лайм) 20 кр | Переможний Джин 12 кр | Веспер 30 кр | "
            "Кадр-Кола 1 кр | Димний (маргарита з мескалем) 15 кр | Звичайний коктейль 10 кр | "
            "Фірмовий коктейль 20–75 кр | Пиво 5 кр\n"
            "Сикорах (неоново-рожева таблетка, +20 до порятунків при встановленні імпланта) 750 кр/таб\n"
            "Порятунки від сп'яніння: [+] після кількох / звичайний для спокійного вечора / [-] для довгої ночі.\n\n"
            "НЕБЕСА (Верхній рівень):\n"
            "VIP-кабінка (звукове заглушення) 250 кр | Доступ до балкону 50 кр\n\n"
            "ЕКСТАЗ (100 кр вхід):\n"
            "Приватний танець (−1d5 Стресу [-]) 20 кр | Погодинна ставка (−1d5 Стресу [+]) 100 кр | "
            "На ніч (−1d10 Стресу) 1 500 кр | XP-слік 40 кр/год (своє) / 5 ккр/год (чуже)",
        ),
    },
    {
        "id": 232, "icon": "🔪", "source_page": 14, "sort_order": 4,
        "name": ("03 The Chop Shop", "03 Мастерская", "03 Майстерня"),
        "desc": (
            "Overflowing with trash and grime. Run by the legendary cybersurgeon THE BABUSHKA and her "
            "holographic AI child ZHENYA. Access requires background check — must be on good terms with Yandee.\n\n"
            "1. ENTRANCE — Crowded. Zhenya greets visitors. 3 Augmented Toys hidden as guards "
            "[COMBAT 55, SMG+ 4d10[+] DMG + Frag Grenades, HITS 2 (10)].\n"
            "2. RECOVERY ROOM — 6 dingy bunks. One contains a melted horrific cybermod mutant. "
            "(Fear Save or 1d10 Stress.) 100cr/day.\n"
            "3. SYCORAX STASH — Babushka's anaesthetic. 1d10 barrels, guarded by Augmented Toy.\n"
            "4–7. OPERATING THEATERS — Babushka works ~20hrs/day in surgery. Room 7 quarantined for ACMD patients.\n"
            "8. BABUSHKA'S ROOM — Photo of Zhenya as a real boy. Note: 'Vera — one more trip and Y will let me home.'\n"
            "9. CYBERMOD STORAGE & REAPER BARN — Back tunnel to The Choke. 2d10 of each cybermod in stock.\n\n"
            "THE BABUSHKA: COMBAT 25 (Sawed-Off 2d10 DMG or MegaTranq) | INSTINCT 90 | HITS 2 (45)\n"
            "Cyber Savant: On any hit, may shut down one cybermod of target for the encounter.",

            "Завалена мусором и грязью. Управляется легендарным кибернетическим хирургом БАБУШКОЙ "
            "и её голографическим ИИ-ребёнком ЖЕНЕЙ. Нужен допуск — не должен быть на плохом счету у Яндея.\n\n"
            "1. ВХОД — Захламлён. Женя встречает посетителей. 3 Дополненных игрушки-охранника.\n"
            "2. КОМНАТА ВОССТАНОВЛЕНИЯ — 6 коек. Одна занята расплавленным мутантом-имплантатом. 100 кр/день.\n"
            "3. ЗАПАС СИКОРАХА — Анестетик Бабушки. 1d10 бочек, охраняется Дополненной игрушкой.\n"
            "4–7. ОПЕРАЦИОННЫЕ — Бабушка работает ~20 ч/день. Палата 7 — на карантине для ACMD.\n"
            "8. КОМНАТА БАБУШКИ — Фото Жени маленьким. Записка: «Вера — ещё один рейс, и Я отпустит домой».\n"
            "9. ХРАНЕНИЕ ИМПЛАНТОВ — Тоннель в Удавку. 2d10 каждого кибермода в запасе.\n\n"
            "БАБУШКА: БОЙ 25 (Обрез 2d10 / МегаТранк) | ИНСТИНКТ 90 | ОЗ 2 (45)\n"
            "Кибер-Мастер: При любом попадании отключает один имплант цели на время боя.",

            "Завалена сміттям і брудом. Керується легендарним кібернетичним хірургом БАБУСЕЮ "
            "та її голографічним ШІ-дитям ЖЕНЕЮ. Потрібен допуск — не повинен бути на поганому рахунку у Яндея.\n\n"
            "1. ВХІД — Захаращений. Женя зустрічає відвідувачів. 3 Доповнені іграшки-охоронці.\n"
            "2. КІМНАТА ВІДНОВЛЕННЯ — 6 ліжок. Одне зайняте розплавленим мутантом-імплантатом. 100 кр/день.\n"
            "3. ЗАПАС СИКОРАХУ — Анестетик Бабусі. 1d10 бочок, охороняється Доповненою іграшкою.\n"
            "4–7. ОПЕРАЦІЙНІ — Бабуся працює ~20 год/день. Палата 7 — на карантині для ACMD.\n"
            "8. КІМНАТА БАБУСІ — Фото Жені маленьким. Записка: «Віра — ще один рейс, і Я відпустить додому».\n"
            "9. ЗБЕРІГАННЯ ІМПЛАНТІВ — Тунель до Задуші. 2d10 кожного кіберімпланта в запасі.\n\n"
            "БАБУСЯ: БІЙ 25 (Обріз 2d10 / МегаТранк) | ІНСТИНКТ 90 | ОЗ 2 (45)\n"
            "Кібер-Майстер: При будь-якому влученні вимикає один імплант цілі на час бою.",
        ),
    },
    {
        "id": 233, "icon": "❄️", "source_page": 20, "sort_order": 5,
        "name": ("04 The Ice Box", "04 Морозильник", "04 Морозильник"),
        "desc": (
            "The Dream's slang for its highly illegal Synthetic Sleeving Facility and Slickbay venue.\n\n"
            "1. THE SLICKBAYS — Hundreds of human-sized pods. Enter virtual Slickworlds for education, "
            "escape, and pleasure. Install Slickware while logged in. After 1 month, in-world damage applies "
            "to Sanity. 'Hard mode' Slickworlds have no safety feature — damage applies immediately.\n"
            "2. THE RUNWAY — Minimalistic, surgically-lit. Sleeves paraded for inspection. "
            "Appointment only (ask Angus or The Babushka for an invite).\n"
            "3. THE NEMO MACHINE — Downloads memories for future upload into a Sleeve. "
            "Takes 24hrs. Sanity Save or forget last 1d10 days. Critical Failure: Panic Check + total amnesia.\n"
            "4. THE CRYOVATS — Enormous facility. Sleeves grown on spines like fruit. "
            "Sanity Save or 1d5 Stress on first viewing.\n"
            "5. THE STACKS — Cryostorage of backups and sleeves. Freezing cold. "
            "Body Save every round without protection or take 1d5 DMG.",

            "Сленговое название нелегального слик-боксного клуба и базы для смены тел.\n\n"
            "1. СЛИК-БОКСЫ — Сотни капсул. Вход в виртуальные слик-миры. Установка слик-ПО онлайн. "
            "После 1 месяца урон в мире бьёт по Рассудку. 'Хардмод' — без защиты, урон сразу.\n"
            "2. ВЗЛЁТНАЯ ПОЛОСА — Минималистичная, хирургически-освещённая. Тела-оболочки на показ. "
            "Только по записи (спросите Ангуса или Бабушку).\n"
            "3. МАШИНА НЕМО — Скачивает воспоминания для загрузки в тело-оболочку. 24 ч. "
            "Спасбросок Рассудка или забудьте 1d10 дней. Критический провал: паника + полная амнезия.\n"
            "4. КРИОВАНЫ — Огромный цех. Тела-оболочки растут на позвоночниках как плоды. "
            "Спасбросок Рассудка или 1d5 Стресса при первом просмотре.\n"
            "5. СТЕКИ — Криохранилище бэкапов и тел. Жуткий холод. "
            "Спасбросок Тела каждый раунд без защиты или 1d5 урона.",

            "Сленгова назва нелегального слік-боксного клубу та бази для зміни тіл.\n\n"
            "1. СЛІК-БОКСИ — Сотні капсул. Вхід у віртуальні слік-світи. Встановлення слік-ПЗ онлайн. "
            "Після 1 місяця шкода у світі б'є по Розсудку. 'Хардмод' — без захисту, шкода одразу.\n"
            "2. ЗЛІТНА СМУГА — Мінімалістична, хірургічно-освітлена. Тіла-оболонки на показ. "
            "Лише за записом (запитайте Ангуса або Бабусю).\n"
            "3. МАШИНА НЕМО — Скачує спогади для завантаження в тіло-оболонку. 24 год. "
            "Порятунок Розсудку або забудьте 1d10 днів. Критичний провал: паніка + повна амнезія.\n"
            "4. КРІОВАНИ — Величезний цех. Тіла-оболонки ростуть на хребтах як плоди. "
            "Порятунок Розсудку або 1d5 Стресу при першому перегляді.\n"
            "5. СТЕКИ — Кріосховище бекапів та тіл. Лютий холод. "
            "Порятунок Тіла щороку без захисту або 1d5 шкоди.",
        ),
    },
    {
        "id": 234, "icon": "💊", "source_page": 21, "sort_order": 6,
        "name": ("Ice Box Services", "Услуги Морозильника", "Послуги Морозильника"),
        "desc": (
            "SLEEVE TYPES:\n"
            "Reclamation Sleeve (memory-wiped prisoners): 100kcr. Reroll stats. 10% chance of random skill. "
            "10% chance of someone else's memories.\n"
            "Model-A Series: 500kcr. 10 physical models (A1–A10). All Stats/Saves −5. Heavily discriminated against.\n"
            "Atlas X Premium: 2.2mcr. Custom designed. +5 Str/Spd/Body. Recovery only 48hrs.\n"
            "Narcissus-1: 50mcr. Luxury. All new stats — spend 240 points between Str/Int/Combat/Spd. Recovery 12hrs.\n\n"
            "SERVICES:\n"
            "Sleeve Backup (NeMo Machine, 24hrs): 10kcr. Sanity Save or forget last 1d10 days.\n"
            "Sleeve Storage (monthly): 500cr\n"
            "Slickbay (1hr — enough to install a Slick): 50cr\n"
            "Slickworld (1 month — DIY or join a Clan Server): 100cr",

            "ТИПЫ ТЕЛ-ОБОЛОЧЕК:\n"
            "Рекламационное тело (заключённые с удалёнными воспоминаниями): 100 ккр. Перебросить хар-ки. "
            "10% шанс случайного навыка. 10% шанс чужих воспоминаний.\n"
            "Серия Модель-А: 500 ккр. 10 физических моделей (A1–A10). Все хар-ки/спасброски −5. Сильная дискриминация.\n"
            "Атлас X Премиум: 2,2 мкр. Индивидуальный дизайн. +5 Сила/Скорость/Тело. Восстановление 48 ч.\n"
            "Нарцисс-1: 50 мкр. Роскошь. Все новые хар-ки — 240 очков на Силу/Интеллект/Бой/Скорость. Восстановление 12 ч.\n\n"
            "УСЛУГИ:\n"
            "Резервная копия (Машина НеМо, 24 ч): 10 ккр. Спасбросок Рассудка или потеря 1d10 дней.\n"
            "Хранение тела (месяц): 500 кр\n"
            "Слик-бокс (1 ч — достаточно для установки слика): 50 кр\n"
            "Слик-мир (1 месяц — свой или клановый сервер): 100 кр",

            "ТИПИ ТІЛ-ОБОЛОНОК:\n"
            "Рекламаційне тіло (ув'язнені зі стертими спогадами): 100 ккр. Перекинути хар-ки. "
            "10% шанс випадкового навику. 10% шанс чужих спогадів.\n"
            "Серія Модель-А: 500 ккр. 10 фізичних моделей (A1–A10). Всі хар-ки/порятунки −5. Сильна дискримінація.\n"
            "Атлас X Преміум: 2,2 мкр. Індивідуальний дизайн. +5 Сила/Швидкість/Тіло. Відновлення 48 год.\n"
            "Нарцис-1: 50 мкр. Розкіш. Всі нові хар-ки — 240 очок на Силу/Інтелект/Бій/Швидкість. Відновлення 12 год.\n\n"
            "ПОСЛУГИ:\n"
            "Резервна копія (Машина НеМо, 24 год): 10 ккр. Порятунок Розсудку або втрата 1d10 днів.\n"
            "Зберігання тіла (місяць): 500 кр\n"
            "Слік-бокс (1 год — достатньо для встановлення сліка): 50 кр\n"
            "Слік-світ (1 місяць — власний або клановий сервер): 100 кр",
        ),
    },
    {
        "id": 235, "icon": "🌿", "source_page": 22, "sort_order": 7,
        "name": ("05 The Farm", "05 Ферма", "05 Ферма"),
        "desc": (
            "Run by the Evangelical Solarian Church. The Dream's food supply and an important holy site. "
            "Also the major drug producer for the Golyanovo II Bratva.\n\n"
            "1. THE SANCTUARY — Grand sunlit chapel. Ukko/Ukka leads meditations at 0600, 1200, 1800.\n"
            "2. THE SUN MARKET — Bustling farmer's market: fruits, vegetables, drugs, arts & crafts.\n"
            "3. THE GARDENS — Silent meditation gardens. Statue of Tonatiuh. 1d5 Gardener Monks.\n"
            "4. THE MONASTERY — Restricted to Solarian Monks (~40). Stone and wood architecture.\n"
            "5. THE DRUG LAB — Guarded by 2d10 Tempest Operators + 1d10 Solarian Scientists. "
            "Thousands of doses of any drug. Sycorax packaged here but secretly made at Farm Two.\n"
            "6. THE SEED VAULT — Cryogenic vault. Guarded by Tempest Armored Troopers [COMBAT 65, Armor 65].\n"
            "7. THE SOLARIUM — Massive artificial sun room. 100cr donation for access. Reduce Stress by 1.\n"
            "8. FARM ONE — Immense zero-g hydroponic farm. 2d10 Swarms of Cybernetic Drone Bees.\n"
            "9. THE AARNIVALKEA — The oldest living tree on a space station. Gargantuan. Lives on an island "
            "in a man-made lake. Restricted (5kcr donation). Secretly maintained through proprietary Solarian "
            "cybermods — its sterile fruit + Burrows fruit = Sycorax.\n"
            "10. FARM TWO (Secret) — Only rumored to exist. Reached through a hidden underwater entrance "
            "from The Tree. Where Sycorax is actually manufactured.",

            "Управляется Евангелической Солярианской Церковью. Источник еды Мечты и святое место. "
            "Также главный производитель наркотиков для Братвы Голяново II.\n\n"
            "1. СВЯТИЛИЩЕ — Солнечная часовня. Укко/Укка ведёт медитации в 06:00, 12:00, 18:00.\n"
            "2. СОЛНЕЧНЫЙ РЫНОК — Оживлённый рынок: фрукты, овощи, наркотики, ремёсла.\n"
            "3. САДЫ — Тихие медитационные сады. Статуя Тонатиу. 1d5 Садовников-монахов.\n"
            "4. МОНАСТЫРЬ — Только для монахов (~40). Архитектура из камня и дерева.\n"
            "5. ЛАБОРАТОРИЯ НАРКОТИКОВ — 2d10 операторов Tempest + 1d10 учёных-Солярианцев. Тысячи доз.\n"
            "6. ХРАНИЛИЩЕ СЕМЯН — Криогенное хранилище. Охраняется бронепехотой Tempest.\n"
            "7. СОЛЯРИЙ — Огромный искусственный солярий. 100 кр за вход. Снимает 1 Стресс.\n"
            "8. ФЕРМА ОДИН — Огромная гидропонная ферма в невесомости. 2d10 роёв Кибернетических пчёл.\n"
            "9. ААРНИВАЛКЕА — Старейшее дерево на космической станции. Гигантское. Его стерильный плод "
            "+ плод Нор = Сикорах.\n"
            "10. ФЕРМА ДВА (Секрет) — Только слухи. Скрытый вход под водой от Дерева. "
            "Здесь реально производится Сикорах.",

            "Керується Євангелічною Соляріанською Церквою. Джерело їжі Мрії та свята місця. "
            "Також головний виробник наркотиків для Братви Голяново II.\n\n"
            "1. СВЯТИЛИЩЕ — Сонячна каплиця. Укко/Укка веде медитації о 06:00, 12:00, 18:00.\n"
            "2. СОНЯЧНИЙ РИНОК — Жвавий ринок: фрукти, овочі, наркотики, ремесла.\n"
            "3. САДИ — Тихі медитаційні сади. Статуя Тонатіу. 1d5 Садівників-ченців.\n"
            "4. МОНАСТИР — Лише для ченців (~40). Архітектура з каменю та дерева.\n"
            "5. ЛАБОРАТОРІЯ НАРКОТИКІВ — 2d10 операторів Tempest + 1d10 вчених-Соляріанців. Тисячі доз.\n"
            "6. СХОВИЩЕ НАСІННЯ — Кріогенне сховище. Охороняється бронепіхотою Tempest.\n"
            "7. СОЛЯРІЙ — Величезна штучна кімната-солярій. 100 кр за вхід. Знімає 1 Стрес.\n"
            "8. ФЕРМА ОДИН — Величезна гідропонна ферма в невагомості. 2d10 роїв Кібернетичних бджіл.\n"
            "9. ААРНІВАЛКЕА — Найстаріше дерево на космічній станції. Гігантське. Його стерильний плід "
            "+ плід Нір = Сикорах.\n"
            "10. ФЕРМА ДВА (Секрет) — Лише чутки. Прихований вхід під водою від Дерева. "
            "Тут реально виробляється Сикорах.",
        ),
    },
    {
        "id": 236, "icon": "💉", "source_page": 23, "sort_order": 8,
        "name": ("Drugs", "Наркотики", "Наркотики"),
        "desc": (
            "Available at The Farm (Sun Market), Heaven (Stellar Burn), and various dealers.\n"
            "SYCORAX (entry 10): +20 to Body Saves for cybermod installation. Heals Xd10 DMG "
            "(X = slots of mods installed). Each use: mark a tally, roll d10 — if result ≤ tally, "
            "gain a Random Mutation then reset. Addictive.",
            "Доступны на Ферме (Солнечный рынок), в Небесах (Звёздный Ожог) и у торговцев.\n"
            "СИКОРАХ (запись 10): +20 к Спасброскам Тела при установке импланта. Исцеляет Xd10 урона "
            "(X = слотов имплантов установлено). При каждом приёме: отметь черту, брось d10 — "
            "если результат ≤ черте, получи Случайную мутацию и сбрось счётчик. Вызывает привыкание.",
            "Доступні на Фермі (Сонячний ринок), у Небесах (Зоряний Опік) та у дилерів.\n"
            "СИКОРАХ (запис 10): +20 до Порятунків Тіла при встановленні імпланта. Лікує Xd10 шкоди "
            "(X = слотів імплантів встановлено). При кожному прийомі: відміть рисочку, кинь d10 — "
            "якщо результат ≤ рисочці, отримай Випадкову мутацію та скинь лічильник. Викликає звикання.",
        ),
        "dice": {
            "die": "d10",
            "entries": [
                {"min": 1,  "max": 1,  "text": "Method — Eidetic memory for 2d10 min. Lower Intellect by 5. Addictive. 800cr"},
                {"min": 2,  "max": 2,  "text": "Liquid Sword — [+] on Combat Checks for 1d5 turns, then take 3d10 DMG. Addictive. 1,500cr"},
                {"min": 3,  "max": 3,  "text": "Daytona — Go first in initiative, extra action for 1d10 turns. Permanently reduce Speed by 1d10 after. 1kcr"},
                {"min": 4,  "max": 4,  "text": "Triumph — [+] on next 1d10 rolls. 1d5 Stress. Reduce max Health 2d10. Addictive. 2.5kcr"},
                {"min": 5,  "max": 5,  "text": "Soma — No Stress gain for 1d10 hrs. [-] on Speed Checks for 1d10 days. Min Stress +1. Addictive. 750cr"},
                {"min": 6,  "max": 6,  "text": "Ruckus — Permanently increase Strength by 1d10. Reduce Sanity by 1d10. 600cr"},
                {"min": 7,  "max": 7,  "text": "Seed — Gain a new Skill for 1d10 days. Lower a random Skill's bonus by 5. 2kcr"},
                {"min": 8,  "max": 8,  "text": "Stimspice — Read target's mind for 1d10 min. Gain 2 Stress. Sanity Save or Panic Check. Addictive. 30kcr"},
                {"min": 9,  "max": 9,  "text": "Slug — Mentally visit a virtual world shared by all current Slug takers for 1d10 hrs. Sanity Save or −2 Sanity per use. Addictive. 1kcr"},
                {"min": 10, "max": 10, "text": "Sycorax — +20 Body Save for cybermod install. Heals Xd10 DMG (X = mod slots). Mutation risk per use. Addictive. 750cr"},
            ],
        },
        "dice_ru": [
            "Метод — Фотографическая память на 2d10 мин. Интеллект −5. Привыкание. 800 кр",
            "Жидкий Меч — [+] к Бою на 1d5 ходов, затем 3d10 урона. Привыкание. 1 500 кр",
            "Дейтона — Первый в инициативе, доп. действие на 1d10 ходов. Постоянное снижение Скорости на 1d10. 1 ккр",
            "Триумф — [+] к следующим 1d10 броскам. 1d5 Стресса. Макс. здоровье −2d10. Привыкание. 2,5 ккр",
            "Сома — Нет Стресса 1d10 ч. [-] к Скорости 1d10 дней. Мин. Стресс +1. Привыкание. 750 кр",
            "Бунт — Постоянное увеличение Силы на 1d10. Рассудок −1d10. 600 кр",
            "Семя — Новый Навык на 1d10 дней. Случайный навык −5. 2 ккр",
            "Стимпряность — Читать мысли цели 1d10 мин. 2 Стресса. Спасбросок Рассудка или Паника. Привыкание. 30 ккр",
            "Слизь — Виртуальный мир всех принимающих Слизь на 1d10 ч. Рассудок −2 за приём. Привыкание. 1 ккр",
            "Сикорах — +20 Тело при установке. Исцеляет Xd10 (X = слоты). Риск мутации. Привыкание. 750 кр",
        ],
        "dice_ua": [
            "Метод — Фотографічна пам'ять на 2d10 хв. Інтелект −5. Звикання. 800 кр",
            "Рідкий Меч — [+] до Бою на 1d5 ходів, потім 3d10 шкоди. Звикання. 1 500 кр",
            "Дейтона — Перший в ініціативі, доп. дія на 1d10 ходів. Постійне зниження Швидкості на 1d10. 1 ккр",
            "Тріумф — [+] до наступних 1d10 кидків. 1d5 Стресу. Макс. здоров'я −2d10. Звикання. 2,5 ккр",
            "Сома — Немає Стресу 1d10 год. [-] до Швидкості 1d10 днів. Мін. Стрес +1. Звикання. 750 кр",
            "Бунт — Постійне збільшення Сили на 1d10. Розсудок −1d10. 600 кр",
            "Насіння — Новий Навик на 1d10 днів. Випадковий навик −5. 2 ккр",
            "Стимприправа — Читати думки цілі 1d10 хв. 2 Стреси. Порятунок Розсудку або Паніка. Звикання. 30 ккр",
            "Слиз — Віртуальний світ усіх, хто приймає Слиз, на 1d10 год. Розсудок −2 за прийом. Звикання. 1 ккр",
            "Сикорах — +20 Тіло при встановленні. Лікує Xd10 (X = слоти). Ризик мутації. Звикання. 750 кр",
        ],
    },
    {
        "id": 237, "icon": "🖥️", "source_page": 24, "sort_order": 9,
        "name": ("06 CANYONHEAVY.market", "06 CANYONHEAVY.market", "06 CANYONHEAVY.market"),
        "desc": (
            "Intergalactic haven for hackers run by prodigy Angus. Effectively the intelligence apparatus "
            "of the Golyanovo II Bratva. Access restricted to vetted clients (first met at The Stellar Burn).\n\n"
            "1. THE BATTLESTATIONS — Zero-G sphere coated in multi-terminal workstations. Console-Cowboys "
            "kick off and drift between terminals. Scoreboard in the center. Air thick with Daytona smoke.\n"
            "2. THE CANYONHEAVY DATACACHE — Zero-G nest of servers. Contains strange malware, leverage "
            "over corporations, and nuclear hacking tools. Guarded by 1d10 Mercenaries. "
            "If recovered and decrypted: 1d5bcr and CANYONHEAVY as a lifelong enemy.\n"
            "3. SYSOPS — Zero-G planning room. Hidden tunnel to The Ice Box Stacks (20% chance of "
            "Chokespawn encounter per pass).\n"
            "4. ANGUS'S OFFICE — Zero-G. Cramped and dingy. Terminals, mechanical keyboards, takeout boxes "
            "floating through the air. Pays for good information.",

            "Межгалактическое убежище хакеров под управлением виртуоза Ангуса. "
            "Фактически — разведывательный аппарат Братвы Голяново II. Вход только для проверенных клиентов.\n\n"
            "1. БОЕВЫЕ ПОСТЫ — Нулевая гравитация. Рабочие станции по всем стенам. "
            "Консольные Ковбои парят между терминалами. Воздух пропитан дымом Дейтоны.\n"
            "2. КЭШ ДАННЫХ — Нулевая гравитация. Серверы, вредоносное ПО, компромат на корпорации. "
            "Охраняется 1d10 наёмниками. При взломе: 1d5 млрд кр и CANYONHEAVY — враги на всю жизнь.\n"
            "3. СИСОПЫ — Нулевая гравитация. Скрытый тоннель к Стекам Морозильника (20% шанс Чокспауна).\n"
            "4. КАБИНЕТ АНГУСА — Нулевая гравитация. Тесный, грязный. Терминалы, еда в воздухе. "
            "Платит за хорошую информацию.",

            "Міжгалактичне притулок хакерів під управлінням віртуоза Ангуса. "
            "Фактично — розвідувальний апарат Братви Голяново II. Вхід лише для перевірених клієнтів.\n\n"
            "1. БОЙОВІ ПОСТИ — Нульова гравітація. Робочі станції по всіх стінах. "
            "Консольні Ковбої парять між терміналами. Повітря просочене димом Дейтони.\n"
            "2. КЕШ ДАНИХ — Нульова гравітація. Сервери, шкідливе ПЗ, компромат на корпорації. "
            "Охороняється 1d10 найманцями. При зламі: 1d5 млрд кр і CANYONHEAVY — вороги на все життя.\n"
            "3. СИСОПИ — Нульова гравітація. Прихований тунель до Стеків Морозильника (20% шанс Чокспауна).\n"
            "4. КАБІНЕТ АНГУСА — Нульова гравітація. Тісний, брудний. Термінали, їжа в повітрі. "
            "Платить за хорошу інформацію.",
        ),
    },
    {
        "id": 238, "icon": "🎯", "source_page": 25, "sort_order": 10,
        "name": ("CANYONHEAVY Missions", "Миссии CANYONHEAVY", "Місії CANYONHEAVY"),
        "desc": (
            "Roll d10 or assign. Pay on completion.",
            "Бросьте d10 или назначьте. Оплата при выполнении.",
            "Киньте d10 або призначте. Оплата при виконанні.",
        ),
        "dice": {
            "die": "d10",
            "entries": [
                {"min": 1,  "max": 1,  "text": "Infiltrate Local 32819L. Gain membership. Find dirt on Reidmar. Foment insurrection. 150kcr"},
                {"min": 2,  "max": 2,  "text": "Infiltrate the Golyonovo II Bratva. Become a Droog for Yandee. Report secretly to Angus. 250kcr"},
                {"min": 3,  "max": 3,  "text": "Locate and break into Farm Two. Find the formula for Sycorax production at The Farm. 2mcr"},
                {"min": 4,  "max": 4,  "text": "Contact Imogene Kane. Rumored to be in Doptown. 50kcr"},
                {"min": 5,  "max": 5,  "text": "Locate Dr. Bancali. Ask around in Doptown. 100kcr"},
                {"min": 6,  "max": 6,  "text": "Make contact with Hideo Kieslowski. Reclusive genius hiding in a private Slickworld (Ice Box) for over a decade. Convince him to help with the ACMD outbreak. 350kcr"},
                {"min": 7,  "max": 7,  "text": "Extract Anouk Falconetti from Sublevel C (Tempest HQ). Escort her to Loshe. 750kcr"},
                {"min": 8,  "max": 8,  "text": "Relay slickware message to Goblin X, currently held in a high security cell at The Court. 150kcr"},
                {"min": 9,  "max": 9,  "text": "Retrieve Brunhildh's terminal passcode. Hidden on a disc inside her library near The Court. 375kcr"},
                {"min": 10, "max": 10, "text": "Deliver Dead Drop. Visit specified private booth in Heaven (Stellar Burn) and hide package. Do not open. 100kcr"},
            ],
        },
        "dice_ru": [
            "Проникнуть в Местную 32819L. Стать членом. Найти компромат на Рейдмара. 150 ккр",
            "Проникнуть в Братву Голяново II. Стать Дружинником Яндея. Тайно докладывать Ангусу. 250 ккр",
            "Найти и вскрыть Ферму Два. Найти формулу Сикораха. 2 мкр",
            "Связаться с Имоджен Кейн. По слухам — в Доптауне. 50 ккр",
            "Найти доктора Банкали. Разузнать в Доптауне. 100 ккр",
            "Найти Хидео Кислёвского. Затворник, прячется в слик-мире (Морозильник) >10 лет. Убедить помочь со вспышкой ACMD. 350 ккр",
            "Вытащить Анук Фальконетти с Подуровня C (штаб Tempest). Доставить к Лоше. 750 ккр",
            "Передать слик-сообщение Гоблину Икс в камере высокой безопасности (Суд). 150 ккр",
            "Достать код терминала Брунхильд. Спрятан на диске в её библиотеке у Суда. 375 ккр",
            "Доставить «мёртвый ящик». Зайти в приватную кабинку в Небесах (Звёздный ожог) и спрятать пакет. Не открывать. 100 ккр",
        ],
        "dice_ua": [
            "Проникнути до Місцевої 32819L. Стати членом. Знайти компромат на Рейдмара. 150 ккр",
            "Проникнути до Братви Голяново II. Стати Дружинником Яндея. Таємно доповідати Ангусу. 250 ккр",
            "Знайти та відкрити Ферму Два. Знайти формулу Сикораху. 2 мкр",
            "Зв'язатися з Імоджен Кейн. За чутками — в Доптауні. 50 ккр",
            "Знайти доктора Банкалі. Розпитати в Доптауні. 100 ккр",
            "Знайти Хідео Кіслевського. Затворник, ховається в слік-світі (Морозильник) >10 років. Переконати допомогти зі спалахом ACMD. 350 ккр",
            "Витягнути Анук Фальконетті з Підрівня C (штаб Tempest). Доставити до Лоше. 750 ккр",
            "Передати слік-повідомлення Гобліну Ікс у камері суворого режиму (Суд). 150 ккр",
            "Дістати код терміналу Брунхільд. Захований на диску в її бібліотеці біля Суду. 375 ккр",
            "Доставити «мертвий ящик». Зайти у приватну кабінку в Небесах (Зоряний опік) та сховати пакет. Не відкривати. 100 ккр",
        ],
    },
    {
        "id": 239, "icon": "🛠️", "source_page": 25, "sort_order": 11,
        "name": ("Hacking Tools", "Хакерские инструменты", "Хакерські інструменти"),
        "desc": (
            "Specialty gear sold by CANYONHEAVY. Roll d10 or pick.",
            "Специализированное снаряжение от CANYONHEAVY. Бросьте d10 или выберите.",
            "Спеціалізоване спорядження від CANYONHEAVY. Киньте d10 або виберіть.",
        ),
        "dice": {
            "die": "d10",
            "entries": [
                {"min": 1,  "max": 1,  "text": "TrashKid (5kcr) — Portable device that generates believable iconography and attack patterns for a fictitious cyber-gang, leading investigators astray."},
                {"min": 2,  "max": 2,  "text": "Splintermask (3kcr) — Transparent balaclava whose outer surface transmits jagged noise-patterns, defeating conventional and IR cameras. Stressful to Androids/AI."},
                {"min": 3,  "max": 3,  "text": "Racketball (4.5kcr) — Transmitters, speakers, and LEDs that aggressively output noise on all spectrums, destroying delicate sensors within 30m and stunning standard sensors for 1d10min."},
                {"min": 4,  "max": 4,  "text": "Office Assistant (55kcr) — Large suitcase: blank Android personality storage + I/O cables. A willing Android can download their personality into it and, if connected to an unwilling Android (Sanity Save to resist), control that body."},
                {"min": 5,  "max": 5,  "text": "Moebius Strip (3.5kcr) — Connected to a camera: endlessly replays 30 seconds of selected footage while incrementing the timestamp."},
                {"min": 6,  "max": 6,  "text": "Doorstop (500cr) — Small siphon-circuit that traps any open/close signal from a door so no notification is reported to the network."},
                {"min": 7,  "max": 7,  "text": "Remote Autohacker (250kcr) — Radio-operated, pre-programmable output device; allows remote Hacking Check at up to 100m range."},
                {"min": 8,  "max": 8,  "text": "Slaveshot (15kcr) — Dartgun (20m). On hit, injects malicious code into a Cybermod, giving the hacker remote access within 200m. Body Save to resist."},
                {"min": 9,  "max": 9,  "text": "Socketsnake (750cr) — Bundle of cables. Once connected to a device, any further input causes the snake to thrash, dealing 3d10 DMG to the user."},
                {"min": 10, "max": 10, "text": "Mommybird (75kcr) — Heavy cylinder of capacitors. Siphons power from a device over 60 seconds, then outputs all stored charge back in one surge."},
            ],
        },
        "dice_ru": [
            "ТрэшКид (5 ккр) — Устройство, генерирующее иконографию и паттерны атак вымышленной кибергруппировки.",
            "Осколочная маска (3 ккр) — Прозрачная балаклава, транслирующая помехи для камер. Стрессовый для андроидов/ИИ.",
            "Мяч-трещотка (4,5 ккр) — Излучает шум на всех частотах, уничтожая сенсоры в 30 м на 1d10 мин.",
            "Офис-ассистент (55 ккр) — Хранилище личности андроида + кабели. Контроль над другим андроидом (Спасбросок Рассудка).",
            "Лента Мёбиуса (3,5 ккр) — Зацикливает 30 сек видео с подменой метки времени на камере.",
            "Дверной стоппер (500 кр) — Ловит сигнал открытия/закрытия двери, чтобы сеть не получила уведомления.",
            "Удалённый автохакер (250 ккр) — Радиоустройство для удалённой Проверки взлома на расстоянии до 100 м.",
            "Выстрел-раб (15 ккр) — Дартган (20 м). Вводит вредоносный код в имплант, давая доступ в 200 м. Спасбросок Тела.",
            "Змея-разъём (750 кр) — Пучок кабелей. Любой ввод после подключения — хлыст и 3d10 урона пользователю.",
            "Птица-мама (75 ккр) — Конденсаторный цилиндр. Поглощает мощность 60 с, затем выбрасывает обратно.",
        ],
        "dice_ua": [
            "ТрешКід (5 ккр) — Пристрій, що генерує іконографію та паттерни атак вигаданої кіберзграї.",
            "Осколкова маска (3 ккр) — Прозора балаклава, що транслює завади для камер. Стресовий для андроїдів/ШІ.",
            "М'яч-тріскачка (4,5 ккр) — Випромінює шум на всіх частотах, знищуючи сенсори в 30 м на 1d10 хв.",
            "Офіс-асистент (55 ккр) — Сховище особистості андроїда + кабелі. Контроль над іншим андроїдом (Порятунок Розсудку).",
            "Стрічка Мебіуса (3,5 ккр) — Зациклює 30 сек відео з підміною мітки часу на камері.",
            "Дверний стопор (500 кр) — Ловить сигнал відкриття/закриття дверей, щоб мережа не отримала повідомлення.",
            "Віддалений автохакер (250 ккр) — Радіопристрій для віддаленої Перевірки зламу на відстані до 100 м.",
            "Постріл-раб (15 ккр) — Дартган (20 м). Вводить шкідливий код в імплант, даючи доступ у 200 м. Порятунок Тіла.",
            "Змія-роз'єм (750 кр) — Пучок кабелів. Будь-яке введення після підключення — удар і 3d10 шкоди користувачу.",
            "Птиця-мама (75 ккр) — Конденсаторний циліндр. Поглинає потужність 60 с, потім викидає назад.",
        ],
    },
    {
        "id": 240, "icon": "⚔️", "source_page": 26, "sort_order": 12,
        "name": ("07 The Court", "07 Суд", "07 Суд"),
        "desc": (
            "Presided over by Chief Adjudicator Brunhildh. The only law on a lawless station. "
            "Anyone breaking written laws or many unwritten ones is thrown in The Holding Cells to await "
            "trial by combat in The Cage.\n\n"
            "1. THE COURT — Throngs of spectators. Rampant side-betting. Stadium seating 10cr. Floor 2kcr. Boxed 10kcr/box.\n"
            "2. THE CAGE — Elevated revolving electrified stage (Body Save or 1d10 DMG + lose action if touched).\n"
            "3. THE BENCH — Balcony reserved for Brunhildh and the major power brokers of The Dream.\n"
            "4. HOLDING CELLS — Guarded by 1d10 Tempest Probies. Mostly O2 debtors. Cell 4A: the Rage of Caliban "
            "[COMBAT 80, Bash 3d10 DMG or x2 Mutated Arm Cannons 1d100 DMG, HITS 4 (30)].\n"
            "5. THE PIT — Animal odor. Horrific beasts. Heavily guarded.\n"
            "6. EXECUTIONERS' QUARTERS — Dozen spartan rooms. Electrolash, badge of office, robes. "
            "15% chance jailbroken O2 credstick (1d10×2kcr).\n\n"
            "TO BECOME AN ADVOCATE: Submit thumbscan contract with the Accused. "
            "Loss = no pay and Accused goes to The Choke. Win = paid. If you die, your estate is still paid.\n"
            "TO BECOME AN EXECUTIONER: Donate 150kcr to Bratva + win 10 Advocate bouts.",

            "Под председательством Главного арбитра Брунхильд. Единственный закон на беззаконной станции.\n\n"
            "1. СУД — Толпы зрителей. Тотальное боковое пари. Трибуна 10 кр. Пол 2 ккр. Ложа 10 ккр/ложа.\n"
            "2. КЛЕТКА — Вращающаяся электрифицированная сцена (Тело или 1d10 урона + потеря действия).\n"
            "3. СКАМЬЯ — Балкон Брунхильд и ключевых фигур Мечты.\n"
            "4. КАМЕРЫ — 1d10 пробников Tempest. В основном должники за О2. Камера 4А: Ярость Калибана.\n"
            "5. ЯМА — Запах животных. Ужасные твари. Сильная охрана.\n"
            "6. ПОКОИ ПАЛАЧЕЙ — Электрокнут, знак власти, мантия. 15% шанс взломанного стика (1d10×2 ккр).\n\n"
            "СТАТЬ АДВОКАТОМ: Подписать контракт с Обвиняемым. Проигрыш = нет оплаты, Обвиняемый в Удавку.\n"
            "СТАТЬ ПАЛАЧОМ: Пожертвовать 150 ккр Братве + выиграть 10 боёв как Адвокат.",

            "Під головуванням Головного арбітра Брунхільд. Єдиний закон на беззаконній станції.\n\n"
            "1. СУД — Натовпи глядачів. Тотальні ставки. Трибуна 10 кр. Підлога 2 ккр. Ложа 10 ккр/ложа.\n"
            "2. КЛІТКА — Обертова електрифікована сцена (Тіло або 1d10 шкоди + втрата дії).\n"
            "3. ЛАВА — Балкон Брунхільд і ключових осіб Мрії.\n"
            "4. КАМЕРИ — 1d10 пробників Tempest. Переважно боржники за О2. Камера 4А: Лють Калібана.\n"
            "5. ЯМА — Запах тварин. Жахливі істоти. Сильна охорона.\n"
            "6. ПОКОЇ КАТІВ — Електробатіг, знак влади, мантія. 15% шанс зламаного стіку (1d10×2 ккр).\n\n"
            "СТАТИ АДВОКАТОМ: Підписати контракт з Обвинуваченим. Програш = без оплати, Обвинувачений до Задуші.\n"
            "СТАТИ КАТОМ: Пожертвувати 150 ккр Братві + виграти 10 боїв як Адвокат.",
        ),
    },
    {
        "id": 241, "icon": "🐉", "source_page": 27, "sort_order": 13,
        "name": ("Pit Creatures", "Создания Ямы", "Істоти Ями"),
        "desc": (
            "Creatures kept in The Pit for use in trial by combat. Roll d10.",
            "Существа в Яме для использования в судебных поединках. Бросьте d10.",
            "Істоти у Ямі для використання в судових поєдинках. Киньте d10.",
        ),
        "dice": {
            "die": "d10",
            "entries": [
                {"min": 1,  "max": 1,  "text": "Infected Cyberfreak — COMBAT 20, Unarmed 1d5 DMG + Infect, SPEED 20, INSTINCT 20, HITS 3"},
                {"min": 2,  "max": 4,  "text": "1d10 Diamond Dogs — COMBAT 65, Bite/Bite/Claw 1d10 DMG, SPEED 85, INSTINCT 35, HITS 1 each"},
                {"min": 4,  "max": 5,  "text": "Sleevewraith — COMBAT 70, Rusty Blade 2d10 DMG, SPEED 45, INSTINCT 35, HITS 2. Reclamation Sleeve with combat slickware."},
                {"min": 6,  "max": 7,  "text": "Slicksquid — COMBAT 65, Tentacle/Tentacle 3d10 DMG, SPEED 50, INSTINCT 85, HITS 3. Combat via Slickbay, projected into The Court."},
                {"min": 8,  "max": 8,  "text": "The Brute — COMBAT 65, Swipe 5d10 DMG (hits multiple targets), SPEED 25, INSTINCT 75, HITS 5. Giant slow mech."},
                {"min": 9,  "max": 10, "text": "Specimen 869 — COMBAT 85, Psi-Blast (Sanity Save or Xd10 DMG + 1d10 Stress where X=rounds concentrating), SPEED 35, INSTINCT 95, HITS 2"},
            ],
        },
        "dice_ru": [
            "Заражённый Кибербезумец — БОЙ 20, Безоружный 1d5 + Заражение, СКР 20, ИНС 20, ОЗ 3",
            "1d10 Алмазных Псов — БОЙ 65, Укус/Укус/Коготь 1d10, СКР 85, ИНС 35, ОЗ 1 каждый",
            "Призрак Тела — БОЙ 70, Ржавый клинок 2d10, СКР 45, ИНС 35, ОЗ 2. Тело-оболочка с боевым слик-ПО.",
            "Слик-кальмар — БОЙ 65, Щупальце×2 3d10, СКР 50, ИНС 85, ОЗ 3. Боевой через слик-бокс.",
            "Громила — БОЙ 65, Удар 5d10 (несколько целей), СКР 25, ИНС 75, ОЗ 5. Гигантский медленный мех.",
            "Экземпляр 869 — БОЙ 85, Псибласт (Рассудок или Xd10+1d10 Стресса), СКР 35, ИНС 95, ОЗ 2",
        ],
        "dice_ua": [
            "Заражений Кібершаленець — БІЙ 20, Беззбройний 1d5 + Зараження, ШВД 20, ІНС 20, ОЗ 3",
            "1d10 Алмазних Псів — БІЙ 65, Укус/Укус/Пазур 1d10, ШВД 85, ІНС 35, ОЗ 1 кожен",
            "Примара Тіла — БІЙ 70, Іржавий клинок 2d10, ШВД 45, ІНС 35, ОЗ 2. Тіло-оболонка з бойовим слік-ПЗ.",
            "Слік-кальмар — БІЙ 65, Щупальце×2 3d10, ШВД 50, ІНС 85, ОЗ 3. Бойовий через слік-бокс.",
            "Громила — БІЙ 65, Удар 5d10 (кілька цілей), ШВД 25, ІНС 75, ОЗ 5. Гігантський повільний мех.",
            "Зразок 869 — БІЙ 85, Псіробласт (Розсудок або Xd10+1d10 Стресу), ШВД 35, ІНС 95, ОЗ 2",
        ],
    },
    {
        "id": 242, "icon": "🏛️", "source_page": 28, "sort_order": 14,
        "name": ("08 Tempest Company HQ", "08 Штаб Tempest Company", "08 Штаб Tempest Company"),
        "desc": (
            "A detachment of the Czernobog Private Military Corporation. 7 Platoons (42 Fireteams). "
            "Officers: 36. Armored Troopers: 54. Operators: 350. Probies: 906. Admin: 85.\n\n"
            "LEVEL 1 — HABITAT: Entry control. Client consultation, barracks, clinic, mess, officer quarters, "
            "recreation, quartermaster, trophy room, 'The Blue Rabbit' bar.\n"
            "LEVEL 2 — OPERATIONS: Mission control, monitoring stations, analyst offices, archives, planning rooms.\n"
            "LEVEL 3 — COMMANDER'S MANSION: Cutter's lavish penthouse. Guarded by The Zirnitra (elite Armored Troopers). "
            "Terminal reveals encrypted evidence of Cutter's disloyalty to Yandee.\n"
            "SUBLEVEL A — ARMAMENT (R2+): Armory, gunsmith, exosuit bays, foundry, ammo stores, slickbay training suite.\n"
            "SUBLEVEL B — R&D (R5+): Experimental exosuits, Caliban virus research, Sycorax vault, cybermod testing.\n"
            "SUBLEVEL C — CONTAINMENT (R7+): Enhanced interrogation cells, deep cryostorage, quarantine. "
            "30-minute elevator. Access to The Veins via hidden ducts.\n\n"
            "HOW TO JOIN: Complete one mission (roll 1d10 [-] on the Mission Table), donate all pay back to Tempest. "
            "Become Rank 1 Probie. To rank up: successfully complete missions equal to next rank.",

            "Отряд Частной военной корпорации Чернобог. 7 взводов (42 отделения). "
            "Офицеров: 36. Бронепехоты: 54. Операторов: 350. Новобранцев: 906. Администраторов: 85.\n\n"
            "УРОВЕНЬ 1 — ЖИЛОЙ: Контроль входа. Консультации клиентов, казармы, клиника, столовая, бар «Синий Кролик».\n"
            "УРОВЕНЬ 2 — ОПЕРАТИВНЫЙ: Центр управления миссиями, мониторинг, аналитика, архивы.\n"
            "УРОВЕНЬ 3 — ОСОБНЯК КОМАНДИРА: Пентхаус Каттера. Охраняют Зирнитра (элитная бронепехота). "
            "Терминал содержит зашифрованные доказательства нелояльности Каттера Яндею.\n"
            "ПОДУРОВЕНЬ А — ВООРУЖЕНИЕ (R2+): Арсенал, оружейник, боксы экзокостюмов, литейная, слик-тренировки.\n"
            "ПОДУРОВЕНЬ Б — РАЗРАБОТКИ (R5+): Экзокостюмы, исследование вируса Калибана, хранилище Сикораха.\n"
            "ПОДУРОВЕНЬ В — ИЗОЛЯЦИЯ (R7+): Допросные камеры, криохранилище, карантин. Лифт 30 мин.\n\n"
            "КАК ВСТУПИТЬ: Выполнить одну миссию (бросок d10 [-] на таблице миссий) и пожертвовать всю оплату. "
            "Стать Пробником R1. Для повышения: выполнять миссии = новому рангу.",

            "Загін Приватної військової корпорації Чорнобог. 7 взводів (42 відділення). "
            "Офіцерів: 36. Бронепіхоти: 54. Операторів: 350. Новобранців: 906. Адміністраторів: 85.\n\n"
            "РІВЕНЬ 1 — ЖИТЛОВИЙ: Контроль входу. Консультації клієнтів, казарми, клініка, їдальня, бар «Синій Кролик».\n"
            "РІВЕНЬ 2 — ОПЕРАТИВНИЙ: Центр управління місіями, моніторинг, аналітика, архіви.\n"
            "РІВЕНЬ 3 — ОСОБНЯК КОМАНДИРА: Пентхаус Каттера. Охороняє Зірніцра (елітна бронепіхота). "
            "Термінал містить зашифровані докази нелояльності Каттера Яндею.\n"
            "ПІДРІВЕНЬ А — ОЗБРОЄННЯ (R2+): Арсенал, зброяр, бокси екзокостюмів, ливарня, слік-тренування.\n"
            "ПІДРІВЕНЬ Б — РОЗРОБКИ (R5+): Екзокостюми, дослідження вірусу Калібана, сховище Сикораху.\n"
            "ПІДРІВЕНЬ В — ІЗОЛЯЦІЯ (R7+): Допитові камери, кріосховище, карантин. Ліфт 30 хв.\n\n"
            "ЯК ВСТУПИТИ: Виконати одну місію (кидок d10 [-] на таблиці місій) і пожертвувати всю оплату. "
            "Стати Пробником R1. Для підвищення: виконувати місії = новому рангу.",
        ),
    },
    {
        "id": 243, "icon": "📈", "source_page": 29, "sort_order": 15,
        "name": ("Tempest Co. Ranks", "Звания Tempest Co.", "Звання Tempest Co."),
        "desc": (
            "R0 RECRUIT: 1 job, donate all pay. H1 C20 Stun Baton 1d10 I20. Advance: 50cr, Salary: 100cr/wk. No benefits.\n"
            "R1 PROBIE: Assigned to a fireteam (R6+ CO). H2 C25 SMG 4d10 I25. Adv: 150cr, Sal: 600cr/wk. "
            "Access to Mission Table at [-].\n"
            "R2–R5 OPERATOR: Full member. H2 C35 Pulse Rifle 5d10 I25. Adv: 300cr. "
            "Rank×1kcr monthly salary. Access to Mission Table.\n"
            "R6–R7 SQUAD LEADER: Leader of 1 squad (10 troopers). H2 C45 Combat Shotgun 2d10 I35. Adv: 750cr. "
            "+1 Skill Point. All hired mercs gain +10 Loyalty.\n"
            "R8–R9 ARMORED TROOPER: Elite drop soldiers. H3 C65 Smart Rifle 1d10 I45 Armor:65. Adv: 2kcr. "
            "Exosuit (+20 Armor Save, [+] Strength, +5 Combat). Doubled salary.\n"
            "R10 PLATOON COMMANDER: Leader of 3 squads + Troopship. H2 C65 Revolver 3d10 I65. Adv: 5kcr. "
            "Command Skill. Hire mercs at 75% off. Assign missions to R2 squads for profit.\n\n"
            "EXOSUIT: Armor Save +20, [+] on Strength Checks, Combat +10, ×2 O2 tanks. 40kcr.\n"
            "DEMOTION: Fail missions = current rank, or lose soldiers = 3×rank.",

            "R0 НОВОБРАНЕЦ: 1 задание, вся оплата — в Tempest. ОЗ1 БОЙ20 Дубинка 1d10 ИНС20. Аванс: 50 кр, Зарплата: 100 кр/нед.\n"
            "R1 ПРОБНИК: В отделении (командир R6+). ОЗ2 БОЙ25 ПП 4d10 ИНС25. Аванс: 150 кр, З/п: 600 кр/нед. Таблица миссий на [-].\n"
            "R2–R5 ОПЕРАТОР: Полноправный член. ОЗ2 БОЙ35 Импульсная 5d10 ИНС25. Аванс: 300 кр. Ранг×1 ккр/месяц.\n"
            "R6–R7 КОМАНДИР ОТДЕЛЕНИЯ: 10 солдат. ОЗ2 БОЙ45 Дробовик 2d10 ИНС35. Аванс: 750 кр. +1 Навык. Наёмники +10 Лояльность.\n"
            "R8–R9 БРОНЕПЕХОТА: Элита. ОЗ3 БОЙ65 Умная 1d10 ИНС45 Броня:65. Аванс: 2 ккр. Экзокостюм. Удвоенная зарплата.\n"
            "R10 КОМАНДИР ВЗВОДА: 3 отделения + Troopship. ОЗ2 БОЙ65 Револьвер 3d10 ИНС65. Аванс: 5 ккр. "
            "Навык Командования. Наёмники −75% стоимости.\n\n"
            "ЭКЗОКОСТЮМ: Броня +20, [+] Сила, Бой +10, ×2 О2. 40 ккр.\n"
            "ПОНИЖЕНИЕ: Провалить миссии = текущий ранг, или потерять солдат = 3×ранг.",

            "R0 НОВОБРАНЕЦЬ: 1 завдання, вся оплата — в Tempest. ОЗ1 БІЙ20 Дубинка 1d10 ІНС20. Аванс: 50 кр, З/п: 100 кр/тиж.\n"
            "R1 ПРОБНИК: У відділенні (командир R6+). ОЗ2 БІЙ25 ПП 4d10 ІНС25. Аванс: 150 кр, З/п: 600 кр/тиж. Таблиця місій на [-].\n"
            "R2–R5 ОПЕРАТОР: Повноправний член. ОЗ2 БІЙ35 Імпульсна 5d10 ІНС25. Аванс: 300 кр. Ранг×1 ккр/міс.\n"
            "R6–R7 КОМАНДИР ВІДДІЛЕННЯ: 10 солдат. ОЗ2 БІЙ45 Дробовик 2d10 ІНС35. Аванс: 750 кр. +1 Навик. Найманці +10 Лояльність.\n"
            "R8–R9 БРОНЕПІХОТА: Еліта. ОЗ3 БІЙ65 Розумна 1d10 ІНС45 Броня:65. Аванс: 2 ккр. Екзокостюм. Подвоєна зарплата.\n"
            "R10 КОМАНДИР ВЗВОДУ: 3 відділення + Troopship. ОЗ2 БІЙ65 Револьвер 3d10 ІНС65. Аванс: 5 ккр. "
            "Навик Командування. Найманці −75% вартості.\n\n"
            "ЕКЗОКОСТЮМ: Броня +20, [+] Сила, Бій +10, ×2 О2. 40 ккр.\n"
            "ПОНИЖЕННЯ: Провалити місії = поточний ранг, або втратити солдат = 3×ранг.",
        ),
    },
    {
        "id": 244, "icon": "📋", "source_page": 29, "sort_order": 16,
        "name": ("Tempest Mission Table", "Таблица миссий Tempest", "Таблиця місій Tempest"),
        "desc": (
            "Roll 1d10 + current Rank. Cross off completed missions and add new ones. "
            "Higher rank = access to more dangerous (and lucrative) assignments.",
            "Бросьте 1d10 + текущий ранг. Вычёркивайте выполненные и добавляйте новые. "
            "Более высокий ранг = доступ к более опасным и прибыльным заданиям.",
            "Киньте 1d10 + поточний ранг. Викреслюйте виконані та додавайте нові. "
            "Вищий ранг = доступ до більш небезпечних і прибуткових завдань.",
        ),
        "dice": {
            "die": "d20",
            "entries": [
                {"min": 1,  "max": 1,  "text": "Outer Hull Patrol. Babysit repair crews as they fix cracks, bullet holes, check for illegally docked craft. 500cr"},
                {"min": 2,  "max": 3,  "text": "Night cycle corridor guard duty. Make 2 rounds of The Dream and deal with any issues. 1kcr"},
                {"min": 4,  "max": 4,  "text": "Teamster riots in (roll 1d10 on station map). Squash the rebellion. 20kcr per leader brought to Sublevel C"},
                {"min": 5,  "max": 5,  "text": "Insurgents organizing in Doptown. Capture their leader Imogene Kane and bring her to Sublevel C. 1mcr"},
                {"min": 6,  "max": 6,  "text": "Transfer accused prisoner from (roll 1d10 on station map) to The Court. 15kcr"},
                {"min": 7,  "max": 7,  "text": "Retrieve subject from The Choke (roll 1d10 on Choke map). 45kcr"},
                {"min": 8,  "max": 8,  "text": "Visit The Sink and hunt Chokespawn. See Col. Antonio in Doptown for details. 30kcr/kill"},
                {"min": 9,  "max": 9,  "text": "Accompany Dažbog Squad to The Burrows, retrieve 3d10 fruits, deliver to The Farm. 50kcr/fruit"},
                {"min": 10, "max": 10, "text": "R&D needs 10 infected corpses for vaccination research. Deliver to The Babushka. 15kcr/corpse"},
                {"min": 11, "max": 11, "text": "Black box retrieval from KIA operator on Calipse Citymoon (Jump 3). Requires Surgery Skill. 85kcr"},
                {"min": 12, "max": 12, "text": "Data breach traced to Ov Fire and Void. Capture the spy and escort to Sublevel C. 200kcr"},
                {"min": 13, "max": 13, "text": "Seraphs of Virtue haven't been paying up to Yandee. They owe 2.3mcr. Get them to pay or kill them. 250kcr"},
                {"min": 14, "max": 14, "text": "Hyperspace raiders captured the Chant for Ezkaton (Jump 2). Extract hostages. 55kcr/hostage"},
                {"min": 15, "max": 15, "text": "Retrieve artifact from The Alexis derelict in Sector Unknown. See Angus for details. 750kcr"},
                {"min": 16, "max": 16, "text": "Assassinate Yandee. Failed operations will be disavowed and Operators purged. 10mcr"},
                {"min": 17, "max": 17, "text": "Covertly inject experimental biotoxin to the life support unit on The Messe Noire. Observe field test. 3mcr"},
                {"min": 18, "max": 18, "text": "Deliver cybernetic weapons cargo to Orobas Moonbase (Jump 6). 7mcr"},
                {"min": 19, "max": 19, "text": "Transport cryopod containing Project Svetovid VII to research facility on Camelot-XIII (Jump 7). 1mcr"},
                {"min": 20, "max": 20, "text": "Transfer to Gabriel's Sword space station (Jump 10). Report to Cmdr. Mokosh. Prepare for war. 40mcr"},
            ],
        },
        "dice_ru": [
            "Патруль внешней обшивки. Сопровождение ремонтных бригад. 500 кр",
            "Охрана коридоров в ночном цикле. 2 обхода Мечты. 1 ккр",
            "Беспорядки Тимстеров (1d10 на карте). Подавить. 20 ккр за лидера в Подуровень В",
            "Повстанцы в Доптауне. Поймать лидера Имоджен Кейн и доставить в Подуровень В. 1 мкр",
            "Перевезти заключённого из (1d10 на карте) в Суд. 15 ккр",
            "Вытащить объект из Удавки (1d10 на карте). 45 ккр",
            "Охота на Чокспаунов в Провале. Детали у полк. Антонио. 30 ккр/убийство",
            "Сопровождать отряд Дажбог в Норы, собрать 3d10 плодов, доставить на Ферму. 50 ккр/плод",
            "НИОКР нужны 10 заражённых трупов. Доставить Бабушке. 15 ккр/труп",
            "Извлечение чёрного ящика с Calipse Citymoon (Прыжок 3). Нужен навык Хирургии. 85 ккр",
            "Утечка данных через «Огонь и Пустота». Поймать шпиона и доставить в Подуровень В. 200 ккр",
            "Серафимы Добродетели не платят Яндею. Долг 2,3 мкр. Заплатят или умрут. 250 ккр",
            "Пираты Гиперпространства захватили «Песнопение для Эзкатона» (Прыжок 2). Спасти заложников. 55 ккр/чел.",
            "Артефакт с деrelict-корабля «Алексис» (Сектор неизвестен). Детали у Ангуса. 750 ккр",
            "Убить Яндея. Провальные операции отрицаются, операторы уничтожаются. 10 мкр",
            "Тайно ввести биотоксин в систему жизнеобеспечения «Мессе Нуар». Наблюдать. 3 мкр",
            "Доставить кибероружие на Лунную базу Оробас (Прыжок 6). 7 мкр",
            "Транспортировать криокапсулу Проекта Световид VII на Камелот-XIII (Прыжок 7). 1 мкр",
            "Перевод на космостанцию «Меч Гавриила» (Прыжок 10). Доложить командиру Мокош. Готовиться к войне. 40 мкр",
        ],
        "dice_ua": [
            "Патруль зовнішньої обшивки. Супроводження ремонтних бригад. 500 кр",
            "Охорона коридорів у нічному циклі. 2 обходи Мрії. 1 ккр",
            "Заворушення Тімстерів (1d10 на карті). Придушити. 20 ккр за лідера на Підрівень В",
            "Повстанці в Доптауні. Зловити лідера Імоджен Кейн і доставити на Підрівень В. 1 мкр",
            "Перевезти ув'язненого з (1d10 на карті) до Суду. 15 ккр",
            "Витягнути об'єкт із Задуші (1d10 на карті). 45 ккр",
            "Полювання на Чокспаунів у Провалі. Деталі у полк. Антоніо. 30 ккр/вбивство",
            "Супроводити загін Дажбог до Нір, зібрати 3d10 плодів, доставити на Ферму. 50 ккр/плід",
            "НДДКР потрібні 10 заражених трупів. Доставити Бабусі. 15 ккр/труп",
            "Вилучення чорної скриньки з Calipse Citymoon (Стрибок 3). Потрібен навик Хірургії. 85 ккр",
            "Витік даних через «Вогонь і Порожнеча». Зловити шпигуна і доставити на Підрівень В. 200 ккр",
            "Серафими Чесноти не платять Яндею. Борг 2,3 мкр. Заплатять або помруть. 250 ккр",
            "Пірати Гіперпростору захопили «Пісноспів для Ескатона» (Стрибок 2). Врятувати заручників. 55 ккр/особу",
            "Артефакт з деrelict-корабля «Алексіс» (Сектор невідомий). Деталі у Ангуса. 750 ккр",
            "Вбити Яндея. Провальні операції відрікаються, оператори знищуються. 10 мкр",
            "Таємно ввести біотоксин у систему життєзабезпечення «Месс Нуар». Спостерігати. 3 мкр",
            "Доставити кіберзброю на Місячну базу Оробас (Стрибок 6). 7 мкр",
            "Транспортувати кріокапсулу Проекту Световид VII на Камелот-XIII (Стрибок 7). 1 мкр",
            "Переведення на космостанцію «Меч Гавриїла» (Стрибок 10). Доповісти командиру Мокош. Готуватися до війни. 40 мкр",
        ],
    },
]


# Sub-items linked via content_links — not direct P35 buttons.
SUB_ITEMS = {231, 234, 236, 238, 239, 241, 243, 244}

BASE = "images/A Pound of Flesh/ProsperosDreamLocs"
CONTENT_IMAGES: dict[int, str] = {
    229: f"{BASE}/1.DryDock.png",
    230: f"{BASE}/2.TheStellarBurn.png",
    232: f"{BASE}/3.TheChopShop.png",
    233: f"{BASE}/4.TheIceBox.png",
    235: f"{BASE}/5.TheFarm.png",
    237: f"{BASE}/6.CanyonHeavyMarket.png",
    240: f"{BASE}/7.TheCourt.png",
    242: f"{BASE}/8.TempestCompanyHQ.png",
}


def _insert_content(conn: sqlite3.Connection, page_id: int, item: dict, sort_override: int | None = None) -> None:
    cid           = item["id"]
    icon          = item["icon"]
    src_page      = item.get("source_page")
    item_sort     = item.get("sort_order", cid)    # natural sort order for contents table
    page_sort     = sort_override if sort_override is not None else item_sort  # for page_contents
    dice_data     = item.get("dice")
    dice_json     = json.dumps(dice_data) if dice_data else None
    image_url     = CONTENT_IMAGES.get(cid)

    conn.execute("""
        INSERT OR IGNORE INTO contents
            (id, icon, source_slug, source_page, dice, sort_order, image_url)
        VALUES (?, ?, 'apof', ?, ?, ?, ?)
    """, (cid, icon, src_page, dice_json, item_sort, image_url))
    if image_url:
        conn.execute(
            "UPDATE contents SET image_url = ? WHERE id = ? AND image_url IS NULL",
            (image_url, cid),
        )

    names = item["name"]
    descs = item["desc"]
    dice_ru = item.get("dice_ru")
    dice_ua = item.get("dice_ua")

    for i, (lang, d_override) in enumerate([("en", None), ("ru", dice_ru), ("ua", dice_ua)]):
        if dice_data and d_override:
            overridden = []
            for j, entry in enumerate(dice_data["entries"]):
                overridden.append({**entry, "text": d_override[j]})
            de_json = json.dumps(overridden)
        else:
            de_json = None

        conn.execute("""
            INSERT OR IGNORE INTO content_i18n
                (content_id, lang, name, desc, dice_entries)
            VALUES (?, ?, ?, ?, ?)
        """, (cid, lang, names[i], descs[i] if descs else None, de_json))

    if cid not in SUB_ITEMS:
        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (?, ?, ?)
        """, (page_id, cid, page_sort))


# Direct buttons on P35 — one per location.
# Sub-items (C231, C234, C236, C238-239, C241, C243-244) and dice tables
# (C329-C333) are linked via content_links from their parent location.
P35_CONTENT_ORDER = [
    (229,  1),
    (230,  4),
    (232,  6),
    (233,  8),
    (235, 10),
    (237, 12),
    (240, 15),
    (242, 19),
]

# content_id → (parent_page_id, sort_order_on_page)
_CONTENT_PAGE_MAP: dict[int, tuple[int, int]] = {
    cid: (35, so) for cid, so in P35_CONTENT_ORDER
}


def _seed(conn: sqlite3.Connection) -> None:
    # Insert content items; sub-items get content/i18n only (no page_contents)
    for item in CONTENTS:
        cid = item["id"]
        mapping = _CONTENT_PAGE_MAP.get(cid)
        parent_page = mapping[0] if mapping else 35
        sub_sort = mapping[1] if mapping else cid
        _insert_content(conn, page_id=parent_page, item=item, sort_override=sub_sort)

    # Ensure P35 has no linked_pages
    conn.execute("UPDATE pages SET linked_pages = '[]' WHERE id = 35")

    # Sub-item links: each location's secondary content accessible from its parent.
    # Only links between items created by THIS script (C229–C244).
    # Links to C329–C333 (from add_apof_missed_tables.py) are created there instead.
    sub_links = [
        (230, 231, 0),   # 02 The Stellar Burn → Heaven/Ecstasy
        (233, 234, 0),   # 04 The Ice Box → Ice Box Services
        (235, 236, 0),   # 05 The Farm → Sycorax
        (237, 238, 0),   # 06 CANYONHEAVY.market → CANYONHEAVY Missions
        (237, 239, 1),   # 06 CANYONHEAVY.market → CANYONHEAVY Stock
        (240, 241, 0),   # 07 The Court → Pit Fighters
        (242, 243, 0),   # 08 Tempest Company HQ → Tempest Missions
        (242, 244, 1),   # 08 Tempest Company HQ → Tempest Roster
    ]
    for from_id, to_id, sort in sub_links:
        conn.execute(
            "INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key, sort_order) VALUES (?, ?, 'related', ?)",
            (from_id, to_id, sort),
        )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(CONTENTS)} location content items added directly to P35 (flat structure).")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
