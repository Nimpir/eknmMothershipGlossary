"""
scripts/add_psw_equipment.py
Seed Equipment items (P10) from PSG pg 10-11.
Creates P10 linked under P7.
Run after add_psw_tables.py: python scripts/add_psw_equipment.py
"""

import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── P10: Equipment ────────────────────────────────────────────────────────────

PAGE = (10, "🎒", 10, "Equipment", "Снаряжение", "Спорядження")


# ── Equipment items ───────────────────────────────────────────────────────────
# (id, icon, cost, name_en, name_ru, name_ua, desc_en, desc_ru, desc_ua)

EQUIPMENT = [
    (57, "🔧", "20cr",
     "Assorted Tools",
     "Набор Инструментов",
     "Набір Інструментів",
     "Wrenches, spanners, screwdrivers, etc. Can be used as weapons in a pinch (1d5 DMG).",
     "Гаечные ключи, разводные ключи, отвёртки и т.д. В крайнем случае можно использовать как оружие (1d5 урона).",
     "Гайкові ключі, розвідні ключі, викрутки тощо. У крайньому випадку можна використовувати як зброю (1d5 шкоди)."),

    (58, "💊", "1.5kcr",
     "Automed (x5)",
     "Автомед (x5)",
     "Автомед (x5)",
     "Nanotech pills that assist your body in repairing Damage by granting Advantage to Body Saves meant to repel disease and poison, as well as attempts to heal from rest.",
     "Нанотехнологические таблетки, помогающие телу восстанавливаться: дают Преимущество на Спасброски Тела против болезней и ядов, а также при попытках исцеления во время отдыха.",
     "Нанотехнологічні таблетки, що допомагають тілу відновлюватися: дають Перевагу на Порятунки Тіла проти хвороб і отрут, а також при спробах відновлення під час відпочинку."),

    (59, "🔋", "500cr",
     "Battery (High Power)",
     "Аккумулятор (Мощный)",
     "Акумулятор (Потужний)",
     "Heavy duty battery for powering laser cutters, salvage drones, and other items. Recharges in 1 hour connected to power or 6 hours with solar power. Add waterproofing (+500cr).",
     "Мощный аккумулятор для лазерных резаков, дронов и другого оборудования. Заряжается за 1 час от сети или за 6 часов от солнечной энергии. Гидроизоляция (+500кр).",
     "Потужний акумулятор для лазерних різаків, дронів та іншого обладнання. Заряджається за 1 годину від мережі або за 6 годин від сонячної енергії. Гідроізоляція (+500кр)."),

    (60, "🔭", "150cr",
     "Binoculars",
     "Бинокль",
     "Бінокль",
     "20x magnification. Add night vision (+300cr) or thermal vision (+1kcr).",
     "20-кратное увеличение. Добавить ночное зрение (+300кр) или тепловизор (+1ккр).",
     "20-кратне збільшення. Додати нічний зір (+300кр) або тепловізор (+1ккр)."),

    (61, "📡", "3kcr",
     "Bioscanner",
     "Биосканер",
     "Біосканер",
     "Long Range. Scans for signs of life, showing location but not what that life is. Blocked by some materials at the Warden's discretion.",
     "Дальняя дистанция. Сканирует признаки жизни, показывая местоположение, но не тип. Блокируется некоторыми материалами на усмотрение Надзирателя.",
     "Далека дистанція. Сканує ознаки життя, показуючи місцезнаходження, але не тип. Блокується деякими матеріалами на розсуд Охоронця."),

    (62, "📷", "50cr",
     "Body Cam",
     "Нагрудная Камера",
     "Нагрудна Камера",
     "Worn on your clothing. Streams video back to a control center so crewmembers can see what you're seeing. Add night vision (+300cr) or thermal vision (+1kcr).",
     "Носится на одежде. Транслирует видео на пункт управления. Добавить ночное зрение (+300кр) или тепловизор (+1ккр).",
     "Носиться на одязі. Транслює відео на пункт управління. Додати нічний зір (+300кр) або тепловізор (+1ккр)."),

    (63, "🕯️", "5cr",
     "Chemlight (x5)",
     "Химсвет (x5)",
     "Хімсвітло (x5)",
     "Small disposable glowsticks. Dim illumination in a 1m radius.",
     "Маленькие одноразовые световые палочки. Слабое освещение в радиусе 1 метра.",
     "Маленькі одноразові світлові палиці. Слабке освітлення в радіусі 1 метра."),

    (64, "🔬", "2kcr",
     "Cybernetic Diagnostic Scanner",
     "Кибердиагностический Сканер",
     "Кібердіагностичний Сканер",
     "Scans androids and other cybernetic organisms to diagnose physical or mental issues. Often distrusted by androids.",
     "Сканирует андроидов и других киберорганизмов для диагностики физических или ментальных проблем. Андроиды часто относятся к нему с недоверием.",
     "Сканує андроїдів та інших кіберорганізмів для діагностики фізичних або ментальних проблем. Андроїди часто ставляться до нього з недовірою."),

    (65, "🔌", "100cr",
     "Electronic Tool Set",
     "Электронный Набор Инструментов",
     "Електронний Набір Інструментів",
     "A full set of tools for detailed repair or construction work on electronics.",
     "Полный набор инструментов для детального ремонта или сборки электроники.",
     "Повний набір інструментів для детального ремонту або збирання електроніки."),

    (66, "🚨", "2kcr",
     "Emergency Beacon",
     "Аварийный Маяк",
     "Аварійний Маяк",
     "Sends up a flare and emits a loud beep every few seconds. Broadcasts a call on all radio channels to ships or vehicles in the area. Can be blocked by a radio jammer.",
     "Запускает сигнальную ракету и издаёт громкий сигнал каждые несколько секунд. Транслирует вызов на все радиоканалы. Может быть заблокирован радиопомехами.",
     "Запускає сигнальну ракету і видає гучний сигнал кожні кілька секунд. Транслює виклик на всі радіоканали. Може бути заблокований радіоглушником."),

    (67, "🦾", "100kcr",
     "Exoloader",
     "Экзозагрузчик",
     "Екзозавантажувач",
     "Open-air mechanical exoskeleton for heavy lifting (up to 5000kg). Loader claws deal 1 Wound. User can only wear Standard Crew Attire or Standard Battle Dress while operating. Battery operated (48 hours).",
     "Открытый механический экзоскелет для подъёма тяжестей (до 5000 кг). Захваты наносят 1 Ранение. Оператор может носить только Стандартную Одежду или Стандартный Боевой Костюм. Работает от аккумулятора (48 часов).",
     "Відкритий механічний екзоскелет для підняття важких вантажів (до 5000 кг). Захвати завдають 1 Поранення. Оператор може носити лише Стандартний Одяг або Стандартний Бойовий Костюм. Працює від акумулятора (48 годин)."),

    (68, "💣", "500cr",
     "Explosives & Detonator",
     "Взрывчатка и Детонатор",
     "Вибухівка та Детонатор",
     "Explosive charge powerful enough to blow open an airlock. All organisms in Close Range must make a Body Save or take a Wound (Explosive). Detonator works at Long Range, but can be blocked by a radio jammer.",
     "Взрывной заряд, способный вскрыть шлюз. Все существа на Ближней дистанции должны пройти Спасбросок Тела или получить Ранение (Взрыв). Детонатор работает на Дальней дистанции, но может быть заблокирован радиопомехами.",
     "Вибуховий заряд, здатний відкрити шлюз. Усі істоти на Близькій дистанції мають пройти Порятунок Тіла або отримати Поранення (Вибух). Детонатор працює на Далекій дистанції, але може бути заблокований радіоглушником."),

    (69, "🩹", "75cr",
     "First Aid Kit",
     "Аптечка",
     "Аптечка",
     "An assortment of dressings and treatments to help stop bleeding, bandage cuts, and treat other minor injuries.",
     "Набор перевязочных материалов и средств для остановки кровотечения, перевязки порезов и лечения других мелких травм.",
     "Набір перев'язувальних матеріалів і засобів для зупинки кровотечі, перев'язки порізів і лікування інших дрібних травм."),

    (70, "🔦", "30cr",
     "Flashlight",
     "Фонарик",
     "Ліхтарик",
     "Handheld or shoulder mounted. Illuminates 10m ahead of the user.",
     "Ручной или крепится на плечо. Освещает 10 метров перед пользователем.",
     "Ручний або кріпиться на плече. Освітлює 10 метрів перед користувачем."),

    (71, "🛏️", "150cr",
     "Foldable Stretcher",
     "Складные Носилки",
     "Складні Ноші",
     "Portable stretcher that fits within a rucksack. Allows the user to safely strap down the patient and carry them to where their wounds can be better treated. Unfolds to roughly 2m.",
     "Переносные носилки, помещающиеся в рюкзак. Позволяют надёжно зафиксировать пациента и перенести его туда, где можно оказать более качественную помощь. Разворачиваются примерно до 2 метров.",
     "Переносні ноші, що поміщаються у рюкзак. Дозволяють надійно зафіксувати пацієнта і перенести його туди, де можна надати кращу допомогу. Розгортаються приблизно до 2 метрів."),

    (72, "☢️", "20cr",
     "Geiger Counter",
     "Счётчик Гейгера",
     "Лічильник Гейгера",
     "Detects radiation and displays radiation levels.",
     "Обнаруживает радиацию и отображает уровень радиации.",
     "Виявляє радіацію та відображає рівень радіації."),

    (73, "🖥️", "100cr",
     "Heads-Up Display (HUD)",
     "Нашлемный Дисплей",
     "Нашоломний Дисплей",
     "Often worn by marines. Allows the wearer to see through the body cams of others in their unit, and connect to any smart-link upgraded weapon.",
     "Часто используется морскими пехотинцами. Позволяет видеть через нагрудные камеры других бойцов и подключаться к оружию с умной привязкой.",
     "Часто використовується морськими піхотинцями. Дозволяє бачити через нагрудні камери інших бійців і підключатися до зброї з розумним зв'язком."),

    (74, "👁️", "1.5kcr",
     "Infrared Goggles",
     "Инфракрасные Очки",
     "Інфрачервоні Окуляри",
     "Allows the wearer to see heat signatures, sometimes up to several hours old. Add night vision (+300cr).",
     "Позволяют видеть тепловые следы, иногда до нескольких часов давности. Добавить ночное зрение (+300кр).",
     "Дозволяють бачити теплові сліди, іноді до кількох годин давності. Додати нічний зір (+300кр)."),

    (75, "🚀", "75kcr",
     "Jetpack",
     "Реактивный Ранец",
     "Реактивний Ранець",
     "Fly up to 100m high at up to 100km/hr for 2 hours on a tank of fuel. Deals 1d100[+] DMG if destroyed. Fuel can be refilled for 200cr.",
     "Полёт до 100 м высоты со скоростью до 100 км/ч в течение 2 часов на баке топлива. При уничтожении наносит 1d100[+] урона. Заправка — 200кр.",
     "Політ до 100 м висоти зі швидкістю до 100 км/год протягом 2 годин на баку пального. При знищенні завдає 1d100[+] шкоди. Заправка — 200кр."),

    (76, "🔓", "40cr",
     "Lockpick Set",
     "Отмычки",
     "Відмички",
     "A highly advanced set of tools for hacking basic airlock and electronic door systems.",
     "Высокотехнологичный набор инструментов для взлома базовых систем шлюзов и электронных дверей.",
     "Високотехнологічний набір інструментів для злому базових систем шлюзів та електронних дверей."),

    (77, "📻", "1kcr",
     "Long-range Comms",
     "Дальнобойная Радиосвязь",
     "Далекобійний Радіозв'язок",
     "Rucksack-sized communication device for surface-to-ship communication.",
     "Рюкзачное устройство связи для передачи сигнала с поверхности на корабль.",
     "Рюкзачний пристрій зв'язку для передачі сигналу з поверхні на корабель."),

    (78, "👢", "350cr",
     "Mag-boots",
     "Магнитные Ботинки",
     "Магнітні Черевики",
     "Grants a magnetic grip, allowing easy walking on ship exteriors (in space, docked, or free-floating), metal asteroids, or any magnetic surface.",
     "Обеспечивают магнитное сцепление для ходьбы по внешней поверхности корабля (в космосе, пришвартованного или в свободном полёте), металлическим астероидам и другим магнитным поверхностям.",
     "Забезпечують магнітне зчеплення для ходьби по зовнішній поверхні корабля (у космосі, пришвартованого або у вільному польоті), металевим астероїдам та іншим магнітним поверхням."),

    (79, "🏥", "8kcr",
     "Medscanner",
     "Медсканер",
     "Медсканер",
     "Scans a living or dead body to analyze it for disease or abnormalities without biopsy or autopsy. Results may not be instantaneous and may require a lab for complete analysis.",
     "Сканирует живое или мёртвое тело для анализа на заболевания или аномалии без биопсии или аутопсии. Результаты могут быть не мгновенными и требовать лаборатории.",
     "Сканує живе або мертве тіло для аналізу на захворювання або аномалії без біопсії чи розтину. Результати можуть бути не миттєвими і вимагати лабораторії."),

    (80, "⛺", "1kcr",
     "MoHab Unit",
     "Модуль Мобильного Жилья",
     "Модуль Мобільного Житла",
     "Tent, canteen, stove, rucksack, compass, and sleeping bag.",
     "Палатка, фляга, плита, рюкзак, компас и спальный мешок.",
     "Палатка, фляга, плита, рюкзак, компас і спальний мішок."),

    (81, "🍱", "70cr",
     "MRE (x7)",
     "Сухпаёк (x7)",
     "Сухпайок (x7)",
     "\"Meal, Ready-to-Eat.\" Self-contained field rations in lightweight packaging. Each provides sufficient sustenance for one person for one day (does not include water).",
     "«Готовый к употреблению паёк». Самодостаточный полевой рацион в лёгкой упаковке. Каждый обеспечивает одного человека питанием на один день (вода не включена).",
     "«Готовий до вживання пайок». Самодостатній польовий раціон у легкій упаковці. Кожен забезпечує одну людину харчуванням на один день (вода не включена)."),

    (82, "🌡️", "10cr",
     "Mylar Blanket",
     "Термоодеяло",
     "Термоковдра",
     "Lightweight heat-reflective blanket. Often used for thermal regulation of patients suffering from extreme cold or other trauma.",
     "Лёгкое теплоотражающее одеяло. Часто используется для терморегуляции пациентов, страдающих от экстремального холода или других травм.",
     "Легка теплоотбивна ковдра. Часто використовується для терморегуляції пацієнтів, що страждають від екстремального холоду або інших травм."),

    (83, "💨", "50cr",
     "Oxygen Tank",
     "Кислородный Баллон",
     "Кисневий Балон",
     "When attached to a vaccsuit provides up to 12 hours of oxygen under normal circumstances, 4 hours under stressful circumstances. Explosive.",
     "При подключении к вакуумному костюму обеспечивает до 12 часов кислорода в нормальных условиях, 4 часа в стрессовых. Взрывоопасен.",
     "При підключенні до вакуумного костюма забезпечує до 12 годин кисню в нормальних умовах, 4 години в стресових. Вибухонебезпечний."),

    (84, "🪢", "10cr",
     "Paracord (50m)",
     "Паракорд (50м)",
     "Паракорд (50м)",
     "General purpose lightweight nylon rope.",
     "Лёгкая нейлоновая верёвка общего назначения.",
     "Легка нейлонова мотузка загального призначення."),

    (85, "🩺", "200cr",
     "Patch Kit (x3)",
     "Ремнабор для Скафандра (x3)",
     "Ремкомплект для Скафандра (x3)",
     "Repairs punctured and torn vaccsuits, restoring their space readiness. Patched vaccsuits have an AP of 1.",
     "Ремонтирует проколотые и порванные вакуумные костюмы, восстанавливая их годность к использованию в космосе. Залатанные костюмы имеют AP 1.",
     "Ремонтує проколоті та розірвані вакуумні костюми, відновлюючи їх придатність для космосу. Полагоджені костюми мають AP 1."),

    (86, "📍", "200cr",
     "Personal Locator",
     "Персональный Маяк",
     "Персональний Маяк",
     "Allows crewmembers at a control center (or on the bridge of a ship) to track the location of the wearer.",
     "Позволяет членам экипажа на пункте управления (или на мостике корабля) отслеживать местонахождение носителя.",
     "Дозволяє членам екіпажу на пункті управління (або на містку корабля) відстежувати місцезнаходження носія."),

    (87, "🐾", "200kcr",
     "Pet (Organic)",
     "Питомец (Органический)",
     "Вихованець (Органічний)",
     "Small to medium-sized organic pet animal. Larger or rare pets cost 2d10× base price.\n\nWounds: 1(10). Instinct: 2d10+40. 1 Trained Skill. [+] on Rest Saves. 1 Stress when pet takes Damage. Panic Check if pet is killed. Minimum Stress +1.",
     "Небольшое или среднее органическое животное. Крупные или редкие питомцы стоят в 2d10× дороже.\n\nРанения: 1(10). Инстинкт: 2d10+40. 1 Начальный Навык. [+] на Броски Отдыха. 1 Стресс при получении урона питомцем. Проверка Паники при гибели питомца. Минимальный Стресс +1.",
     "Невелика або середня органічна тварина. Великі або рідкісні вихованці коштують у 2d10× дорожче.\n\nПоранення: 1(10). Інстинкт: 2d10+40. 1 Початковий Навик. [+] на Кидки Відпочинку. 1 Стрес при отриманні шкоди вихованцем. Перевірка Паніки при загибелі вихованця. Мінімальний Стрес +1."),

    (88, "🤖", "15kcr",
     "Pet (Synthetic)",
     "Питомец (Синтетический)",
     "Вихованець (Синтетичний)",
     "Small to medium-sized synthetic pet animal. Larger or rare pets cost 2d10× base price.\n\nWounds: 2(15). Instinct: 2d10+30. 2 Trained Skills or 1 Expert Skill. +5 to Rest Saves. Sanity Save or 1 Stress when pet takes Damage. 1 Stress if pet is destroyed.",
     "Небольшое или среднее синтетическое животное. Крупные или редкие питомцы стоят в 2d10× дороже.\n\nРанения: 2(15). Инстинкт: 2d10+30. 2 Начальных Навыка или 1 Экспертный. +5 к Броскам Отдыха. Спасбросок Рассудка или 1 Стресс при получении урона. 1 Стресс при уничтожении питомца.",
     "Невелика або середня синтетична тварина. Великі або рідкісні вихованці коштують у 2d10× дорожче.\n\nПоранення: 2(15). Інстинкт: 2d10+30. 2 Початкових Навики або 1 Експертний. +5 до Кидків Відпочинку. Порятунок Розуму або 1 Стрес при отриманні шкоди. 1 Стрес при знищенні вихованця."),

    (89, "💻", "1.5kcr",
     "Portable Computer Terminal",
     "Портативный Компьютерный Терминал",
     "Портативний Комп'ютерний Термінал",
     "Flat monitor, keyboard and interface allowing the user to hack into pre-existing computers and networks, as well as perform standard computer tasks.",
     "Плоский монитор, клавиатура и интерфейс для взлома существующих компьютеров и сетей, а также для стандартных компьютерных задач.",
     "Плаский монітор, клавіатура та інтерфейс для злому існуючих комп'ютерів і мереж, а також для стандартних комп'ютерних завдань."),

    (90, "🧬", "200cr",
     "Radiation Pills (x5)",
     "Таблетки от Радиации (x5)",
     "Таблетки від Радіації (x5)",
     "Take 1d5 DMG and reduce your Radiation Level by 1 for 2d10 minutes.",
     "Примите, получив 1d5 урона, и снизьте уровень Радиации на 1 на 2d10 минут.",
     "Прийміть, отримавши 1d5 шкоди, і знизьте рівень Радіації на 1 на 2d10 хвилин."),

    (91, "📵", "4kcr",
     "Radio Jammer",
     "Радиоглушитель",
     "Радіоглушник",
     "Rucksack-sized device which, when activated, renders all radio signals within 100km incomprehensible.",
     "Устройство размером с рюкзак. При активации делает все радиосигналы в радиусе 100 км неразборчивыми.",
     "Пристрій розміром з рюкзак. При активації робить усі радіосигнали в радіусі 100 км нерозбірливими."),

    (92, "😷", "500cr",
     "Rebreather",
     "Ребризер",
     "Ребризер",
     "Filters toxic air and/or allows for underwater breathing for up to 20 minutes at a time without resurfacing. Can be connected to an oxygen tank.",
     "Фильтрует токсичный воздух и/или позволяет дышать под водой до 20 минут без подъёма на поверхность. Можно подключить к кислородному баллону.",
     "Фільтрує токсичне повітря та/або дозволяє дихати під водою до 20 хвилин без підйому на поверхню. Можна підключити до кисневого балону."),

    (93, "🎒", "50cr",
     "Rucksack",
     "Рюкзак",
     "Рюкзак",
     "Large, durable, waterproof backpack.",
     "Большой, прочный, водонепроницаемый рюкзак.",
     "Великий, міцний, водонепроникний рюкзак."),

    (94, "🚁", "10kcr",
     "Salvage Drone",
     "Дрон-Мусорщик",
     "Дрон-Збирач",
     "Battery-operated remote controlled drone. Flies up to 450m high, up to 3km from operator, for 2 hours. Records and transmits footage. Can be equipped with up to two attachments: binoculars, radio jammer, Geiger counter, laser cutter, medscanner, personal locator, infrared goggles, emergency beacon, cybernetic diagnostic scanner, or bioscanner. Carries up to 20–30kg.",
     "Дрон с дистанционным управлением на аккумуляторе. Летает до 450 м высоты, до 3 км от оператора, 2 часа. Записывает и передаёт видео. Оснащается двумя приспособлениями: бинокль, глушилка, счётчик Гейгера, лазерный резак, медсканер, маяк, ИК-очки, аварийный маяк, кибердиагностика или биосканер. Грузоподъёмность — до 20–30 кг.",
     "Дрон з дистанційним управлінням на акумуляторі. Летить до 450 м висоти, до 3 км від оператора, 2 години. Записує та передає відео. Оснащується двома пристосуваннями: бінокль, глушник, лічильник Гейгера, лазерний різак, медсканер, маяк, ІЧ-окуляри, аварійний маяк, кібердіагностика або біосканер. Вантажопідйомність — до 20–30 кг."),

    (95, "🧪", "50cr",
     "Sample Collection Kit",
     "Набор для Сбора Образцов",
     "Набір для Збору Зразків",
     "Used to research xenoflora and xenofauna in the field. Takes vital signs, DNA samples, and collects other data on foreign material. Results may require a lab for complete analysis.",
     "Используется для изучения ксенофлоры и ксенофауны в полевых условиях. Снимает жизненные показатели, берёт образцы ДНК и собирает другие данные. Результаты могут требовать лаборатории.",
     "Використовується для вивчення ксенофлори та ксенофауни в польових умовах. Знімає жизнєві показники, бере зразки ДНК та збирає інші дані. Результати можуть вимагати лабораторії."),

    (96, "📟", "100cr",
     "Short-range Comms",
     "Коротковолновая Связь",
     "Короткохвильовий Зв'язок",
     "Allows communication from ship-to-ship within a reasonable distance, and surface-to-surface within a dozen kilometers. Blocked by radio jammer.",
     "Позволяет общаться между кораблями на небольшом расстоянии и на поверхности в пределах нескольких километров. Блокируется радиоглушителем.",
     "Дозволяє спілкуватися між кораблями на невеликій відстані та на поверхні в межах кількох кілометрів. Блокується радіоглушником."),

    (97, "🎯", "10kcr",
     "Smart-link Add-On",
     "Умная Привязка",
     "Розумний Зв'язок",
     "Grants remote viewing, recording, and operation of a ranged weapon, plus +5 DMG to the weapon.",
     "Даёт дистанционный просмотр, запись и управление дальнобойным оружием, а также +5 урона.",
     "Дає дистанційний перегляд, запис і управління далекобійною зброєю, а також +5 шкоди."),

    (98, "💉", "1kcr",
     "Stimpak",
     "Стимпак",
     "Стімпак",
     "Cures cryosickness, reduces Stress by 1, restores 1d10 Health, and grants [+] to all rolls for 1d10 minutes.\n\nOverdose: Roll 1d10. If you roll under the number of doses taken in the past 24 hours, make a Death Save.",
     "Излечивает криобольность, снижает Стресс на 1, восстанавливает 1d10 Здоровья и даёт [+] ко всем броскам на 1d10 минут.\n\nПередозировка: Бросьте 1d10. Если результат ниже числа доз за последние 24 часа — совершите Спасбросок от Смерти.",
     "Лікує кріохворобу, знижує Стрес на 1, відновлює 1d10 Здоров'я і дає [+] до всіх кидків на 1d10 хвилин.\n\nПередозування: Киньте 1d10. Якщо результат нижче кількості доз за останні 24 години — зробіть Порятунок від Смерті."),

    (99, "💧", "50cr",
     "Water Filtration Device",
     "Устройство Фильтрации Воды",
     "Пристрій Фільтрації Води",
     "Can pump 4 liters of filtered water per hour from even the most brackish swamps.",
     "Может перекачивать 4 литра фильтрованной воды в час даже из самых мутных болот.",
     "Може перекачувати 4 літри фільтрованої води на годину навіть з найбрудніших боліт."),
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


# ── Seed ──────────────────────────────────────────────────────────────────────

def _seed(conn: sqlite3.Connection) -> None:
    conn.execute("""
        INSERT OR IGNORE INTO sources (id, slug, title, type)
        VALUES (1, 'psg', 'Player''s Survival Guide', 'core')
    """)

    # Create P10
    pid, icon, src_page, name_en, name_ru, name_ua = PAGE
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (?, ?, 'psg', ?, '[]')
    """, (pid, icon, src_page))
    for lang, name in [("en", name_en), ("ru", name_ru), ("ua", name_ua)]:
        conn.execute("""
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
            VALUES (?, ?, ?)
        """, (pid, lang, name))

    # Link P10 under P7
    _add_linked_page(conn, parent_id=7, child_id=10)

    # Seed each equipment item
    eq_ids = [e[0] for e in EQUIPMENT]
    conn.execute(
        f"DELETE FROM contents WHERE id IN ({','.join('?'*len(eq_ids))})",
        eq_ids,
    )

    for (cid, icon, cost,
         name_en, name_ru, name_ua,
         desc_en, desc_ru, desc_ua) in EQUIPMENT:

        subinfo = json.dumps([{"label_key": "cost", "value": cost, "type": "cost"}])

        conn.execute("""
            INSERT INTO contents (id, icon, source_slug, source_page, subinfo_fixed, sort_order)
            VALUES (?, ?, 'psg', 10, ?, ?)
        """, (cid, icon, subinfo, cid))

        for lang, name, desc in [
            ("en", name_en, desc_en),
            ("ru", name_ru, desc_ru),
            ("ua", name_ua, desc_ua),
        ]:
            conn.execute("""
                INSERT INTO content_i18n (content_id, lang, name, desc, subinfo_text)
                VALUES (?, ?, ?, ?, NULL)
            """, (cid, lang, name, desc))

        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (10, ?, ?)
        """, (cid, cid))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — Equipment (P10) + C57–C99 ({len(EQUIPMENT)} items) seeded into '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
