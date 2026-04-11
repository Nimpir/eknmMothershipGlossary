"""
scripts/add_psw_combat.py
Seed Combat, Wounds & Death, and Range & Distance from the Player's Survival Guide.
Run after schema init: python scripts/add_psw_combat.py
"""

import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── Pages ─────────────────────────────────────────────────────────────────────

PAGES = [
    # (id, icon, source_page,
    #  name_en, name_ru, name_ua,
    #  desc_en, desc_ru, desc_ua)
    (3, "⚔️", 26,
     "Combat",           "Бой",          "Бій",
     None, None, None),

    (4, "💀", 29,
     "Wounds & Death",   "Ранения и Смерть",  "Поранення та Смерть",
     None, None, None),

    (5, "📏", 30,
     "Range & Distance", "Дистанция",    "Дистанція",
     "Range, distance, and movement are tracked abstractly in Range Bands.",
     "Дальность, расстояние и движение отслеживаются абстрактно в Диапазонах Дистанций.",
     "Відстань і рух відстежуються абстрактно у Смугах Дистанцій."),
]


# ── Contents ──────────────────────────────────────────────────────────────────
# Each entry is a dict so the varied fields stay readable.

CONTENTS = [

    # ── P3: Combat ────────────────────────────────────────────────────────────

    {"id": 23, "page": 3, "icon": "⚔️", "source_page": 26, "dice": None, "subinfo": None,
     "name":    ("Turn Order",          "Порядок Ходов",            "Порядок Ходів"),
     "desc":    (
         "Violence in Mothership is incredibly dangerous and should be avoided at all costs. "
         "During a violent confrontation, time splits into roughly 10-second intervals called rounds. "
         "Everything within a round happens simultaneously.\n\n"
         "The Warden describes the situation. Each player describes their reaction. "
         "Everyone commits, then the Warden resolves all actions at once, assigning Stat Checks and Saves. "
         "Damage and Wounds are resolved last. Then the next round begins.",

         "Насилие в Mothership невероятно опасно — избегайте его любой ценой. "
         "Во время столкновения время делится на раунды примерно по 10 секунд. "
         "Всё в раунде происходит одновременно.\n\n"
         "Варден описывает ситуацию, затем каждый игрок описывает реакцию своего персонажа. "
         "Все берут обязательства, после чего Варден разрешает все действия разом, "
         "назначая Проверки и Спасброски. Урон и Ранения разрешаются последними. "
         "Затем начинается следующий раунд.",

         "Насильство у Mothership надзвичайно небезпечне — уникайте його будь-якою ціною. "
         "Під час сутички час ділиться на раунди приблизно по 10 секунд. "
         "Усе в раунді відбувається одночасно.\n\n"
         "Варден описує ситуацію, потім кожен гравець описує реакцію свого персонажа. "
         "Всі беруть зобов'язання, після чого Варден розв'язує всі дії разом, "
         "призначаючи Перевірки та Порятунки. Шкода та Поранення розв'язуються останніми. "
         "Потім починається наступний раунд.",
     )},

    {"id": 24, "page": 3, "icon": "😱", "source_page": 26, "dice": None, "subinfo": None,
     "name":    ("Surprise",            "Внезапность",              "Раптовість"),
     "desc":    (
         "If there is a chance characters are ambushed or stunned by a horrific encounter, "
         "the Warden calls for a Fear Save. Those who succeed can react; those who fail are "
         "too shocked to act until the next round.\n\n"
         "Strict Turn Order: If preferred, everyone makes a Speed Check at the start of the encounter. "
         "Success means acting before the enemies; failure means acting after. "
         "Speed Checks can be called again if the situation changes dramatically.",

         "Если есть шанс, что персонажи окажутся в засаде или будут потрясены ужасной встречей, "
         "Варден требует Спасбросок Страха. Успех — можно действовать; провал — "
         "слишком потрясены, чтобы действовать до следующего раунда.\n\n"
         "Строгий порядок ходов: при желании все делают Проверку Скорости в начале схватки. "
         "Успех — ход до врагов; провал — ход после. "
         "Проверку можно вызвать снова при резком изменении ситуации.",

         "Якщо є шанс, що персонажів можуть застати в засідці або вони будуть приголомшені "
         "жахливою зустріччю, Варден вимагає Порятунок від Страху. "
         "Успіх — можна діяти; провал — занадто приголомшені для дій до наступного раунду.\n\n"
         "Суворий порядок ходів: за бажанням усі роблять Перевірку Швидкості на початку сутички. "
         "Успіх — хід до ворогів; провал — хід після. "
         "Перевірку можна викликати знову при різкій зміні ситуації.",
     )},

    {"id": 25, "page": 3, "icon": "❓", "source_page": 27, "dice": None, "subinfo": None,
     "name":    ("What Can I Do?",      "Что Я Могу Сделать?",      "Що Я Можу Зробити?"),
     "desc":    (
         "Characters can generally move to somewhere within Close Range and then do one thing "
         "before the situation changes.\n\n"
         "Things you can attempt in a round:\n"
         "• Attack something or someone\n"
         "• Bandage a wound\n"
         "• Check vital signs with a medscanner\n"
         "• Move again (up to Close Range)\n"
         "• Fire a vehicle's weapon\n"
         "• Maneuver or pilot a vehicle\n"
         "• Open an airlock\n"
         "• Operate a machine\n"
         "• Reload a weapon\n"
         "• Throw something at or to someone\n"
         "• Use a computer terminal\n\n"
         "If you do nothing but run, you can move within Long Range during the round.",

         "Персонажи обычно могут переместиться на Близкую Дистанцию и сделать одно действие "
         "до изменения ситуации.\n\n"
         "Что можно сделать за раунд:\n"
         "• Атаковать\n"
         "• Перевязать рану\n"
         "• Проверить жизненные показатели медсканером\n"
         "• Ещё раз переместиться (до Близкой Дистанции)\n"
         "• Выстрелить из оружия транспортного средства\n"
         "• Управлять транспортным средством\n"
         "• Открыть шлюз\n"
         "• Управлять машиной\n"
         "• Перезарядить оружие\n"
         "• Бросить что-то кому-то\n"
         "• Использовать компьютерный терминал\n\n"
         "Если только бежать — можно переместиться на Дальнюю Дистанцию за раунд.",

         "Персонажі зазвичай можуть переміститися на Близьку Дистанцію і зробити одну дію "
         "до зміни ситуації.\n\n"
         "Що можна зробити за раунд:\n"
         "• Атакувати\n"
         "• Перев'язати рану\n"
         "• Перевірити жизневі показники медсканером\n"
         "• Ще раз переміститися (до Близької Дистанції)\n"
         "• Вистрілити зі зброї транспортного засобу\n"
         "• Керувати транспортним засобом\n"
         "• Відкрити шлюз\n"
         "• Керувати машиною\n"
         "• Перезарядити зброю\n"
         "• Кинути щось комусь\n"
         "• Використати комп'ютерний термінал\n\n"
         "Якщо тільки бігти — можна переміститися на Далеку Дистанцію за раунд.",
     )},

    {"id": 26, "page": 3, "icon": "🎯", "source_page": 28, "dice": None, "subinfo": None,
     "name":    ("How Do I Attack?",    "Как Атаковать?",           "Як Атакувати?"),
     "desc":    (
         "Make a Combat Check. If successful, roll the weapon's Damage and subtract it from "
         "the enemy's Health. If you fail, the situation gets worse and you gain 1 Stress.",

         "Сделайте Проверку Боя. При успехе бросьте Урон оружия и вычтите из Здоровья врага. "
         "При провале ситуация ухудшается и вы получаете 1 Стресс.",

         "Зробіть Перевірку Бою. При успіху киньте Шкоду зброї і відніміть від Здоров'я ворога. "
         "При провалі ситуація погіршується і ви отримуєте 1 Стрес.",
     )},

    {"id": 27, "page": 3, "icon": "💥", "source_page": 28, "dice": None, "subinfo": None,
     "name":    ("Damage",              "Урон",                     "Шкода"),
     "desc":    (
         "When taking Damage (DMG), subtract it from Health. If your Health reaches zero, "
         "gain a Wound and roll on the Wounds Table. Reset Health to Maximum, then subtract "
         "any carryover damage. When a character suffers their Maximum Wounds, make a Death Save.",

         "При получении Урона вычтите его из Здоровья. Если Здоровье падает до нуля, "
         "получите Ранение и бросьте на Таблице Ранений. Сбросьте Здоровье до Максимума, "
         "вычтя остаточный урон. Когда персонаж получает Максимальное количество Ранений — "
         "совершите Спасбросок от Смерти.",

         "При отриманні Шкоди відніміть її від Здоров'я. Якщо Здоров'я падає до нуля, "
         "отримайте Поранення і киньте на Таблиці Поранень. Скиньте Здоров'я до Максимуму, "
         "відніміши залишкову шкоду. Коли персонаж отримує Максимальну кількість Поранень — "
         "зробіть Порятунок від Смерті.",
     )},

    {"id": 28, "page": 3, "icon": "🛡️", "source_page": 28, "dice": None, "subinfo": None,
     "name":    ("Armor",               "Броня",                    "Броня"),
     "desc":    (
         "Characters ignore all Damage less than their Armor Points (AP). If they take "
         "Damage ≥ AP in one hit, armor is destroyed and they suffer the remaining Damage.\n\n"
         "Weapons with Anti-Armor (AA) ignore and destroy armor on any hit.\n\n"
         "Damage Reduction (DR) always reduces incoming Damage by the stated amount — "
         "even if armor is destroyed or the weapon has AA. DR applies first, before Armor.",

         "Персонажи игнорируют весь Урон меньше Очков Брони (AP). Если за один удар "
         "Урон ≥ AP, броня уничтожается и персонаж получает остаточный урон.\n\n"
         "Оружие с Антибронью (AA) игнорирует и уничтожает броню при каждом попадании.\n\n"
         "Снижение Урона (DR) всегда уменьшает входящий Урон — даже если броня уничтожена "
         "или у оружия есть AA. DR применяется первым, до брони.",

         "Персонажі ігнорують всю Шкоду менше Очок Броні (AP). Якщо за один удар "
         "Шкода ≥ AP, броня знищується і персонаж отримує залишкову шкоду.\n\n"
         "Зброя з Антибронею (AA) ігнорує і знищує броню при кожному влученні.\n\n"
         "Зниження Шкоди (DR) завжди зменшує вхідну Шкоду — навіть якщо броня знищена "
         "або зброя має AA. DR застосовується першим, до броні.",
     )},

    {"id": 29, "page": 3, "icon": "🪨", "source_page": 28, "dice": None,
     "subinfo": [
         {"label_key": "cover_insignificant", "value": "AP 5",         "type": "stat"},
         {"label_key": "cover_light",         "value": "AP 10",        "type": "stat"},
         {"label_key": "cover_heavy",         "value": "DR 5 / AP 20", "type": "stat"},
     ],
     "name":    ("Cover",               "Укрытие",                  "Укриття"),
     "desc":    (
         "The environment can provide Cover. It is destroyed like armor when dealt "
         "Damage ≥ its AP. Cover typically protects only against ranged attacks. "
         "If you shoot while in Cover, you are out of Cover until your next turn.",

         "Окружение может давать Укрытие. Оно уничтожается как броня при Уроне ≥ его AP. "
         "Укрытие обычно защищает только от дальних атак. "
         "Если вы стреляете из Укрытия, то считаетесь вышедшим из него до своего следующего хода.",

         "Навколишнє середовище може давати Укриття. Воно знищується як броня при Шкоді ≥ його AP. "
         "Укриття зазвичай захищає лише від далекобійних атак. "
         "Якщо ви стріляєте з Укриття, вважаєтеся таким, що вийшов з нього до свого наступного ходу.",
     )},

    # ── P4: Wounds & Death ────────────────────────────────────────────────────

    {"id": 30, "page": 4, "icon": "🩹", "source_page": 29, "dice": None, "subinfo": None,
     "name":    ("What Are Wounds?",    "Что такое Ранения?",       "Що таке Поранення?"),
     "desc":    (
         "When gaining a Wound, roll 1d10 on the Wounds Table for the type of Damage received:\n\n"
         "• Blunt Force — punched, hit with crowbar or thrown object, falling\n"
         "• Bleeding — stabbed or cut\n"
         "• Gunshot — shot by a firearm\n"
         "• Fire & Explosives — grenades, flamethrowers, set on fire\n"
         "• Gore & Massive — giant or gruesome attacks\n\n"
         "Severity guide:\n"
         "• Flesh Wound — small inconvenience\n"
         "• Minor / Major Injury — lasting issues requiring medical treatment\n"
         "• Lethal Injury — Death Save in 1d10 rounds\n"
         "• Fatal Injury — Death Save immediately",

         "При получении Ранения бросьте 1d10 на Таблице Ранений для типа полученного Урона:\n\n"
         "• Тупой удар — удар кулаком, монтировкой или брошенным предметом, падение\n"
         "• Кровотечение — удар ножом или порез\n"
         "• Огнестрел — выстрел из огнестрельного оружия\n"
         "• Огонь и взрывы — гранаты, огнемёты, поджог\n"
         "• Расчленение — гигантские или жуткие атаки\n\n"
         "Степень тяжести:\n"
         "• Царапина — небольшое неудобство\n"
         "• Лёгкая / Тяжёлая травма — продолжительные проблемы, требующие лечения\n"
         "• Смертельная травма — Спасбросок от Смерти через 1d10 раундов\n"
         "• Фатальная травма — Спасбросок от Смерти немедленно",

         "При отриманні Поранення киньте 1d10 на Таблиці Поранень для типу отриманої Шкоди:\n\n"
         "• Тупий удар — удар кулаком, монтировкою або кинутим предметом, падіння\n"
         "• Кровотеча — удар ножем або порізання\n"
         "• Вогнепальне — постріл з вогнепальної зброї\n"
         "• Вогонь та вибухи — гранати, вогнемети, підпал\n"
         "• Масивний урон — гігантські або жахливі атаки\n\n"
         "Ступінь тяжкості:\n"
         "• Подряпина — невелике незручність\n"
         "• Легка / Важка травма — тривалі проблеми, що потребують лікування\n"
         "• Смертельна травма — Порятунок від Смерті через 1d10 раундів\n"
         "• Фатальна травма — Порятунок від Смерті негайно",
     )},

    {"id": 31, "page": 4, "icon": "🎲", "source_page": 29,
     "subinfo": [{"label_key": "wound_type", "value": "Blunt Force", "type": "stat"}],
     "dice": {"die": "d10", "entries": [
         {"min": 0, "max": 0, "text": "Flesh Wound. Knocked down."},
         {"min": 1, "max": 1, "text": "Winded. [-] until you catch your breath."},
         {"min": 2, "max": 2, "text": "Minor Injury. Sprained Ankle. [-] on Speed Checks."},
         {"min": 3, "max": 3, "text": "Concussion. [-] on mental tasks."},
         {"min": 4, "max": 4, "text": "Leg or foot broken. [-] on Speed Checks."},
         {"min": 5, "max": 5, "text": "Major Injury. Arm or hand broken. [-] on manual tasks."},
         {"min": 6, "max": 6, "text": "Snapped collarbone. [-] on Strength Checks."},
         {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Back broken. [-] on all rolls."},
         {"min": 8, "max": 8, "text": "Skull fracture. [-] on all rolls."},
         {"min": 9, "max": 9, "text": "Fatal Injury. Spine or neck broken. Death Save."},
     ]},
     "name":    ("Wounds — Blunt Force",    "Ранения — Тупой Удар",     "Поранення — Тупий Удар"),
     "desc":    (
         "Roll when you are punched, hit with a crowbar or thrown object, or fall.",
         "Бросьте при ударе кулаком, монтировкой, брошенным предметом или при падении.",
         "Киньте при ударі кулаком, монтировкою, кинутим предметом або при падінні.",
     )},

    {"id": 32, "page": 4, "icon": "🎲", "source_page": 29,
     "subinfo": [{"label_key": "wound_type", "value": "Bleeding", "type": "stat"}],
     "dice": {"die": "d10", "entries": [
         {"min": 0, "max": 0, "text": "Flesh Wound. Drop held item."},
         {"min": 1, "max": 1, "text": "Lots of blood. Those Close gain 1 Stress."},
         {"min": 2, "max": 2, "text": "Minor Injury. Blood in eyes. [-] until wiped clean."},
         {"min": 3, "max": 3, "text": "Laceration. Bleeding +1."},
         {"min": 4, "max": 4, "text": "Major cut. Bleeding +2."},
         {"min": 5, "max": 5, "text": "Major Injury. Fingers/toes severed. Bleeding +3."},
         {"min": 6, "max": 6, "text": "Hand/foot severed. Bleeding +4."},
         {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Limb severed. Bleeding +5."},
         {"min": 8, "max": 8, "text": "Major artery cut. Bleeding +6."},
         {"min": 9, "max": 9, "text": "Fatal Injury. Throat slit or heart pierced. Death Save."},
     ]},
     "name":    ("Wounds — Bleeding",       "Ранения — Кровотечение",   "Поранення — Кровотеча"),
     "desc":    (
         "Roll when you are stabbed or cut.",
         "Бросьте при ударе ножом или порезе.",
         "Киньте при ударі ножем або порізанні.",
     )},

    {"id": 33, "page": 4, "icon": "🎲", "source_page": 29,
     "subinfo": [{"label_key": "wound_type", "value": "Gunshot", "type": "stat"}],
     "dice": {"die": "d10", "entries": [
         {"min": 0, "max": 0, "text": "Flesh Wound. Grazed. Knocked down."},
         {"min": 1, "max": 1, "text": "Bleeding +1."},
         {"min": 2, "max": 2, "text": "Minor Injury. Broken rib."},
         {"min": 3, "max": 3, "text": "Fractured extremity."},
         {"min": 4, "max": 4, "text": "Internal bleeding. Bleeding +2."},
         {"min": 5, "max": 5, "text": "Major Injury. Lodged bullet. Surgery required."},
         {"min": 6, "max": 6, "text": "Gunshot wound to the neck."},
         {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Major blood loss. Bleeding +4."},
         {"min": 8, "max": 8, "text": "Sucking chest wound. Bleeding +5."},
         {"min": 9, "max": 9, "text": "Fatal Injury. Headshot. Death Save."},
     ]},
     "name":    ("Wounds — Gunshot",        "Ранения — Огнестрел",      "Поранення — Вогнепальне"),
     "desc":    (
         "Roll when you are shot by a firearm.",
         "Бросьте при попадании огнестрельного оружия.",
         "Киньте при влученні вогнепальної зброї.",
     )},

    {"id": 34, "page": 4, "icon": "🎲", "source_page": 29,
     "subinfo": [{"label_key": "wound_type", "value": "Fire & Explosives", "type": "stat"}],
     "dice": {"die": "d10", "entries": [
         {"min": 0, "max": 0, "text": "Flesh Wound. Hair burnt. Gain 1d5 Stress."},
         {"min": 1, "max": 1, "text": "Awesome scar. +1 Minimum Stress."},
         {"min": 2, "max": 2, "text": "Minor Injury. Singed. [-] on next action."},
         {"min": 3, "max": 3, "text": "Shrapnel / large burn."},
         {"min": 4, "max": 4, "text": "Extensive burns."},
         {"min": 5, "max": 5, "text": "Major Injury. Major Burn. -2d10 Body Save."},
         {"min": 6, "max": 6, "text": "Skin grafts required. -2d10 Body Save."},
         {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Limb on fire. 2d10 Damage per round."},
         {"min": 8, "max": 8, "text": "Body on fire. 3d10 Damage per round."},
         {"min": 9, "max": 9, "text": "Fatal Injury. Engulfed in fiery explosion. Death Save."},
     ]},
     "name":    ("Wounds — Fire & Explosives", "Ранения — Огонь и Взрывы", "Поранення — Вогонь та Вибухи"),
     "desc":    (
         "Roll when hit by grenades, flamethrowers, or set on fire.",
         "Бросьте при попадании гранаты, огнемёта или поджоге.",
         "Киньте при влученні гранати, вогнемета або підпалу.",
     )},

    {"id": 35, "page": 4, "icon": "🎲", "source_page": 29,
     "subinfo": [{"label_key": "wound_type", "value": "Gore & Massive", "type": "stat"}],
     "dice": {"die": "d10", "entries": [
         {"min": 0, "max": 0, "text": "Flesh Wound. Vomit. [-] on next action."},
         {"min": 1, "max": 1, "text": "Awesome scar. +1 Minimum Stress."},
         {"min": 2, "max": 2, "text": "Minor Injury. Digit mangled."},
         {"min": 3, "max": 3, "text": "Eyes gouged out."},
         {"min": 4, "max": 4, "text": "Ripped off flesh. -1d10 Strength."},
         {"min": 5, "max": 5, "text": "Major Injury. Paralyzed waist down."},
         {"min": 6, "max": 6, "text": "Limb severed. Bleeding +5."},
         {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Impaled. Bleeding +6."},
         {"min": 8, "max": 8, "text": "Guts spooled on floor. Bleeding +7."},
         {"min": 9, "max": 9, "text": "Fatal Injury. Head explodes. No Death Save. You have died."},
     ]},
     "name":    ("Wounds — Gore & Massive",  "Ранения — Расчленение",    "Поранення — Масивний урон"),
     "desc":    (
         "Roll when hit by a giant creature or a gruesome, massive attack.",
         "Бросьте при атаке гигантского существа или чудовищном ударе.",
         "Киньте при атаці гігантської істоти або при масивному ударі.",
     )},

    {"id": 36, "page": 4, "icon": "💀", "source_page": 29, "subinfo": None,
     "dice": {"die": "d10", "entries": [
         {"min": 0, "max": 0, "text": "Unconscious. Wake up in 2d10 minutes. Reduce Maximum Health by 1d5."},
         {"min": 1, "max": 2, "text": "Unconscious and dying. You die in 1d5 rounds without intervention."},
         {"min": 3, "max": 4, "text": "Comatose. Only extraordinary measures can return you to the waking world."},
         {"min": 5, "max": 9, "text": "You have died. Roll up a new character."},
     ]},
     "name":    ("Death Table",             "Таблица Смерти",           "Таблиця Смерті"),
     "desc":    (
         "When you die, the Warden places 1d10 in a cup, shakes it, and places it face down on the table. "
         "As soon as someone spends a turn checking your vitals, the die is revealed.",

         "Когда вы умираете, Варден кладёт 1d10 в стакан, трясёт его и кладёт перевёрнутым на стол. "
         "Как только кто-то тратит ход на проверку ваших жизненных показателей, кубик открывается.",

         "Коли ви вмираєте, Варден кладе 1d10 у стакан, трясе його і кладе перевернутим на стіл. "
         "Щойно хтось витрачає хід на перевірку ваших жизневих показників, кубик відкривається.",
     )},

    # ── P5: Range & Distance ─────────────────────────────────────────────────

    {"id": 37, "page": 5, "icon": "👁️", "source_page": 30, "dice": None, "subinfo": None,
     "name":    ("Adjacent",            "Рядом",                    "Поруч"),
     "desc":    (
         "You're basically touching. Covers fist fights, close-quarters combat, and trying to escape "
         "a creature's claws. Also covers using a computer terminal or administering first aid. "
         "You can talk, whisper, and even smell someone at this range.\n\nLess than 1m / 3ft.",

         "Вы практически касаетесь друг друга. Это рукопашный бой, попытки вырваться из когтей "
         "чудовища, использование компьютерного терминала или оказание первой помощи. "
         "На этой дистанции можно говорить, шептать и даже учуять запах.\n\nМенее 1м / 3 фута.",

         "Ви практично торкаєтеся одне одного. Це рукопашний бій, спроби вирватися з кігтів "
         "монстра, використання комп'ютерного терміналу або надання першої допомоги. "
         "На цій дистанції можна говорити, шептати і навіть відчути запах.\n\nМенше 1м / 3 фути.",
     )},

    {"id": 38, "page": 5, "icon": "🏃", "source_page": 31, "dice": None, "subinfo": None,
     "name":    ("Close Range",         "Близкая Дистанция",        "Близька Дистанція"),
     "desc":    (
         "Someone Close can be reached by running over to them in a few seconds. Near enough that "
         "you could throw something at them and hit them. You'd have to speak loud enough that someone "
         "on the other side of the room could hear you. Powerful stenches can be smelled. "
         "Firearms like shotguns are most effective at this range or Adjacent.",

         "На Близкой Дистанции можно добраться до кого-то за несколько секунд. Достаточно близко, "
         "чтобы бросить в него что-то и попасть. Нужно говорить достаточно громко, чтобы вас "
         "слышали на другом конце комнаты. Сильные запахи ощущаются на этой дистанции. "
         "Дробовики наиболее эффективны на Близкой Дистанции или Рядом.",

         "На Близькій Дистанції можна дістатися до когось за кілька секунд. Досить близько, "
         "щоб кинути в нього щось і влучити. Треба говорити досить голосно, щоб вас чули "
         "на іншому кінці кімнати. Сильні запахи відчуваються на цій дистанції. "
         "Дробовики найбільш ефективні на Близькій Дистанції або Поруч.",
     )},

    {"id": 39, "page": 5, "icon": "🔭", "source_page": 31, "dice": None, "subinfo": None,
     "name":    ("Long Range",          "Дальняя Дистанция",        "Далека Дистанція"),
     "desc":    (
         "Things in this band are far enough away that they take an entire round or longer to reach. "
         "Rifles are effective at this range, but handguns and shotguns less so. "
         "You'd have to yell to get someone's attention, and you won't smell anyone, no matter how bad they stink.",

         "На Дальней Дистанции враг настолько далеко, что добраться до него займёт целый раунд или дольше. "
         "Винтовки эффективны на этой дистанции, но пистолеты и дробовики — меньше. "
         "Чтобы привлечь внимание, нужно кричать; запах на этой дистанции не ощутить.",

         "На Далекій Дистанції ворог настільки далеко, що дістатися до нього займе цілий раунд або більше. "
         "Гвинтівки ефективні на цій дистанції, але пістолети та дробовики — менше. "
         "Щоб привернути увагу, треба кричати; запах на цій дистанції не відчути.",
     )},

    {"id": 40, "page": 5, "icon": "🌌", "source_page": 31, "dice": None, "subinfo": None,
     "name":    ("Extreme Range",       "Крайняя Дистанция",        "Крайня Дистанція"),
     "desc":    (
         "Only the longest range weapons, like smart rifles, can hit accurately at this distance. "
         "It takes more than one round to reach something here. Even if you hear a scream "
         "you might not know which direction it's coming from.\n\nMore than 100m / 300ft.",

         "Только оружие с максимальной дальностью, как умная винтовка, может точно поразить цель "
         "на этой дистанции. Добраться сюда займёт больше одного раунда. "
         "Даже услышав крик, вы можете не понять, откуда он доносится.\n\nБолее 100м / 300 футов.",

         "Лише зброя з максимальною дальністю, як розумна гвинтівка, може точно вразити ціль "
         "на цій дистанції. Дістатися сюди займе більше одного раунду. "
         "Навіть почувши крик, ви можете не зрозуміти, звідки він лунає.\n\nБільше 100м / 300 футів.",
     )},
]


# ── Content links ─────────────────────────────────────────────────────────────

CONTENT_LINKS = [
    # (from_id, to_id, label_key, sort_order)
    (26, 29, "related",  0),   # How Do I Attack? → Cover
    (26, 27, "related",  1),   # How Do I Attack? → Damage
    (27, 30, "related",  0),   # Damage → What Are Wounds?
    (30, 31, "see_also", 0),   # What Are Wounds? → Blunt Force table
    (30, 32, "see_also", 1),   # What Are Wounds? → Bleeding table
    (30, 33, "see_also", 2),   # What Are Wounds? → Gunshot table
    (30, 34, "see_also", 3),   # What Are Wounds? → Fire & Explosives table
    (30, 35, "see_also", 4),   # What Are Wounds? → Gore & Massive table
    (30, 36, "see_also", 5),   # What Are Wounds? → Death Table
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    """Add child_id to parent's linked_pages JSON array if not already present."""
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


# ── Seed ──────────────────────────────────────────────────────────────────────

def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(CONTENTS)} contents, {len(PAGES)} pages, "
              f"{len(CONTENT_LINKS)} links seeded into '{DB_PATH}'.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    conn.execute("""
        INSERT OR IGNORE INTO sources (id, slug, title, type)
        VALUES (1, 'psg', 'Player''s Survival Guide', 'core')
    """)

    # ── Pages ─────────────────────────────────────────────────────────────────
    for (pid, icon, src_page,
         name_en, name_ru, name_ua,
         desc_en, desc_ru, desc_ua) in PAGES:

        conn.execute("""
            INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
            VALUES (?, ?, 'psg', ?, '[]')
        """, (pid, icon, src_page))

        descs = {"en": desc_en, "ru": desc_ru, "ua": desc_ua}
        names = {"en": name_en, "ru": name_ru, "ua": name_ua}
        for lang in ("en", "ru", "ua"):
            conn.execute("""
                INSERT OR IGNORE INTO page_i18n (page_id, lang, name, desc)
                VALUES (?, ?, ?, ?)
            """, (pid, lang, names[lang], descs[lang]))

    # Add new top-level pages to P1 without overwriting pages from other scripts
    for pid in (3, 4, 5):
        _add_linked_page(conn, parent_id=1, child_id=pid)

    # ── Contents ──────────────────────────────────────────────────────────────
    content_ids = [c["id"] for c in CONTENTS]
    conn.execute(
        f"DELETE FROM contents WHERE id IN ({','.join('?'*len(content_ids))})",
        content_ids,
    )

    for idx, c in enumerate(CONTENTS):
        cid       = c["id"]
        dice_json = json.dumps(c["dice"]) if c["dice"] else None
        sub_json  = json.dumps(c["subinfo"]) if c["subinfo"] else None

        conn.execute("""
            INSERT INTO contents
                (id, icon, source_slug, source_page, dice, subinfo_fixed, sort_order)
            VALUES (?, ?, 'psg', ?, ?, ?, ?)
        """, (cid, c["icon"], c["source_page"], dice_json, sub_json, idx))

        name_en, name_ru, name_ua = c["name"]
        desc_en, desc_ru, desc_ua = c["desc"]
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
            INSERT INTO page_contents (page_id, content_id, sort_order)
            VALUES (?, ?, ?)
        """, (c["page"], cid, idx))

    # ── Content links ─────────────────────────────────────────────────────────
    for from_id, to_id, label_key, sort in CONTENT_LINKS:
        conn.execute("""
            INSERT OR IGNORE INTO content_links
                (from_content_id, to_content_id, label_key, sort_order)
            VALUES (?, ?, ?, ?)
        """, (from_id, to_id, label_key, sort))


if __name__ == "__main__":
    run()
