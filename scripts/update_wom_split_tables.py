"""
scripts/update_wom_split_tables.py
Split C199 Planets into 4 tables (Surface, Size/Gravity, Atmosphere, Climate)
and C205 Settlements into 3 tables (Type, Conditions, Weird).
New IDs: C207-C211. Planet contents → P29, Settlement contents → P30, C206 → P28.
Run: python scripts/update_wom_split_tables.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


def dj(die, entries):
    return json.dumps({"die": die, "entries": entries}, ensure_ascii=False)


# ── PLANET TABLES ─────────────────────────────────────────────────────────────

# C199 Planet Surface (d10)
_SURFACE_ENTRIES = [
    {"min": 0, "max": 2, "text": "Liquid"},
    {"min": 3, "max": 7, "text": "Terrestrial"},
    {"min": 8, "max": 9, "text": "Gas"},
]
_SURFACE_RU = ["Жидкая", "Твёрдая", "Газовая"]
_SURFACE_UA = ["Рідка", "Тверда", "Газова"]
_SURFACE_DESC = (
    "Roll separately for each planet column: Surface / Size & Gravity / Atmosphere / Climate.",
    "Бросайте отдельно для каждого столбца: Поверхность / Размер и гравитация / Атмосфера / Климат.",
    "Кидайте окремо для кожного стовпця: Поверхня / Розмір і гравітація / Атмосфера / Клімат.",
)

# C207 Planet Size & Gravity (d10)
_SIZE_ENTRIES = [
    {"min": 0, "max": 1, "text": "Giant (Crushing Gravity)"},
    {"min": 2, "max": 4, "text": "Mini-Giant (Heavy Gravity)"},
    {"min": 5, "max": 6, "text": "Earth-Sized Planet (Normal Gravity)"},
    {"min": 7, "max": 9, "text": "Dwarf Planet (Light Gravity)"},
]
_SIZE_RU = [
    "Гигант (Дробящая гравитация)",
    "Мини-гигант (Тяжёлая гравитация)",
    "Земного размера (Нормальная гравитация)",
    "Карликовая (Лёгкая гравитация)",
]
_SIZE_UA = [
    "Гігант (Роздроблювальна гравітація)",
    "Міні-гігант (Важка гравітація)",
    "Земного розміру (Нормальна гравітація)",
    "Карликова (Легка гравітація)",
]

# C208 Planet Atmosphere (d10)
_ATMO_ENTRIES = [
    {"min": 0, "max": 1, "text": "Corrosive"},
    {"min": 2, "max": 3, "text": "Toxic"},
    {"min": 4, "max": 5, "text": "Thin"},
    {"min": 6, "max": 8, "text": "Terraformed"},
    {"min": 9, "max": 9, "text": "Pristine"},
]
_ATMO_RU = ["Едкая", "Токсичная", "Разреженная", "Терраформированная", "Первозданная"]
_ATMO_UA = ["Їдка", "Токсична", "Розріджена", "Терраформована", "Первозданна"]

# C209 Planet Climate (d10)
_CLIMATE_ENTRIES = [
    {"min": 0, "max": 0, "text": "Hellish"},
    {"min": 1, "max": 2, "text": "Hot"},
    {"min": 3, "max": 3, "text": "Balmy"},
    {"min": 4, "max": 4, "text": "Temperate"},
    {"min": 5, "max": 5, "text": "Heavenly"},
    {"min": 6, "max": 6, "text": "Rainy"},
    {"min": 7, "max": 7, "text": "Turbulent"},
    {"min": 8, "max": 8, "text": "Cold"},
    {"min": 9, "max": 9, "text": "Freezing"},
]
_CLIMATE_RU = ["Адский", "Горячий", "Тёплый", "Умеренный", "Небесный", "Дождливый", "Бурный", "Холодный", "Морозный"]
_CLIMATE_UA = ["Пекельний", "Гарячий", "Теплий", "Помірний", "Небесний", "Дощовий", "Бурхливий", "Холодний", "Морозний"]

# ── SETTLEMENT TABLES ─────────────────────────────────────────────────────────

_SETT_RANGES = [
    (0,   0),  (1,  9), (10, 19), (20, 26), (27, 32), (33, 35),
    (36, 38), (39, 41), (42, 44), (45, 47), (48, 50), (51, 53),
    (54, 56), (57, 59), (60, 62), (63, 65), (66, 68), (69, 71),
    (72, 74), (75, 77), (78, 80), (81, 83), (84, 86), (87, 89),
    (90, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96),
    (97, 97), (98, 98), (99, 99),
]

_SETT_TYPES_EN = [
    "Forced Relocation Slum", "Terraformer Colony", "Mining Colony",
    "Colonial Settlement", "Marine Garrison", "Research Facility",
    "Corporate Operations Center", "Manufacturing Complex", "Deep Sea Research Base",
    "Heavy Industry Complex", "Shipping & Logistics Center", "Ore Refinery",
    "Forward Military Base", "Rural Backworld Installation", "Corporate Resupply Depot",
    "Monitoring Outpost", "Off-World Training Installation", "Polar Research Station",
    "Restricted Testing Facility", "Maximum Security Prison Complex", "Stakeholder Camp",
    "Farming Colony", "Prison, formerly a… (roll again)", "Autonomous Factory Zone",
    "Independent Frontier Settlement", "Covert Pirate Base", "Classified Corporate Installation",
    "Desolate Scrapworld", "Major Colonial Settlement", "Religious Compound",
    "Anti-corporate Rebel Base", "Undisclosed Black Site", "Private C-Suite Game Preserve",
]
_SETT_TYPES_RU = [
    "Трущобы принудительного переселения", "Колония терраформеров", "Горная колония",
    "Колониальное поселение", "Морской гарнизон", "Исследовательский центр",
    "Корпоративный операционный центр", "Производственный комплекс", "Глубоководная исследовательская база",
    "Комплекс тяжёлой промышленности", "Центр логистики и перевозок", "Рудный завод",
    "Передовая военная база", "Захолустная установка", "Корпоративный склад снабжения",
    "Наблюдательный пост", "Внеземная учебная установка", "Полярная исследовательская станция",
    "Закрытый испытательный полигон", "Комплекс тюрьмы строгого режима", "Лагерь акционеров",
    "Фермерская колония", "Бывшая тюрьма, ранее… (бросьте ещё раз)", "Зона автономного завода",
    "Независимое фронтирное поселение", "Тайная пиратская база", "Засекреченная корпоративная установка",
    "Безлюдный свалочный мир", "Крупное колониальное поселение", "Религиозная резиденция",
    "База антикорпоративных повстанцев", "Нераскрытый чёрный объект", "Частный игровой заповедник C-Suite",
]
_SETT_TYPES_UA = [
    "Нетрі примусового переселення", "Колонія терраформерів", "Гірська колонія",
    "Колоніальне поселення", "Морський гарнізон", "Дослідницький центр",
    "Корпоративний операційний центр", "Виробничий комплекс", "Глибоководна дослідницька база",
    "Комплекс важкої промисловості", "Центр логістики та перевезень", "Рудний завод",
    "Передова військова база", "Захолустна установка", "Корпоративний склад постачання",
    "Спостережний пост", "Позаземна навчальна установка", "Полярна дослідницька станція",
    "Закритий випробувальний полігон", "Комплекс тюрми суворого режиму", "Табір акціонерів",
    "Фермерська колонія", "Колишня тюрма, раніше… (киньте ще раз)", "Зона автономного заводу",
    "Незалежне фронтирне поселення", "Таємна піратська база", "Засекречена корпоративна установка",
    "Безлюдний смітниковий світ", "Велике колоніальне поселення", "Релігійна садиба",
    "База антикорпоративних повстанців", "Нерозкритий чорний об'єкт", "Приватний ігровий заповідник C-Suite",
]

_SETT_CONDITIONS_EN = [
    "Under quarantine.", "Overworked, tired. Low morale.", "Business as usual.",
    "Workers on strike.", "Hazardous working conditions.", "Security forces in control.",
    "Gross managerial misconduct.", "Frequent storms.", "Productivity low.",
    "Corporate strikebreakers called in.", "Hostile wildlife.", "Military blockade.",
    "Lush overgrown wilderness.", "In desperate need of aid.", "Weather frighteningly unstable.",
    "Food shortage.", "Colonists talking of joining a Union.", "Awaiting orders from corporate.",
    "Local Union elections.", "Contract negotiation breakdown.", "Low on supplies.",
    "Massive crop failure.", "Communications cut off.", "Company holiday celebrations.",
    "Under constant threat of terrorist attacks.", "Local government crumbling.", "Rumours of layoffs.",
    "Overpopulation issue.", "Settlement being shut down by corporate.", "Petty bickering escalating out of control.",
    "Population entirely synthetic.", "Co-opted by military as temporary base.", "Mutiny brewing.",
]
_SETT_CONDITIONS_RU = [
    "На карантине.", "Перегружены, устали, низкий моральный дух.", "Всё как обычно.",
    "Рабочие бастуют.", "Опасные условия труда.", "Контроль у сил безопасности.",
    "Грубое управленческое нарушение.", "Частые бури.", "Низкая производительность.",
    "Вызваны корпоративные штрейкбрехеры.", "Враждебная дикая природа.", "Военная блокада.",
    "Буйные джунгли.", "В отчаянной нужде в помощи.", "Пугающе нестабильная погода.",
    "Нехватка еды.", "Колонисты говорят о вступлении в профсоюз.", "Ждут приказов от корпоратов.",
    "Местные выборы в профсоюз.", "Срыв переговоров по контракту.", "Мало запасов.",
    "Массовый неурожай.", "Связь отрезана.", "Корпоративные праздничные торжества.",
    "Под постоянной угрозой террористических атак.", "Местное правительство рушится.", "Слухи о сокращениях.",
    "Проблема перенаселения.", "Поселение закрывается корпоратами.", "Мелкие склоки выходят из-под контроля.",
    "Население полностью синтетическое.", "Занят военными как временная база.", "Назревает мятеж.",
]
_SETT_CONDITIONS_UA = [
    "На карантині.", "Перевантажені, втомлені, низький моральний дух.", "Все як завжди.",
    "Робітники страйкують.", "Небезпечні умови праці.", "Контроль у сил безпеки.",
    "Грубе управлінське порушення.", "Часті бурі.", "Низька продуктивність.",
    "Викликані корпоративні страйкбрехери.", "Ворожа дика природа.", "Військова блокада.",
    "Буйні джунглі.", "У відчайдушній потребі допомоги.", "Лячно нестабільна погода.",
    "Нестача їжі.", "Колоністи говорять про вступ у профспілку.", "Чекають наказів від корпорацій.",
    "Місцеві вибори у профспілку.", "Зрив переговорів за контрактом.", "Мало запасів.",
    "Масовий неврожай.", "Зв'язок відрізаний.", "Корпоративні святкові урочистості.",
    "Під постійною загрозою терористичних атак.", "Місцевий уряд руйнується.", "Чутки про скорочення.",
    "Проблема перенаселення.", "Поселення закривається корпораціями.", "Дрібні сварки виходять з-під контролю.",
    "Населення повністю синтетичне.", "Зайнятий військовими як тимчасова база.", "Назріває бунт.",
]

_SETT_WEIRD_EN = [
    "Failed utopia.", "Unsolved string of gruesome murders.", "Home to powerful criminal syndicate.",
    "Local customs are strange, wary of outsiders.", "Deserted.", "Secretly a corporate re-education camp.",
    "Settlement has newfound religious significance.", "Company secretly dosing the water.", "Live hostage situation.",
    "Local environment is a radioactive wasteland.", "Rapidly growing doomsday cult.", "Controlled by separatist militia.",
    "Collapse of local social order.", "Refugee crisis.", "Extinction event.",
    "Settlement has descended into anarchy.", "Colonists report being replaced by imposters.", "Secret military operation recently arrived.",
    "Deadly viral outbreak.", "Environmental collapse imminent.", "Recent breakthrough discovery.",
    "Settlement houses decadent corporate nobility.", "Colonists slowly disappearing.", "Strange black monolith unearthed.",
    "Rumours of meddling from powerful AI.", "Colonists believe settlement haunted.", "Android uprising imminent.",
    "Gigantic unidentifiable fossilised remains.", "Reports of interference by 'Celestials.'", "Wreckage of spacecraft of unknown origin.",
    "Ruins of precursor star-faring civilisation found.", "Ancient gateway recently uncovered.", "First Contact event.",
]
_SETT_WEIRD_RU = [
    "Провалившаяся утопия.", "Нераскрытая серия жестоких убийств.", "Здесь орудует мощный криминальный синдикат.",
    "Местные обычаи странные, чужаков опасаются.", "Покинут.", "Втайне является корпоративным лагерем перевоспитания.",
    "Поселение обрело новое религиозное значение.", "Компания тайно добавляет что-то в воду.", "Активная ситуация с заложниками.",
    "Местная среда — радиоактивная пустошь.", "Стремительно растущий апокалиптический культ.", "Под контролем сепаратистской милиции.",
    "Распад местного общественного порядка.", "Кризис беженцев.", "Событие вымирания.",
    "Поселение скатилось в анархию.", "Колонисты сообщают, что их заменяют самозванцами.", "Недавно прибыла тайная военная операция.",
    "Смертельная вирусная вспышка.", "Надвигается экологический коллапс.", "Недавнее прорывное открытие.",
    "В поселении обитает декадентская корпоративная знать.", "Колонисты медленно исчезают.", "Обнаружен странный чёрный монолит.",
    "Слухи о вмешательстве мощного ИИ.", "Колонисты верят, что поселение проклято.", "Восстание андроидов вот-вот произойдёт.",
    "Гигантские неопознанные окаменелые останки.", "Сообщения о вмешательстве «Небожителей».", "Обломки космического корабля неизвестного происхождения.",
    "Обнаружены руины звёздной цивилизации предшественников.", "Недавно обнаружен древний портал.", "Событие Первого Контакта.",
]
_SETT_WEIRD_UA = [
    "Провалена утопія.", "Нерозкрита серія жорстоких вбивств.", "Тут діє потужний злочинний синдикат.",
    "Місцеві звичаї дивні, чужинців остерігаються.", "Покинутий.", "Таємно є корпоративним табором перевиховання.",
    "Поселення набуло нового релігійного значення.", "Компанія таємно додає щось у воду.", "Активна ситуація з заручниками.",
    "Місцеве середовище — радіоактивне пустище.", "Стрімко зростаючий апокаліптичний культ.", "Під контролем сепаратистської міліції.",
    "Розпад місцевого суспільного порядку.", "Криза біженців.", "Подія вимирання.",
    "Поселення скотилося в анархію.", "Колоністи повідомляють, що їх замінюють самозванцями.", "Нещодавно прибула таємна військова операція.",
    "Смертельний вірусний спалах.", "Наближається екологічний колапс.", "Нещодавнє проривне відкриття.",
    "У поселенні живе декадентська корпоративна знать.", "Колоністи повільно зникають.", "Виявлено дивний чорний моноліт.",
    "Чутки про втручання потужного ШІ.", "Колоністи вважають, що поселення проклято.", "Повстання андроїдів ось-ось станеться.",
    "Гігантські невпізнані скам'янілі залишки.", "Повідомлення про втручання «Небожителів».", "Уламки космічного корабля невідомого походження.",
    "Виявлено руїни зіркової цивілізації попередників.", "Нещодавно виявлено стародавні ворота.", "Подія Першого Контакту.",
]

def _make_entries(ranges, texts):
    return [{"min": lo, "max": hi, "text": txt} for (lo, hi), txt in zip(ranges, texts)]


# ── Final sort orders per page ────────────────────────────────────────────────
# (page_id, content_id, sort_order)
PAGE_CONTENT_ORDER = [
    (29, 199, 1),   # P29 Planet — Planet Surface
    (29, 207, 2),   # P29 Planet — Planet Size & Gravity
    (29, 208, 3),   # P29 Planet — Planet Atmosphere
    (29, 209, 4),   # P29 Planet — Planet Climate
    (30, 200, 1),   # P30 Settlement — Settlement Locale
    (30, 201, 2),   # P30 Settlement — Control Faction
    (30, 202, 3),   # P30 Settlement — Population
    (30, 203, 4),   # P30 Settlement — Factions Table
    (30, 204, 5),   # P30 Settlement — Port Class
    (30, 205, 6),   # P30 Settlement — Settlement Type
    (30, 210, 7),   # P30 Settlement — Settlement Conditions
    (30, 211, 8),   # P30 Settlement — Settlement Weird
    (28, 206, 13),  # P28 Random Generators — Random Lore
]


def _seed(conn: sqlite3.Connection) -> None:
    # ── Update C199 to Planet Surface ────────────────────────────────────────
    conn.execute(
        "UPDATE contents SET dice=? WHERE id=199",
        (dj("d10", _SURFACE_ENTRIES),),
    )
    for lang, de in [("en", None), ("ru", json.dumps(_SURFACE_RU, ensure_ascii=False)), ("ua", json.dumps(_SURFACE_UA, ensure_ascii=False))]:
        names = {"en": "Planet Surface", "ru": "Поверхность планеты", "ua": "Поверхня планети"}
        conn.execute(
            "UPDATE content_i18n SET name=?, desc=?, dice_entries=? WHERE content_id=199 AND lang=?",
            (names[lang], _SURFACE_DESC[{"en":0,"ru":1,"ua":2}[lang]], de, lang),
        )

    # ── Update C205 to Settlement Type ───────────────────────────────────────
    type_entries = _make_entries(_SETT_RANGES, _SETT_TYPES_EN)
    conn.execute(
        "UPDATE contents SET dice=? WHERE id=205",
        (dj("d100", type_entries),),
    )
    for lang, texts_list in [("en", None), ("ru", _SETT_TYPES_RU), ("ua", _SETT_TYPES_UA)]:
        names = {"en": "Settlement Type", "ru": "Тип поселения", "ua": "Тип поселення"}
        desc = (
            "Roll for the settlement's type, then separately for Conditions and Weird.",
            "Бросьте для типа поселения, затем отдельно для Условий и Странностей.",
            "Киньте для типу поселення, потім окремо для Умов і Дивацтв.",
        )
        de = json.dumps(texts_list, ensure_ascii=False) if texts_list else None
        conn.execute(
            "UPDATE content_i18n SET name=?, desc=?, dice_entries=? WHERE content_id=205 AND lang=?",
            (names[lang], desc[{"en":0,"ru":1,"ua":2}[lang]], de, lang),
        )

    # ── Insert C207 Planet Size & Gravity ─────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (207, ?, 'wom', 58, ?, 207)
    """, ("🌍", dj("d10", _SIZE_ENTRIES)))
    for lang, texts, name in [
        ("en", None,     "Planet Size & Gravity"),
        ("ru", _SIZE_RU, "Размер и гравитация планеты"),
        ("ua", _SIZE_UA, "Розмір і гравітація планети"),
    ]:
        de = json.dumps(texts, ensure_ascii=False) if texts else None
        desc = (
            "Roll separately for each planet column: Surface / Size & Gravity / Atmosphere / Climate.",
            "Бросайте отдельно для каждого столбца: Поверхность / Размер и гравитация / Атмосфера / Климат.",
            "Кидайте окремо для кожного стовпця: Поверхня / Розмір і гравітація / Атмосфера / Клімат.",
        )[{"en":0,"ru":1,"ua":2}[lang]]
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (207, ?, ?, ?, ?)
        """, (lang, name, desc, de))

    # ── Insert C208 Planet Atmosphere ─────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (208, ?, 'wom', 58, ?, 208)
    """, ("💨", dj("d10", _ATMO_ENTRIES)))
    for lang, texts, name in [
        ("en", None,      "Planet Atmosphere"),
        ("ru", _ATMO_RU,  "Атмосфера планеты"),
        ("ua", _ATMO_UA,  "Атмосфера планети"),
    ]:
        de = json.dumps(texts, ensure_ascii=False) if texts else None
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (208, ?, ?, ?, ?)
        """, (lang, name, _SURFACE_DESC[{"en":0,"ru":1,"ua":2}[lang]], de))

    # ── Insert C209 Planet Climate ────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (209, ?, 'wom', 58, ?, 209)
    """, ("🌡️", dj("d10", _CLIMATE_ENTRIES)))
    for lang, texts, name in [
        ("en", None,          "Planet Climate"),
        ("ru", _CLIMATE_RU,   "Климат планеты"),
        ("ua", _CLIMATE_UA,   "Клімат планети"),
    ]:
        de = json.dumps(texts, ensure_ascii=False) if texts else None
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (209, ?, ?, ?, ?)
        """, (lang, name, _SURFACE_DESC[{"en":0,"ru":1,"ua":2}[lang]], de))

    # ── Insert C210 Settlement Conditions ─────────────────────────────────────
    cond_entries = _make_entries(_SETT_RANGES, _SETT_CONDITIONS_EN)
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (210, ?, 'wom', 59, ?, 210)
    """, ("⚠️", dj("d100", cond_entries)))
    for lang, texts, name in [
        ("en", None,                "Settlement Conditions"),
        ("ru", _SETT_CONDITIONS_RU, "Условия в поселении"),
        ("ua", _SETT_CONDITIONS_UA, "Умови в поселенні"),
    ]:
        de = json.dumps(texts, ensure_ascii=False) if texts else None
        desc = (
            "Roll for current conditions in this settlement.",
            "Бросьте для текущих условий в поселении.",
            "Киньте для поточних умов у поселенні.",
        )[{"en":0,"ru":1,"ua":2}[lang]]
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (210, ?, ?, ?, ?)
        """, (lang, name, desc, de))

    # ── Insert C211 Settlement Weird ──────────────────────────────────────────
    weird_entries = _make_entries(_SETT_RANGES, _SETT_WEIRD_EN)
    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (211, ?, 'wom', 59, ?, 211)
    """, ("👁️", dj("d100", weird_entries)))
    for lang, texts, name in [
        ("en", None,              "Settlement Weird"),
        ("ru", _SETT_WEIRD_RU,   "Странности поселения"),
        ("ua", _SETT_WEIRD_UA,   "Дивацтва поселення"),
    ]:
        de = json.dumps(texts, ensure_ascii=False) if texts else None
        desc = (
            "Roll for a weird element unique to this settlement.",
            "Бросьте для странного элемента, присущего этому поселению.",
            "Киньте для дивного елементу, притаманного цьому поселенню.",
        )[{"en":0,"ru":1,"ua":2}[lang]]
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (211, ?, ?, ?, ?)
        """, (lang, name, desc, de))

    # ── Set page_contents for P29 (Planet), P30 (Settlement), P28 (Random Lore)
    for pid, cid, sord in PAGE_CONTENT_ORDER:
        conn.execute("""
            INSERT INTO page_contents (page_id, content_id, sort_order)
            VALUES (?, ?, ?)
            ON CONFLICT(page_id, content_id) DO UPDATE SET sort_order = excluded.sort_order
        """, (pid, cid, sord))

    # ── Add content_links for split tables ────────────────────────────────────
    new_links = [
        # Planet sub-tables cross-reference each other
        (199, 207, "see_also"),
        (199, 208, "see_also"),
        (199, 209, "see_also"),
        # Settlement sub-tables cross-reference each other
        (205, 210, "see_also"),
        (205, 211, "see_also"),
    ]
    for from_id, to_id, label in new_links:
        conn.execute("""
            INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key)
            VALUES (?, ?, ?)
        """, (from_id, to_id, label))

    # Remove the old combined C178→C199 "see_also" (178→199 was see_also, keep it)
    # The C205→C199 "related" link was between old settlement and old planet — keep it


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — C199/C205 split into 4+3 tables. C207-C211 added.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
