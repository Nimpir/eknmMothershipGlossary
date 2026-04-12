"""
scripts/add_wom_part5_generators.py
Warden's Operations Manual — Part 5: P28 Random Generators.
Creates P29 (Planet) and P30 (Settlement) as sub-pages of P28.
Seeds C199-C206: planet contents → P29, settlement contents → P30, C206 → P28.
Run: python scripts/add_wom_part5_generators.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


def dice_json(die: str, entries: list[dict]) -> str:
    return json.dumps({"die": die, "entries": entries}, ensure_ascii=False)


# ── C199 Planets (d10) ────────────────────────────────────────────────────────
# Table has 4 columns: Surface, Size/Gravity, Atmosphere, Climate
# Combined as: "Surface / Size / Atmosphere / Climate"
_PLANETS_ENTRIES = [
    {"min": 0, "max": 0, "text": "Liquid / Giant (Crushing Gravity) / Corrosive / Hellish"},
    {"min": 1, "max": 1, "text": "Liquid / Giant (Crushing Gravity) / Corrosive / Hot"},
    {"min": 2, "max": 2, "text": "Liquid / Mini-Giant (Heavy Gravity) / Toxic / Hot"},
    {"min": 3, "max": 3, "text": "Terrestrial / Mini-Giant (Heavy Gravity) / Toxic / Balmy"},
    {"min": 4, "max": 4, "text": "Terrestrial / Mini-Giant (Heavy Gravity) / Thin / Temperate"},
    {"min": 5, "max": 5, "text": "Terrestrial / Earth-Sized Planet (Normal Gravity) / Thin / Heavenly"},
    {"min": 6, "max": 6, "text": "Terrestrial / Earth-Sized Planet (Normal Gravity) / Terraformed / Rainy"},
    {"min": 7, "max": 7, "text": "Terrestrial / Dwarf Planet (Light Gravity) / Terraformed / Turbulent"},
    {"min": 8, "max": 8, "text": "Gas / Dwarf Planet (Light Gravity) / Terraformed / Cold"},
    {"min": 9, "max": 9, "text": "Gas / Dwarf Planet (Light Gravity) / Pristine / Freezing"},
]
_PLANETS_RU = [
    "Жидкая / Гигант (Дробящая гравитация) / Едкая / Адская",
    "Жидкая / Гигант (Дробящая гравитация) / Едкая / Горячая",
    "Жидкая / Мини-гигант (Тяжёлая гравитация) / Токсичная / Горячая",
    "Твёрдая / Мини-гигант (Тяжёлая гравитация) / Токсичная / Тёплая",
    "Твёрдая / Мини-гигант (Тяжёлая гравитация) / Разреженная / Умеренная",
    "Твёрдая / Земного размера (Нормальная гравитация) / Разреженная / Небесная",
    "Твёрдая / Земного размера (Нормальная гравитация) / Терраформированная / Дождливая",
    "Твёрдая / Карликовая (Лёгкая гравитация) / Терраформированная / Бурная",
    "Газовая / Карликовая (Лёгкая гравитация) / Терраформированная / Холодная",
    "Газовая / Карликовая (Лёгкая гравитация) / Первозданная / Морозная",
]
_PLANETS_UA = [
    "Рідка / Гігант (Роздроблювальна гравітація) / Їдка / Пекельна",
    "Рідка / Гігант (Роздроблювальна гравітація) / Їдка / Гаряча",
    "Рідка / Міні-гігант (Важка гравітація) / Токсична / Гаряча",
    "Тверда / Міні-гігант (Важка гравітація) / Токсична / Тепла",
    "Тверда / Міні-гігант (Важка гравітація) / Розріджена / Помірна",
    "Тверда / Земного розміру (Нормальна гравітація) / Розріджена / Небесна",
    "Тверда / Земного розміру (Нормальна гравітація) / Терраформована / Дощова",
    "Тверда / Карликова (Легка гравітація) / Терраформована / Бурхлива",
    "Газова / Карликова (Легка гравітація) / Терраформована / Холодна",
    "Газова / Карликова (Легка гравітація) / Первозданна / Морозна",
]
_PLANETS_DESC = (
    "Roll once; each result gives Surface / Size & Gravity / Atmosphere / Climate.\nCombine results to quickly sketch a planet.",
    "Бросьте один раз; каждый результат даёт Поверхность / Размер и гравитация / Атмосфера / Климат.",
    "Киньте один раз; кожен результат дає Поверхня / Розмір і гравітація / Атмосфера / Клімат.",
)

# ── C200 Settlement Locale (d100) ──────────────────────────────────────────────
_LOCALE_ENTRIES = [
    {"min": 0,  "max": 4,  "text": "CATENA — crater chain"},
    {"min": 5,  "max": 8,  "text": "CHAOS — broken terrain"},
    {"min": 9,  "max": 12, "text": "COLLIS — small hill"},
    {"min": 13, "max": 16, "text": "CRATER — impact valley"},
    {"min": 17, "max": 20, "text": "DORSUM — ridge"},
    {"min": 21, "max": 24, "text": "ERUPTIVE CENTER — volcano"},
    {"min": 25, "max": 28, "text": "FOSSA — trough"},
    {"min": 29, "max": 32, "text": "LABES — landslide"},
    {"min": 33, "max": 35, "text": "LABYRINTHUS — complex of intersecting valleys/ridges"},
    {"min": 36, "max": 39, "text": "LACUS — 'lake' or small plain"},
    {"min": 40, "max": 43, "text": "LANDING SITE"},
    {"min": 44, "max": 47, "text": "MARE — 'sea' on a moon"},
    {"min": 48, "max": 51, "text": "MENSA — mesa"},
    {"min": 52, "max": 56, "text": "MONS — mountain"},
    {"min": 57, "max": 60, "text": "MONTES — mountain range"},
    {"min": 61, "max": 65, "text": "PATERA — irregular crater"},
    {"min": 66, "max": 69, "text": "PLANITIA — low plain"},
    {"min": 70, "max": 73, "text": "PLANUM — high plain or plateau"},
    {"min": 74, "max": 77, "text": "RUPES — cliff or scarp"},
    {"min": 78, "max": 81, "text": "RIMA — fissure"},
    {"min": 82, "max": 85, "text": "SAXUM — boulder"},
    {"min": 86, "max": 89, "text": "TERRA — extensive land mass"},
    {"min": 90, "max": 94, "text": "THOLUS — small mountain"},
    {"min": 95, "max": 99, "text": "UNDAE — field of dunes"},
]
_LOCALE_RU = [
    "КАТЕНА — цепочка кратеров",
    "ХАОС — разломанный рельеф",
    "КОЛЛИС — небольшой холм",
    "КРАТЕР — ударная долина",
    "ДОРСУМ — гряда",
    "ВУЛКАНИЧЕСКИЙ ЦЕНТР — вулкан",
    "ФОССА — впадина",
    "ЛАБЕС — оползень",
    "ЛАБИРИНТ — комплекс пересекающихся долин/гряд",
    "ЛАКУС — 'озеро' или малая равнина",
    "ПОСАДОЧНАЯ ПЛОЩАДКА",
    "МАРЕ — 'море' на спутнике",
    "МЕНСА — меса",
    "МОНС — гора",
    "МОНТЕС — горный хребет",
    "ПАТЕРА — неправильный кратер",
    "ПЛАНИЦИЯ — низкая равнина",
    "ПЛАНУМ — высокая равнина или плато",
    "РУПЕС — обрыв или эскарп",
    "РИМА — трещина",
    "САКСУМ — валун",
    "ТЕРРА — обширный материк",
    "ТОЛУС — небольшая гора",
    "УНДАЕ — поле дюн",
]
_LOCALE_UA = [
    "КАТЕНА — ланцюжок кратерів",
    "ХАОС — розламаний рельєф",
    "КОЛЛІС — невеликий пагорб",
    "КРАТЕР — ударна долина",
    "ДОРСУМ — гряда",
    "ВУЛКАНІЧНИЙ ЦЕНТР — вулкан",
    "ФОССА — западина",
    "ЛАБЕС — зсув",
    "ЛАБІРИНТ — комплекс пересічних долин/гряд",
    "ЛАКУС — 'озеро' або мала рівнина",
    "МАЙДАНЧИК ДЛЯ ПОСАДКИ",
    "МАРЕ — 'море' на супутнику",
    "МЕНСА — меса",
    "МОНС — гора",
    "МОНТЕС — гірський хребет",
    "ПАТЕРА — нерегулярний кратер",
    "ПЛАНІЦІЯ — низька рівнина",
    "ПЛАНУМ — висока рівнина або плато",
    "РУПЕС — обрив або ескарп",
    "РІМА — тріщина",
    "САКСУМ — валун",
    "ТЕРРА — обширний материк",
    "ТОЛУС — невелика гора",
    "УНДАЕ — поле дюн",
]
_LOCALE_DESC = (
    "Geological features that serve as settlement locales on planets and moons.",
    "Геологические объекты, служащие локациями поселений на планетах и спутниках.",
    "Геологічні об'єкти, що служать локаціями поселень на планетах і супутниках.",
)

# ── C201 Control Faction (d10) ─────────────────────────────────────────────────
_CONTROL_ENTRIES = [
    {"min": 0, "max": 0, "text": "Religious Group"},
    {"min": 1, "max": 5, "text": "Corporation"},
    {"min": 6, "max": 7, "text": "Government"},
    {"min": 8, "max": 8, "text": "Union"},
    {"min": 9, "max": 9, "text": "Criminal Organization"},
]
_CONTROL_RU = [
    "Религиозная организация",
    "Корпорация",
    "Правительство",
    "Профсоюз",
    "Преступная организация",
]
_CONTROL_UA = [
    "Релігійна організація",
    "Корпорація",
    "Уряд",
    "Профспілка",
    "Злочинна організація",
]
_CONTROL_DESC = (
    "Roll to determine which type of organisation controls this settlement.",
    "Бросьте, чтобы определить тип организации, контролирующей поселение.",
    "Киньте, щоб визначити тип організації, що контролює поселення.",
)

# ── C202 Population (d10) ──────────────────────────────────────────────────────
_POPULATION_ENTRIES = [
    {"min": 0, "max": 0, "text": "A single person."},
    {"min": 1, "max": 2, "text": "A small handful of people."},
    {"min": 3, "max": 4, "text": "A few dozen people."},
    {"min": 5, "max": 6, "text": "Roughly a hundred people."},
    {"min": 7, "max": 7, "text": "A few hundred people."},
    {"min": 8, "max": 8, "text": "Roughly a thousand people."},
    {"min": 9, "max": 9, "text": "Overpopulated."},
]
_POPULATION_RU = [
    "Один человек.",
    "Небольшая горстка людей.",
    "Несколько десятков человек.",
    "Около сотни людей.",
    "Несколько сотен человек.",
    "Около тысячи человек.",
    "Перенаселено.",
]
_POPULATION_UA = [
    "Одна людина.",
    "Невелика жменька людей.",
    "Кілька десятків людей.",
    "Близько сотні людей.",
    "Кілька сотень людей.",
    "Близько тисячі людей.",
    "Перенаселено.",
]
_POPULATION_DESC = (
    "Roll to determine the population of a settlement.",
    "Бросьте, чтобы определить население поселения.",
    "Киньте, щоб визначити населення поселення.",
)

# ── C203 Factions Table (d100) ─────────────────────────────────────────────────
_FACTIONS_ENTRIES = [
    {"min": 0,  "max": 0,  "text": "The Seraphim Institute"},
    {"min": 1,  "max": 9,  "text": "The Outer Rim Colonial Marshalls (OCRM)"},
    {"min": 10, "max": 19, "text": "SEBACO Mining Ltd."},
    {"min": 20, "max": 26, "text": "The Teamster's Union"},
    {"min": 27, "max": 31, "text": "The Alliance of Hyperspace Jump Couriers"},
    {"min": 32, "max": 35, "text": "The Evangelical Solarian Church (AKA The Solarians)"},
    {"min": 36, "max": 40, "text": "Los Niños Basura"},
    {"min": 41, "max": 44, "text": "The Computer Coders Collective (AKA T-Triple-C)"},
    {"min": 45, "max": 48, "text": "PROJECT RICHTER"},
    {"min": 49, "max": 52, "text": "BAS-Lehman Ges.m.b.H"},
    {"min": 53, "max": 56, "text": "Tannhäuser Heavy Industries"},
    {"min": 57, "max": 60, "text": "The Synthetic Liberation Front"},
    {"min": 61, "max": 64, "text": "Parker-Vance Holding Company"},
    {"min": 65, "max": 68, "text": "The Interstellar Postal Inspection Service"},
    {"min": 69, "max": 72, "text": "The Komarov Squad"},
    {"min": 73, "max": 76, "text": "The Interstellar Asteroid Miners Association"},
    {"min": 77, "max": 80, "text": "The Jump-9 Club"},
    {"min": 81, "max": 84, "text": "Second Samael Church"},
    {"min": 85, "max": 89, "text": "The Zero-G Laborers Coalition (AKA Zed-GLC)"},
    {"min": 90, "max": 90, "text": "REDKNIFE Psyops Unit"},
    {"min": 91, "max": 91, "text": "The Astronavigator's Guild"},
    {"min": 92, "max": 92, "text": "The Organization"},
    {"min": 93, "max": 93, "text": "Revolutionary Forces of Luna"},
    {"min": 94, "max": 94, "text": "The Interplanetary Sex Workers Union"},
    {"min": 95, "max": 95, "text": "The Space Monkey Mafia"},
    {"min": 96, "max": 96, "text": "House Sivaranjan"},
    {"min": 97, "max": 97, "text": "Uplifted Dolphin Pod 67"},
    {"min": 98, "max": 98, "text": "Aleph Gate"},
    {"min": 99, "max": 99, "text": "FRIEND"},
]
_FACTIONS_TABLE_DESC = (
    "Roll to determine a faction present or relevant in the current setting.",
    "Бросьте, чтобы определить фракцию, присутствующую или актуальную в текущем сеттинге.",
    "Киньте, щоб визначити фракцію, присутню або актуальну у поточному сеттингу.",
)

# ── C204 Port Class (d10) ──────────────────────────────────────────────────────
_PORT_ENTRIES = [
    {"min": 0, "max": 0, "text": "X-Class Port — Abandoned. No services. Dangerous."},
    {"min": 1, "max": 5, "text": "C-Class Port — Basic docking and refuelling. Minimal amenities."},
    {"min": 6, "max": 7, "text": "B-Class Port — Standard services, local markets, some Shore Leave options."},
    {"min": 8, "max": 8, "text": "A-Class Port — Well-equipped hub. Good medical, Shore Leave, and trade options."},
    {"min": 9, "max": 9, "text": "S-Class Port — Major transit hub. Full services. Luxury Shore Leave available."},
]
_PORT_RU = [
    "Порт X-класса — Заброшен. Без сервиса. Опасен.",
    "Порт C-класса — Базовая стыковка и заправка. Минимальные удобства.",
    "Порт B-класса — Стандартные услуги, местные рынки, некоторые варианты берегового отпуска.",
    "Порт A-класса — Хорошо оснащённый узел. Хорошее медобслуживание, береговой отпуск и торговля.",
    "Порт S-класса — Крупный транзитный узел. Полный сервис. Доступен люксовый береговой отпуск.",
]
_PORT_UA = [
    "Порт X-класу — Покинутий. Без сервісу. Небезпечний.",
    "Порт C-класу — Базове стикування та заправка. Мінімальні зручності.",
    "Порт B-класу — Стандартні послуги, місцеві ринки, деякі варіанти берегового відпочинку.",
    "Порт A-класу — Добре обладнаний вузол. Хороше медобслуговування, береговий відпочинок і торгівля.",
    "Порт S-класу — Великий транзитний вузол. Повний сервіс. Доступний розкішний береговий відпочинок.",
]
_PORT_DESC = (
    "Roll to determine the class of a port encountered by the crew.",
    "Бросьте, чтобы определить класс порта, с которым столкнулась команда.",
    "Киньте, щоб визначити клас порту, з яким зіткнулася команда.",
)

# ── C205 Settlements Table (d100) ──────────────────────────────────────────────
# Three columns: Type | Conditions | Weird — combined with " — " separators
_SETTLEMENT_ENTRIES = [
    {"min": 0,  "max": 0,  "text": "Forced Relocation Slum — Under quarantine — Failed utopia."},
    {"min": 1,  "max": 9,  "text": "Terraformer Colony — Overworked, tired, low morale — Unsolved string of gruesome murders."},
    {"min": 10, "max": 19, "text": "Mining Colony — Business as usual — Home to powerful criminal syndicate."},
    {"min": 20, "max": 26, "text": "Colonial Settlement — Workers on strike — Local customs are strange, wary of outsiders."},
    {"min": 27, "max": 32, "text": "Marine Garrison — Hazardous working conditions — Deserted."},
    {"min": 33, "max": 35, "text": "Research Facility — Security forces in control — Secretly a corporate re-education camp."},
    {"min": 36, "max": 38, "text": "Corporate Operations Center — Gross managerial misconduct — Settlement has newfound religious significance."},
    {"min": 39, "max": 41, "text": "Manufacturing Complex — Frequent storms — Company secretly dosing the water."},
    {"min": 42, "max": 44, "text": "Deep Sea Research Base — Productivity low — Live hostage situation."},
    {"min": 45, "max": 47, "text": "Heavy Industry Complex — Corporate strikebreakers called in — Local environment is a radioactive wasteland."},
    {"min": 48, "max": 50, "text": "Shipping & Logistics Center — Hostile wildlife — Rapidly growing doomsday cult."},
    {"min": 51, "max": 53, "text": "Ore Refinery — Military blockade — Controlled by separatist militia."},
    {"min": 54, "max": 56, "text": "Forward Military Base — Lush overgrown wilderness — Collapse of local social order."},
    {"min": 57, "max": 59, "text": "Rural Backworld Installation — In desperate need of aid — Refugee crisis."},
    {"min": 60, "max": 62, "text": "Corporate Resupply Depot — Weather frighteningly unstable — Extinction event."},
    {"min": 63, "max": 65, "text": "Monitoring Outpost — Food shortage — Settlement has descended into anarchy."},
    {"min": 66, "max": 68, "text": "Off-World Training Installation — Colonists talking of joining a Union — Colonists report being replaced by imposters."},
    {"min": 69, "max": 71, "text": "Polar Research Station — Awaiting orders from corporate — Secret military operation recently arrived."},
    {"min": 72, "max": 74, "text": "Restricted Testing Facility — Local Union elections — Deadly viral outbreak."},
    {"min": 75, "max": 77, "text": "Maximum Security Prison Complex — Contract negotiation breakdown — Environmental collapse imminent."},
    {"min": 78, "max": 80, "text": "Stakeholder Camp — Low on supplies — Recent breakthrough discovery."},
    {"min": 81, "max": 83, "text": "Farming Colony — Massive crop failure — Settlement houses decadent corporate nobility."},
    {"min": 84, "max": 86, "text": "Prison, formerly a… (roll again) — Communications cut off — Colonists slowly disappearing."},
    {"min": 87, "max": 89, "text": "Autonomous Factory Zone — Company holiday celebrations — Strange black monolith unearthed."},
    {"min": 90, "max": 91, "text": "Independent Frontier Settlement — Under constant threat of terrorist attacks — Rumours of meddling from powerful AI."},
    {"min": 92, "max": 92, "text": "Covert Pirate Base — Local government crumbling — Colonists believe settlement haunted."},
    {"min": 93, "max": 93, "text": "Classified Corporate Installation — Rumours of layoffs — Android uprising imminent."},
    {"min": 94, "max": 94, "text": "Desolate Scrapworld — Overpopulation issue — Gigantic unidentifiable fossilised remains."},
    {"min": 95, "max": 95, "text": "Major Colonial Settlement — Settlement being shut down by corporate — Reports of interference by 'Celestials.'"},
    {"min": 96, "max": 96, "text": "Religious Compound — Petty bickering escalating out of control — Wreckage of spacecraft of unknown origin."},
    {"min": 97, "max": 97, "text": "Anti-corporate Rebel Base — Population entirely synthetic — Ruins of precursor star-faring civilisation found."},
    {"min": 98, "max": 98, "text": "Undisclosed Black Site — Co-opted by military as temporary base — Ancient gateway recently uncovered."},
    {"min": 99, "max": 99, "text": "Private C-Suite Game Preserve — Mutiny brewing — First Contact event."},
]
_SETTLEMENT_RU = [
    "Трущобы принудительного переселения — На карантине — Провалившаяся утопия.",
    "Колония терраформеров — Перегружены, устали, низкий моральный дух — Нераскрытая серия жестоких убийств.",
    "Горная колония — Всё как обычно — Здесь орудует мощный криминальный синдикат.",
    "Колониальное поселение — Рабочие бастуют — Местные обычаи странные, чужаков опасаются.",
    "Морской гарнизон — Опасные условия труда — Покинут.",
    "Исследовательский центр — Контроль у сил безопасности — Втайне является корпоративным лагерем перевоспитания.",
    "Корпоративный операционный центр — Грубое управленческое нарушение — Поселение обрело новое религиозное значение.",
    "Производственный комплекс — Частые бури — Компания тайно добавляет что-то в воду.",
    "Глубоководная исследовательская база — Низкая производительность — Активная ситуация с заложниками.",
    "Комплекс тяжёлой промышленности — Вызваны корпоративные штрейкбрехеры — Местная среда — радиоактивная пустошь.",
    "Центр логистики и перевозок — Враждебная дикая природа — Стремительно растущий апокалиптический культ.",
    "Рудный завод — Военная блокада — Под контролем сепаратистской милиции.",
    "Передовая военная база — Буйные джунгли — Распад местного общественного порядка.",
    "Захолустная установка — В отчаянной нужде в помощи — Кризис беженцев.",
    "Корпоративный склад снабжения — Пугающе нестабильная погода — Событие вымирания.",
    "Наблюдательный пост — Нехватка еды — Поселение скатилось в анархию.",
    "Внеземная учебная установка — Колонисты говорят о вступлении в профсоюз — Колонисты сообщают, что их заменяют самозванцами.",
    "Полярная исследовательская станция — Ждут приказов от корпоратов — Недавно прибыла тайная военная операция.",
    "Закрытый испытательный полигон — Местные выборы в профсоюз — Смертельная вирусная вспышка.",
    "Комплекс тюрьмы строгого режима — Срыв переговоров по контракту — Надвигается экологический коллапс.",
    "Лагерь акционеров — Мало запасов — Недавнее прорывное открытие.",
    "Фермерская колония — Массовый неурожай — В поселении обитает декадентская корпоративная знать.",
    "Бывшая тюрьма, ранее… (бросьте ещё раз) — Связь отрезана — Колонисты медленно исчезают.",
    "Зона автономного завода — Корпоративные праздничные торжества — Обнаружен странный чёрный монолит.",
    "Независимое фронтирное поселение — Под постоянной угрозой террористических атак — Слухи о вмешательстве мощного ИИ.",
    "Тайная пиратская база — Местное правительство рушится — Колонисты верят, что поселение проклято.",
    "Засекреченная корпоративная установка — Слухи о сокращениях — Восстание андроидов вот-вот произойдёт.",
    "Безлюдный свалочный мир — Проблема перенаселения — Гигантские неопознанные окаменелые останки.",
    "Крупное колониальное поселение — Поселение закрывается корпоратами — Сообщения о вмешательстве «Небожителей».",
    "Религиозная резиденция — Мелкие склоки выходят из-под контроля — Обломки космического корабля неизвестного происхождения.",
    "База антикорпоративных повстанцев — Население полностью синтетическое — Обнаружены руины звёздной цивилизации предшественников.",
    "Нераскрытый чёрный объект — Занят военными как временная база — Недавно обнаружен древний портал.",
    "Частный игровой заповедник C-Suite — Назревает мятеж — Событие Первого Контакта.",
]
_SETTLEMENT_UA = [
    "Нетрі примусового переселення — На карантині — Провалена утопія.",
    "Колонія терраформерів — Перевантажені, втомлені, низький моральний дух — Нерозкрита серія жорстоких вбивств.",
    "Гірська колонія — Все як завжди — Тут діє потужний злочинний синдикат.",
    "Колоніальне поселення — Робітники страйкують — Місцеві звичаї дивні, чужинців остерігаються.",
    "Морський гарнізон — Небезпечні умови праці — Покинутий.",
    "Дослідницький центр — Контроль у сил безпеки — Таємно є корпоративним табором перевиховання.",
    "Корпоративний операційний центр — Грубе управлінське порушення — Поселення набуло нового релігійного значення.",
    "Виробничий комплекс — Часті бурі — Компанія таємно додає щось у воду.",
    "Глибоководна дослідницька база — Низька продуктивність — Активна ситуація з заручниками.",
    "Комплекс важкої промисловості — Викликані корпоративні страйкбрехери — Місцеве середовище — радіоактивне пустище.",
    "Центр логістики та перевезень — Ворожа дика природа — Стрімко зростаючий апокаліптичний культ.",
    "Рудний завод — Військова блокада — Під контролем сепаратистської міліції.",
    "Передова військова база — Буйні джунглі — Розпад місцевого суспільного порядку.",
    "Захолустна установка — У відчайдушній потребі допомоги — Криза біженців.",
    "Корпоративний склад постачання — Лячно нестабільна погода — Подія вимирання.",
    "Спостережний пост — Нестача їжі — Поселення скотилося в анархію.",
    "Позаземна навчальна установка — Колоністи говорять про вступ у профспілку — Колоністи повідомляють, що їх замінюють самозванцями.",
    "Полярна дослідницька станція — Чекають наказів від корпорацій — Нещодавно прибула таємна військова операція.",
    "Закритий випробувальний полігон — Місцеві вибори у профспілку — Смертельний вірусний спалах.",
    "Комплекс тюрми суворого режиму — Зрив переговорів за контрактом — Наближається екологічний колапс.",
    "Табір акціонерів — Мало запасів — Нещодавнє проривне відкриття.",
    "Фермерська колонія — Масовий неврожай — У поселенні живе декадентська корпоративна знать.",
    "Колишня тюрма, раніше… (киньте ще раз) — Зв'язок відрізаний — Колоністи повільно зникають.",
    "Зона автономного заводу — Корпоративні святкові урочистості — Виявлено дивний чорний моноліт.",
    "Незалежне фронтирне поселення — Під постійною загрозою терористичних атак — Чутки про втручання потужного ШІ.",
    "Таємна піратська база — Місцевий уряд руйнується — Колоністи вважають, що поселення проклято.",
    "Засекречена корпоративна установка — Чутки про скорочення — Повстання андроїдів ось-ось станеться.",
    "Безлюдний смітниковий світ — Проблема перенаселення — Гігантські невпізнані скам'янілі залишки.",
    "Велике колоніальне поселення — Поселення закривається корпораціями — Повідомлення про втручання «Небожителів».",
    "Релігійна садиба — Дрібні сварки виходять з-під контролю — Уламки космічного корабля невідомого походження.",
    "База антикорпоративних повстанців — Населення повністю синтетичне — Виявлено руїни зіркової цивілізації попередників.",
    "Нерозкритий чорний об'єкт — Зайнятий військовими як тимчасова база — Нещодавно виявлено стародавні ворота.",
    "Приватний ігровий заповідник C-Suite — Назріває бунт — Подія Першого Контакту.",
]
_SETTLEMENT_DESC = (
    "Roll once for settlement Type, Conditions, and a Weird element. Each result provides all three.",
    "Бросьте один раз: один результат даёт Тип, Условия и Странность поселения.",
    "Киньте один раз: один результат дає Тип, Умови та Дивацтво поселення.",
)

# ── C206 Random Lore (d100) ────────────────────────────────────────────────────
_LORE_ENTRIES = [
    {"min": 0,  "max": 0,  "text": "The Maru Banking Colonies"},
    {"min": 1,  "max": 4,  "text": "False Europa"},
    {"min": 5,  "max": 8,  "text": "The Egosystem"},
    {"min": 9,  "max": 12, "text": "The MIDAS-12 Massacre"},
    {"min": 13, "max": 16, "text": "The Shadow Algorithm"},
    {"min": 17, "max": 20, "text": "Universal Remote"},
    {"min": 21, "max": 24, "text": "The Conway Machine"},
    {"min": 25, "max": 28, "text": "The Book of Sar"},
    {"min": 29, "max": 32, "text": "MOGUL: Maximum Prison Planet"},
    {"min": 33, "max": 36, "text": "The Orlov Incident"},
    {"min": 37, "max": 40, "text": "Fred, the Disappearing Man"},
    {"min": 41, "max": 44, "text": "The Creeping Fog"},
    {"min": 45, "max": 48, "text": "Mindpillers"},
    {"min": 49, "max": 52, "text": "The Precursors"},
    {"min": 53, "max": 56, "text": "Zygotean Mercenaries"},
    {"min": 57, "max": 60, "text": "The Teaman Murders"},
    {"min": 61, "max": 64, "text": "The Whispering Plague"},
    {"min": 65, "max": 68, "text": "Sea of Tranquility Conspiracy"},
    {"min": 69, "max": 72, "text": "UCSCV Mournbringer Flight 364"},
    {"min": 73, "max": 76, "text": "The Bracewell Autonomous Zone"},
    {"min": 77, "max": 80, "text": "Spasi, Otets, Syna"},
    {"min": 81, "max": 83, "text": "Cosmetic Vampire Hoax"},
    {"min": 84, "max": 84, "text": "IMG 2238"},
    {"min": 85, "max": 85, "text": "The Magnetic Typhoon"},
    {"min": 86, "max": 86, "text": "The Battle for Columbia Gate"},
    {"min": 87, "max": 87, "text": "The Spitz-Okoro Theorem"},
    {"min": 88, "max": 88, "text": "The Uplifted Possums"},
    {"min": 89, "max": 89, "text": "The Silent Century"},
    {"min": 90, "max": 90, "text": "Naktari War Syndrome"},
    {"min": 91, "max": 91, "text": "The Autumnal City at Bellona"},
    {"min": 92, "max": 92, "text": "Origin Point Zero"},
    {"min": 93, "max": 93, "text": "The Mountebank Game"},
    {"min": 94, "max": 94, "text": "The Helium Uprising"},
    {"min": 95, "max": 95, "text": "The Dearborn Corpse"},
    {"min": 96, "max": 96, "text": "Wombship"},
    {"min": 97, "max": 97, "text": "The Hymn of Saeeda Dawn"},
    {"min": 98, "max": 98, "text": "Divinity Strain"},
    {"min": 99, "max": 99, "text": "Rey Burtnolds is Alive and Well and Living on Casimir"},
]
_LORE_DESC = (
    "Roll for a cryptic piece of galactic lore — a rumour, legend, or whispered name that can inspire an adventure or haunt the setting.",
    "Бросьте для случайного фрагмента галактического предания — слуха, легенды или таинственного имени, способного вдохновить на приключение.",
    "Киньте для випадкового фрагменту галактичного переказу — чутки, легенди або загадкового імені, що може надихнути на пригоду.",
)


# ── Content list ───────────────────────────────────────────────────────────────
P28_CONTENTS = [
    {
        "id": 199, "icon": "🪐", "source_page": 58,
        "name": ("Planets", "Планеты", "Планети"),
        "desc": _PLANETS_DESC,
        "dice": dice_json("d10", _PLANETS_ENTRIES),
        "dice_ru": _PLANETS_RU, "dice_ua": _PLANETS_UA,
    },
    {
        "id": 200, "icon": "🏔️", "source_page": 58,
        "name": ("Settlement Locale", "Местоположение поселения", "Розташування поселення"),
        "desc": _LOCALE_DESC,
        "dice": dice_json("d100", _LOCALE_ENTRIES),
        "dice_ru": _LOCALE_RU, "dice_ua": _LOCALE_UA,
    },
    {
        "id": 201, "icon": "🏛️", "source_page": 58,
        "name": ("Control Faction", "Управляющая фракция", "Керуюча фракція"),
        "desc": _CONTROL_DESC,
        "dice": dice_json("d10", _CONTROL_ENTRIES),
        "dice_ru": _CONTROL_RU, "dice_ua": _CONTROL_UA,
    },
    {
        "id": 202, "icon": "👥", "source_page": 58,
        "name": ("Population", "Население", "Населення"),
        "desc": _POPULATION_DESC,
        "dice": dice_json("d10", _POPULATION_ENTRIES),
        "dice_ru": _POPULATION_RU, "dice_ua": _POPULATION_UA,
    },
    {
        "id": 203, "icon": "🤝", "source_page": 58,
        "name": ("Factions Table", "Таблица фракций", "Таблиця фракцій"),
        "desc": _FACTIONS_TABLE_DESC,
        "dice": dice_json("d100", _FACTIONS_ENTRIES),
        "dice_ru": None, "dice_ua": None,  # Proper nouns — EN only
    },
    {
        "id": 204, "icon": "⚓", "source_page": 58,
        "name": ("Port Class", "Класс порта", "Клас порту"),
        "desc": _PORT_DESC,
        "dice": dice_json("d10", _PORT_ENTRIES),
        "dice_ru": _PORT_RU, "dice_ua": _PORT_UA,
    },
    {
        "id": 205, "icon": "🏚️", "source_page": 59,
        "name": ("Settlements", "Поселения", "Поселення"),
        "desc": _SETTLEMENT_DESC,
        "dice": dice_json("d100", _SETTLEMENT_ENTRIES),
        "dice_ru": _SETTLEMENT_RU, "dice_ua": _SETTLEMENT_UA,
    },
    {
        "id": 206, "icon": "📜", "source_page": 56,
        "name": ("Random Lore", "Случайный лор", "Випадковий лор"),
        "desc": _LORE_DESC,
        "dice": dice_json("d100", _LORE_ENTRIES),
        "dice_ru": None, "dice_ua": None,  # Proper nouns — EN only
    },
]


# Planet contents go to P29; settlement contents go to P30; C206 stays on P28.
_CONTENT_PAGE = {
    199: 29,  # Planet Surface → P29
    200: 30,  # Settlement Locale → P30
    201: 30,  # Control Faction → P30
    202: 30,  # Population → P30
    203: 30,  # Factions Table → P30
    204: 30,  # Port Class → P30
    205: 30,  # Settlement Type → P30
    206: 28,  # Random Lore → P28
}


def _seed(conn: sqlite3.Connection) -> None:
    # ── Create P29 Planet ─────────────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (29, '🪐', 'wom', 58, '[]')
    """)
    for lang, name in (("en", "Planet"), ("ru", "Планета"), ("ua", "Планета")):
        conn.execute(
            "INSERT OR IGNORE INTO page_i18n (page_id, lang, name) VALUES (29, ?, ?)",
            (lang, name),
        )

    # ── Create P30 Settlement ─────────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (30, '🏘️', 'wom', 58, '[]')
    """)
    for lang, name in (("en", "Settlement"), ("ru", "Поселение"), ("ua", "Поселення")):
        conn.execute(
            "INSERT OR IGNORE INTO page_i18n (page_id, lang, name) VALUES (30, ?, ?)",
            (lang, name),
        )

    # ── Update P28 linked_pages → [29, 30] ────────────────────────────────────
    row = conn.execute("SELECT linked_pages FROM pages WHERE id = 28").fetchone()
    current = json.loads(row[0]) if row and row[0] else []
    new_linked = current[:]
    for pid in (29, 30):
        if pid not in new_linked:
            new_linked.append(pid)
    conn.execute("UPDATE pages SET linked_pages = ? WHERE id = 28", (json.dumps(new_linked),))

    # ── Seed contents ─────────────────────────────────────────────────────────
    for c in P28_CONTENTS:
        cid = c["id"]
        conn.execute("""
            INSERT OR IGNORE INTO contents
                (id, icon, source_slug, source_page, dice, sort_order)
            VALUES (?, ?, 'wom', ?, ?, ?)
        """, (cid, c["icon"], c["source_page"], c.get("dice"), cid))

        for lang in ("en", "ru", "ua"):
            idx = {"en": 0, "ru": 1, "ua": 2}[lang]
            name = c["name"][idx]
            desc = c["desc"][idx]

            dice_entries = None
            if lang == "ru" and c.get("dice_ru"):
                dice_entries = json.dumps(c["dice_ru"], ensure_ascii=False)
            elif lang == "ua" and c.get("dice_ua"):
                dice_entries = json.dumps(c["dice_ua"], ensure_ascii=False)

            conn.execute("""
                INSERT OR IGNORE INTO content_i18n
                    (content_id, lang, name, desc, dice_entries)
                VALUES (?, ?, ?, ?, ?)
            """, (cid, lang, name, desc, dice_entries))

        target_page = _CONTENT_PAGE[cid]
        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (?, ?, ?)
        """, (target_page, cid, cid))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — P29 (Planet), P30 (Settlement) created; {len(P28_CONTENTS)} contents seeded into '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
