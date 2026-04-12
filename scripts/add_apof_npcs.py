"""
scripts/add_apof_npcs.py
A Pound of Flesh — P33 Power Brokers (C218-C223): 6 major NPCs.
Each NPC entry includes stats, what they want, and a d10 location table.
Run after add_apof_source_pages.py.
Run: python scripts/add_apof_npcs.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ─────────────────────────────────────────────────────────────────────────────
# P33 POWER BROKERS  (C218–C223)
# (id, icon, source_page, sort_order,
#  name_en, name_ru, name_ua,
#  desc_en, desc_ru, desc_ua,
#  dice_entries_en, dice_entries_ru, dice_entries_ua)
# ─────────────────────────────────────────────────────────────────────────────

NPCS = [
    {
        "id": 218, "icon": "💻", "source_page": 8, "sort_order": 1,
        "name": ("Angus", "Ангус", "Ангус"),
        "desc": (
            "Sysadmin of CANYONHEAVY.market — the intelligence arm of the Golyanovo II Bratva.\n"
            "COMBAT 25 (Revolver 3d10 DMG) | INSTINCT 75 | HITS 2 (20)\n\n"
            "Role: Runs the sector's most powerful data brokerage and hacking collective. Loyal to Yandee. "
            "Always has a lead on work (finder's fee: 2d10cr). Chatty, manic voice.\n\n"
            "JOBS:\n"
            "» Always buying information — tips pay 3d10×10kcr each.\n"
            "» [Strike 1] Locate the Stratemeyer Syndicate hideout. 200kcr.\n"
            "» [Unrest 1] Find who is broadcasting the Hunglung footage. 250kcr.\n"
            "» [Outbreak 1] Investigate rumors of a girl named Ariel haunting the Slickbays. 200kcr.\n"
            "» [Strike 2] Negotiate with Reidmar to end the strike. 2mcr.\n"
            "» Hack The Babushka's OGRE. 5mcr.\n"
            "» See CANYONHEAVY Missions (pg. 25) for more.",

            "Системный администратор CANYONHEAVY.market — разведывательный аппарат Братвы Голяново II.\n"
            "БОЙ 25 (Револьвер 3d10 урона) | ИНСТИНКТ 75 | ОЗ 2 (20)\n\n"
            "Роль: Управляет самым мощным брокером данных и хакерским коллективом сектора. Верен Яндею. "
            "Всегда есть наводка на работу (гонорар: 2d10 кр). Разговорчивый, маниакальный голос.\n\n"
            "ЗАДАНИЯ:\n"
            "» Всегда покупает информацию — чаевые 3d10×10 ккр за штуку.\n"
            "» [Забастовка 1] Найти логово Синдиката Стратемейера. 200 ккр.\n"
            "» [Волнения 1] Найти источник трансляции хунглунгских записей. 250 ккр.\n"
            "» [Вспышка 1] Расследовать слухи о девочке по имени Ариэль в слик-боксах. 200 ккр.\n"
            "» [Забастовка 2] Провести переговоры с Рейдмаром для окончания забастовки. 2 мкр.\n"
            "» Взломать ОГРР Бабушки. 5 мкр.\n"
            "» Миссии CANYONHEAVY (стр. 25).",

            "Системний адміністратор CANYONHEAVY.market — розвідувальний апарат Братви Голяново II.\n"
            "БІЙ 25 (Револьвер 3d10 шкоди) | ІНСТИНКТ 75 | ОЗ 2 (20)\n\n"
            "Роль: Керує найпотужнішим брокером даних і хакерським колективом сектора. Вірний Яндею. "
            "Завжди є наводка на роботу (гонорар: 2d10 кр). Балакучий, маніакальний голос.\n\n"
            "ЗАВДАННЯ:\n"
            "» Завжди купує інформацію — 3d10×10 ккр за штуку.\n"
            "» [Страйк 1] Знайти лігво Синдикату Стратемейера. 200 ккр.\n"
            "» [Заворушення 1] Знайти джерело трансляції записів Хунглунгів. 250 ккр.\n"
            "» [Спалах 1] Розслідувати чутки про дівчинку на ім'я Аріель у слік-боксах. 200 ккр.\n"
            "» [Страйк 2] Провести переговори з Рейдмаром для завершення страйку. 2 мкр.\n"
            "» Зламати ОГРР Бабусі. 5 мкр.\n"
            "» Місії CANYONHEAVY (стор. 25).",
        ),
        "dice_en": [
            "Getting his slicksocket tuned up at The Chop Shop.",
            "Locked in his office on a marathon hacking sprint. (×4)",
            "Locked in his office on a marathon hacking sprint. (×4)",
            "Locked in his office on a marathon hacking sprint. (×4)",
            "Locked in his office on a marathon hacking sprint. (×4)",
            "Coding in the Battlestations with the rest of his crew. (×4)",
            "Coding in the Battlestations with the rest of his crew. (×4)",
            "Coding in the Battlestations with the rest of his crew. (×4)",
            "Coding in the Battlestations with the rest of his crew. (×4)",
            "On a slickraid with his legendary Clan DEKALOG in The Slickbays.",
        ],
        "dice_ru": [
            "Настраивает разъём слика в Мастерской.",
            "Заперся в кабинете на долгом хакерском марафоне. (×4)",
            "Заперся в кабинете на долгом хакерском марафоне. (×4)",
            "Заперся в кабинете на долгом хакерском марафоне. (×4)",
            "Заперся в кабинете на долгом хакерском марафоне. (×4)",
            "Кодирует на Боевых постах с остальными. (×4)",
            "Кодирует на Боевых постах с остальными. (×4)",
            "Кодирует на Боевых постах с остальными. (×4)",
            "Кодирует на Боевых постах с остальными. (×4)",
            "На слик-рейде с легендарным кланом ДЕКАЛОГ в слик-боксах.",
        ],
        "dice_ua": [
            "Налаштовує роз'єм сліка в Майстерні.",
            "Замкнувся в кабінеті на довгому хакерському марафоні. (×4)",
            "Замкнувся в кабінеті на довгому хакерському марафоні. (×4)",
            "Замкнувся в кабінеті на довгому хакерському марафоні. (×4)",
            "Замкнувся в кабінеті на довгому хакерському марафоні. (×4)",
            "Кодує на Бойових постах з рештою. (×4)",
            "Кодує на Бойових постах з рештою. (×4)",
            "Кодує на Бойових постах з рештою. (×4)",
            "Кодує на Бойових постах з рештою. (×4)",
            "На слік-рейді з легендарним кланом ДЕКАЛОГ у слік-боксах.",
        ],
    },
    {
        "id": 219, "icon": "✊", "source_page": 8, "sort_order": 2,
        "name": ("Reidmar", "Рейдмар", "Рейдмар"),
        "desc": (
            "Union rep of Teamsters Local 32819L.\n"
            "COMBAT 35 (Spanner 2d10 DMG) | INSTINCT 55 | HITS 3 (20)\n\n"
            "Role: Union loyalist and legendary pilot. Distributes Yandee's Sycorax to fund Local 32819L's "
            "corporate lobbying. Fluid expression beneath a gruff exterior. Notoriously impatient. Rough voice.\n\n"
            "JOBS:\n"
            "» [Strike 1] Locate the Stratemeyer Syndicate hideout where the fleet is held. 50kcr.\n"
            "» [Strike 1] Provide protection for the Teamsters during negotiations with Yandee. 100kcr.\n"
            "» [Strike 2] Sabotage scab freighters attempting to leave port. 75kcr per ship disabled/destroyed.\n"
            "» [Unrest 2] Smuggle weapons into The Choke. 500kcr/run.\n"
            "» [Outbreak 2] Help evacuate The Dream. 1mcr/evacuation run.\n"
            "» Make a Jump-6 delivery. 5mcr.",

            "Представитель профсоюза Местной 32819L Тимстеров.\n"
            "БОЙ 35 (Ключ 2d10 урона) | ИНСТИНКТ 55 | ОЗ 3 (20)\n\n"
            "Роль: Верный профсоюзник и легендарный пилот. Распространяет Сикорах Яндея для финансирования "
            "лоббирования. За грубой внешностью скрыты эмоции. Чрезвычайно нетерпелив. Грубый голос.\n\n"
            "ЗАДАНИЯ:\n"
            "» [Забастовка 1] Найти логово Синдиката Стратемейера, где удерживается флот. 50 ккр.\n"
            "» [Забастовка 1] Охранять Тимстеров на переговорах с Яндеем. 100 ккр.\n"
            "» [Забастовка 2] Саботировать грузовики штрейкбрехеров. 75 ккр за корабль.\n"
            "» [Волнения 2] Переправить оружие в Удавку. 500 ккр/рейс.\n"
            "» [Вспышка 2] Помочь эвакуировать Мечту. 1 мкр/рейс.\n"
            "» Доставка с Прыжком-6. 5 мкр.",

            "Представник профспілки Місцевої 32819L Тімстерів.\n"
            "БІЙ 35 (Ключ 2d10 шкоди) | ІНСТИНКТ 55 | ОЗ 3 (20)\n\n"
            "Роль: Вірний профспілкіст і легендарний пілот. Розповсюджує Сикорах Яндея для фінансування "
            "лобіювання. За грубою зовнішністю ховаються емоції. Надзвичайно нетерплячий. Грубий голос.\n\n"
            "ЗАВДАННЯ:\n"
            "» [Страйк 1] Знайти лігво Синдикату Стратемейера, де утримується флот. 50 ккр.\n"
            "» [Страйк 1] Охороняти Тімстерів на переговорах з Яндеєм. 100 ккр.\n"
            "» [Страйк 2] Саботувати вантажівки штрейкбрехерів. 75 ккр за корабель.\n"
            "» [Заворушення 2] Переправити зброю до Задуші. 500 ккр/рейс.\n"
            "» [Спалах 2] Допомогти евакуювати Мрію. 1 мкр/рейс.\n"
            "» Доставка зі Стрибком-6. 5 мкр.",
        ),
        "dice_en": [
            "Fixing up the Conquer All with his daughter, Trieu.",
            "Overseeing Sycorax shipment in a Hangar Bay. (×4)",
            "Overseeing Sycorax shipment in a Hangar Bay. (×4)",
            "Overseeing Sycorax shipment in a Hangar Bay. (×4)",
            "Overseeing Sycorax shipment in a Hangar Bay. (×4)",
            "Swapping piloting stories with the Oldtimers at Sem's Bar. (×4)",
            "Swapping piloting stories with the Oldtimers at Sem's Bar. (×4)",
            "Swapping piloting stories with the Oldtimers at Sem's Bar. (×4)",
            "Swapping piloting stories with the Oldtimers at Sem's Bar. (×4)",
            "Union meeting in Loshe's Office. Leadership challenge. High tensions.",
        ],
        "dice_ru": [
            "Чинит «Покори всё» вместе с дочерью Трьё.",
            "Следит за отгрузкой Сикораха в ангаре. (×4)",
            "Следит за отгрузкой Сикораха в ангаре. (×4)",
            "Следит за отгрузкой Сикораха в ангаре. (×4)",
            "Следит за отгрузкой Сикораха в ангаре. (×4)",
            "Обменивается историями с ветеранами в баре Сема. (×4)",
            "Обменивается историями с ветеранами в баре Сема. (×4)",
            "Обменивается историями с ветеранами в баре Сема. (×4)",
            "Обменивается историями с ветеранами в баре Сема. (×4)",
            "Собрание профсоюза в офисе Лоше. Оспаривание лидерства. Высокое напряжение.",
        ],
        "dice_ua": [
            "Лагодить «Підкори всіх» разом з донькою Трьє.",
            "Спостерігає за відвантаженням Сикораху в ангарі. (×4)",
            "Спостерігає за відвантаженням Сикораху в ангарі. (×4)",
            "Спостерігає за відвантаженням Сикораху в ангарі. (×4)",
            "Спостерігає за відвантаженням Сикораху в ангарі. (×4)",
            "Обмінюється пілотськими історіями з ветеранами в барі Сема. (×4)",
            "Обмінюється пілотськими історіями з ветеранами в барі Сема. (×4)",
            "Обмінюється пілотськими історіями з ветеранами в барі Сема. (×4)",
            "Обмінюється пілотськими історіями з ветеранами в барі Сема. (×4)",
            "Збори профспілки в офісі Лоше. Оспорювання лідерства. Висока напруга.",
        ],
    },
    {
        "id": 220, "icon": "🎩", "source_page": 8, "sort_order": 3,
        "name": ("Yandee", "Яндей", "Яндей"),
        "desc": (
            "Vor of the Golyanovo II Bratva. (Secretly an android.)\n"
            "COMBAT 65 (Laser Pistol 1d10 DMG) | INSTINCT 80 | HITS 4 (55)\n\n"
            "Role: Built from scraps on a prison world. Rose through the Bratva by discovering the Sycorax trade. "
            "Methodical and meticulous. Runs The Dream through fear, money, and information. "
            "The truth of their android nature is their most guarded secret.\n\n"
            "JOBS:\n"
            "» The Babushka is late on protection money. Collect. 50kcr.\n"
            "» [Strike 1] Assassinate the head of The Syndicate. 20mcr.\n"
            "» [Strike 2] Destroy the Conquer All. Make it look like an accident. 1mcr.\n"
            "» [Strike 2] Escort Teamster scabs to work. 50kcr/day.\n"
            "» [Unrest 2] Find the Sycorax formula in Farm Two. 20mcr and a ship.\n"
            "» [Outbreak 3] Kill Caliban. 50mcr.\n"
            "» Harvest Sycorax. 10kcr per 3 fruit.\n"
            "» Do 3 jobs for Yandee and become a Novo Droog (10kcr/week).",

            "Вор братвы Голяново II. (Тайно — андроид.)\n"
            "БОЙ 65 (Лазерный пистолет 1d10 урона) | ИНСТИНКТ 80 | ОЗ 4 (55)\n\n"
            "Роль: Собран из запчастей на тюремном мире. Поднялся в Братве, открыв торговлю Сикорахом. "
            "Педантичный и методичный. Управляет Мечтой через страх, деньги и информацию. "
            "Правда об андроидной природе — самый охраняемый секрет.\n\n"
            "ЗАДАНИЯ:\n"
            "» Бабушка задерживает деньги за крышу. Взыскать. 50 ккр.\n"
            "» [Забастовка 1] Убить главу Синдиката. 20 мкр.\n"
            "» [Забастовка 2] Уничтожить «Покори всё». Под видом несчастного случая. 1 мкр.\n"
            "» [Забастовка 2] Сопровождать штрейкбрехеров на работу. 50 ккр/день.\n"
            "» [Волнения 2] Найти формулу Сикораха на Ферме-2. 20 мкр и корабль.\n"
            "» [Вспышка 3] Убить Калибана. 50 мкр.\n"
            "» Собрать Сикорах. 10 ккр за 3 плода.\n"
            "» Выполни 3 задания Яндея — стань Дружинником Новосов (10 ккр/неделя).",

            "Вор Братви Голяново II. (Таємно — андроїд.)\n"
            "БІЙ 65 (Лазерний пістолет 1d10 шкоди) | ІНСТИНКТ 80 | ОЗ 4 (55)\n\n"
            "Роль: Зібраний з брухту на тюремному світі. Піднявся у Братві, відкривши торгівлю Сикорахом. "
            "Педантичний і методичний. Керує Мрією через страх, гроші та інформацію. "
            "Правда про андроїдну природу — найбільш охоронюваний секрет.\n\n"
            "ЗАВДАННЯ:\n"
            "» Бабуся затримує гроші за дах. Стягти. 50 ккр.\n"
            "» [Страйк 1] Вбити голову Синдикату. 20 мкр.\n"
            "» [Страйк 2] Знищити «Підкори всіх». Під виглядом нещасного випадку. 1 мкр.\n"
            "» [Страйк 2] Супроводжувати штрейкбрехерів на роботу. 50 ккр/день.\n"
            "» [Заворушення 2] Знайти формулу Сикораху на Фермі-2. 20 мкр і корабель.\n"
            "» [Спалах 3] Вбити Калібана. 50 мкр.\n"
            "» Зібрати Сикорах. 10 ккр за 3 плоди.\n"
            "» Виконай 3 завдання Яндея — стань Дружинником Новосів (10 ккр/тиждень).",
        ),
        "dice_en": [
            "The Farm: Processing. Random audit of Sycorax production.",
            "Giving orders to the Novo Droogs in Heaven (The Stellar Burn upper level). (×4)",
            "Giving orders to the Novo Droogs in Heaven (The Stellar Burn upper level). (×4)",
            "Giving orders to the Novo Droogs in Heaven (The Stellar Burn upper level). (×4)",
            "Giving orders to the Novo Droogs in Heaven (The Stellar Burn upper level). (×4)",
            "In their penthouse above The Stellar Burn, going over intelligence reports from Angus. (×4)",
            "In their penthouse above The Stellar Burn, going over intelligence reports from Angus. (×4)",
            "In their penthouse above The Stellar Burn, going over intelligence reports from Angus. (×4)",
            "In their penthouse above The Stellar Burn, going over intelligence reports from Angus. (×4)",
            "Gambling at The Court.",
        ],
        "dice_ru": [
            "Ферма: производство. Случайный аудит выпуска Сикораха.",
            "Раздаёт приказы Дружинникам в «Небесах» (верхний уровень Звёздного ожога). (×4)",
            "Раздаёт приказы Дружинникам в «Небесах» (верхний уровень Звёздного ожога). (×4)",
            "Раздаёт приказы Дружинникам в «Небесах» (верхний уровень Звёздного ожога). (×4)",
            "Раздаёт приказы Дружинникам в «Небесах» (верхний уровень Звёздного ожога). (×4)",
            "В пентхаусе над Звёздным ожогом, изучает разведывательные отчёты Ангуса. (×4)",
            "В пентхаусе над Звёздным ожогом, изучает разведывательные отчёты Ангуса. (×4)",
            "В пентхаусе над Звёздным ожогом, изучает разведывательные отчёты Ангуса. (×4)",
            "В пентхаусе над Звёздным ожогом, изучает разведывательные отчёты Ангуса. (×4)",
            "Играет в азартные игры в Суде.",
        ],
        "dice_ua": [
            "Ферма: виробництво. Випадковий аудит випуску Сикораху.",
            "Роздає накази Дружинникам на «Небесах» (верхній рівень Зоряного опіку). (×4)",
            "Роздає накази Дружинникам на «Небесах» (верхній рівень Зоряного опіку). (×4)",
            "Роздає накази Дружинникам на «Небесах» (верхній рівень Зоряного опіку). (×4)",
            "Роздає накази Дружинникам на «Небесах» (верхній рівень Зоряного опіку). (×4)",
            "У пентхаусі над Зоряним опіком, вивчає розвідувальні звіти Ангуса. (×4)",
            "У пентхаусі над Зоряним опіком, вивчає розвідувальні звіти Ангуса. (×4)",
            "У пентхаусі над Зоряним опіком, вивчає розвідувальні звіти Ангуса. (×4)",
            "У пентхаусі над Зоряним опіком, вивчає розвідувальні звіти Ангуса. (×4)",
            "Грає в азартні ігри в Суді.",
        ],
    },
    {
        "id": 221, "icon": "⚖️", "source_page": 9, "sort_order": 4,
        "name": ("Brunhildh", "Брунхильд", "Брунхільд"),
        "desc": (
            "Chief Adjudicator of The Court.\n"
            "COMBAT 70 (Antique Blunderbuss 6d10 DMG) | INSTINCT 65 | HITS 3 (45)\n\n"
            "Role: Retired bounty hunter. Yandee's fanatical right hand. Feared interrogator. "
            "Settled on The Dream for quality Big Switch and combat. "
            "Uses a modded antique blunderbuss worth 2mcr. (Note: secretly an android — see Rumors.)\n\n"
            "JOBS:\n"
            "» Find out if Cutter is loyal to Yandee. 1mcr for hard evidence.\n"
            "» Playtest new Slicksquid design — survive and become an honorary Executioner.\n"
            "» [Unrest 2] Locate and apprehend Imogene Kane. Alive. 2mcr.\n"
            "» [Outbreak 2] The Court needs Chokespawn for the Pit. 100kcr each, alive only.\n"
            "» [Strike 3] Protect Yandee from Teamsters and get them off The Dream. 2mcr. Become Novo Captain.\n"
            "» Act as Public Defender. 5kcr/win.",

            "Главный арбитр Суда.\n"
            "БОЙ 70 (Антикварный мушкет 6d10 урона) | ИНСТИНКТ 65 | ОЗ 3 (45)\n\n"
            "Роль: Бывший охотник за головами. Фанатичная правая рука Яндея. Грозный следователь. "
            "Осела на Мечте ради качественного Большого переключателя и боёв. "
            "Использует модифицированный антикварный мушкет стоимостью 2 мкр. (Тайно — андроид.)\n\n"
            "ЗАДАНИЯ:\n"
            "» Выяснить, верен ли Каттер Яндею. 1 мкр за твёрдые улики.\n"
            "» Опробовать новый дизайн Слик-кальмара — выжить и стать почётным Палачом.\n"
            "» [Волнения 2] Найти и задержать Имоджен Кейн. Живой. 2 мкр.\n"
            "» [Вспышка 2] Суду нужны Чокспауны для Ямы. 100 ккр за штуку, только живых.\n"
            "» [Забастовка 3] Защитить Яндея от Тимстеров. 2 мкр. Стать капитаном Новосов.\n"
            "» Работа Публичным защитником. 5 ккр/победа.",

            "Головний арбітр Суду.\n"
            "БІЙ 70 (Антикварний мушкет 6d10 шкоди) | ІНСТИНКТ 65 | ОЗ 3 (45)\n\n"
            "Роль: Колишній мисливець за головами. Фанатична права рука Яндея. Грозний слідчий. "
            "Осіла на Мрії заради якісного Великого перемикача та боїв. "
            "Використовує модифікований антикварний мушкет вартістю 2 мкр. (Таємно — андроїд.)\n\n"
            "ЗАВДАННЯ:\n"
            "» З'ясувати, чи вірний Каттер Яндею. 1 мкр за тверді докази.\n"
            "» Випробувати новий дизайн Слік-кальмара — вижити та стати почесним Катом.\n"
            "» [Заворушення 2] Знайти та затримати Імоджен Кейн. Живою. 2 мкр.\n"
            "» [Спалах 2] Суду потрібні Чокспауни для Ями. 100 ккр за штуку, лише живих.\n"
            "» [Страйк 3] Захистити Яндея від Тімстерів. 2 мкр. Стати капітаном Новосів.\n"
            "» Робота Публічним захисником. 5 ккр/перемога.",
        ),
        "dice_en": [
            "Detailed weapon maintenance in her Quarters.",
            "Sitting on The Bench at The Court. (×4)",
            "Sitting on The Bench at The Court. (×4)",
            "Sitting on The Bench at The Court. (×4)",
            "Sitting on The Bench at The Court. (×4)",
            "Sublevel C (Tempest HQ), with Yandee, interrogating captured Hunglungs. (×4)",
            "Sublevel C (Tempest HQ), with Yandee, interrogating captured Hunglungs. (×4)",
            "Sublevel C (Tempest HQ), with Yandee, interrogating captured Hunglungs. (×4)",
            "Sublevel C (Tempest HQ), with Yandee, interrogating captured Hunglungs. (×4)",
            "The Dry Dock. Sending out a team of bounty hunters.",
        ],
        "dice_ru": [
            "Детальное обслуживание оружия в своих покоях.",
            "Сидит на Скамье судьи в Суде. (×4)",
            "Сидит на Скамье судьи в Суде. (×4)",
            "Сидит на Скамье судьи в Суде. (×4)",
            "Сидит на Скамье судьи в Суде. (×4)",
            "Подуровень C (штаб Tempest), допрашивает захваченных Хунглунгов с Яндеем. (×4)",
            "Подуровень C (штаб Tempest), допрашивает захваченных Хунглунгов с Яндеем. (×4)",
            "Подуровень C (штаб Tempest), допрашивает захваченных Хунглунгов с Яндеем. (×4)",
            "Подуровень C (штаб Tempest), допрашивает захваченных Хунглунгов с Яндеем. (×4)",
            "Сухой dok. Отправляет группу охотников за головами.",
        ],
        "dice_ua": [
            "Детальне обслуговування зброї у своїх покоях.",
            "Сидить на Лаві судді в Суді. (×4)",
            "Сидить на Лаві судді в Суді. (×4)",
            "Сидить на Лаві судді в Суді. (×4)",
            "Сидить на Лаві судді в Суді. (×4)",
            "Підрівень C (штаб Tempest), допитує захоплених Хунглунгів з Яндеєм. (×4)",
            "Підрівень C (штаб Tempest), допитує захоплених Хунглунгів з Яндеєм. (×4)",
            "Підрівень C (штаб Tempest), допитує захоплених Хунглунгів з Яндеєм. (×4)",
            "Підрівень C (штаб Tempest), допитує захоплених Хунглунгів з Яндеєм. (×4)",
            "Сухий dok. Відправляє групу мисливців за головами.",
        ],
    },
    {
        "id": 222, "icon": "🎖️", "source_page": 9, "sort_order": 5,
        "name": ("Cutter", "Каттер", "Каттер"),
        "desc": (
            "Commander of Tempest Company.\n"
            "COMBAT 75 (Pulse Rifle 5d10 DMG) | INSTINCT 55 | HITS 3 (50)\n\n"
            "Role: Established his command as a privateer during the Corp Wars. Widely feared as a "
            "salt-the-earth tactician. Security arm of the Golyanovo II Bratva. Doesn't trust Yandee. "
            "Unrelenting voice. (Secret: plotting Yandee's overthrow with an inner circle of Platoon Commanders.)\n\n"
            "JOBS:\n"
            "» [Unrest 1] Find the Hunglungs who bombed the station. 250kcr.\n"
            "» [Unrest 2] Arrest Ukko/Ukka. Gain a Rank in Tempest Co. 400kcr.\n"
            "» [Outbreak 2] Hunt Chokespawn. Given an Exosuit and 30kcr/kill.\n"
            "» [Strike 3] Kill Reidmar. Gain a Rank in Tempest Co. and your own 5-member Operator Squad.\n"
            "» [Unrest 3] Defeat the Hunglung Insurgency. Kill Imogene Kane. Promoted to Platoon Commander.\n"
            "» (Secret) Kill Novo Droogs. 10kcr/kill.\n"
            "» See Tempest Mission Table for more work.",

            "Командир наёмной компании Tempest.\n"
            "БОЙ 75 (Импульсная винтовка 5d10 урона) | ИНСТИНКТ 55 | ОЗ 3 (50)\n\n"
            "Роль: Создал командование в период корпоративных войн. Прославился как тактик, "
            "выжигающий землю за собой. Силовое крыло Братвы Голяново II. Не доверяет Яндею. "
            "Непреклонный голос. (Секрет: планирует свержение Яндея с кругом комсостава.)\n\n"
            "ЗАДАНИЯ:\n"
            "» [Волнения 1] Найти хунглунгов, взорвавших станцию. 250 ккр.\n"
            "» [Волнения 2] Арестовать Укко/Укку. Получить звание в Tempest Co. 400 ккр.\n"
            "» [Вспышка 2] Охотиться на Чокспаунов. Выдаётся экзокостюм + 30 ккр/убийство.\n"
            "» [Забастовка 3] Убить Рейдмара. Звание + собственный отряд из 5 операторов.\n"
            "» [Волнения 3] Подавить восстание Хунглунгов. Убить Имоджен Кейн. Повышение.\n"
            "» (Секрет) Убивать Дружинников Новосов. 10 ккр/убийство.\n"
            "» Таблица миссий Tempest Co. — ещё работа.",

            "Командир найманської компанії Tempest.\n"
            "БІЙ 75 (Імпульсна гвинтівка 5d10 шкоди) | ІНСТИНКТ 55 | ОЗ 3 (50)\n\n"
            "Роль: Створив командування під час корпоративних воєн. Прославився як тактик, "
            "що спалює землю за собою. Силове крило Братви Голяново II. Не довіряє Яндею. "
            "Непохитний голос. (Секрет: планує повалення Яндея з колом командного складу.)\n\n"
            "ЗАВДАННЯ:\n"
            "» [Заворушення 1] Знайти Хунглунгів, що підірвали станцію. 250 ккр.\n"
            "» [Заворушення 2] Арештувати Укко/Укку. Отримати звання в Tempest Co. 400 ккр.\n"
            "» [Спалах 2] Полювати на Чокспаунів. Видається екзокостюм + 30 ккр/вбивство.\n"
            "» [Страйк 3] Вбити Рейдмара. Звання + власний загін з 5 операторів.\n"
            "» [Заворушення 3] Придушити повстання Хунглунгів. Вбити Імоджен Кейн. Підвищення.\n"
            "» (Секрет) Вбивати Дружинників Новосів. 10 ккр/вбивство.\n"
            "» Таблиця місій Tempest Co. — ще робота.",
        ),
        "dice_en": [
            "R&R at The Ecstacy (lower level of The Stellar Burn).",
            "Armament Level (Tempest HQ) running new recruits through slicktraining. (×4)",
            "Armament Level (Tempest HQ) running new recruits through slicktraining. (×4)",
            "Armament Level (Tempest HQ) running new recruits through slicktraining. (×4)",
            "Armament Level (Tempest HQ) running new recruits through slicktraining. (×4)",
            "Operations Level (Tempest HQ) commanding in-progress missions. (×4)",
            "Operations Level (Tempest HQ) commanding in-progress missions. (×4)",
            "Operations Level (Tempest HQ) commanding in-progress missions. (×4)",
            "Operations Level (Tempest HQ) commanding in-progress missions. (×4)",
            "In his mansion (Tempest HQ) plotting Yandee's overthrow with his inner circle.",
        ],
        "dice_ru": [
            "Отдыхает в «Экстазе» (нижний уровень Звёздного ожога).",
            "Уровень вооружения (штаб Tempest) — тренирует новобранцев в слик-обучении. (×4)",
            "Уровень вооружения (штаб Tempest) — тренирует новобранцев в слик-обучении. (×4)",
            "Уровень вооружения (штаб Tempest) — тренирует новобранцев в слик-обучении. (×4)",
            "Уровень вооружения (штаб Tempest) — тренирует новобранцев в слик-обучении. (×4)",
            "Оперативный уровень (штаб Tempest) — командует текущими операциями. (×4)",
            "Оперативный уровень (штаб Tempest) — командует текущими операциями. (×4)",
            "Оперативный уровень (штаб Tempest) — командует текущими операциями. (×4)",
            "Оперативный уровень (штаб Tempest) — командует текущими операциями. (×4)",
            "В своём особняке (штаб Tempest) — планирует свержение Яндея с кругом офицеров.",
        ],
        "dice_ua": [
            "Відпочиває в «Екстазі» (нижній рівень Зоряного опіку).",
            "Рівень озброєння (штаб Tempest) — тренує новобранців у слік-навчанні. (×4)",
            "Рівень озброєння (штаб Tempest) — тренує новобранців у слік-навчанні. (×4)",
            "Рівень озброєння (штаб Tempest) — тренує новобранців у слік-навчанні. (×4)",
            "Рівень озброєння (штаб Tempest) — тренує новобранців у слік-навчанні. (×4)",
            "Оперативний рівень (штаб Tempest) — командує поточними операціями. (×4)",
            "Оперативний рівень (штаб Tempest) — командує поточними операціями. (×4)",
            "Оперативний рівень (штаб Tempest) — командує поточними операціями. (×4)",
            "Оперативний рівень (штаб Tempest) — командує поточними операціями. (×4)",
            "У своєму особняку (штаб Tempest) — планує повалення Яндея з колом офіцерів.",
        ],
    },
    {
        "id": 223, "icon": "🌞", "source_page": 9, "sort_order": 6,
        "name": ("Ukko/Ukka", "Укко/Укка", "Укко/Укка"),
        "desc": (
            "High Gardener of Invictus Sol (the Evangelical Solarian Church).\n"
            "COMBAT 20 (Unarmed 1d5 DMG) | INSTINCT 60 | HITS 2 (20)\n\n"
            "Role: Born in Doptown; harvested Sycorax to pay off their birth debt. Joined the Solarians as a "
            "chemist and rose quickly to High Gardener. Donates massive O2 to The Choke. Coughs. "
            "Secretly a Hunglung sympathizer and patron.\n\n"
            "JOBS:\n"
            "» Always looking for Public Defenders for the oxy-poor. Can pay in drug supply.\n"
            "» [Strike 1] Negotiate a deal between The Novos and Local 32819L. 20mcr.\n"
            "» [Outbreak 1] Investigate rumors of a 'Dr. Bancali' in The Choke. 40kcr.\n"
            "» [Unrest 2] Smuggle Ukko/Ukka off The Dream before Tempest Co. can kill them. "
            "The Solarian Church will owe you a great debt.\n"
            "» [Outbreak 3] Destroy the infected Aarnivalkea. You'll be given a Solarian shuttle.\n"
            "» Donate O2 to Doptown.",

            "Старший Садовник Непобедимого Солнца (Евангелической Солярианской Церкви).\n"
            "БОЙ 20 (Безоружный 1d5 урона) | ИНСТИНКТ 60 | ОЗ 2 (20)\n\n"
            "Роль: Родился в Доптауне; собирал Сикорах, чтобы расплатиться за долг при рождении. "
            "Вступил в Солярианцев химиком, быстро поднялся до Старшего Садовника. "
            "Жертвует огромные запасы О2 в Удавку. Кашляет. Тайно — сочувствующий Хунглунгам.\n\n"
            "ЗАДАНИЯ:\n"
            "» Всегда ищет Публичных защитников для бедных кислородом. Платит наркотиками.\n"
            "» [Забастовка 1] Договориться между Новосами и Местной 32819L. 20 мкр.\n"
            "» [Вспышка 1] Расследовать слухи о «докторе Банкали» в Удавке. 40 ккр.\n"
            "» [Волнения 2] Вывезти Укко/Укку с Мечты до того, как Tempest Co. их уничтожит. "
            "Солярианская Церковь будет в долгу.\n"
            "» [Вспышка 3] Уничтожить заражённое Аарнивалкеа. Получите шаттл Солярианцев.\n"
            "» Пожертвовать О2 Доптауну.",

            "Старший Садівник Непереможного Сонця (Євангелічної Соляріанської Церкви).\n"
            "БІЙ 20 (Беззбройний 1d5 шкоди) | ІНСТИНКТ 60 | ОЗ 2 (20)\n\n"
            "Роль: Народився в Доптауні; збирав Сикорах, щоб розплатитися за борг при народженні. "
            "Вступив до Соляріанців хіміком, швидко піднявся до Старшого Садівника. "
            "Жертвує величезні запаси О2 до Задуші. Кашляє. Таємно — симпатик Хунглунгів.\n\n"
            "ЗАВДАННЯ:\n"
            "» Завжди шукає Публічних захисників для бідних на кисень. Платить наркотиками.\n"
            "» [Страйк 1] Домовитися між Новосами та Місцевою 32819L. 20 мкр.\n"
            "» [Спалах 1] Розслідувати чутки про «доктора Банкалі» в Задуші. 40 ккр.\n"
            "» [Заворушення 2] Вивезти Укко/Укку з Мрії до того, як Tempest Co. їх знищить. "
            "Соляріанська Церква буде в боргу.\n"
            "» [Спалах 3] Знищити заражене Аарнівалкеа. Отримаєте шаттл Соляріанців.\n"
            "» Пожертвувати О2 Доптауну.",
        ),
        "dice_en": [
            "In The Holding Cells (The Court), giving counsel to the Accused.",
            "Walking the corridors giving money and seeds to the poor. (×4)",
            "Walking the corridors giving money and seeds to the poor. (×4)",
            "Walking the corridors giving money and seeds to the poor. (×4)",
            "Walking the corridors giving money and seeds to the poor. (×4)",
            "Silently tending to the Aarnivalkea (The Farm). Will listen to anyone. (×4)",
            "Silently tending to the Aarnivalkea (The Farm). Will listen to anyone. (×4)",
            "Silently tending to the Aarnivalkea (The Farm). Will listen to anyone. (×4)",
            "Silently tending to the Aarnivalkea (The Farm). Will listen to anyone. (×4)",
            "Secretly meeting with Imogene Kane in Doptown.",
        ],
        "dice_ru": [
            "В камерах задержанных (Суд), консультирует обвиняемых.",
            "Ходит по коридорам, раздавая деньги и семена бедным. (×4)",
            "Ходит по коридорам, раздавая деньги и семена бедным. (×4)",
            "Ходит по коридорам, раздавая деньги и семена бедным. (×4)",
            "Ходит по коридорам, раздавая деньги и семена бедным. (×4)",
            "Молча ухаживает за Аарнивалкеа (Ферма). Выслушает любого. (×4)",
            "Молча ухаживает за Аарнивалкеа (Ферма). Выслушает любого. (×4)",
            "Молча ухаживает за Аарнивалкеа (Ферма). Выслушает любого. (×4)",
            "Молча ухаживает за Аарнивалкеа (Ферма). Выслушает любого. (×4)",
            "Тайно встречается с Имоджен Кейн в Доптауне.",
        ],
        "dice_ua": [
            "У камерах затримання (Суд), консультує обвинувачених.",
            "Ходить коридорами, роздаючи гроші та насіння бідним. (×4)",
            "Ходить коридорами, роздаючи гроші та насіння бідним. (×4)",
            "Ходить коридорами, роздаючи гроші та насіння бідним. (×4)",
            "Ходить коридорами, роздаючи гроші та насіння бідним. (×4)",
            "Мовчки доглядає за Аарнівалкеа (Ферма). Вислухає кожного. (×4)",
            "Мовчки доглядає за Аарнівалкеа (Ферма). Вислухає кожного. (×4)",
            "Мовчки доглядає за Аарнівалкеа (Ферма). Вислухає кожного. (×4)",
            "Мовчки доглядає за Аарнівалкеа (Ферма). Вислухає кожного. (×4)",
            "Таємно зустрічається з Імоджен Кейн у Доптауні.",
        ],
    },
]


def _seed(conn: sqlite3.Connection) -> None:
    for npc in NPCS:
        cid        = npc["id"]
        icon       = npc["icon"]
        src_page   = npc["source_page"]
        sort_order = npc["sort_order"]

        # Build dice data (d10 location table)
        entries_en = npc["dice_en"]
        entries_ru = npc["dice_ru"]
        entries_ua = npc["dice_ua"]

        dice_base = {
            "die": "d10",
            "entries": [
                {"min": i, "max": i, "text": entries_en[i]}
                for i in range(10)
            ],
        }

        conn.execute("""
            INSERT OR IGNORE INTO contents
                (id, icon, source_slug, source_page, dice, sort_order)
            VALUES (?, ?, 'apof', ?, ?, ?)
        """, (cid, icon, src_page, json.dumps(dice_base), sort_order))

        names = npc["name"]
        descs = npc["desc"]

        for i, (lang, d_texts) in enumerate([
            ("en", entries_en),
            ("ru", entries_ru),
            ("ua", entries_ua),
        ]):
            overridden_entries = [
                {"min": j, "max": j, "text": d_texts[j]}
                for j in range(10)
            ]
            conn.execute("""
                INSERT OR IGNORE INTO content_i18n
                    (content_id, lang, name, desc, dice_entries)
                VALUES (?, ?, ?, ?, ?)
            """, (cid, lang, names[i], descs[i], json.dumps(overridden_entries)))

        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (33, ?, ?)
        """, (cid, sort_order))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(NPCS)} NPC content items added to P33.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
