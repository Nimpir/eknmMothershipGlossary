"""
scripts/add_wom_part1_pages.py
Warden's Operations Manual — Part 1: source, pages P23-P28, P24 Session Prep contents C172-C178.
Updates P1 linked_pages to include P23.
Run: python scripts/add_wom_part1_pages.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── Pages ─────────────────────────────────────────────────────────────────────
# (id, icon, source_page, name_en, name_ru, name_ua)
PAGES = [
    (23, "🎭", None, "Warden's Guide",     "Руководство Судьи",    "Посібник Судді"),
    (24, "📋", 4,    "Session Prep",        "Подготовка Сессии",    "Підготовка Сесії"),
    (25, "👾", 8,    "The Horror",          "Ужас",                 "Жах"),
    (26, "🎙️", 26,   "Running the Game",    "Ведение Игры",         "Ведення Гри"),
    (27, "🗺️", 41,   "Campaign Building",   "Построение Кампании",  "Побудова Кампанії"),
    (28, "🎲", 58,   "Random Generators",   "Случайные Генераторы", "Випадкові Генератори"),
]

# ── P24 Session Prep contents ─────────────────────────────────────────────────
P24_CONTENTS = [
    {
        "id": 172, "icon": "🎬", "source_page": 6,
        "name": (
            "Starting Scenarios",
            "Стартовые Сценарии",
            "Стартові Сценарії",
        ),
        "desc": (
            "Roll 1d10 (1–10) or pick a scenario type for your first session.",
            "Бросьте 1d10 (1–10) или выберите тип сценария для первой сессии.",
            "Киньте 1d10 (1–10) або оберіть тип сценарію для першої сесії.",
        ),
        "dice": {"die": "d10", "entries": [
            {"min": 1,  "max": 1,  "text": "Explore the Unknown — Survey an uncharted planet or strange vessel. No backup. God speed."},
            {"min": 2,  "max": 2,  "text": "Investigate a Strange Rumor — Something is alive in the vents. Colonists are disappearing. Separating fact from fiction was the easy part."},
            {"min": 3,  "max": 3,  "text": "Salvage a Derelict Ship — Distress signal on repeat. Scans show no life. Every abandoned ship is abandoned for a reason."},
            {"min": 4,  "max": 4,  "text": "Exterminate an Otherworldly Threat — No one goes outside anymore. Wipe them out by any means. Bring back a living sample."},
            {"min": 5,  "max": 5,  "text": "Visit an Offworld Colony — The Company hasn't heard from the miners on PK-294. Get production back on track."},
            {"min": 6,  "max": 6,  "text": "Undertake a Dangerous Mission — A C-level's child kidnapped by a fringe group. Android activists want to sabotage a facility. No scruples required."},
            {"min": 7,  "max": 7,  "text": "Survive a Colossal Disaster — Abandon ship! Radiation leaks and warp anomalies. Make it to the escape pods before the station collapses."},
            {"min": 8,  "max": 8,  "text": "Respond to a Distress Signal — Help is never nearby on the rim. You can never tell legitimate cries from traps laid by wolves."},
            {"min": 9,  "max": 9,  "text": "Transport Precious Cargo — They won't tell you what's in the container. Don't open it, don't scan it, don't listen to anything it says."},
            {"min": 10, "max": 10, "text": "Make Contact with the Beyond — Found at the edge of the system. Eons old, intricate stonework. When the probe arrived, it started humming a tune."},
        ]},
        "dice_ru": [
            "Исследуйте Неизведанное — Разведка неизвестной планеты или странного корабля. Без подкрепления. Помогай вам бог.",
            "Расследуйте Странной Слух — Что-то живёт в вентиляции. Колонисты исчезают. Отделить правду от вымысла было лёгкой частью.",
            "Мародёрство Деrelict-корабля — Сигнал бедствия повторяется. Сканеры не показывают жизни. Каждый брошенный корабль брошен не зря.",
            "Уничтожьте Потустороннюю Угрозу — Никто больше не выходит наружу. Уничтожить любыми средствами. Принести живой образец.",
            "Посетите Внеземную Колонию — Корпорация не получает новостей с шахт PK-294. Восстановите производство.",
            "Выполните Опасную Миссию — Ребёнок топ-менеджера похищен сектой. Андроиды-активисты хотят саботировать завод. Без угрызений совести.",
            "Переживите Колоссальную Катастрофу — Покинуть корабль! Утечка радиации и аномалии варп-двигателя. Добраться до капсул до того, как станция рухнет.",
            "Откликнитесь на Сигнал Бедствия — На окраине помощь никогда не близко. Не всегда понять: настоящий крик или ловушка.",
            "Перевезите Ценный Груз — Содержимое контейнера — тайна. Не открывать, не сканировать, не слушать то, что внутри говорит.",
            "Установите Контакт с Запредельным — Найдено на краю системы. Тысячелетней давности. Когда прилетел зонд, оно начало гудеть мелодию.",
        ],
        "dice_ua": [
            "Досліджуйте Невідоме — Розвідка невідомої планети або дивного корабля. Без підкріплення. Бережіть себе.",
            "Розслідуйте Дивний Слух — Щось живе у вентиляції. Колоністи зникають. Відокремити правду від вигадки було легкою частиною.",
            "Мародерство на Покинутому Кораблі — Сигнал лиха повторюється. Сканери не показують жодного життя. Кожен покинутий корабель покинутий не просто так.",
            "Знищте Потойбічну Загрозу — Ніхто більше не виходить надвір. Знищити будь-якими засобами. Принести живий зразок.",
            "Відвідайте Позаземну Колонію — Корпорація не отримує новин з шахт PK-294. Відновіть виробництво.",
            "Виконайте Небезпечну Місію — Дитину топ-менеджера викрала секта. Андроїди-активісти хочуть саботувати завод. Без жодних докорів сумління.",
            "Переживіть Колосальну Катастрофу — Покинути корабель! Витік радіації та аномалії варп-двигуна. Дістатися капсул до того, як станція впаде.",
            "Відгукніться на Сигнал Лиха — На окраїні допомога ніколи не близько. Неможливо відрізнити справжній крик від пастки.",
            "Перевезіть Цінний Вантаж — Вміст контейнера — таємниця. Не відкривати, не сканувати, не слухати те, що всередині говорить.",
            "Встановіть Контакт із Потойбічним — Знайдено на краю системи. Тисячолітньої давнини. Коли прилетів зонд, воно почало наспівувати мелодію.",
        ],
    },
    {
        "id": 173, "icon": "🏙️", "source_page": 6,
        "name": (
            "Setting Table",
            "Таблица Локаций",
            "Таблиця Локацій",
        ),
        "desc": (
            "Roll 1d10 (0–9) for a starting location.",
            "Бросьте 1d10 (0–9) для выбора стартовой локации.",
            "Киньте 1d10 (0–9) для вибору стартової локації.",
        ),
        "dice": {"die": "d10", "entries": [
            {"min": 0, "max": 0, "text": "Space Station"},
            {"min": 1, "max": 1, "text": "Aboard Your Own Ship"},
            {"min": 2, "max": 2, "text": "Military Outpost"},
            {"min": 3, "max": 3, "text": "Prison Complex"},
            {"min": 4, "max": 4, "text": "Derelict Spacecraft"},
            {"min": 5, "max": 5, "text": "Religious Compound"},
            {"min": 6, "max": 6, "text": "Mining Colony"},
            {"min": 7, "max": 7, "text": "Research Facility"},
            {"min": 8, "max": 8, "text": "Underwater Base"},
            {"min": 9, "max": 9, "text": "Mothership"},
        ]},
        "dice_ru": [
            "Космическая Станция",
            "На Собственном Корабле",
            "Военный Аванпост",
            "Тюремный Комплекс",
            "Брошенный Космический Корабль",
            "Религиозный Комплекс",
            "Горнодобывающая Колония",
            "Исследовательский Объект",
            "Подводная База",
            "Материнский Корабль",
        ],
        "dice_ua": [
            "Космічна Станція",
            "На Власному Кораблі",
            "Військовий Аванпост",
            "Тюремний Комплекс",
            "Покинутий Космічний Корабель",
            "Релігійний Комплекс",
            "Гірничодобувна Колонія",
            "Дослідницький Об'єкт",
            "Підводна База",
            "Материнський Корабель",
        ],
    },
    {
        "id": 174, "icon": "🛡️", "source_page": 10,
        "name": (
            "Something to Survive",
            "Нечто, Чтобы Выжить",
            "Щось, Щоб Вижити",
        ),
        "desc": (
            "Create obstacles that threaten the players' survival. Vary the types:\n\n"
            "Environmental Hazards — Space is the most inhospitable environment. Use as a palette cleanser for violence.\n"
            "• Dangerous vegetation, toxic atmosphere, radiation, zero-gravity, volcanoes, underwater locations, caves, lack of oxygen.\n\n"
            "Violent Encounters — The most common obstacle. Use sparingly and brutally so players learn to avoid them.\n"
            "• Brawls, chases, ship-to-ship combat, sieges, tactical gunfights.\n\n"
            "Psychological Trauma — Represented by Sanity, Fear, and Stress mechanics.\n"
            "• Creepy environment, darkness, loneliness, isolation, splitting the group, evidence of violence, Omens.\n\n"
            "Resource Scarcity — Keeping resources scarce and forcing hard choices amps up tension.\n"
            "• Lack of oxygen, food, ammo. Destroyed equipment. Time. Fuel. Credits.\n\n"
            "Social Pressures — Convincing others is often the difference between living and dying.\n"
            "• Good planning, convincing arguments, negotiation, favors, allies, and enemies.",

            "Создайте препятствия, угрожающие выживанию игроков. Варьируйте типы:\n\n"
            "Экологические Опасности — Космос — самая негостеприимная среда. Используйте как контраст к насилию.\n"
            "• Опасная растительность, токсичная атмосфера, радиация, невесомость, вулканы, подводные локации, пещеры, нехватка кислорода.\n\n"
            "Насильственные Встречи — Самое распространённое препятствие. Используйте редко и жестоко.\n"
            "• Потасовки, погони, бой корабль-корабль, осады, перестрелки.\n\n"
            "Психологическая Травма — Отражается механиками Рассудка, Страха и Стресса.\n"
            "• Жуткая обстановка, темнота, одиночество, изоляция, разделение группы, следы насилия, Знамения.\n\n"
            "Нехватка Ресурсов — Дефицит ресурсов и трудный выбор накаляют обстановку.\n"
            "• Нехватка кислорода, еды, патронов. Уничтоженное оборудование. Время. Топливо. Кредиты.\n\n"
            "Социальное Давление — Убеждение других часто решает вопрос жизни и смерти.\n"
            "• Хорошее планирование, убедительные аргументы, переговоры, услуги, союзники и враги.",

            "Створіть перешкоди, що загрожують виживанню гравців. Варіюйте типи:\n\n"
            "Екологічні Небезпеки — Космос — найнегостинніше середовище. Використовуйте як контраст до насилля.\n"
            "• Небезпечна рослинність, токсична атмосфера, радіація, невагомість, вулкани, підводні локації, печери, брак кисню.\n\n"
            "Насильницькі Зустрічі — Найпоширеніша перешкода. Використовуйте рідко і жорстоко.\n"
            "• Бійки, погоні, бій корабель-корабель, облоги, перестрілки.\n\n"
            "Психологічна Травма — Відображається механіками Розуму, Страху та Стресу.\n"
            "• Моторошна обстановка, темрява, самотність, ізоляція, розділення групи, сліди насилля, Знамення.\n\n"
            "Дефіцит Ресурсів — Дефіцит ресурсів і важкий вибір нагнітають обстановку.\n"
            "• Брак кисню, їжі, набоїв. Знищене обладнання. Час. Пальне. Кредити.\n\n"
            "Соціальний Тиск — Переконання інших часто вирішує питання життя і смерті.\n"
            "• Хороше планування, переконливі аргументи, переговори, послуги, союзники та вороги.",
        ),
        "dice": None,
    },
    {
        "id": 175, "icon": "🔍", "source_page": 12,
        "name": (
            "Something to Solve",
            "Нечто, Что Решить",
            "Щось, Що Вирішити",
        ),
        "desc": (
            "Every mystery has a Question. Every puzzle is an obstacle that, when defeated, reveals a new secret. Every answer points to a new lead.\n\n"
            "Questions:\n"
            "• What happened here? — Clues at the scene reveal the truth.\n"
            "• Who did it? — Whoever did it doesn't want to be found. Ever.\n"
            "• Where are they? — From missing persons to entire disappeared colonies.\n\n"
            "Puzzle Components: use 1–2 components per puzzle. Too many components = too complicated. (See Puzzle Components table.)\n\n"
            "Tips for good answers:\n"
            "• Show the lock before the key.\n"
            "• Call the same thing by two or three different names — players fill in their own backstory.\n"
            "• Answers lead to new questions.\n"
            "• Reveal facts, not conclusions.\n"
            "• More clues than you think you need.",

            "У каждой тайны есть Вопрос. Каждая головоломка — препятствие, которое при решении раскрывает новый секрет. Каждый ответ указывает на новую зацепку.\n\n"
            "Вопросы:\n"
            "• Что здесь произошло? — Улики на месте событий раскрывают правду.\n"
            "• Кто это сделал? — Тот, кто это сделал, не хочет быть найденным. Никогда.\n"
            "• Где они? — От пропавших людей до исчезнувших колоний.\n\n"
            "Компоненты головоломки: используйте 1–2 компонента на головоломку. Слишком много = слишком сложно. (См. таблицу Компонентов Головоломок.)\n\n"
            "Советы по хорошим ответам:\n"
            "• Покажите замок до ключа.\n"
            "• Называйте одно и то же разными именами — игроки сами придумают историю.\n"
            "• Ответы ведут к новым вопросам.\n"
            "• Раскрывайте факты, а не выводы.\n"
            "• Больше улик, чем вам кажется нужным.",

            "У кожної таємниці є Питання. Кожна головоломка — перешкода, яка при вирішенні розкриває новий секрет. Кожна відповідь вказує на нову зачіпку.\n\n"
            "Питання:\n"
            "• Що тут сталося? — Докази на місці події розкривають правду.\n"
            "• Хто це зробив? — Той, хто це зробив, не хоче бути знайденим. Ніколи.\n"
            "• Де вони? — Від зниклих людей до зниклих колоній.\n\n"
            "Компоненти головоломки: використовуйте 1–2 компоненти на головоломку. Занадто багато = занадто складно. (Дивіться таблицю Компонентів Головоломок.)\n\n"
            "Поради щодо хороших відповідей:\n"
            "• Покажіть замок до ключа.\n"
            "• Називайте одне й те саме різними іменами — гравці самі придумають історію.\n"
            "• Відповіді ведуть до нових питань.\n"
            "• Розкривайте факти, а не висновки.\n"
            "• Більше підказок, ніж вам здається потрібним.",
        ),
        "dice": None,
    },
    {
        "id": 176, "icon": "🤝", "source_page": 16,
        "name": (
            "Someone to Save",
            "Кого-то Спасти",
            "Когось Врятувати",
        ),
        "desc": (
            "Every scenario needs someone worth saving. Design characters with clear wants and put them in peril.\n\n"
            "Define each character by:\n"
            "1. What do they think with? (fists, wallet, heart, watch?)\n"
            "2. What do they want? (concrete, attainable, material goal)\n"
            "3. How do the players interact with them?\n\n"
            "Character matrix (Powerful ↔ Powerless / Helpful ↔ Unhelpful):\n"
            "• Gatekeeper — powerful, unhelpful. Blocks what you want.\n"
            "• Employer — powerful, neutral. You work for them.\n"
            "• Benefactor — powerful, helpful. Rarest ally.\n"
            "• Traitor — could be anyone. The more helpful, the worse the betrayal.\n"
            "• Survivor — only cares about themselves. Help them or get out of the way.\n"
            "• Expert — their power is their expertise.\n"
            "• Coward — powerless, unhelpful. Completely useless.\n"
            "• Victim — needs you the most.\n"
            "• Drinking Buddy — would do anything; just not much they can do.\n"
            "• Wildcard — unpredictable. Use sparingly.\n\n"
            "For your first session: one Gatekeeper, one Drinking Buddy, one Survivor.",

            "Каждому сценарию нужен кто-то, кого стоит спасти. Создавайте персонажей с чёткими желаниями и ставьте их в опасность.\n\n"
            "Определите каждого персонажа через:\n"
            "1. Чем он думает? (кулаки, кошелёк, сердце, часы?)\n"
            "2. Чего он хочет? (конкретная, достижимая, материальная цель)\n"
            "3. Как игроки взаимодействуют с ним?\n\n"
            "Матрица персонажей (Сильный ↔ Слабый / Полезный ↔ Бесполезный):\n"
            "• Привратник — сильный, бесполезный. Блокирует то, что вам нужно.\n"
            "• Работодатель — сильный, нейтральный. Вы работаете на него.\n"
            "• Благодетель — сильный, полезный. Редчайший союзник.\n"
            "• Предатель — может быть кем угодно. Чем полезнее, тем хуже предательство.\n"
            "• Выживший — думает только о себе. Помогите или уйдите с дороги.\n"
            "• Эксперт — его сила в его знаниях.\n"
            "• Трус — слабый, бесполезный. Совершенно бесполезен.\n"
            "• Жертва — нуждается в вас больше всего.\n"
            "• Собутыльник — сделает всё, что угодно; просто мало что может.\n"
            "• Непредсказуемый — хаотичен. Используйте редко.\n\n"
            "Для первой сессии: один Привратник, один Собутыльник, один Выживший.",

            "Кожен сценарій потребує когось, кого варто врятувати. Створюйте персонажів із чіткими бажаннями і ставте їх у небезпеку.\n\n"
            "Визначте кожного персонажа через:\n"
            "1. Чим він думає? (кулаки, гаманець, серце, годинник?)\n"
            "2. Чого він хоче? (конкретна, досяжна, матеріальна мета)\n"
            "3. Як гравці взаємодіють із ним?\n\n"
            "Матриця персонажів (Сильний ↔ Слабкий / Корисний ↔ Некорисний):\n"
            "• Воротар — сильний, некорисний. Блокує те, що вам потрібно.\n"
            "• Роботодавець — сильний, нейтральний. Ви працюєте на нього.\n"
            "• Благодійник — сильний, корисний. Найрідкісніший союзник.\n"
            "• Зрадник — може бути ким завгодно. Що корисніший, то гірше зрадництво.\n"
            "• Той, хто виживає — думає лише про себе. Допоможіть або йдіть з дороги.\n"
            "• Експерт — його сила в його знаннях.\n"
            "• Боягуз — слабкий, некорисний. Абсолютно марний.\n"
            "• Жертва — потребує вас найбільше.\n"
            "• Приятель — зробить усе що завгодно; просто мало що може.\n"
            "• Непередбачуваний — хаотичний. Використовуйте рідко.\n\n"
            "Для першої сесії: один Воротар, один Приятель, один Той, хто виживає.",
        ),
        "dice": None,
    },
    {
        "id": 177, "icon": "⚡", "source_page": 11,
        "name": (
            "Tactical Considerations",
            "Тактические Соображения",
            "Тактичні Міркування",
        ),
        "desc": (
            "Roll 1d12 to add a tactical wrinkle to a violent encounter.",
            "Бросьте 1d12, чтобы добавить тактическую изюминку к насильственной встрече.",
            "Киньте 1d12, щоб додати тактичну родзинку до насильницької зустрічі.",
        ),
        "dice": {"die": "d12", "entries": [
            {"min": 1,  "max": 1,  "text": "High Ground — One side is located high above the other and has an advantage in attacking and defending."},
            {"min": 2,  "max": 2,  "text": "Kinetic Potential — Objects in the area have the potential to deal a great amount of damage, radically changing the situation."},
            {"min": 3,  "max": 3,  "text": "Breach — The enemy is deeply entrenched in a highly defensible position which must be defeated first."},
            {"min": 4,  "max": 4,  "text": "Take & Hold — One side must capture an objective and defend it until reinforcements arrive."},
            {"min": 5,  "max": 5,  "text": "Escalation Risk — The longer the encounter takes, the more likely it is to spiral out of control."},
            {"min": 6,  "max": 6,  "text": "Ambush — If one side is surprised, the encounter will end quickly."},
            {"min": 7,  "max": 7,  "text": "Stealth Mission — Stealth and silence are required for the situation not to escalate."},
            {"min": 8,  "max": 8,  "text": "Collateral Damage — There are non-combatants in the area which must be considered and may be leveraged by enemies."},
            {"min": 9,  "max": 9,  "text": "Danger Zone — The encounter takes place in a limited area; straying from it risks damage or death."},
            {"min": 10, "max": 10, "text": "Key Objective — The encounter ends as soon as a key objective is reached, captured, or killed."},
            {"min": 11, "max": 11, "text": "Pursuit & Evade — One side is attempting to get to a location and the other party must stop them."},
            {"min": 12, "max": 12, "text": "Rules of Engagement — One side is required to be non-lethal, radically altering the weapons at the players' disposal."},
        ]},
        "dice_ru": [
            "Высокая Позиция — Одна сторона находится значительно выше другой и имеет преимущество при атаке и обороне.",
            "Кинетический Потенциал — Объекты в зоне могут нанести огромный урон, резко изменив ситуацию.",
            "Прорыв — Враг глубоко окопался на хорошо защищённой позиции, которую нужно сначала преодолеть.",
            "Захват и Удержание — Одна сторона должна захватить цель и защищать её до прихода подкрепления.",
            "Риск Эскалации — Чем дольше длится столкновение, тем вероятнее, что оно выйдет из-под контроля.",
            "Засада — Если одна сторона застигнута врасплох, столкновение закончится быстро.",
            "Скрытная Миссия — Для предотвращения эскалации требуются скрытность и тишина.",
            "Сопутствующий Ущерб — В зоне присутствуют мирные жители, которых нужно учитывать — враги могут их использовать.",
            "Опасная Зона — Столкновение происходит в ограниченной зоне; выход за её пределы грозит уроном или смертью.",
            "Ключевая Цель — Столкновение заканчивается, как только ключевая цель достигнута, захвачена или уничтожена.",
            "Погоня и Уклонение — Одна сторона стремится попасть в определённое место, другая должна её остановить.",
            "Правила Ведения Боя — Одна сторона обязана действовать нелетально, что существенно ограничивает её арсенал.",
        ],
        "dice_ua": [
            "Висока Позиція — Одна сторона знаходиться значно вище іншої і має перевагу при атаці та обороні.",
            "Кінетичний Потенціал — Об'єкти в зоні здатні завдати величезної шкоди, різко змінивши ситуацію.",
            "Прорив — Ворог глибоко закопався на добре захищеній позиції, яку потрібно спочатку подолати.",
            "Захоплення і Утримання — Одна сторона повинна захопити ціль і обороняти її до приходу підкріплення.",
            "Ризик Ескалації — Чим довше тривало зіткнення, тим імовірніше, що воно вийде з-під контролю.",
            "Засідка — Якщо одну сторону застали зненацька, зіткнення закінчиться швидко.",
            "Прихована Місія — Для запобігання ескалації необхідні скритність і тиша.",
            "Супутні Втрати — У зоні присутні мирні жителі, яких потрібно враховувати — вороги можуть їх використати.",
            "Небезпечна Зона — Зіткнення відбувається в обмеженій зоні; вихід за її межі загрожує шкодою або смертю.",
            "Ключова Ціль — Зіткнення закінчується, щойно ключова ціль досягнута, захоплена або знищена.",
            "Погоня і Ухилення — Одна сторона прагне потрапити до певного місця, інша повинна її зупинити.",
            "Правила Ведення Бою — Одна сторона зобов'язана діяти нелетально, що суттєво обмежує її арсенал.",
        ],
    },
    {
        "id": 178, "icon": "🗺️", "source_page": 18,
        "name": (
            "Map It Out",
            "Составьте Карту",
            "Складіть Карту",
        ),
        "desc": (
            "Draw a simple flowchart — not a beautiful map, just a usable one.\n\n"
            "Steps:\n"
            "1. Draw 10 numbered boxes. Each box = one location.\n"
            "2. Box 1 = players' starting location.\n"
            "3. Lines between boxes = routes (corridors, maintenance shafts, hyperspace jumps).\n"
            "4. Note the most important detail from each location on the map itself.\n"
            "5. On the opposite page, write a key: list 1–10, label each location, then bullet the most important interactive elements.\n\n"
            "Each path is a choice. Don't label routes just 'hallway' — note what makes them meaningful (guards, exposure, danger, opportunity).\n\n"
            "Put everything on the map. If it's not on the map, it won't come up in the game.\n\n"
            "When are you done? When you can run the scenario from the map without flipping through notes.",

            "Нарисуйте простую блок-схему — не красивую карту, а рабочий инструмент.\n\n"
            "Шаги:\n"
            "1. Нарисуйте 10 пронумерованных прямоугольников. Каждый = одна локация.\n"
            "2. Прямоугольник 1 = стартовая локация игроков.\n"
            "3. Линии между прямоугольниками = маршруты (коридоры, технические шахты, прыжки в гиперпространство).\n"
            "4. На самой карте отметьте самую важную деталь каждой локации.\n"
            "5. На обратной странице напишите легенду: пронумеруйте 1–10, дайте каждой локации название, затем маркером отметьте ключевые интерактивные элементы.\n\n"
            "Каждый маршрут — это выбор. Не называйте пути просто «коридор» — отметьте, что делает их значимыми (охрана, открытость, опасность, возможности).\n\n"
            "Всё должно быть на карте. Если этого нет на карте — это не появится в игре.\n\n"
            "Когда готово? Когда вы можете провести сценарий по карте, не перелистывая заметки.",

            "Намалюйте просту блок-схему — не красиву карту, а робочий інструмент.\n\n"
            "Кроки:\n"
            "1. Намалюйте 10 пронумерованих прямокутників. Кожен = одна локація.\n"
            "2. Прямокутник 1 = стартова локація гравців.\n"
            "3. Лінії між прямокутниками = маршрути (коридори, технічні шахти, стрибки в гіперпростір).\n"
            "4. На самій карті відзначте найважливішу деталь кожної локації.\n"
            "5. На зворотній сторінці напишіть легенду: пронумеруйте 1–10, дайте кожній локації назву, потім маркером відзначте ключові інтерактивні елементи.\n\n"
            "Кожен маршрут — це вибір. Не називайте шляхи просто 'коридор' — відзначте, що робить їх значущими (охорона, відкритість, небезпека, можливості).\n\n"
            "Все повинно бути на карті. Якщо цього немає на карті — цього не з'явиться в грі.\n\n"
            "Коли готово? Коли ви можете провести сценарій по карті, не гортаючи нотатки.",
        ),
        "dice": None,
    },
]


# ── Seed ──────────────────────────────────────────────────────────────────────

def _seed(conn: sqlite3.Connection) -> None:
    # ── Source ────────────────────────────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO sources (slug, title, type)
        VALUES ('wom', 'Warden''s Operations Manual', 'supplement')
    """)

    # ── Pages ─────────────────────────────────────────────────────────────────
    for pid, icon, src_page, name_en, name_ru, name_ua in PAGES:
        linked = json.dumps(
            [24, 25, 26, 27, 28] if pid == 23 else []
        )
        conn.execute("""
            INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
            VALUES (?, ?, 'wom', ?, ?)
        """, (pid, icon, src_page, linked))
        for lang, name in (("en", name_en), ("ru", name_ru), ("ua", name_ua)):
            conn.execute("""
                INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
                VALUES (?, ?, ?)
            """, (pid, lang, name))

    # ── Add P23 to P1 linked_pages ────────────────────────────────────────────
    row = conn.execute("SELECT linked_pages FROM pages WHERE id = 1").fetchone()
    current = json.loads(row[0]) if row and row[0] else []
    if 23 not in current:
        conn.execute(
            "UPDATE pages SET linked_pages = ? WHERE id = 1",
            (json.dumps(current + [23]),)
        )

    # ── P24 contents ──────────────────────────────────────────────────────────
    for i, c in enumerate(P24_CONTENTS):
        cid  = c["id"]
        dice = c.get("dice")
        conn.execute("""
            INSERT OR IGNORE INTO contents
                (id, icon, source_slug, source_page, dice, sort_order)
            VALUES (?, ?, 'wom', ?, ?, ?)
        """, (cid, c["icon"], c["source_page"], json.dumps(dice) if dice else None, cid))

        for lang in ("en", "ru", "ua"):
            name = c["name"][{"en": 0, "ru": 1, "ua": 2}[lang]]
            desc = c["desc"][{"en": 0, "ru": 1, "ua": 2}[lang]]
            dice_entries = None
            if dice and lang in ("ru", "ua"):
                key = f"dice_{lang}"
                if key in c:
                    dice_entries = json.dumps(c[key])
            conn.execute("""
                INSERT OR IGNORE INTO content_i18n
                    (content_id, lang, name, desc, dice_entries)
                VALUES (?, ?, ?, ?, ?)
            """, (cid, lang, name, desc, dice_entries))

        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (24, ?, ?)
        """, (cid, cid))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(
            "Done — source wom, pages P23-P28, "
            f"{len(P24_CONTENTS)} P24 contents seeded into '{DB_PATH}'."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
