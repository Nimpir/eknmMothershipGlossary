"""
scripts/add_apof_deep.py
A Pound of Flesh — Deep locations: Doptown (C245) and The Choke (C247) are placed
on P35 (The Station). Their sub-items (C246, C248–C253) are linked via content_links.
The Sink, Life Support 01, The Burrows, Caliban's Heart, Chokespawn, and encounter
tables are seeded here but accessible only through content_links from C247.
Run after add_apof_source_pages.py.
Run: python scripts/add_apof_deep.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

PAGE_ID = 36  # P36 is the source page for this content; C245/C247 land on P35

# ── Content items ────────────────────────────────────────────────────────────
# Each tuple: (id, icon, slug, sort_order, dice_sides_or_None,
#              name_en, name_ru, name_ua,
#              desc_en, desc_ru, desc_ua,
#              dice_en, dice_ru, dice_ua)   — dice_* are lists or None
# subinfo_fixed handled separately where needed

ITEMS = [
    # ── C245 Doptown ──────────────────────────────────────────────────────────
    (
        245, "😷", "apof_doptown", 1, None,
        "09 Doptown",
        "09 Доптаун",
        "09 Доптаун",
        (
            "Slang for 'de-oxygenated people's town.' A hellish slum for oxygen debtors. "
            "On entering make a Fear Save or gain 1d10 Stress.\n\n"
            "1. THE AIRLOCK. Heavily armed gate, cement turret bunkers (200dmg), "
            "1d10 Armored Troopers. Col. Antonio commands with cold indifference. "
            "Cannot re-enter The Dream without a pass.\n\n"
            "2. THE AUCTION. Silent market — Doptownians sell services to pay O2 debt. "
            "Wealthy citizens descend with bodyguards.\n\n"
            "3. THE SLUMS. Overcrowded, stench of death. Roll encounters every 30 min. "
            "Rumors cost 1 O2 tank each: Imogene Kane leads the Hunglungs; Dr. Bancali "
            "implants 'gills' behind the sludge waterfall; Sycorax grows in The Burrows; "
            "something speaks to Doptownians in their sleep; a broken Life Support Tower "
            "could be repaired; the Sink is accessible via the waterfall.\n\n"
            "4. THE LOTTERY. Scavenged O2 tanks distributed by lottery (5% chance/PC of "
            "winning 1d10 hrs O2). Imogene Kane distributes stolen tanks here — a hero "
            "to the Doptownians."
        ),
        (
            "Сленг от 'дезоксигенизированный народный город.' Ужасные трущобы для "
            "должников по кислороду. При входе — Спасбросок от Страха или 1d10 Стресса.\n\n"
            "1. ШЛЮЗ. Тяжеловооружённые ворота, цементные турели (200ед. урона), "
            "1d10 Бронированных Бойцов. Полковник Антонио командует с холодным безразличием. "
            "Без пропуска обратно в Мечту не попасть.\n\n"
            "2. АУКЦИОН. Молчаливый рынок — Доптаунцы продают услуги, чтобы расплатиться "
            "за O2. Богатые граждане спускаются с охраной.\n\n"
            "3. ТРУЩОБЫ. Переполненные, с запахом смерти. Броски на встречи каждые 30 мин. "
            "Слухи стоят 1 баллон O2: Иможен Кейн возглавляет Хунглунгов; Доктор Банкали "
            "вживляет 'жабры' за грязевым водопадом; Сикоракс растёт в Норах; нечто "
            "говорит с Доптаунцами во сне; сломанная Башня Жизнеобеспечения подлежит "
            "ремонту; в Провал можно попасть через водопад.\n\n"
            "4. ЛОТЕРЕЯ. Собранные баллоны O2 распределяются по лотерее (5% шанс/ПС "
            "выиграть 1d10 часов O2). Иможен Кейн раздаёт здесь украденные баллоны — "
            "она герой для Доптаунцев."
        ),
        (
            "Сленг від 'дезоксигенізоване народне місто.' Пекельні нетрі для боржників "
            "за кисень. При вході — Рятівний кидок від Страху або 1d10 Стресу.\n\n"
            "1. ШЛЮЗ. Важкоозброєні ворота, цементні турелі (200 од. шкоди), "
            "1d10 Бронетрупперів. Полковник Антоніо командує з холодною байдужістю. "
            "Без перепустки назад у Мрію не потрапити.\n\n"
            "2. АУКЦІОН. Мовчазний ринок — Доптаунці продають послуги, щоб погасити "
            "борг за O2. Заможні громадяни спускаються з охороною.\n\n"
            "3. НЕТРІ. Переповнені, зі смородом смерті. Кидки на зустрічі кожні 30 хв. "
            "Чутки коштують 1 балон O2: Іможен Кейн очолює Хунглунгів; Доктор Банкалі "
            "вживляє 'зябра' за брудним водоспадом; Сикоракс росте в Норах; щось "
            "промовляє до Доптаунців уві сні; зламана Вежа Забезпечення підлягає "
            "ремонту; в Провал можна потрапити через водоспад.\n\n"
            "4. ЛОТЕРЕЯ. Зібрані балони O2 розподіляються за лотереєю (5% шанс/ПС "
            "виграти 1d10 год O2). Іможен Кейн роздає тут вкрадені балони — "
            "вона героїня для Доптаунців."
        ),
        None, None, None,
    ),
    # ── C246 Doptown NPCs & Encounters ───────────────────────────────────────
    (
        246, "👾", "apof_doptown_encounters", 2, 10,
        "Doptown NPCs & Encounters",
        "Доптаун: НИП и Встречи",
        "Доптаун: НГП та Зустрічі",
        "Roll once per change of location in Doptown.",
        "Бросайте при каждой смене локации в Доптауне.",
        "Кидайте при кожній зміні локації в Доптауні.",
        [
            "Chokespawn: Running rampant and attacking Doptownians. Always stops to consume bodies.",
            "Deceased O2 Beggar.",
            "O2 Beggar: Cardboard sign of a clock showing how many hours the beggar has left to live. PCs who don't donate O2 must make a Sanity Save or gain 1 Stress.",
            "O2 Beggars, Family of Three: Child has a sign that says 'Paying for my father's sins.' PCs who don't donate must make a Sanity Save or gain 1d5 Stress.",
            "2d10 Beggars: Group of desperate beggars mob you for O2, credits, weapons, anything.",
            "1d10 Scavengers: Going from home to home collecting O2 tanks from the dead.",
            "1d5 Tempest Armored Troopers: Patrolling. Harassing and murdering those who approach too closely or annoy them.",
            "Standoff between 1d5 Tempest Armored Troopers [H:3 C:65 Smart Rifle 1d10dmg I:45 Armor:65] and 2 Hunglung Snipers [C:75 Smart Rifle 1d10dmg S:25 I:55 H:2]: Tempest mercs pinned down, calling for reinforcements.",
            "1d5 Hunglung Insurgency Recruiters: Want to take you to speak with Imogene Kane. They have snipers on you.",
            "Imogene Kane: Leader of the Hunglungs. Has 'gills' from Dr. Bancali (pg. 34). Doesn't know this is making her sick and paranoid. Seeks volunteers to upload Doptown citizens into new Sleeves via Caliban's Heart.",
        ],
        [
            "Чокеспаун: Разгуливает и нападает на жителей Доптауна. Всегда останавливается, чтобы пожрать трупы.",
            "Мёртвый попрошайка O2.",
            "Попрошайка O2: Картонный знак с часами, показывающими, сколько часов осталось жить. Если ПС не дают O2, Спасбросок Рассудка или +1 Стресс.",
            "Семья попрошаек O2 из трёх: На знаке у ребёнка написано 'Расплачиваюсь за грехи отца.' Если не дать — Спасбросок Рассудка или +1d5 Стресса.",
            "2d10 попрошаек: Толпа отчаявшихся попрошаек требует O2, кредиты, оружие — что угодно.",
            "1d10 Мародёров: Обходят дома, собирая баллоны O2 с мертвецов.",
            "1d5 Бронетруппера Tempest: Патрулируют. Издеваются и убивают тех, кто подходит слишком близко.",
            "Противостояние 1d5 Бронетрупперов Tempest [H:3 C:65 Умная винтовка 1d10 урона I:45 Броня:65] и 2 Снайперов Хунглунгов [C:75 Умная винтовка 1d10 урона S:25 I:55 H:2]: Tempest прижаты, вызывают подкрепление.",
            "1d5 Вербовщиков Повстанцев Хунглунг: Хотят отвести к Иможен Кейн. На вас наведены снайперы.",
            "Иможен Кейн: Лидер Хунглунгов. Имеет 'жабры' от Доктора Банкали. Не знает, что это делает её больной и параноидальной. Ищет добровольцев для загрузки граждан Доптауна в новые Рукава через Сердце Калибана.",
        ],
        [
            "Чокеспаун: Безчинствує і нападає на жителів Доптауну. Завжди зупиняється, щоб пожерти трупи.",
            "Мертвий жебрак O2.",
            "Жебрак O2: Картонний знак з годинником, що показує скільки годин залишилось жити. Якщо ПС не дають O2, Рятівний кидок Розуму або +1 Стрес.",
            "Родина жебраків O2 з трьох: На знаку дитини написано 'Розплачуюсь за гріхи батька.' Якщо не дати — Рятівний кидок Розуму або +1d5 Стресу.",
            "2d10 жебраків: Натовп відчайдушних жебраків вимагає O2, кредити, зброю — що завгодно.",
            "1d10 Мародерів: Обходять будинки, збираючи балони O2 з мерців.",
            "1d5 Бронетрупперів Tempest: Патрулюють. Знущаються і вбивають тих, хто підходить надто близько.",
            "Протистояння 1d5 Бронетрупперів Tempest [H:3 C:65 Розумна гвинтівка 1d10 шкоди I:45 Броня:65] і 2 Снайперів Хунглунгів [C:75 Розумна гвинтівка 1d10 шкоди S:25 I:55 H:2]: Tempest притиснуті, викликають підкріплення.",
            "1d5 Вербувальників Повстанців Хунглунг: Хочуть відвести до Іможен Кейн. На вас наведено снайпери.",
            "Іможен Кейн: Лідер Хунглунгів. Має 'зябра' від Доктора Банкалі. Не знає, що це робить її хворою та параноїчною. Шукає добровольців для завантаження громадян Доптауну в нові Рукави через Серце Калібана.",
        ],
    ),
    # ── C247 The Choke (overview / map) ──────────────────────────────────────
    (
        247, "🕳️", "apof_the_choke", 3, None,
        "10 The Choke",
        "10 Удавка",
        "10 Задуша",
        (
            "The deep dark below Doptown. All of The Choke is dark — you'll need light to travel. "
            "BYO-O2: without it you are at disadvantage to all rolls and must make a Body Save "
            "once per day to stay conscious.\n\n"
            "TRAVEL TIMES:\n"
            "• Airlock → Doptown: 30-min massive freight elevator, 30 stories down.\n"
            "• Doptown → The Sink: 20-story climb down sludge waterfall.\n"
            "• Doptown → Life Support 01: 4-hour walk; roll twice for encounters.\n"
            "• The Sink → Life Support 01: 2-hour walk through cramped drain pipes; "
            "roll three times for encounters.\n"
            "• Life Support 01 → Caliban's Heart: see The Burrows / The Veins.\n\n"
            "LOCATIONS IN THE CHOKE:\n"
            "1. The Airlock (pg. 30) — 2. Doptown (pg. 30) — 3. Life Support 01 (pg. 36) — "
            "4. The Doctor (pg. 34) — 5. The Sink (pg. 34) — 6. The Veins (pg. 35) — "
            "7. Mass Grave (pg. 35) — 8. The Burrows (pg. 37) — 9. Caliban's Heart (pg. 38)."
        ),
        (
            "Тёмные глубины под Доптауном. Повсюду в Удавке темно — нужен источник света. "
            "Берите кислород с собой: без него все броски с помехой, "
            "Body Save раз в день, чтобы оставаться в сознании.\n\n"
            "ВРЕМЯ В ПУТИ:\n"
            "• Шлюз → Доптаун: 30 мин. на грузовом лифте, 30 этажей вниз.\n"
            "• Доптаун → Провал: спуск по грязевому водопаду 20 этажей.\n"
            "• Доптаун → Система ЖО 01: 4 часа пешком; два броска на встречи.\n"
            "• Провал → Система ЖО 01: 2 часа по узким дренажным трубам; "
            "три броска на встречи.\n"
            "• Система ЖО 01 → Сердце Калибана: см. Норы / Вены.\n\n"
            "ЛОКАЦИИ В УДАВКЕ:\n"
            "1. Шлюз — 2. Доптаун — 3. Система ЖО 01 — "
            "4. Доктор — 5. Провал — 6. Вены — "
            "7. Братская могила — 8. Норы — 9. Сердце Калибана."
        ),
        (
            "Темні глибини під Доптауном. Уся Задуша темна — потрібне джерело світла. "
            "Беріть кисень з собою: без нього всі кидки з перешкодою, "
            "Рятівний кидок Тіла раз на день, щоб залишатися при свідомості.\n\n"
            "ЧАС У ДОРОЗІ:\n"
            "• Шлюз → Доптаун: 30 хв. на вантажному ліфті, 30 поверхів вниз.\n"
            "• Доптаун → Провал: спуск по брудному водоспаду 20 поверхів.\n"
            "• Доптаун → Система ЖЗ 01: 4 години пішки; два кидки на зустрічі.\n"
            "• Провал → Система ЖЗ 01: 2 години вузькими дренажними трубами; "
            "три кидки на зустрічі.\n"
            "• Система ЖЗ 01 → Серце Калібана: див. Нори / Вени.\n\n"
            "ЛОКАЦІЇ В ЗАДУШІ:\n"
            "1. Шлюз — 2. Доптаун — 3. Система ЖЗ 01 — "
            "4. Лікар — 5. Провал — 6. Вени — "
            "7. Братська могила — 8. Нори — 9. Серце Калібана."
        ),
        None, None, None,
    ),
    # ── C248 The Sink ─────────────────────────────────────────────────────────
    (
        248, "🌊", "apof_the_sink", 4, None,
        "The Sink",
        "Провал",
        "Провал",
        (
            "What remains of The Dream's once-bustling downtown — now a sunken city wasteland "
            "covered in cybernetic wires. Dark, fetid, quiet. Make an Infection Check once per "
            "hour unless wearing a Hazard/Vacc/Exosuit. 6 hours end-to-end; ~2 hours to any "
            "connected location. Roll encounters once/hr.\n\n"
            "1. THE FALLS. Twenty-story toxic sludge waterfall. Strength Check to climb unassisted. "
            "Old Hunglung Otto sells scavenged gear (1 O2 tank/set or 2kcr; 5% chance it's faulty). "
            "500cr for a map to The Doctor.\n\n"
            "2. THE DOCTOR. Hidden behind the sludge falls — pulsating tunnel, makeshift operating "
            "theater of reaped limbs. Dr. Bancali works feverishly on a Hunglung. Stats: C:65 "
            "(Scalpel 1d10+Infection Save), SPD:75, INST:65, H:2(20). Devoutly curing Ariel of 'her "
            "sickness.' If killed → move to Outbreak Phase 3. Will install 'gills' on request.\n\n"
            "3. THE OLD CITY. Collapsing buildings (1d5×10 stories), raw sewage, Chokespawn. "
            "Landmarks (each ~1 hr apart): Juno Tower (34 floors, Tempest Sniper perched high), "
            "The Metro (fast travel to The Veins or Mass Grave if power restored), The Outpost "
            "(Tempest FOB, 1d5 paranoid Operators), The Sewers (100' drop → Mass Grave/The Burrows), "
            "The Archives (patient records revealing Dr. Bancali's history).\n\n"
            "4. MASS GRAVE. 'Even if you cannot breathe, you don't deserve to die here.' One-story "
            "pile of corpses, reaped limbs, discarded Husks. Fear Save or 1d5 Stress. 25% chance "
            "of finding a random cybermod (2 Mutation Table rolls + permanent [-] on Saves vs Caliban).\n\n"
            "5. THE VEINS. Drainage pipes, ventilation shafts, maintenance tunnels linking all "
            "modules. Follow Hunglung symbols. 2d10 hours to any module (roll random). "
            "A gross orifice near The Doctor opens to a tunnel leading to The Atrium (pg. 39)."
        ),
        (
            "Руины бывшего оживлённого центра Мечты — затопленный городской пустырь, "
            "оплетённый кибернетическими проводами. Тёмный, зловонный, тихий. "
            "Проверка на Заражение каждый час без Защитного/Вакуум/Экзокостюма. "
            "6 часов из конца в конец; ~2 часа до любой смежной локации. Встречи раз/час.\n\n"
            "1. ВОДОПАД. Двадцатиэтажный водопад токсической грязи. Проверка Силы без снаряжения. "
            "Отто-Хунглунг продаёт снаряжение (1 баллон O2/набор или 2 ккр; 5% что сломано). "
            "500кр за карту до Доктора.\n\n"
            "2. ДОКТОР. Спрятан за грязевым водопадом — пульсирующий тоннель, "
            "самодельная операционная из ампутированных конечностей. Доктор Банкали "
            "работает над Хунглунгом. Стат: C:65, СКР:75, ИНС:65, H:2(20). Лечит Ариэль. "
            "Если убит → Вспышка Фаза 3. По просьбе вживит 'жабры'.\n\n"
            "3. СТАРЫЙ ГОРОД. Рушащиеся здания (1d5×10 этажей), канализация, Чокеспауны. "
            "Ориентиры (~1 час до каждого): Башня Юно (34 этажа, снайпер Tempest), "
            "Метро (быстрый путь в Вены/Братскую Могилу после подачи питания), "
            "Форпост (1d5 параноидальных Операторов), Канализация (100' вниз → Могила/Норы), "
            "Архивы (история Доктора Банкали).\n\n"
            "4. БРАТСКАЯ МОГИЛА. 'Даже если ты не можешь дышать, ты не заслуживаешь "
            "умереть здесь.' Куча трупов высотой в этаж. Спасбросок от Страха или 1d5 Стресса. "
            "25% шанс найти кибермод (2 броска на Мутации + [-] на Спасброски против Калибана).\n\n"
            "5. ВЕНЫ. Трубы дренажа, вентиляционные шахты, технические тоннели, "
            "связывающие все модули. Следуйте символам Хунглунгов. 2d10 часов до любого "
            "модуля. Уродливый оrifice у Доктора ведёт в Атриум Сердца Калибана."
        ),
        (
            "Руїни колишнього центру Мрії — затоплений міський пустир, обплетений "
            "кібернетичними дротами. Темний, смердючий, тихий. "
            "Перевірка на Зараження кожну годину без Захисного/Вакуум/Екзокостюма. "
            "6 годин із кінця в кінець; ~2 год до будь-якої суміжної локації. Зустрічі раз/год.\n\n"
            "1. ВОДОСПАД. Двадцятиповерховий токсичний брудний водоспад. Перевірка Сили без спорядження. "
            "Старий Хунглунг Отто продає спорядження (1 балон O2/набір або 2 ккр; 5% що зламано). "
            "500 кр за карту до Лікаря.\n\n"
            "2. ЛІКАР. Захований за брудним водоспадом — пульсуючий тунель, "
            "саморобна операційна з ампутованих кінцівок. Доктор Банкалі "
            "працює над Хунглунгом. Стат: C:65, ШВ:75, ІНС:65, H:2(20). Лікує Аріель. "
            "Якщо вбитий → Спалах Фаза 3. На прохання вживить 'зябра'.\n\n"
            "3. СТАРЕ МІСТО. Будинки, що руйнуються (1d5×10 поверхів), каналізація, Чокеспауни. "
            "Орієнтири (~1 год до кожного): Вежа Юно (34 поверхи, снайпер Tempest), "
            "Метро (швидкий шлях у Вени/Братську Могилу після подачі живлення), "
            "Форпост (1d5 параноїчних Операторів), Каналізація (30 м вниз → Могила/Нори), "
            "Архіви (історія Доктора Банкалі).\n\n"
            "4. БРАТСЬКА МОГИЛА. 'Навіть якщо ти не можеш дихати, ти не заслуговуєш "
            "вмерти тут.' Купа трупів заввишки в поверх. Рятівний кидок від Страху або 1d5 Стресу. "
            "25% шанс знайти кіберімплант (2 кидки на Мутації + [-] на Рятівні кидки проти Калібана).\n\n"
            "5. ВЕНИ. Дренажні труби, вентиляційні шахти, технічні тунелі, "
            "що зв'язують усі модулі. Слідуйте символам Хунглунгів. 2d10 годин до будь-якого "
            "модуля. Потворний отвір біля Лікаря веде в Атріум Серця Калібана."
        ),
        None, None, None,
    ),
    # ── C249 Life Support 01 ──────────────────────────────────────────────────
    (
        249, "💨", "apof_life_support", 5, None,
        "Life Support 01",
        "Система ЖО 01",
        "Система ЖЗ 01",
        (
            "The only remaining semi-functional life support unit in The Choke. "
            "Mood: No light. Loud thrumming machinery. Floors groan.\n\n"
            "1. MASSIVE CRACKED DOOR. Encrusted with cables and wires. Too heavy without "
            "heavy construction equipment or an Exosuit.\n"
            "1A. HIDDEN ENTRANCE. Spend time searching to find a gap where a fallen tower "
            "(EST-03) has gouged a hole. Bulky armor users risk suit damage.\n\n"
            "2. CONTROL ROOMS. Decayed terminal banks. One salvageable terminal contains a "
            "map of The Veins. Rusty staircase — collapses if more than one person climbs.\n\n"
            "3. PROCESSING PLANT. Quiet save for O2 scrubbers. Booby-trapped staircase "
            "(noisemaker). Cart of dirty uniforms hides entrance to The Outpost (4).\n\n"
            "4. OUTPOST. Dingy safehouse. Bloodless corpse in corner. Pulse rifle ammo + "
            "×3 O2 tanks (1d10 hrs each).\n\n"
            "5. THE FILTER. Replace in 1 hour with a new filter, or 3d10 hours to scrub "
            "the old one (lasts 4d10 days).\n\n"
            "GUILE OF CALIBAN\n"
            "C:40 (Slash×2 2d10, Tranq Lash, Bloodsucker Bite) INST:65 ARMOR:80 H:3(35)\n"
            "• Tranq Lash: Body Save or unconscious 1d5 rounds.\n"
            "• Bloodsucker Bite: 1d10dmg (×2 if unconscious); heals 1 Hit.\n"
            "Fast six-armed beast. Silent. Crawls walls/ceilings. Ambushes then retreats. "
            "Always runs after losing a Hit."
        ),
        (
            "Единственная оставшаяся полуфункциональная система жизнеобеспечения в Удавке. "
            "Атмосфера: Темнота. Громкое гудение машин. Полы стонут.\n\n"
            "1. ОГРОМНАЯ ТРЕСНУВШАЯ ДВЕРЬ. Покрыта кабелями и проводами. Слишком тяжела "
            "без тяжёлой строительной техники или Экзокостюма.\n"
            "1А. СКРЫТЫЙ ВХОД. При тщательном поиске — пробоина от упавшей башни "
            "(EST-03). Владельцы громоздкой брони рискуют повредить её.\n\n"
            "2. КОМНАТЫ УПРАВЛЕНИЯ. Гнилые терминалы. Один рабочий — карта Вен. "
            "Ржавая лестница — рухнет, если залезет более одного человека.\n\n"
            "3. ПЕРЕРАБАТЫВАЮЩИЙ ЦЕХ. Тихо, кроме гудения скрубберов O2. "
            "Заминированная лестница (шумовая). Тележка с грязной одеждой скрывает вход в Форпост (4).\n\n"
            "4. ФОРПОСТ. Мрачное убежище. Трупы без крови в углу. Патроны к пульсовой "
            "винтовке + ×3 баллона O2 (1d10 ч. каждый).\n\n"
            "5. ФИЛЬТР. Замена нового — 1 час. Чистка старого — 3d10 часов (служит 4d10 дней).\n\n"
            "ХИТРОСТЬ КАЛИБАНА\n"
            "C:40 (Удар×2 2d10, Транквилизатор, Укус кровопийцы) ИНС:65 БРОНЯ:80 H:3(35)\n"
            "• Транквилизатор: Спасбросок Тела или без сознания 1d5 раундов.\n"
            "• Укус кровопийцы: 1d10 урона (×2 если без сознания); восстанавливает 1 Hit.\n"
            "Быстрое шестирукое существо. Тихое. Ползает по стенам/потолкам. "
            "Нападает из засады, отступает. Всегда убегает, потеряв Hit."
        ),
        (
            "Єдина наявна напівфункціональна система життєзабезпечення в Задуші. "
            "Атмосфера: Темрява. Гучний гул машин. Підлоги стогнуть.\n\n"
            "1. ВЕЛИЧЕЗНІ ТРІСНУТІ ДВЕРІ. Вкриті кабелями й дротами. Занадто важкі "
            "без важкого будівельного обладнання або Екзокостюма.\n"
            "1А. ПРИХОВАНИЙ ВХІД. Ретельний пошук виявляє пробоїну від впалої вежі "
            "(EST-03). Власники громіздкої броні ризикують її пошкодити.\n\n"
            "2. КІМНАТИ УПРАВЛІННЯ. Прогнилі термінали. Один робочий — карта Вен. "
            "Іржаві сходи — впадуть, якщо піде більше однієї людини.\n\n"
            "3. ПЕРЕРОБНИЙ ЦЕХ. Тихо, крім гудіння скруберів O2. "
            "Заміновані сходи (шумова пастка). Тачка з брудним одягом ховає вхід до Форпосту (4).\n\n"
            "4. ФОРПОСТ. Похмуре сховище. Безкровний труп у кутку. Патрони до імпульсної "
            "гвинтівки + ×3 балони O2 (1d10 год. кожен).\n\n"
            "5. ФІЛЬТР. Заміна нового — 1 година. Чистка старого — 3d10 годин (служить 4d10 днів).\n\n"
            "ХИТРІСТЬ КАЛІБАНА\n"
            "C:40 (Удар×2 2d10, Транквілізатор, Укус кровопийці) ІНС:65 БРОНЯ:80 H:3(35)\n"
            "• Транквілізатор: Рятівний кидок Тіла або без свідомості 1d5 раундів.\n"
            "• Укус кровопийці: 1d10 шкоди (×2 якщо без свідомості); відновлює 1 Hit.\n"
            "Швидке шестируке створіння. Тихе. Повзає по стінах/стелях. "
            "Нападає з засідки, відступає. Завжди тікає, втративши Hit."
        ),
        None, None, None,
    ),
    # ── C250 The Burrows ──────────────────────────────────────────────────────
    (
        250, "🕸️", "apof_the_burrows", 6, None,
        "The Burrows",
        "Норы",
        "Нори",
        (
            "A cluster of cybernetic veins the size of corridors. Its slick, fleshy walls spawn "
            "swarms of Husks. The only place to harvest fruit which becomes Sycorax.\n\n"
            "HUSKS (SWARM)\n"
            "C:X×10 (Mindless clawing Xd10dmg) SPD:20 INST:20 H:1d10(5)\n"
            "Swarm: Hits = number of creatures. Combat/damage based on current Hits.\n"
            "Half-formed clones with sanded features. No eyes or orifices. "
            "Grow from walls, slide off when finished.\n\n"
            "1. THE BIG WALL. Giant patch of hive-like burrows at the edge of The Sink. "
            "One burrow glows dimly. Climb in → wet closed orifice opens at 2d10dmg. "
            "Leads to burrow chambers.\n\n"
            "2. DEAD HUNGLUNG. Flesh has started to reclaim him. Scalpel in one hand, "
            "'He's coming for you' carved into the other.\n\n"
            "3. GENE POOL. 2d10 Doptownians (or important NPC) stuck to the flesh. "
            "They merge with Caliban in 1d10 rounds if not removed (Strength Check). "
            "Large sphincter in floor: if stepped on reveals sliding tunnel to Caliban's Heart."
        ),
        (
            "Лабиринт кибернетических вен размером с коридоры. Скользкие, мясистые стены "
            "порождают стаи Хасков. Единственное место сбора плодов для производства Сикоракса.\n\n"
            "ХАСКИ (РОЙ)\n"
            "C:X×10 (Бездумные когти Xd10 урона) СКР:20 ИНС:20 H:1d10(5)\n"
            "Рой: Удары = количество существ. Бой/урон = текущие Удары.\n"
            "Полуготовые клоны без черт лица. Без глаз и отверстий. "
            "Вырастают из стен, сползают когда готовы.\n\n"
            "1. БОЛЬШАЯ СТЕНА. Гигантский улей нор на краю Провала. "
            "Одна нора тускло светится. Залезть → закрытое мокрое отверстие открывается при 2d10 урона. "
            "Ведёт в камеры нор.\n\n"
            "2. МЁРТВЫЙ ХУНГЛУНГ. Плоть начала поглощать его. Скальпель в одной руке, "
            "'Он идёт за тобой' вырезано на другой.\n\n"
            "3. ГЕНЕТИЧЕСКИЙ ПУЛ. 2d10 Доптаунцев (или важный НИП) прилипли к плоти. "
            "Они сливаются с Калибаном за 1d10 раундов (Проверка Силы для освобождения). "
            "Большой сфинктер в полу → скользящий тоннель к Сердцу Калибана."
        ),
        (
            "Лабіринт кібернетичних вен завширшки з коридори. Слизькі, м'ясисті стіни "
            "породжують рої Хасків. Єдине місце збору плодів для виробництва Сикоракса.\n\n"
            "ХАСКИ (РІЙ)\n"
            "C:X×10 (Бездумні кігті Xd10 шкоди) ШВ:20 ІНС:20 H:1d10(5)\n"
            "Рій: Удари = кількість істот. Бій/шкода = поточні Удари.\n"
            "Напівготові клони без рис обличчя. Без очей і отворів. "
            "Виростають зі стін, сповзають коли готові.\n\n"
            "1. ВЕЛИКА СТІНА. Гігантський вулик нір на краю Провалу. "
            "Одна нора тьмяно світиться. Залізти → закритий мокрий отвір відкривається при 2d10 шкоди. "
            "Веде до камер нір.\n\n"
            "2. МЕРТВИЙ ХУНГЛУНГ. Плоть почала поглинати його. Скальпель в одній руці, "
            "'Він іде за тобою' вирізано на іншій.\n\n"
            "3. ГЕНЕТИЧНИЙ ПУЛ. 2d10 Доптаунців (або важливий НГП) прилипли до плоті. "
            "Вони зливаються з Калібаном за 1d10 раундів (Перевірка Сили для звільнення). "
            "Великий сфінктер у підлозі → ковзний тунель до Серця Калібана."
        ),
        None, None, None,
    ),
    # ── C251 Caliban's Heart ──────────────────────────────────────────────────
    (
        251, "💀", "apof_calibans_heart", 7, None,
        "Caliban's Heart",
        "Сердце Калибана",
        "Серце Калібана",
        (
            "A slick wet pit of cybernetic and organic fusion. Wire tendrils seek to merge with "
            "living tissue. Every turn roll 1d10: on 1–5 the location floods with tendrils — "
            "everyone knocked to the floor + Infection Check. On Critical Fail you begin to merge: "
            "1d5 rounds, Strength Check to be pulled free.\n\n"
            "1. FLOODED ATRIUM. The Jealousy of Caliban is slumped in a corner, half-sunken "
            "in dark blood. Attacks anyone who isn't Infected, otherwise ignores PCs.\n"
            "JEALOUSY: C:80 (Bash 5d10, Fleshcannon 3d10) SPD:10 INST:20 H:5(45)\n"
            "Fleshcannon: disgorged limbs/viscera — Infection Check at [-].\n\n"
            "2. COLLAPSED VENTRICLE. 100s of terminal monitors fused into the bulkhead "
            "(each shows an unblinking eye — Sanity Save or 1d5 Stress). Password-protected "
            "console (ARIEL) allows surveillance of anyone on The Dream.\n\n"
            "3. ROTTING CHAMBER. Avatar of Caliban on a throne of disfigured cyborgs. "
            "Killing the Avatar + donning the crown grants total control of The Dream's systems. "
            "Sanity Save [-] to remove crown; impossible without killing user.\n"
            "AVATAR: C:80 (Tendril/Tendril 2d10+Infection) SPD:45 INST:65 H:5(50)\n"
            "Awful Crown: commands any machine; cybermods/slickware/Androids get Sanity Save.\n\n"
            "4. ATRIUM. 3d10 denizens hang on meathooks. Fist-sized Cyberleeches (C:45 "
            "Infection Check, H:1) slowly digest bodies. Orifice in floor → The Doctor.\n\n"
            "5. INNER CHAMBER. Dark, towering, quiet. Caliban fused into the wall — "
            "pathetic and mutilated, unrecognizable, machine-assisted breathing. "
            "A child-sized black box holds Ariel, Dr. Bancali's daughter: alive but unaging "
            "for 23 years. She will die if removed from the box. Caliban exists only to keep her alive.\n"
            "CALIBAN: C:50 SPD:50 INST:85 H:2(200). Cannot fight; calls Chokespawn/Husks. "
            "If original form killed → Dream self-destructs in 1d10 hours."
        ),
        (
            "Влажная яма киберорганического слияния. Проволочные щупальца ищут живую ткань. "
            "Каждый раунд 1d10: на 1–5 щупальца затопляют локацию — все на пол + Проверка Заражения. "
            "На крит. провале начинается слияние: 1d5 раундов, Проверка Силы чтобы вырваться.\n\n"
            "1. ЗАТОПЛЕННЫЙ АТРИУМ. Зависть Калибана сидит в углу, наполовину утопая "
            "в тёмной крови. Атакует незаражённых, остальных игнорирует.\n"
            "ЗАВИСТЬ: C:80 (Удар 5d10, Мясопушка 3d10) СКР:10 ИНС:20 H:5(45)\n"
            "Мясопушка: конечности/внутренности — Проверка Заражения с [-].\n\n"
            "2. ОБРУШЕННЫЙ ЖЕЛУДОЧЕК. Сотни мониторов с немигающим глазом "
            "(Спасбросок Рассудка или 1d5 Стресса). Консоль (пароль ARIEL) позволяет "
            "следить за кем угодно на Мечте.\n\n"
            "3. ГНИЛАЯ КАМЕРА. Аватар Калибана на троне из киборгов. Убить + надеть корону "
            "= полный контроль над Мечтой. Спасбросок Рассудка [-] чтобы снять корону.\n"
            "АВАТАР: C:80 (Щупальце/Щупальце 2d10+Заражение) СКР:45 ИНС:65 H:5(50)\n"
            "Ужасная Корона: командует любыми машинами; кибермоды/слик-ПО/Андроиды — Спасбросок Рассудка.\n\n"
            "4. АТРИУМ. 3d10 жителей на мясных крюках. Кибервиявки (C:45 Проверка Заражения, H:1). "
            "Отверстие в полу → Доктор.\n\n"
            "5. ВНУТРЕННЯЯ КАМЕРА. Тёмный, высокий, тихий. Калибан вплавлен в стену — "
            "жалкий и изувеченный, неузнаваемый, дышит с помощью машины. "
            "Чёрный ящик размером с ребёнка хранит Ариэль — жива, но не стареет 23 года. "
            "Умрёт, если убрать из ящика. Калибан существует только ради неё.\n"
            "КАЛИБАН: C:50 СКР:50 ИНС:85 H:2(200). Не сражается; призывает Чокеспаунов/Хасков. "
            "Если убит → Мечта самоуничтожится через 1d10 часов."
        ),
        (
            "Волога яма кіберорганічного злиття. Дротяні щупальці шукають живу тканину. "
            "Кожен раунд 1d10: на 1–5 щупальці затоплюють локацію — всі на підлогу + Перевірка Зараження. "
            "На крит. провалі починається злиття: 1d5 раундів, Перевірка Сили щоб вирватись.\n\n"
            "1. ЗАТОПЛЕНИЙ АТРІУМ. Заздрість Калібана сидить у кутку, наполовину занурена "
            "в темну кров. Атакує незаражених, решту ігнорує.\n"
            "ЗАЗДРІСТЬ: C:80 (Удар 5d10, М'ясогармата 3d10) ШВ:10 ІНС:20 H:5(45)\n"
            "М'ясогармата: кінцівки/нутрощі — Перевірка Зараження з [-].\n\n"
            "2. ОБВАЛЕНИЙ ШЛУНОЧОК. Сотні моніторів з немиготливим оком "
            "(Рятівний кидок Розуму або 1d5 Стресу). Консоль (пароль ARIEL) дає змогу "
            "стежити за будь-ким на Мрії.\n\n"
            "3. ГНИЛА КАМЕРА. Аватар Калібана на троні з кіборгів. Вбити + надіти корону "
            "= повний контроль над Мрією. Рятівний кидок Розуму [-] щоб зняти корону.\n"
            "АВАТАР: C:80 (Щупальце/Щупальце 2d10+Зараження) ШВ:45 ІНС:65 H:5(50)\n"
            "Жахлива Корона: командує будь-якими машинами; кіберімпланти/слік-ПЗ/Андроїди — Рятівний кидок Розуму.\n\n"
            "4. АТРІУМ. 3d10 мешканців на м'ясних гаках. Кіберп'явки (C:45 Перевірка Зараження, H:1). "
            "Отвір у підлозі → Лікар.\n\n"
            "5. ВНУТРІШНЯ КАМЕРА. Темна, висока, тиха. Калібан вплавлений у стіну — "
            "жалюгідний і понівечений, невпізнанний, дихає з допомогою машини. "
            "Чорна скринька розміром з дитину зберігає Аріель — жива, але не старіє 23 роки. "
            "Помре, якщо вийняти зі скриньки. Калібан існує лише заради неї.\n"
            "КАЛІБАН: C:50 ШВ:50 ІНС:85 H:2(200). Не б'ється; кличе Чокеспаунів/Хасків. "
            "Якщо вбитий → Мрія самознищиться за 1d10 годин."
        ),
        None, None, None,
    ),
    # ── C252 Chokespawn Table (d10) ───────────────────────────────────────────
    (
        252, "🧬", "apof_chokespawn", 8, 10,
        "Chokespawn",
        "Чокеспаун",
        "Чокеспаун",
        "Roll d10 for Base Form. Each entry also lists a Unique Feature and Special Attack.",
        "Бросьте d10 для Базовой Формы. Каждый результат содержит Уникальную черту и Особую атаку.",
        "Киньте d10 для Базової Форми. Кожен результат містить Унікальну рису і Особливу атаку.",
        [
            "Disfigured Human Child — C:20 1d5dmg S:50 I:20 H:1 | Feature: Hideous — Gain 1 Stress; Fear Save or cower 1d5[+] rounds | Attack: Begs You To Kill It — Sanity Save or 1 Stress/round",
            "1d10 Skittering Rats — C:30 1d10dmg I:25 S:55 H:1 | Feature: Survivor — +10 Combat, +1d10dmg, +1 Hit, +5 Health | Attack: Crawls All Over You — Fear Save or Panic Check",
            "1d10 Feral Dogs — C:45 2d10dmg I:55 S:65 H:1(15) | Feature: Machine-mesh — overflowing cybermods, takes ½dmg | Attack: Howl — 50% chance 1d5 identical Chokespawn arrive in 1d10 rounds",
            "Infected Hybrid Human — C:50 2d10dmg I:45 S:45 H:2(10) | Feature: Conjoined — Roll 2nd Base Form, take highest stats, +1 Special Attack | Attack: Acid Vomit — Armor Save fail: Armor –5% and +1 Stress",
            "2d10 Throbbing Eggs — C:0 S:0 I:0 H:2(20) | Feature: Cocoon — Inert; hatches 1d10 rounds with +10 Combat and +10dmg | Attack: Noxious Spray — Body Save or raise Infection Level by 1",
            "Centipede of Discarded Limbs — C:65 3d10dmg S:55 I:70 H:3(40) | Feature: Mass of Limbs — can act 1d5 times/round, +1 Special Attack | Attack: Swallow — Body Save or ingested whole; 1d10dmg/round until 1 Hit dealt",
            "Mechanical Spider — C:70 3d10dmg S:55 I:75 H:4(12) | Feature: Egg Sack — after 20dmg sack splits, spews 1d10 Chokespawn | Attack: Infect — Infection Check whenever you are hit",
            "Tangled Wires & Cables — C:75 4d10dmg S:65 I:50 H:3(30) | Feature: Morph — after 1d5 rounds changes Base Form; add new form's Hits and damage | Attack: Snatch — Body Save or grabbed and prone; next attack auto-hits",
            "Pulsating Flesh Sack — C:0 S:10 I:10 H:1(100) | Feature: Mitosis — every 1d10 rounds divides into a copy of itself | Attack: Pseudopod — new limb sprouts; Chokespawn gains +1 action/round",
            "Grotesque (2 Unique Features) — C:65 1d10dmg S:25 I:45 H:3(50) | Feature: Engorged — 3× as large, +20 Health, double damage | Attack: Body Snatcher — Body[+] Save or next turn taken by the Warden",
        ],
        [
            "Изуродованный человеческий ребёнок — C:20 1d5 уд. S:50 I:20 H:1 | Черта: Ужасающий — +1 Стресс; Спасбросок Страха или оцепенение 1d5[+] раундов | Атака: Умоляет убить — Спасбросок Рассудка или 1 Стресс/раунд",
            "1d10 скуттерных крыс — C:30 1d10 уд. I:25 S:55 H:1 | Черта: Выживший — +10 Бой, +1d10 урона, +1 Hit, +5 Здоровья | Атака: Облепляет — Спасбросок Страха или Проверка Паники",
            "1d10 одичавших собак — C:45 2d10 уд. I:55 S:65 H:1(15) | Черта: Машинная сетка — переполнен кибермодами, получает ½ урона | Атака: Вой — 50% шанс 1d5 идентичных Чокеспаунов через 1d10 раундов",
            "Заражённый гибридный человек — C:50 2d10 уд. I:45 S:45 H:2(10) | Черта: Сросшийся — бросить 2-ю Форму, взять лучшую статистику, +1 Атака | Атака: Кислотная рвота — при провале Брони: Броня –5% и +1 Стресс",
            "2d10 пульсирующих яиц — C:0 S:0 I:0 H:2(20) | Черта: Кокон — Инертный; вылупляется через 1d10 раундов с +10 Бой и +10 урона | Атака: Зловонный спрей — Спасбросок Тела или повысить Уровень Заражения на 1",
            "Сороконожка из отброшенных конечностей — C:65 3d10 уд. S:55 I:70 H:3(40) | Черта: Масса конечностей — действует 1d5 раз/раунд, +1 Атака | Атака: Проглотить — Спасбросок Тела или проглочен целиком; 1d10 урона/раунд до 1 Hit",
            "Механический паук — C:70 3d10 уд. S:55 I:75 H:4(12) | Черта: Яйцевой мешок — после 20 урона лопается, выпуская 1d10 Чокеспаунов | Атака: Заразить — Проверка Заражения при каждом попадании",
            "Сплетение проводов и кабелей — C:75 4d10 уд. S:65 I:50 H:3(30) | Черта: Оборотень — через 1d5 раундов меняет форму; добавить Hits и урон новой формы | Атака: Захват — Спасбросок Тела или схвачен/лежит; следующая атака авто-попадает",
            "Пульсирующий мешок плоти — C:0 S:10 I:10 H:1(100) | Черта: Митоз — каждые 1d10 раундов делится на копию себя | Атака: Псевдоподия — вырастает новая конечность; +1 действие/раунд",
            "Гротеск (2 Уникальных черты) — C:65 1d10 уд. S:25 I:45 H:3(50) | Черта: Раздутый — ×3 размер, +20 Здоровья, двойной урон | Атака: Похититель тел — Тело[+] Спасбросок или следующий ход перехватит Ведущий",
        ],
        [
            "Спотворена людська дитина — C:20 1d5 уд. S:50 I:20 H:1 | Риса: Жахливий — +1 Стрес; Рятівний кидок Страху або оцепеніння 1d5[+] раундів | Атака: Благає вбити — Рятівний кидок Розуму або 1 Стрес/раунд",
            "1d10 скуттерних щурів — C:30 1d10 уд. I:25 S:55 H:1 | Риса: Виживший — +10 Бій, +1d10 шкоди, +1 Hit, +5 Здоров'я | Атака: Обліпляє — Рятівний кидок Страху або Перевірка Паніки",
            "1d10 здичавілих собак — C:45 2d10 уд. I:55 S:65 H:1(15) | Риса: Машинна сітка — переповнений кіберімплантами, отримує ½ шкоди | Атака: Вий — 50% шанс 1d5 ідентичних Чокеспаунів через 1d10 раундів",
            "Заражений гібридний людина — C:50 2d10 уд. I:45 S:45 H:2(10) | Риса: Зрощений — кинути 2-у Форму, взяти кращу статистику, +1 Атака | Атака: Кислотне блювання — при провалі Броні: Броня –5% і +1 Стрес",
            "2d10 пульсуючих яєць — C:0 S:0 I:0 H:2(20) | Риса: Кокон — Інертний; вилуплюється через 1d10 раундів з +10 Бій і +10 шкоди | Атака: Смердючий спрей — Рятівний кидок Тіла або підвищити Рівень Зараження на 1",
            "Сороконіжка з відкинутих кінцівок — C:65 3d10 уд. S:55 I:70 H:3(40) | Риса: Маса кінцівок — діє 1d5 разів/раунд, +1 Атака | Атака: Проковтнути — Рятівний кидок Тіла або проковтнутий цілком; 1d10 шкоди/раунд до 1 Hit",
            "Механічний павук — C:70 3d10 уд. S:55 I:75 H:4(12) | Риса: Яйцевий мішок — після 20 шкоди лопається, випускаючи 1d10 Чокеспаунів | Атака: Заразити — Перевірка Зараження при кожному влученні",
            "Сплетіння дротів і кабелів — C:75 4d10 уд. S:65 I:50 H:3(30) | Риса: Перевертень — через 1d5 раундів змінює форму; додати Hits і шкоду нової форми | Атака: Захоплення — Рятівний кидок Тіла або схоплений/лежить; наступна атака авто-влучає",
            "Пульсуючий мішок плоті — C:0 S:10 I:10 H:1(100) | Риса: Мітоз — кожні 1d10 раундів ділиться на копію себе | Атака: Псевдоподія — виростає нова кінцівка; +1 дія/раунд",
            "Гротеск (2 Унікальні риси) — C:65 1d10 уд. S:25 I:45 H:3(50) | Риса: Роздутий — ×3 розмір, +20 Здоров'я, подвійна шкода | Атака: Викрадач тіл — Тіло[+] Рятівний кидок або наступний хід перехопить Провідник",
        ],
    ),
    # ── C253 The Choke Encounters (d10) ──────────────────────────────────────
    (
        253, "🗺️", "apof_choke_encounters", 9, 10,
        "The Choke/Sink Encounters",
        "Встречи в Удавке/Провале",
        "Зустрічі в Задуші/Провалі",
        "Roll d10 once per hour while travelling in The Choke or The Sink.",
        "Бросайте d10 раз в час при путешествии по Удавке или Провалу.",
        "Кидайте d10 раз на годину під час подорожі по Задуші або Провалу.",
        [
            "Discarded O2 tank. 1d10 hours remaining.",
            "Septic Wave. Fear Save or be split up.",
            "Sinkhole. Body Save or fall to lower level. Take 1d10dmg.",
            "Doptownian looking for a place to die.",
            "2d10 Hunglungs [C:25 Spears 2d10dmg S:10 I:25 H:1] waiting in ambush.",
            "1d10 Hunglung Engineers heading to Life Support 01, dragging a huge replacement filter. Without help they won't survive the trip.",
            "1d5 Tempest Operators [C:35 Pulse Rifle 5d10dmg S:30 I:25 H:2] lost and paranoid.",
            "Chokespawn (roll on Chokespawn table).",
            "1d10 Chokespawn.",
            "The Wire Man: 10-story tall faceless behemoth built entirely of wires. Stomps reverberate across The Sink. Easy to hide from but peers into cracks and windows. Swipe 1d10dmg, Body Save for half. H:5(200). Retreats after losing a Hit.",
        ],
        [
            "Выброшенный баллон O2. 1d10 часов осталось.",
            "Септическая волна. Спасбросок Страха или группа разделяется.",
            "Провал в полу. Спасбросок Тела или упасть на нижний уровень. 1d10 урона.",
            "Доптаунец в поисках места умереть.",
            "2d10 Хунглунгов [C:25 Копья 2d10 уд. S:10 I:25 H:1] в засаде.",
            "1d10 Инженеров Хунглунгов направляются в Систему ЖО 01, тащат огромный сменный фильтр. Без помощи они не доберутся.",
            "1d5 Операторов Tempest [C:35 Импульсная винтовка 5d10 уд. S:30 I:25 H:2] заблудились и параноят.",
            "Чокеспаун (бросок по таблице Чокеспаунов).",
            "1d10 Чокеспаунов.",
            "Проволочный Человек: 10-этажный безликий монстр из проводов. Шаги ощущаются по всему Провалу. Легко спрятаться, но он заглядывает в щели и окна. Удар 1d10 уд., Спасбросок Тела для половины. H:5(200). Отступает, потеряв Hit.",
        ],
        [
            "Викинутий балон O2. 1d10 годин залишилось.",
            "Септична хвиля. Рятівний кидок Страху або група розділяється.",
            "Провал у підлозі. Рятівний кидок Тіла або впасти на нижній рівень. 1d10 шкоди.",
            "Доптаунець, що шукає місце померти.",
            "2d10 Хунглунгів [C:25 Списи 2d10 уд. S:10 I:25 H:1] у засідці.",
            "1d10 Інженерів Хунглунгів прямують до Системи ЖЗ 01, тягнуть величезний замінний фільтр. Без допомоги вони не доберуться.",
            "1d5 Операторів Tempest [C:35 Імпульсна гвинтівка 5d10 уд. S:30 I:25 H:2] заблукали і параноять.",
            "Чокеспаун (кидок по таблиці Чокеспаунів).",
            "1d10 Чокеспаунів.",
            "Дротяна Людина: 10-поверховий безликий монстр з дротів. Кроки відчуваються по всьому Провалу. Легко сховатися, але він заглядає в щілини і вікна. Удар 1d10 уд., Рятівний кидок Тіла для половини. H:5(200). Відступає, втративши Hit.",
        ],
    ),
]


BASE = "images/A Pound of Flesh/ProsperosDreamLocs"
CONTENT_IMAGES: dict[int, str] = {
    245: f"{BASE}/9.DopTown.png",
    248: f"{BASE}/10.TheSink.png",
    249: f"{BASE}/TheSinkLocs/LifeSupport.png",
    250: f"{BASE}/TheSinkLocs/TheBurrows.png",
    251: f"{BASE}/TheSinkLocs/CalibansHeart.png",
}

# Items NOT inserted into P36 page_contents.
# C245/C247 go to P35 (see P35_PLACEMENTS below).
# C246, C248–C253 are accessible only via content_links from their parents.
SUB_ITEMS = {
    245, 247,         # Doptown/The Choke → placed on P35, not P36
    246,              # Doptown NPCs & Encounters → sub of C245
    248, 249, 250, 251, 252, 253,  # Choke sub-locations → sub of C247
}

# C245/C247 are placed on P35 (The Station) at these sort positions.
P35_PLACEMENTS = [
    (245, 22),   # 09 Doptown
    (247, 23),   # 10 The Choke
]

# Forward content_links: (from_id, to_id, sort_order)
SUB_LINKS = [
    (245, 246, 0),   # 09 Doptown → Doptown NPCs & Encounters
    (247, 248, 0),   # 10 The Choke → The Sink (see_also set by update script)
    (247, 249, 1),   # 10 The Choke → Life Support 01
    (247, 250, 2),   # 10 The Choke → The Burrows
    (247, 251, 3),   # 10 The Choke → Caliban's Heart
    (247, 252, 4),   # 10 The Choke → Chokespawn
    (247, 253, 5),   # 10 The Choke → The Choke/Sink Encounters
]


def _insert_content(conn: sqlite3.Connection, page_id: int, item: tuple) -> None:
    (cid, icon, slug, sort_order, dice_sides,
     name_en, name_ru, name_ua,
     desc_en, desc_ru, desc_ua,
     dice_en, dice_ru, dice_ua) = item

    dice_json = json.dumps({"sides": dice_sides}) if dice_sides else None
    image_url = CONTENT_IMAGES.get(cid)

    conn.execute("""
        INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order, image_url)
        VALUES (?, ?, 'apof', NULL, ?, ?, ?)
    """, (cid, icon, dice_json, sort_order, image_url))
    if image_url:
        conn.execute(
            "UPDATE contents SET image_url = ? WHERE id = ? AND image_url IS NULL",
            (image_url, cid),
        )

    for lang, name, desc, dice_entries in [
        ("en", name_en, desc_en, dice_en),
        ("ru", name_ru, desc_ru, dice_ru),
        ("ua", name_ua, desc_ua, dice_ua),
    ]:
        entries_json = json.dumps(dice_entries) if dice_entries else None
        conn.execute("""
            INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)
            VALUES (?, ?, ?, ?, ?)
        """, (cid, lang, name, desc, entries_json))

    if cid not in SUB_ITEMS:
        conn.execute("""
            INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
            VALUES (?, ?, ?)
        """, (page_id, cid, sort_order))


def _seed(conn: sqlite3.Connection) -> None:
    for item in ITEMS:
        _insert_content(conn, PAGE_ID, item)

    # Place Doptown and The Choke on P35 (The Station), not P36
    for cid, sort_order in P35_PLACEMENTS:
        conn.execute(
            "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (35, ?, ?)",
            (cid, sort_order),
        )

    for from_id, to_id, sort in SUB_LINKS:
        conn.execute(
            "INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key, sort_order) VALUES (?, ?, 'related', ?)",
            (from_id, to_id, sort),
        )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(ITEMS)} contents added to P{PAGE_ID} (The Deep).")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
