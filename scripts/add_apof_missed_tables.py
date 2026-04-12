"""
scripts/add_apof_missed_tables.py
A Pound of Flesh — missed rollable tables:
  - Update C217 (Infection Rules) with Infection Table dice
  - C326 Cybernetic Mutations (d100, back cover)
  - C327 Random Search (d100, back cover)
  - C328 Noteworthy Locations — Refuel/Repair (d100, pg. 50-51)
  - C329 Dry Dock Rumors (d10, pg. 10)
  - C330 Ships Currently Docked (d10, pg. 11)
  - C331 Jobs for The Babushka (d10, pg. 14)
  - C332 The Docket (d10, pg. 26)
  - C333 Accused & What They Can Pay (d10, pg. 27)
  - C334 Noteworthy Locations — Port/Market (d100, pg. 50-51)
  - C335 Noteworthy Locations — Colony/Habitat (d100, pg. 50-51)
  - C336 Noteworthy Locations — Military (d100, pg. 50-51)
  - C337 Noteworthy Locations — Mining/Factory (d100, pg. 50-51)
  - C338 Noteworthy Locations — Corporate/Research (d100, pg. 50-51)
  - C339 Noteworthy Locations — Prison (d100, pg. 50-51)
  - C340 Noteworthy Locations — Religious (d100, pg. 50-51)
Run: python scripts/add_apof_missed_tables.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ---------------------------------------------------------------------------
# C217 — Infection Table dice (added to existing "Infection Rules" content)
# ---------------------------------------------------------------------------
INFECTION_TABLE_ENTRIES = [
    {"min": 1, "max": 1, "text": "Weak Immune System. All Body Saves are at [-]."},
    {"min": 2, "max": 2, "text": "Once/day make a Body Save or go into a coughing fit for 1d5 rounds. Anyone within 10m must make an Infection Check."},
    {"min": 3, "max": 3, "text": "Fever & Chills. Take 1d10 damage per day."},
    {"min": 4, "max": 4, "text": "Random Mutation — roll on Cybernetic Mutations table."},
    {"min": 5, "max": 5, "text": "Frailty. All Strength & Speed Checks at [-]. Roll a Mutation."},
    {"min": 6, "max": 6, "text": "2d10 damage per day. Random Malfunction — roll on Cybermod Malfunctions."},
    {"min": 7, "max": 7, "text": "Panic Check. [+] on Reaping Checks until cured. Roll a Mutation."},
    {"min": 8, "max": 8, "text": "Install 1 cybermod per week or gain 2d10 Stress. Roll a Mutation."},
    {"min": 9, "max": 9, "text": "Once/day make a Body Save or spew an infectious Nanoswarm. All within 20m make an Infection Check at [-]. Roll a Mutation."},
    {"min": 10, "max": 10, "text": "Lose control of your PC and transform into Chokespawn."},
]

INFECTION_TABLE_RU = [
    {"min": 1, "max": 1, "text": "Слабый иммунитет. Все Спасброски Тела со штрафом [-]."},
    {"min": 2, "max": 2, "text": "Раз/день — Спасбросок Тела или кашель 1d5 раундов. Все в 10м должны пройти Проверку Инфекции."},
    {"min": 3, "max": 3, "text": "Жар и озноб. Получать 1d10 урона в день."},
    {"min": 4, "max": 4, "text": "Случайная Мутация — см. таблицу Кибернетических Мутаций."},
    {"min": 5, "max": 5, "text": "Немощь. Все Проверки Силы и Скорости со штрафом [-]. Бросить Мутацию."},
    {"min": 6, "max": 6, "text": "2d10 урона в день. Случайная Неисправность — см. таблицу Неисправностей Кибермодов."},
    {"min": 7, "max": 7, "text": "Проверка Паники. [+] на Проверки Жатвы до излечения. Бросить Мутацию."},
    {"min": 8, "max": 8, "text": "Устанавливать 1 кибермод в неделю или получать 2d10 Стресса. Бросить Мутацию."},
    {"min": 9, "max": 9, "text": "Раз/день — Спасбросок Тела или выброс заразного Нанороя. Все в 20м проходят Проверку Инфекции со штрафом [-]. Бросить Мутацию."},
    {"min": 10, "max": 10, "text": "Потеря контроля над персонажем — превращение в Чокспауна."},
]

INFECTION_TABLE_UA = [
    {"min": 1, "max": 1, "text": "Слабкий імунітет. Усі Рятівні Тіла зі штрафом [-]."},
    {"min": 2, "max": 2, "text": "Раз/день — Рятівний Тіла або кашель 1d5 раундів. Усі в 10м повинні пройти Перевірку Інфекції."},
    {"min": 3, "max": 3, "text": "Жар і озноб. Отримувати 1d10 шкоди на день."},
    {"min": 4, "max": 4, "text": "Випадкова Мутація — див. таблицю Кібернетичних Мутацій."},
    {"min": 5, "max": 5, "text": "Кволість. Усі Перевірки Сили та Швидкості зі штрафом [-]. Кинути Мутацію."},
    {"min": 6, "max": 6, "text": "2d10 шкоди на день. Випадкова Несправність — див. таблицю Несправностей Кібермодів."},
    {"min": 7, "max": 7, "text": "Перевірка Паніки. [+] на Перевірки Жнив до одужання. Кинути Мутацію."},
    {"min": 8, "max": 8, "text": "Встановлювати 1 кіберМод на тиждень або отримувати 2d10 Стресу. Кинути Мутацію."},
    {"min": 9, "max": 9, "text": "Раз/день — Рятівний Тіла або викид заразного Нанорою. Усі в 20м проходять Перевірку Інфекції зі штрафом [-]. Кинути Мутацію."},
    {"min": 10, "max": 10, "text": "Втрата контролю над персонажем — перетворення на Чокспауна."},
]

# ---------------------------------------------------------------------------
# C326 — Cybernetic Mutations (d100, back cover)
# ---------------------------------------------------------------------------
CYBERNETIC_MUTATIONS_EN = [
    {"min": 0,  "max": 0,  "text": "Teeth enlarged and coated in metal alloy."},
    {"min": 1,  "max": 4,  "text": "Fingers lengthen. Fingernails turn into circuit boards."},
    {"min": 5,  "max": 9,  "text": "Eyes turn black. Wires spread from irises across face."},
    {"min": 10, "max": 14, "text": "Voice loses its human quality. Now choral and robotic."},
    {"min": 15, "max": 19, "text": "All hair falls out, tubing protrudes from back of skull."},
    {"min": 20, "max": 24, "text": "Vestigial synthetic appendage grows from ribcage."},
    {"min": 25, "max": 29, "text": "Tangle of wires weave through your abdomen."},
    {"min": 30, "max": 34, "text": "Metallic spinal column extrudes and pierces skin."},
    {"min": 35, "max": 39, "text": "Limb consumed by mods. Misshapen metal mass."},
    {"min": 40, "max": 44, "text": "Metallic fingers sprout from limb."},
    {"min": 45, "max": 49, "text": "Hand permanently fuses with equipped weapon."},
    {"min": 50, "max": 54, "text": "Semi-organic vents form in underarms and neck."},
    {"min": 55, "max": 59, "text": "Insectile eyes cluster across your face."},
    {"min": 60, "max": 64, "text": "Tongue grows 6 times normal length. Constant drool."},
    {"min": 65, "max": 69, "text": "Neck grows an extra foot and is sheathed in metal."},
    {"min": 70, "max": 73, "text": "Heavy organic sac swells across your hunchback."},
    {"min": 74, "max": 75, "text": "Neck vents grow and emit periodic exhaust fumes."},
    {"min": 76, "max": 77, "text": "Half of face melts away revealing metal skull."},
    {"min": 78, "max": 79, "text": "Spiked prongs extrude from your shoulders."},
    {"min": 80, "max": 80, "text": "Patch of 2d10 synthetic eyes grow out of your back."},
    {"min": 81, "max": 81, "text": "Arms grow until your hands touch the floor and drag."},
    {"min": 82, "max": 82, "text": "Metallic, wiry antlers grow from your skull."},
    {"min": 83, "max": 83, "text": "Second face grows out of your chest."},
    {"min": 84, "max": 84, "text": "Mouths form in the palms of your hands."},
    {"min": 85, "max": 85, "text": "Hair turns to thick black wires, always seeking ports."},
    {"min": 86, "max": 86, "text": "Fingers fuse together and turn into metal claws."},
    {"min": 87, "max": 87, "text": "Mouth splits into impossibly wide smile. Metal throat."},
    {"min": 88, "max": 88, "text": "Spines grow out of your arm bones."},
    {"min": 89, "max": 89, "text": "Your skin becomes a liquid metal surface."},
    {"min": 90, "max": 90, "text": "Hoses grow from your torso and drag along the floor."},
    {"min": 91, "max": 91, "text": "The features of your face constantly drip and shift."},
    {"min": 92, "max": 92, "text": "Sensitive antennae grow from your skull."},
    {"min": 93, "max": 93, "text": "Your skin grows a tiny swarm of metal tentacles."},
    {"min": 94, "max": 94, "text": "Prehensile tail of wire and bone."},
    {"min": 95, "max": 95, "text": "Entire body becomes a shifting swarm of nanobots."},
    {"min": 96, "max": 96, "text": "Keyboard keys sprout from your arms."},
    {"min": 97, "max": 97, "text": "A small person grows out of your torso."},
    {"min": 98, "max": 98, "text": "All your skin sloughs off to reveal a metal skeleton."},
    {"min": 99, "max": 99, "text": "Roll twice and combine."},
]

CYBERNETIC_MUTATIONS_RU = [
    {"min": 0,  "max": 0,  "text": "Зубы увеличились и покрылись металлическим сплавом."},
    {"min": 1,  "max": 4,  "text": "Пальцы удлинились. Ногти стали платами."},
    {"min": 5,  "max": 9,  "text": "Глаза почернели. Провода расходятся от радужек по лицу."},
    {"min": 10, "max": 14, "text": "Голос потерял человеческое звучание — теперь хоровой и роботизированный."},
    {"min": 15, "max": 19, "text": "Все волосы выпали, из затылка торчат трубки."},
    {"min": 20, "max": 24, "text": "Из рёбер вырастает рудиментарный синтетический отросток."},
    {"min": 25, "max": 29, "text": "Клубок проводов оплёл ваш живот."},
    {"min": 30, "max": 34, "text": "Металлический позвоночник выдвигается и пробивает кожу."},
    {"min": 35, "max": 39, "text": "Конечность поглощена модами. Бесформенная металлическая масса."},
    {"min": 40, "max": 44, "text": "Из конечности прорастают металлические пальцы."},
    {"min": 45, "max": 49, "text": "Рука навсегда сросла с экипированным оружием."},
    {"min": 50, "max": 54, "text": "В подмышках и на шее появились полуорганические вентиляционные отверстия."},
    {"min": 55, "max": 59, "text": "По лицу гроздьями рассыпались глаза-фасетки."},
    {"min": 60, "max": 64, "text": "Язык вырос в 6 раз. Постоянное слюноотделение."},
    {"min": 65, "max": 69, "text": "Шея выросла на полметра и закована в металл."},
    {"min": 70, "max": 73, "text": "На горбу разбухает тяжёлый органический мешок."},
    {"min": 74, "max": 75, "text": "Шейные вентиляционные отверстия росли и периодически выбрасывают выхлоп."},
    {"min": 76, "max": 77, "text": "Половина лица расплавилась, обнажив металлический череп."},
    {"min": 78, "max": 79, "text": "Из плеч торчат шипастые зубцы."},
    {"min": 80, "max": 80, "text": "На спине вырастает пятно из 2d10 синтетических глаз."},
    {"min": 81, "max": 81, "text": "Руки выросли так, что руки волочатся по полу."},
    {"min": 82, "max": 82, "text": "Из черепа выросли металлические проволочные рога."},
    {"min": 83, "max": 83, "text": "Второе лицо выросло из груди."},
    {"min": 84, "max": 84, "text": "На ладонях появились рты."},
    {"min": 85, "max": 85, "text": "Волосы стали толстой чёрной проволокой, ищущей разъёмы."},
    {"min": 86, "max": 86, "text": "Пальцы срослись и превратились в металлические когти."},
    {"min": 87, "max": 87, "text": "Рот растянулся в невозможно широкую ухмылку. Металлическое горло."},
    {"min": 88, "max": 88, "text": "Из костей рук проросли шипы."},
    {"min": 89, "max": 89, "text": "Кожа стала жидкометаллической поверхностью."},
    {"min": 90, "max": 90, "text": "Из торса вырастают шланги и волочатся по полу."},
    {"min": 91, "max": 91, "text": "Черты лица постоянно стекают и смещаются."},
    {"min": 92, "max": 92, "text": "Из черепа выросли чувствительные антенны."},
    {"min": 93, "max": 93, "text": "Кожа покрылась крошечным роем металлических щупалец."},
    {"min": 94, "max": 94, "text": "Хвост из проволоки и кости."},
    {"min": 95, "max": 95, "text": "Всё тело стало движущимся роем нанороботов."},
    {"min": 96, "max": 96, "text": "Из рук проросли клавиши клавиатуры."},
    {"min": 97, "max": 97, "text": "Из торса вырастает маленький человек."},
    {"min": 98, "max": 98, "text": "Вся кожа слезла, обнажив металлический скелет."},
    {"min": 99, "max": 99, "text": "Бросьте дважды и объедините."},
]

CYBERNETIC_MUTATIONS_UA = [
    {"min": 0,  "max": 0,  "text": "Зуби збільшились і вкрились металевим сплавом."},
    {"min": 1,  "max": 4,  "text": "Пальці видовжились. Нігті стали платами."},
    {"min": 5,  "max": 9,  "text": "Очі почорніли. Проводи розходяться від райдужок по обличчю."},
    {"min": 10, "max": 14, "text": "Голос втратив людське звучання — тепер хоровий і роботизований."},
    {"min": 15, "max": 19, "text": "Все волосся випало, з потилиці стирчать трубки."},
    {"min": 20, "max": 24, "text": "З ребер виростає рудиментарний синтетичний відросток."},
    {"min": 25, "max": 29, "text": "Клубок проводів обплів ваш живіт."},
    {"min": 30, "max": 34, "text": "Металевий хребет висувається і пробиває шкіру."},
    {"min": 35, "max": 39, "text": "Кінцівка поглинута модами. Безформна металева маса."},
    {"min": 40, "max": 44, "text": "З кінцівки проростають металеві пальці."},
    {"min": 45, "max": 49, "text": "Рука назавжди зрослась з екіпірованою зброєю."},
    {"min": 50, "max": 54, "text": "У пахвах і на шиї з'явились напівorganic вентиляційні отвори."},
    {"min": 55, "max": 59, "text": "По обличчю гронами розсипались очі-фасетки."},
    {"min": 60, "max": 64, "text": "Язик виріс у 6 разів. Постійне слиновиділення."},
    {"min": 65, "max": 69, "text": "Шия виросла на пів метра і закована в метал."},
    {"min": 70, "max": 73, "text": "На горбі розбухає важкий органічний мішок."},
    {"min": 74, "max": 75, "text": "Шийні вентиляційні отвори виросли й periodично викидають вихлоп."},
    {"min": 76, "max": 77, "text": "Половина обличчя розплавилась, оголивши металевий череп."},
    {"min": 78, "max": 79, "text": "З плечей стирчать шипасті зубці."},
    {"min": 80, "max": 80, "text": "На спині виростає пляма з 2d10 синтетичних очей."},
    {"min": 81, "max": 81, "text": "Руки виросли так, що волочаться по підлозі."},
    {"min": 82, "max": 82, "text": "З черепа виросли металеві дротяні роги."},
    {"min": 83, "max": 83, "text": "Друге обличчя виросло з грудей."},
    {"min": 84, "max": 84, "text": "На долонях з'явились роти."},
    {"min": 85, "max": 85, "text": "Волосся стало товстим чорним дротом, що шукає роз'єми."},
    {"min": 86, "max": 86, "text": "Пальці зрослись і перетворились на металеві кігті."},
    {"min": 87, "max": 87, "text": "Рот розтягнувся в неможливо широку посмішку. Металеве горло."},
    {"min": 88, "max": 88, "text": "З кісток рук проросли шипи."},
    {"min": 89, "max": 89, "text": "Шкіра стала рідкометалевою поверхнею."},
    {"min": 90, "max": 90, "text": "З тулуба виростають шланги і волочаться по підлозі."},
    {"min": 91, "max": 91, "text": "Риси обличчя постійно стікають і зміщуються."},
    {"min": 92, "max": 92, "text": "З черепа виросли чутливі антени."},
    {"min": 93, "max": 93, "text": "Шкіра вкрилась крихітним роєм металевих щупалець."},
    {"min": 94, "max": 94, "text": "Хвіст з дроту і кістки."},
    {"min": 95, "max": 95, "text": "Все тіло стало рухомим роєм нанороботів."},
    {"min": 96, "max": 96, "text": "З рук проросли клавіші клавіатури."},
    {"min": 97, "max": 97, "text": "З тулуба виростає маленька людина."},
    {"min": 98, "max": 98, "text": "Вся шкіра злізла, оголивши металевий скелет."},
    {"min": 99, "max": 99, "text": "Кидайте двічі та поєднуйте."},
]

# ---------------------------------------------------------------------------
# C327 — Random Search (d100, back cover)
# ---------------------------------------------------------------------------
RANDOM_SEARCH_EN = [
    {"min": 0,  "max": 0,  "text": "Credstick without ID. 1d100×100cr."},
    {"min": 1,  "max": 4,  "text": "Credstick ID'd to victim. 1d100×10cr."},
    {"min": 5,  "max": 9,  "text": "VIP invite to gamble in Heaven."},
    {"min": 10, "max": 14, "text": "Fake rubber revolver. Looks pretty realistic."},
    {"min": 15, "max": 19, "text": "Functioning synthpet."},
    {"min": 20, "max": 24, "text": "Metallic folding fan."},
    {"min": 25, "max": 29, "text": 'Leather jacket. "Суки Любят Острый Нож" on back.'},
    {"min": 30, "max": 34, "text": "Bundle of ×5 Stimpacks and ×4 Automeds."},
    {"min": 35, "max": 39, "text": "Empty O2 tank."},
    {"min": 40, "max": 44, "text": "Dried Meatapede."},
    {"min": 45, "max": 49, "text": "Bracelet with flashing colored lights."},
    {"min": 50, "max": 54, "text": "Flask of station hooch."},
    {"min": 55, "max": 59, "text": "Artisanal chocolate (relieves 2 Stress)."},
    {"min": 60, "max": 64, "text": 'Patch: "SUKA".'},
    {"min": 65, "max": 69, "text": "Crossbow with 2d10 bolts."},
    {"min": 70, "max": 73, "text": "Intact Panzerfist cybermod."},
    {"min": 74, "max": 75, "text": "Map to a credit stash in The Sink."},
    {"min": 76, "max": 77, "text": "SMG + 2 clips (non-frangible ammo)."},
    {"min": 78, "max": 79, "text": "Adjudicator Guard's modified Stun Baton. 3d10 DMG."},
    {"min": 80, "max": 80, "text": "Cryopack. Three human fingers. Fingerprints intact."},
    {"min": 81, "max": 81, "text": "The Lottery Man by Benno von Archimboldi."},
    {"min": 82, "max": 82, "text": "One-shot mini flame thrower."},
    {"min": 83, "max": 83, "text": "CalixQ's autograph on holopic. Worth 3d10×100cr."},
    {"min": 84, "max": 84, "text": "Dose of Sycorax."},
    {"min": 85, "max": 85, "text": "Well-thumbed copy of The Grasshopper Lies Heavy."},
    {"min": 86, "max": 86, "text": '"Nemo" journal recounting 4 days prior to a Sleeving.'},
    {"min": 87, "max": 87, "text": "Pipebomb — 5d10 DMG, 4m radius."},
    {"min": 88, "max": 88, "text": "Subversive anti-corporate Samizdat literature."},
    {"min": 89, "max": 89, "text": "A small bottle of Tendre Poison eau de toilette."},
    {"min": 90, "max": 90, "text": "Dog-eared copy of the Orange Catholic Bible."},
    {"min": 91, "max": 91, "text": "O2 tank with 1d10 hours remaining."},
    {"min": 92, "max": 92, "text": "Inactive robotic spider named Icarus. Needs repair."},
    {"min": 93, "max": 93, "text": "Sheathed zipgun with 6 bullets."},
    {"min": 94, "max": 94, "text": "La Boussole des précieux, by Pierre Menard."},
    {"min": 95, "max": 95, "text": "A holomap of Caliban's Heart."},
    {"min": 96, "max": 96, "text": "Writhing cyberworm. Worth 1d10×1kcr."},
    {"min": 97, "max": 97, "text": "Tattooed piece of preserved skin."},
    {"min": 98, "max": 98, "text": "Raggedy broken doll. Still talks."},
    {"min": 99, "max": 99, "text": 'Tempest Co. Exosuit. Tagged: "MAMA TRIED."'},
]

RANDOM_SEARCH_RU = [
    {"min": 0,  "max": 0,  "text": "Кредстик без удостоверения. 1d100×100 кр."},
    {"min": 1,  "max": 4,  "text": "Кредстик, привязанный к жертве. 1d100×10 кр."},
    {"min": 5,  "max": 9,  "text": "VIP-приглашение в игорный зал Heaven."},
    {"min": 10, "max": 14, "text": "Фальшивый резиновый револьвер. Выглядит реалистично."},
    {"min": 15, "max": 19, "text": "Работающий синтетический питомец."},
    {"min": 20, "max": 24, "text": "Металлический складной веер."},
    {"min": 25, "max": 29, "text": 'Кожаная куртка. На спине: "Суки Любят Острый Нож".'},
    {"min": 30, "max": 34, "text": "Набор: ×5 Стимпаков и ×4 Автомедов."},
    {"min": 35, "max": 39, "text": "Пустой баллон O2."},
    {"min": 40, "max": 44, "text": "Засушенный Мясопед."},
    {"min": 45, "max": 49, "text": "Браслет с мигающими цветными огоньками."},
    {"min": 50, "max": 54, "text": "Фляга со станционным самогоном."},
    {"min": 55, "max": 59, "text": "Артизанный шоколад (снимает 2 Стресса)."},
    {"min": 60, "max": 64, "text": 'Нашивка: "SUKA".'},
    {"min": 65, "max": 69, "text": "Арбалет с 2d10 болтами."},
    {"min": 70, "max": 73, "text": "Целый кибермод Панцерфист."},
    {"min": 74, "max": 75, "text": "Карта к кредитному тайнику в Отстойнике."},
    {"min": 76, "max": 77, "text": "ПП + 2 магазина (патроны без пробития корпуса)."},
    {"min": 78, "max": 79, "text": "Модифицированная дубинка охранника Суда. 3d10 урона."},
    {"min": 80, "max": 80, "text": "Криоупаковка. Три человеческих пальца. Отпечатки целы."},
    {"min": 81, "max": 81, "text": "«Человек лотереи» Бенно фон Архимбольди."},
    {"min": 82, "max": 82, "text": "Одноразовый мини-огнемёт."},
    {"min": 83, "max": 83, "text": "Автограф CalixQ на голофото. Стоит 3d10×100 кр."},
    {"min": 84, "max": 84, "text": "Доза Сикоракса."},
    {"min": 85, "max": 85, "text": "Зачитанный экземпляр «Кузнечик лжёт тяжело»."},
    {"min": 86, "max": 86, "text": 'Журнал "Немо" — записи 4 дней до Рукавичного.'},
    {"min": 87, "max": 87, "text": "Трубчатая бомба — 5d10 урона, радиус 4 м."},
    {"min": 88, "max": 88, "text": "Подрывная антикорпоративная самиздатовская литература."},
    {"min": 89, "max": 89, "text": "Маленький флакон Tendre Poison, туалетная вода."},
    {"min": 90, "max": 90, "text": "Потрёпанный экземпляр Оранжевой католической Библии."},
    {"min": 91, "max": 91, "text": "Баллон O2 с 1d10 часами кислорода."},
    {"min": 92, "max": 92, "text": "Неработающий роботизированный паук по имени Икар. Нужен ремонт."},
    {"min": 93, "max": 93, "text": "Зипган в ножнах, 6 патронов."},
    {"min": 94, "max": 94, "text": "La Boussole des précieux, Пьер Менар."},
    {"min": 95, "max": 95, "text": "Голокарта Сердца Калибана."},
    {"min": 96, "max": 96, "text": "Извивающийся киберчервь. Стоит 1d10×1 ткр."},
    {"min": 97, "max": 97, "text": "Татуированный лоскут законсервированной кожи."},
    {"min": 98, "max": 98, "text": "Потрёпанная сломанная кукла. Ещё разговаривает."},
    {"min": 99, "max": 99, "text": 'Экзоскафандр Tempest Co. Метка: "MAMA TRIED."'},
]

RANDOM_SEARCH_UA = [
    {"min": 0,  "max": 0,  "text": "Кредстік без посвідчення. 1d100×100 кр."},
    {"min": 1,  "max": 4,  "text": "Кредстік, прив'язаний до жертви. 1d100×10 кр."},
    {"min": 5,  "max": 9,  "text": "VIP-запрошення до ігрового залу Heaven."},
    {"min": 10, "max": 14, "text": "Фальшивий гумовий револьвер. Виглядає реалістично."},
    {"min": 15, "max": 19, "text": "Працюючий синтетичний вихованець."},
    {"min": 20, "max": 24, "text": "Металевий складний віяло."},
    {"min": 25, "max": 29, "text": 'Шкіряна куртка. На спині: "Суки Любят Острый Нож".'},
    {"min": 30, "max": 34, "text": "Набір: ×5 Стімпаків та ×4 Автомедів."},
    {"min": 35, "max": 39, "text": "Порожній балон O2."},
    {"min": 40, "max": 44, "text": "Засушений М'ясопед."},
    {"min": 45, "max": 49, "text": "Браслет з блимаючими кольоровими вогниками."},
    {"min": 50, "max": 54, "text": "Фляга зі станційним самогоном."},
    {"min": 55, "max": 59, "text": "Артизанний шоколад (знімає 2 Стреси)."},
    {"min": 60, "max": 64, "text": 'Нашивка: "SUKA".'},
    {"min": 65, "max": 69, "text": "Арбалет з 2d10 болтами."},
    {"min": 70, "max": 73, "text": "Цілий кібермод Панцерфіст."},
    {"min": 74, "max": 75, "text": "Карта до кредитного схову у Відстійнику."},
    {"min": 76, "max": 77, "text": "ПП + 2 магазини (патрони без пробиття корпусу)."},
    {"min": 78, "max": 79, "text": "Модифікована дубинка охоронця Суду. 3d10 шкоди."},
    {"min": 80, "max": 80, "text": "Кріоупаковка. Три людських пальці. Відбитки цілі."},
    {"min": 81, "max": 81, "text": "«Людина лотереї» Бенно фон Архімбольді."},
    {"min": 82, "max": 82, "text": "Одноразовий міні-вогнемет."},
    {"min": 83, "max": 83, "text": "Автограф CalixQ на голофото. Коштує 3d10×100 кр."},
    {"min": 84, "max": 84, "text": "Доза Сікоракса."},
    {"min": 85, "max": 85, "text": "Зачитаний примірник «Коник бреше важко»."},
    {"min": 86, "max": 86, "text": 'Журнал "Немо" — записи 4 днів до Рукавиці.'},
    {"min": 87, "max": 87, "text": "Трубчаста бомба — 5d10 шкоди, радіус 4 м."},
    {"min": 88, "max": 88, "text": "Підривна антикорпоративна самвидавівська література."},
    {"min": 89, "max": 89, "text": "Маленький флакон Tendre Poison, туалетна вода."},
    {"min": 90, "max": 90, "text": "Потріпаний примірник Помаранчевої католицької Біблії."},
    {"min": 91, "max": 91, "text": "Балон O2 з 1d10 годинами кисню."},
    {"min": 92, "max": 92, "text": "Непрацюючий роботизований павук на ім'я Ікар. Потрібен ремонт."},
    {"min": 93, "max": 93, "text": "Зіпган у піхвах, 6 патронів."},
    {"min": 94, "max": 94, "text": "La Boussole des précieux, П'єр Менар."},
    {"min": 95, "max": 95, "text": "Голокарта Серця Каліба на."},
    {"min": 96, "max": 96, "text": "Звивистий кібервхервь. Коштує 1d10×1 ткр."},
    {"min": 97, "max": 97, "text": "Татуйований шматок законсервованої шкіри."},
    {"min": 98, "max": 98, "text": "Потріпана зламана лялька. Ще розмовляє."},
    {"min": 99, "max": 99, "text": 'Екзоскафандр Tempest Co. Мітка: "MAMA TRIED."'},
]

# ---------------------------------------------------------------------------
# C328–C340 — Space Station Noteworthy Locations (d100, pp. 50-51)
# 8 individual tables, one per station type column.
# ---------------------------------------------------------------------------
def _e(groups: list, singles: list) -> list:
    """18 groups of 5 (00-04..85-89) + 10 singles (90-99)."""
    entries = []
    for i, text in enumerate(groups):
        lo = i * 5
        entries.append({"min": lo, "max": lo + 4, "text": text})
    for i, text in enumerate(singles):
        entries.append({"min": 90 + i, "max": 90 + i, "text": text})
    return entries


# (id, icon, name_en, name_ru, name_ua, groups, singles)
# ru/ua use English as placeholder per Rule 1
NOTEWORTHY_LOCATION_TABLES = [
    (
        328, "🔧",
        "Noteworthy Locations — Refuel/Repair",
        "Примечательные места — Дозаправка/Ремонт",
        "Примітні місця — Дозаправка/Ремонт",
        ["Dry Dock", "Vehicle Repair", "Chop Shop", "Bars", "Showers",
         "Capsule Motel", "Navigation Library", "Warp Core Storage",
         "Teamster Union Hall", "Military Lounge", "Commercial Travel",
         "Private Hangar", "Showers", "Metal Foundry", "Ore Trade / Refinery",
         "Food Court", "Fuel Bays / Warp Cores", "Slickscreens"],
        ["Red Light District", "Black Market", "Tiny Chapel",
         "Weapons Fabrication", "Advanced R&D", "Experimental FTL Lab",
         "Astronavigator Terminals", "Station Overseer", "Holding Cells",
         "Power Station"],
    ),
    (
        334, "🏬",
        "Noteworthy Locations — Port/Market",
        "Примечательные места — Порт/Рынок",
        "Примітні місця — Порт/Ринок",
        ["Food Stand", "Dry Dock", "Fence for Stolen Goods", "Black Market",
         "Re-Sleeving Facility", "Cybermod Shop", "Imports Warehouse",
         "Designer Drugs", "Gene Therapy", "Holotat Shop", "Glass Blower",
         "Technobladesmith", "Slaughter Yard", "Fabric Loom", "Sweatshop",
         "Gambling House", "Dance Club", "Teamster Bar"],
        ["Cassette Library", "Specimens & Oddities", "Red Light District",
         "Military Black Site", "Navigator Guildhouse", "Decorative Rugs",
         "Tea Shop", "Old Earth Antique Shop", "Custom Androids", "Ship Designer"],
    ),
    (
        335, "🏘️",
        "Noteworthy Locations — Colony/Habitat",
        "Примечательные места — Колония/Жильё",
        "Примітні місця — Колонія/Житло",
        ["Farming Unit", "Food Court", "Slickscreen", "Bar/Club",
         "Slaughterhouse", "Seed/Gene Storage", "Sleeping Units",
         "Meeting Square", "Aquaponics Tanks", "Markets",
         "School/Training Facilities", "Library/Research Lab",
         "Upscale Housing", "Security Outpost", "Clinic",
         "Factory", "Greenhouse", "Turret Emplacement"],
        ["Red Light District", "Brig", "Power Station", "Pharmalab",
         "Governor's Mansion", "Armory", "Temple", "Courthouse/Records",
         "Landing Strip", "Communication Array"],
    ),
    (
        336, "⚔️",
        "Noteworthy Locations — Military",
        "Примечательные места — Военная база",
        "Примітні місця — Військова база",
        ["Admin Offices", "Drop Station", "Training Rooms", "Shooting Range",
         "Command Center", "Defensive Weaponry", "Vehicle Repair Center",
         "Brig", "Troopship Carrier", "Barracks", "Interrogation Rooms",
         "Medbay", "R&D Department", "Drop-tank Hangar", "Mess Hall",
         "Officer's Lounge", '"Off-base" Housing', "Master Computer"],
        ["Diplomatic Embassy", "Officer's Quarters", "Weapon Testing",
         "Fighter Squadron", "Ammunition Storage", "Re-Sleeving Facility",
         "Cryochambers", "Intelligence Facility", "Exomech Hangar",
         "Massive Weapon"],
    ),
    (
        337, "⛏️",
        "Noteworthy Locations — Mining/Factory",
        "Примечательные места — Шахта/Завод",
        "Примітні місця — Шахта/Завод",
        ["Material Processing", "Shipping Warehouse", "Storage Warehouse",
         "Dry Dock", "Assembly Line", "Metal Refinery", "Air Scrubber",
         "Water Reclamation", "Sleeping Pods", "Cafeteria",
         "Showers/Soakers", "Corp. Conference Room", "Garage/Hangar",
         "Geology Lab", "Records/Maps/Blueprints", "Slickscreen",
         "Fighting Ring", "Android Maintenance"],
        ["Conjugal Trailers", "Xenobio Lab", "Extraction Point",
         "Infraction Cells", "Cloning Facility", "Communications",
         "Exosuit Hangar/Repair", "Life Support", "Laser Drilling Array",
         "Company Store"],
    ),
    (
        338, "🔬",
        "Noteworthy Locations — Corporate/Research",
        "Примечательные места — Корпоративная станция",
        "Примітні місця — Корпоративна станція",
        ["Offices", "Open Floor Plan Office", "Cubicles", "Testing Lab",
         "AI Computer Banks", "Laboratory", "Quarantine Room",
         "Data Analysis Office", "Android Storage", "Warehouse",
         "Shipping & Receiving", "Mail Rooms", "Meeting Rooms",
         "Clean Room", "Employee Housing", "Hazardous Materials",
         "Cryostorage", "Containment Lab"],
        ["Private Offices", "Luxurious Boardroom", "High Security Vault",
         "Illegal DNA Splicing Lab", "Embryonic Storage", "Morgue",
         "Animal Testing Pens", "Killteam Barracks", "Experiment #237",
         "Mega-AI Brain"],
    ),
    (
        339, "🔒",
        "Noteworthy Locations — Prison",
        "Примечательные места — Тюрьма",
        "Примітні місця — Тюрма",
        ["Ruined Cellblock", "Administration Offices", "Morgue",
         "Riot Armory", "Guard Quarters", "High Security Area",
         "Isolation Chambers", "Cryostorage", "VR Exercise Yard",
         "Prison Cells", "Group Dormitory", "Quarantine Unit",
         "Solitary Confinement", "Canteen", "Gruel Kitchen",
         "Labor Camp", "Execution Chambers", "Scrap Metal Workshop"],
        ["Slickscreen Classrooms", "Illegal Human Testing", "Mind Wipe Lab",
         "Mass Grave", "Reprogramming Facility", "Military Black Site",
         "AI Prison Server", "Android Scrapyard", "Commissary", "Crematorium"],
    ),
    (
        340, "⛪",
        "Noteworthy Locations — Religious",
        "Примечательные места — Религиозная станция",
        "Примітні місця — Релігійна станція",
        ["Prayer Gardens", "Observatory", "Cellarium", "Chapter House",
         "Dorter", "Refectory", "Infirmary", "Kitchens", "Lavatorium",
         "Misericord", "Scriptorium", "Calefactory", "Musalla",
         "Minaret", "Prayer Hall", "Ablution Fountains",
         "Chinjusha", "Three Gate"],
        ["Bell Tower", "Shrine", "Lecture Hall", "Grand Reliquary",
         "Massive Statue", "Secret Chambers", "Palatial Gardens",
         "Scourging Room", "Bishop's Manor", "Unmarked Prison Cell"],
    ),
]

# ---------------------------------------------------------------------------
# C329 — Dry Dock Rumors (d10, pg. 10)
# ---------------------------------------------------------------------------
DRY_DOCK_RUMORS_EN = [
    {"min": 1,  "max": 1,  "text": "There's creatures growing in The Choke. (1kcr/rumor)"},
    {"min": 2,  "max": 2,  "text": "Yandee is secretly an android."},
    {"min": 3,  "max": 3,  "text": "Cutter is looking to overthrow Yandee."},
    {"min": 4,  "max": 4,  "text": "Ukko/Ukka is a Hunglung sympathizer."},
    {"min": 5,  "max": 5,  "text": "Imogene Kane is planning an uprising."},
    {"min": 6,  "max": 6,  "text": "Sycorax makes installing cybermods easy."},
    {"min": 7,  "max": 7,  "text": "Angus knows everything about everyone."},
    {"min": 8,  "max": 8,  "text": "Brunhildh keeps a pet monster in the cells."},
    {"min": 9,  "max": 9,  "text": 'Something called "Caliban" is infecting the terminals.'},
    {"min": 10, "max": 10, "text": "The Aarnivalkea can heal any disease."},
]

DRY_DOCK_RUMORS_RU = [
    {"min": 1,  "max": 1,  "text": "В Удушье растут какие-то существа. (1 ткр/слух)"},
    {"min": 2,  "max": 2,  "text": "Янди — тайный андроид."},
    {"min": 3,  "max": 3,  "text": "Каттер планирует свергнуть Янди."},
    {"min": 4,  "max": 4,  "text": "Укко/Укка симпатизирует Хунглунгам."},
    {"min": 5,  "max": 5,  "text": "Имогена Кейн готовит восстание."},
    {"min": 6,  "max": 6,  "text": "Сикоракс облегчает установку кибермодов."},
    {"min": 7,  "max": 7,  "text": "Ангус знает всё обо всех."},
    {"min": 8,  "max": 8,  "text": "Брунхильд держит чудовище в камерах."},
    {"min": 9,  "max": 9,  "text": 'Что-то под названием "Калибан" заражает терминалы.'},
    {"min": 10, "max": 10, "text": "Аарнивалкеа способна вылечить любую болезнь."},
]

DRY_DOCK_RUMORS_UA = [
    {"min": 1,  "max": 1,  "text": "У Задусі ростуть якісь істоти. (1 ткр/чутка)"},
    {"min": 2,  "max": 2,  "text": "Янді — таємний андроїд."},
    {"min": 3,  "max": 3,  "text": "Каттер планує повалити Янді."},
    {"min": 4,  "max": 4,  "text": "Укко/Укка симпатизує Хунглунгам."},
    {"min": 5,  "max": 5,  "text": "Імоген Кейн готує повстання."},
    {"min": 6,  "max": 6,  "text": "Сікоракс полегшує встановлення кібермодів."},
    {"min": 7,  "max": 7,  "text": "Ангус знає все про всіх."},
    {"min": 8,  "max": 8,  "text": "Брунхільд тримає чудовисько в камерах."},
    {"min": 9,  "max": 9,  "text": 'Щось під назвою "Каліban" заражає термінали.'},
    {"min": 10, "max": 10, "text": "Аарнівалкеа здатна вилікувати будь-яку хворобу."},
]

# ---------------------------------------------------------------------------
# C330 — Ships Currently Docked (d10, pg. 11)
# ---------------------------------------------------------------------------
SHIPS_DOCKED_EN = [
    {"min": 1,  "max": 1,  "text": "Conquer All — Looking for gunmen. Leaves tomorrow. 200cr/day, 6-month tour."},
    {"min": 2,  "max": 2,  "text": "Bartzabel — Strikebreakers heading to Tybalt Blue research station. 100cr/day."},
    {"min": 3,  "max": 3,  "text": "Decade of Therion — Blockade runner heading to DMZ. Room for 5. Tickets 1,000cr/ea."},
    {"min": 4,  "max": 4,  "text": "Horns of Baphomet — Rescue mission. Looking for a ship called The Defiance."},
    {"min": 5,  "max": 5,  "text": "In the Absence ov Light — Needs 2 scientists, heading to remote research station for 3 weeks. Pays 50kcr."},
    {"min": 6,  "max": 6,  "text": "Ov Fire and Void — Smuggler looking for work. 1.5kcr advance + 10% of profits."},
    {"min": 7,  "max": 7,  "text": "Daimonos — Needs 100 doses of Sycorax."},
    {"min": 8,  "max": 8,  "text": "Alas, Lord is Upon Me — Mining crew taking apprentices. 1% share of profits, 3-month tour."},
    {"min": 9,  "max": 9,  "text": "Inner Sanctum — Solarians on a pilgrimage to Päivätär 1019. Will take anyone."},
    {"min": 10, "max": 10, "text": "From the Pagan Vastlands — Sensitive cargo heading to Thelema Sector. Guards needed. 500cr/day, 1-month tour."},
]

# ru/ua use English as placeholder
SHIPS_DOCKED_RU = SHIPS_DOCKED_EN
SHIPS_DOCKED_UA = SHIPS_DOCKED_EN

# ---------------------------------------------------------------------------
# C331 — Jobs for The Babushka (d10, pg. 14)
# ---------------------------------------------------------------------------
BABUSHKA_JOBS_EN = [
    {"min": 1,  "max": 4,  "text": "1d5 infected corpses. Bring them here for study. Don't get sick. Pay: 2kcr/ea."},
    {"min": 5,  "max": 6,  "text": "Sycorax pickup from The Farm. Talk to Ukko/Ukka only. Pay: 3kcr."},
    {"min": 7,  "max": 8,  "text": "House call — mutated patient found dead at home. Visit the scene, collect evidence. Don't get sick. Pay: 15kcr."},
    {"min": 9,  "max": 9,  "text": "Rumors of Dr. Bancali modding patients in The Choke. Go to Doptown and track him down. Investigate the ACMD outbreak. Pay: Free cybermod."},
    {"min": 10, "max": 10, "text": "Yandee has called The Babushka in for a meeting. Provide protection. Pay: 40kcr."},
]

BABUSHKA_JOBS_RU = [
    {"min": 1,  "max": 4,  "text": "1d5 заражённых трупов. Доставить для изучения. Не заражайтесь. Оплата: 2 ткр/шт."},
    {"min": 5,  "max": 6,  "text": "Забрать Сикоракс с Фермы. Говорить только с Укко/Укка. Оплата: 3 ткр."},
    {"min": 7,  "max": 8,  "text": "Вызов на дом — мутировавший пациент найден мёртвым. Осмотреть место, собрать улики. Не заразитесь. Оплата: 15 ткр."},
    {"min": 9,  "max": 9,  "text": "Слухи о докторе Банкали в Удушье. Идти в Дауптаун и найти его. Расследовать вспышку ACMD. Оплата: бесплатный кибермод."},
    {"min": 10, "max": 10, "text": "Янди вызвала Бабушку на встречу. Обеспечить охрану. Оплата: 40 ткр."},
]

BABUSHKA_JOBS_UA = [
    {"min": 1,  "max": 4,  "text": "1d5 заражених трупів. Доставити для вивчення. Не заражайтеся. Оплата: 2 ткр/шт."},
    {"min": 5,  "max": 6,  "text": "Забрати Сікоракс із Ферми. Говорити лише з Укко/Уккою. Оплата: 3 ткр."},
    {"min": 7,  "max": 8,  "text": "Виклик додому — мутований пацієнт знайдений мертвим. Оглянути місце, зібрати докази. Не заражайтеся. Оплата: 15 ткр."},
    {"min": 9,  "max": 9,  "text": "Чутки про доктора Банкалі в Задусі. Іти до Даунтауну і знайти його. Розслідувати спалах ACMD. Оплата: безкоштовний кібермод."},
    {"min": 10, "max": 10, "text": "Янді викликала Бабусю на зустріч. Забезпечити охорону. Оплата: 40 ткр."},
]

# ---------------------------------------------------------------------------
# C332 — The Docket (d10, pg. 26)
# ---------------------------------------------------------------------------
DOCKET_EN = [
    {"min": 1,  "max": 1,  "text": "1d10 Doptownians [C:20 Unarmed 1d5dmg S:20 I:20 H:1] vs. 1 Executioner Probate [C:30 Vibechete 2d10dmg S:35 I:35 H:2] — Odds 1:1"},
    {"min": 2,  "max": 3,  "text": "Accused [C:25 Vibechete 2d10dmg S:45 I:35 H:1] vs. Accuser [same stats] — Odds 1:1"},
    {"min": 4,  "max": 5,  "text": "Accused [C:25 Spear 3d10dmg S:45 I:35 H:1] vs. Executioner [C:55 Electrolash 4d10dmg S:50 I:35 H:3] — Odds 1:5"},
    {"min": 6,  "max": 7,  "text": "Advocate [C:55 Rigging Gun 2d10dmg S:50 I:45 H:2] vs. Executioner [C:55 Electrolash 4d10dmg S:50 I:35 H:3] — Odds 1:2"},
    {"min": 8,  "max": 8,  "text": "Accused [C:25 Spear 3d10dmg S:45 I:35 H:1] vs. Random Pit Creature — Odds 1:10"},
    {"min": 9,  "max": 9,  "text": "1d10 Traitors [C:45 Spear 3d10dmg S:40 I:35 H:1] vs. Chief Adjudicator Brunhildh [C:75 Antique 5d10dmg S:65 I:75 H:4] — Odds 1:3"},
    {"min": 10, "max": 10, "text": "2d10 Accused & 1d10 Advocates (melee weapons) vs. 1d10 Chokespawn & 5 Executioners — Odds 1:2"},
]

# ru/ua use English as placeholder
DOCKET_RU = DOCKET_EN
DOCKET_UA = DOCKET_EN

# ---------------------------------------------------------------------------
# C333 — Accused & What They Can Pay (d10, pg. 27)
# ---------------------------------------------------------------------------
ACCUSED_PAY_EN = [
    {"min": 1,  "max": 1,  "text": "Golyonovo Traitor — 1d10×100cr for Advocate. You'll have to fight the Chief Adjudicator."},
    {"min": 2,  "max": 5,  "text": "O2 Debtor — No money. Talk to Ukko/Ukka."},
    {"min": 6,  "max": 7,  "text": "Contraband Smuggler — 50kcr and free ride."},
    {"min": 8,  "max": 8,  "text": "Teamster who stole from Yandee — 1d100×1kcr and free ride (max 3 Jumps)."},
    {"min": 9,  "max": 9,  "text": "Hunglung Insurgent — Can't pay, but Imogene Kane will owe you a favor."},
    {"min": 10, "max": 10, "text": "Political Prisoner — Enemy of Teamster Union, Tempest Co., the Bratva or Solarians. 300kcr+ if you win the rigged trial and escort them off The Dream."},
]

ACCUSED_PAY_RU = [
    {"min": 1,  "max": 1,  "text": "Предатель Голяновских — 1d10×100 кр. адвокату. Придётся драться с Главным Арбитром."},
    {"min": 2,  "max": 5,  "text": "Должник О2 — нет денег вообще. Поговорите с Укко/Укка."},
    {"min": 6,  "max": 7,  "text": "Контрабандист — 50 ткр и бесплатный проезд."},
    {"min": 8,  "max": 8,  "text": "Тимстер, укравший у Янди — 1d100×1 ткр и бесплатный проезд (макс. 3 прыжка)."},
    {"min": 9,  "max": 9,  "text": "Инсургент Хунглунгов — заплатить нечем, но Имогена Кейн будет должна."},
    {"min": 10, "max": 10, "text": "Политический заключённый — враг профсоюза, Tempest Co., Братвы или Солярийцев. 300 ткр+, если выиграете подтасованный суд и вывезете с Мечты."},
]

ACCUSED_PAY_UA = [
    {"min": 1,  "max": 1,  "text": "Зрадник Голянових — 1d10×100 кр. адвокату. Доведеться битись з Головним Арбітром."},
    {"min": 2,  "max": 5,  "text": "Боржник О2 — грошей немає. Поговоріть з Укко/Уккою."},
    {"min": 6,  "max": 7,  "text": "Контрабандист — 50 ткр та безкоштовна поїздка."},
    {"min": 8,  "max": 8,  "text": "Тімстер, що вкрав у Янді — 1d100×1 ткр та безкоштовна поїздка (макс. 3 стрибки)."},
    {"min": 9,  "max": 9,  "text": "Інсургент Хунглунгів — заплатити нема чим, але Імоген Кейн буде винна."},
    {"min": 10, "max": 10, "text": "Політичний в'язень — ворог профспілки, Tempest Co., Братви або Солярійців. 300 ткр+, якщо виграєте підтасований суд і вивезете з Мрії."},
]

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
def _upsert_content(
    conn, cid, icon, entries_en, entries_ru, entries_ua,
    name_en, name_ru, name_ua, die, page_id, sort_order,
    desc_en="", desc_ru="", desc_ua="",
):
    dice_json = json.dumps({"die": die, "entries": entries_en}, ensure_ascii=False)
    conn.execute(
        "INSERT OR IGNORE INTO contents (id, icon, dice, source_slug) VALUES (?, ?, ?, 'apof')",
        (cid, icon, dice_json),
    )
    conn.execute(
        "UPDATE contents SET icon=?, dice=? WHERE id=?",
        (icon, dice_json, cid),
    )
    for lang, name, desc, entries in [
        ("en", name_en, desc_en, entries_en),
        ("ru", name_ru, desc_ru, entries_ru),
        ("ua", name_ua, desc_ua, entries_ua),
    ]:
        de_json = json.dumps(entries, ensure_ascii=False)
        conn.execute(
            """INSERT INTO content_i18n (content_id, lang, name, desc, dice_entries)
               VALUES (?, ?, ?, ?, ?)
               ON CONFLICT (content_id, lang)
               DO UPDATE SET name=excluded.name, desc=excluded.desc, dice_entries=excluded.dice_entries""",
            (cid, lang, name, desc, de_json),
        )
    if page_id is not None:
        conn.execute(
            "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (?, ?, ?)",
            (page_id, cid, sort_order),
        )


def _seed(conn: sqlite3.Connection) -> None:
    # ── Update C217: add Infection Table dice ────────────────────────────────
    dice_217 = json.dumps({"die": "d10", "entries": INFECTION_TABLE_ENTRIES}, ensure_ascii=False)
    conn.execute("UPDATE contents SET dice=? WHERE id=217", (dice_217,))
    for lang, entries in [("en", INFECTION_TABLE_ENTRIES), ("ru", INFECTION_TABLE_RU), ("ua", INFECTION_TABLE_UA)]:
        conn.execute(
            """UPDATE content_i18n SET dice_entries=?
               WHERE content_id=217 AND lang=?""",
            (json.dumps(entries, ensure_ascii=False), lang),
        )

    # ── C326 Cybernetic Mutations (P38, sort=12) ─────────────────────────────
    _upsert_content(
        conn, 326, "🧬",
        CYBERNETIC_MUTATIONS_EN, CYBERNETIC_MUTATIONS_RU, CYBERNETIC_MUTATIONS_UA,
        "Cybernetic Mutations", "Кибернетические Мутации", "Кібернетичні Мутації",
        "d100", 38, 12,
        desc_en="Roll when a character contracts ACMD or is instructed by another table. Healing mutations requires cybersurgery similar to installation.",
        desc_ru="Бросайте при заражении ACMD или по указанию другой таблицы. Лечение мутаций требует кибер-хирургии.",
        desc_ua="Кидайте при зараженні ACMD або за вказівкою іншої таблиці. Лікування мутацій потребує кібер-хірургії.",
    )

    # ── C327 Random Search (P38, sort=13) ────────────────────────────────────
    _upsert_content(
        conn, 327, "🔍",
        RANDOM_SEARCH_EN, RANDOM_SEARCH_RU, RANDOM_SEARCH_UA,
        "Random Search", "Случайный Обыск", "Випадковий Обшук",
        "d100", 38, 13,
        desc_en="Roll to determine what is found when searching a body or scavenging on Prospero's Dream.",
        desc_ru="Бросайте при обыске тела или мародёрстве на Мечте Просперо.",
        desc_ua="Кидайте при обшуку тіла або мародерстві на Мрії Просперо.",
    )

    # ── C328–C340 Noteworthy Locations, one table per station type ───────────────
    # Not placed on any page directly — accessed via C341 content links
    # (see add_noteworthy_locations_intro.py).
    for cid, icon, name_en, name_ru, name_ua, groups, singles in NOTEWORTHY_LOCATION_TABLES:
        entries = _e(groups, singles)
        _upsert_content(
            conn, cid, icon,
            entries, entries, entries,
            name_en, name_ru, name_ua,
            "d100", None, None,
        )

    # ── C329 Dry Dock Rumors (sub-item of C229, not on P35 directly) ─────────
    _upsert_content(
        conn, 329, "👂",
        DRY_DOCK_RUMORS_EN, DRY_DOCK_RUMORS_RU, DRY_DOCK_RUMORS_UA,
        "Dry Dock Rumors", "Слухи на Доке", "Чутки в Доці",
        "d10", None, None,
        desc_en="Sem will dispense a rumor for 1kcr if you've bought a drink. Loshe also shares rumors freely.",
        desc_ru="Сем расскажет слух за 1 ткр, если купите выпивку. Лоше тоже охотно делится слухами.",
        desc_ua="Сем поділиться чуткою за 1 ткр, якщо купите напій. Лоше також охоче ділиться чутками.",
    )

    # ── C330 Ships Currently Docked (sub-item of C229, not on P35 directly) ──
    _upsert_content(
        conn, 330, "⚓",
        SHIPS_DOCKED_EN, SHIPS_DOCKED_RU, SHIPS_DOCKED_UA,
        "Ships Currently Docked", "Пришвартованные корабли", "Пришвартовані кораблі",
        "d10", None, None,
        desc_en="Roll to see which ship is currently docked and what work they're offering.",
        desc_ru="Бросайте, чтобы узнать, какой корабль стоит у дока и какую работу предлагает.",
        desc_ua="Кидайте, щоб дізнатись, який корабель стоїть у доці та яку роботу пропонує.",
    )

    # ── C331 Jobs for The Babushka (sub-item of C232, not on P35 directly) ───
    _upsert_content(
        conn, 331, "📋",
        BABUSHKA_JOBS_EN, BABUSHKA_JOBS_RU, BABUSHKA_JOBS_UA,
        "Jobs for The Babushka", "Работа от Бабушки", "Робота від Бабусі",
        "d10", None, None,
        desc_en="Work available from The Babushka at The Chop Shop. Appointments through Zhenya.",
        desc_ru="Работа от Бабушки в Разделочной. Запись через Женю.",
        desc_ua="Робота від Бабусі в Розбірній. Запис через Женю.",
    )

    # ── C332 The Docket (sub-item of C240, not on P35 directly) ─────────────
    _upsert_content(
        conn, 332, "⚖️",
        DOCKET_EN, DOCKET_RU, DOCKET_UA,
        "The Docket", "Список Дел", "Список Справ",
        "d10", None, None,
        desc_en="Roll to determine today's trial matchup in The Court. Gambling on outcomes is common.",
        desc_ru="Бросайте для определения поединка в суде. На исходы активно делают ставки.",
        desc_ua="Кидайте для визначення двобою у Суді. Ставки на результат — звичайна справа.",
    )

    # ── C333 Accused & What They Can Pay (sub-item of C240, not on P35 directly)
    _upsert_content(
        conn, 333, "💰",
        ACCUSED_PAY_EN, ACCUSED_PAY_RU, ACCUSED_PAY_UA,
        "Accused & What They Can Pay", "Обвиняемый и Его Предложение", "Обвинувачений та Його Пропозиція",
        "d10", None, None,
        desc_en="Roll to see who is in The Holding Cells and what they can offer an Advocate.",
        desc_ru="Бросайте, чтобы узнать, кто в камерах и что они могут предложить адвокату.",
        desc_ua="Кидайте, щоб дізнатись, хто в камерах і що вони можуть запропонувати адвокату.",
    )

    # ── Content links ─────────────────────────────────────────────────────────
    links = [
        (326, 254, "related", 0),   # Cybernetic Mutations → Installation Rules
        (326, 255, "related", 1),   # Cybernetic Mutations → Cybermod Malfunctions
        (326, 256, "related", 2),   # Cybernetic Mutations → Cybermod Panic Table
        (229, 329, "related", 0),   # 01 Dry Dock → Dry Dock Rumors
        (229, 330, "related", 1),   # 01 Dry Dock → Ships Currently Docked
        (329, 229, "related", 0),   # Dry Dock Rumors → 01 Dry Dock (back)
        (330, 229, "related", 0),   # Ships Currently Docked → 01 Dry Dock (back)
        (232, 331, "related", 0),   # 03 The Chop Shop → Jobs for The Babushka
        (240, 332, "related", 1),   # 07 The Court → The Docket  (forward; sort 0 = Pit Fighters from add_apof_locations)
        (240, 333, "related", 2),   # 07 The Court → Accused & What They Can Pay
        (331, 232, "related", 0),   # Jobs for The Babushka → 03 The Chop Shop (back)
        (332, 240, "related", 0),   # The Docket → 07 The Court (back)
        (333, 240, "related", 0),   # Accused & What They Can Pay → 07 The Court (back)
        (333, 332, "related", 1),   # Accused & What They Can Pay → The Docket
        # Noteworthy Locations tables (C328–C340) → Structure + Issues
        *[(cid, 305, "related", 0) for cid, *_ in NOTEWORTHY_LOCATION_TABLES],
        *[(cid, 306, "related", 1) for cid, *_ in NOTEWORTHY_LOCATION_TABLES],
        (217, 252, "related", 0),   # Infection Rules → Chokespawn
    ]
    for from_id, to_id, label, sort in links:
        conn.execute(
            """INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key, sort_order)
               VALUES (?, ?, ?, ?)""",
            (from_id, to_id, label, sort),
        )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(
            "Done — C217 updated with Infection Table dice; "
            "C326 (Cybernetic Mutations), C327 (Random Search), "
            "C328–C340 (Noteworthy Locations ×8), C329 (Dry Dock Rumors), "
            "C330 (Ships Currently Docked), C331 (Jobs for The Babushka), "
            "C332 (The Docket), C333 (Accused & What They Can Pay) added. "
            "12 content links added."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
