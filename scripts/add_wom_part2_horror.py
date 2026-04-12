"""
scripts/add_wom_part2_horror.py
Warden's Operations Manual — Part 2: P25 The Horror contents C179-C182.
Run: python scripts/add_wom_part2_horror.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── C179 Random Horrors (d100, 5-column TOMBS table) ─────────────────────────
_HORRORS_EN = [
    (0,  4,  "T: Making first contact | O: Dead animals | M: Alien creature | B: Righting a wrong | S: Returns in 100 years"),
    (5,  9,  "T: Studying arcane text | O: Visions of future victims | M: Deranged killer | B: Human sacrifice | S: Recurring hallucinations"),
    (10, 14, "T: Boarding a ship | O: Writing on the wall | M: Elder evil returned | B: Vaccine | S: Victims forever scarred"),
    (15, 19, "T: Opening a grave | O: Stigmata | M: Cult | B: Only harmed by fire | S: Slumbers until next Jump"),
    (20, 24, "T: Mining strange ore | O: Unexplained suicides | M: Tainted technology | B: Nuking from orbit | S: Retreats into hiding"),
    (25, 29, "T: Trespassing | O: Distress signal | M: Colossal space being | B: Obscure occult ritual | S: Feigns death, escapes"),
    (30, 34, "T: Gross negligence | O: Stranger appears | M: Ruthless apex predator | B: Returning it to its home | S: Awaits next Transgression"),
    (35, 39, "T: Tampering with biology | O: Abnormal birth | M: Ghost or spirit | B: Tough, but killable | S: Recurring nightmares"),
    (40, 44, "T: Reneging on a deal | O: Unlucky numbers | M: Tangled mass of flesh | B: Giving it what it wants | S: Possesses closest victim"),
    (45, 49, "T: Disturbing holy site | O: Ancient distress beacon | M: Mutated being | B: Special weapon | S: Awakens if Transgression is repeated"),
    (50, 54, "T: Leaving someone behind | O: Android having visions | M: Child | B: Making a pact with it | S: Hibernates deep underground"),
    (55, 59, "T: Study of strange relic | O: Ancient recorded warning | M: Biological experiment | B: Serving it | S: Whispers from the shadows"),
    (60, 64, "T: Forgotten atrocity | O: Researcher's incoherent notes | M: Sentient environment | B: Learning its true identity | S: Evolves into its more powerful form"),
    (65, 69, "T: Interfacing with forbidden technology | O: Irrational computer behavior | M: Gateway or portal | B: Certain kinds of light | S: Hidden in the background of screens"),
    (70, 74, "T: Landing on uncharted planet | O: Significant astrological alignment | M: Dream | B: It can't be killed, only avoided | S: Slumbers in its killer's mind"),
    (75, 79, "T: Altering its natural habitat | O: Speaking in tongues | M: Cybernetic organism | B: Interment in rightful resting place | S: Herald of a greater Horror to come"),
    (80, 84, "T: Breaking a cultural taboo | O: Mysterious disappearances | M: Haunted location | B: Closing the portal/gate | S: Uploads into nearest computer"),
    (85, 89, "T: Failing to stop a previous Transgression | O: Strange weather phenomena | M: Doppelganger | B: Requires a certain time/location | S: Never stay in one place — it will find you"),
    (90, 94, "T: Ingesting an unknown substance | O: Ancient calendar foretells arrival | M: Invisible being | B: Sending it to another dimension | S: Parental entity comes looking for answers"),
    (95, 99, "T: Allowing harm to come to an innocent | O: Gruesomely displayed corpse(s) | M: Mothership | B: Trapping it inside a powerful container | S: Apocalyptic events set in motion"),
]

_HORRORS_RU = [
    "П: Первый контакт | З: Мёртвые животные | П: Инопланетное существо | И: Исправить ошибку | Д: Возвращается через 100 лет",
    "П: Изучение тайного текста | З: Видения будущих жертв | П: Безумный убийца | И: Человеческая жертва | Д: Повторяющиеся галлюцинации",
    "П: Посадка на корабль | З: Надписи на стенах | П: Вернувшееся древнее зло | И: Вакцина | Д: Жертвы навсегда искалечены",
    "П: Вскрытие могилы | З: Стигматы | П: Культ | И: Уязвим только к огню | Д: Спит до следующего прыжка",
    "П: Добыча странной руды | З: Необъяснимые самоубийства | П: Заражённые технологии | И: Ядерный удар с орбиты | Д: Отступает в укрытие",
    "П: Вторжение на чужую территорию | З: Сигнал бедствия | П: Колоссальное космическое существо | И: Тайный оккультный ритуал | Д: Притворяется мёртвым, бежит",
    "П: Грубая халатность | З: Появляется незнакомец | П: Безжалостный хищник | И: Вернуть его домой | Д: Ждёт следующего Проступка",
    "П: Вмешательство в биологию | З: Уродливые роды | П: Призрак или дух | И: Крепкий, но смертный | Д: Повторяющиеся кошмары",
    "П: Нарушение договора | З: Несчастливые числа | П: Клубок переплетённой плоти | И: Дать ему то, чего оно хочет | Д: Вселяется в ближайшую жертву",
    "П: Осквернение священного места | З: Древний маяк бедствия | П: Мутировавшее существо | И: Особое оружие | Д: Пробуждается при повторении Проступка",
    "П: Оставить кого-то позади | З: Видения у андроида | П: Ребёнок | И: Заключить с ним пакт | Д: Спит глубоко под землёй",
    "П: Изучение странной реликвии | З: Древнее записанное предупреждение | П: Биологический эксперимент | И: Служить ему | Д: Шёпот из теней",
    "П: Забытое злодеяние | З: Бессвязные записки исследователя | П: Разумная среда | И: Раскрыть его истинную сущность | Д: Эволюционирует в более мощную форму",
    "П: Контакт с запрещёнными технологиями | З: Иррациональное поведение компьютера | П: Врата или портал | И: Определённые виды света | Д: Скрыто на фоне экранов",
    "П: Посадка на неизведанную планету | З: Знаковое астрологическое совпадение | П: Сон | И: Его нельзя убить, только избежать | Д: Спит в разуме своего убийцы",
    "П: Изменение природной среды обитания | З: Говорение на языках | П: Кибернетический организм | И: Захоронение на законном месте | Д: Предвестник более грозного Ужаса",
    "П: Нарушение культурного табу | З: Таинственные исчезновения | П: Проклятое место | И: Закрыть портал/врата | Д: Загружается в ближайший компьютер",
    "П: Неудача в остановке прошлого Проступка | З: Странные погодные явления | П: Двойник | И: Требует определённого времени/места | Д: Не задерживайся нигде — оно найдёт тебя",
    "П: Поглощение неизвестного вещества | З: Древний календарь предвещает приход | П: Невидимое существо | И: Отправить в другое измерение | Д: Сущность-родитель ищет ответы",
    "П: Допущение вреда невинному | З: Жутко выставленные на показ трупы | П: Материнский Корабль | И: Запереть в мощном контейнере | Д: Апокалиптические события запущены",
]

_HORRORS_UA = [
    "П: Перший контакт | З: Мертві тварини | П: Інопланетна істота | В: Виправити помилку | С: Повертається через 100 років",
    "П: Вивчення таємного тексту | З: Видіння майбутніх жертв | П: Божевільний вбивця | В: Людська жертва | С: Повторювані галюцинації",
    "П: Посадка на корабель | З: Написи на стінах | П: Давнє зло повернулось | В: Вакцина | С: Жертви назавжди скалічені",
    "П: Розкриття могили | З: Стигмати | П: Культ | В: Вразливий лише до вогню | С: Спить до наступного стрибка",
    "П: Видобуток дивної руди | З: Незрозумілі самогубства | П: Заражені технології | В: Ядерний удар з орбіти | С: Відступає в укриття",
    "П: Вторгнення на чужу територію | З: Сигнал лиха | П: Колосальна космічна істота | В: Таємний окультний ритуал | С: Вдає, що мертва, тікає",
    "П: Груба халатність | З: З'являється незнайомець | П: Безжальний хижак | В: Повернути його додому | С: Чекає на наступний Проступок",
    "П: Втручання в біологію | З: Потворні пологи | П: Привид або дух | В: Міцний, але смертний | С: Повторювані кошмари",
    "П: Порушення договору | З: Нещасливі числа | П: Клубок переплетеної плоті | В: Дати йому те, чого воно хоче | С: Вселяється в найближчу жертву",
    "П: Осквернення святого місця | З: Давній маяк лиха | П: Мутована істота | В: Особлива зброя | С: Прокидається при повторенні Проступку",
    "П: Залишити когось позаду | З: Видіння в андроїда | П: Дитина | В: Укласти з ним пакт | С: Спить глибоко під землею",
    "П: Вивчення дивної реліквії | З: Давнє записане попередження | П: Біологічний експеримент | В: Служити йому | С: Шепіт із тіней",
    "П: Забуте злодіяння | З: Безладні нотатки дослідника | П: Розумне середовище | В: Розкрити його справжню сутність | С: Еволюціонує у більш потужну форму",
    "П: Контакт із забороненими технологіями | З: Ірраціональна поведінка комп'ютера | П: Ворота або портал | В: Певні види світла | С: Прихований на фоні екранів",
    "П: Посадка на невідому планету | З: Знакове астрологічне збіг | П: Сон | В: Його не можна вбити, лише уникнути | С: Спить у розумі свого вбивці",
    "П: Зміна природного середовища існування | З: Говоріння мовами | П: Кібернетичний організм | В: Поховання на законному місці | С: Провісник більш грізного Жаху",
    "П: Порушення культурного табу | З: Таємничі зникнення | П: Проклятe місце | В: Закрити портал/ворота | С: Завантажується в найближчий комп'ютер",
    "П: Невдача у зупинці минулого Проступку | З: Дивні погодні явища | П: Двійник | В: Потребує певного часу/місця | С: Не затримуйся ніде — воно знайде тебе",
    "П: Поглинання невідомої речовини | З: Давній календар провіщає прихід | П: Невидима істота | В: Відіслати в інший вимір | С: Батьківська сутність шукає відповіді",
    "П: Допущення шкоди невинному | З: Жахливо виставлені напоказ трупи | П: Материнський Корабель | В: Замкнути у потужному контейнері | С: Апокаліптичні події запущені",
]

# ── C180 Horror Themes (d100) ─────────────────────────────────────────────────
_THEMES_EN = [
    (0,  3,  "Death, ancient, arise"),
    (4,  9,  "Underwater, sunken, drowning"),
    (10, 12, "Politics, government, nationalism"),
    (13, 16, "Humanity, love, memory"),
    (17, 19, "Resistance, struggle, suffering"),
    (20, 22, "Travel, road-weariness, rural"),
    (23, 25, "Darkness, absence, void"),
    (26, 29, "Medicine, hospitals, surgery"),
    (30, 32, "Rust, the Machine, noise"),
    (33, 35, "Transformation, rebirth"),
    (36, 38, "Childhood, innocence, time"),
    (39, 41, "Underground, crime, buried"),
    (42, 43, "Fading beauty, age, fame"),
    (44, 46, "Technology, excess, decay"),
    (47, 49, "Abduction, identity, silence"),
    (50, 52, "The City, rain, flood"),
    (53, 55, "Fear, the afterlife, prophecy"),
    (56, 58, "Factories, work, oppression"),
    (59, 61, "Belief, god, hell"),
    (62, 64, "Cold, sleep, snow"),
    (65, 67, "Fire, ashes, war"),
    (68, 71, "Hunger, famine, food"),
    (72, 74, "Pleasure, touch, passion"),
    (75, 77, "Artifice, dolls, toys"),
    (78, 81, "Meat, slaughter, animal"),
    (82, 84, "Truth, solitude, loneliness"),
    (85, 87, "Wilderness, nature, growth"),
    (88, 91, "Capitalism, greed, fortune"),
    (92, 94, "Chaos, change, laughter"),
    (95, 99, "Abandoned, empty, forgotten"),
]

_THEMES_RU = [
    "Смерть, древность, воскрешение",
    "Вода, затопленное, утопление",
    "Политика, правительство, национализм",
    "Человечность, любовь, память",
    "Сопротивление, борьба, страдание",
    "Путешествие, усталость дороги, сельское",
    "Тьма, отсутствие, пустота",
    "Медицина, больницы, хирургия",
    "Ржавчина, Машина, шум",
    "Трансформация, перерождение",
    "Детство, невинность, время",
    "Подземелье, преступность, погребённое",
    "Угасающая красота, возраст, слава",
    "Технологии, излишества, разложение",
    "Похищение, идентичность, тишина",
    "Город, дождь, наводнение",
    "Страх, загробная жизнь, пророчество",
    "Фабрики, труд, угнетение",
    "Вера, бог, ад",
    "Холод, сон, снег",
    "Огонь, пепел, война",
    "Голод, голодомор, еда",
    "Удовольствие, прикосновение, страсть",
    "Искусственное, куклы, игрушки",
    "Мясо, бойня, животное",
    "Правда, уединение, одиночество",
    "Дикая природа, природа, рост",
    "Капитализм, жадность, состояние",
    "Хаос, перемены, смех",
    "Покинутое, пустое, забытое",
]

_THEMES_UA = [
    "Смерть, давнина, воскресіння",
    "Вода, затоплене, потоплення",
    "Політика, уряд, націоналізм",
    "Людяність, любов, пам'ять",
    "Опір, боротьба, страждання",
    "Мандрівка, втома дороги, сільське",
    "Темрява, відсутність, порожнеча",
    "Медицина, лікарні, хірургія",
    "Іржа, Машина, шум",
    "Трансформація, переродження",
    "Дитинство, невинність, час",
    "Підземелля, злочинність, поховане",
    "Краса, що згасає, вік, слава",
    "Технології, надмірність, розкладання",
    "Викрадення, ідентичність, тиша",
    "Місто, дощ, повінь",
    "Страх, загробне життя, пророцтво",
    "Фабрики, праця, гноблення",
    "Віра, бог, пекло",
    "Холод, сон, сніг",
    "Вогонь, попіл, війна",
    "Голод, голодомор, їжа",
    "Задоволення, дотик, пристрасть",
    "Штучне, ляльки, іграшки",
    "М'ясо, бійня, тварина",
    "Правда, усамітнення, самотність",
    "Дика природа, природа, зростання",
    "Капіталізм, жадібність, статок",
    "Хаос, зміни, сміх",
    "Покинуте, порожнє, забуте",
]

# ── C182 Puzzle Components (d100) ─────────────────────────────────────────────
_PUZZLES_EN = [
    (0,  4,  "Alarm — If solved incorrectly, sets off an alarm alerting nearby enemies."),
    (5,  9,  "Connect the Dots — Connect a series of dots using some kind of item (e.g. wires, light, water, blood)."),
    (10, 13, "Construction — Construct an item using pieces that must be found or provided."),
    (14, 17, "Dilemma — Choose between the lesser of two evils or the greater of two goods."),
    (18, 21, "Egg Carry — Safely deliver a delicate or vulnerable item/organism to a certain location."),
    (22, 25, "Find the Clue — Search for one or more objects leading to more Questions, Puzzles, or Answers."),
    (26, 29, "Guardian — Defeat, appease, or bypass a guardian who denies access to a location or item."),
    (30, 34, "Hazardous Path — Route blocked by danger which must be avoided, circumnavigated, or defeated."),
    (35, 38, "Illusion — Contains an element that appears to be one thing but is actually another."),
    (39, 42, "Labyrinth — Forces players to navigate a maze or complicated path."),
    (43, 47, "Lock & Key — Collect an item (the key) and use it on the lock to gain access."),
    (48, 51, "Missing Part — Locate a missing item for the puzzle to work properly."),
    (52, 56, "Mundane Obstacle — A real-world problem (broken elevator, collapsed pylon, etc.)."),
    (57, 60, "Outside-the-Box — No obvious solution; players must bring outside resources to bear."),
    (61, 64, "Pattern Recognition — Requires noticing repeated symbols or other repeated information."),
    (65, 69, "Remote Switch — Activate a switch in another location to bypass the current obstacle."),
    (70, 73, "Riddle — Requires recitation of a coded phrase or password."),
    (74, 78, "Rising Tide — Danger that escalates naturally, forcing a quick solution or harm."),
    (79, 82, "Sacrifice — Requires players to sacrifice something of great value."),
    (83, 86, "Sequence — Complete a certain number of steps in a specific order."),
    (87, 90, "Teamwork — Multiple players must do something simultaneously."),
    (91, 93, "Timelock — Solve in a certain amount of time or fail (or restart the attempt)."),
    (94, 96, "Trap — The puzzle punishes players for failed attempts."),
    (97, 99, "Trial and Error — Players must experiment with several ingredients to solve the puzzle."),
]

_PUZZLES_RU = [
    "Тревога — Неверное решение поднимает тревогу, оповещая ближайших врагов.",
    "Соединить точки — Соединить серию «точек» с помощью предмета (проводов, света, воды, крови).",
    "Конструкция — Собрать предмет из деталей, которые нужно найти или предоставить.",
    "Дилемма — Выбор между меньшим из двух зол или большим из двух благ.",
    "Перенос яйца — Безопасно доставить хрупкий или уязвимый предмет/организм в нужное место.",
    "Найти улику — Поиск предметов, ведущих к новым Вопросам, Головоломкам или Ответам.",
    "Страж — Победить, умиротворить или обойти стража, преграждающего путь.",
    "Опасный маршрут — Путь заблокирован опасностью, которую нужно обойти или преодолеть.",
    "Иллюзия — Содержит элемент, который выглядит иначе, чем есть на самом деле.",
    "Лабиринт — Игроки должны пройти сложный лабиринт или запутанный путь.",
    "Замок и ключ — Найти предмет (ключ) и использовать его, чтобы получить доступ к содержимому замка.",
    "Недостающая часть — Найти недостающий предмет, чтобы головоломка заработала.",
    "Обычное препятствие — Реальная проблема (сломанный лифт, упавшая опора и т.п.).",
    "Нестандартное мышление — Нет очевидного решения; нужно задействовать внешние ресурсы.",
    "Распознавание паттерна — Нужно заметить повторяющиеся символы или другую повторяющуюся информацию.",
    "Дистанционный переключатель — Активировать переключатель в другом месте для обхода текущего препятствия.",
    "Загадка — Нужно произнести закодированную фразу или пароль.",
    "Нарастающая угроза — Опасность нарастает сама по себе, вынуждая действовать быстро.",
    "Жертва — Игроки должны пожертвовать чем-то ценным.",
    "Последовательность — Выполнить определённое количество шагов в заданном порядке.",
    "Командная работа — Несколько игроков должны одновременно выполнить определённое действие.",
    "Таймлок — Решить за отведённое время или провалиться (перезапустить попытку).",
    "Ловушка — Головоломка наказывает игроков за неудачные попытки.",
    "Метод проб и ошибок — Игроки должны экспериментировать с несколькими элементами для решения.",
]

_PUZZLES_UA = [
    "Тривога — Невірне рішення піднімає тривогу, сповіщаючи найближчих ворогів.",
    "З'єднати точки — З'єднати серію «точок» за допомогою предмета (дроти, світло, вода, кров).",
    "Конструкція — Зібрати предмет з деталей, які потрібно знайти або надати.",
    "Дилема — Вибір між меншим із двох зол або більшим із двох благ.",
    "Перенесення яйця — Безпечно доставити крихкий або вразливий предмет/організм у потрібне місце.",
    "Знайти підказку — Пошук предметів, що ведуть до нових Питань, Головоломок або Відповідей.",
    "Вартовий — Перемогти, заспокоїти або обійти вартового, що перегороджує шлях.",
    "Небезпечний маршрут — Шлях заблокований небезпекою, яку потрібно обійти або подолати.",
    "Ілюзія — Містить елемент, що виглядає інакше, ніж є насправді.",
    "Лабіринт — Гравці повинні пройти складний лабіринт або заплутаний шлях.",
    "Замок і ключ — Знайти предмет (ключ) і використати його, щоб отримати доступ до вмісту замка.",
    "Відсутня частина — Знайти відсутній предмет, щоб головоломка запрацювала.",
    "Звичайна перешкода — Реальна проблема (зламаний ліфт, впала опора тощо).",
    "Нестандартне мислення — Немає очевидного рішення; потрібно залучити зовнішні ресурси.",
    "Розпізнавання паттерну — Потрібно помітити повторювані символи або іншу повторювану інформацію.",
    "Дистанційний перемикач — Активувати перемикач в іншому місці для обходу поточної перешкоди.",
    "Загадка — Потрібно вимовити закодовану фразу або пароль.",
    "Наростаюча загроза — Небезпека наростає сама по собі, змушуючи діяти швидко.",
    "Жертва — Гравці повинні пожертвувати чимось цінним.",
    "Послідовність — Виконати певну кількість кроків у заданому порядку.",
    "Командна робота — Кілька гравців повинні одночасно виконати певну дію.",
    "Таймлок — Вирішити за відведений час або провалитись (перезапустити спробу).",
    "Пастка — Головоломка карає гравців за невдалі спроби.",
    "Метод спроб і помилок — Гравці повинні експериментувати з кількома елементами для вирішення.",
]

# ── Content definitions ───────────────────────────────────────────────────────
P25_CONTENTS = [
    {
        "id": 179, "icon": "😱", "source_page": 2,
        "name": ("Random Horrors", "Случайные Ужасы", "Випадкові Жахи"),
        "desc": (
            "Roll d100 for each column or roll once and read across:\n"
            "T = Transgression (what awakens it)\n"
            "O = Omens (signs of its arrival)\n"
            "M = Manifestation (its form)\n"
            "B = Banishment (how to defeat it)\n"
            "S = Slumber (what it does if not defeated)",
            "Бросьте d100 для каждого столбца или один раз и читайте по строке:\n"
            "П = Проступок (что его пробуждает)\n"
            "З = Знамения (признаки прихода)\n"
            "П = Проявление (его форма)\n"
            "И = Изгнание (как победить)\n"
            "Д = Дремота (что происходит, если не победить)",
            "Киньте d100 для кожного стовпця або один раз і читайте по рядку:\n"
            "П = Проступок (що його пробуджує)\n"
            "З = Знамення (ознаки приходу)\n"
            "П = Прояв (його форма)\n"
            "В = Вигнання (як перемогти)\n"
            "С = Сон (що відбувається, якщо не перемогти)",
        ),
        "dice": {"die": "d100", "entries": [
            {"min": lo, "max": hi, "text": txt} for lo, hi, txt in _HORRORS_EN
        ]},
        "dice_ru": _HORRORS_RU,
        "dice_ua": _HORRORS_UA,
    },
    {
        "id": 180, "icon": "🌑", "source_page": 2,
        "name": ("Horror Themes", "Темы Ужаса", "Теми Жаху"),
        "desc": (
            "Roll d100 for a thematic direction. Use it to name characters, places, and add evocative descriptions.",
            "Бросьте d100 для тематического направления. Используйте для имён персонажей, мест и красочных описаний.",
            "Киньте d100 для тематичного напрямку. Використовуйте для імен персонажів, місць і виразних описів.",
        ),
        "dice": {"die": "d100", "entries": [
            {"min": lo, "max": hi, "text": txt} for lo, hi, txt in _THEMES_EN
        ]},
        "dice_ru": _THEMES_RU,
        "dice_ua": _THEMES_UA,
    },
    {
        "id": 181, "icon": "📖", "source_page": 8,
        "name": ("The TOMBS Cycle", "Цикл TOMBS", "Цикл TOMBS"),
        "desc": (
            "The TOMBS Cycle describes how a Horror originates, arrives, and is (temporarily) defeated.\n\n"
            "Act I — Transgression\n"
            "Someone knowingly or unknowingly awakens the Horror. A line is crossed — a moral boundary, "
            "a forbidden place, a past atrocity. Players usually only realise they have Transgressed when "
            "it is too late.\n\n"
            "Act II — Omens\n"
            "The Horror heralds its arrival through signs: nightmares, a trail of victims, strange rumors. "
            "Omens build tension and act as clues. Once solved (or time runs out) the Horror appears.\n\n"
            "Act III — Manifestation\n"
            "The Horror reveals its true form. This is the big moment. Think about its smells, sounds, and "
            "tactics. A Manifestation is a symptom — once it appears, the players are on the defensive.\n\n"
            "Act IV — Banishment\n"
            "Players race to fight back. The Horror must be dealt with or all hell breaks loose. Banishment "
            "can mean killing it, appeasing it, or freeing it from torment. Things ramp up fast.\n\n"
            "Act V — Slumber\n"
            "The Horror relents… for now. If players succeed it goes dormant, awaiting the next "
            "Transgression. If they fail it completes its plan and evolves. It is never permanently defeated — "
            "just kept at bay for another day.",

            "Цикл TOMBS описывает, как Ужас возникает, приходит и (временно) побеждается.\n\n"
            "Акт I — Проступок\n"
            "Кто-то сознательно или нет пробуждает Ужас. Переходится черта — моральная граница, "
            "запретное место, прошлое злодеяние. Игроки осознают Проступок, как правило, слишком поздно.\n\n"
            "Акт II — Знамения\n"
            "Ужас предвещает своё прибытие: кошмары, след жертв, странные слухи. Знамения нагнетают "
            "напряжение и служат уликами. Как только они разгаданы (или время истекает), Ужас появляется.\n\n"
            "Акт III — Проявление\n"
            "Ужас раскрывает свою истинную форму. Это ключевой момент. Подумайте о его запахах, звуках "
            "и тактике. Проявление — это симптом: когда он появляется, игроки переходят в оборону.\n\n"
            "Акт IV — Изгнание\n"
            "Игроки спешат дать отпор. С Ужасом нужно справиться, иначе всё рухнет. Изгнание может "
            "означать убийство, умиротворение или освобождение от страданий. Темп нарастает стремительно.\n\n"
            "Акт V — Дремота\n"
            "Ужас затихает… на время. При победе игроков он дремлет в ожидании следующего Проступка. "
            "При поражении — завершает план и эволюционирует. Его невозможно победить навсегда — "
            "лишь сдержать ещё на один день.",

            "Цикл TOMBS описує, як Жах виникає, приходить і (тимчасово) перемагається.\n\n"
            "Акт I — Проступок\n"
            "Хтось свідомо або ні пробуджує Жах. Перетинається межа — моральна границя, "
            "заборонене місце, минуле злодіяння. Гравці усвідомлюють Проступок, як правило, надто пізно.\n\n"
            "Акт II — Знамення\n"
            "Жах провіщає своє прибуття: кошмари, слід жертв, дивні чутки. Знамення нагнітають "
            "напругу і слугують підказками. Як тільки вони розгадані (або час вичерпаний), Жах з'являється.\n\n"
            "Акт III — Прояв\n"
            "Жах розкриває свою справжню форму. Це ключовий момент. Подумайте про його запахи, звуки "
            "і тактику. Прояв — це симптом: коли він з'являється, гравці переходять в оборону.\n\n"
            "Акт IV — Вигнання\n"
            "Гравці поспішають дати відсіч. З Жахом потрібно впоратись, інакше все рухне. Вигнання може "
            "означати вбивство, умиротворення або звільнення від страждань. Темп наростає стрімко.\n\n"
            "Акт V — Сон\n"
            "Жах затихає… на час. При перемозі гравців він дрімає в очікуванні наступного Проступку. "
            "При поразці — завершує план і еволюціонує. Його неможливо перемогти назавжди — "
            "лише стримати ще на один день.",
        ),
        "dice": None,
    },
    {
        "id": 182, "icon": "🧩", "source_page": 13,
        "name": ("Puzzle Components", "Компоненты Головоломок", "Компоненти Головоломок"),
        "desc": (
            "Roll d100 for a puzzle type. Use 1–2 components per puzzle — more = too complicated. "
            "Every puzzle should allow multiple solutions and leave open the possibility of failure.",
            "Бросьте d100 для типа головоломки. Используйте 1–2 компонента — больше = слишком сложно. "
            "Каждая головоломка должна допускать несколько решений и возможность провала.",
            "Киньте d100 для типу головоломки. Використовуйте 1–2 компоненти — більше = занадто складно. "
            "Кожна головоломка повинна допускати кілька рішень і можливість провалу.",
        ),
        "dice": {"die": "d100", "entries": [
            {"min": lo, "max": hi, "text": txt} for lo, hi, txt in _PUZZLES_EN
        ]},
        "dice_ru": _PUZZLES_RU,
        "dice_ua": _PUZZLES_UA,
    },
]


def _seed(conn: sqlite3.Connection) -> None:
    for c in P25_CONTENTS:
        cid  = c["id"]
        dice = c.get("dice")
        conn.execute("""
            INSERT OR IGNORE INTO contents
                (id, icon, source_slug, source_page, dice, sort_order)
            VALUES (?, ?, 'wom', ?, ?, ?)
        """, (cid, c["icon"], c["source_page"], json.dumps(dice) if dice else None, cid))

        for lang in ("en", "ru", "ua"):
            idx  = {"en": 0, "ru": 1, "ua": 2}[lang]
            name = c["name"][idx]
            desc = c["desc"][idx]
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
            VALUES (25, ?, ?)
        """, (cid, cid))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(P25_CONTENTS)} P25 Horror contents seeded into '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
