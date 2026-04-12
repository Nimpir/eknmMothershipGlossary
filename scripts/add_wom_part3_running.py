"""
scripts/add_wom_part3_running.py
Warden's Operations Manual — Part 3: P26 Running the Game contents C183-C190.
Run: python scripts/add_wom_part3_running.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

P26_CONTENTS = [
    {
        "id": 183, "icon": "🔄", "source_page": 26,
        "name": ("How the Game Works", "Как Работает Игра", "Як Працює Гра"),
        "desc": (
            "The core loop:\n"
            "1. Warden describes the situation — honestly and evocatively. Use all five senses. "
            "Smell is particularly good for horror. Only describe the horror a little at a time.\n"
            "2. Players ask questions — encourage as many as needed. The more information they have, "
            "the better decisions they make.\n"
            "3. Players make a decision — everything follows from their choices.\n"
            "4. Warden sets the stakes — clearly tell players what failure looks like before they commit.\n"
            "5. Players commit to action.\n"
            "6. Resolve the action — if it's obvious, it just happens. If stakes are high and outcome "
            "uncertain, roll dice.\n\n"
            "Key principles:\n"
            "• Roll as little as possible.\n"
            "• Stats and Saves represent capability under extreme pressure, not personality.\n"
            "• Most rolls have a 30–40% success rate — failure is expected. Never say 'you miss,' "
            "instead describe how the situation gets worse.\n"
            "• Be impartial. Your job is to create interesting situations, not dramatic stories.",

            "Основной цикл:\n"
            "1. Судья описывает ситуацию — честно и образно. Задействуйте все пять чувств. "
            "Запах особенно хорош для ужаса. Раскрывайте Ужас постепенно.\n"
            "2. Игроки задают вопросы — поощряйте любые. Чем больше информации, тем лучше решения.\n"
            "3. Игроки принимают решение — всё следует из их выборов.\n"
            "4. Судья устанавливает ставки — чётко говорите, как выглядит провал, до подтверждения действия.\n"
            "5. Игроки подтверждают действие.\n"
            "6. Разрешение действия — если очевидно, просто происходит. При высоких ставках и "
            "неясном исходе — бросайте кубики.\n\n"
            "Ключевые принципы:\n"
            "• Бросайте кубики как можно реже.\n"
            "• Параметры и Спасброски отражают способности под сильным давлением, а не личность.\n"
            "• Большинство бросков имеют шанс успеха 30–40% — провал ожидаем. Никогда не говорите "
            "'вы промахнулись' — описывайте, как ситуация ухудшается.\n"
            "• Будьте беспристрастны. Ваша задача — создавать интересные ситуации, а не драматические истории.",

            "Основний цикл:\n"
            "1. Суддя описує ситуацію — чесно і образно. Залучайте всі п'ять чуттів. "
            "Запах особливо добрий для жаху. Розкривайте Жах поступово.\n"
            "2. Гравці ставлять питання — заохочуйте будь-які. Що більше інформації, то кращі рішення.\n"
            "3. Гравці приймають рішення — все випливає з їхніх виборів.\n"
            "4. Суддя встановлює ставки — чітко кажіть, як виглядає провал, до підтвердження дії.\n"
            "5. Гравці підтверджують дію.\n"
            "6. Вирішення дії — якщо очевидно, просто відбувається. При високих ставках і "
            "незрозумілому результаті — кидайте кубики.\n\n"
            "Ключові принципи:\n"
            "• Кидайте кубики якомога рідше.\n"
            "• Параметри та Порятунки відображають здібності під сильним тиском, а не особистість.\n"
            "• Більшість кидків мають шанс успіху 30–40% — провал очікуваний. Ніколи не кажіть "
            "'ви промахнулися' — описуйте, як ситуація погіршується.\n"
            "• Будьте неупередженими. Ваше завдання — створювати цікаві ситуації, а не драматичні історії.",
        ),
    },
    {
        "id": 184, "icon": "⚖️", "source_page": 30,
        "name": ("Setting the Stakes", "Установка Ставок", "Встановлення Ставок"),
        "desc": (
            "Before every roll, clearly tell the players what failure looks like.\n\n"
            "When to set stakes:\n"
            "• Whenever players come in conflict with people, creatures, or their environment.\n"
            "• Any time life or death hangs in the balance.\n"
            "• Skip it for low-stakes routine actions.\n\n"
            "What to communicate:\n"
            "• The likely outcome if they fail (ballpark is enough — no need to be exact).\n"
            "• Whether there are degrees of success/failure ('barely failed' can mean something).\n"
            "• That actions doomed to failure still have stakes — how badly do they fail?\n\n"
            "Why this works:\n"
            "Players can now weigh the risks, change plans, and make informed decisions. "
            "Setting stakes doesn't ruin the surprise — it creates a real gamble. "
            "It also lets players correct your logic before the dice fly.\n\n"
            "When NOT to roll dice:\n"
            "• Stakes are low.\n"
            "• The outcome is obvious.\n"
            "• They have the right tool, skill, or class.\n"
            "• They have a good plan — the reward is enacting it.",

            "Перед каждым броском чётко говорите игрокам, как выглядит провал.\n\n"
            "Когда устанавливать ставки:\n"
            "• Когда игроки вступают в конфликт с людьми, существами или средой.\n"
            "• Всякий раз, когда речь идёт о жизни и смерти.\n"
            "• Пропускайте для рутинных действий с низкими ставками.\n\n"
            "Что нужно сообщить:\n"
            "• Вероятный исход при провале (приблизительно — точность не нужна).\n"
            "• Есть ли степени успеха/провала ('едва провалился' может что-то значить).\n"
            "• Что даже обречённые на провал действия имеют ставки — насколько плохо они провалятся?\n\n"
            "Почему это работает:\n"
            "Игроки могут взвесить риски, изменить планы и принять взвешенные решения. "
            "Установка ставок не портит сюрприз — она создаёт настоящий азарт. "
            "Кроме того, игроки могут поправить вашу логику до броска.\n\n"
            "Когда НЕ бросать кубики:\n"
            "• Ставки низкие.\n"
            "• Исход очевиден.\n"
            "• У них есть нужный инструмент, навык или класс.\n"
            "• У них хороший план — наградой служит его выполнение.",

            "Перед кожним кидком чітко кажіть гравцям, як виглядає провал.\n\n"
            "Коли встановлювати ставки:\n"
            "• Коли гравці вступають у конфлікт із людьми, істотами або середовищем.\n"
            "• Щоразу, коли йдеться про життя і смерть.\n"
            "• Пропускайте для рутинних дій із низькими ставками.\n\n"
            "Що потрібно повідомити:\n"
            "• Ймовірний результат при провалі (приблизно — точність не потрібна).\n"
            "• Чи є ступені успіху/провалу ('ледь провалився' може щось означати).\n"
            "• Що навіть приречені на провал дії мають ставки — наскільки погано вони провалюються?\n\n"
            "Чому це працює:\n"
            "Гравці можуть зважити ризики, змінити плани і прийняти зважені рішення. "
            "Встановлення ставок не псує сюрприз — воно створює справжній азарт. "
            "Крім того, гравці можуть виправити вашу логіку до кидка.\n\n"
            "Коли НЕ кидати кубики:\n"
            "• Ставки низькі.\n"
            "• Результат очевидний.\n"
            "• У них є потрібний інструмент, навик або клас.\n"
            "• У них хороший план — нагородою слугує його виконання.",
        ),
    },
    {
        "id": 185, "icon": "📊", "source_page": 33,
        "name": ("Interpreting Failure", "Интерпретация Провала", "Інтерпретація Провалу"),
        "desc": (
            "A failed roll does not mean 'nothing happens.' It means the situation gets worse in some way. "
            "Every roll moves the game forward. Instead of 'you fail,' describe how the situation changes.\n\n"
            "Four ways to interpret failure:\n\n"
            "1. Action succeeds, but costs more time or resources\n"
            "• Fail a Piloting Check to outmaneuver an enemy? They pull it off, but burn extra fuel.\n"
            "• Fail to find a ship's manifest in time? They find it — 20 minutes later, now enemies are coming.\n\n"
            "2. Action succeeds, but causes harm\n"
            "• Fail a Repair Check? Hull fixed, but they injure themselves (1d10 DMG).\n"
            "• Fail a Combat Check at Close range? Player rolls damage — so does the enemy.\n\n"
            "3. Action succeeds, but leaves a tactical disadvantage\n"
            "• Fail to scavenge parts? Found after an hour — now they're lost.\n"
            "• Fail a Strength Check on a stuck airlock while being chased? Got it open, but now they're stuck.\n\n"
            "4. Action fails and the situation gets much worse\n"
            "• Fail to stop bleeding? Complication — patient takes 1d10 DMG, bleeding worsens.\n"
            "• Fail to fire at an enemy in a crowded corridor? Bullets ricochet — whole party makes a Body Save.",

            "Провальный бросок не означает «ничего не происходит». Он означает, что ситуация ухудшается. "
            "Каждый бросок двигает игру вперёд. Вместо 'вы провалились' описывайте, как изменилась ситуация.\n\n"
            "Четыре способа интерпретировать провал:\n\n"
            "1. Действие удаётся, но требует больше времени или ресурсов\n"
            "• Провал Проверки Пилотирования? Манёвр выполнен, но сожжено лишнее топливо.\n"
            "• Не успел найти манифест груза? Нашёл — через 20 минут, враги уже идут.\n\n"
            "2. Действие удаётся, но наносит вред\n"
            "• Провал Проверки Ремонта? Корпус отремонтирован, но получена травма (1d10 урона).\n"
            "• Провал Проверки Боя на Ближней дистанции? Игрок бросает урон — враг тоже.\n\n"
            "3. Действие удаётся, но создаёт тактический проигрыш\n"
            "• Провал добычи запчастей? Нашёл через час — и потерялся.\n"
            "• Провал Проверки Силы на заклинившем шлюзе во время погони? Открыл, но застрял.\n\n"
            "4. Действие проваливается, и ситуация резко ухудшается\n"
            "• Провал остановки кровотечения? Осложнение — пациент получает 1d10 урона, кровотечение усиливается.\n"
            "• Провал атаки в переполненном коридоре? Рикошет — вся группа делает Спасбросок Тела.",

            "Провальний кидок не означає «нічого не відбувається». Він означає, що ситуація погіршується. "
            "Кожен кидок рухає гру вперед. Замість 'ви провалилися' описуйте, як змінилася ситуація.\n\n"
            "Чотири способи інтерпретувати провал:\n\n"
            "1. Дія вдається, але потребує більше часу або ресурсів\n"
            "• Провал Перевірки Пілотування? Маневр виконаний, але спалено зайве паливо.\n"
            "• Не встиг знайти маніфест вантажу? Знайшов — через 20 хвилин, вороги вже йдуть.\n\n"
            "2. Дія вдається, але завдає шкоди\n"
            "• Провал Перевірки Ремонту? Корпус відремонтований, але отримана травма (1d10 шкоди).\n"
            "• Провал Перевірки Бою на Близькій дистанції? Гравець кидає шкоду — ворог теж.\n\n"
            "3. Дія вдається, але створює тактичний програш\n"
            "• Провал видобутку запчастин? Знайшов через годину — і заблукав.\n"
            "• Провал Перевірки Сили на заклиненому шлюзі під час погоні? Відкрив, але застряг.\n\n"
            "4. Дія провалюється, і ситуація різко погіршується\n"
            "• Провал зупинки кровотечі? Ускладнення — пацієнт отримує 1d10 шкоди, кровотеча посилюється.\n"
            "• Провал атаки в переповненому коридорі? Рикошет — вся група робить Порятунок Тіла.",
        ),
    },
    {
        "id": 186, "icon": "🛠️", "source_page": 52,
        "name": ("Difficulty Settings", "Настройки Сложности", "Налаштування Складності"),
        "desc": (
            "Optional house rules to tune difficulty up or down. Add any to your Campaign Notebook.\n\n"
            "Ablative Wounds — Players gain 1 extra Wound that doesn't trigger the Wound table; regained with 30 min rest.\n"
            "Armor Degradation — AP reduced by 1 whenever excess damage is dealt; armor destroyed at 0 AP.\n"
            "Critical Stress Relief — On a Critical Success, reduce Stress by 1.\n"
            "Exhaustable Skills — Auto-succeed one Skill Check per skill per session.\n"
            "Fragility — All players get 1 Wound (androids get 5).\n"
            "High Score Breaker — Beat your player High Score → gain 20 points to divide between Stats and Saves.\n"
            "Impenetrable Wounds — Damage does not carry over after receiving a Wound.\n"
            "Improved Advancement — Stats and Saves can both improve from Shore Leave.\n"
            "Lethality — Ignore Health; all weapons deal 1+ Wounds directly.\n"
            "Light Ammo Tracking — Only track ammo when narratively relevant; assume 1d5 shots remaining.\n"
            "One Time Advancement — After surviving the first session, add 10 to any 1 Stat or Save.\n"
            "Opt-In Stress — Players volunteer to take Stress and make Panic Checks when they feel it's appropriate.\n"
            "Player Facing Rolls — Players make all rolls; a miss in combat means they might be hit instead.\n"
            "Rapid Skill Learning — Trained Skill in 3 sessions, Expert in 5, Master in 10.\n"
            "Resolve — Each session survived grants 1 Resolve, spendable as a free reroll.\n"
            "Simple Skills — Ignore Skill bonuses; all Skills grant Advantage instead.",

            "Опциональные домашние правила для настройки сложности. Добавьте нужные в Кампейн Ноутбук.\n\n"
            "Абляционные Ранения — Игроки получают 1 дополнительное Ранение без броска по таблице; восстанавливается за 30 мин отдыха.\n"
            "Деградация Брони — КБ снижается на 1 при каждом избыточном уроне; броня уничтожается при 0 КБ.\n"
            "Снятие Критического Стресса — При Критическом Успехе снизить Стресс на 1.\n"
            "Исчерпаемые Навыки — Раз в сессию автоматически успешная Проверка Навыка для каждого навыка.\n"
            "Хрупкость — Все игроки получают 1 Ранение (андроиды — 5).\n"
            "Рекордсмен — Побить личный рекорд → получить 20 очков для распределения между Параметрами и Спасбросками.\n"
            "Непроницаемые Ранения — Урон не переносится после получения Ранения.\n"
            "Улучшенное Развитие — Параметры и Спасброски могут улучшаться во время Берегового Отпуска.\n"
            "Летальность — Игнорировать Здоровье; все оружия наносят 1+ Ранений напрямую.\n"
            "Упрощённый Учёт Патронов — Отслеживать только когда нарративно важно; считать 1d5 выстрелов остатком.\n"
            "Одноразовое Развитие — После выживания в первой сессии добавить 10 к любому 1 Параметру или Спасброску.\n"
            "Добровольный Стресс — Игроки сами решают, когда получать Стресс и делать Проверки Паники.\n"
            "Броски Игроков — Игроки делают все броски; промах в бою может означать, что попали по ним.\n"
            "Быстрое Обучение — Обученный Навык за 3 сессии, Экспертный за 5, Мастерский за 10.\n"
            "Решимость — Каждая пережитая сессия даёт 1 Решимость — можно потратить как бесплатный перебросок.\n"
            "Простые Навыки — Игнорировать бонусы Навыков; все Навыки дают Преимущество.",

            "Опціональні домашні правила для налаштування складності. Додайте потрібні до Кампейн Ноутбуку.\n\n"
            "Абляційні Поранення — Гравці отримують 1 додаткове Поранення без кидка по таблиці; відновлюється за 30 хв відпочинку.\n"
            "Деградація Броні — КБ знижується на 1 при кожній надлишковій шкоді; броня знищується при 0 КБ.\n"
            "Зняття Критичного Стресу — При Критичному Успіху знизити Стрес на 1.\n"
            "Вичерпні Навики — Раз на сесію автоматично успішна Перевірка Навику для кожного навику.\n"
            "Крихкість — Усі гравці отримують 1 Поранення (андроїди — 5).\n"
            "Рекордсмен — Побити особистий рекорд → отримати 20 очок для розподілу між Параметрами та Порятунками.\n"
            "Непроникні Поранення — Шкода не переноситься після отримання Поранення.\n"
            "Поліпшений Розвиток — Параметри та Порятунки можуть покращуватися під час Берегової Відпустки.\n"
            "Летальність — Ігнорувати Здоров'я; вся зброя завдає 1+ Поранень напряму.\n"
            "Спрощений Облік Патронів — Відстежувати тільки коли нараційно важливо; вважати 1d5 пострілів залишком.\n"
            "Одноразовий Розвиток — Після виживання в першій сесії додати 10 до будь-якого 1 Параметра або Порятунку.\n"
            "Добровільний Стрес — Гравці самі вирішують, коли отримувати Стрес і робити Перевірки Паніки.\n"
            "Кидки Гравців — Гравці роблять усі кидки; промах у бою може означати, що влучили по них.\n"
            "Швидке Навчання — Навчений Навик за 3 сесії, Експертний за 5, Майстерний за 10.\n"
            "Рішучість — Кожна пережита сесія дає 1 Рішучість — можна витратити як безкоштовний перекид.\n"
            "Прості Навики — Ігнорувати бонуси Навиків; усі Навики дають Перевагу.",
        ),
    },
    {
        "id": 187, "icon": "💬", "source_page": 36,
        "name": ("Social Encounters", "Социальные Встречи", "Соціальні Зустрічі"),
        "desc": (
            "Subtlety is your worst enemy. Say the quiet part loud. "
            "A cookie-cutter character with clear wants beats a mysterious one whose motivations are a mystery.\n\n"
            "Lying & Deception\n"
            "When an NPC lies to the players, just tell them — 'it seems like this person is lying.' "
            "This leads to better play as they try to prove it. When players lie to NPCs, let it work "
            "until consequences catch up. Only call for an Instinct Check if the lie is really bad.\n\n"
            "Negotiation\n"
            "• Most people would rather talk than fight.\n"
            "• A reputation for violence will follow the players.\n"
            "• Negotiation requires leverage — blackmail, solving a problem, favors.\n"
            "• In life-or-death situations, remind players that talking may buy escape time.\n"
            "• Don't kill surrendered players — take them to their captors' leader instead.\n\n"
            "There are no social rolls. Handle social encounters through roleplay. "
            "Let players talk, plan, scheme, and have access to knowledge they shouldn't.",

            "Тонкость — ваш худший враг. Говорите прямо. "
            "Шаблонный персонаж с чёткими желаниями лучше загадочного с непонятными мотивами.\n\n"
            "Ложь и Обман\n"
            "Когда персонаж лжёт игрокам, просто скажите им — 'кажется, этот человек лжёт.' "
            "Это ведёт к лучшей игре. Когда игроки врут персонажам — пусть проходит, пока последствия не настигнут. "
            "Бросайте Проверку Инстинкта только при очень плохой лжи.\n\n"
            "Переговоры\n"
            "• Большинство предпочитает разговор драке.\n"
            "• Репутация насилия будет преследовать игроков.\n"
            "• Переговоры требуют рычагов влияния — шантаж, решение проблемы, услуги.\n"
            "• В ситуации жизни и смерти напомните, что разговор может дать время сбежать.\n"
            "• Не убивайте сдавшихся — ведите их к предводителю захватчиков.\n\n"
            "Социальных бросков нет. Социальные встречи разыгрываются в ролевом отыгрыше. "
            "Позволяйте игрокам говорить, планировать, строить схемы.",

            "Тонкість — ваш найгірший ворог. Кажіть прямо. "
            "Шаблонний персонаж із чіткими бажаннями кращий за таємничого з незрозумілими мотивами.\n\n"
            "Брехня та Обман\n"
            "Коли персонаж бреше гравцям, просто скажіть їм — 'схоже, ця людина бреше.' "
            "Це веде до кращої гри. Коли гравці брешуть персонажам — нехай проходить, поки наслідки не наздоженуть. "
            "Кидайте Перевірку Інстинкту тільки при дуже поганій брехні.\n\n"
            "Переговори\n"
            "• Більшість воліє розмову бійці.\n"
            "• Репутація насилля переслідуватиме гравців.\n"
            "• Переговори потребують важелів — шантаж, вирішення проблеми, послуги.\n"
            "• У ситуації життя і смерті нагадайте, що розмова може дати час втекти.\n"
            "• Не вбивайте тих, хто здався — ведіть їх до ватажка загарбників.\n\n"
            "Соціальних кидків немає. Соціальні зустрічі розігруються в рольовому відіграванні. "
            "Дозволяйте гравцям говорити, планувати, будувати схеми.",
        ),
    },
    {
        "id": 188, "icon": "💥", "source_page": 37,
        "name": ("Violent Encounters", "Насильственные Встречи", "Насильницькі Зустрічі"),
        "desc": (
            "Think of violent encounters as disasters happening in real time to real people, "
            "not a tactical mini-game.\n\n"
            "Every monster is a boss monster.\n"
            "Treat horrors as forces to be reckoned with over a session or more. Players learn their "
            "weaknesses gradually and eventually defeat them — or don't.\n\n"
            "Never say 'You miss.'\n"
            "Whenever someone attacks, something interesting happens. Failed attacks destroy environmental "
            "obstacles, kill bystanders, or leave the attacker exposed.\n\n"
            "Every violent encounter is the worst day of someone's life.\n"
            "In real life, attempted murder is traumatic with long-term consequences. "
            "Most intelligent beings de-escalate or flee rather than fight to the death.\n\n"
            "Smart enemies are deadly.\n"
            "When an enemy takes a Wound, it changes tactics — retreats, sets traps, targets the weak.\n\n"
            "Defeat ≠ death.\n"
            "Drag players back to a lair. Lock them in a brig. Cocoon them and leave them for dead.\n\n"
            "Death — if a character might die, say so: 'If you do this and fail, you could die.' "
            "When they are going to die, ask what their final action will be. "
            "Add their name to the Roster page in your Campaign Notebook.",

            "Воспринимайте насильственные встречи как катастрофу в реальном времени с реальными людьми, "
            "а не как тактическую мини-игру.\n\n"
            "Каждый монстр — это босс.\n"
            "Воспринимайте Ужасы как силы, с которыми нужно бороться на протяжении сессии или больше. "
            "Игроки постепенно узнают их слабости и в итоге побеждают — или нет.\n\n"
            "Никогда не говорите 'Вы промахнулись.'\n"
            "Каждая атака — это что-то интересное. Промахи уничтожают укрытия, убивают свидетелей "
            "или оставляют атакующего в уязвимом положении.\n\n"
            "Каждая насильственная встреча — худший день в чьей-то жизни.\n"
            "В реальной жизни попытка убийства — это травма с долгосрочными последствиями. "
            "Большинство разумных существ скорее отступит, чем будет биться насмерть.\n\n"
            "Умные враги смертельно опасны.\n"
            "После Ранения враг меняет тактику — отступает, ставит ловушки, выбирает слабых.\n\n"
            "Поражение ≠ смерть.\n"
            "Утащите игроков в логово. Закройте в камере. Обмотайте паутиной и бросьте умирать.\n\n"
            "Смерть — если персонаж может умереть, скажите об этом: 'Если ты это сделаешь и провалишься, ты можешь умереть.' "
            "Когда персонаж умирает, спросите, каким будет его последнее действие. Занесите имя в Ростер.",

            "Сприймайте насильницькі зустрічі як катастрофу в реальному часі з реальними людьми, "
            "а не як тактичну міні-гру.\n\n"
            "Кожен монстр — це бос.\n"
            "Сприймайте Жахи як сили, з якими потрібно боротися протягом сесії або більше. "
            "Гравці поступово дізнаються їхні слабкості і врешті перемагають — або ні.\n\n"
            "Ніколи не кажіть 'Ви промахнулися.'\n"
            "Кожна атака — це щось цікаве. Промахи знищують укриття, вбивають свідків "
            "або залишають атакуючого у вразливому становищі.\n\n"
            "Кожна насильницька зустріч — найгірший день у чиємусь житті.\n"
            "У реальному житті спроба вбивства — це травма з довгостроковими наслідками. "
            "Більшість розумних істот скоріше відступить, ніж битиметься насмерть.\n\n"
            "Розумні вороги смертельно небезпечні.\n"
            "Після Поранення ворог змінює тактику — відступає, ставить пастки, вибирає слабких.\n\n"
            "Поразка ≠ смерть.\n"
            "Затягніть гравців у лігво. Замкніть у камері. Обмотайте павутиною і залиште вмирати.\n\n"
            "Смерть — якщо персонаж може померти, скажіть про це: 'Якщо ти це зробиш і провалишся, ти можеш померти.' "
            "Коли персонаж вмирає, запитайте, якою буде його остання дія. Занесіть ім'я до Ростеру.",
        ),
    },
    {
        "id": 189, "icon": "🔎", "source_page": 38,
        "name": ("Running Investigations", "Расследования", "Розслідування"),
        "desc": (
            "Treat Mothership like the ultimate game of Twenty Questions: answer everything truthfully "
            "without regard to the outcome.\n\n"
            "Never make players roll to find clues.\n"
            "If they look in the right place or 'search the room,' they find what's there. "
            "The game is about what they do with the information — not the roll.\n\n"
            "Don't hint, but do remind.\n"
            "Don't drop hints to 'help' them. The game is fun whether they solve it or not. "
            "But if they've already found a clue and forgotten it, just remind them.\n\n"
            "Use Skills.\n"
            "A Scientist and a Marine examining the same corpse should get different information. "
            "Use class, skills, and background to colour the details you reveal.\n\n"
            "Only roll when there isn't time.\n"
            "Under normal conditions, players get the information they need. Only roll when they're "
            "working against a hard deadline or without resources (lab out of power, guard approaching).\n\n"
            "Types of evidence:\n"
            "• Physical — blood, DNA, organisms, crashed vessels, ancient idols, murder weapons.\n"
            "• Documentary — corporate memos, deck plans, handwritten notes, distress signals.\n"
            "• Testimonial — anything someone says under questioning. Can be hearsay or lies.",

            "Воспринимайте Mothership как игру в «Двадцать вопросов»: отвечайте честно, "
            "не думая о результате.\n\n"
            "Никогда не заставляйте игроков бросать кубики для поиска улик.\n"
            "Если они смотрят в нужном месте или 'обыскивают комнату' — они находят то, что там есть. "
            "Игра — в том, что они делают с информацией, а не в броске.\n\n"
            "Не подсказывайте, но напоминайте.\n"
            "Не давайте подсказок 'на помощь'. Игра интересна вне зависимости от того, решат ли они загадку. "
            "Но если они уже нашли улику и забыли — просто напомните.\n\n"
            "Используйте Навыки.\n"
            "Учёный и Морпех, осматривающие один труп, должны получить разную информацию. "
            "Используйте класс, навыки и биографию для окраски деталей.\n\n"
            "Бросайте кубики только при нехватке времени.\n"
            "В нормальных условиях игроки получают нужную информацию. Бросок нужен только при жёстком "
            "дедлайне или нехватке ресурсов (нет электричества в лаборатории, приближается охрана).\n\n"
            "Типы улик:\n"
            "• Физические — кровь, ДНК, организмы, разбитые корабли, древние идолы, орудия убийства.\n"
            "• Документальные — корпоративные меморандумы, планы палуб, рукописные заметки, сигналы бедствия.\n"
            "• Свидетельские — всё, что кто-то говорит на допросе. Могут быть слухами или ложью.",

            "Сприймайте Mothership як гру в 'Двадцять питань': відповідайте чесно, "
            "не думаючи про результат.\n\n"
            "Ніколи не змушуйте гравців кидати кубики для пошуку підказок.\n"
            "Якщо вони дивляться в потрібному місці або 'обшукують кімнату' — вони знаходять те, що там є. "
            "Гра — у тому, що вони роблять з інформацією, а не в кидку.\n\n"
            "Не підказуйте, але нагадуйте.\n"
            "Не давайте підказок 'на допомогу'. Гра цікава незалежно від того, чи розгадають вони таємницю. "
            "Але якщо вони вже знайшли підказку і забули — просто нагадайте.\n\n"
            "Використовуйте Навики.\n"
            "Вчений і Морський піхотинець, що оглядають один труп, повинні отримати різну інформацію. "
            "Використовуйте клас, навики і біографію для забарвлення деталей.\n\n"
            "Кидайте кубики тільки при браку часу.\n"
            "У нормальних умовах гравці отримують потрібну інформацію. Кидок потрібен тільки при жорсткому "
            "дедлайні або браку ресурсів (немає електрики в лабораторії, наближається охорона).\n\n"
            "Типи доказів:\n"
            "• Фізичні — кров, ДНК, організми, розбиті кораблі, давні ідоли, знаряддя вбивства.\n"
            "• Документальні — корпоративні меморандуми, плани палуб, рукописні нотатки, сигнали лиха.\n"
            "• Свідчення — все, що хтось каже на допиті. Можуть бути чутками або брехнею.",
        ),
    },
    {
        "id": 190, "icon": "🚀", "source_page": 39,
        "name": ("Ship-to-Ship Combat", "Бой Корабль-Корабль", "Бій Корабель-Корабель"),
        "desc": (
            "Ship combat is one of the most horrifying things in space. Treat it as a natural disaster, "
            "not a tactical encounter.\n\n"
            "Key principles:\n"
            "• It's a natural disaster — treat any ship damage as an environmental hazard spiralling out of control.\n"
            "• Players make decisions; the Computer handles targeting, aiming, and firing.\n"
            "• It's a last resort — ships are astronomical investments. Factions would rather lose a crew "
            "than pay for a new ship.\n"
            "• It's a social encounter — what does the enemy want? Use hailing frequently.\n\n"
            "Ship combat is a scenario, not an encounter.\n"
            "The ideal scenario: a creature loose on the players' ship, a patrol craft attacking for being "
            "in restricted space, life support down, a toxic atmosphere, and marines boarding — "
            "just as the thing in the vents finally attacks.\n\n"
            "Pace with Ship Turns.\n"
            "Call a Ship Turn after a few rounds of player action. No ship combat should last more than "
            "2–3 rounds at the absolute maximum. Most should end after one.\n\n"
            "Ship economics:\n"
            "• Players work on a ship — best for short campaigns.\n"
            "• Players don't have a ship — travel becomes another problem to solve.\n"
            "• Players are owner-operators — give them a beat-up raider with Profit Save 2d10+20 "
            "and roll annually for financial health.",

            "Бой корабль-корабль — одна из самых страшных вещей в космосе. "
            "Воспринимайте его как стихийное бедствие, а не тактическую встречу.\n\n"
            "Ключевые принципы:\n"
            "• Это стихийное бедствие — любой ущерб кораблю превращается в неуправляемую экологическую угрозу.\n"
            "• Игроки принимают решения; Компьютер управляет наведением и стрельбой.\n"
            "• Это крайняя мера — корабли стоят астрономических денег. Фракции предпочтут потерять команду.\n"
            "• Это социальная встреча — чего хочет враг? Чаще используйте связь.\n\n"
            "Бой — это сценарий, а не встреча.\n"
            "Идеальный сценарий: существо на борту корабля игроков, патрульный корабль атакует за нарушение "
            "запретной зоны, система жизнеобеспечения отключена, токсичная атмосфера и десант — "
            "как раз когда тварь из вентиляции наконец атакует.\n\n"
            "Темп через Ходы Корабля.\n"
            "Объявляйте Ход Корабля после нескольких раундов действий игроков. "
            "Никакой бой не должен длиться более 2–3 раундов. Большинство заканчивается после одного.\n\n"
            "Экономика кораблей:\n"
            "• Игроки работают на корабле — лучший вариант для коротких кампаний.\n"
            "• У игроков нет корабля — путешествия становятся ещё одной проблемой.\n"
            "• Игроки — владельцы-операторы — дайте им потрёпанный рейдер с Спасброском Прибыли 2d10+20.",

            "Бій корабель-корабель — одна з найстрашніших речей у космосі. "
            "Сприймайте його як стихійне лихо, а не тактичну зустріч.\n\n"
            "Ключові принципи:\n"
            "• Це стихійне лихо — будь-яка шкода кораблю перетворюється на некеровану екологічну загрозу.\n"
            "• Гравці приймають рішення; Комп'ютер керує прицілюванням і стріляниною.\n"
            "• Це крайній захід — кораблі коштують астрономічних грошей. Фракції воліють втратити команду.\n"
            "• Це соціальна зустріч — чого хоче ворог? Частіше використовуйте зв'язок.\n\n"
            "Бій — це сценарій, а не зустріч.\n"
            "Ідеальний сценарій: істота на борту корабля гравців, патрульний корабель атакує за порушення "
            "забороненої зони, система життєзабезпечення відключена, токсична атмосфера і десант — "
            "саме коли тварина з вентиляції нарешті атакує.\n\n"
            "Темп через Ходи Корабля.\n"
            "Оголошуйте Хід Корабля після кількох раундів дій гравців. "
            "Жоден бій не повинен тривати більше 2–3 раундів. Більшість закінчується після одного.\n\n"
            "Економіка кораблів:\n"
            "• Гравці працюють на кораблі — найкращий варіант для коротких кампаній.\n"
            "• У гравців немає корабля — подорожі стають ще однією проблемою.\n"
            "• Гравці — власники-оператори — дайте їм потрепаний рейдер із Порятунком Прибутку 2d10+20.",
        ),
    },
]


def _seed(conn: sqlite3.Connection) -> None:
    for c in P26_CONTENTS:
        cid = c["id"]
        conn.execute("""
            INSERT OR IGNORE INTO contents
                (id, icon, source_slug, source_page, dice, sort_order)
            VALUES (?, ?, 'wom', ?, NULL, ?)
        """, (cid, c["icon"], c["source_page"], cid))

        for lang in ("en", "ru", "ua"):
            idx  = {"en": 0, "ru": 1, "ua": 2}[lang]
            name = c["name"][idx]
            desc = c["desc"][idx]
            conn.execute("""
                INSERT OR IGNORE INTO content_i18n
                    (content_id, lang, name, desc)
                VALUES (?, ?, ?, ?)
            """, (cid, lang, name, desc))

        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (26, ?, ?)
        """, (cid, cid))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(P26_CONTENTS)} P26 Running the Game contents seeded into '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
