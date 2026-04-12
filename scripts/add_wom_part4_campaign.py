"""
scripts/add_wom_part4_campaign.py
Warden's Operations Manual — Part 4: P27 Campaign Building contents C191-C198.
Run: python scripts/add_wom_part4_campaign.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── helpers ──────────────────────────────────────────────────────────────────
def dice_json(die: str, entries: list[dict]) -> str:
    return json.dumps({"die": die, "entries": entries}, ensure_ascii=False)


# ── C191 Campaign Style ───────────────────────────────────────────────────────
_STYLE = (
    # EN
    "How your campaign is structured and the style of play your players can expect.\n\n"
    "ANTHOLOGY — Sessions have little (if any) narrative cohesion. Each adventure stands alone.\n"
    "APOCALYPSE — Play centres around a massive threat to all life (alien invasion, interstellar war, plague, AI revolt, etc.).\n"
    "ENSEMBLE — Players routinely control multiple characters and switch between them as play dictates.\n"
    "EPISODIC — Sessions emphasise downtime and roleplaying, with frequent time skips and slice-of-life encounters.\n"
    "HEROIC — Players are key figures in a large-scale epic struggle with stakes that affect millions.\n"
    "NARRATIVE — Players unravel a cohesive narrative as part of the background or foreground of play.\n"
    "OPEN TABLE — A large pool of potential players may drop in or out on a session-by-session basis.\n"
    "SANDBOX — Players are given a large area with several leads on potential work in any order they wish.\n"
    "SERIAL — Play takes place from moment to moment, day to day, with infrequent time skips.",
    # RU
    "Как структурирована ваша кампания и какого стиля игры ждать игрокам.\n\n"
    "АНТОЛОГИЯ — Сессии почти не связаны нарративно. Каждое приключение самостоятельно.\n"
    "АПОКАЛИПСИС — Игра вращается вокруг массовой угрозы жизни (вторжение, межзвёздная война, чума, бунт ИИ и т.д.).\n"
    "АНСАМБЛЬ — Игроки регулярно управляют несколькими персонажами, переключаясь между ними.\n"
    "ЭПИЗОДИЧЕСКАЯ — Упор на отдых и отыгрыш, частые прыжки во времени и бытовые сцены.\n"
    "ГЕРОИЧЕСКАЯ — Игроки — ключевые фигуры масштабной эпической борьбы с судьбами миллионов.\n"
    "НАРРАТИВНАЯ — Игроки распутывают связный нарратив на переднем или заднем плане игры.\n"
    "ОТКРЫТЫЙ СТОЛ — Большой пул игроков может входить и выходить сессия за сессией.\n"
    "ПЕСОЧНИЦА — Игрокам дан большой регион с множеством зацепок для работы в любом порядке.\n"
    "СЕРИАЛЬНАЯ — Игра идёт момент за моментом, день за днём, с редкими прыжками во времени.",
    # UA
    "Як структурована ваша кампанія і якого стилю гри очікувати гравцям.\n\n"
    "АНТОЛОГІЯ — Сесії майже не пов'язані наративно. Кожна пригода самостійна.\n"
    "АПОКАЛІПСИС — Гра обертається навколо масової загрози всьому живому (вторгнення, міжзоряна війна, чума, бунт ШІ тощо).\n"
    "АНСАМБЛЬ — Гравці регулярно керують кількома персонажами, перемикаючись між ними.\n"
    "ЕПІЗОДИЧНА — Упор на відпочинок і відіграш, часті стрибки у часі та побутові сцени.\n"
    "ГЕРОЇЧНА — Гравці — ключові фігури масштабної епічної боротьби з долями мільйонів.\n"
    "НАРАТИВНА — Гравці розплутують зв'язний наратив на передньому або задньому плані гри.\n"
    "ВІДКРИТИЙ СТІЛ — Великий пул гравців може входити й виходити сесія за сесією.\n"
    "ПІСОЧНИЦЯ — Гравцям дано великий регіон з безліччю зачіпок для роботи у будь-якому порядку.\n"
    "СЕРІАЛЬНА — Гра йде момент за моментом, день за днем, з рідкими стрибками у часі.",
)

# ── C192 Campaign Frames ──────────────────────────────────────────────────────
_FRAMES = (
    # EN
    "Your campaign's frame tells players who they are, what kind of work they do, and what kinds of things they might encounter.\n\n"
    "00 — SPACE TRUCKERS: Blockade running, smuggling contraband, or working as a certified owner-operator. Watch out for stowaways and customs patrols.\n"
    "01 — PRIVATE MERCENARIES: Jump and drop. Sweep and clear. Seek and destroy. You go where the Company sends you.\n"
    "02 — EXPLORERS: You wanted to go where no one had gone before. Turns out there's a reason why.\n"
    "03 — DOGS OF WAR: Humanity was in trouble and you answered the call. You've looked into the yawning maw of destruction.\n"
    "04 — CORPORATE INSPECTORS: Production has shut down, vessels have gone missing, strikes are brewing. The C-Levels have questions and it's your job to get answers.\n"
    "05 — OFFWORLD COLONISTS: Planting terraformers in inhospitable environments, researching planetary phenomena, defending against local flora and fauna.\n"
    "06 — CRASHLANDERS: You scraped together money for a ticket to a new life off-world. Now the sirens are blaring and you're waking up from cryosleep amongst chaos.\n"
    "07 — HYPERSPACE RAIDERS: Stealing from the rich and giving to whomever you please. Make sure you Jump before the Marshalls close in.\n"
    "08 — MINING & SALVAGE: Asteroid mining, skimming gas giants, or salvaging derelicts. Steady pay and no suit and tie required.\n"
    "09 — BOUNTY HUNTERS: There is no law on the Rim, just Corporate Policy. Check the bounty boards, bring in your charge, stay alive.",
    # RU
    "Рамка кампании говорит игрокам, кто они, какую работу выполняют и что их ожидает.\n\n"
    "00 — КОСМИЧЕСКИЕ ДАЛЬНОБОЙЩИКИ: Прорыв блокады, контрабанда или работа сертифицированного перевозчика-собственника.\n"
    "01 — ЧАСТНЫЕ НАЁМНИКИ: Прыжок и высадка. Зачистка. Ликвидация. Вы идёте туда, куда посылает Компания.\n"
    "02 — ИССЛЕДОВАТЕЛИ: Вы хотели пойти туда, куда не ступала нога человека. Оказывается, на это есть причина.\n"
    "03 — ПСЫ ВОЙНЫ: Человечество было в беде, и вы откликнулись на призыв. Вы заглянули в разверзшуюся пасть уничтожения.\n"
    "04 — КОРПОРАТИВНЫЕ ИНСПЕКТОРЫ: Производство остановлено, суда пропали, забастовки назревают. У топ-менеджеров вопросы — вы обязаны дать ответы.\n"
    "05 — КОЛОНИСТЫ ВНЕ МИРА: Установка терраформеров в негостеприимной среде, изучение планетарных явлений, защита от местной флоры и фауны.\n"
    "06 — ПОТЕРПЕВШИЕ КРУШЕНИЕ: Вы скопили деньги на билет к новой жизни за пределами Земли. Но сирены уже воют, а вы просыпаетесь из криосна в хаосе.\n"
    "07 — РЕЙДЕРЫ ГИПЕРПРОСТРАНСТВА: Воровство у богатых и раздача кому придётся. Успейте прыгнуть до того, как Маршалы настигнут вас.\n"
    "08 — ДОБЫЧА И УТИЛИЗАЦИЯ: Добыча астероидов, скимминг газовых гигантов или подъём деrelict-кораблей. Стабильная зарплата — галстук не нужен.\n"
    "09 — ОХОТНИКИ ЗА ГОЛОВАМИ: На Окраине нет закона, только корпоративная политика. Проверьте доски объявлений и живите.",
    # UA
    "Рамка кампанії говорить гравцям, хто вони, яку роботу виконують і що на них чекає.\n\n"
    "00 — КОСМІЧНІ ДАЛЕКОБІЙНИКИ: Прорив блокади, контрабанда або робота сертифікованого перевізника-власника.\n"
    "01 — ПРИВАТНІ НАЙМАНЦІ: Стрибок і висадка. Зачистка. Ліквідація. Ви йдете туди, куди посилає Компанія.\n"
    "02 — ДОСЛІДНИКИ: Ви хотіли піти туди, куди ще не ступала нога людини. Виявляється, на це є причина.\n"
    "03 — ПСИ ВІЙНИ: Людство було в біді, і ви відгукнулися на заклик. Ви зазирнули у разверзлу пащу знищення.\n"
    "04 — КОРПОРАТИВНІ ІНСПЕКТОРИ: Виробництво зупинено, судна зникли, страйки назрівають. У топ-менеджерів питання — ви зобов'язані дати відповіді.\n"
    "05 — КОЛОНІСТИ ЗА МЕЖЕЮ СВІТУ: Встановлення терраформерів у негостинному середовищі, вивчення планетарних явищ, захист від місцевої флори й фауни.\n"
    "06 — ПОТЕРПІЛІ АВАРІЮ: Ви назбирали грошей на квиток до нового життя поза Землею. Але сирени вже виють, а ви прокидаєтесь із кріосну в хаосі.\n"
    "07 — РЕЙДЕРИ ГІПЕРПРОСТОРУ: Крадіжка у багатих і роздача кому завгодно. Встигніть стрибнути до того, як Маршали наздоженуть вас.\n"
    "08 — ВИДОБУТОК І УТИЛІЗАЦІЯ: Добуток астероїдів, скімінг газових гігантів або підйом derelict-кораблів. Стабільна зарплата — краватка не потрібна.\n"
    "09 — МИСЛИВЦІ ЗА ГОЛОВАМИ: На Окраїні немає закону, лише корпоративна політика. Перевірте дошки оголошень і живіть.",
)

# ── C193 The Company ──────────────────────────────────────────────────────────
_COMPANY = (
    # EN
    "Design the Company as your campaign's interstellar megacorporation. It can serve as:\n\n"
    "• PRIMARY EMPLOYER or CLIENT: The players have to work for someone, and the Company has resources to operate far from the Core. Stable pay — but you're first in line to be discarded when things go sideways.\n"
    "• PRINCIPAL ANTAGONIST or RIVAL: A persistent threat, faceless and inexhaustible. Its resources are so infinite it could take one or more campaigns to uncover all of its schemes.\n"
    "• FRAMING DEVICE or SETTING: Your Company tells you what kind of work players will be doing and what technologies will define the setting.\n\n"
    "CORPORATE POWER: Assume unlimited resources. Assume it's above the law. Assume permanent blackmail records on every crew member. Assume anything the crew owns is actually leased through the Company. Assume illegal research, flagrant violations, price fixing, espionage, extortion, bribery, embezzlement. Assume invasive tracking, disinformation, industrial sabotage, proxy wars, human experimentation, environmental collapse. Assume they've done all this before. Assume they'll never stop.\n\n"
    "CORPORATE MIND MAP: Label a page 'The Company.' Write it in the centre and circle it. Draw connections to important people, subsidiaries, and secret projects. Add to it as play goes on.",
    # RU
    "Создайте Компанию как межзвёздную мегакорпорацию вашей кампании. Она может служить:\n\n"
    "• ОСНОВНЫМ РАБОТОДАТЕЛЕМ или КЛИЕНТОМ: Игрокам нужно на кого-то работать, а у Компании есть ресурсы на Окраине. Стабильная зарплата — но вы первые на вылет, когда всё идёт наперекосяк.\n"
    "• ГЛАВНЫМ АНТАГОНИСТОМ или СОПЕРНИКОМ: Постоянная угроза, безликая и неистощимая. Её ресурсы столь бесконечны, что потребуется несколько кампаний, чтобы раскрыть все схемы.\n"
    "• ОБРАМЛЯЮЩИМ УСТРОЙСТВОМ или НАСТРОЙКОЙ: Ваша Компания показывает, какую работу будут выполнять игроки и какие технологии будут определять сеттинг.\n\n"
    "КОРПОРАТИВНАЯ ВЛАСТЬ: Предположите неограниченные ресурсы. Она выше закона. Постоянные досье с компроматом на каждого члена команды. Всё, чем владеет команда, фактически арендовано у Компании. Незаконные исследования, нарушения, манипуляции ценами, шпионаж, вымогательство, взятки, хищения. Слежка, дезинформация, промышленный саботаж, войны по доверенности, опыты над людьми, экологические катастрофы. Это всё уже было. И будет снова.\n\n"
    "МЕНТАЛЬНАЯ КАРТА КОМПАНИИ: Назовите страницу 'Компания.' Напишите её в центре и обведите. Рисуйте связи с важными людьми, дочерними структурами и секретными проектами.",
    # UA
    "Створіть Компанію як міжзоряну мегакорпорацію вашої кампанії. Вона може служити:\n\n"
    "• ОСНОВНИМ РОБОТОДАВЦЕМ або КЛІЄНТОМ: Гравцям потрібно на когось працювати, а у Компанії є ресурси на Окраїні. Стабільна зарплата — але ви перші на вихід, коли все йде не так.\n"
    "• ГОЛОВНИМ АНТАГОНІСТОМ або СУПЕРНИКОМ: Постійна загроза, безлика й невичерпна. Її ресурси настільки нескінченні, що знадобиться кілька кампаній, щоб розкрити всі схеми.\n"
    "• ОБРАМЛЮЮЧИМ ПРИСТРОЄМ або НАЛАШТУВАННЯМ: Ваша Компанія показує, яку роботу виконуватимуть гравці і які технології визначатимуть сеттинг.\n\n"
    "КОРПОРАТИВНА ВЛАДА: Припустіть необмежені ресурси. Вона вище закону. Постійні досьє з компроматом на кожного члена команди. Все, чим володіє команда, фактично орендоване у Компанії. Незаконні дослідження, порушення, маніпуляції цінами, шпигунство, вимагання, хабарі, розкрадання. Слідкування, дезінформація, промисловий саботаж, проксі-війни, досліди над людьми, екологічні катастрофи. Це все вже було. І буде знову.\n\n"
    "МЕНТАЛЬНА КАРТА КОМПАНІЇ: Назвіть сторінку 'Компанія.' Напишіть її в центрі й обведіть. Малюйте зв'язки з важливими людьми, дочірніми структурами та секретними проектами.",
)

# ── C194 How to Create Factions ───────────────────────────────────────────────
_FACTIONS = (
    # EN
    "Factions are the organisations, corporations, cults, gangs, and other groups your players interact with.\n\n"
    "CREATE A FACTION: Turn to a new page in your Campaign Notebook, title it with the faction's name, and write a short description. Note their:\n"
    "• VIPs: Important members with short descriptions and page references.\n"
    "• Locations: Notable locations with page references.\n"
    "• Goals: Compelling goals that will affect the players.\n\n"
    "USING FACTIONS: Factions become useful once players have encountered two or three, creating situations where they must choose between competing interests. Ally factions offer work, safe ports, and resources. Enemy factions hunt players down and cut them off from supplies.\n\n"
    "FACTION GOALS: Assign each goal a number of boxes (easy = 1–2, long/challenging = 5–10). Roll 1d100 at regular intervals:\n"
    "• Evens: Forward progress — fill in a box.\n"
    "• Odds: Obstacle or roadblock — mark a box with an X.\n"
    "• Even doubles: Breakthrough — fill in two boxes (or clear an X).\n"
    "• Odd doubles: Catastrophic event — erase a filled box.\n"
    "When all boxes are filled, the faction achieves their goal.",
    # RU
    "Фракции — это организации, корпорации, культы, банды и другие группы, с которыми взаимодействуют игроки.\n\n"
    "СОЗДАНИЕ ФРАКЦИИ: Откройте новую страницу в Блокноте Кампании, назовите её именем фракции и напишите краткое описание. Укажите:\n"
    "• ВИП: Важных членов с кратким описанием и ссылками на страницы.\n"
    "• Локации: Примечательные места со ссылками на страницы.\n"
    "• Цели: Значимые цели, которые затронут игроков.\n\n"
    "ИСПОЛЬЗОВАНИЕ ФРАКЦИЙ: Фракции становятся наиболее полезными, когда игроки столкнулись с двумя-тремя, создавая ситуации с конкурирующими интересами. Союзные фракции предлагают работу, безопасные порты и ресурсы. Враждебные — преследуют игроков и отрезают от снаряжения.\n\n"
    "ЦЕЛИ ФРАКЦИЙ: Назначьте каждой цели количество клеточек (лёгкая = 1–2, трудная/долгая = 5–10). Бросайте 1d100 через регулярные промежутки:\n"
    "• Чётные: Прогресс — закрасьте клетку.\n"
    "• Нечётные: Препятствие — отметьте клетку крестом.\n"
    "• Чётные дубли: Прорыв — закройте две клетки (или сотрите крест).\n"
    "• Нечётные дубли: Катастрофа — сотрите закрашенную клетку.\n"
    "Когда все клетки закрашены, фракция достигает цели.",
    # UA
    "Фракції — це організації, корпорації, культи, банди та інші групи, з якими взаємодіють гравці.\n\n"
    "СТВОРЕННЯ ФРАКЦІЇ: Відкрийте нову сторінку в Блокноті Кампанії, назвіть її ім'ям фракції та напишіть короткий опис. Вкажіть:\n"
    "• ВІП: Важливих членів із коротким описом і посиланнями на сторінки.\n"
    "• Локації: Примітні місця з посиланнями на сторінки.\n"
    "• Цілі: Значущі цілі, які зачеплять гравців.\n\n"
    "ВИКОРИСТАННЯ ФРАКЦІЙ: Фракції стають найкориснішими, коли гравці зіткнулися з двома-трьома, створюючи ситуації з конкуруючими інтересами. Союзні фракції пропонують роботу, безпечні порти та ресурси. Ворожі — переслідують гравців і відрізають від спорядження.\n\n"
    "ЦІЛІ ФРАКЦІЙ: Призначте кожній цілі кількість клітинок (легка = 1–2, складна/тривала = 5–10). Кидайте 1d100 через регулярні проміжки:\n"
    "• Парні: Прогрес — зафарбуйте клітинку.\n"
    "• Непарні: Перешкода — позначте клітинку хрестом.\n"
    "• Парні дублі: Прорив — закрийте дві клітинки (або зітріть хрест).\n"
    "• Непарні дублі: Катастрофа — зітріть зафарбовану клітинку.\n"
    "Коли всі клітинки зафарбовані, фракція досягає цілі.",
)

# ── C195 Contract Work (d10 rollable) ─────────────────────────────────────────
_CONTRACT_ENTRIES = [
    {"min": 0, "max": 1, "text": "PRODUCTION & MANUFACTURE — Asteroid mining, derelict salvage and scrap, strikebreaking, terraformer installation, and android troubleshooting."},
    {"min": 2, "max": 3, "text": "SHIPPING & HANDLING — Cargo freight, VIP escort, scrap hauling, prisoner transport, sensitive materials handling, passenger transport, and contraband smuggling."},
    {"min": 4, "max": 5, "text": "RESEARCH & DEVELOPMENT — Sample & specimen collection, planetary survey, field testing, sabotage, containment breach, archaeological dig, and corporate espionage."},
    {"min": 6, "max": 7, "text": "RISK MANAGEMENT — Sweep and clear, liquidation, asset protection, quarantine enforcement, bounty hunting, distress signal response, and system patrol."},
    {"min": 8, "max": 8, "text": "HUMAN RESOURCES — Missing persons, suspicious death, communication breakdown, troubleshooting, AI negotiation, and settlement evacuation."},
    {"min": 9, "max": 9, "text": "MERGERS & ACQUISITIONS — Asset recovery, salvage retention, personnel recruitment, first contact protocol, repossession, and piracy."},
]
_CONTRACT_RU = [
    "ПРОИЗВОДСТВО И ДОБЫЧА — Горная добыча астероидов, утилизация дрейфующих кораблей, срыв забастовок, установка терраформеров, обслуживание андроидов.",
    "ТРАНСПОРТИРОВКА — Доставка грузов, сопровождение ВИП, вывоз лома, перевозка заключённых, обработка чувствительных материалов, транспорт пассажиров, контрабанда.",
    "ИССЛЕДОВАНИЯ И РАЗРАБОТКИ — Сбор образцов, планетарная разведка, полевые испытания, саботаж, ликвидация утечки, археологические раскопки, корпоративный шпионаж.",
    "УПРАВЛЕНИЕ РИСКАМИ — Зачистка, ликвидация, защита активов, соблюдение карантина, охота за головами, реагирование на сигнал бедствия, патрулирование системы.",
    "КАДРОВЫЕ РЕСУРСЫ — Поиск пропавших, подозрительная смерть, сбой связи, устранение неполадок, переговоры с ИИ, эвакуация поселений.",
    "СЛИЯНИЯ И ПОГЛОЩЕНИЯ — Возврат активов, удержание утилизации, подбор персонала, протокол первого контакта, изъятие имущества, пиратство.",
]
_CONTRACT_UA = [
    "ВИРОБНИЦТВО ТА ВИДОБУТОК — Гірська розробка астероїдів, утилізація дрейфуючих кораблів, зрив страйків, встановлення терраформерів, обслуговування андроїдів.",
    "ТРАНСПОРТУВАННЯ — Доставка вантажів, супровід ВІП, вивіз металобрухту, перевезення ув'язнених, обробка чутливих матеріалів, транспорт пасажирів, контрабанда.",
    "ДОСЛІДЖЕННЯ ТА РОЗРОБКИ — Збір зразків, планетарна розвідка, польові випробування, саботаж, ліквідація витоку, археологічні розкопки, корпоративний шпіонаж.",
    "УПРАВЛІННЯ РИЗИКАМИ — Зачистка, ліквідація, захист активів, дотримання карантину, полювання за головами, реагування на сигнал лиха, патрулювання системи.",
    "КАДРОВІ РЕСУРСИ — Пошук зниклих, підозріла смерть, збій зв'язку, усунення несправностей, переговори зі ШІ, евакуація поселень.",
    "ЗЛИТТЯ ТА ПОГЛИНАННЯ — Повернення активів, утримання утилізації, підбір персоналу, протокол першого контакту, вилучення майна, піратство.",
]

_CONTRACT_DESC = (
    # EN
    "Roll to determine the department offering contract work. See Pay Scale for payment.\n\n"
    "0–1: PRODUCTION & MANUFACTURE\n2–3: SHIPPING & HANDLING\n4–5: RESEARCH & DEVELOPMENT\n"
    "6–7: RISK MANAGEMENT\n8: HUMAN RESOURCES\n9: MERGERS & ACQUISITIONS",
    # RU
    "Бросьте, чтобы определить отдел, предлагающий контрактную работу. Оплата — по Шкале оплаты.\n\n"
    "0–1: ПРОИЗВОДСТВО И ДОБЫЧА\n2–3: ТРАНСПОРТИРОВКА\n4–5: ИССЛЕДОВАНИЯ И РАЗРАБОТКИ\n"
    "6–7: УПРАВЛЕНИЕ РИСКАМИ\n8: КАДРОВЫЕ РЕСУРСЫ\n9: СЛИЯНИЯ И ПОГЛОЩЕНИЯ",
    # UA
    "Киньте, щоб визначити відділ, що пропонує контрактну роботу. Оплата — за Шкалою оплати.\n\n"
    "0–1: ВИРОБНИЦТВО ТА ВИДОБУТОК\n2–3: ТРАНСПОРТУВАННЯ\n4–5: ДОСЛІДЖЕННЯ ТА РОЗРОБКИ\n"
    "6–7: УПРАВЛІННЯ РИЗИКАМИ\n8: КАДРОВІ РЕСУРСИ\n9: ЗЛИТТЯ ТА ПОГЛИНАННЯ",
)

# ── C196 Pay Scale (d100 rollable) ────────────────────────────────────────────
_PAY_ENTRIES = [
    {"min": 0,  "max": 0,  "text": "POWERFUL FAVOR — The client can't pay, but owes the crew a big favor to call in at their discretion. Lifestyle: DEAD BROKE — 1d10 days of living expenses or one piece of cheap equipment."},
    {"min": 1,  "max": 9,  "text": "DESPERATE — Pays 1d10×100cr up front. This is all the money the client has. Doing this job makes them a long-time ally. Lifestyle: SCRAPING BY — 1d10 weeks of living expenses or one piece of decent equipment."},
    {"min": 10, "max": 34, "text": "BARTER AGREEMENT — Trade only: astronavigation data, ship repairs, weapons, equipment, or other accommodations. Lifestyle: NEED WORK — 1d10 months of living expenses or one piece of expensive equipment."},
    {"min": 35, "max": 93, "text": "GRUNT WORK — Pays the crew's salaries; expenses are the crew's to handle. No Jump Pay or Hazard Pay. Lifestyle: PAYING DOWN DEBT — C/B/A-Class Shore Leave, cheap cybermod, medical treatment, minor bribe, or skill training."},
    {"min": 94, "max": 98, "text": "PAYDAY — Pays 1d10×10,000cr upon completion and up to 10% up front. All travel expenses paid; up to 1d10 Contractors provided. Lifestyle: FLUSH WITH CREDITS — X/S-Class Shore Leave, decent cybermod, or a ship upgrade."},
    {"min": 99, "max": 99, "text": "JACKPOT — Pays 1d10×1,000,000cr upon completion and up to 1d10×10,000cr up front. All necessary expenses paid; private contractors available. Lifestyle: I CAN RETIRE AFTER THIS JOB — Enough for a small ship, small business, or retirement."},
]
_PAY_RU = [
    "ВЛИЯТЕЛЬНОЕ ОДОЛЖЕНИЕ — Клиент не может заплатить, но должен команде большое одолжение. Образ жизни: ПО НУЛЯМ — 1d10 дней расходов на жизнь или одна дешёвая вещь.",
    "ОТЧАЯНИЕ — Платит 1d10×100 кр. авансом. Это всё, что есть у клиента. Выполнение работы делает его долгосрочным союзником. Образ жизни: ЕДВА СВОДИТ КОНЦЫ — 1d10 недель расходов или одна приличная вещь.",
    "БАРТЕР — Только обмен: данные астронавигации, ремонт корабля, оружие, снаряжение или проживание. Образ жизни: НУЖНА РАБОТА — 1d10 месяцев расходов или одна дорогая вещь.",
    "РУТИННАЯ РАБОТА — Платит зарплаты команды; расходы за счёт команды. Никакой надбавки за прыжок или риск. Образ жизни: ВЫПЛАТА ДОЛГОВ — Берег. отпуск C/B/A, дешёвый киберрм, мед. помощь, небольшая взятка или обучение навыку.",
    "ХОРОШАЯ ОПЛАТА — Платит 1d10×10 000 кр. по завершению и до 10% аванса. Все расходы на дорогу покрыты; до 1d10 Подрядчиков. Образ жизни: В ДЕНЬГАХ — Берег. отпуск X/S, приличный кибермод или апгрейд корабля.",
    "ДЖЕКПОТ — Платит 1d10×1 000 000 кр. по завершению и до 1d10×10 000 кр. аванса. Все расходы покрыты; частные подрядчики доступны. Образ жизни: МОЖНО НА ПЕНСИЮ — Хватит на корабль, малый бизнес или выход на пенсию.",
]
_PAY_UA = [
    "ВПЛИВОВА ПОСЛУГА — Клієнт не може заплатити, але завдячує команді велику послугу. Спосіб життя: НА НУЛЯХ — 1d10 днів витрат на прожиток або одна дешева річ.",
    "ВІДЧАЙ — Платить 1d10×100 кр. авансом. Це все, що є у клієнта. Виконання роботи робить його довгостроковим союзником. Спосіб життя: ЛЕДВЕ ЗВОДИТЬ КІНЦІ — 1d10 тижнів витрат або одна пристойна річ.",
    "БАРТЕР — Лише обмін: дані астронавігації, ремонт корабля, зброя, спорядження або проживання. Спосіб життя: ПОТРІБНА РОБОТА — 1d10 місяців витрат або одна дорога річ.",
    "БУДЕННА РОБОТА — Платить зарплати команди; витрати за рахунок команди. Жодної надбавки за стрибок або ризик. Спосіб життя: ВИПЛАТА БОРГІВ — Берег. відпустка C/B/A, дешевий кіберм, мед. допомога, невелика хабара або навчання навичці.",
    "ХОРОША ОПЛАТА — Платить 1d10×10 000 кр. після завершення і до 10% авансу. Усі дорожні витрати покриті; до 1d10 Підрядників. Спосіб життя: У ГРОШАХ — Берег. відпустка X/S, пристойний кібермод або апгрейд корабля.",
    "ДЖЕКПОТ — Платить 1d10×1 000 000 кр. після завершення і до 1d10×10 000 кр. авансу. Усі витрати покриті; приватні підрядники доступні. Спосіб життя: МОЖНА НА ПЕНСІЮ — Вистачить на корабель, малий бізнес або вихід на пенсію.",
]

_PAY_DESC = (
    # EN
    "Salary: 500cr/month per Trained Skill, 1,000cr/month per Expert Skill, 2,000cr/month per Master Skill.\n"
    "Jump Pay: flat bonus equal to Jump × 1,000cr.\n"
    "Hazard Pay: 1d5 months of salary as a bonus (not an admission of liability).",
    # RU
    "Зарплата: 500 кр./мес. за каждый Обученный навык, 1 000 кр./мес. за Экспертный, 2 000 кр./мес. за Мастерский.\n"
    "Надбавка за прыжок: фиксированный бонус равный Прыжку × 1 000 кр.\n"
    "Боевые: 1d5 месяца зарплаты в качестве бонуса (не признание ответственности).",
    # UA
    "Зарплата: 500 кр./міс. за кожну Навчену навичку, 1 000 кр./міс. за Експертну, 2 000 кр./міс. за Майстерну.\n"
    "Надбавка за стрибок: фіксований бонус рівний Стрибку × 1 000 кр.\n"
    "Бойові: 1d5 місяця зарплати як бонус (не визнання відповідальності).",
)

# ── C197 Campaign Economics ───────────────────────────────────────────────────
_ECONOMICS = (
    # EN
    "Money in Mothership limits players' options — another resource like Health and Stress to manage.\n\n"
    "NET WORTH TABLE:\n"
    "Nothing — Everything.\n"
    "Hundreds — Basic living: food, shelter.\n"
    "Thousands — Weapons, equipment, Shore Leave, rent, space travel.\n"
    "Hundreds of thousands — Cybermods, private contractors, skill training, land vehicles.\n"
    "Millions — Ship repairs, fuel, and maintenance.\n"
    "Tens of millions — Mechs, small spacecraft, small businesses.\n"
    "Hundreds of millions — Ships, asteroids, small fleets.\n"
    "Billions — Companies, R&D, moons, private armies.\n"
    "Trillions — War, colonisation, planets, space stations.\n\n"
    "DEBT: In Mothership, debt means owing violent people non-trivial money. Players increase minimum Stress by 1 for every significant debtor. Loan terms: 1d5×10% downpayment, interest equal to the amount borrowed (pay back double), term of 2d10 months.\n\n"
    "KEY PRINCIPLES:\n"
    "• The shorter the campaign, the less important the economics.\n"
    "• Favours and information are more interesting rewards than credits.\n"
    "• Upper mobility is statistically impossible. Vast wealth is held by a small number of generationally wealthy companies and families.",
    # RU
    "Деньги в Mothership ограничивают возможности игроков — ещё один ресурс наряду со Здоровьем и Стрессом.\n\n"
    "ТАБЛИЦА СОСТОЯНИЯ:\n"
    "Ничего — Буквально всё.\n"
    "Сотни — Базовое проживание: еда, кров.\n"
    "Тысячи — Оружие, снаряжение, береговой отпуск, аренда, перелёты.\n"
    "Сотни тысяч — Кибермоды, подрядчики, обучение навыкам, наземный транспорт.\n"
    "Миллионы — Ремонт корабля, топливо и обслуживание.\n"
    "Десятки миллионов — Мехи, малые корабли, малый бизнес.\n"
    "Сотни миллионов — Корабли, астероиды, малые флоты.\n"
    "Миллиарды — Компании, НИОКР, луны, частные армии.\n"
    "Триллионы — Война, колонизация, планеты, космические станции.\n\n"
    "ДОЛГ: В Mothership долг означает задолженность перед жестокими людьми. Игроки увеличивают минимальный Стресс на 1 за каждого значимого кредитора. Условия займа: первоначальный взнос 1d5×10%, проценты равные сумме займа (выплата двойной суммы), срок 2d10 месяцев.\n\n"
    "КЛЮЧЕВЫЕ ПРИНЦИПЫ:\n"
    "• Чем короче кампания, тем менее важна экономика.\n"
    "• Услуги и информация — более интересные награды, чем кредиты.\n"
    "• Социальная мобильность статистически невозможна. Большинство богатства сосредоточено в руках немногих.",
    # UA
    "Гроші в Mothership обмежують можливості гравців — ще один ресурс поряд зі Здоров'ям і Стресом.\n\n"
    "ТАБЛИЦЯ СТАТКУ:\n"
    "Нічого — Буквально все.\n"
    "Сотні — Базове проживання: їжа, дах над головою.\n"
    "Тисячі — Зброя, спорядження, береговий відпочинок, оренда, перельоти.\n"
    "Сотні тисяч — Кібермоди, підрядники, навчання навичкам, наземний транспорт.\n"
    "Мільйони — Ремонт корабля, пальне та обслуговування.\n"
    "Десятки мільйонів — Мехи, малі кораблі, малий бізнес.\n"
    "Сотні мільйонів — Кораблі, астероїди, малі флоти.\n"
    "Мільярди — Компанії, НДДКР, місяці, приватні армії.\n"
    "Трильйони — Війна, колонізація, планети, космічні станції.\n\n"
    "БОРГ: У Mothership борг означає заборгованість перед жорстокими людьми. Гравці збільшують мінімальний Стрес на 1 за кожного значного кредитора. Умови позики: перший внесок 1d5×10%, відсотки рівні сумі позики (виплата подвійної суми), строк 2d10 місяців.\n\n"
    "КЛЮЧОВІ ПРИНЦИПИ:\n"
    "• Чим коротша кампанія, тим менш важлива економіка.\n"
    "• Послуги та інформація — більш цікаві нагороди, ніж кредити.\n"
    "• Соціальна мобільність статистично неможлива. Більшість багатства сконцентровано в руках небагатьох.",
)

# ── C198 Ending Your Campaign ─────────────────────────────────────────────────
_ENDING = (
    # EN
    "Sooner or later every campaign ends. Knowing how and when to end it gives players closure and a sense of accomplishment.\n\n"
    "RUN SHORTER CAMPAIGNS & SEQUELS: Set a clear goal up front. Ask a question and end the campaign when your players have the answer. Ask whose characters survived what they plan to do next, then start a sequel with some of the same characters and a few new ones.\n\n"
    "OMEGA SESSIONS: When you see the symptoms (players missing more sessions, people can't remember what happened last time, longer breaks between games), schedule an Omega Session. Cut right to the end — drop your players into one last session that brings the house down. Everyone finds out who lives and who dies, what the mystery was all about, and everyone goes home with an ending.\n\n"
    "CAMPAIGN MAINTENANCE:\n"
    "• Skip 1d10 months between adventures to avoid non-stop struggle.\n"
    "• Run slice-of-life sessions where players visit friends, shop, and pursue relationships.\n"
    "• Threats page: three major Threats with three escalating events each, on a calendar.\n"
    "• Fallout page: track consequences of players' actions between sessions.",
    # RU
    "Рано или поздно каждая кампания заканчивается. Знание того, как и когда завершить её, даёт игрокам ощущение завершённости.\n\n"
    "КОРОТКИЕ КАМПАНИИ И СИКВЕЛЫ: Установите чёткую цель с самого начала. Задайте вопрос и завершите кампанию, когда игроки найдут ответ. Спросите, чьи персонажи выжили и что планируют дальше, затем начните сиквел с частью старых персонажей и несколькими новыми.\n\n"
    "ОМЕГА-СЕССИИ: Когда появляются признаки угасания (игроки пропускают сессии, никто не помнит, что было в прошлый раз, перерывы всё длиннее), запланируйте Омега-сессию. Прыжок к финалу — бросьте игроков в последнюю сессию, которая всё решит. Все узнают, кто выжил и кто умер, в чём была тайна, и все уходят с концовкой.\n\n"
    "СОПРОВОЖДЕНИЕ КАМПАНИИ:\n"
    "• Пропускайте 1d10 месяцев между приключениями.\n"
    "• Проводите бытовые сессии, где игроки встречаются с друзьями, ходят по магазинам и развивают отношения.\n"
    "• Страница Угроз: три основные Угрозы с тремя нарастающими событиями каждая, на календаре.\n"
    "• Страница Последствий: отслеживайте последствия действий игроков между сессиями.",
    # UA
    "Рано чи пізно кожна кампанія закінчується. Знання того, як і коли завершити її, дає гравцям відчуття завершеності.\n\n"
    "КОРОТКІ КАМПАНІЇ ТА СИКВЕЛИ: Встановіть чітку мету з самого початку. Поставте питання і завершіть кампанію, коли гравці знайдуть відповідь. Запитайте, чиї персонажі вижили і що планують далі, потім почніть сиквел із частиною старих персонажів і кількома новими.\n\n"
    "ОМЕГА-СЕСІЇ: Коли з'являються ознаки згасання (гравці пропускають сесії, ніхто не пам'ятає, що було минулого разу, перерви все довші), заплануйте Омега-сесію. Стрибок до фіналу — киньте гравців в останню сесію, яка вирішить усе. Всі дізнаються, хто вижив і хто помер, у чому була таємниця, і всі йдуть із кінцівкою.\n\n"
    "СУПРОВІД КАМПАНІЇ:\n"
    "• Пропускайте 1d10 місяців між пригодами.\n"
    "• Проводьте побутові сесії, де гравці зустрічаються з друзями, ходять по магазинах і розвивають стосунки.\n"
    "• Сторінка Загроз: три основні Загрози з трьома наростаючими подіями кожна, на календарі.\n"
    "• Сторінка Наслідків: відстежуйте наслідки дій гравців між сесіями.",
)


# ── Content list: (id, icon, source_page, has_dice, die, entries, names, descs, dice_ru, dice_ua) ──
P27_CONTENTS = [
    {
        "id": 191, "icon": "🗒️", "source_page": 41,
        "name": ("Campaign Style", "Стиль кампании", "Стиль кампанії"),
        "desc": _STYLE,
        "dice": None,
    },
    {
        "id": 192, "icon": "🌌", "source_page": 42,
        "name": ("Campaign Frames", "Рамки кампании", "Рамки кампанії"),
        "desc": _FRAMES,
        "dice": None,
    },
    {
        "id": 193, "icon": "🏢", "source_page": 47,
        "name": ("The Company", "Компания", "Компанія"),
        "desc": _COMPANY,
        "dice": None,
    },
    {
        "id": 194, "icon": "⚙️", "source_page": 46,
        "name": ("How to Create Factions", "Как создать фракции", "Як створити фракції"),
        "desc": _FACTIONS,
        "dice": None,
    },
    {
        "id": 195, "icon": "💼", "source_page": 48,
        "name": ("Contract Work", "Контрактная работа", "Контрактна робота"),
        "desc": _CONTRACT_DESC,
        "dice": dice_json("d10", _CONTRACT_ENTRIES),
        "dice_ru": _CONTRACT_RU,
        "dice_ua": _CONTRACT_UA,
    },
    {
        "id": 196, "icon": "💰", "source_page": 49,
        "name": ("Pay Scale", "Шкала оплаты", "Шкала оплати"),
        "desc": _PAY_DESC,
        "dice": dice_json("d100", _PAY_ENTRIES),
        "dice_ru": _PAY_RU,
        "dice_ua": _PAY_UA,
    },
    {
        "id": 197, "icon": "📈", "source_page": 50,
        "name": ("Campaign Economics", "Экономика кампании", "Економіка кампанії"),
        "desc": _ECONOMICS,
        "dice": None,
    },
    {
        "id": 198, "icon": "🔚", "source_page": 57,
        "name": ("Ending Your Campaign", "Завершение кампании", "Завершення кампанії"),
        "desc": _ENDING,
        "dice": None,
    },
]


def _seed(conn: sqlite3.Connection) -> None:
    for c in P27_CONTENTS:
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
            if lang == "ru" and "dice_ru" in c:
                dice_entries = json.dumps(c["dice_ru"], ensure_ascii=False)
            elif lang == "ua" and "dice_ua" in c:
                dice_entries = json.dumps(c["dice_ua"], ensure_ascii=False)

            conn.execute("""
                INSERT OR IGNORE INTO content_i18n
                    (content_id, lang, name, desc, dice_entries)
                VALUES (?, ?, ?, ?, ?)
            """, (cid, lang, name, desc, dice_entries))

        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (27, ?, ?)
        """, (cid, cid))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(P27_CONTENTS)} P27 Campaign Building contents seeded into '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
