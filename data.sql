-- sources
INSERT OR IGNORE INTO "sources" VALUES(1,'psg','Player''s Survival Guide','core');
INSERT OR IGNORE INTO "sources" VALUES(2,'wom','Warden''s Operations Manual','supplement');
-- pages
INSERT OR IGNORE INTO "pages" VALUES(1,'🚀',NULL,NULL,'[22, 3, 11, 23]');
INSERT OR IGNORE INTO "pages" VALUES(2,'🔫','psg',NULL,'[]');
INSERT OR IGNORE INTO "pages" VALUES(3,'⚔️','psg',26,'[5, 4]');
INSERT OR IGNORE INTO "pages" VALUES(4,'💀','psg',29,'[]');
INSERT OR IGNORE INTO "pages" VALUES(5,'📏','psg',30,'[]');
INSERT OR IGNORE INTO "pages" VALUES(6,'🛡️','psg',NULL,'[]');
INSERT OR IGNORE INTO "pages" VALUES(7,'📋','psg',4,'[8, 9]');
INSERT OR IGNORE INTO "pages" VALUES(8,'🎭','psg',5,'[]');
INSERT OR IGNORE INTO "pages" VALUES(9,'🎲','psg',7,'[]');
INSERT OR IGNORE INTO "pages" VALUES(10,'🎒','psg',10,'[]');
INSERT OR IGNORE INTO "pages" VALUES(11,'📖','psg',18,'[12, 13, 14, 15]');
INSERT OR IGNORE INTO "pages" VALUES(12,'😰','psg',20,'[]');
INSERT OR IGNORE INTO "pages" VALUES(13,'🧠','psg',22,'[16, 17, 18, 19]');
INSERT OR IGNORE INTO "pages" VALUES(14,'🌍','psg',32,'[]');
INSERT OR IGNORE INTO "pages" VALUES(15,'🏥','psg',34,'[]');
INSERT OR IGNORE INTO "pages" VALUES(16,'📚','psg',22,'[]');
INSERT OR IGNORE INTO "pages" VALUES(17,'🎓','psg',23,'[]');
INSERT OR IGNORE INTO "pages" VALUES(18,'🏆','psg',23,'[]');
INSERT OR IGNORE INTO "pages" VALUES(19,'⏳','psg',24,'[]');
INSERT OR IGNORE INTO "pages" VALUES(20,'⚓','psg',38,'[21]');
INSERT OR IGNORE INTO "pages" VALUES(21,'👥','psg',40,'[]');
INSERT OR IGNORE INTO "pages" VALUES(22,'👤',NULL,NULL,'[7, 10, 2, 6, 20]');
INSERT OR IGNORE INTO "pages" VALUES(23,'🎭','wom',NULL,'[24, 25, 26, 27, 28]');
INSERT OR IGNORE INTO "pages" VALUES(24,'📋','wom',4,'[]');
INSERT OR IGNORE INTO "pages" VALUES(25,'👾','wom',8,'[]');
INSERT OR IGNORE INTO "pages" VALUES(26,'🎙️','wom',26,'[]');
INSERT OR IGNORE INTO "pages" VALUES(27,'🗺️','wom',41,'[]');
INSERT OR IGNORE INTO "pages" VALUES(28,'🎲','wom',58,'[29, 30]');
INSERT OR IGNORE INTO "pages" VALUES(29,'🪐','wom',58,'[]');
INSERT OR IGNORE INTO "pages" VALUES(30,'🏘️','wom',58,'[]');
-- page_i18n
INSERT OR IGNORE INTO "page_i18n" VALUES(1,1,'en','Mothership RPG','Quick reference for the Mothership RPG.');
INSERT OR IGNORE INTO "page_i18n" VALUES(2,1,'ru','Mothership RPG','Справочник по Mothership RPG.');
INSERT OR IGNORE INTO "page_i18n" VALUES(3,1,'ua','Mothership RPG','Довідник по Mothership RPG.');
INSERT OR IGNORE INTO "page_i18n" VALUES(4,3,'en','Combat','How fights work — turn order, actions, attacking, dealing damage, and using cover.');
INSERT OR IGNORE INTO "page_i18n" VALUES(5,3,'ru','Бой','Как работают бои — очерёдность ходов, действия, атаки, нанесение урона и укрытия.');
INSERT OR IGNORE INTO "page_i18n" VALUES(6,3,'ua','Бій','Як працюють бої — черговість ходів, дії, атаки, нанесення пошкодження та укриття.');
INSERT OR IGNORE INTO "page_i18n" VALUES(7,4,'en','Wounds & Death','What happens to your body — wound tables by damage type and the Death Table.');
INSERT OR IGNORE INTO "page_i18n" VALUES(8,4,'ru','Ранения и Смерть','Что происходит с вашим телом — таблицы ранений по типу урона и таблица смерти.');
INSERT OR IGNORE INTO "page_i18n" VALUES(9,4,'ua','Поранення та Смерть','Що відбувається з вашим тілом — таблиці поранень за типом пошкодження та таблиця смерті.');
INSERT OR IGNORE INTO "page_i18n" VALUES(10,5,'en','Range & Distance','Range, distance, and movement are tracked abstractly in Range Bands.');
INSERT OR IGNORE INTO "page_i18n" VALUES(11,5,'ru','Дистанция','Дальность, расстояние и движение отслеживаются абстрактно в Диапазонах Дистанций.');
INSERT OR IGNORE INTO "page_i18n" VALUES(12,5,'ua','Дистанція','Відстань і рух відстежуються абстрактно у Смугах Дистанцій.');
INSERT OR IGNORE INTO "page_i18n" VALUES(13,2,'en','Weapons & Damage','All weapons available to the crew — firearms, melee, and special. Includes ammo types and damage ratings.');
INSERT OR IGNORE INTO "page_i18n" VALUES(14,2,'ru','Оружие и Урон','Всё оружие экипажа — огнестрельное, рукопашное и специальное. Включает типы боеприпасов и показатели урона.');
INSERT OR IGNORE INTO "page_i18n" VALUES(15,2,'ua','Зброя та Шкода','Вся зброя екіпажу — вогнепальна, рукопашна та спеціальна. Включає типи боєприпасів та показники пошкодження.');
INSERT OR IGNORE INTO "page_i18n" VALUES(16,6,'en','Armour','Five armour types that protect the crew — from basic crew attire to Advanced Battle Dress.');
INSERT OR IGNORE INTO "page_i18n" VALUES(17,6,'ru','Броня','Пять типов брони для защиты экипажа — от стандартной одежды до продвинутого боевого снаряжения.');
INSERT OR IGNORE INTO "page_i18n" VALUES(18,6,'ua','Броня','П''ять типів броні для захисту екіпажу — від стандартного одягу до просунутого бойового спорядження.');
INSERT OR IGNORE INTO "page_i18n" VALUES(19,7,'en','Character Creation','The 9-step process to build your character, choose a class, and roll your starting loadout.');
INSERT OR IGNORE INTO "page_i18n" VALUES(20,7,'ru','Создание Персонажа','9 шагов для создания персонажа, выбора класса и броска начального снаряжения.');
INSERT OR IGNORE INTO "page_i18n" VALUES(21,7,'ua','Створення Персонажа','9 кроків для створення персонажа, вибору класу та кидка початкового спорядження.');
INSERT OR IGNORE INTO "page_i18n" VALUES(22,8,'en','Classes','Four playable classes — Marine, Android, Scientist, and Teamster — each with unique stat bonuses and a Trauma Response.');
INSERT OR IGNORE INTO "page_i18n" VALUES(23,8,'ru','Классы','Четыре играбельных класса — Морпех, Андроид, Учёный и Рабочий — каждый с уникальными бонусами и реакцией на травму.');
INSERT OR IGNORE INTO "page_i18n" VALUES(24,8,'ua','Класи','Чотири відіграваних класи — Морпіх, Андроїд, Вчений і Робітник — кожен з унікальними бонусами та реакцією на травму.');
INSERT OR IGNORE INTO "page_i18n" VALUES(25,9,'en','Loadouts & Tables','Starting equipment loadouts rolled randomly by class.');
INSERT OR IGNORE INTO "page_i18n" VALUES(26,9,'ru','Снаряжение и Таблицы','Начальное снаряжение, случайно разыгрываемое для каждого класса.');
INSERT OR IGNORE INTO "page_i18n" VALUES(27,9,'ua','Спорядження та Таблиці','Початкове спорядження, що випадково розігрується для кожного класу.');
INSERT OR IGNORE INTO "page_i18n" VALUES(28,10,'en','Equipment','All purchasable gear, tools, and supplies available to the crew.');
INSERT OR IGNORE INTO "page_i18n" VALUES(29,10,'ru','Снаряжение','Всё покупное снаряжение, инструменты и расходники для экипажа.');
INSERT OR IGNORE INTO "page_i18n" VALUES(30,10,'ua','Спорядження','Все купівельне спорядження, інструменти та витратники для екіпажу.');
INSERT OR IGNORE INTO "page_i18n" VALUES(31,11,'en','Core Rules','The core mechanics — stat checks, saves, and advantage & disadvantage.');
INSERT OR IGNORE INTO "page_i18n" VALUES(32,11,'ru','Основные Правила','Основные механики — проверки параметров, спасброски и преимущество с помехой.');
INSERT OR IGNORE INTO "page_i18n" VALUES(33,11,'ua','Основні Правила','Основні механіки — перевірки параметрів, порятунки та перевага і перешкода.');
INSERT OR IGNORE INTO "page_i18n" VALUES(34,12,'en','Stress & Panic','How stress builds, when to roll Panic Checks, and the conditions that result from breaking down.');
INSERT OR IGNORE INTO "page_i18n" VALUES(35,12,'ru','Стресс и Паника','Как накапливается стресс, когда делать броски на панику и какие состояния возникают при срыве.');
INSERT OR IGNORE INTO "page_i18n" VALUES(36,12,'ua','Стрес та Паніка','Як накопичується стрес, коли робити кидки на паніку та які стани виникають при зриві.');
INSERT OR IGNORE INTO "page_i18n" VALUES(37,13,'en','Skills','Three tiers of skills — Trained, Expert, and Master — with prerequisite chains and training rules.');
INSERT OR IGNORE INTO "page_i18n" VALUES(38,13,'ru','Навыки','Три уровня навыков — Начальный, Экспертный и Мастерский — с цепочками требований и правилами обучения.');
INSERT OR IGNORE INTO "page_i18n" VALUES(39,13,'ua','Навички','Три рівні навичок — Початковий, Експертний та Майстерний — з ланцюжками вимог та правилами навчання.');
INSERT OR IGNORE INTO "page_i18n" VALUES(40,16,'en','Trained Skills','The foundational skill tier — sixteen skills available to any character.');
INSERT OR IGNORE INTO "page_i18n" VALUES(41,16,'ru','Начальные Навыки','Базовый уровень навыков — шестнадцать навыков, доступных любому персонажу.');
INSERT OR IGNORE INTO "page_i18n" VALUES(42,16,'ua','Початкові Навички','Базовий рівень навичок — шістнадцять навичок, доступних будь-якому персонажу.');
INSERT OR IGNORE INTO "page_i18n" VALUES(43,17,'en','Expert Skills','Advanced skills requiring a Trained prerequisite — available after basic training.');
INSERT OR IGNORE INTO "page_i18n" VALUES(44,17,'ru','Экспертные Навыки','Продвинутые навыки, требующие базового навыка в качестве условия.');
INSERT OR IGNORE INTO "page_i18n" VALUES(45,17,'ua','Експертні Навички','Просунуті навички, що потребують базового навику як умови.');
INSERT OR IGNORE INTO "page_i18n" VALUES(46,18,'en','Master Skills','The highest tier of skills, each requiring an Expert prerequisite.');
INSERT OR IGNORE INTO "page_i18n" VALUES(47,18,'ru','Мастерские Навыки','Высший уровень навыков, каждый из которых требует экспертного навыка.');
INSERT OR IGNORE INTO "page_i18n" VALUES(48,18,'ua','Майстерні Навички','Найвищий рівень навичок, кожен з яких вимагає експертного навику.');
INSERT OR IGNORE INTO "page_i18n" VALUES(49,19,'en','Skill Training','How to train new skills between sessions and how to enlist in Military Training.');
INSERT OR IGNORE INTO "page_i18n" VALUES(50,19,'ru','Обучение Навыкам','Как осваивать новые навыки между сессиями и как записаться на военную подготовку.');
INSERT OR IGNORE INTO "page_i18n" VALUES(51,19,'ua','Навчання Навичкам','Як освоювати нові навички між сесіями та як записатися на військову підготовку.');
INSERT OR IGNORE INTO "page_i18n" VALUES(52,14,'en','Survival','Environmental hazards that threaten the crew — atmosphere, oxygen, radiation, temperature, and more.');
INSERT OR IGNORE INTO "page_i18n" VALUES(53,14,'ru','Выживание','Опасности окружающей среды — атмосфера, кислород, радиация, температура и другое.');
INSERT OR IGNORE INTO "page_i18n" VALUES(54,14,'ua','Виживання','Екологічні загрози для екіпажу — атмосфера, кисень, радіація, температура та інше.');
INSERT OR IGNORE INTO "page_i18n" VALUES(55,15,'en','Medical Care','Recovery and treatment — from short-term first aid to long-term therapy and specialized procedures.');
INSERT OR IGNORE INTO "page_i18n" VALUES(56,15,'ru','Медицинская Помощь','Восстановление и лечение — от неотложной помощи до долгосрочной терапии и специализированных процедур.');
INSERT OR IGNORE INTO "page_i18n" VALUES(57,15,'ua','Медична Допомога','Відновлення та лікування — від першої допомоги до довгострокової терапії та спеціалізованих процедур.');
INSERT OR IGNORE INTO "page_i18n" VALUES(58,20,'en','Ports & Shore Leave','What happens when the crew makes port — shore leave activities, spending credits, and port classes.');
INSERT OR IGNORE INTO "page_i18n" VALUES(59,20,'ru','Порты и Берег','Что происходит, когда экипаж прибывает в порт — береговой отпуск, трата кредитов и классы портов.');
INSERT OR IGNORE INTO "page_i18n" VALUES(60,20,'ua','Порти та Берег','Що відбувається, коли екіпаж прибуває до порту — берегова відпустка, витрата кредитів та класи портів.');
INSERT OR IGNORE INTO "page_i18n" VALUES(61,21,'en','Contractors','Hiring and managing contractor NPCs — their stats, costs, and the Contractors Table.');
INSERT OR IGNORE INTO "page_i18n" VALUES(62,21,'ru','Наемники','Найм и управление НПС-подрядчиками — параметры, стоимость и таблица подрядчиков.');
INSERT OR IGNORE INTO "page_i18n" VALUES(63,21,'ua','Найманці','Найм та управління НПС-підрядниками — параметри, вартість та таблиця підрядників.');
INSERT OR IGNORE INTO "page_i18n" VALUES(64,22,'en','Character','Everything about your character: who they are, what they carry, and how they survive. Covers character creation, weapons & damage, armour, and ports.');
INSERT OR IGNORE INTO "page_i18n" VALUES(65,22,'ru','Персонаж','Всё о вашем персонаже: кто он, что несёт и как выживает. Включает создание персонажа, оружие и урон, броню и порты.');
INSERT OR IGNORE INTO "page_i18n" VALUES(66,22,'ua','Персонаж','Все про вашого персонажа: хто він, що несе і як виживає. Включає створення персонажа, зброю та пошкодження, броню і порти.');
INSERT OR IGNORE INTO "page_i18n" VALUES(67,23,'en','Warden''s Guide',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(68,23,'ru','Руководство Судьи',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(69,23,'ua','Посібник Судді',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(70,24,'en','Session Prep',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(71,24,'ru','Подготовка Сессии',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(72,24,'ua','Підготовка Сесії',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(73,25,'en','The Horror',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(74,25,'ru','Ужас',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(75,25,'ua','Жах',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(76,26,'en','Running the Game',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(77,26,'ru','Ведение Игры',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(78,26,'ua','Ведення Гри',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(79,27,'en','Campaign Building',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(80,27,'ru','Построение Кампании',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(81,27,'ua','Побудова Кампанії',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(82,28,'en','Random Generators',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(83,28,'ru','Случайные Генераторы',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(84,28,'ua','Випадкові Генератори',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(85,29,'en','Planet',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(86,29,'ru','Планета',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(87,29,'ua','Планета',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(88,30,'en','Settlement',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(89,30,'ru','Поселение',NULL);
INSERT OR IGNORE INTO "page_i18n" VALUES(90,30,'ua','Поселення',NULL);
-- contents
INSERT OR IGNORE INTO "contents" VALUES(1,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "50cr", "type": "cost"}, {"label_key": "range", "value": "N/A", "type": "stat"}, {"label_key": "damage", "value": "\u2014", "type": "roll"}, {"label_key": "shots", "value": "N/A", "type": "stat"}, {"label_key": "wound_type", "value": "N/A", "type": "stat"}]',NULL,'psg',NULL,1);
INSERT OR IGNORE INTO "contents" VALUES(2,'⚔️',NULL,NULL,'[{"label_key": "cost", "value": "150cr", "type": "cost"}, {"label_key": "range", "value": "Adjacent", "type": "stat"}, {"label_key": "damage", "value": "2d10 DMG", "type": "roll"}, {"label_key": "shots", "value": "N/A", "type": "stat"}, {"label_key": "wound_type", "value": "Gore [+]", "type": "stat"}]',NULL,'psg',NULL,2);
INSERT OR IGNORE INTO "contents" VALUES(3,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "1,400cr", "type": "cost"}, {"label_key": "range", "value": "Close", "type": "stat"}, {"label_key": "damage", "value": "4d10 DMG", "type": "roll"}, {"label_key": "shots", "value": "4", "type": "stat"}, {"label_key": "wound_type", "value": "Gunshot", "type": "stat"}]',NULL,'psg',NULL,3);
INSERT OR IGNORE INTO "contents" VALUES(4,'🔧',NULL,NULL,'[{"label_key": "cost", "value": "25cr", "type": "cost"}, {"label_key": "range", "value": "Adjacent", "type": "stat"}, {"label_key": "damage", "value": "1d5 DMG", "type": "roll"}, {"label_key": "shots", "value": "N/A", "type": "stat"}, {"label_key": "wound_type", "value": "Blunt Force [+]", "type": "stat"}]',NULL,'psg',NULL,4);
INSERT OR IGNORE INTO "contents" VALUES(5,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "4kcr", "type": "cost"}, {"label_key": "range", "value": "Close", "type": "stat"}, {"label_key": "damage", "value": "2d10 DMG", "type": "roll"}, {"label_key": "shots", "value": "4", "type": "stat"}, {"label_key": "wound_type", "value": "Fire/Explosives [+]", "type": "stat"}]',NULL,'psg',NULL,5);
INSERT OR IGNORE INTO "contents" VALUES(6,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "25cr", "type": "cost"}, {"label_key": "range", "value": "Long", "type": "stat"}, {"label_key": "damage", "value": "1d5 DMG", "type": "roll"}, {"label_key": "shots", "value": "2", "type": "stat"}, {"label_key": "wound_type", "value": "Fire/Explosives [-]", "type": "stat"}]',NULL,'psg',NULL,6);
INSERT OR IGNORE INTO "contents" VALUES(7,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "500cr", "type": "cost"}, {"label_key": "range", "value": "Close", "type": "stat"}, {"label_key": "damage", "value": "1 DMG", "type": "roll"}, {"label_key": "shots", "value": "3", "type": "stat"}, {"label_key": "wound_type", "value": "Blunt Force", "type": "stat"}]',NULL,'psg',NULL,7);
INSERT OR IGNORE INTO "contents" VALUES(8,'💣',NULL,NULL,'[{"label_key": "cost", "value": "400cr ea.", "type": "cost"}, {"label_key": "range", "value": "Close", "type": "stat"}, {"label_key": "damage", "value": "3d10 DMG", "type": "roll"}, {"label_key": "shots", "value": "1", "type": "stat"}, {"label_key": "wound_type", "value": "Fire/Explosives", "type": "stat"}]',NULL,'psg',NULL,8);
INSERT OR IGNORE INTO "contents" VALUES(9,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "4.5kcr", "type": "cost"}, {"label_key": "range", "value": "Long", "type": "stat"}, {"label_key": "damage", "value": "4d10 DMG", "type": "roll"}, {"label_key": "shots", "value": "5", "type": "stat"}, {"label_key": "wound_type", "value": "Gunshot [+]", "type": "stat"}]',NULL,'psg',NULL,9);
INSERT OR IGNORE INTO "contents" VALUES(10,'🔧',NULL,NULL,'[{"label_key": "cost", "value": "250cr", "type": "cost"}, {"label_key": "range", "value": "Adjacent", "type": "stat"}, {"label_key": "damage", "value": "1d10 DMG", "type": "roll"}, {"label_key": "shots", "value": "N/A", "type": "stat"}, {"label_key": "wound_type", "value": "Bleeding", "type": "stat"}]',NULL,'psg',NULL,10);
INSERT OR IGNORE INTO "contents" VALUES(11,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "1,200cr", "type": "cost"}, {"label_key": "range", "value": "Long", "type": "stat"}, {"label_key": "damage", "value": "1d100 DMG", "type": "roll"}, {"label_key": "shots", "value": "6", "type": "stat"}, {"label_key": "wound_type", "value": "Bleeding [+] or Gore [+]", "type": "stat"}]',NULL,'psg',NULL,11);
INSERT OR IGNORE INTO "contents" VALUES(12,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "150cr", "type": "cost"}, {"label_key": "range", "value": "Close", "type": "stat"}, {"label_key": "damage", "value": "1d5 DMG", "type": "roll"}, {"label_key": "shots", "value": "32", "type": "stat"}, {"label_key": "wound_type", "value": "Bleeding", "type": "stat"}]',NULL,'psg',NULL,12);
INSERT OR IGNORE INTO "contents" VALUES(13,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "2.4kcr", "type": "cost"}, {"label_key": "range", "value": "Long", "type": "stat"}, {"label_key": "damage", "value": "3d10 DMG", "type": "roll"}, {"label_key": "shots", "value": "5", "type": "stat"}, {"label_key": "wound_type", "value": "Gunshot", "type": "stat"}]',NULL,'psg',NULL,13);
INSERT OR IGNORE INTO "contents" VALUES(14,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "750cr", "type": "cost"}, {"label_key": "range", "value": "Close", "type": "stat"}, {"label_key": "damage", "value": "1d10+1 DMG", "type": "roll"}, {"label_key": "shots", "value": "6", "type": "stat"}, {"label_key": "wound_type", "value": "Gunshot", "type": "stat"}]',NULL,'psg',NULL,14);
INSERT OR IGNORE INTO "contents" VALUES(15,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "350cr", "type": "cost"}, {"label_key": "range", "value": "Close", "type": "stat"}, {"label_key": "damage", "value": "1d10 DMG + 2d10 when removed", "type": "roll"}, {"label_key": "shots", "value": "1", "type": "stat"}, {"label_key": "wound_type", "value": "Bleeding [+]", "type": "stat"}]',NULL,'psg',NULL,15);
INSERT OR IGNORE INTO "contents" VALUES(16,'⚔️',NULL,NULL,'[{"label_key": "cost", "value": "50cr", "type": "cost"}, {"label_key": "range", "value": "Adjacent", "type": "stat"}, {"label_key": "damage", "value": "1d5 DMG", "type": "roll"}, {"label_key": "shots", "value": "N/A", "type": "stat"}, {"label_key": "wound_type", "value": "Bleeding [+]", "type": "stat"}]',NULL,'psg',NULL,16);
INSERT OR IGNORE INTO "contents" VALUES(17,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "5kcr", "type": "cost"}, {"label_key": "range", "value": "Extreme", "type": "stat"}, {"label_key": "damage", "value": "4d10 DMG (AA)", "type": "roll"}, {"label_key": "shots", "value": "3", "type": "stat"}, {"label_key": "wound_type", "value": "Gunshot [+]", "type": "stat"}]',NULL,'psg',NULL,17);
INSERT OR IGNORE INTO "contents" VALUES(18,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "1kcr", "type": "cost"}, {"label_key": "range", "value": "Long", "type": "stat"}, {"label_key": "damage", "value": "2d10 DMG", "type": "roll"}, {"label_key": "shots", "value": "5", "type": "stat"}, {"label_key": "wound_type", "value": "Gunshot", "type": "stat"}]',NULL,'psg',NULL,18);
INSERT OR IGNORE INTO "contents" VALUES(19,'⚔️',NULL,NULL,'[{"label_key": "cost", "value": "150cr", "type": "cost"}, {"label_key": "range", "value": "Adjacent", "type": "stat"}, {"label_key": "damage", "value": "1d5 DMG", "type": "roll"}, {"label_key": "shots", "value": "N/A", "type": "stat"}, {"label_key": "wound_type", "value": "Blunt Force", "type": "stat"}]',NULL,'psg',NULL,19);
INSERT OR IGNORE INTO "contents" VALUES(20,'🔫',NULL,NULL,'[{"label_key": "cost", "value": "250cr", "type": "cost"}, {"label_key": "range", "value": "Close", "type": "stat"}, {"label_key": "damage", "value": "1d5 DMG", "type": "roll"}, {"label_key": "shots", "value": "6", "type": "stat"}, {"label_key": "wound_type", "value": "Blunt Force", "type": "stat"}]',NULL,'psg',NULL,20);
INSERT OR IGNORE INTO "contents" VALUES(21,'👊',NULL,NULL,'[{"label_key": "cost", "value": "Free", "type": "cost"}, {"label_key": "range", "value": "Adjacent", "type": "stat"}, {"label_key": "damage", "value": "Str/10 DMG", "type": "roll"}, {"label_key": "shots", "value": "N/A", "type": "stat"}, {"label_key": "wound_type", "value": "Blunt Force", "type": "stat"}]',NULL,'psg',NULL,21);
INSERT OR IGNORE INTO "contents" VALUES(22,'⚔️',NULL,NULL,'[{"label_key": "cost", "value": "1kcr", "type": "cost"}, {"label_key": "range", "value": "Adjacent", "type": "stat"}, {"label_key": "damage", "value": "3d10 DMG (AA)", "type": "roll"}, {"label_key": "shots", "value": "N/A", "type": "stat"}, {"label_key": "wound_type", "value": "Bleeding + Gore", "type": "stat"}]',NULL,'psg',NULL,22);
INSERT OR IGNORE INTO "contents" VALUES(23,'⚔️',NULL,NULL,NULL,NULL,'psg',26,0);
INSERT OR IGNORE INTO "contents" VALUES(24,'😱',NULL,NULL,NULL,NULL,'psg',26,1);
INSERT OR IGNORE INTO "contents" VALUES(25,'❓',NULL,NULL,NULL,NULL,'psg',27,2);
INSERT OR IGNORE INTO "contents" VALUES(26,'🎯',NULL,NULL,NULL,NULL,'psg',28,3);
INSERT OR IGNORE INTO "contents" VALUES(27,'💥',NULL,NULL,NULL,NULL,'psg',28,4);
INSERT OR IGNORE INTO "contents" VALUES(28,'🛡️',NULL,NULL,NULL,NULL,'psg',28,5);
INSERT OR IGNORE INTO "contents" VALUES(29,'🪨',NULL,NULL,'[{"label_key": "cover_insignificant", "value": "AP 5", "type": "stat"}, {"label_key": "cover_light", "value": "AP 10", "type": "stat"}, {"label_key": "cover_heavy", "value": "DR 5 / AP 20", "type": "stat"}]',NULL,'psg',28,6);
INSERT OR IGNORE INTO "contents" VALUES(30,'🩹',NULL,NULL,NULL,NULL,'psg',29,7);
INSERT OR IGNORE INTO "contents" VALUES(31,'🎲',NULL,NULL,'[{"label_key": "wound_type", "value": "Blunt Force", "type": "stat"}]','{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Flesh Wound. Knocked down."}, {"min": 1, "max": 1, "text": "Winded. [-] until you catch your breath."}, {"min": 2, "max": 2, "text": "Minor Injury. Sprained Ankle. [-] on Speed Checks."}, {"min": 3, "max": 3, "text": "Concussion. [-] on mental tasks."}, {"min": 4, "max": 4, "text": "Leg or foot broken. [-] on Speed Checks."}, {"min": 5, "max": 5, "text": "Major Injury. Arm or hand broken. [-] on manual tasks."}, {"min": 6, "max": 6, "text": "Snapped collarbone. [-] on Strength Checks."}, {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Back broken. [-] on all rolls."}, {"min": 8, "max": 8, "text": "Skull fracture. [-] on all rolls."}, {"min": 9, "max": 9, "text": "Fatal Injury. Spine or neck broken. Death Save."}]}','psg',29,8);
INSERT OR IGNORE INTO "contents" VALUES(32,'🎲',NULL,NULL,'[{"label_key": "wound_type", "value": "Bleeding", "type": "stat"}]','{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Flesh Wound. Drop held item."}, {"min": 1, "max": 1, "text": "Lots of blood. Those Close gain 1 Stress."}, {"min": 2, "max": 2, "text": "Minor Injury. Blood in eyes. [-] until wiped clean."}, {"min": 3, "max": 3, "text": "Laceration. Bleeding +1."}, {"min": 4, "max": 4, "text": "Major cut. Bleeding +2."}, {"min": 5, "max": 5, "text": "Major Injury. Fingers/toes severed. Bleeding +3."}, {"min": 6, "max": 6, "text": "Hand/foot severed. Bleeding +4."}, {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Limb severed. Bleeding +5."}, {"min": 8, "max": 8, "text": "Major artery cut. Bleeding +6."}, {"min": 9, "max": 9, "text": "Fatal Injury. Throat slit or heart pierced. Death Save."}]}','psg',29,9);
INSERT OR IGNORE INTO "contents" VALUES(33,'🎲',NULL,NULL,'[{"label_key": "wound_type", "value": "Gunshot", "type": "stat"}]','{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Flesh Wound. Grazed. Knocked down."}, {"min": 1, "max": 1, "text": "Bleeding +1."}, {"min": 2, "max": 2, "text": "Minor Injury. Broken rib."}, {"min": 3, "max": 3, "text": "Fractured extremity."}, {"min": 4, "max": 4, "text": "Internal bleeding. Bleeding +2."}, {"min": 5, "max": 5, "text": "Major Injury. Lodged bullet. Surgery required."}, {"min": 6, "max": 6, "text": "Gunshot wound to the neck."}, {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Major blood loss. Bleeding +4."}, {"min": 8, "max": 8, "text": "Sucking chest wound. Bleeding +5."}, {"min": 9, "max": 9, "text": "Fatal Injury. Headshot. Death Save."}]}','psg',29,10);
INSERT OR IGNORE INTO "contents" VALUES(34,'🎲',NULL,NULL,'[{"label_key": "wound_type", "value": "Fire & Explosives", "type": "stat"}]','{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Flesh Wound. Hair burnt. Gain 1d5 Stress."}, {"min": 1, "max": 1, "text": "Awesome scar. +1 Minimum Stress."}, {"min": 2, "max": 2, "text": "Minor Injury. Singed. [-] on next action."}, {"min": 3, "max": 3, "text": "Shrapnel / large burn."}, {"min": 4, "max": 4, "text": "Extensive burns."}, {"min": 5, "max": 5, "text": "Major Injury. Major Burn. -2d10 Body Save."}, {"min": 6, "max": 6, "text": "Skin grafts required. -2d10 Body Save."}, {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Limb on fire. 2d10 Damage per round."}, {"min": 8, "max": 8, "text": "Body on fire. 3d10 Damage per round."}, {"min": 9, "max": 9, "text": "Fatal Injury. Engulfed in fiery explosion. Death Save."}]}','psg',29,11);
INSERT OR IGNORE INTO "contents" VALUES(35,'🎲',NULL,NULL,'[{"label_key": "wound_type", "value": "Gore & Massive", "type": "stat"}]','{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Flesh Wound. Vomit. [-] on next action."}, {"min": 1, "max": 1, "text": "Awesome scar. +1 Minimum Stress."}, {"min": 2, "max": 2, "text": "Minor Injury. Digit mangled."}, {"min": 3, "max": 3, "text": "Eyes gouged out."}, {"min": 4, "max": 4, "text": "Ripped off flesh. -1d10 Strength."}, {"min": 5, "max": 5, "text": "Major Injury. Paralyzed waist down."}, {"min": 6, "max": 6, "text": "Limb severed. Bleeding +5."}, {"min": 7, "max": 7, "text": "Lethal Injury (Death Save in 1d10 rounds). Impaled. Bleeding +6."}, {"min": 8, "max": 8, "text": "Guts spooled on floor. Bleeding +7."}, {"min": 9, "max": 9, "text": "Fatal Injury. Head explodes. No Death Save. You have died."}]}','psg',29,12);
INSERT OR IGNORE INTO "contents" VALUES(36,'💀',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Unconscious. Wake up in 2d10 minutes. Reduce Maximum Health by 1d5."}, {"min": 1, "max": 2, "text": "Unconscious and dying. You die in 1d5 rounds without intervention."}, {"min": 3, "max": 4, "text": "Comatose. Only extraordinary measures can return you to the waking world."}, {"min": 5, "max": 9, "text": "You have died. Roll up a new character."}]}','psg',29,13);
INSERT OR IGNORE INTO "contents" VALUES(37,'👁️',NULL,NULL,NULL,NULL,'psg',30,14);
INSERT OR IGNORE INTO "contents" VALUES(38,'🏃',NULL,NULL,NULL,NULL,'psg',31,15);
INSERT OR IGNORE INTO "contents" VALUES(39,'🔭',NULL,NULL,NULL,NULL,'psg',31,16);
INSERT OR IGNORE INTO "contents" VALUES(40,'🌌',NULL,NULL,NULL,NULL,'psg',31,17);
INSERT OR IGNORE INTO "contents" VALUES(41,'👕',NULL,NULL,'[{"label_key": "cost", "value": "100cr", "type": "cost"}, {"label_key": "ap", "value": "1", "type": "stat"}, {"label_key": "o2", "value": "\u2014", "type": "stat"}, {"label_key": "speed", "value": "Normal", "type": "stat"}]',NULL,'psg',NULL,41);
INSERT OR IGNORE INTO "contents" VALUES(42,'🔵',NULL,NULL,'[{"label_key": "cost", "value": "10kcr", "type": "cost"}, {"label_key": "ap", "value": "3", "type": "stat"}, {"label_key": "o2", "value": "12 hrs", "type": "stat"}, {"label_key": "speed", "value": "[-]", "type": "stat"}]',NULL,'psg',NULL,42);
INSERT OR IGNORE INTO "contents" VALUES(43,'☢️',NULL,NULL,'[{"label_key": "cost", "value": "4kcr", "type": "cost"}, {"label_key": "ap", "value": "5", "type": "stat"}, {"label_key": "o2", "value": "1 hr", "type": "stat"}, {"label_key": "speed", "value": "Normal", "type": "stat"}]',NULL,'psg',NULL,43);
INSERT OR IGNORE INTO "contents" VALUES(44,'🪖',NULL,NULL,'[{"label_key": "cost", "value": "2kcr", "type": "cost"}, {"label_key": "ap", "value": "7", "type": "stat"}, {"label_key": "o2", "value": "\u2014", "type": "stat"}, {"label_key": "speed", "value": "Normal", "type": "stat"}]',NULL,'psg',NULL,44);
INSERT OR IGNORE INTO "contents" VALUES(45,'🤖',NULL,NULL,'[{"label_key": "cost", "value": "12kcr", "type": "cost"}, {"label_key": "ap", "value": "10", "type": "stat"}, {"label_key": "o2", "value": "1 hr", "type": "stat"}, {"label_key": "speed", "value": "[-]", "type": "stat"}]',NULL,'psg',NULL,45);
INSERT OR IGNORE INTO "contents" VALUES(46,'📝',NULL,NULL,NULL,NULL,'psg',4,46);
INSERT OR IGNORE INTO "contents" VALUES(47,'🪖',NULL,NULL,'[{"label_key": "combat", "value": "+10 Combat", "type": "stat"}, {"label_key": "body_save", "value": "+10 Body Save", "type": "stat"}, {"label_key": "fear_save", "value": "+20 Fear Save", "type": "stat"}, {"label_key": "wounds", "value": "+1 Max Wounds", "type": "stat"}]',NULL,'psg',5,47);
INSERT OR IGNORE INTO "contents" VALUES(48,'🤖',NULL,NULL,'[{"label_key": "intellect", "value": "+20 Intellect", "type": "stat"}, {"label_key": "any_stat", "value": "-10 to 1 Stat", "type": "stat"}, {"label_key": "fear_save", "value": "+60 Fear Save", "type": "stat"}, {"label_key": "wounds", "value": "+1 Max Wounds", "type": "stat"}]',NULL,'psg',5,48);
INSERT OR IGNORE INTO "contents" VALUES(49,'🔬',NULL,NULL,'[{"label_key": "intellect", "value": "+10 Intellect", "type": "stat"}, {"label_key": "any_stat", "value": "+5 to 1 Stat", "type": "stat"}, {"label_key": "sanity_save", "value": "+30 Sanity Save", "type": "stat"}]',NULL,'psg',5,49);
INSERT OR IGNORE INTO "contents" VALUES(50,'🔧',NULL,NULL,'[{"label_key": "all_stats", "value": "+5 to all Stats", "type": "stat"}, {"label_key": "all_saves", "value": "+10 to all Saves", "type": "stat"}]',NULL,'psg',5,50);
INSERT OR IGNORE INTO "contents" VALUES(51,'🪖',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Tank Top and Camo Pants (AP 1), Combat Knife (as Scalpel DMG [+]), Stimpak (x5)"}, {"min": 1, "max": 1, "text": "Advanced Battle Dress (AP 10), Flamethrower (4 shots), Boarding Axe"}, {"min": 2, "max": 2, "text": "Standard Battle Dress (AP 7), Combat Shotgun (4 rounds), Rucksack, Camping Gear"}, {"min": 3, "max": 3, "text": "Standard Battle Dress (AP 7), Pulse Rifle (3 mags), Infrared Goggles"}, {"min": 4, "max": 4, "text": "Standard Battle Dress (AP 7), Smart Rifle (3 mags), Binoculars, Personal Locator"}, {"min": 5, "max": 5, "text": "Standard Battle Dress (AP 7), SMG (3 mags), MRE (x7)"}, {"min": 6, "max": 6, "text": "Fatigues (AP 2), Combat Shotgun (2 rounds), Dog (pet), Leash, Tennis Ball"}, {"min": 7, "max": 7, "text": "Fatigues (AP 2), Revolver (12 rounds), Frag Grenade"}, {"min": 8, "max": 8, "text": "Dress Uniform (AP 1), Revolver (1 round), Challenge Coin"}, {"min": 9, "max": 9, "text": "Advanced Battle Dress (AP 10), General-Purpose Machine Gun (1 can of ammo), HUD"}]}','psg',7,51);
INSERT OR IGNORE INTO "contents" VALUES(52,'🤖',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Vaccsuit (AP 3), Smart Rifle (2 mags), Infrared Goggles, Mylar Blanket"}, {"min": 1, "max": 1, "text": "Vaccsuit (AP 3), Revolver (12 rounds), Long-range Comms, Satchel"}, {"min": 2, "max": 2, "text": "Hazard Suit (AP 5), Revolver (6 rounds), Defibrillator, First Aid Kit, Flashlight"}, {"min": 3, "max": 3, "text": "Hazard Suit (AP 5), Foam Gun (2 charges), Sample Collection Kit, Screwdriver (as Assorted Tools)"}, {"min": 4, "max": 4, "text": "Standard Battle Dress (AP 7), Tranq Pistol (3 shots), Paracord (100m)"}, {"min": 5, "max": 5, "text": "Standard Crew Attire (AP 1), Stun Baton, Small Pet (organic)"}, {"min": 6, "max": 6, "text": "Standard Crew Attire (AP 1), Scalpel, Bioscanner"}, {"min": 7, "max": 7, "text": "Standard Crew Attire (AP 1), Frag Grenade, Pen Knife"}, {"min": 8, "max": 8, "text": "Manufacturer Supplied Attire (AP 1), Jump-9 Ticket (destination blank)"}, {"min": 9, "max": 9, "text": "Corporate Attire (AP 1), VIP Corporate Key Card"}]}','psg',7,52);
INSERT OR IGNORE INTO "contents" VALUES(53,'🔬',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Hazard Suit (AP 5), Tranq Pistol (3 shots), Bioscanner, Sample Collection Kit"}, {"min": 1, "max": 1, "text": "Hazard Suit (AP 5), Flamethrower (1 charge), Stimpak, Electronic Tool Set"}, {"min": 2, "max": 2, "text": "Vaccsuit (AP 3), Rigging Gun, Sample Collection Kit, Flashlight, Lab Rat (pet)"}, {"min": 3, "max": 3, "text": "Vaccsuit (AP 3), Foam Gun (2 charges), Foldable Stretcher, First Aid Kit, Radiation Pills (x5)"}, {"min": 4, "max": 4, "text": "Lab Coat (AP 1), Screwdriver (as Assorted Tools), Medscanner, Vaccine (1 dose)"}, {"min": 5, "max": 5, "text": "Lab Coat (AP 1), Cybernetic Diagnostic Scanner, Portable Computer Terminal"}, {"min": 6, "max": 6, "text": "Scrubs (AP 1), Scalpel, Automed (x5), Oxygen Tank with Filter Mask"}, {"min": 7, "max": 7, "text": "Scrubs (AP 1), Vial of Acid, Mylar Blanket, First Aid Kit"}, {"min": 8, "max": 8, "text": "Standard Crew Attire (AP 1), Utility Knife (as Scalpel), Cybernetic Diagnostic Scanner, Duct Tape"}, {"min": 9, "max": 9, "text": "Civilian Clothes (AP 1), Briefcase, Prescription Pad, Fountain Pen (Poison Injector)"}]}','psg',7,53);
INSERT OR IGNORE INTO "contents" VALUES(54,'🔧',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Vaccsuit (AP 3), Laser Cutter (1 extra battery), Patch Kit (x3), Toolbelt with Assorted Tools"}, {"min": 1, "max": 1, "text": "Vaccsuit (AP 3), Revolver (6 rounds), Crowbar, Flashlight"}, {"min": 2, "max": 2, "text": "Vaccsuit (AP 3), Rigging Gun (1 shot), Shovel, Salvage Drone"}, {"min": 3, "max": 3, "text": "Hazard Suit (AP 5), Vibechete, Spanner, Camping Gear, Water Filtration Device"}, {"min": 4, "max": 4, "text": "Heavy Duty Work Clothes (AP 2), Explosives & Detonator, Cigarettes"}, {"min": 5, "max": 5, "text": "Heavy Duty Work Clothes (AP 2), Drill (as Assorted Tools), Paracord (100m), Salvage Drone"}, {"min": 6, "max": 6, "text": "Standard Crew Attire (AP 1), Combat Shotgun (4 rounds), Extension Cord (20m), Cat (pet)"}, {"min": 7, "max": 7, "text": "Standard Crew Attire (AP 1), Nail Gun (32 rounds), Head Lamp, Toolbelt with Assorted Tools, Lunch Box"}, {"min": 8, "max": 8, "text": "Standard Crew Attire (AP 1), Flare Gun (2 rounds), Water Filtration Device, Personal Locator, Subsurface Scanner"}, {"min": 9, "max": 9, "text": "Lounge Wear (AP 1), Crowbar, Stimpak, Six Pack of Beer"}]}','psg',7,54);
INSERT OR IGNORE INTO "contents" VALUES(55,'💎',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "Manual: PANIC: Harbinger of Catastrophe"}, {"min": 1, "max": 1, "text": "Antique Company Scrip (Asteroid Mine)"}, {"min": 2, "max": 2, "text": "Manual: SURVIVAL: Eat Soup With a Knife"}, {"min": 3, "max": 3, "text": "Desiccated Husk Doll"}, {"min": 4, "max": 4, "text": "Pressed Alien Flower (common)"}, {"min": 5, "max": 5, "text": "Necklace of Shell Casings"}, {"min": 6, "max": 6, "text": "Corroded Android Logic Core"}, {"min": 7, "max": 7, "text": "Pamphlet: Signs of Parasitical Infection"}, {"min": 8, "max": 8, "text": "Manual: Treat Your Rifle Like A Lady"}, {"min": 9, "max": 9, "text": "Bone Knife"}, {"min": 10, "max": 10, "text": "Calendar: Alien Pin-Up Art"}, {"min": 11, "max": 11, "text": "Rejected Application (Colony Ship)"}, {"min": 12, "max": 12, "text": "Holographic Serpentine Dancer"}, {"min": 13, "max": 13, "text": "Snake Whiskey"}, {"min": 14, "max": 14, "text": "Medical Container, Purple Powder"}, {"min": 15, "max": 15, "text": "Pills: Male Enhancement, Shoddy"}, {"min": 16, "max": 16, "text": "Casino Playing Cards"}, {"min": 17, "max": 17, "text": "Lagomorph Foot"}, {"min": 18, "max": 18, "text": "Moonstone Ring"}, {"min": 19, "max": 19, "text": "Manual: Mining Safety and You"}, {"min": 20, "max": 20, "text": "Pamphlet: Against Human Simulacra"}, {"min": 21, "max": 21, "text": "Animal Skull, 3 Eyes, Curled Horns"}, {"min": 22, "max": 22, "text": "Bartender''s Certification (Expired)"}, {"min": 23, "max": 23, "text": "Bunraku Puppet"}, {"min": 24, "max": 24, "text": "Prospecting Mug, Dented"}, {"min": 25, "max": 25, "text": "Eerie Mask"}, {"min": 26, "max": 26, "text": "Ultrablack Marble"}, {"min": 27, "max": 27, "text": "Ivory Dice"}, {"min": 28, "max": 28, "text": "Tarot Cards, Worn, Pyrite Gilded Edges"}, {"min": 29, "max": 29, "text": "Bag of Assorted Teeth"}, {"min": 30, "max": 30, "text": "Ashes (A Relative)"}, {"min": 31, "max": 31, "text": "DNR Beacon Necklace"}, {"min": 32, "max": 32, "text": "Cigarettes (Grinning Skull)"}, {"min": 33, "max": 33, "text": "Pills: Areca Nut"}, {"min": 34, "max": 34, "text": "Pendant: Shell Fragments Suspended in Plastic"}, {"min": 35, "max": 35, "text": "Pamphlet: Zen and the Art of Cargo Arrangement"}, {"min": 36, "max": 36, "text": "Pair of Shot Glasses (Spent Shotgun Shells)"}, {"min": 37, "max": 37, "text": "Key (Childhood Home)"}, {"min": 38, "max": 38, "text": "Dog Tags (Heirloom)"}, {"min": 39, "max": 39, "text": "Token: \"Is Your Morale Improving?\""}, {"min": 40, "max": 40, "text": "Pamphlet: The Relic of Flesh"}, {"min": 41, "max": 41, "text": "Pamphlet: The Indifferent Stars"}, {"min": 42, "max": 42, "text": "Calendar: Military Battles"}, {"min": 43, "max": 43, "text": "Manual: Rich Captain, Poor Captain"}, {"min": 44, "max": 44, "text": "Campaign Poster (Home Planet)"}, {"min": 45, "max": 45, "text": "Preserved Insectile Aberration"}, {"min": 46, "max": 46, "text": "Titanium Toothpick"}, {"min": 47, "max": 47, "text": "Gloves, Leather (Xenomorph Hide)"}, {"min": 48, "max": 48, "text": "Smut (Seditious): The Captain, Ordered"}, {"min": 49, "max": 49, "text": "Towel, Slightly Frayed"}, {"min": 50, "max": 50, "text": "Brass Knuckles"}, {"min": 51, "max": 51, "text": "Fuzzy Handcuffs"}, {"min": 52, "max": 52, "text": "Journal of Grudges"}, {"min": 53, "max": 53, "text": "Stylized Cigarette Case"}, {"min": 54, "max": 54, "text": "Ball of Assorted Gauge Wire"}, {"min": 55, "max": 55, "text": "Spanner"}, {"min": 56, "max": 56, "text": "Switchblade, Ornamental"}, {"min": 57, "max": 57, "text": "Powdered Xenomorph Horn"}, {"min": 58, "max": 58, "text": "Bonsai Tree, Potted"}, {"min": 59, "max": 59, "text": "Golf Club (Putter)"}, {"min": 60, "max": 60, "text": "Trilobite Fossil"}, {"min": 61, "max": 61, "text": "Pamphlet: A Lover In Every Port"}, {"min": 62, "max": 62, "text": "Patched Overalls, Personalized"}, {"min": 63, "max": 63, "text": "Fleshy Thing Sealed in a Murky Jar"}, {"min": 64, "max": 64, "text": "Spiked Bracelet"}, {"min": 65, "max": 65, "text": "Harmonica"}, {"min": 66, "max": 66, "text": "Pictorial Pornography, Dog-eared, Well-thumbed"}, {"min": 67, "max": 67, "text": "Coffee Cup, Chipped, reads: HAPPINESS IS MANDATORY"}, {"min": 68, "max": 68, "text": "Manual: Moonshining With Gun Oil & Fuel"}, {"min": 69, "max": 69, "text": "Miniature Chess Set, Bone, Pieces Missing"}, {"min": 70, "max": 70, "text": "Gyroscope, Bent, Tin"}, {"min": 71, "max": 71, "text": "Faded Green Poker Chip"}, {"min": 72, "max": 72, "text": "Ukulele"}, {"min": 73, "max": 73, "text": "Spray Paint"}, {"min": 74, "max": 74, "text": "Wanted Poster, Weathered"}, {"min": 75, "max": 75, "text": "Locket, Hair Braid"}, {"min": 76, "max": 76, "text": "Sculpture of a Rat (Gold)"}, {"min": 77, "max": 77, "text": "Blanket, Fire Retardant"}, {"min": 78, "max": 78, "text": "Hooded Parka, Fleece-Lined"}, {"min": 79, "max": 79, "text": "BB Gun"}, {"min": 80, "max": 80, "text": "Flint Hatchet"}, {"min": 81, "max": 81, "text": "Pendant: Two Astronauts form a Skull"}, {"min": 82, "max": 82, "text": "Rubik''s Cube"}, {"min": 83, "max": 83, "text": "Stress Ball, reads: Zero Stress in Zero G"}, {"min": 84, "max": 84, "text": "Sputnik Pin"}, {"min": 85, "max": 85, "text": "Ushanka"}, {"min": 86, "max": 86, "text": "Trucker Cap, Mesh, Grey Alien Logo"}, {"min": 87, "max": 87, "text": "Menthol Balm"}, {"min": 88, "max": 88, "text": "Pith Helmet"}, {"min": 89, "max": 89, "text": "10m x 10m Tarp"}, {"min": 90, "max": 90, "text": "I Ching, Missing Sticks"}, {"min": 91, "max": 91, "text": "Kukri"}, {"min": 92, "max": 92, "text": "Trench Shovel"}, {"min": 93, "max": 93, "text": "Shiv, Sharpened Butter Knife"}, {"min": 94, "max": 94, "text": "Taxidermied Cat"}, {"min": 95, "max": 95, "text": "Pamphlet: Interpreting Sheep Dreams"}, {"min": 96, "max": 96, "text": "Faded Photograph, A Windswept Heath"}, {"min": 97, "max": 97, "text": "Opera Glasses"}, {"min": 98, "max": 98, "text": "Pamphlet: Android Overlords"}, {"min": 99, "max": 99, "text": "Interstellar Compass, Always Points to Homeworld"}]}','psg',8,55);
INSERT OR IGNORE INTO "contents" VALUES(56,'🏷️',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "\"I''m Not A Rocket Scientist / But You''re An Idiot\""}, {"min": 1, "max": 1, "text": "Medic Patch (Skull and Crossbones over Cross)"}, {"min": 2, "max": 2, "text": "\"Don''t Run You''ll Only Die Tired\" Backpatch"}, {"min": 3, "max": 3, "text": "Red Shirt Logo"}, {"min": 4, "max": 4, "text": "Blood Type (Reference Patch)"}, {"min": 5, "max": 5, "text": "\"Do I LOOK Like An Expert?\""}, {"min": 6, "max": 6, "text": "Biohazard Symbol"}, {"min": 7, "max": 7, "text": "Mr. Yuck"}, {"min": 8, "max": 8, "text": "Nuclear Symbol"}, {"min": 9, "max": 9, "text": "\"Eat The Rich\""}, {"min": 10, "max": 10, "text": "\"Be Sure: Doubletap\""}, {"min": 11, "max": 11, "text": "Flame Emoji"}, {"min": 12, "max": 12, "text": "Smiley Face (Glow in the Dark)"}, {"min": 13, "max": 13, "text": "\"Smile: Big Brother is Watching\""}, {"min": 14, "max": 14, "text": "Jolly Roger"}, {"min": 15, "max": 15, "text": "Viking Skull"}, {"min": 16, "max": 16, "text": "\"APEX PREDATOR\" (Sabertooth Skull)"}, {"min": 17, "max": 17, "text": "Pin-Up Model (Ace of Spades)"}, {"min": 18, "max": 18, "text": "Queen of Hearts"}, {"min": 19, "max": 19, "text": "Security Guard"}, {"min": 20, "max": 20, "text": "\"LONER\""}, {"min": 21, "max": 21, "text": "\"Front Towards Enemy\" (Claymore Mine)"}, {"min": 22, "max": 22, "text": "Pin-Up Model (Riding Missile)"}, {"min": 23, "max": 23, "text": "FUBAR"}, {"min": 24, "max": 24, "text": "\"I''m A (Love) Machine\""}, {"min": 25, "max": 25, "text": "Pin-Up Model (Mechanic)"}, {"min": 26, "max": 26, "text": "\"HELLO MY NAME IS:\""}, {"min": 27, "max": 27, "text": "\"Powered By Coffee\""}, {"min": 28, "max": 28, "text": "\"Take Me To Your Leader\" (UFO)"}, {"min": 29, "max": 29, "text": "\"DO YOUR JOB\""}, {"min": 30, "max": 30, "text": "\"Take My Life (Please)\""}, {"min": 31, "max": 31, "text": "\"Upstanding Citizen\""}, {"min": 32, "max": 32, "text": "\"Allergic To Bullshit\" (Medical Style Patch)"}, {"min": 33, "max": 33, "text": "\"Fix Me First\" (Caduceus)"}, {"min": 34, "max": 34, "text": "\"I Like My Tools Clean / And My Lovers Dirty\""}, {"min": 35, "max": 35, "text": "\"The Louder You Scream the Faster I Come\" (Nurse Pin-Up)"}, {"min": 36, "max": 36, "text": "HMFIC (Head Mother Fucker In Charge)"}, {"min": 37, "max": 37, "text": "Dove in Crosshairs"}, {"min": 38, "max": 38, "text": "Chibi Cthulhu"}, {"min": 39, "max": 39, "text": "\"Welcome to the DANGER ZONE\""}, {"min": 40, "max": 40, "text": "Skull and Crossed Wrenches"}, {"min": 41, "max": 41, "text": "Pin-Up Model (Succubus)"}, {"min": 42, "max": 42, "text": "\"DILLIGAF?\""}, {"min": 43, "max": 43, "text": "\"DRINK / FIGHT / FUCK\""}, {"min": 44, "max": 44, "text": "\"Work Hard / Party Harder\""}, {"min": 45, "max": 45, "text": "Mudflap Girl"}, {"min": 46, "max": 46, "text": "Fun Meter (reads: Bad Time)"}, {"min": 47, "max": 47, "text": "\"GAME OVER\" (Bride & Groom)"}, {"min": 48, "max": 48, "text": "Heart"}, {"min": 49, "max": 49, "text": "\"IMPROVE / ADAPT / OVERCOME\""}, {"min": 50, "max": 50, "text": "\"SUCK IT UP\""}, {"min": 51, "max": 51, "text": "\"Cowboy Up\" (Crossed Revolvers)"}, {"min": 52, "max": 52, "text": "\"Troubleshooter\""}, {"min": 53, "max": 53, "text": "NASA Logo"}, {"min": 54, "max": 54, "text": "Crossed Hammers with Wings"}, {"min": 55, "max": 55, "text": "\"Keep Well Lubricated\""}, {"min": 56, "max": 56, "text": "Soviet Hammer & Sickle"}, {"min": 57, "max": 57, "text": "\"Plays Well With Others\""}, {"min": 58, "max": 58, "text": "\"Live Free and Die\""}, {"min": 59, "max": 59, "text": "\"IF I''M RUNNING KEEP UP\" Backpatch"}, {"min": 60, "max": 60, "text": "\"Meat Bag\""}, {"min": 61, "max": 61, "text": "\"I Am Not A Robot\""}, {"min": 62, "max": 62, "text": "Red Gear"}, {"min": 63, "max": 63, "text": "\"I Can''t Fix Stupid\""}, {"min": 64, "max": 64, "text": "\"Space IS My Home\" (Sad Astronaut)"}, {"min": 65, "max": 65, "text": "All Seeing Eye"}, {"min": 66, "max": 66, "text": "\"Solve Et Coagula\" (Baphomet)"}, {"min": 67, "max": 67, "text": "\"All Out of Fucks To Give\" (Astronaut with Turned Out Pockets)"}, {"min": 68, "max": 68, "text": "\"Travel To Distant Places / Meet Unusual Things / Get Eaten\""}, {"min": 69, "max": 69, "text": "BOHICA (Bend Over Here It Comes Again)"}, {"min": 70, "max": 70, "text": "\"I Am My Brother''s Keeper\""}, {"min": 71, "max": 71, "text": "\"Mama Tried\""}, {"min": 72, "max": 72, "text": "Black Widow Spider"}, {"min": 73, "max": 73, "text": "\"My Other Ride Married You\""}, {"min": 74, "max": 74, "text": "\"One Size Fits All\" (Grenade)"}, {"min": 75, "max": 75, "text": "Grim Reaper Backpatch"}, {"min": 76, "max": 76, "text": "\u043e\u0442\u044a\u0435\u0431\u0438\u0441\u044c (\"Fuck Off,\" Russian)"}, {"min": 77, "max": 77, "text": "\"Smooth Operator\""}, {"min": 78, "max": 78, "text": "Atom Symbol"}, {"min": 79, "max": 79, "text": "\"For Science!\""}, {"min": 80, "max": 80, "text": "\"Actually, I AM A Rocket Scientist\""}, {"min": 81, "max": 81, "text": "\"Help Wanted\""}, {"min": 82, "max": 82, "text": "Princess"}, {"min": 83, "max": 83, "text": "\"NOMAD\""}, {"min": 84, "max": 84, "text": "\"GOOD BOY\""}, {"min": 85, "max": 85, "text": "Dice (Snake Eyes)"}, {"min": 86, "max": 86, "text": "\"#1 Worker\""}, {"min": 87, "max": 87, "text": "\"Good\" (Brain)"}, {"min": 88, "max": 88, "text": "\"Bad Bitch\""}, {"min": 89, "max": 89, "text": "\"Too Pretty To Die\""}, {"min": 90, "max": 90, "text": "\"Fuck Forever\" (Roses)"}, {"min": 91, "max": 91, "text": "Icarus"}, {"min": 92, "max": 92, "text": "\"Girl''s Best Friend\" (Diamond)"}, {"min": 93, "max": 93, "text": "Risk of Electrocution Symbol"}, {"min": 94, "max": 94, "text": "Inverted Cross"}, {"min": 95, "max": 95, "text": "\"Do You Sign My Paychecks?\" Backpatch"}, {"min": 96, "max": 96, "text": "\"I \u2665 Myself\""}, {"min": 97, "max": 97, "text": "Double Cherry"}, {"min": 98, "max": 98, "text": "\"Volunteer\""}, {"min": 99, "max": 99, "text": "Poker Hand: Dead Man''s Hand (Aces Full of Eights)"}]}','psg',9,56);
INSERT OR IGNORE INTO "contents" VALUES(57,'🔧',NULL,NULL,'[{"label_key": "cost", "value": "20cr", "type": "cost"}]',NULL,'psg',10,57);
INSERT OR IGNORE INTO "contents" VALUES(58,'💊',NULL,NULL,'[{"label_key": "cost", "value": "1.5kcr", "type": "cost"}]',NULL,'psg',10,58);
INSERT OR IGNORE INTO "contents" VALUES(59,'🔋',NULL,NULL,'[{"label_key": "cost", "value": "500cr", "type": "cost"}]',NULL,'psg',10,59);
INSERT OR IGNORE INTO "contents" VALUES(60,'🔭',NULL,NULL,'[{"label_key": "cost", "value": "150cr", "type": "cost"}]',NULL,'psg',10,60);
INSERT OR IGNORE INTO "contents" VALUES(61,'📡',NULL,NULL,'[{"label_key": "cost", "value": "3kcr", "type": "cost"}]',NULL,'psg',10,61);
INSERT OR IGNORE INTO "contents" VALUES(62,'📷',NULL,NULL,'[{"label_key": "cost", "value": "50cr", "type": "cost"}]',NULL,'psg',10,62);
INSERT OR IGNORE INTO "contents" VALUES(63,'🕯️',NULL,NULL,'[{"label_key": "cost", "value": "5cr", "type": "cost"}]',NULL,'psg',10,63);
INSERT OR IGNORE INTO "contents" VALUES(64,'🔬',NULL,NULL,'[{"label_key": "cost", "value": "2kcr", "type": "cost"}]',NULL,'psg',10,64);
INSERT OR IGNORE INTO "contents" VALUES(65,'🔌',NULL,NULL,'[{"label_key": "cost", "value": "100cr", "type": "cost"}]',NULL,'psg',10,65);
INSERT OR IGNORE INTO "contents" VALUES(66,'🚨',NULL,NULL,'[{"label_key": "cost", "value": "2kcr", "type": "cost"}]',NULL,'psg',10,66);
INSERT OR IGNORE INTO "contents" VALUES(67,'🦾',NULL,NULL,'[{"label_key": "cost", "value": "100kcr", "type": "cost"}]',NULL,'psg',10,67);
INSERT OR IGNORE INTO "contents" VALUES(68,'💣',NULL,NULL,'[{"label_key": "cost", "value": "500cr", "type": "cost"}]',NULL,'psg',10,68);
INSERT OR IGNORE INTO "contents" VALUES(69,'🩹',NULL,NULL,'[{"label_key": "cost", "value": "75cr", "type": "cost"}]',NULL,'psg',10,69);
INSERT OR IGNORE INTO "contents" VALUES(70,'🔦',NULL,NULL,'[{"label_key": "cost", "value": "30cr", "type": "cost"}]',NULL,'psg',10,70);
INSERT OR IGNORE INTO "contents" VALUES(71,'🛏️',NULL,NULL,'[{"label_key": "cost", "value": "150cr", "type": "cost"}]',NULL,'psg',10,71);
INSERT OR IGNORE INTO "contents" VALUES(72,'☢️',NULL,NULL,'[{"label_key": "cost", "value": "20cr", "type": "cost"}]',NULL,'psg',10,72);
INSERT OR IGNORE INTO "contents" VALUES(73,'🖥️',NULL,NULL,'[{"label_key": "cost", "value": "100cr", "type": "cost"}]',NULL,'psg',10,73);
INSERT OR IGNORE INTO "contents" VALUES(74,'👁️',NULL,NULL,'[{"label_key": "cost", "value": "1.5kcr", "type": "cost"}]',NULL,'psg',10,74);
INSERT OR IGNORE INTO "contents" VALUES(75,'🚀',NULL,NULL,'[{"label_key": "cost", "value": "75kcr", "type": "cost"}]',NULL,'psg',10,75);
INSERT OR IGNORE INTO "contents" VALUES(76,'🔓',NULL,NULL,'[{"label_key": "cost", "value": "40cr", "type": "cost"}]',NULL,'psg',10,76);
INSERT OR IGNORE INTO "contents" VALUES(77,'📻',NULL,NULL,'[{"label_key": "cost", "value": "1kcr", "type": "cost"}]',NULL,'psg',10,77);
INSERT OR IGNORE INTO "contents" VALUES(78,'👢',NULL,NULL,'[{"label_key": "cost", "value": "350cr", "type": "cost"}]',NULL,'psg',10,78);
INSERT OR IGNORE INTO "contents" VALUES(79,'🏥',NULL,NULL,'[{"label_key": "cost", "value": "8kcr", "type": "cost"}]',NULL,'psg',10,79);
INSERT OR IGNORE INTO "contents" VALUES(80,'⛺',NULL,NULL,'[{"label_key": "cost", "value": "1kcr", "type": "cost"}]',NULL,'psg',10,80);
INSERT OR IGNORE INTO "contents" VALUES(81,'🍱',NULL,NULL,'[{"label_key": "cost", "value": "70cr", "type": "cost"}]',NULL,'psg',10,81);
INSERT OR IGNORE INTO "contents" VALUES(82,'🌡️',NULL,NULL,'[{"label_key": "cost", "value": "10cr", "type": "cost"}]',NULL,'psg',10,82);
INSERT OR IGNORE INTO "contents" VALUES(83,'💨',NULL,NULL,'[{"label_key": "cost", "value": "50cr", "type": "cost"}]',NULL,'psg',10,83);
INSERT OR IGNORE INTO "contents" VALUES(84,'🪢',NULL,NULL,'[{"label_key": "cost", "value": "10cr", "type": "cost"}]',NULL,'psg',10,84);
INSERT OR IGNORE INTO "contents" VALUES(85,'🩺',NULL,NULL,'[{"label_key": "cost", "value": "200cr", "type": "cost"}]',NULL,'psg',10,85);
INSERT OR IGNORE INTO "contents" VALUES(86,'📍',NULL,NULL,'[{"label_key": "cost", "value": "200cr", "type": "cost"}]',NULL,'psg',10,86);
INSERT OR IGNORE INTO "contents" VALUES(87,'🐾',NULL,NULL,'[{"label_key": "cost", "value": "200kcr", "type": "cost"}]',NULL,'psg',10,87);
INSERT OR IGNORE INTO "contents" VALUES(88,'🤖',NULL,NULL,'[{"label_key": "cost", "value": "15kcr", "type": "cost"}]',NULL,'psg',10,88);
INSERT OR IGNORE INTO "contents" VALUES(89,'💻',NULL,NULL,'[{"label_key": "cost", "value": "1.5kcr", "type": "cost"}]',NULL,'psg',10,89);
INSERT OR IGNORE INTO "contents" VALUES(90,'🧬',NULL,NULL,'[{"label_key": "cost", "value": "200cr", "type": "cost"}]',NULL,'psg',10,90);
INSERT OR IGNORE INTO "contents" VALUES(91,'📵',NULL,NULL,'[{"label_key": "cost", "value": "4kcr", "type": "cost"}]',NULL,'psg',10,91);
INSERT OR IGNORE INTO "contents" VALUES(92,'😷',NULL,NULL,'[{"label_key": "cost", "value": "500cr", "type": "cost"}]',NULL,'psg',10,92);
INSERT OR IGNORE INTO "contents" VALUES(93,'🎒',NULL,NULL,'[{"label_key": "cost", "value": "50cr", "type": "cost"}]',NULL,'psg',10,93);
INSERT OR IGNORE INTO "contents" VALUES(94,'🚁',NULL,NULL,'[{"label_key": "cost", "value": "10kcr", "type": "cost"}]',NULL,'psg',10,94);
INSERT OR IGNORE INTO "contents" VALUES(95,'🧪',NULL,NULL,'[{"label_key": "cost", "value": "50cr", "type": "cost"}]',NULL,'psg',10,95);
INSERT OR IGNORE INTO "contents" VALUES(96,'📟',NULL,NULL,'[{"label_key": "cost", "value": "100cr", "type": "cost"}]',NULL,'psg',10,96);
INSERT OR IGNORE INTO "contents" VALUES(97,'🎯',NULL,NULL,'[{"label_key": "cost", "value": "10kcr", "type": "cost"}]',NULL,'psg',10,97);
INSERT OR IGNORE INTO "contents" VALUES(98,'💉',NULL,NULL,'[{"label_key": "cost", "value": "1kcr", "type": "cost"}]',NULL,'psg',10,98);
INSERT OR IGNORE INTO "contents" VALUES(99,'💧',NULL,NULL,'[{"label_key": "cost", "value": "50cr", "type": "cost"}]',NULL,'psg',10,99);
INSERT OR IGNORE INTO "contents" VALUES(100,'🎯',NULL,NULL,NULL,NULL,'psg',18,100);
INSERT OR IGNORE INTO "contents" VALUES(101,'🛟',NULL,NULL,NULL,NULL,'psg',18,101);
INSERT OR IGNORE INTO "contents" VALUES(102,'⚖️',NULL,NULL,NULL,NULL,'psg',19,102);
INSERT OR IGNORE INTO "contents" VALUES(103,'😤',NULL,NULL,NULL,NULL,'psg',20,103);
INSERT OR IGNORE INTO "contents" VALUES(104,'🎲',NULL,NULL,NULL,'{"die": "d20", "entries": [{"min": 1, "max": 1, "text": "ADRENALINE RUSH. [+] on all rolls for 2d10 minutes. Reduce Stress by 1d5."}, {"min": 2, "max": 2, "text": "NERVOUS. Gain 1 Stress."}, {"min": 3, "max": 3, "text": "JUMPY. Gain 1 Stress. All Close crewmembers gain 2 Stress."}, {"min": 4, "max": 4, "text": "OVERWHELMED. [-] on all rolls for 1d10 minutes. Increase Minimum Stress by 1."}, {"min": 5, "max": 5, "text": "COWARD. New Condition: You must make a Fear Save to engage in violence, otherwise you flee."}, {"min": 6, "max": 6, "text": "FRIGHTENED. New Condition: When encountering what frightened you, make a Fear Save [-] or gain 1d5 Stress."}, {"min": 7, "max": 7, "text": "NIGHTMARES. New Condition: Sleep is difficult, gain [-] on Rest Saves."}, {"min": 8, "max": 8, "text": "LOSS OF CONFIDENCE. New Condition: Choose one Skill and lose that Skill''s bonus."}, {"min": 9, "max": 9, "text": "DEFLATED. New Condition: Whenever a Close crewmember fails a Save, gain 1 Stress."}, {"min": 10, "max": 10, "text": "DOOMED. New Condition: You feel cursed and unlucky. All Critical Successes are instead Critical Failures."}, {"min": 11, "max": 11, "text": "SUSPICIOUS. For the next week, whenever someone joins the crew (even briefly), make a Fear Save or gain 1 Stress."}, {"min": 12, "max": 12, "text": "HAUNTED. New Condition: Something starts visiting the character at night. In their dreams. Out of the corner of their eye. And soon it will start making demands."}, {"min": 13, "max": 13, "text": "DEATH WISH. For the next 24 hours, whenever encountering a stranger or known enemy, make a Sanity Save or immediately attack them."}, {"min": 14, "max": 14, "text": "PROPHETIC VISION. Character immediately experiences an intense hallucination or vision of an impending terror or horrific event. Increase Minimum Stress by 2."}, {"min": 15, "max": 15, "text": "CATATONIC. Become unresponsive and unmoving for 2d10 minutes. Reduce Stress by 1d10."}, {"min": 16, "max": 16, "text": "RAGE. [+] on all Damage rolls for 1d10 hours. All crewmembers gain 1 Stress."}, {"min": 17, "max": 17, "text": "SPIRALING. New Condition: Panic Checks are at [-]."}, {"min": 18, "max": 18, "text": "COMPOUNDING PROBLEMS. Roll twice on this table. Increase Minimum Stress by 1."}, {"min": 19, "max": 19, "text": "HEART ATTACK / SHORT CIRCUIT (ANDROIDS). Reduce Maximum Wounds by 1. [-] on all rolls for 1d10 hours. Increase Minimum Stress by 1."}, {"min": 20, "max": 20, "text": "RETIRE. Roll up a new character to play."}]}','psg',21,104);
INSERT OR IGNORE INTO "contents" VALUES(105,'😵',NULL,NULL,NULL,NULL,'psg',21,105);
INSERT OR IGNORE INTO "contents" VALUES(106,'🗣️',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,106);
INSERT OR IGNORE INTO "contents" VALUES(107,'🦎',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,107);
INSERT OR IGNORE INTO "contents" VALUES(108,'🌱',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,108);
INSERT OR IGNORE INTO "contents" VALUES(109,'🪨',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,109);
INSERT OR IGNORE INTO "contents" VALUES(110,'⚙️',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,110);
INSERT OR IGNORE INTO "contents" VALUES(111,'🪛',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,111);
INSERT OR IGNORE INTO "contents" VALUES(112,'⚗️',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,112);
INSERT OR IGNORE INTO "contents" VALUES(113,'💻',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,113);
INSERT OR IGNORE INTO "contents" VALUES(114,'🌌',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,114);
INSERT OR IGNORE INTO "contents" VALUES(115,'➕',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,115);
INSERT OR IGNORE INTO "contents" VALUES(116,'🎨',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,116);
INSERT OR IGNORE INTO "contents" VALUES(117,'🏺',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,117);
INSERT OR IGNORE INTO "contents" VALUES(118,'✝️',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,118);
INSERT OR IGNORE INTO "contents" VALUES(119,'🎖️',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,119);
INSERT OR IGNORE INTO "contents" VALUES(120,'🌃',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,120);
INSERT OR IGNORE INTO "contents" VALUES(121,'🏃',NULL,NULL,'[{"label_key": "tier", "value": "Trained +10", "type": "stat"}]',NULL,'psg',22,121);
INSERT OR IGNORE INTO "contents" VALUES(122,'🧠',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,122);
INSERT OR IGNORE INTO "contents" VALUES(123,'🦠',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,123);
INSERT OR IGNORE INTO "contents" VALUES(124,'🩺',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,124);
INSERT OR IGNORE INTO "contents" VALUES(125,'🌿',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,125);
INSERT OR IGNORE INTO "contents" VALUES(126,'⛏️',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,126);
INSERT OR IGNORE INTO "contents" VALUES(127,'🔨',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,127);
INSERT OR IGNORE INTO "contents" VALUES(128,'💥',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,128);
INSERT OR IGNORE INTO "contents" VALUES(129,'💊',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,129);
INSERT OR IGNORE INTO "contents" VALUES(130,'🖥️',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,130);
INSERT OR IGNORE INTO "contents" VALUES(131,'✈️',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,131);
INSERT OR IGNORE INTO "contents" VALUES(132,'⚛️',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,132);
INSERT OR IGNORE INTO "contents" VALUES(133,'🔮',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,133);
INSERT OR IGNORE INTO "contents" VALUES(134,'🔫',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,134);
INSERT OR IGNORE INTO "contents" VALUES(135,'🥊',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,135);
INSERT OR IGNORE INTO "contents" VALUES(136,'🏕️',NULL,NULL,'[{"label_key": "tier", "value": "Expert +15", "type": "stat"}]',NULL,'psg',22,136);
INSERT OR IGNORE INTO "contents" VALUES(137,'👽',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,137);
INSERT OR IGNORE INTO "contents" VALUES(138,'🧬',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,138);
INSERT OR IGNORE INTO "contents" VALUES(139,'✂️',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,139);
INSERT OR IGNORE INTO "contents" VALUES(140,'🪐',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,140);
INSERT OR IGNORE INTO "contents" VALUES(141,'🤖',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,141);
INSERT OR IGNORE INTO "contents" VALUES(142,'🏗️',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,142);
INSERT OR IGNORE INTO "contents" VALUES(143,'🦿',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,143);
INSERT OR IGNORE INTO "contents" VALUES(144,'🧮',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,144);
INSERT OR IGNORE INTO "contents" VALUES(145,'🌀',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,145);
INSERT OR IGNORE INTO "contents" VALUES(146,'🔯',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,146);
INSERT OR IGNORE INTO "contents" VALUES(147,'⭐',NULL,NULL,'[{"label_key": "tier", "value": "Master +20", "type": "stat"}]',NULL,'psg',22,147);
INSERT OR IGNORE INTO "contents" VALUES(148,'📅',NULL,NULL,NULL,NULL,'psg',24,148);
INSERT OR IGNORE INTO "contents" VALUES(149,'🎖️',NULL,NULL,NULL,NULL,'psg',25,149);
INSERT OR IGNORE INTO "contents" VALUES(150,'🌫️',NULL,NULL,NULL,NULL,'psg',32,0);
INSERT OR IGNORE INTO "contents" VALUES(151,'🩸',NULL,NULL,NULL,NULL,'psg',32,0);
INSERT OR IGNORE INTO "contents" VALUES(152,'🧊',NULL,NULL,NULL,NULL,'psg',32,0);
INSERT OR IGNORE INTO "contents" VALUES(153,'🍱',NULL,NULL,NULL,NULL,'psg',32,0);
INSERT OR IGNORE INTO "contents" VALUES(154,'💨',NULL,NULL,NULL,NULL,'psg',33,0);
INSERT OR IGNORE INTO "contents" VALUES(155,'☢️',NULL,NULL,NULL,'{"die": "d3", "entries": [{"min": 1, "max": 1, "text": "Level 1 \u2013 Trace: Normal everyday radiation, cosmic rays. No immediate damage. Possible long-term side effects (cancer, etc.)."}, {"min": 2, "max": 2, "text": "Level 2 \u2013 Acute: Unshielded reactors, warp cores. Reduce all Stats and Saves by 1 every round."}, {"min": 3, "max": 3, "text": "Level 3 \u2013 Lethal: Atomic weapons, direct handling of warp cores. Every round: Body Save or lethal dose (death in 1d5 days)."}]}','psg',33,0);
INSERT OR IGNORE INTO "contents" VALUES(156,'💊',NULL,NULL,NULL,NULL,'psg',33,0);
INSERT OR IGNORE INTO "contents" VALUES(157,'🌡️',NULL,NULL,NULL,NULL,'psg',33,0);
INSERT OR IGNORE INTO "contents" VALUES(158,'🩹',NULL,NULL,NULL,NULL,'psg',34,0);
INSERT OR IGNORE INTO "contents" VALUES(159,'📋',NULL,NULL,NULL,NULL,'psg',34,0);
INSERT OR IGNORE INTO "contents" VALUES(160,'🤝',NULL,NULL,'[{"label_key": "cost", "value": "~150cr", "type": "cost"}]',NULL,'psg',35,0);
INSERT OR IGNORE INTO "contents" VALUES(161,'🧠',NULL,NULL,'[{"label_key": "cost", "value": "100kcr", "type": "cost"}]',NULL,'psg',35,0);
INSERT OR IGNORE INTO "contents" VALUES(162,'💆',NULL,NULL,'[{"label_key": "cost", "value": "24kcr", "type": "cost"}]',NULL,'psg',35,0);
INSERT OR IGNORE INTO "contents" VALUES(163,'🎮',NULL,NULL,'[{"label_key": "cost", "value": "1kcr", "type": "cost"}]',NULL,'psg',35,0);
INSERT OR IGNORE INTO "contents" VALUES(164,'🛏️',NULL,NULL,'[{"label_key": "cost", "value": "6kcr", "type": "cost"}]',NULL,'psg',35,0);
INSERT OR IGNORE INTO "contents" VALUES(165,'💉',NULL,NULL,'[{"label_key": "cost", "value": "18kcr", "type": "cost"}]',NULL,'psg',35,0);
INSERT OR IGNORE INTO "contents" VALUES(166,'✂️',NULL,NULL,'[{"label_key": "cost", "value": "28kcr", "type": "cost"}]',NULL,'psg',35,0);
INSERT OR IGNORE INTO "contents" VALUES(167,'🏙️',NULL,NULL,NULL,NULL,'psg',38,0);
INSERT OR IGNORE INTO "contents" VALUES(168,'🍻',NULL,NULL,NULL,NULL,'psg',39,0);
INSERT OR IGNORE INTO "contents" VALUES(169,'📊',NULL,NULL,NULL,NULL,'psg',40,0);
INSERT OR IGNORE INTO "contents" VALUES(170,'💰',NULL,NULL,NULL,NULL,'psg',40,0);
INSERT OR IGNORE INTO "contents" VALUES(171,'🎲',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "Archaeologist (6kcr/mo | Combat 20, Instinct 15, Wounds 1) \u2014 Secretly investigating a Corporate cover-up."}, {"min": 1, "max": 9, "text": "Asteroid Miner (2kcr/mo | Combat 25, Instinct 25, Wounds 2) \u2014 Sending money back home to family."}, {"min": 10, "max": 19, "text": "Android (6kcr/mo | Combat 20, Instinct 35, Wounds 2) \u2014 Badly needs to pay off a loan shark."}, {"min": 20, "max": 24, "text": "Bodyguard (2kcr/mo | Combat 30, Instinct 25, Wounds 2) \u2014 Can''t stop in one place for too long, gets restless."}, {"min": 25, "max": 29, "text": "Captain (10kcr/mo | Combat 30, Instinct 40, Wounds 3) \u2014 Hears a call from an entity they can''t explain."}, {"min": 30, "max": 34, "text": "Chaplain (750cr/mo | Combat 10, Instinct 20, Wounds 2) \u2014 Using you/your ship to smuggle contraband."}, {"min": 35, "max": 39, "text": "Corporate Fixer (24kcr/mo | Combat 15, Instinct 30, Wounds 1) \u2014 Revenge."}, {"min": 40, "max": 44, "text": "Doctor (8kcr/mo | Combat 15, Instinct 25, Wounds 1) \u2014 Secretly a con artist with no other expertise."}, {"min": 45, "max": 49, "text": "Engineer (7kcr/mo | Combat 20, Instinct 25, Wounds 2) \u2014 Paying a loved one''s medical bills."}, {"min": 50, "max": 54, "text": "Hacker (8kcr/mo | Combat 15, Instinct 30, Wounds 1) \u2014 Secretly a spy for a rival corporation."}, {"min": 55, "max": 59, "text": "Marine (Grunt) (1.5kcr/mo | Combat 30, Instinct 25, Wounds 2) \u2014 Needs to pay off jumped bail or a court fine."}, {"min": 60, "max": 64, "text": "Marine (Officer) (3.5kcr/mo | Combat 35, Instinct 35, Wounds 3) \u2014 Undercover secret police investigating your crew."}, {"min": 65, "max": 69, "text": "Pilot (3kcr/mo | Combat 15, Instinct 25, Wounds 1) \u2014 In huge debt to a powerful crime syndicate."}, {"min": 70, "max": 74, "text": "Pioneer (1.5kcr/mo | Combat 25, Instinct 25, Wounds 1) \u2014 Took the money and ran out on their last job."}, {"min": 75, "max": 79, "text": "Scientist (4kcr/mo | Combat 15, Instinct 10, Wounds 1) \u2014 Family member held hostage, needs ransom."}, {"min": 80, "max": 84, "text": "Survivor (3kcr/mo | Combat 30, Instinct 35, Wounds 2) \u2014 Secretly a bounty hunter looking for your crew."}, {"min": 85, "max": 89, "text": "Surgeon (12kcr/mo | Combat 15, Instinct 20, Wounds 1) \u2014 Seeking an honorable and glorious death."}, {"min": 90, "max": 94, "text": "Teamster (2kcr/mo | Combat 25, Instinct 25, Wounds 1) \u2014 Unknowingly contagious with a deadly disease."}, {"min": 95, "max": 98, "text": "Therapist (3kcr/mo | Combat 10, Instinct 20, Wounds 1) \u2014 Escaped from a corporate research facility."}, {"min": 99, "max": 99, "text": "Void Urchin (100cr/mo | Combat 30, Instinct 40, Wounds 2) \u2014 Secretly a wanted serial killer in hiding."}]}','psg',41,0);
INSERT OR IGNORE INTO "contents" VALUES(172,'🎬',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 1, "max": 1, "text": "Explore the Unknown \u2014 Survey an uncharted planet or strange vessel. No backup. God speed."}, {"min": 2, "max": 2, "text": "Investigate a Strange Rumor \u2014 Something is alive in the vents. Colonists are disappearing. Separating fact from fiction was the easy part."}, {"min": 3, "max": 3, "text": "Salvage a Derelict Ship \u2014 Distress signal on repeat. Scans show no life. Every abandoned ship is abandoned for a reason."}, {"min": 4, "max": 4, "text": "Exterminate an Otherworldly Threat \u2014 No one goes outside anymore. Wipe them out by any means. Bring back a living sample."}, {"min": 5, "max": 5, "text": "Visit an Offworld Colony \u2014 The Company hasn''t heard from the miners on PK-294. Get production back on track."}, {"min": 6, "max": 6, "text": "Undertake a Dangerous Mission \u2014 A C-level''s child kidnapped by a fringe group. Android activists want to sabotage a facility. No scruples required."}, {"min": 7, "max": 7, "text": "Survive a Colossal Disaster \u2014 Abandon ship! Radiation leaks and warp anomalies. Make it to the escape pods before the station collapses."}, {"min": 8, "max": 8, "text": "Respond to a Distress Signal \u2014 Help is never nearby on the rim. You can never tell legitimate cries from traps laid by wolves."}, {"min": 9, "max": 9, "text": "Transport Precious Cargo \u2014 They won''t tell you what''s in the container. Don''t open it, don''t scan it, don''t listen to anything it says."}, {"min": 10, "max": 10, "text": "Make Contact with the Beyond \u2014 Found at the edge of the system. Eons old, intricate stonework. When the probe arrived, it started humming a tune."}]}','wom',6,172);
INSERT OR IGNORE INTO "contents" VALUES(173,'🏙️',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Space Station"}, {"min": 1, "max": 1, "text": "Aboard Your Own Ship"}, {"min": 2, "max": 2, "text": "Military Outpost"}, {"min": 3, "max": 3, "text": "Prison Complex"}, {"min": 4, "max": 4, "text": "Derelict Spacecraft"}, {"min": 5, "max": 5, "text": "Religious Compound"}, {"min": 6, "max": 6, "text": "Mining Colony"}, {"min": 7, "max": 7, "text": "Research Facility"}, {"min": 8, "max": 8, "text": "Underwater Base"}, {"min": 9, "max": 9, "text": "Mothership"}]}','wom',6,173);
INSERT OR IGNORE INTO "contents" VALUES(174,'🛡️',NULL,NULL,NULL,NULL,'wom',10,174);
INSERT OR IGNORE INTO "contents" VALUES(175,'🔍',NULL,NULL,NULL,NULL,'wom',12,175);
INSERT OR IGNORE INTO "contents" VALUES(176,'🤝',NULL,NULL,NULL,NULL,'wom',16,176);
INSERT OR IGNORE INTO "contents" VALUES(177,'⚡',NULL,NULL,NULL,'{"die": "d12", "entries": [{"min": 1, "max": 1, "text": "High Ground \u2014 One side is located high above the other and has an advantage in attacking and defending."}, {"min": 2, "max": 2, "text": "Kinetic Potential \u2014 Objects in the area have the potential to deal a great amount of damage, radically changing the situation."}, {"min": 3, "max": 3, "text": "Breach \u2014 The enemy is deeply entrenched in a highly defensible position which must be defeated first."}, {"min": 4, "max": 4, "text": "Take & Hold \u2014 One side must capture an objective and defend it until reinforcements arrive."}, {"min": 5, "max": 5, "text": "Escalation Risk \u2014 The longer the encounter takes, the more likely it is to spiral out of control."}, {"min": 6, "max": 6, "text": "Ambush \u2014 If one side is surprised, the encounter will end quickly."}, {"min": 7, "max": 7, "text": "Stealth Mission \u2014 Stealth and silence are required for the situation not to escalate."}, {"min": 8, "max": 8, "text": "Collateral Damage \u2014 There are non-combatants in the area which must be considered and may be leveraged by enemies."}, {"min": 9, "max": 9, "text": "Danger Zone \u2014 The encounter takes place in a limited area; straying from it risks damage or death."}, {"min": 10, "max": 10, "text": "Key Objective \u2014 The encounter ends as soon as a key objective is reached, captured, or killed."}, {"min": 11, "max": 11, "text": "Pursuit & Evade \u2014 One side is attempting to get to a location and the other party must stop them."}, {"min": 12, "max": 12, "text": "Rules of Engagement \u2014 One side is required to be non-lethal, radically altering the weapons at the players'' disposal."}]}','wom',11,177);
INSERT OR IGNORE INTO "contents" VALUES(178,'🗺️',NULL,NULL,NULL,NULL,'wom',18,178);
INSERT OR IGNORE INTO "contents" VALUES(179,'😱',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 4, "text": "T: Making first contact | O: Dead animals | M: Alien creature | B: Righting a wrong | S: Returns in 100 years"}, {"min": 5, "max": 9, "text": "T: Studying arcane text | O: Visions of future victims | M: Deranged killer | B: Human sacrifice | S: Recurring hallucinations"}, {"min": 10, "max": 14, "text": "T: Boarding a ship | O: Writing on the wall | M: Elder evil returned | B: Vaccine | S: Victims forever scarred"}, {"min": 15, "max": 19, "text": "T: Opening a grave | O: Stigmata | M: Cult | B: Only harmed by fire | S: Slumbers until next Jump"}, {"min": 20, "max": 24, "text": "T: Mining strange ore | O: Unexplained suicides | M: Tainted technology | B: Nuking from orbit | S: Retreats into hiding"}, {"min": 25, "max": 29, "text": "T: Trespassing | O: Distress signal | M: Colossal space being | B: Obscure occult ritual | S: Feigns death, escapes"}, {"min": 30, "max": 34, "text": "T: Gross negligence | O: Stranger appears | M: Ruthless apex predator | B: Returning it to its home | S: Awaits next Transgression"}, {"min": 35, "max": 39, "text": "T: Tampering with biology | O: Abnormal birth | M: Ghost or spirit | B: Tough, but killable | S: Recurring nightmares"}, {"min": 40, "max": 44, "text": "T: Reneging on a deal | O: Unlucky numbers | M: Tangled mass of flesh | B: Giving it what it wants | S: Possesses closest victim"}, {"min": 45, "max": 49, "text": "T: Disturbing holy site | O: Ancient distress beacon | M: Mutated being | B: Special weapon | S: Awakens if Transgression is repeated"}, {"min": 50, "max": 54, "text": "T: Leaving someone behind | O: Android having visions | M: Child | B: Making a pact with it | S: Hibernates deep underground"}, {"min": 55, "max": 59, "text": "T: Study of strange relic | O: Ancient recorded warning | M: Biological experiment | B: Serving it | S: Whispers from the shadows"}, {"min": 60, "max": 64, "text": "T: Forgotten atrocity | O: Researcher''s incoherent notes | M: Sentient environment | B: Learning its true identity | S: Evolves into its more powerful form"}, {"min": 65, "max": 69, "text": "T: Interfacing with forbidden technology | O: Irrational computer behavior | M: Gateway or portal | B: Certain kinds of light | S: Hidden in the background of screens"}, {"min": 70, "max": 74, "text": "T: Landing on uncharted planet | O: Significant astrological alignment | M: Dream | B: It can''t be killed, only avoided | S: Slumbers in its killer''s mind"}, {"min": 75, "max": 79, "text": "T: Altering its natural habitat | O: Speaking in tongues | M: Cybernetic organism | B: Interment in rightful resting place | S: Herald of a greater Horror to come"}, {"min": 80, "max": 84, "text": "T: Breaking a cultural taboo | O: Mysterious disappearances | M: Haunted location | B: Closing the portal/gate | S: Uploads into nearest computer"}, {"min": 85, "max": 89, "text": "T: Failing to stop a previous Transgression | O: Strange weather phenomena | M: Doppelganger | B: Requires a certain time/location | S: Never stay in one place \u2014 it will find you"}, {"min": 90, "max": 94, "text": "T: Ingesting an unknown substance | O: Ancient calendar foretells arrival | M: Invisible being | B: Sending it to another dimension | S: Parental entity comes looking for answers"}, {"min": 95, "max": 99, "text": "T: Allowing harm to come to an innocent | O: Gruesomely displayed corpse(s) | M: Mothership | B: Trapping it inside a powerful container | S: Apocalyptic events set in motion"}]}','wom',2,179);
INSERT OR IGNORE INTO "contents" VALUES(180,'🌑',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 3, "text": "Death, ancient, arise"}, {"min": 4, "max": 9, "text": "Underwater, sunken, drowning"}, {"min": 10, "max": 12, "text": "Politics, government, nationalism"}, {"min": 13, "max": 16, "text": "Humanity, love, memory"}, {"min": 17, "max": 19, "text": "Resistance, struggle, suffering"}, {"min": 20, "max": 22, "text": "Travel, road-weariness, rural"}, {"min": 23, "max": 25, "text": "Darkness, absence, void"}, {"min": 26, "max": 29, "text": "Medicine, hospitals, surgery"}, {"min": 30, "max": 32, "text": "Rust, the Machine, noise"}, {"min": 33, "max": 35, "text": "Transformation, rebirth"}, {"min": 36, "max": 38, "text": "Childhood, innocence, time"}, {"min": 39, "max": 41, "text": "Underground, crime, buried"}, {"min": 42, "max": 43, "text": "Fading beauty, age, fame"}, {"min": 44, "max": 46, "text": "Technology, excess, decay"}, {"min": 47, "max": 49, "text": "Abduction, identity, silence"}, {"min": 50, "max": 52, "text": "The City, rain, flood"}, {"min": 53, "max": 55, "text": "Fear, the afterlife, prophecy"}, {"min": 56, "max": 58, "text": "Factories, work, oppression"}, {"min": 59, "max": 61, "text": "Belief, god, hell"}, {"min": 62, "max": 64, "text": "Cold, sleep, snow"}, {"min": 65, "max": 67, "text": "Fire, ashes, war"}, {"min": 68, "max": 71, "text": "Hunger, famine, food"}, {"min": 72, "max": 74, "text": "Pleasure, touch, passion"}, {"min": 75, "max": 77, "text": "Artifice, dolls, toys"}, {"min": 78, "max": 81, "text": "Meat, slaughter, animal"}, {"min": 82, "max": 84, "text": "Truth, solitude, loneliness"}, {"min": 85, "max": 87, "text": "Wilderness, nature, growth"}, {"min": 88, "max": 91, "text": "Capitalism, greed, fortune"}, {"min": 92, "max": 94, "text": "Chaos, change, laughter"}, {"min": 95, "max": 99, "text": "Abandoned, empty, forgotten"}]}','wom',2,180);
INSERT OR IGNORE INTO "contents" VALUES(181,'📖',NULL,NULL,NULL,NULL,'wom',8,181);
INSERT OR IGNORE INTO "contents" VALUES(182,'🧩',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 4, "text": "Alarm \u2014 If solved incorrectly, sets off an alarm alerting nearby enemies."}, {"min": 5, "max": 9, "text": "Connect the Dots \u2014 Connect a series of dots using some kind of item (e.g. wires, light, water, blood)."}, {"min": 10, "max": 13, "text": "Construction \u2014 Construct an item using pieces that must be found or provided."}, {"min": 14, "max": 17, "text": "Dilemma \u2014 Choose between the lesser of two evils or the greater of two goods."}, {"min": 18, "max": 21, "text": "Egg Carry \u2014 Safely deliver a delicate or vulnerable item/organism to a certain location."}, {"min": 22, "max": 25, "text": "Find the Clue \u2014 Search for one or more objects leading to more Questions, Puzzles, or Answers."}, {"min": 26, "max": 29, "text": "Guardian \u2014 Defeat, appease, or bypass a guardian who denies access to a location or item."}, {"min": 30, "max": 34, "text": "Hazardous Path \u2014 Route blocked by danger which must be avoided, circumnavigated, or defeated."}, {"min": 35, "max": 38, "text": "Illusion \u2014 Contains an element that appears to be one thing but is actually another."}, {"min": 39, "max": 42, "text": "Labyrinth \u2014 Forces players to navigate a maze or complicated path."}, {"min": 43, "max": 47, "text": "Lock & Key \u2014 Collect an item (the key) and use it on the lock to gain access."}, {"min": 48, "max": 51, "text": "Missing Part \u2014 Locate a missing item for the puzzle to work properly."}, {"min": 52, "max": 56, "text": "Mundane Obstacle \u2014 A real-world problem (broken elevator, collapsed pylon, etc.)."}, {"min": 57, "max": 60, "text": "Outside-the-Box \u2014 No obvious solution; players must bring outside resources to bear."}, {"min": 61, "max": 64, "text": "Pattern Recognition \u2014 Requires noticing repeated symbols or other repeated information."}, {"min": 65, "max": 69, "text": "Remote Switch \u2014 Activate a switch in another location to bypass the current obstacle."}, {"min": 70, "max": 73, "text": "Riddle \u2014 Requires recitation of a coded phrase or password."}, {"min": 74, "max": 78, "text": "Rising Tide \u2014 Danger that escalates naturally, forcing a quick solution or harm."}, {"min": 79, "max": 82, "text": "Sacrifice \u2014 Requires players to sacrifice something of great value."}, {"min": 83, "max": 86, "text": "Sequence \u2014 Complete a certain number of steps in a specific order."}, {"min": 87, "max": 90, "text": "Teamwork \u2014 Multiple players must do something simultaneously."}, {"min": 91, "max": 93, "text": "Timelock \u2014 Solve in a certain amount of time or fail (or restart the attempt)."}, {"min": 94, "max": 96, "text": "Trap \u2014 The puzzle punishes players for failed attempts."}, {"min": 97, "max": 99, "text": "Trial and Error \u2014 Players must experiment with several ingredients to solve the puzzle."}]}','wom',13,182);
INSERT OR IGNORE INTO "contents" VALUES(183,'🔄',NULL,NULL,NULL,NULL,'wom',26,183);
INSERT OR IGNORE INTO "contents" VALUES(184,'⚖️',NULL,NULL,NULL,NULL,'wom',30,184);
INSERT OR IGNORE INTO "contents" VALUES(185,'📊',NULL,NULL,NULL,NULL,'wom',33,185);
INSERT OR IGNORE INTO "contents" VALUES(186,'🛠️',NULL,NULL,NULL,NULL,'wom',52,186);
INSERT OR IGNORE INTO "contents" VALUES(187,'💬',NULL,NULL,NULL,NULL,'wom',36,187);
INSERT OR IGNORE INTO "contents" VALUES(188,'💥',NULL,NULL,NULL,NULL,'wom',37,188);
INSERT OR IGNORE INTO "contents" VALUES(189,'🔎',NULL,NULL,NULL,NULL,'wom',38,189);
INSERT OR IGNORE INTO "contents" VALUES(190,'🚀',NULL,NULL,NULL,NULL,'wom',39,190);
INSERT OR IGNORE INTO "contents" VALUES(191,'🗒️',NULL,NULL,NULL,NULL,'wom',41,191);
INSERT OR IGNORE INTO "contents" VALUES(192,'🌌',NULL,NULL,NULL,NULL,'wom',42,192);
INSERT OR IGNORE INTO "contents" VALUES(193,'🏢',NULL,NULL,NULL,NULL,'wom',47,193);
INSERT OR IGNORE INTO "contents" VALUES(194,'⚙️',NULL,NULL,NULL,NULL,'wom',46,194);
INSERT OR IGNORE INTO "contents" VALUES(195,'💼',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 1, "text": "PRODUCTION & MANUFACTURE — Asteroid mining, derelict salvage and scrap, strikebreaking, terraformer installation, and android troubleshooting."}, {"min": 2, "max": 3, "text": "SHIPPING & HANDLING — Cargo freight, VIP escort, scrap hauling, prisoner transport, sensitive materials handling, passenger transport, and contraband smuggling."}, {"min": 4, "max": 5, "text": "RESEARCH & DEVELOPMENT — Sample & specimen collection, planetary survey, field testing, sabotage, containment breach, archaeological dig, and corporate espionage."}, {"min": 6, "max": 7, "text": "RISK MANAGEMENT — Sweep and clear, liquidation, asset protection, quarantine enforcement, bounty hunting, distress signal response, and system patrol."}, {"min": 8, "max": 8, "text": "HUMAN RESOURCES — Missing persons, suspicious death, communication breakdown, troubleshooting, AI negotiation, and settlement evacuation."}, {"min": 9, "max": 9, "text": "MERGERS & ACQUISITIONS — Asset recovery, salvage retention, personnel recruitment, first contact protocol, repossession, and piracy."}]}','wom',48,195);
INSERT OR IGNORE INTO "contents" VALUES(196,'💰',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "POWERFUL FAVOR — The client can''t pay, but owes the crew a big favor to call in at their discretion. Lifestyle: DEAD BROKE — 1d10 days of living expenses or one piece of cheap equipment."}, {"min": 1, "max": 9, "text": "DESPERATE — Pays 1d10×100cr up front. This is all the money the client has. Doing this job makes them a long-time ally. Lifestyle: SCRAPING BY — 1d10 weeks of living expenses or one piece of decent equipment."}, {"min": 10, "max": 34, "text": "BARTER AGREEMENT — Trade only: astronavigation data, ship repairs, weapons, equipment, or other accommodations. Lifestyle: NEED WORK — 1d10 months of living expenses or one piece of expensive equipment."}, {"min": 35, "max": 93, "text": "GRUNT WORK — Pays the crew''s salaries; expenses are the crew''s to handle. No Jump Pay or Hazard Pay. Lifestyle: PAYING DOWN DEBT — C/B/A-Class Shore Leave, cheap cybermod, medical treatment, minor bribe, or skill training."}, {"min": 94, "max": 98, "text": "PAYDAY — Pays 1d10×10,000cr upon completion and up to 10% up front. All travel expenses paid; up to 1d10 Contractors provided. Lifestyle: FLUSH WITH CREDITS — X/S-Class Shore Leave, decent cybermod, or a ship upgrade."}, {"min": 99, "max": 99, "text": "JACKPOT — Pays 1d10×1,000,000cr upon completion and up to 1d10×10,000cr up front. All necessary expenses paid; private contractors available. Lifestyle: I CAN RETIRE AFTER THIS JOB — Enough for a small ship, small business, or retirement."}]}','wom',49,196);
INSERT OR IGNORE INTO "contents" VALUES(197,'📈',NULL,NULL,NULL,NULL,'wom',50,197);
INSERT OR IGNORE INTO "contents" VALUES(198,'🔚',NULL,NULL,NULL,NULL,'wom',57,198);
INSERT OR IGNORE INTO "contents" VALUES(199,'🪐',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 2, "text": "Liquid"}, {"min": 3, "max": 7, "text": "Terrestrial"}, {"min": 8, "max": 9, "text": "Gas"}]}','wom',58,199);
INSERT OR IGNORE INTO "contents" VALUES(200,'🏔️',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 4, "text": "CATENA — crater chain"}, {"min": 5, "max": 8, "text": "CHAOS — broken terrain"}, {"min": 9, "max": 12, "text": "COLLIS — small hill"}, {"min": 13, "max": 16, "text": "CRATER — impact valley"}, {"min": 17, "max": 20, "text": "DORSUM — ridge"}, {"min": 21, "max": 24, "text": "ERUPTIVE CENTER — volcano"}, {"min": 25, "max": 28, "text": "FOSSA — trough"}, {"min": 29, "max": 32, "text": "LABES — landslide"}, {"min": 33, "max": 35, "text": "LABYRINTHUS — complex of intersecting valleys/ridges"}, {"min": 36, "max": 39, "text": "LACUS — ''lake'' or small plain"}, {"min": 40, "max": 43, "text": "LANDING SITE"}, {"min": 44, "max": 47, "text": "MARE — ''sea'' on a moon"}, {"min": 48, "max": 51, "text": "MENSA — mesa"}, {"min": 52, "max": 56, "text": "MONS — mountain"}, {"min": 57, "max": 60, "text": "MONTES — mountain range"}, {"min": 61, "max": 65, "text": "PATERA — irregular crater"}, {"min": 66, "max": 69, "text": "PLANITIA — low plain"}, {"min": 70, "max": 73, "text": "PLANUM — high plain or plateau"}, {"min": 74, "max": 77, "text": "RUPES — cliff or scarp"}, {"min": 78, "max": 81, "text": "RIMA — fissure"}, {"min": 82, "max": 85, "text": "SAXUM — boulder"}, {"min": 86, "max": 89, "text": "TERRA — extensive land mass"}, {"min": 90, "max": 94, "text": "THOLUS — small mountain"}, {"min": 95, "max": 99, "text": "UNDAE — field of dunes"}]}','wom',58,200);
INSERT OR IGNORE INTO "contents" VALUES(201,'🏛️',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Religious Group"}, {"min": 1, "max": 5, "text": "Corporation"}, {"min": 6, "max": 7, "text": "Government"}, {"min": 8, "max": 8, "text": "Union"}, {"min": 9, "max": 9, "text": "Criminal Organization"}]}','wom',58,201);
INSERT OR IGNORE INTO "contents" VALUES(202,'👥',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "A single person."}, {"min": 1, "max": 2, "text": "A small handful of people."}, {"min": 3, "max": 4, "text": "A few dozen people."}, {"min": 5, "max": 6, "text": "Roughly a hundred people."}, {"min": 7, "max": 7, "text": "A few hundred people."}, {"min": 8, "max": 8, "text": "Roughly a thousand people."}, {"min": 9, "max": 9, "text": "Overpopulated."}]}','wom',58,202);
INSERT OR IGNORE INTO "contents" VALUES(203,'🤝',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "The Seraphim Institute"}, {"min": 1, "max": 9, "text": "The Outer Rim Colonial Marshalls (OCRM)"}, {"min": 10, "max": 19, "text": "SEBACO Mining Ltd."}, {"min": 20, "max": 26, "text": "The Teamster''s Union"}, {"min": 27, "max": 31, "text": "The Alliance of Hyperspace Jump Couriers"}, {"min": 32, "max": 35, "text": "The Evangelical Solarian Church (AKA The Solarians)"}, {"min": 36, "max": 40, "text": "Los Niños Basura"}, {"min": 41, "max": 44, "text": "The Computer Coders Collective (AKA T-Triple-C)"}, {"min": 45, "max": 48, "text": "PROJECT RICHTER"}, {"min": 49, "max": 52, "text": "BAS-Lehman Ges.m.b.H"}, {"min": 53, "max": 56, "text": "Tannhäuser Heavy Industries"}, {"min": 57, "max": 60, "text": "The Synthetic Liberation Front"}, {"min": 61, "max": 64, "text": "Parker-Vance Holding Company"}, {"min": 65, "max": 68, "text": "The Interstellar Postal Inspection Service"}, {"min": 69, "max": 72, "text": "The Komarov Squad"}, {"min": 73, "max": 76, "text": "The Interstellar Asteroid Miners Association"}, {"min": 77, "max": 80, "text": "The Jump-9 Club"}, {"min": 81, "max": 84, "text": "Second Samael Church"}, {"min": 85, "max": 89, "text": "The Zero-G Laborers Coalition (AKA Zed-GLC)"}, {"min": 90, "max": 90, "text": "REDKNIFE Psyops Unit"}, {"min": 91, "max": 91, "text": "The Astronavigator''s Guild"}, {"min": 92, "max": 92, "text": "The Organization"}, {"min": 93, "max": 93, "text": "Revolutionary Forces of Luna"}, {"min": 94, "max": 94, "text": "The Interplanetary Sex Workers Union"}, {"min": 95, "max": 95, "text": "The Space Monkey Mafia"}, {"min": 96, "max": 96, "text": "House Sivaranjan"}, {"min": 97, "max": 97, "text": "Uplifted Dolphin Pod 67"}, {"min": 98, "max": 98, "text": "Aleph Gate"}, {"min": 99, "max": 99, "text": "FRIEND"}]}','wom',58,203);
INSERT OR IGNORE INTO "contents" VALUES(204,'⚓',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "X-Class Port — Abandoned. No services. Dangerous."}, {"min": 1, "max": 5, "text": "C-Class Port — Basic docking and refuelling. Minimal amenities."}, {"min": 6, "max": 7, "text": "B-Class Port — Standard services, local markets, some Shore Leave options."}, {"min": 8, "max": 8, "text": "A-Class Port — Well-equipped hub. Good medical, Shore Leave, and trade options."}, {"min": 9, "max": 9, "text": "S-Class Port — Major transit hub. Full services. Luxury Shore Leave available."}]}','wom',58,204);
INSERT OR IGNORE INTO "contents" VALUES(205,'🏚️',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "Forced Relocation Slum"}, {"min": 1, "max": 9, "text": "Terraformer Colony"}, {"min": 10, "max": 19, "text": "Mining Colony"}, {"min": 20, "max": 26, "text": "Colonial Settlement"}, {"min": 27, "max": 32, "text": "Marine Garrison"}, {"min": 33, "max": 35, "text": "Research Facility"}, {"min": 36, "max": 38, "text": "Corporate Operations Center"}, {"min": 39, "max": 41, "text": "Manufacturing Complex"}, {"min": 42, "max": 44, "text": "Deep Sea Research Base"}, {"min": 45, "max": 47, "text": "Heavy Industry Complex"}, {"min": 48, "max": 50, "text": "Shipping & Logistics Center"}, {"min": 51, "max": 53, "text": "Ore Refinery"}, {"min": 54, "max": 56, "text": "Forward Military Base"}, {"min": 57, "max": 59, "text": "Rural Backworld Installation"}, {"min": 60, "max": 62, "text": "Corporate Resupply Depot"}, {"min": 63, "max": 65, "text": "Monitoring Outpost"}, {"min": 66, "max": 68, "text": "Off-World Training Installation"}, {"min": 69, "max": 71, "text": "Polar Research Station"}, {"min": 72, "max": 74, "text": "Restricted Testing Facility"}, {"min": 75, "max": 77, "text": "Maximum Security Prison Complex"}, {"min": 78, "max": 80, "text": "Stakeholder Camp"}, {"min": 81, "max": 83, "text": "Farming Colony"}, {"min": 84, "max": 86, "text": "Prison, formerly a… (roll again)"}, {"min": 87, "max": 89, "text": "Autonomous Factory Zone"}, {"min": 90, "max": 91, "text": "Independent Frontier Settlement"}, {"min": 92, "max": 92, "text": "Covert Pirate Base"}, {"min": 93, "max": 93, "text": "Classified Corporate Installation"}, {"min": 94, "max": 94, "text": "Desolate Scrapworld"}, {"min": 95, "max": 95, "text": "Major Colonial Settlement"}, {"min": 96, "max": 96, "text": "Religious Compound"}, {"min": 97, "max": 97, "text": "Anti-corporate Rebel Base"}, {"min": 98, "max": 98, "text": "Undisclosed Black Site"}, {"min": 99, "max": 99, "text": "Private C-Suite Game Preserve"}]}','wom',59,205);
INSERT OR IGNORE INTO "contents" VALUES(206,'📜',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "The Maru Banking Colonies"}, {"min": 1, "max": 4, "text": "False Europa"}, {"min": 5, "max": 8, "text": "The Egosystem"}, {"min": 9, "max": 12, "text": "The MIDAS-12 Massacre"}, {"min": 13, "max": 16, "text": "The Shadow Algorithm"}, {"min": 17, "max": 20, "text": "Universal Remote"}, {"min": 21, "max": 24, "text": "The Conway Machine"}, {"min": 25, "max": 28, "text": "The Book of Sar"}, {"min": 29, "max": 32, "text": "MOGUL: Maximum Prison Planet"}, {"min": 33, "max": 36, "text": "The Orlov Incident"}, {"min": 37, "max": 40, "text": "Fred, the Disappearing Man"}, {"min": 41, "max": 44, "text": "The Creeping Fog"}, {"min": 45, "max": 48, "text": "Mindpillers"}, {"min": 49, "max": 52, "text": "The Precursors"}, {"min": 53, "max": 56, "text": "Zygotean Mercenaries"}, {"min": 57, "max": 60, "text": "The Teaman Murders"}, {"min": 61, "max": 64, "text": "The Whispering Plague"}, {"min": 65, "max": 68, "text": "Sea of Tranquility Conspiracy"}, {"min": 69, "max": 72, "text": "UCSCV Mournbringer Flight 364"}, {"min": 73, "max": 76, "text": "The Bracewell Autonomous Zone"}, {"min": 77, "max": 80, "text": "Spasi, Otets, Syna"}, {"min": 81, "max": 83, "text": "Cosmetic Vampire Hoax"}, {"min": 84, "max": 84, "text": "IMG 2238"}, {"min": 85, "max": 85, "text": "The Magnetic Typhoon"}, {"min": 86, "max": 86, "text": "The Battle for Columbia Gate"}, {"min": 87, "max": 87, "text": "The Spitz-Okoro Theorem"}, {"min": 88, "max": 88, "text": "The Uplifted Possums"}, {"min": 89, "max": 89, "text": "The Silent Century"}, {"min": 90, "max": 90, "text": "Naktari War Syndrome"}, {"min": 91, "max": 91, "text": "The Autumnal City at Bellona"}, {"min": 92, "max": 92, "text": "Origin Point Zero"}, {"min": 93, "max": 93, "text": "The Mountebank Game"}, {"min": 94, "max": 94, "text": "The Helium Uprising"}, {"min": 95, "max": 95, "text": "The Dearborn Corpse"}, {"min": 96, "max": 96, "text": "Wombship"}, {"min": 97, "max": 97, "text": "The Hymn of Saeeda Dawn"}, {"min": 98, "max": 98, "text": "Divinity Strain"}, {"min": 99, "max": 99, "text": "Rey Burtnolds is Alive and Well and Living on Casimir"}]}','wom',56,206);
INSERT OR IGNORE INTO "contents" VALUES(207,'🌍',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 1, "text": "Giant (Crushing Gravity)"}, {"min": 2, "max": 4, "text": "Mini-Giant (Heavy Gravity)"}, {"min": 5, "max": 6, "text": "Earth-Sized Planet (Normal Gravity)"}, {"min": 7, "max": 9, "text": "Dwarf Planet (Light Gravity)"}]}','wom',58,207);
INSERT OR IGNORE INTO "contents" VALUES(208,'💨',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 1, "text": "Corrosive"}, {"min": 2, "max": 3, "text": "Toxic"}, {"min": 4, "max": 5, "text": "Thin"}, {"min": 6, "max": 8, "text": "Terraformed"}, {"min": 9, "max": 9, "text": "Pristine"}]}','wom',58,208);
INSERT OR IGNORE INTO "contents" VALUES(209,'🌡️',NULL,NULL,NULL,'{"die": "d10", "entries": [{"min": 0, "max": 0, "text": "Hellish"}, {"min": 1, "max": 2, "text": "Hot"}, {"min": 3, "max": 3, "text": "Balmy"}, {"min": 4, "max": 4, "text": "Temperate"}, {"min": 5, "max": 5, "text": "Heavenly"}, {"min": 6, "max": 6, "text": "Rainy"}, {"min": 7, "max": 7, "text": "Turbulent"}, {"min": 8, "max": 8, "text": "Cold"}, {"min": 9, "max": 9, "text": "Freezing"}]}','wom',58,209);
INSERT OR IGNORE INTO "contents" VALUES(210,'⚠️',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "Under quarantine."}, {"min": 1, "max": 9, "text": "Overworked, tired. Low morale."}, {"min": 10, "max": 19, "text": "Business as usual."}, {"min": 20, "max": 26, "text": "Workers on strike."}, {"min": 27, "max": 32, "text": "Hazardous working conditions."}, {"min": 33, "max": 35, "text": "Security forces in control."}, {"min": 36, "max": 38, "text": "Gross managerial misconduct."}, {"min": 39, "max": 41, "text": "Frequent storms."}, {"min": 42, "max": 44, "text": "Productivity low."}, {"min": 45, "max": 47, "text": "Corporate strikebreakers called in."}, {"min": 48, "max": 50, "text": "Hostile wildlife."}, {"min": 51, "max": 53, "text": "Military blockade."}, {"min": 54, "max": 56, "text": "Lush overgrown wilderness."}, {"min": 57, "max": 59, "text": "In desperate need of aid."}, {"min": 60, "max": 62, "text": "Weather frighteningly unstable."}, {"min": 63, "max": 65, "text": "Food shortage."}, {"min": 66, "max": 68, "text": "Colonists talking of joining a Union."}, {"min": 69, "max": 71, "text": "Awaiting orders from corporate."}, {"min": 72, "max": 74, "text": "Local Union elections."}, {"min": 75, "max": 77, "text": "Contract negotiation breakdown."}, {"min": 78, "max": 80, "text": "Low on supplies."}, {"min": 81, "max": 83, "text": "Massive crop failure."}, {"min": 84, "max": 86, "text": "Communications cut off."}, {"min": 87, "max": 89, "text": "Company holiday celebrations."}, {"min": 90, "max": 91, "text": "Under constant threat of terrorist attacks."}, {"min": 92, "max": 92, "text": "Local government crumbling."}, {"min": 93, "max": 93, "text": "Rumours of layoffs."}, {"min": 94, "max": 94, "text": "Overpopulation issue."}, {"min": 95, "max": 95, "text": "Settlement being shut down by corporate."}, {"min": 96, "max": 96, "text": "Petty bickering escalating out of control."}, {"min": 97, "max": 97, "text": "Population entirely synthetic."}, {"min": 98, "max": 98, "text": "Co-opted by military as temporary base."}, {"min": 99, "max": 99, "text": "Mutiny brewing."}]}','wom',59,210);
INSERT OR IGNORE INTO "contents" VALUES(211,'👁️',NULL,NULL,NULL,'{"die": "d100", "entries": [{"min": 0, "max": 0, "text": "Failed utopia."}, {"min": 1, "max": 9, "text": "Unsolved string of gruesome murders."}, {"min": 10, "max": 19, "text": "Home to powerful criminal syndicate."}, {"min": 20, "max": 26, "text": "Local customs are strange, wary of outsiders."}, {"min": 27, "max": 32, "text": "Deserted."}, {"min": 33, "max": 35, "text": "Secretly a corporate re-education camp."}, {"min": 36, "max": 38, "text": "Settlement has newfound religious significance."}, {"min": 39, "max": 41, "text": "Company secretly dosing the water."}, {"min": 42, "max": 44, "text": "Live hostage situation."}, {"min": 45, "max": 47, "text": "Local environment is a radioactive wasteland."}, {"min": 48, "max": 50, "text": "Rapidly growing doomsday cult."}, {"min": 51, "max": 53, "text": "Controlled by separatist militia."}, {"min": 54, "max": 56, "text": "Collapse of local social order."}, {"min": 57, "max": 59, "text": "Refugee crisis."}, {"min": 60, "max": 62, "text": "Extinction event."}, {"min": 63, "max": 65, "text": "Settlement has descended into anarchy."}, {"min": 66, "max": 68, "text": "Colonists report being replaced by imposters."}, {"min": 69, "max": 71, "text": "Secret military operation recently arrived."}, {"min": 72, "max": 74, "text": "Deadly viral outbreak."}, {"min": 75, "max": 77, "text": "Environmental collapse imminent."}, {"min": 78, "max": 80, "text": "Recent breakthrough discovery."}, {"min": 81, "max": 83, "text": "Settlement houses decadent corporate nobility."}, {"min": 84, "max": 86, "text": "Colonists slowly disappearing."}, {"min": 87, "max": 89, "text": "Strange black monolith unearthed."}, {"min": 90, "max": 91, "text": "Rumours of meddling from powerful AI."}, {"min": 92, "max": 92, "text": "Colonists believe settlement haunted."}, {"min": 93, "max": 93, "text": "Android uprising imminent."}, {"min": 94, "max": 94, "text": "Gigantic unidentifiable fossilised remains."}, {"min": 95, "max": 95, "text": "Reports of interference by ''Celestials.''"}, {"min": 96, "max": 96, "text": "Wreckage of spacecraft of unknown origin."}, {"min": 97, "max": 97, "text": "Ruins of precursor star-faring civilisation found."}, {"min": 98, "max": 98, "text": "Ancient gateway recently uncovered."}, {"min": 99, "max": 99, "text": "First Contact event."}]}','wom',59,211);
-- content_i18n
INSERT OR IGNORE INTO "content_i18n" VALUES(1,23,'en','Turn Order','Violence in Mothership is incredibly dangerous and should be avoided at all costs. During a violent confrontation, time splits into roughly 10-second intervals called rounds. Everything within a round happens simultaneously.

The Warden describes the situation. Each player describes their reaction. Everyone commits, then the Warden resolves all actions at once, assigning Stat Checks and Saves. Damage and Wounds are resolved last. Then the next round begins.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(2,23,'ru','Порядок Ходов','Насилие в Mothership невероятно опасно — избегайте его любой ценой. Во время столкновения время делится на раунды примерно по 10 секунд. Всё в раунде происходит одновременно.

Варден описывает ситуацию, затем каждый игрок описывает реакцию своего персонажа. Все берут обязательства, после чего Варден разрешает все действия разом, назначая Проверки и Спасброски. Урон и Ранения разрешаются последними. Затем начинается следующий раунд.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(3,23,'ua','Порядок Ходів','Насильство у Mothership надзвичайно небезпечне — уникайте його будь-якою ціною. Під час сутички час ділиться на раунди приблизно по 10 секунд. Усе в раунді відбувається одночасно.

Варден описує ситуацію, потім кожен гравець описує реакцію свого персонажа. Всі беруть зобов''язання, після чого Варден розв''язує всі дії разом, призначаючи Перевірки та Порятунки. Шкода та Поранення розв''язуються останніми. Потім починається наступний раунд.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(4,24,'en','Surprise','If there is a chance characters are ambushed or stunned by a horrific encounter, the Warden calls for a Fear Save. Those who succeed can react; those who fail are too shocked to act until the next round.

Strict Turn Order: If preferred, everyone makes a Speed Check at the start of the encounter. Success means acting before the enemies; failure means acting after. Speed Checks can be called again if the situation changes dramatically.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(5,24,'ru','Внезапность','Если есть шанс, что персонажи окажутся в засаде или будут потрясены ужасной встречей, Варден требует Спасбросок Страха. Успех — можно действовать; провал — слишком потрясены, чтобы действовать до следующего раунда.

Строгий порядок ходов: при желании все делают Проверку Скорости в начале схватки. Успех — ход до врагов; провал — ход после. Проверку можно вызвать снова при резком изменении ситуации.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(6,24,'ua','Раптовість','Якщо є шанс, що персонажів можуть застати в засідці або вони будуть приголомшені жахливою зустріччю, Варден вимагає Порятунок від Страху. Успіх — можна діяти; провал — занадто приголомшені для дій до наступного раунду.

Суворий порядок ходів: за бажанням усі роблять Перевірку Швидкості на початку сутички. Успіх — хід до ворогів; провал — хід після. Перевірку можна викликати знову при різкій зміні ситуації.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(7,25,'en','What Can I Do?','Characters can generally move to somewhere within Close Range and then do one thing before the situation changes.

Things you can attempt in a round:
• Attack something or someone
• Bandage a wound
• Check vital signs with a medscanner
• Move again (up to Close Range)
• Fire a vehicle''s weapon
• Maneuver or pilot a vehicle
• Open an airlock
• Operate a machine
• Reload a weapon
• Throw something at or to someone
• Use a computer terminal

If you do nothing but run, you can move within Long Range during the round.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(8,25,'ru','Что Я Могу Сделать?','Персонажи обычно могут переместиться на Близкую Дистанцию и сделать одно действие до изменения ситуации.

Что можно сделать за раунд:
• Атаковать
• Перевязать рану
• Проверить жизненные показатели медсканером
• Ещё раз переместиться (до Близкой Дистанции)
• Выстрелить из оружия транспортного средства
• Управлять транспортным средством
• Открыть шлюз
• Управлять машиной
• Перезарядить оружие
• Бросить что-то кому-то
• Использовать компьютерный терминал

Если только бежать — можно переместиться на Дальнюю Дистанцию за раунд.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(9,25,'ua','Що Я Можу Зробити?','Персонажі зазвичай можуть переміститися на Близьку Дистанцію і зробити одну дію до зміни ситуації.

Що можна зробити за раунд:
• Атакувати
• Перев''язати рану
• Перевірити жизневі показники медсканером
• Ще раз переміститися (до Близької Дистанції)
• Вистрілити зі зброї транспортного засобу
• Керувати транспортним засобом
• Відкрити шлюз
• Керувати машиною
• Перезарядити зброю
• Кинути щось комусь
• Використати комп''ютерний термінал

Якщо тільки бігти — можна переміститися на Далеку Дистанцію за раунд.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(10,26,'en','How Do I Attack?','Make a Combat Check. If successful, roll the weapon''s Damage and subtract it from the enemy''s Health. If you fail, the situation gets worse and you gain 1 Stress.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(11,26,'ru','Как Атаковать?','Сделайте Проверку Боя. При успехе бросьте Урон оружия и вычтите из Здоровья врага. При провале ситуация ухудшается и вы получаете 1 Стресс.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(12,26,'ua','Як Атакувати?','Зробіть Перевірку Бою. При успіху киньте Шкоду зброї і відніміть від Здоров''я ворога. При провалі ситуація погіршується і ви отримуєте 1 Стрес.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(13,27,'en','Damage','When taking Damage (DMG), subtract it from Health. If your Health reaches zero, gain a Wound and roll on the Wounds Table. Reset Health to Maximum, then subtract any carryover damage. When a character suffers their Maximum Wounds, make a Death Save.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(14,27,'ru','Урон','При получении Урона вычтите его из Здоровья. Если Здоровье падает до нуля, получите Ранение и бросьте на Таблице Ранений. Сбросьте Здоровье до Максимума, вычтя остаточный урон. Когда персонаж получает Максимальное количество Ранений — совершите Спасбросок от Смерти.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(15,27,'ua','Шкода','При отриманні Шкоди відніміть її від Здоров''я. Якщо Здоров''я падає до нуля, отримайте Поранення і киньте на Таблиці Поранень. Скиньте Здоров''я до Максимуму, відніміши залишкову шкоду. Коли персонаж отримує Максимальну кількість Поранень — зробіть Порятунок від Смерті.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(16,28,'en','Armor','Characters ignore all Damage less than their Armor Points (AP). If they take Damage ≥ AP in one hit, armor is destroyed and they suffer the remaining Damage.

Weapons with Anti-Armor (AA) ignore and destroy armor on any hit.

Damage Reduction (DR) always reduces incoming Damage by the stated amount — even if armor is destroyed or the weapon has AA. DR applies first, before Armor.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(17,28,'ru','Броня','Персонажи игнорируют весь Урон меньше Очков Брони (AP). Если за один удар Урон ≥ AP, броня уничтожается и персонаж получает остаточный урон.

Оружие с Антибронью (AA) игнорирует и уничтожает броню при каждом попадании.

Снижение Урона (DR) всегда уменьшает входящий Урон — даже если броня уничтожена или у оружия есть AA. DR применяется первым, до брони.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(18,28,'ua','Броня','Персонажі ігнорують всю Шкоду менше Очок Броні (AP). Якщо за один удар Шкода ≥ AP, броня знищується і персонаж отримує залишкову шкоду.

Зброя з Антибронею (AA) ігнорує і знищує броню при кожному влученні.

Зниження Шкоди (DR) завжди зменшує вхідну Шкоду — навіть якщо броня знищена або зброя має AA. DR застосовується першим, до броні.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(19,29,'en','Cover','The environment can provide Cover. It is destroyed like armor when dealt Damage ≥ its AP. Cover typically protects only against ranged attacks. If you shoot while in Cover, you are out of Cover until your next turn.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(20,29,'ru','Укрытие','Окружение может давать Укрытие. Оно уничтожается как броня при Уроне ≥ его AP. Укрытие обычно защищает только от дальних атак. Если вы стреляете из Укрытия, то считаетесь вышедшим из него до своего следующего хода.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(21,29,'ua','Укриття','Навколишнє середовище може давати Укриття. Воно знищується як броня при Шкоді ≥ його AP. Укриття зазвичай захищає лише від далекобійних атак. Якщо ви стріляєте з Укриття, вважаєтеся таким, що вийшов з нього до свого наступного ходу.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(22,30,'en','What Are Wounds?','When gaining a Wound, roll 1d10 on the Wounds Table for the type of Damage received:

• Blunt Force — punched, hit with crowbar or thrown object, falling
• Bleeding — stabbed or cut
• Gunshot — shot by a firearm
• Fire & Explosives — grenades, flamethrowers, set on fire
• Gore & Massive — giant or gruesome attacks

Severity guide:
• Flesh Wound — small inconvenience
• Minor / Major Injury — lasting issues requiring medical treatment
• Lethal Injury — Death Save in 1d10 rounds
• Fatal Injury — Death Save immediately',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(23,30,'ru','Что такое Ранения?','При получении Ранения бросьте 1d10 на Таблице Ранений для типа полученного Урона:

• Тупой удар — удар кулаком, монтировкой или брошенным предметом, падение
• Кровотечение — удар ножом или порез
• Огнестрел — выстрел из огнестрельного оружия
• Огонь и взрывы — гранаты, огнемёты, поджог
• Расчленение — гигантские или жуткие атаки

Степень тяжести:
• Царапина — небольшое неудобство
• Лёгкая / Тяжёлая травма — продолжительные проблемы, требующие лечения
• Смертельная травма — Спасбросок от Смерти через 1d10 раундов
• Фатальная травма — Спасбросок от Смерти немедленно',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(24,30,'ua','Що таке Поранення?','При отриманні Поранення киньте 1d10 на Таблиці Поранень для типу отриманої Шкоди:

• Тупий удар — удар кулаком, монтировкою або кинутим предметом, падіння
• Кровотеча — удар ножем або порізання
• Вогнепальне — постріл з вогнепальної зброї
• Вогонь та вибухи — гранати, вогнемети, підпал
• Масивний урон — гігантські або жахливі атаки

Ступінь тяжкості:
• Подряпина — невелике незручність
• Легка / Важка травма — тривалі проблеми, що потребують лікування
• Смертельна травма — Порятунок від Смерті через 1d10 раундів
• Фатальна травма — Порятунок від Смерті негайно',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(25,31,'en','Wounds — Blunt Force','Roll when you are punched, hit with a crowbar or thrown object, or fall.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(26,31,'ru','Ранения — Тупой Удар','Бросьте при ударе кулаком, монтировкой, брошенным предметом или при падении.',NULL,'["Царапина. Сбит с ног.", "Задыхается. [-] пока не восстановит дыхание.", "Лёгкая травма. Вывих лодыжки. [-] на проверки Скорости.", "Сотрясение мозга. [-] на умственные задачи.", "Сломана нога или ступня. [-] на проверки Скорости.", "Тяжёлая травма. Сломана рука или кисть. [-] на физические задачи.", "Сломана ключица. [-] на проверки Силы.", "Смертельная травма (Спасбросок от Смерти через 1d10 раундов). Сломан позвоночник. [-] на все броски.", "Перелом черепа. [-] на все броски.", "Фатальная травма. Сломан позвоночник или шея. Спасбросок от Смерти."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(27,31,'ua','Поранення — Тупий Удар','Киньте при ударі кулаком, монтировкою, кинутим предметом або при падінні.',NULL,'["Подряпина. Збитий з ніг.", "Задихався. [-] поки не відновить дихання.", "Легка травма. Вивих щиколотки. [-] на перевірки Швидкості.", "Струс мозку. [-] на розумові задачі.", "Зламана нога або стопа. [-] на перевірки Швидкості.", "Важка травма. Зламана рука або кисть. [-] на фізичні задачі.", "Зламана ключиця. [-] на перевірки Сили.", "Смертельна травма (Рятівний від Смерті через 1d10 раундів). Зламаний хребет. [-] на всі кидки.", "Перелом черепа. [-] на всі кидки.", "Фатальна травма. Хребет або шия зламані. Рятівний від Смерті."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(28,32,'en','Wounds — Bleeding','Roll when you are stabbed or cut.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(29,32,'ru','Ранения — Кровотечение','Бросьте при ударе ножом или порезе.',NULL,'["Царапина. Выронил предмет в руке.", "Много крови. Те, кто рядом, получают 1 Стресс.", "Лёгкая травма. Кровь в глазах. [-] пока не вытрет.", "Рассечение. Кровотечение +1.", "Глубокий порез. Кровотечение +2.", "Тяжёлая травма. Пальцы рук/ног отсечены. Кровотечение +3.", "Кисть/стопа отсечена. Кровотечение +4.", "Смертельная травма (Спасбросок от Смерти через 1d10 раундов). Конечность отсечена. Кровотечение +5.", "Артерия перерезана. Кровотечение +6.", "Фатальная травма. Горло перерезано или сердце пробито. Спасбросок от Смерти."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(30,32,'ua','Поранення — Кровотеча','Киньте при ударі ножем або порізанні.',NULL,'["Подряпина. Впустив тримане.", "Багато крові. Ті, хто поруч, отримують 1 Стрес.", "Легка травма. Кров в очах. [-] поки не витре.", "Розтин. Кровотеча +1.", "Глибокий порізок. Кровотеча +2.", "Важка травма. Пальці рук/ніг відрубані. Кровотеча +3.", "Рука/нога відрубана. Кровотеча +4.", "Смертельна травма (Рятівний від Смерті через 1d10 раундів). Кінцівка відрубана. Кровотеча +5.", "Артерія перерізана. Кровотеча +6.", "Фатальна травма. Горло перерізане або серце пробите. Рятівний від Смерті."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(31,33,'en','Wounds — Gunshot','Roll when you are shot by a firearm.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(32,33,'ru','Ранения — Огнестрел','Бросьте при попадании огнестрельного оружия.',NULL,'["Царапина. Скользящее попадание. Сбит с ног.", "Кровотечение +1.", "Лёгкая травма. Сломано ребро.", "Перелом конечности.", "Внутреннее кровотечение. Кровотечение +2.", "Тяжёлая травма. Пуля застряла. Требуется операция.", "Огнестрельное ранение шеи.", "Смертельная травма (Спасбросок от Смерти через 1d10 раундов). Большая кровопотеря. Кровотечение +4.", "Проникающее ранение груди. Кровотечение +5.", "Фатальная травма. Выстрел в голову. Спасбросок от Смерти."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(33,33,'ua','Поранення — Вогнепальне','Киньте при влученні вогнепальної зброї.',NULL,'["Подряпина. Ковзнула куля. Збитий з ніг.", "Кровотеча +1.", "Легка травма. Зламане ребро.", "Перелом кінцівки.", "Внутрішня кровотеча. Кровотеча +2.", "Важка травма. Куля застрягла. Потрібна операція.", "Вогнепальне поранення шиї.", "Смертельна травма (Рятівний від Смерті через 1d10 раундів). Велика крововтрата. Кровотеча +4.", "Проникаюче поранення грудей. Кровотеча +5.", "Фатальна травма. Постріл в голову. Рятівний від Смерті."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(34,34,'en','Wounds — Fire & Explosives','Roll when hit by grenades, flamethrowers, or set on fire.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(35,34,'ru','Ранения — Огонь и Взрывы','Бросьте при попадании гранаты, огнемёта или поджоге.',NULL,'["Царапина. Волосы сгорели. Получите 1d5 Стресса.", "Крутой шрам. +1 Минимальный Стресс.", "Лёгкая травма. Опалён. [-] на следующее действие.", "Осколки / сильный ожог.", "Обширные ожоги.", "Тяжёлая травма. Сильный ожог. -2d10 Спасбросок Тела.", "Требуется пересадка кожи. -2d10 Спасбросок Тела.", "Смертельная травма (Спасбросок от Смерти через 1d10 раундов). Конечность горит. 2d10 урона в раунд.", "Тело горит. 3d10 урона в раунд.", "Фатальная травма. Поглощён огненным взрывом. Спасбросок от Смерти."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(36,34,'ua','Поранення — Вогонь та Вибухи','Киньте при влученні гранати, вогнемета або підпалу.',NULL,'["Подряпина. Волосся обгоріло. Отримайте 1d5 Стресу.", "Крутий шрам. +1 Мінімальний Стрес.", "Легка травма. Підпалений. [-] на наступну дію.", "Осколки / сильний опік.", "Великі опіки.", "Важка травма. Сильний опік. -2d10 Рятівний Тіла.", "Потрібне пересадження шкіри. -2d10 Рятівний Тіла.", "Смертельна травма (Рятівний від Смерті через 1d10 раундів). Кінцівка палає. 2d10 шкоди за раунд.", "Тіло в полум''ї. 3d10 шкоди за раунд.", "Фатальна травма. Охоплений вогняним вибухом. Рятівний від Смерті."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(37,35,'en','Wounds — Gore & Massive','Roll when hit by a giant creature or a gruesome, massive attack.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(38,35,'ru','Ранения — Расчленение','Бросьте при атаке гигантского существа или чудовищном ударе.',NULL,'["Царапина. Рвота. [-] на следующее действие.", "Крутой шрам. +1 Минимальный Стресс.", "Лёгкая травма. Палец искалечен.", "Глаза выколоты.", "Кусок плоти оторван. -1d10 Силы.", "Тяжёлая травма. Парализован ниже пояса.", "Конечность отсечена. Кровотечение +5.", "Смертельная травма (Спасбросок от Смерти через 1d10 раундов). Пронзён. Кровотечение +6.", "Кишки вывалились на пол. Кровотечение +7.", "Фатальная травма. Голова взрывается. Спасбросок от Смерти невозможен. Вы мертвы."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(39,35,'ua','Поранення — Масивний урон','Киньте при атаці гігантської істоти або при масивному ударі.',NULL,'["Подряпина. Блювота. [-] на наступну дію.", "Крутий шрам. +1 Мінімальний Стрес.", "Легка травма. Палець скалічений.", "Очі видряпані.", "Шматок плоті відірваний. -1d10 Сили.", "Важка травма. Паралізований нижче пояса.", "Кінцівка відрубана. Кровотеча +5.", "Смертельна травма (Рятівний від Смерті через 1d10 раундів). Наколотий на кіл. Кровотеча +6.", "Нутрощі розмотались по підлозі. Кровотеча +7.", "Фатальна травма. Голова вибухає. Рятівний від Смерті не застосовується. Ти помер."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(40,36,'en','Death Table','When you die, the Warden places 1d10 in a cup, shakes it, and places it face down on the table. As soon as someone spends a turn checking your vitals, the die is revealed.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(41,36,'ru','Таблица Смерти','Когда вы умираете, Варден кладёт 1d10 в стакан, трясёт его и кладёт перевёрнутым на стол. Как только кто-то тратит ход на проверку ваших жизненных показателей, кубик открывается.',NULL,'["Без сознания. Очнётесь через 2d10 минут. Уменьшите Максимальное Здоровье на 1d5.", "Без сознания и умираете. Вы умрёте через 1d5 раундов без вмешательства.", "В коме. Только экстраординарные меры могут вернуть вас в сознание.", "Вы умерли. Создайте нового персонажа."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(42,36,'ua','Таблиця Смерті','Коли ви вмираєте, Варден кладе 1d10 у стакан, трясе його і кладе перевернутим на стіл. Щойно хтось витрачає хід на перевірку ваших жизневих показників, кубик відкривається.',NULL,'["Непритомний. Прокинетесь через 2d10 хвилин. Зменшіть Максимальне Здоров''я на 1d5.", "Непритомний і вмираєте. Помрете через 1d5 раундів без втручання.", "У комі. Лише надзвичайні заходи можуть повернути вас до свідомості.", "Ви померли. Створіть нового персонажа."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(43,37,'en','Adjacent','You''re basically touching. Covers fist fights, close-quarters combat, and trying to escape a creature''s claws. Also covers using a computer terminal or administering first aid. You can talk, whisper, and even smell someone at this range.

Less than 1m / 3ft.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(44,37,'ru','Рядом','Вы практически касаетесь друг друга. Это рукопашный бой, попытки вырваться из когтей чудовища, использование компьютерного терминала или оказание первой помощи. На этой дистанции можно говорить, шептать и даже учуять запах.

Менее 1м / 3 фута.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(45,37,'ua','Поруч','Ви практично торкаєтеся одне одного. Це рукопашний бій, спроби вирватися з кігтів монстра, використання комп''ютерного терміналу або надання першої допомоги. На цій дистанції можна говорити, шептати і навіть відчути запах.

Менше 1м / 3 фути.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(46,38,'en','Close Range','Someone Close can be reached by running over to them in a few seconds. Near enough that you could throw something at them and hit them. You''d have to speak loud enough that someone on the other side of the room could hear you. Powerful stenches can be smelled. Firearms like shotguns are most effective at this range or Adjacent.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(47,38,'ru','Близкая Дистанция','На Близкой Дистанции можно добраться до кого-то за несколько секунд. Достаточно близко, чтобы бросить в него что-то и попасть. Нужно говорить достаточно громко, чтобы вас слышали на другом конце комнаты. Сильные запахи ощущаются на этой дистанции. Дробовики наиболее эффективны на Близкой Дистанции или Рядом.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(48,38,'ua','Близька Дистанція','На Близькій Дистанції можна дістатися до когось за кілька секунд. Досить близько, щоб кинути в нього щось і влучити. Треба говорити досить голосно, щоб вас чули на іншому кінці кімнати. Сильні запахи відчуваються на цій дистанції. Дробовики найбільш ефективні на Близькій Дистанції або Поруч.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(49,39,'en','Long Range','Things in this band are far enough away that they take an entire round or longer to reach. Rifles are effective at this range, but handguns and shotguns less so. You''d have to yell to get someone''s attention, and you won''t smell anyone, no matter how bad they stink.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(50,39,'ru','Дальняя Дистанция','На Дальней Дистанции враг настолько далеко, что добраться до него займёт целый раунд или дольше. Винтовки эффективны на этой дистанции, но пистолеты и дробовики — меньше. Чтобы привлечь внимание, нужно кричать; запах на этой дистанции не ощутить.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(51,39,'ua','Далека Дистанція','На Далекій Дистанції ворог настільки далеко, що дістатися до нього займе цілий раунд або більше. Гвинтівки ефективні на цій дистанції, але пістолети та дробовики — менше. Щоб привернути увагу, треба кричати; запах на цій дистанції не відчути.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(52,40,'en','Extreme Range','Only the longest range weapons, like smart rifles, can hit accurately at this distance. It takes more than one round to reach something here. Even if you hear a scream you might not know which direction it''s coming from.

More than 100m / 300ft.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(53,40,'ru','Крайняя Дистанция','Только оружие с максимальной дальностью, как умная винтовка, может точно поразить цель на этой дистанции. Добраться сюда займёт больше одного раунда. Даже услышав крик, вы можете не понять, откуда он доносится.

Более 100м / 300 футов.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(54,40,'ua','Крайня Дистанція','Лише зброя з максимальною дальністю, як розумна гвинтівка, може точно вразити ціль на цій дистанції. Дістатися сюди займе більше одного раунду. Навіть почувши крик, ви можете не зрозуміти, звідки він лунає.

Більше 100м / 300 футів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(55,1,'en','Ammo','Per magazine/container.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(56,1,'ru','Патроны','За магазин/контейнер.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(57,1,'ua','Набої','За магазин/контейнер.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(58,2,'en','Boarding Axe',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(59,2,'ru','Абордажный Топор',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(60,2,'ua','Абордажна Сокира',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(61,3,'en','Combat Shotgun','1d10 DMG at Long Range or greater.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(62,3,'ru','Боевой Дробовик','1d10 урона на Дальней дистанции и дальше.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(63,3,'ua','Бойовий Дробовик','1d10 шкоди на Далекій дистанції і далі.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(64,4,'en','Crowbar','Grants [+] on Strength Checks to open jammed airlocks, lift heavy objects, etc.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(65,4,'ru','Монтировка','Даёт [+] на Проверки Силы для вскрытия заклинивших шлюзов, подъёма тяжёлых предметов и т.д.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(66,4,'ua','Монтажний Лом','Дає [+] на Перевірки Сили для відкривання заклинених шлюзів, підняття важких предметів тощо.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(67,5,'en','Flamethrower','Body Save [-] or be set on fire (2d10 DMG / round).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(68,5,'ru','Огнемёт','Спасбросок Тела [-] или загораетесь (2d10 урона / раунд).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(69,5,'ua','Вогнемет','Порятунок Тіла [-] або загоряєтеся (2d10 шкоди / раунд).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(70,6,'en','Flare Gun','High intensity flare visible day and night from Long Range.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(71,6,'ru','Сигнальный Пистолет','Яркая ракета, видимая днём и ночью на Дальней дистанции.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(72,6,'ua','Сигнальний Пістолет','Яскрава ракета, видима вдень і вночі на Далекій дистанції.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(73,7,'en','Foam Gun','Body Save or become stuck. Strength Check [-] to escape.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(74,7,'ru','Пеногаситель','Спасбросок Тела или застрять. Проверка Силы [-] для побега.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(75,7,'ua','Піногасник','Порятунок Тіла або застрягнути. Перевірка Сили [-] для втечі.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(76,8,'en','Frag Grenade','On a hit, damages all Adjacent to enemy.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(77,8,'ru','Осколочная Граната','При попадании наносит урон всем Рядом с противником.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(78,8,'ua','Осколкова Граната','При влученні завдає шкоди всім Поруч з ворогом.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(79,9,'en','General-Purpose Machine Gun','Two-handed. Heavy. Barrel can be maneuvered to fire around corners.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(80,9,'ru','Пулемёт Общего Назначения','Двуручное. Тяжёлое. Ствол можно повернуть для стрельбы из-за угла.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(81,9,'ua','Кулемет Загального Призначення','Дворучна. Важка. Ствол можна повернути для стрільби з-за кута.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(82,10,'en','Hand Welder','Can cut through airlock doors.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(83,10,'ru','Ручной Сварочник','Может прорезать двери шлюза.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(84,10,'ua','Ручний Зварювальник','Може прорізати двері шлюзу.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(85,11,'en','Laser Cutter','Two-handed. Heavy. 1 round recharge between shots.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(86,11,'ru','Лазерный Резак','Двуручное. Тяжёлое. 1 раунд перезарядки между выстрелами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(87,11,'ua','Лазерний Різак','Дворучний. Важкий. 1 раунд перезарядки між пострілами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(88,12,'en','Nail Gun',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(89,12,'ru','Гвоздезабивной Пистолет',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(90,12,'ua','Цвяховий Пістолет',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(91,13,'en','Pulse Rifle',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(92,13,'ru','Импульсная Винтовка',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(93,13,'ua','Імпульсна Гвинтівка',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(94,14,'en','Revolver',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(95,14,'ru','Револьвер',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(96,14,'ua','Револьвер',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(97,15,'en','Rigging Gun','100m micro-filament. Body Save or become entangled.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(98,15,'ru','Такелажный Пистолет','100м микрофиламент. Спасбросок Тела или запутаться.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(99,15,'ua','Такелажний Пістолет','100м мікрофіламент. Порятунок Тіла або заплутатися.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(100,16,'en','Scalpel',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(101,16,'ru','Скальпель',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(102,16,'ua','Скальпель',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(103,17,'en','Smart Rifle','[-] on Combat Check when fired at Close Range.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(104,17,'ru','Умная Винтовка','[-] на Проверку Боя при стрельбе на Ближней дистанции.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(105,17,'ua','Розумна Гвинтівка','[-] на Перевірку Бою при стрільбі на Близькій дистанції.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(106,18,'en','SMG','Can be fired one-handed.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(107,18,'ru','Пистолет-Пулемёт','Можно стрелять одной рукой.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(108,18,'ua','Пістолет-Кулемет','Можна стріляти однією рукою.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(109,19,'en','Stun Baton','Body Save or stunned 1 round.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(110,19,'ru','Электрошокер','Спасбросок Тела или оглушён 1 раунд.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(111,19,'ua','Електрошокер','Порятунок Тіла або приголомшений 1 раунд.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(112,20,'en','Tranq Pistol','If DMG dealt: enemy must Body Save or be unconscious 1d10 rounds.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(113,20,'ru','Транквилизаторный Пистолет','При нанесении урона: враг должен пройти Спасбросок Тела или потерять сознание на 1d10 раундов.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(114,20,'ua','Транквілізаторний Пістолет','При нанесенні шкоди: ворог має пройти Порятунок Тіла або втратити свідомість на 1d10 раундів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(115,21,'en','Unarmed',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(116,21,'ru','Безоружный Бой',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(117,21,'ua','Беззбройний Бій',NULL,NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(118,22,'en','Vibechete','When dealing a Wound, roll on BOTH the Bleeding AND Gore columns.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(119,22,'ru','Вибромачете','При нанесении Раны бросайте на ОБОИХ столбцах: Кровотечение И Расчленение.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(120,22,'ua','Вібромачете','При нанесенні Рани кидайте на ОБОХ стовпцях: Кровотеча І Масивний урон.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(121,41,'en','Standard Crew Attire','Basic clothing.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(122,41,'ru','Стандартная Одежда Экипажа','Базовая одежда.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(123,41,'ua','Стандартний Одяг Екіпажу','Базовий одяг.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(124,42,'en','Vaccsuit','Includes short-range comms, headlamp, and radiation shielding. Decompression within 1d5 rounds if punctured.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(125,42,'ru','Вакуумный Костюм','Включает ближнюю связь, фонарь и защиту от радиации. Разгерметизация за 1d5 раундов при пробитии.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(126,42,'ua','Вакуумний Костюм','Включає ближній зв''язок, ліхтар і захист від радіації. Розгерметизація за 1d5 раундів при пробитті.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(127,43,'en','Hazard Suit','Includes air filter, extreme heat/cold protection, hydration reclamation (1L of water lasts 4 days), short-range comms, headlamp, and radiation shielding.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(128,43,'ru','Защитный Костюм','Включает воздушный фильтр, защиту от экстремального жара/холода, рекуперацию влаги (1 л воды хватает на 4 дня), ближнюю связь, фонарь и защиту от радиации.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(129,43,'ua','Захисний Костюм','Включає повітряний фільтр, захист від екстремальних температур, рекуперацію вологи (1 л води вистачає на 4 дні), ближній зв''язок, ліхтар і захист від радіації.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(130,44,'en','Standard Battle Dress','Includes short-range comms.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(131,44,'ru','Стандартный Боевой Костюм','Включает ближнюю связь.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(132,44,'ua','Стандартний Бойовий Костюм','Включає ближній зв''язок.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(133,45,'en','Advanced Battle Dress','Includes short-range comms, body cam, headlamp, HUD, exoskeletal weave (Strength Checks [+]), and radiation shielding. Damage Reduction: 3.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(134,45,'ru','Улучшенный Боевой Костюм','Включает ближнюю связь, нагрудную камеру, фонарь, HUD, экзоскелетное плетение (Проверки Силы [+]) и защиту от радиации. Снижение урона: 3.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(135,45,'ua','Покращений Бойовий Костюм','Включає ближній зв''язок, нагрудну камеру, ліхтар, HUD, екзоскелетне плетіння (Перевірки Сили [+]) і захист від радіації. Зменшення шкоди: 3.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(136,46,'en','Character Creation','9 steps to build your character:

1. Roll 2d10+25 for each Stat: Strength, Speed, Intellect, Combat.
2. Roll 2d10+10 for each Save: Sanity, Fear, Body.
3. Select your Class and apply its Stat/Save adjustments.
4. Roll 1d10+10 for Maximum Health. Start at max with 0 Wounds.
5. Gain Stress — Current and Minimum both start at 2.
6. Note your class''s Trauma Response.
7. Note class skills and choose bonus skills.
8. Roll for Equipment Loadout (pg 7), Trinket (pg 8), and Patch (pg 9).
9. Write your name and pronouns. Mark zero above High Score.

Starting Credits: 2d10×10cr. (Forgo loadout for 2d10×100cr instead.)',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(137,46,'ru','Создание Персонажа','9 шагов создания персонажа:

1. Бросьте 2d10+25 для каждого Параметра: Сила, Скорость, Интеллект, Бой.
2. Бросьте 2d10+10 для каждого Спасброска: Рассудок, Страх, Тело.
3. Выберите Класс и примените изменения к Параметрам/Спасброскам.
4. Бросьте 1d10+10 для Максимального Здоровья. Начинайте с максимума и 0 Ранений.
5. Получите Стресс — Текущий и Минимальный начинаются с 2.
6. Запишите Реакцию на Травму своего класса.
7. Запишите навыки класса и выберите бонусные навыки.
8. Бросьте на Снаряжение (стр. 7), Безделушку (стр. 8) и Нашивку (стр. 9).
9. Запишите имя и местоимения. Отметьте ноль над Рекордом.

Начальные Кредиты: 2d10×10кр. (Или откажитесь от снаряжения для 2d10×100кр.)',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(138,46,'ua','Створення Персонажа','9 кроків створення персонажа:

1. Киньте 2d10+25 для кожного Параметра: Сила, Швидкість, Інтелект, Бій.
2. Киньте 2d10+10 для кожного Порятунку: Розум, Страх, Тіло.
3. Оберіть Клас та застосуйте зміни до Параметрів/Порятунків.
4. Киньте 1d10+10 для Максимального Здоров''я. Починайте з максимуму і 0 Поранень.
5. Отримайте Стрес — Поточний і Мінімальний починаються з 2.
6. Запишіть Реакцію на Травму свого класу.
7. Запишіть навички класу та оберіть бонусні навички.
8. Киньте на Спорядження (стор. 7), Дрібничку (стор. 8) та Нашивку (стор. 9).
9. Запишіть ім''я та займенники. Відмітьте нуль над Рекордом.

Початкові Кредити: 2d10×10кр. (Або відмовтеся від спорядження для 2d10×100кр.)',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(139,47,'en','Marine','Handy in a fight, but whenever they Panic it may cause problems for the rest of the crew.

Trauma Response: Whenever you Panic, every Close friendly player must make a Fear Save.

Starting skills: Military Training, Athletics
Bonus: 1 Expert Skill OR 2 Trained Skills',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(140,47,'ru','Морской Пехотинец','Умелый боец, но когда они Паникуют, это может создать проблемы для всего экипажа.

Реакция на Травму: Когда вы Паникуете, каждый ближайший дружественный игрок обязан совершить Спасбросок Страха.

Начальные навыки: Военная Подготовка, Атлетика
Бонус: 1 Экспертный Навык ИЛИ 2 Начальных Навыка',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(141,47,'ua','Морський Піхотинець','Умілий у бою, але коли вони Панікують, це може створити проблеми для решти екіпажу.

Реакція на Травму: Коли ви Панікуєте, кожен близький дружній гравець зобов''язаний зробити Порятунок від Страху.

Початкові навички: Військова Підготовка, Атлетика
Бонус: 1 Експертний Навик АБО 2 Початкових Навики',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(142,48,'en','Android','A terrifying and exciting addition to any crew. They tend to unnerve other crewmembers with their cold inhumanity.

Trauma Response: Fear Saves made by Close friendly players are at Disadvantage.

Starting skills: Linguistics, Computers, Mathematics
Bonus: 1 Expert Skill OR 2 Trained Skills',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(143,48,'ru','Андроид','Пугающее и захватывающее дополнение к любому экипажу. Своей холодной бесчеловечностью они вызывают дискомфорт у других членов экипажа.

Реакция на Травму: Спасброски Страха ближайших дружественных игроков совершаются с Помехой.

Начальные навыки: Лингвистика, Компьютеры, Математика
Бонус: 1 Экспертный Навык ИЛИ 2 Начальных Навыка',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(144,48,'ua','Андроїд','Лякаюче й захопливе доповнення до будь-якого екіпажу. Своєю холодною нелюдяністю вони викликають дискомфорт у інших членів екіпажу.

Реакція на Травму: Порятунки від Страху близьких дружніх гравців здійснюються з Перешкодою.

Початкові навички: Лінгвістика, Комп''ютери, Математика
Бонус: 1 Експертний Навик АБО 2 Початкових Навики',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(145,49,'en','Scientist','Doctors, researchers, or anyone who wants to slice open creatures (or infected crewmembers) with a scalpel.

Trauma Response: Whenever you fail a Sanity Save, all Close friendly players gain 1 Stress.

Starting skills: 1 Master Skill, plus its Expert and Trained prerequisites
Bonus: 1 Trained Skill',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(146,49,'ru','Учёный','Врачи, исследователи или все, кто хочет вскрывать скальпелем существ (или заражённых членов экипажа).

Реакция на Травму: Когда вы проваливаете Спасбросок Рассудка, все ближайшие дружественные игроки получают 1 Стресс.

Начальные навыки: 1 Мастерский Навык, плюс необходимые Экспертный и Начальный
Бонус: 1 Начальный Навык',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(147,49,'ua','Вчений','Лікарі, дослідники або всі, хто хоче розрізати скальпелем істот (або заражених членів екіпажу).

Реакція на Травму: Коли ви провалюєте Порятунок Розуму, всі близькі дружні гравці отримують 1 Стрес.

Початкові навички: 1 Майстерний Навик, плюс необхідні Експертний і Початковий
Бонус: 1 Початковий Навик',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(148,50,'en','Teamster','Rough and tumble blue-collar space workers: mechanics, engineers, miners, and pilots.

Trauma Response: Once per session, you may take Advantage on a Panic Check.

Starting skills: Industrial Equipment, Zero-G
Bonus: 1 Trained Skill and 1 Expert Skill',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(149,50,'ru','Рабочий','Грубоватые синие воротнички: механики, инженеры, шахтёры и пилоты.

Реакция на Травму: Один раз за сессию вы можете совершить Проверку Паники с Преимуществом.

Начальные навыки: Промышленное Оборудование, Невесомость
Бонус: 1 Начальный Навык и 1 Экспертный Навык',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(150,50,'ua','Робітник','Грубуваті робітники: механіки, інженери, шахтарі та пілоти.

Реакція на Травму: Один раз за сесію ви можете здійснити Перевірку Паніки з Перевагою.

Початкові навички: Промислове Обладнання, Невагомість
Бонус: 1 Початковий Навик і 1 Експертний Навик',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(151,51,'en','Marine Loadout','Roll 1d10 to determine your starting gear.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(152,51,'ru','Снаряжение Морпеха','Бросьте 1d10 для определения начального снаряжения.',NULL,'["Майка и Камуфляжные Штаны (AP 1), Боевой Нож (как Скальпель УРО [+]), Стимпак (×5)", "Продвинутый Боевой Костюм (AP 10), Огнемёт (4 выстрела), Абордажный Топор", "Стандартный Боевой Костюм (AP 7), Боевой Дробовик (4 патрона), Рюкзак, Походное Снаряжение", "Стандартный Боевой Костюм (AP 7), Импульсная Винтовка (3 магазина), Инфракрасные Очки", "Стандартный Боевой Костюм (AP 7), Умная Винтовка (3 магазина), Бинокль, Личный Локатор", "Стандартный Боевой Костюм (AP 7), Пистолет-Пулемёт (3 магазина), Сухой Паёк (×7)", "Камуфляж (AP 2), Боевой Дробовик (2 патрона), Собака (питомец), Поводок, Теннисный Мяч", "Камуфляж (AP 2), Револьвер (12 патронов), Осколочная Граната", "Парадная Форма (AP 1), Револьвер (1 патрон), Монета Доблести", "Продвинутый Боевой Костюм (AP 10), Ручной Пулемёт (1 лента), Дисплей Данных"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(153,51,'ua','Спорядження Морського Піхотинця','Киньте 1d10 для визначення початкового спорядження.',NULL,'["Майка та Камуфляжні Штани (AP 1), Бойовий Ніж (як Скальпель ШКО [+]), Стимпак (×5)", "Вдосконалений Бойовий Костюм (AP 10), Вогнемет (4 постріли), Абордажна Сокира", "Стандартний Бойовий Костюм (AP 7), Бойовий Дробовик (4 патрони), Рюкзак, Похідне Спорядження", "Стандартний Бойовий Костюм (AP 7), Імпульсна Гвинтівка (3 магазини), Інфрачервоні Окуляри", "Стандартний Бойовий Костюм (AP 7), Розумна Гвинтівка (3 магазини), Бінокль, Особистий Локатор", "Стандартний Бойовий Костюм (AP 7), Пістолет-Кулемет (3 магазини), Бойовий Паєк (×7)", "Камуфляж (AP 2), Бойовий Дробовик (2 патрони), Собака (улюбленець), Повідок, Тенісний М''яч", "Камуфляж (AP 2), Револьвер (12 патронів), Осколкова Граната", "Парадна Форма (AP 1), Револьвер (1 патрон), Монета Доблесті", "Вдосконалений Бойовий Костюм (AP 10), Кулемет Загального Призначення (1 стрічка), Дисплей Даних"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(154,52,'en','Android Loadout','Roll 1d10 to determine your starting gear.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(155,52,'ru','Снаряжение Андроида','Бросьте 1d10 для определения начального снаряжения.',NULL,'["Вакуумный Скафандр (AP 3), Умная Винтовка (2 магазина), Инфракрасные Очки, Фольгированное Одеяло", "Вакуумный Скафандр (AP 3), Револьвер (12 патронов), Дальняя Связь, Сумка", "Защитный Костюм (AP 5), Револьвер (6 патронов), Дефибриллятор, Аптечка, Фонарик", "Защитный Костюм (AP 5), Пенный Пистолет (2 заряда), Набор для Сбора Образцов, Отвёртка (как Ассорти Инструментов)", "Стандартный Боевой Костюм (AP 7), Пистолет-Транквилизатор (3 выстрела), Паракорд (100м)", "Стандартная Форма Экипажа (AP 1), Электрошоковая Дубинка, Небольшой Питомец (органический)", "Стандартная Форма Экипажа (AP 1), Скальпель, Биосканер", "Стандартная Форма Экипажа (AP 1), Осколочная Граната, Перочинный Нож", "Одежда от Производителя (AP 1), Билет Jump-9 (пункт назначения не указан)", "Корпоративный Наряд (AP 1), VIP-Корпоративная Ключ-Карта"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(156,52,'ua','Спорядження Андроїда','Киньте 1d10 для визначення початкового спорядження.',NULL,'["Вакуумний Скафандр (AP 3), Розумна Гвинтівка (2 магазини), Інфрачервоні Окуляри, Фольгована Ковдра", "Вакуумний Скафандр (AP 3), Револьвер (12 патронів), Далекозв''язок, Сумка", "Захисний Костюм (AP 5), Револьвер (6 патронів), Дефібрилятор, Аптечка, Ліхтарик", "Захисний Костюм (AP 5), Пінний Пістолет (2 заряди), Набір для Збору Зразків, Викрутка (як Різні Інструменти)", "Стандартний Бойовий Костюм (AP 7), Пістолет-Транквілізатор (3 постріли), Паракорд (100м)", "Стандартна Форма Екіпажу (AP 1), Електрошокова Дубинка, Невеликий Улюбленець (органічний)", "Стандартна Форма Екіпажу (AP 1), Скальпель, Біосканер", "Стандартна Форма Екіпажу (AP 1), Осколкова Граната, Перочинний Ніж", "Одяг від Виробника (AP 1), Квиток Jump-9 (пункт призначення не вказано)", "Корпоративний Одяг (AP 1), VIP-Корпоративна Ключ-Карта"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(157,53,'en','Scientist Loadout','Roll 1d10 to determine your starting gear.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(158,53,'ru','Снаряжение Учёного','Бросьте 1d10 для определения начального снаряжения.',NULL,'["Защитный Костюм (AP 5), Пистолет-Транквилизатор (3 выстрела), Биосканер, Набор для Сбора Образцов", "Защитный Костюм (AP 5), Огнемёт (1 заряд), Стимпак, Электронный Набор Инструментов", "Вакуумный Скафандр (AP 3), Буровая Пушка, Набор для Сбора Образцов, Фонарик, Лабораторная Крыса (питомец)", "Вакуумный Скафандр (AP 3), Пенный Пистолет (2 заряда), Складные Носилки, Аптечка, Таблетки от Радиации (×5)", "Лабораторный Халат (AP 1), Отвёртка (как Ассорти Инструментов), Медсканер, Вакцина (1 доза)", "Лабораторный Халат (AP 1), Диагностический Сканер Кибернетики, Портативный Компьютерный Терминал", "Медицинский Халат (AP 1), Скальпель, Автомед (×5), Кислородный Баллон с Маской-Фильтром", "Медицинский Халат (AP 1), Флакон с Кислотой, Фольгированное Одеяло, Аптечка", "Стандартная Форма Экипажа (AP 1), Универсальный Нож (как Скальпель), Диагностический Сканер Кибернетики, Скотч", "Повседневная Одежда (AP 1), Портфель, Бланк Рецепта, Перьевая Ручка (Инжектор Яда)"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(159,53,'ua','Спорядження Вченого','Киньте 1d10 для визначення початкового спорядження.',NULL,'["Захисний Костюм (AP 5), Пістолет-Транквілізатор (3 постріли), Біосканер, Набір для Збору Зразків", "Захисний Костюм (AP 5), Вогнемет (1 заряд), Стимпак, Електронний Набір Інструментів", "Вакуумний Скафандр (AP 3), Бурова Пушка, Набір для Збору Зразків, Ліхтарик, Лабораторний Щур (улюбленець)", "Вакуумний Скафандр (AP 3), Пінний Пістолет (2 заряди), Складні Ноші, Аптечка, Таблетки від Радіації (×5)", "Лабораторний Халат (AP 1), Викрутка (як Різні Інструменти), Медсканер, Вакцина (1 доза)", "Лабораторний Халат (AP 1), Діагностичний Сканер Кібернетики, Портативний Комп''ютерний Термінал", "Медичний Халат (AP 1), Скальпель, Автомед (×5), Кисневий Балон з Маскою-Фільтром", "Медичний Халат (AP 1), Флакон з Кислотою, Фольгована Ковдра, Аптечка", "Стандартна Форма Екіпажу (AP 1), Універсальний Ніж (як Скальпель), Діагностичний Сканер Кібернетики, Скотч", "Повсякденний Одяг (AP 1), Портфель, Бланк Рецепту, Пір''яна Ручка (Ін''єктор Отрути)"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(160,54,'en','Teamster Loadout','Roll 1d10 to determine your starting gear.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(161,54,'ru','Снаряжение Рабочего','Бросьте 1d10 для определения начального снаряжения.',NULL,'["Вакуумный Скафандр (AP 3), Лазерный Резак (1 запасная батарея), Ремкомплект (×3), Пояс с Ассорти Инструментов", "Вакуумный Скафандр (AP 3), Револьвер (6 патронов), Монтировка, Фонарик", "Вакуумный Скафандр (AP 3), Буровая Пушка (1 выстрел), Лопата, Дрон-Мусорщик", "Защитный Костюм (AP 5), Вибромачете, Разводной Ключ, Походное Снаряжение, Фильтр Воды", "Рабочая Одежда Повышенной Прочности (AP 2), Взрывчатка и Детонатор, Сигареты", "Рабочая Одежда Повышенной Прочности (AP 2), Дрель (как Ассорти Инструментов), Паракорд (100м), Дрон-Мусорщик", "Стандартная Форма Экипажа (AP 1), Боевой Дробовик (4 патрона), Удлинитель (20м), Кот (питомец)", "Стандартная Форма Экипажа (AP 1), Гвоздемёт (32 патрона), Налобный Фонарь, Пояс с Ассорти Инструментов, Ланч-Бокс", "Стандартная Форма Экипажа (AP 1), Ракетница (2 патрона), Фильтр Воды, Личный Локатор, Подземный Сканер", "Домашняя Одежда (AP 1), Монтировка, Стимпак, Упаковка Пива (6 штук)"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(162,54,'ua','Спорядження Робітника','Киньте 1d10 для визначення початкового спорядження.',NULL,'["Вакуумний Скафандр (AP 3), Лазерний Різак (1 запасна батарея), Ремкомплект (×3), Пояс з Різними Інструментами", "Вакуумний Скафандр (AP 3), Револьвер (6 патронів), Монтировка, Ліхтарик", "Вакуумний Скафандр (AP 3), Бурова Пушка (1 постріл), Лопата, Дрон-Збирач", "Захисний Костюм (AP 5), Вібромачете, Розвідний Ключ, Похідне Спорядження, Фільтр Води", "Робочий Одяг Підвищеної Міцності (AP 2), Вибухівка та Детонатор, Сигарети", "Робочий Одяг Підвищеної Міцності (AP 2), Дриль (як Різні Інструменти), Паракорд (100м), Дрон-Збирач", "Стандартна Форма Екіпажу (AP 1), Бойовий Дробовик (4 патрони), Подовжувач (20м), Кіт (улюбленець)", "Стандартна Форма Екіпажу (AP 1), Цвяхострільник (32 патрони), Налобний Ліхтар, Пояс з Різними Інструментами, Ланч-Бокс", "Стандартна Форма Екіпажу (AP 1), Ракетниця (2 патрони), Фільтр Води, Особистий Локатор, Підземний Сканер", "Домашній Одяг (AP 1), Монтировка, Стимпак, Упаковка Пива (6 штук)"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(163,55,'en','Trinkets','Roll 1d100 during character creation. May it bring you good luck out there in the void.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(164,55,'ru','Безделушки','Бросьте 1d100 при создании персонажа. Пусть принесёт вам удачу в пустоте.',NULL,'["Руководство: ПАНИКА: Предвестник Катастрофы", "Антикварный Корпоративный Скрип (Астероидная Шахта)", "Руководство: ВЫЖИВАНИЕ: Ешь Суп Ножом", "Иссохшая Кукла-Шелуха", "Прессованный Инопланетный Цветок (обычный)", "Ожерелье из Гильз", "Разъеденное Логическое Ядро Андроида", "Памфлет: Признаки Паразитарной Инфекции", "Руководство: Обращайся с Винтовкой Как с Дамой", "Костяной Нож", "Календарь: Инопланетный Пин-Ап", "Отклонённое Заявление (Колониальный Корабль)", "Голографическая Танцовщица-Змея", "Змеиный Виски", "Медицинский Контейнер, Фиолетовый Порошок", "Таблетки: Для Мужской Силы, Паршивые", "Казино Игральные Карты", "Лапка Зайцеобразного", "Кольцо с Лунным Камнем", "Руководство: Безопасность в Шахтах и Вы", "Памфлет: Против Человеческих Симулякров", "Череп Животного, 3 Глаза, Загнутые Рога", "Сертификат Бармена (Просроченный)", "Кукла Бунраку", "Кружка Геолога, Помятая", "Жуткая Маска", "Ультрачёрный Мрамор", "Кости из Слоновой Кости", "Карты Таро, Потёртые, Позолоченные Пиритом Края", "Мешочек Разнородных Зубов", "Прах (Родственник)", "Ожерелье-Маяк DNR (Не Реанимировать)", "Сигареты (Ухмыляющийся Череп)", "Таблетки: Орех Арека", "Кулон: Осколки Снаряда в Пластике", "Памфлет: Дзен и Искусство Упаковки Грузов", "Пара Рюмок (Стреляные Гильзы Дробовика)", "Ключ (Дом Детства)", "Жетон (Фамильная Реликвия)", "Жетон: «Ваш боевой дух растёт?»", "Памфлет: Реликвия из Плоти", "Памфлет: Равнодушные Звёзды", "Календарь: Военные Сражения", "Руководство: Богатый Капитан, Бедный Капитан", "Агитационный Плакат (Родная Планета)", "Законсервированная Насекомообразная Аберрация", "Титановая Зубочистка", "Перчатки, Кожаные (Шкура Ксеноморфа)", "Похабщина (Подрывная): Капитан по Уставу", "Полотенце, Немного Потрёпанное", "Кастет", "Пушистые Наручники", "Журнал Обид", "Стилизованный Портсигар", "Моток Проволоки Разного Сечения", "Гаечный Ключ", "Выкидной Нож, Декоративный", "Порошок из Рога Ксеноморфа", "Бонсай в Горшке", "Клюшка для Гольфа (Паттер)", "Окаменелость Трилобита", "Памфлет: Любовница в Каждом Порту", "Залатанный Комбинезон, Персонализированный", "Мясистая Штука в Мутной Банке", "Шипованный Браслет", "Губная Гармошка", "Порнографические Картинки, Затрёпанные", "Кофейная Кружка, Сколотая, надпись: СЧАСТЬЕ ОБЯЗАТЕЛЬНО", "Руководство: Самогоноварение на Оружейном Масле и Топливе", "Миниатюрные Шахматы, Костяные, Фигуры Потеряны", "Гироскоп, Погнутый, Жестяной", "Выцветшая Зелёная Покерная Фишка", "Укулеле", "Аэрозольная Краска", "Постер «Разыскивается», Выцветший", "Медальон, Прядь Волос", "Скульптура Крысы (Золото)", "Одеяло, Огнеупорное", "Анорак с Капюшоном, Флисовая Подкладка", "Пистолет-Пулька", "Кремнёвый Топорик", "Кулон: Два Астронавта в форме Черепа", "Кубик Рубика", "Мячик-Антистресс, надпись: Ноль Стресса в Невесомости", "Значок Спутника", "Ушанка", "Кепка Дальнобойщика, Сетчатая, с Серым Инопланетянином", "Ментоловый Бальзам", "Тропический Шлем", "Брезент 10м × 10м", "И-Цзин, Палочки Потеряны", "Кукри", "Сапёрная Лопата", "Заточка из Столового Ножа", "Набитое Чучело Кошки", "Памфлет: Толкование Снов Овец", "Выцветшая Фотография, Продуваемая Ветром Пустошь", "Театральный Бинокль", "Памфлет: Повелители Андроиды", "Межзвёздный Компас, Всегда Указывает на Родину"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(165,55,'ua','Дрібнички','Киньте 1d100 при створенні персонажа. Хай принесе вам удачу у порожнечі.',NULL,'["Посібник: ПАНІКА: Провісник Катастрофи", "Антикварний Корпоративний Скрип (Астероїдна Шахта)", "Посібник: ВИЖИВАННЯ: Їж Суп Ножем", "Висушена Лялька-Лушпиння", "Пресована Інопланетна Квітка (звичайна)", "Намисто з Гільз", "Роз''їджене Логічне Ядро Андроїда", "Памфлет: Ознаки Паразитарної Інфекції", "Посібник: Поводься з Гвинтівкою Як з Дамою", "Кістяний Ніж", "Календар: Інопланетний Пін-Ап", "Відхилена Заявка (Колоніальний Корабель)", "Голографічна Танцівниця-Змія", "Зміїний Віскі", "Медичний Контейнер, Фіолетовий Порошок", "Таблетки: Для Чоловічої Сили, Паршиві", "Казино Ігральні Карти", "Лапка Зайцеподібного", "Кільце з Місячним Каменем", "Посібник: Безпека у Шахтах та Ви", "Памфлет: Проти Людських Симулякрів", "Череп Тварини, 3 Ока, Загнуті Роги", "Сертифікат Бармена (Прострочений)", "Лялька Бунраку", "Кружка Геолога, М''ята", "Моторошна Маска", "Ультрачорний Мармур", "Кості зі Слонової Кістки", "Карти Таро, Затерті, Позолочені Пиритом Краї", "Мішечок Різнорідних Зубів", "Прах (Родич)", "Намисто-Маяк DNR (Не Реанімувати)", "Сигарети (Гримасуючий Череп)", "Таблетки: Горіх Арека", "Кулон: Осколки Снаряда у Пластику", "Памфлет: Дзен та Мистецтво Укладання Вантажу", "Пара Чарок (Стріляні Гільзи Дробовика)", "Ключ (Дитячий Дім)", "Жетон (Сімейна Реліквія)", "Жетон: «Ваш бойовий дух зростає?»", "Памфлет: Реліквія з Плоті", "Памфлет: Байдужі Зорі", "Календар: Військові Битви", "Посібник: Багатий Капітан, Бідний Капітан", "Агітаційний Плакат (Рідна Планета)", "Законсервована Комахоподібна Аберація", "Титанова Зубочистка", "Рукавички, Шкіряні (Шкіра Ксеноморфа)", "Похабщина (Підривна): Капітан за Статутом", "Рушник, Трохи Потертий", "Кастет", "Пухнасті Наручники", "Журнал Образ", "Стилізований Портсигар", "Моток Дроту Різного Перерізу", "Гайковий Ключ", "Викидний Ніж, Декоративний", "Порошок з Рогу Ксеноморфа", "Бонсай у Горщику", "Ключка для Гольфу (Патер)", "Скам''янілість Трилобіта", "Памфлет: Коханка в Кожному Порту", "Залатаний Комбінезон, Персоналізований", "М''ясиста Штука в Каламутній Банці", "Шипований Браслет", "Губна Гармошка", "Порнографічні Картинки, Затерті", "Кавова Кружка, Відколена, напис: ЩАСТЯ ОБО''ВЯЗКОВЕ", "Посібник: Самогоноваріння на Зброярській Олії та Паливі", "Мініатюрні Шахи, Кістяні, Фігури Загублені", "Гіроскоп, Погнутий, Бляшаний", "Вицвіла Зелена Покерна Фішка", "Укулеле", "Аерозольна Фарба", "Постер «Розшукується», Вицвілий", "Медальйон, Прядка Волосся", "Скульптура Щура (Золото)", "Ковдра, Вогнестійка", "Куртка з Капюшоном, Флісова Підкладка", "Пістолет-Кулька", "Кременевий Сокирка", "Кулон: Два Астронавти у формі Черепа", "Кубик Рубіка", "М''ячик-Антистрес, напис: Нуль Стресу в Невагомості", "Значок Супутника", "Вушанка", "Кепка Далекобійника, Сітчаста, із Сірим Інопланетянином", "Ментоловий Бальзам", "Тропічний Шолом", "Брезент 10м × 10м", "І-Цзин, Паличок Немає", "Кукрі", "Сапёрна Лопатка", "Заточка з Столового Ножа", "Опудало Кішки", "Памфлет: Тлумачення Снів Овець", "Вицвіла Фотографія, Продувана Вітром Пустка", "Театральний Бінокль", "Памфлет: Повелителі Андроїди", "Міжзоряний Компас, Завжди Вказує на Батьківщину"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(166,56,'en','Patches','Roll 1d100 during character creation. Sewn on your clothing or gear.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(167,56,'ru','Нашивки','Бросьте 1d100 при создании персонажа. Нашивка на одежде или снаряжении.',NULL,'["«Я Не Ракетный Учёный / Но Ты Идиот»", "Нашивка Медика (Череп и Кости над Крестом)", "«Не Беги — Умрёшь Уставшим» Нашивка на Спину", "Логотип «Красная Рубашка»", "Группа Крови (Справочная Нашивка)", "«Я ВЫГЛЯЖУ Как Эксперт?»", "Символ Биологической Опасности", "Мистер Гадость", "Символ Ядерной Опасности", "«Ешь Богатых»", "«Будь Уверен: Контрольный Выстрел»", "Эмодзи Огня", "Смайлик (Светится в Темноте)", "«Улыбайся: Большой Брат Следит»", "Весёлый Роджер", "Череп Викинга", "«ВЕРХОВНЫЙ ХИЩНИК» (Череп Саблезуба)", "Пин-Ап (Туз Пик)", "Дама Червей", "Охранник", "«ОДИНОЧКА»", "«Лицом к Врагу» (Мина Клеймор)", "Пин-Ап (Верхом на Ракете)", "FUBAR (Полный Абзац)", "«Я (Любовная) Машина»", "Пин-Ап (Механик)", "«ПРИВЕТ МОЁ ИМЯ:»", "«Работает на Кофе»", "«Отведи Меня к Своему Лидеру» (НЛО)", "«ДЕЛАЙ СВОЁ ДЕЛО»", "«Возьми Мою Жизнь (Пожалуйста)»", "«Законопослушный Гражданин»", "«Аллергия на Чушь» (Медицинская Нашивка)", "«Почините Меня Первым» (Кадуцей)", "«Люблю Чистые Инструменты / И Грязных Любовников»", "«Чем Громче Кричишь — Тем Быстрее Приду» (Медсестра Пин-Ап)", "HMFIC (Главный Тут)", "Голубь в Прицеле", "Чиби Ктулху", "«Добро Пожаловать в ОПАСНУЮ ЗОНУ»", "Череп и Скрещённые Ключи", "Пин-Ап (Суккуб)", "«МНЕ ПОХЕР?» (DILLIGAF)", "«ПИТЬ / ДРАТЬСЯ / ТРАХАТЬСЯ»", "«Работай Усердно / Отдыхай Ещё Усерднее»", "Девушка с Брызговика", "Счётчик Веселья (показывает: Плохо)", "«ИГРА ОКОНЧЕНА» (Жених и Невеста)", "Сердце", "«СОВЕРШЕНСТВУЙСЯ / АДАПТИРУЙСЯ / ПРЕОДОЛЕВАЙ»", "«ТЕРПИ»", "«Будь Ковбоем» (Скрещённые Револьверы)", "«Устранитель Проблем»", "Логотип NASA", "Скрещённые Молоты с Крыльями", "«Держи Хорошо Смазанным»", "Советский Серп и Молот", "«Хорошо Ладит с Другими»", "«Живи Свободно и Умри»", "«ЕСЛИ Я БЕГУ — НЕ ОТСТАВАЙ» Нашивка на Спину", "«Мешок с Мясом»", "«Я Не Робот»", "Красная Шестерня", "«Тупость Не Починишь»", "«Космос — МОЙ ДОМ» (Грустный Астронавт)", "Всевидящее Oko", "«Solve Et Coagula» (Бафомет)", "«Всё, Терпение Кончилось» (Астронавт с Вывернутыми Карманами)", "«Путешествуй в Дальние Края / Встречай Необычных Существ / Быть Съеденным»", "BOHICA (Нагнись, Снова Прилетает)", "«Я Хранитель Брата Своего»", "«Мама Старалась»", "Паук Чёрная Вдова", "«На Чём Я Ещё Езжу — Женился на Тебе»", "«Один Размер Для Всех» (Граната)", "Нашивка на Спину «Мрачный Жнец»", "отъебись", "«Гладкий Оператор»", "Символ Атома", "«Во Имя Науки!»", "«Вообще-то, Я ИМЕННО Ракетный Учёный»", "«Требуется Помощь»", "Принцесса", "«КОЧЕВНИК»", "«ХОРОШИЙ»", "Кубики (Змеиные Глаза)", "«Работник №1»", "«Хорошо» (Мозг)", "«Крутая Сука»", "«Слишком Красив(а), Чтобы Умереть»", "«Трахайся Вечно» (Розы)", "Икар", "«Лучший Друг Девушки» (Бриллиант)", "Символ Риска Поражения Током", "Перевёрнутый Крест", "«Ты Подписываешь Мои Чеки?» Нашивка на Спину", "«Я ♥ Себя»", "Двойная Вишня", "«Доброволец»", "Покерная Рука: Рука Мёртвого (Тузы и Восьмёрки)"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(168,56,'ua','Нашивки','Киньте 1d100 при створенні персонажа. Нашивка на одязі або спорядженні.',NULL,'["«Я Не Ракетний Вчений / Але Ти Ідіот»", "Нашивка Медика (Череп і Кістки над Хрестом)", "«Не Бігай — Помреш Стомленим» Нашивка на Спину", "Логотип «Червона Сорочка»", "Група Крові (Довідкова Нашивка)", "«Я ВИГЛЯДАЮ Як Експерт?»", "Символ Біологічної Небезпеки", "Містер Гидота", "Символ Ядерної Небезпеки", "«Їж Багатих»", "«Будь Впевнений: Контрольний Постріл»", "Емодзі Вогню", "Смайлик (Світиться в Темряві)", "«Усміхайся: Великий Брат Стежить»", "Веселий Роджер", "Череп Вікінга", "«ВЕРХОВНИЙ ХИЖАК» (Череп Шаблезуба)", "Пін-Ап (Туз Пік)", "Дама Черв", "Охоронець", "«САМІТНИК»", "«Обличчям до Ворога» (Міна Клеймор)", "Пін-Ап (Верхи на Ракеті)", "FUBAR (Повний Капець)", "«Я (Любовна) Машина»", "Пін-Ап (Механік)", "«ПРИВІТ МОЄ ІМ''Я:»", "«Працює на Каві»", "«Відведи Мене до Свого Лідера» (НЛО)", "«РОБИ СВОЄ ДІЛО»", "«Візьми Моє Життя (Будь Ласка)»", "«Законослухняний Громадянин»", "«Алергія на Нісенітниці» (Медична Нашивка)", "«Полагодьте Мене Першим» (Кадуцей)", "«Люблю Чисті Інструменти / І Брудних Коханців»", "«Чим Голосніше Кричиш — Тим Швидше Прийду» (Медсестра Пін-Ап)", "HMFIC (Головний Тут)", "Голуб у Прицілі", "Чібі Ктулху", "«Ласкаво Просимо до НЕБЕЗПЕЧНОЇ ЗОНИ»", "Череп і Схрещені Ключі", "Пін-Ап (Суккуб)", "«МНІ ПОХЕР?» (DILLIGAF)", "«ПИТИ / БИТИСЯ / ТРАХАТИСЯ»", "«Працюй Наполегливо / Відпочивай Ще Наполегливіше»", "Дівчина з Бризковика", "Лічильник Веселощів (показує: Погано)", "«ГРА СКІНЧЕНА» (Наречений і Наречена)", "Серце", "«ВДОСКОНАЛЮЙСЯ / АДАПТУЙСЯ / ПОДОЛАЙ»", "«ТЕРПИ»", "«Будь Ковбоєм» (Схрещені Револьвери)", "«Вирішувач Проблем»", "Логотип NASA", "Схрещені Молоти з Крилами", "«Тримай Добре Змащеним»", "Радянський Серп і Молот", "«Добре Ладить з Іншими»", "«Живи Вільно і Помри»", "«ЯКЩО Я БІЖУ — НЕ ВІДСТАВАЙ» Нашивка на Спину", "«Мішок з М''ясом»", "«Я Не Робот»", "Червона Шестірня", "«Тупість Не Полагодиш»", "«Космос — МІЙ ДІМ» (Сумний Астронавт)", "Всевидяче Oko", "«Solve Et Coagula» (Бафомет)", "«Все, Терпіння Скінчилось» (Астронавт з Вивернутими Кишенями)", "«Подорожуй до Далеких Місць / Зустрічай Незвичайних Істот / Бути З''їденим»", "BOHICA (Нахились, Знову Летить)", "«Я Охоронець Брата Свого»", "«Мама Старалась»", "Павук Чорна Вдова", "«На Чому Я Ще Їжджу — Одружився з Тобою»", "«Один Розмір Для Всіх» (Граната)", "Нашивка на Спину «Похмурий Жнець»", "відчепись", "«Гладкий Оператор»", "Символ Атома", "«В Ім''я Науки!»", "«Взагалі-то, Я САМЕ Ракетний Вчений»", "«Потрібна Допомога»", "Принцеса", "«КОЧІВНИК»", "«ХОРОШИЙ»", "Кубики (Зміїні Очі)", "«Працівник №1»", "«Добре» (Мозок)", "«Крута Сука»", "«Занадто Гарний(а), Щоб Померти»", "«Трахайся Вічно» (Троянди)", "Ікар", "«Найкращий Друг Дівчини» (Діамант)", "Символ Ризику Ураження Струмом", "Перевернутий Хрест", "«Ти Підписуєш Мої Чеки?» Нашивка на Спину", "«Я ♥ Себе»", "Подвійна Вишня", "«Доброволець»", "Покерна Рука: Рука Мертвого (Тузи та Вісімки)"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(169,57,'en','Assorted Tools','Wrenches, spanners, screwdrivers, etc. Can be used as weapons in a pinch (1d5 DMG).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(170,57,'ru','Набор Инструментов','Гаечные ключи, разводные ключи, отвёртки и т.д. В крайнем случае можно использовать как оружие (1d5 урона).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(171,57,'ua','Набір Інструментів','Гайкові ключі, розвідні ключі, викрутки тощо. У крайньому випадку можна використовувати як зброю (1d5 шкоди).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(172,58,'en','Automed (x5)','Nanotech pills that assist your body in repairing Damage by granting Advantage to Body Saves meant to repel disease and poison, as well as attempts to heal from rest.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(173,58,'ru','Автомед (x5)','Нанотехнологические таблетки, помогающие телу восстанавливаться: дают Преимущество на Спасброски Тела против болезней и ядов, а также при попытках исцеления во время отдыха.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(174,58,'ua','Автомед (x5)','Нанотехнологічні таблетки, що допомагають тілу відновлюватися: дають Перевагу на Порятунки Тіла проти хвороб і отрут, а також при спробах відновлення під час відпочинку.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(175,59,'en','Battery (High Power)','Heavy duty battery for powering laser cutters, salvage drones, and other items. Recharges in 1 hour connected to power or 6 hours with solar power. Add waterproofing (+500cr).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(176,59,'ru','Аккумулятор (Мощный)','Мощный аккумулятор для лазерных резаков, дронов и другого оборудования. Заряжается за 1 час от сети или за 6 часов от солнечной энергии. Гидроизоляция (+500кр).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(177,59,'ua','Акумулятор (Потужний)','Потужний акумулятор для лазерних різаків, дронів та іншого обладнання. Заряджається за 1 годину від мережі або за 6 годин від сонячної енергії. Гідроізоляція (+500кр).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(178,60,'en','Binoculars','20x magnification. Add night vision (+300cr) or thermal vision (+1kcr).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(179,60,'ru','Бинокль','20-кратное увеличение. Добавить ночное зрение (+300кр) или тепловизор (+1ккр).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(180,60,'ua','Бінокль','20-кратне збільшення. Додати нічний зір (+300кр) або тепловізор (+1ккр).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(181,61,'en','Bioscanner','Long Range. Scans for signs of life, showing location but not what that life is. Blocked by some materials at the Warden''s discretion.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(182,61,'ru','Биосканер','Дальняя дистанция. Сканирует признаки жизни, показывая местоположение, но не тип. Блокируется некоторыми материалами на усмотрение Надзирателя.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(183,61,'ua','Біосканер','Далека дистанція. Сканує ознаки життя, показуючи місцезнаходження, але не тип. Блокується деякими матеріалами на розсуд Охоронця.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(184,62,'en','Body Cam','Worn on your clothing. Streams video back to a control center so crewmembers can see what you''re seeing. Add night vision (+300cr) or thermal vision (+1kcr).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(185,62,'ru','Нагрудная Камера','Носится на одежде. Транслирует видео на пункт управления. Добавить ночное зрение (+300кр) или тепловизор (+1ккр).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(186,62,'ua','Нагрудна Камера','Носиться на одязі. Транслює відео на пункт управління. Додати нічний зір (+300кр) або тепловізор (+1ккр).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(187,63,'en','Chemlight (x5)','Small disposable glowsticks. Dim illumination in a 1m radius.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(188,63,'ru','Химсвет (x5)','Маленькие одноразовые световые палочки. Слабое освещение в радиусе 1 метра.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(189,63,'ua','Хімсвітло (x5)','Маленькі одноразові світлові палиці. Слабке освітлення в радіусі 1 метра.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(190,64,'en','Cybernetic Diagnostic Scanner','Scans androids and other cybernetic organisms to diagnose physical or mental issues. Often distrusted by androids.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(191,64,'ru','Кибердиагностический Сканер','Сканирует андроидов и других киберорганизмов для диагностики физических или ментальных проблем. Андроиды часто относятся к нему с недоверием.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(192,64,'ua','Кібердіагностичний Сканер','Сканує андроїдів та інших кіберорганізмів для діагностики фізичних або ментальних проблем. Андроїди часто ставляться до нього з недовірою.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(193,65,'en','Electronic Tool Set','A full set of tools for detailed repair or construction work on electronics.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(194,65,'ru','Электронный Набор Инструментов','Полный набор инструментов для детального ремонта или сборки электроники.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(195,65,'ua','Електронний Набір Інструментів','Повний набір інструментів для детального ремонту або збирання електроніки.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(196,66,'en','Emergency Beacon','Sends up a flare and emits a loud beep every few seconds. Broadcasts a call on all radio channels to ships or vehicles in the area. Can be blocked by a radio jammer.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(197,66,'ru','Аварийный Маяк','Запускает сигнальную ракету и издаёт громкий сигнал каждые несколько секунд. Транслирует вызов на все радиоканалы. Может быть заблокирован радиопомехами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(198,66,'ua','Аварійний Маяк','Запускає сигнальну ракету і видає гучний сигнал кожні кілька секунд. Транслює виклик на всі радіоканали. Може бути заблокований радіоглушником.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(199,67,'en','Exoloader','Open-air mechanical exoskeleton for heavy lifting (up to 5000kg). Loader claws deal 1 Wound. User can only wear Standard Crew Attire or Standard Battle Dress while operating. Battery operated (48 hours).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(200,67,'ru','Экзозагрузчик','Открытый механический экзоскелет для подъёма тяжестей (до 5000 кг). Захваты наносят 1 Ранение. Оператор может носить только Стандартную Одежду или Стандартный Боевой Костюм. Работает от аккумулятора (48 часов).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(201,67,'ua','Екзозавантажувач','Відкритий механічний екзоскелет для підняття важких вантажів (до 5000 кг). Захвати завдають 1 Поранення. Оператор може носити лише Стандартний Одяг або Стандартний Бойовий Костюм. Працює від акумулятора (48 годин).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(202,68,'en','Explosives & Detonator','Explosive charge powerful enough to blow open an airlock. All organisms in Close Range must make a Body Save or take a Wound (Explosive). Detonator works at Long Range, but can be blocked by a radio jammer.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(203,68,'ru','Взрывчатка и Детонатор','Взрывной заряд, способный вскрыть шлюз. Все существа на Ближней дистанции должны пройти Спасбросок Тела или получить Ранение (Взрыв). Детонатор работает на Дальней дистанции, но может быть заблокирован радиопомехами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(204,68,'ua','Вибухівка та Детонатор','Вибуховий заряд, здатний відкрити шлюз. Усі істоти на Близькій дистанції мають пройти Порятунок Тіла або отримати Поранення (Вибух). Детонатор працює на Далекій дистанції, але може бути заблокований радіоглушником.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(205,69,'en','First Aid Kit','An assortment of dressings and treatments to help stop bleeding, bandage cuts, and treat other minor injuries.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(206,69,'ru','Аптечка','Набор перевязочных материалов и средств для остановки кровотечения, перевязки порезов и лечения других мелких травм.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(207,69,'ua','Аптечка','Набір перев''язувальних матеріалів і засобів для зупинки кровотечі, перев''язки порізів і лікування інших дрібних травм.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(208,70,'en','Flashlight','Handheld or shoulder mounted. Illuminates 10m ahead of the user.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(209,70,'ru','Фонарик','Ручной или крепится на плечо. Освещает 10 метров перед пользователем.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(210,70,'ua','Ліхтарик','Ручний або кріпиться на плече. Освітлює 10 метрів перед користувачем.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(211,71,'en','Foldable Stretcher','Portable stretcher that fits within a rucksack. Allows the user to safely strap down the patient and carry them to where their wounds can be better treated. Unfolds to roughly 2m.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(212,71,'ru','Складные Носилки','Переносные носилки, помещающиеся в рюкзак. Позволяют надёжно зафиксировать пациента и перенести его туда, где можно оказать более качественную помощь. Разворачиваются примерно до 2 метров.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(213,71,'ua','Складні Ноші','Переносні ноші, що поміщаються у рюкзак. Дозволяють надійно зафіксувати пацієнта і перенести його туди, де можна надати кращу допомогу. Розгортаються приблизно до 2 метрів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(214,72,'en','Geiger Counter','Detects radiation and displays radiation levels.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(215,72,'ru','Счётчик Гейгера','Обнаруживает радиацию и отображает уровень радиации.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(216,72,'ua','Лічильник Гейгера','Виявляє радіацію та відображає рівень радіації.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(217,73,'en','Heads-Up Display (HUD)','Often worn by marines. Allows the wearer to see through the body cams of others in their unit, and connect to any smart-link upgraded weapon.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(218,73,'ru','Нашлемный Дисплей','Часто используется морскими пехотинцами. Позволяет видеть через нагрудные камеры других бойцов и подключаться к оружию с умной привязкой.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(219,73,'ua','Нашоломний Дисплей','Часто використовується морськими піхотинцями. Дозволяє бачити через нагрудні камери інших бійців і підключатися до зброї з розумним зв''язком.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(220,74,'en','Infrared Goggles','Allows the wearer to see heat signatures, sometimes up to several hours old. Add night vision (+300cr).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(221,74,'ru','Инфракрасные Очки','Позволяют видеть тепловые следы, иногда до нескольких часов давности. Добавить ночное зрение (+300кр).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(222,74,'ua','Інфрачервоні Окуляри','Дозволяють бачити теплові сліди, іноді до кількох годин давності. Додати нічний зір (+300кр).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(223,75,'en','Jetpack','Fly up to 100m high at up to 100km/hr for 2 hours on a tank of fuel. Deals 1d100[+] DMG if destroyed. Fuel can be refilled for 200cr.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(224,75,'ru','Реактивный Ранец','Полёт до 100 м высоты со скоростью до 100 км/ч в течение 2 часов на баке топлива. При уничтожении наносит 1d100[+] урона. Заправка — 200кр.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(225,75,'ua','Реактивний Ранець','Політ до 100 м висоти зі швидкістю до 100 км/год протягом 2 годин на баку пального. При знищенні завдає 1d100[+] шкоди. Заправка — 200кр.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(226,76,'en','Lockpick Set','A highly advanced set of tools for hacking basic airlock and electronic door systems.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(227,76,'ru','Отмычки','Высокотехнологичный набор инструментов для взлома базовых систем шлюзов и электронных дверей.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(228,76,'ua','Відмички','Високотехнологічний набір інструментів для злому базових систем шлюзів та електронних дверей.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(229,77,'en','Long-range Comms','Rucksack-sized communication device for surface-to-ship communication.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(230,77,'ru','Дальнобойная Радиосвязь','Рюкзачное устройство связи для передачи сигнала с поверхности на корабль.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(231,77,'ua','Далекобійний Радіозв''язок','Рюкзачний пристрій зв''язку для передачі сигналу з поверхні на корабель.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(232,78,'en','Mag-boots','Grants a magnetic grip, allowing easy walking on ship exteriors (in space, docked, or free-floating), metal asteroids, or any magnetic surface.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(233,78,'ru','Магнитные Ботинки','Обеспечивают магнитное сцепление для ходьбы по внешней поверхности корабля (в космосе, пришвартованного или в свободном полёте), металлическим астероидам и другим магнитным поверхностям.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(234,78,'ua','Магнітні Черевики','Забезпечують магнітне зчеплення для ходьби по зовнішній поверхні корабля (у космосі, пришвартованого або у вільному польоті), металевим астероїдам та іншим магнітним поверхням.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(235,79,'en','Medscanner','Scans a living or dead body to analyze it for disease or abnormalities without biopsy or autopsy. Results may not be instantaneous and may require a lab for complete analysis.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(236,79,'ru','Медсканер','Сканирует живое или мёртвое тело для анализа на заболевания или аномалии без биопсии или аутопсии. Результаты могут быть не мгновенными и требовать лаборатории.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(237,79,'ua','Медсканер','Сканує живе або мертве тіло для аналізу на захворювання або аномалії без біопсії чи розтину. Результати можуть бути не миттєвими і вимагати лабораторії.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(238,80,'en','MoHab Unit','Tent, canteen, stove, rucksack, compass, and sleeping bag.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(239,80,'ru','Модуль Мобильного Жилья','Палатка, фляга, плита, рюкзак, компас и спальный мешок.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(240,80,'ua','Модуль Мобільного Житла','Палатка, фляга, плита, рюкзак, компас і спальний мішок.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(241,81,'en','MRE (x7)','"Meal, Ready-to-Eat." Self-contained field rations in lightweight packaging. Each provides sufficient sustenance for one person for one day (does not include water).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(242,81,'ru','Сухпаёк (x7)','«Готовый к употреблению паёк». Самодостаточный полевой рацион в лёгкой упаковке. Каждый обеспечивает одного человека питанием на один день (вода не включена).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(243,81,'ua','Сухпайок (x7)','«Готовий до вживання пайок». Самодостатній польовий раціон у легкій упаковці. Кожен забезпечує одну людину харчуванням на один день (вода не включена).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(244,82,'en','Mylar Blanket','Lightweight heat-reflective blanket. Often used for thermal regulation of patients suffering from extreme cold or other trauma.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(245,82,'ru','Термоодеяло','Лёгкое теплоотражающее одеяло. Часто используется для терморегуляции пациентов, страдающих от экстремального холода или других травм.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(246,82,'ua','Термоковдра','Легка теплоотбивна ковдра. Часто використовується для терморегуляції пацієнтів, що страждають від екстремального холоду або інших травм.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(247,83,'en','Oxygen Tank','When attached to a vaccsuit provides up to 12 hours of oxygen under normal circumstances, 4 hours under stressful circumstances. Explosive.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(248,83,'ru','Кислородный Баллон','При подключении к вакуумному костюму обеспечивает до 12 часов кислорода в нормальных условиях, 4 часа в стрессовых. Взрывоопасен.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(249,83,'ua','Кисневий Балон','При підключенні до вакуумного костюма забезпечує до 12 годин кисню в нормальних умовах, 4 години в стресових. Вибухонебезпечний.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(250,84,'en','Paracord (50m)','General purpose lightweight nylon rope.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(251,84,'ru','Паракорд (50м)','Лёгкая нейлоновая верёвка общего назначения.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(252,84,'ua','Паракорд (50м)','Легка нейлонова мотузка загального призначення.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(253,85,'en','Patch Kit (x3)','Repairs punctured and torn vaccsuits, restoring their space readiness. Patched vaccsuits have an AP of 1.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(254,85,'ru','Ремнабор для Скафандра (x3)','Ремонтирует проколотые и порванные вакуумные костюмы, восстанавливая их годность к использованию в космосе. Залатанные костюмы имеют AP 1.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(255,85,'ua','Ремкомплект для Скафандра (x3)','Ремонтує проколоті та розірвані вакуумні костюми, відновлюючи їх придатність для космосу. Полагоджені костюми мають AP 1.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(256,86,'en','Personal Locator','Allows crewmembers at a control center (or on the bridge of a ship) to track the location of the wearer.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(257,86,'ru','Персональный Маяк','Позволяет членам экипажа на пункте управления (или на мостике корабля) отслеживать местонахождение носителя.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(258,86,'ua','Персональний Маяк','Дозволяє членам екіпажу на пункті управління (або на містку корабля) відстежувати місцезнаходження носія.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(259,87,'en','Pet (Organic)','Small to medium-sized organic pet animal. Larger or rare pets cost 2d10× base price.

Wounds: 1(10). Instinct: 2d10+40. 1 Trained Skill. [+] on Rest Saves. 1 Stress when pet takes Damage. Panic Check if pet is killed. Minimum Stress +1.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(260,87,'ru','Питомец (Органический)','Небольшое или среднее органическое животное. Крупные или редкие питомцы стоят в 2d10× дороже.

Ранения: 1(10). Инстинкт: 2d10+40. 1 Начальный Навык. [+] на Броски Отдыха. 1 Стресс при получении урона питомцем. Проверка Паники при гибели питомца. Минимальный Стресс +1.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(261,87,'ua','Вихованець (Органічний)','Невелика або середня органічна тварина. Великі або рідкісні вихованці коштують у 2d10× дорожче.

Поранення: 1(10). Інстинкт: 2d10+40. 1 Початковий Навик. [+] на Кидки Відпочинку. 1 Стрес при отриманні шкоди вихованцем. Перевірка Паніки при загибелі вихованця. Мінімальний Стрес +1.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(262,88,'en','Pet (Synthetic)','Small to medium-sized synthetic pet animal. Larger or rare pets cost 2d10× base price.

Wounds: 2(15). Instinct: 2d10+30. 2 Trained Skills or 1 Expert Skill. +5 to Rest Saves. Sanity Save or 1 Stress when pet takes Damage. 1 Stress if pet is destroyed.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(263,88,'ru','Питомец (Синтетический)','Небольшое или среднее синтетическое животное. Крупные или редкие питомцы стоят в 2d10× дороже.

Ранения: 2(15). Инстинкт: 2d10+30. 2 Начальных Навыка или 1 Экспертный. +5 к Броскам Отдыха. Спасбросок Рассудка или 1 Стресс при получении урона. 1 Стресс при уничтожении питомца.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(264,88,'ua','Вихованець (Синтетичний)','Невелика або середня синтетична тварина. Великі або рідкісні вихованці коштують у 2d10× дорожче.

Поранення: 2(15). Інстинкт: 2d10+30. 2 Початкових Навики або 1 Експертний. +5 до Кидків Відпочинку. Порятунок Розуму або 1 Стрес при отриманні шкоди. 1 Стрес при знищенні вихованця.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(265,89,'en','Portable Computer Terminal','Flat monitor, keyboard and interface allowing the user to hack into pre-existing computers and networks, as well as perform standard computer tasks.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(266,89,'ru','Портативный Компьютерный Терминал','Плоский монитор, клавиатура и интерфейс для взлома существующих компьютеров и сетей, а также для стандартных компьютерных задач.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(267,89,'ua','Портативний Комп''ютерний Термінал','Плаский монітор, клавіатура та інтерфейс для злому існуючих комп''ютерів і мереж, а також для стандартних комп''ютерних завдань.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(268,90,'en','Radiation Pills (x5)','Take 1d5 DMG and reduce your Radiation Level by 1 for 2d10 minutes.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(269,90,'ru','Таблетки от Радиации (x5)','Примите, получив 1d5 урона, и снизьте уровень Радиации на 1 на 2d10 минут.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(270,90,'ua','Таблетки від Радіації (x5)','Прийміть, отримавши 1d5 шкоди, і знизьте рівень Радіації на 1 на 2d10 хвилин.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(271,91,'en','Radio Jammer','Rucksack-sized device which, when activated, renders all radio signals within 100km incomprehensible.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(272,91,'ru','Радиоглушитель','Устройство размером с рюкзак. При активации делает все радиосигналы в радиусе 100 км неразборчивыми.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(273,91,'ua','Радіоглушник','Пристрій розміром з рюкзак. При активації робить усі радіосигнали в радіусі 100 км нерозбірливими.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(274,92,'en','Rebreather','Filters toxic air and/or allows for underwater breathing for up to 20 minutes at a time without resurfacing. Can be connected to an oxygen tank.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(275,92,'ru','Ребризер','Фильтрует токсичный воздух и/или позволяет дышать под водой до 20 минут без подъёма на поверхность. Можно подключить к кислородному баллону.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(276,92,'ua','Ребризер','Фільтрує токсичне повітря та/або дозволяє дихати під водою до 20 хвилин без підйому на поверхню. Можна підключити до кисневого балону.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(277,93,'en','Rucksack','Large, durable, waterproof backpack.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(278,93,'ru','Рюкзак','Большой, прочный, водонепроницаемый рюкзак.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(279,93,'ua','Рюкзак','Великий, міцний, водонепроникний рюкзак.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(280,94,'en','Salvage Drone','Battery-operated remote controlled drone. Flies up to 450m high, up to 3km from operator, for 2 hours. Records and transmits footage. Can be equipped with up to two attachments: binoculars, radio jammer, Geiger counter, laser cutter, medscanner, personal locator, infrared goggles, emergency beacon, cybernetic diagnostic scanner, or bioscanner. Carries up to 20–30kg.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(281,94,'ru','Дрон-Мусорщик','Дрон с дистанционным управлением на аккумуляторе. Летает до 450 м высоты, до 3 км от оператора, 2 часа. Записывает и передаёт видео. Оснащается двумя приспособлениями: бинокль, глушилка, счётчик Гейгера, лазерный резак, медсканер, маяк, ИК-очки, аварийный маяк, кибердиагностика или биосканер. Грузоподъёмность — до 20–30 кг.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(282,94,'ua','Дрон-Збирач','Дрон з дистанційним управлінням на акумуляторі. Летить до 450 м висоти, до 3 км від оператора, 2 години. Записує та передає відео. Оснащується двома пристосуваннями: бінокль, глушник, лічильник Гейгера, лазерний різак, медсканер, маяк, ІЧ-окуляри, аварійний маяк, кібердіагностика або біосканер. Вантажопідйомність — до 20–30 кг.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(283,95,'en','Sample Collection Kit','Used to research xenoflora and xenofauna in the field. Takes vital signs, DNA samples, and collects other data on foreign material. Results may require a lab for complete analysis.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(284,95,'ru','Набор для Сбора Образцов','Используется для изучения ксенофлоры и ксенофауны в полевых условиях. Снимает жизненные показатели, берёт образцы ДНК и собирает другие данные. Результаты могут требовать лаборатории.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(285,95,'ua','Набір для Збору Зразків','Використовується для вивчення ксенофлори та ксенофауни в польових умовах. Знімає жизнєві показники, бере зразки ДНК та збирає інші дані. Результати можуть вимагати лабораторії.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(286,96,'en','Short-range Comms','Allows communication from ship-to-ship within a reasonable distance, and surface-to-surface within a dozen kilometers. Blocked by radio jammer.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(287,96,'ru','Коротковолновая Связь','Позволяет общаться между кораблями на небольшом расстоянии и на поверхности в пределах нескольких километров. Блокируется радиоглушителем.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(288,96,'ua','Короткохвильовий Зв''язок','Дозволяє спілкуватися між кораблями на невеликій відстані та на поверхні в межах кількох кілометрів. Блокується радіоглушником.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(289,97,'en','Smart-link Add-On','Grants remote viewing, recording, and operation of a ranged weapon, plus +5 DMG to the weapon.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(290,97,'ru','Умная Привязка','Даёт дистанционный просмотр, запись и управление дальнобойным оружием, а также +5 урона.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(291,97,'ua','Розумний Зв''язок','Дає дистанційний перегляд, запис і управління далекобійною зброєю, а також +5 шкоди.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(292,98,'en','Stimpak','Cures cryosickness, reduces Stress by 1, restores 1d10 Health, and grants [+] to all rolls for 1d10 minutes.

Overdose: Roll 1d10. If you roll under the number of doses taken in the past 24 hours, make a Death Save.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(293,98,'ru','Стимпак','Излечивает криобольность, снижает Стресс на 1, восстанавливает 1d10 Здоровья и даёт [+] ко всем броскам на 1d10 минут.

Передозировка: Бросьте 1d10. Если результат ниже числа доз за последние 24 часа — совершите Спасбросок от Смерти.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(294,98,'ua','Стімпак','Лікує кріохворобу, знижує Стрес на 1, відновлює 1d10 Здоров''я і дає [+] до всіх кидків на 1d10 хвилин.

Передозування: Киньте 1d10. Якщо результат нижче кількості доз за останні 24 години — зробіть Порятунок від Смерті.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(295,99,'en','Water Filtration Device','Can pump 4 liters of filtered water per hour from even the most brackish swamps.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(296,99,'ru','Устройство Фильтрации Воды','Может перекачивать 4 литра фильтрованной воды в час даже из самых мутных болот.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(297,99,'ua','Пристрій Фільтрації Води','Може перекачувати 4 літри фільтрованої води на годину навіть з найбрудніших боліт.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(298,100,'en','Stat Checks','Roll 1d100 and try to roll lower than your most relevant Stat. Success if you roll under your Stat. Failure: you gain 1 Stress. A roll of 90–99 is always a failure.

Your four Stats:
• Strength — holding airlocks closed, carrying fallen comrades, climbing, pushing, jumping.
• Speed — escaping before blast doors close, acting before others, running away.
• Intellect — recalling training under duress, thinking through difficult problems, fixing things.
• Combat — fighting for your life.

If you have a relevant Skill, add its bonus to your Stat before rolling.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(299,100,'ru','Проверки Параметров','Бросьте 1d100 и постарайтесь выбросить меньше наиболее подходящего Параметра. Успех — если бросок меньше Параметра. Провал — получаете 1 Стресс. Результат 90–99 всегда является провалом.

Четыре Параметра:
• Сила — удерживать шлюзы, нести упавших товарищей, карабкаться, толкать, прыгать.
• Скорость — бежать до закрытия переборок, действовать быстрее других, убегать.
• Интеллект — вспоминать тренировки под давлением, решать сложные задачи, чинить вещи.
• Бой — сражаться за свою жизнь.

Если у вас есть подходящий Навык, прибавьте его бонус к Параметру перед броском.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(300,100,'ua','Перевірки Параметрів','Киньте 1d100 і намагайтеся кинути нижче найбільш відповідного Параметра. Успіх — якщо кидок нижче Параметра. Провал — отримуєте 1 Стрес. Результат 90–99 завжди є провалом.

Чотири Параметри:
• Сила — утримувати шлюзи, нести поранених товаришів, лізти, штовхати, стрибати.
• Швидкість — тікати до закриття переборок, діяти швидше інших, тікати.
• Інтелект — згадувати тренування під тиском, вирішувати складні завдання, лагодити речі.
• Бій — боротися за своє життя.

Якщо у вас є відповідний Навик, додайте його бонус до Параметра перед кидком.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(301,101,'en','Saves','Roll 1d100 and try to roll lower than your most relevant Save to avoid certain dangers or trauma. Success if you roll under your Save. Failure: you gain 1 Stress. A roll of 90–99 is always a failure.

Your three Saves:
• Sanity — rationalize logical inconsistencies, make sense of chaos, detect illusions and mimicry, cope with Stress.
• Fear — maintain a level head while struggling with fear, loneliness, depression, and other emotional surges.
• Body — employ quick reflexes and resist hunger, disease, or organisms trying to invade your insides.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(302,101,'ru','Спасброски','Бросьте 1d100 и постарайтесь выбросить меньше наиболее подходящего Спасброска, чтобы избежать определённых опасностей или травм. Успех — если бросок меньше Спасброска. Провал — получаете 1 Стресс. Результат 90–99 всегда является провалом.

Три Спасброска:
• Рассудок — рационализировать логические противоречия, разобраться в хаосе, обнаружить иллюзии и мимикрию, справляться со Стрессом.
• Страх — сохранять хладнокровие перед лицом страха, одиночества, депрессии и других эмоциональных всплесков.
• Тело — быстрые рефлексы и сопротивление голоду, болезням или организмам, пытающимся проникнуть внутрь.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(303,101,'ua','Порятунки','Киньте 1d100 і намагайтеся кинути нижче найбільш відповідного Порятунку, щоб уникнути певних небезпек або травм. Успіх — якщо кидок нижче Порятунку. Провал — отримуєте 1 Стрес. Результат 90–99 завжди є провалом.

Три Порятунки:
• Розум — раціоналізувати логічні суперечності, розібратися в хаосі, виявити ілюзії та мімікрію, справлятися зі Стресом.
• Страх — зберігати холоднокровність перед обличчям страху, самотності, депресії та інших емоційних сплесків.
• Тіло — швидкі рефлекси і опір голоду, хворобам або організмам, що намагаються проникнути всередину.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(304,102,'en','Advantage & Disadvantage','Advantage [+]: Roll twice, take the better result. Granted by helpful circumstances (assistance from others, good positioning, relevant Skill, etc.).

Disadvantage [-]: Roll twice, take the worse result. Imposed by poor circumstances (bad weather, poor visibility, injury, etc.).

If a character has both Advantage and Disadvantage, they cancel each other out.

Critical Successes & Failures: Rolling doubles (00, 11, 22 … 99) on a Stat Check or Save is a Critical. Succeeding doubles = Critical Success (something very good happens). Failing doubles = Critical Failure (something bad happens AND you must make a Panic Check). 00 is always a Critical Success. 99 is always a Critical Failure.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(305,102,'ru','Преимущество и Помеха','Преимущество [+]: Бросайте дважды, берите лучший результат. Предоставляется благоприятными обстоятельствами (помощь, хорошая позиция, Навык и т.д.).

Помеха [-]: Бросайте дважды, берите худший результат. Накладывается неблагоприятными обстоятельствами (плохая погода, плохая видимость, травма и т.д.).

Если у персонажа есть и Преимущество, и Помеха, они нейтрализуют друг друга.

Критические Успехи и Провалы: Выпадение дублей (00, 11, 22 … 99) на Проверке или Спасброске — Критический результат. Успешные дубли = Критический Успех (происходит что-то очень хорошее). Провальные дубли = Критический Провал (происходит что-то плохое И необходимо совершить Проверку Паники). 00 — всегда Критический Успех. 99 — всегда Критический Провал.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(306,102,'ua','Перевага та Перешкода','Перевага [+]: Кидайте двічі, беріть кращий результат. Надається сприятливими обставинами (допомога, гарна позиція, Навик тощо).

Перешкода [-]: Кидайте двічі, беріть гірший результат. Накладається несприятливими обставинами (погана погода, погана видимість, травма тощо).

Якщо у персонажа є і Перевага, і Перешкода, вони нейтралізують одна одну.

Критичні Успіхи та Провали: Випадання дублів (00, 11, 22 … 99) на Перевірці або Порятунку — Критичний результат. Успішні дубли = Критичний Успіх (відбувається щось дуже хороше). Провальні дубли = Критичний Провал (відбувається щось погане І необхідно зробити Перевірку Паніки). 00 — завжди Критичний Успіх. 99 — завжди Критичний Провал.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(307,103,'en','Stress','Stress measures the toll the cosmos takes on a person. Higher Stress means higher chance to Panic, and more Stress when you Panic means worse results.

Gaining Stress: Gain 1 Stress every time you fail a Stat Check or Save. Some locations or entities grant Stress automatically. Maximum Stress is 20; any Stress over 20 reduces the most relevant Stat or Save by that amount.

Minimum Stress starts at 2 and can be raised or lowered by Panic Check results.

Relieving Stress (Rest): In a relatively safe place, make a Rest Save using your worst Save. Success: reduce Stress by the ones digit of your roll (e.g., rolling 24 under Save of 30 reduces Stress by 4). Failure: gain 1 Stress. Gain Advantage on Rest Saves through consensual sex, recreational drug use, a night of heavy drinking, prayer, or other leisure activities.

Relieving Stress (Shore Leave): Convert Stress into improved Saves at a Port.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(308,103,'ru','Стресс','Стресс измеряет тяжесть последствий космоса для человека. Чем выше Стресс — тем больше шанс Паники и тем хуже её результаты.

Получение Стресса: Получайте 1 Стресс каждый раз, когда проваливаете Проверку Параметра или Спасбросок. Некоторые места или существа дают Стресс автоматически. Максимальный Стресс — 20; любой Стресс сверх 20 снижает наиболее релевантный Параметр или Спасбросок на это значение.

Минимальный Стресс начинается с 2 и может меняться по результатам Проверки Паники.

Снятие Стресса (Отдых): В относительно безопасном месте совершите Бросок Отдыха с использованием худшего Спасброска. Успех: снизьте Стресс на цифру единиц выпавшего результата. Провал: получите 1 Стресс. Преимущество на Броске Отдыха дают секс по согласию, наркотики для отдыха, ночная пьянка, молитва и т.д.

Снятие Стресса (Увольнение): Конвертируйте Стресс в улучшенные Спасброски в Порту.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(309,103,'ua','Стрес','Стрес вимірює тягар наслідків космосу для людини. Вищий Стрес — більший шанс Паніки і гірші її результати.

Отримання Стресу: Отримуйте 1 Стрес кожного разу, коли провалюєте Перевірку Параметра або Порятунок. Деякі місця або істоти дають Стрес автоматично. Максимальний Стрес — 20; будь-який Стрес понад 20 знижує найбільш релевантний Параметр або Порятунок на цю величину.

Мінімальний Стрес починається з 2 і може змінюватися за результатами Перевірки Паніки.

Зняття Стресу (Відпочинок): У відносно безпечному місці зробіть Кидок Відпочинку з використанням найгіршого Порятунку. Успіх: знизьте Стрес на цифру одиниць результату. Провал: отримайте 1 Стрес. Перевагу на Кидку Відпочинку дають секс за згодою, рекреаційні наркотики, нічне пияцтво, молитва тощо.

Зняття Стресу (Відпустка): Конвертуйте Стрес у покращені Порятунки в Порту.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(310,104,'en','Panic Checks','Roll the Panic Die (1d20) and try to roll greater than your current Stress. On failure (roll ≤ Stress), look up your result below.

When to make a Panic Check: On any Critical Failure on a Stat Check or Save; watching another crewmember die; witnessing 2+ crewmembers Panic simultaneously; ship rolls a Critical Failure (all on board Panic); encountering a horrifying entity for the first time; when all hope is lost; whenever you want.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(311,104,'ru','Проверки Паники','Бросьте Кубик Паники (1d20) и постарайтесь выбросить больше текущего Стресса. При провале (результат ≤ Стресс) смотрите результат ниже.

Когда делать Проверку Паники: при Критическом Провале Проверки или Спасброска; при гибели другого члена экипажа; при виде 2+ паникующих одновременно; при Критическом Провале корабля (паникуют все на борту); при первой встрече с ужасающей сущностью; когда всё потеряно; в любой момент по желанию.',NULL,'["ВЫБРОС АДРЕНАЛИНА. [+] на все броски в течение 2d10 минут. Уменьшите Стресс на 1d5.", "НЕРВОЗНОСТЬ. Получите 1 Стресс.", "ВЗВИНЧЕННОСТЬ. Получите 1 Стресс. Все Близкие члены экипажа получают 2 Стресса.", "ПОДАВЛЕННОСТЬ. [-] на все броски в течение 1d10 минут. Увеличьте Минимальный Стресс на 1.", "ТРУСОСТЬ. Новое Состояние: Вы должны сделать Спасбросок Страха, чтобы вступить в бой, иначе вы бежите.", "ИСПУГ. Новое Состояние: При встрече с тем, что вас напугало, делайте Спасбросок Страха [-] или получайте 1d5 Стресса.", "НОЧНЫЕ КОШМАРЫ. Новое Состояние: Сон нарушен, [-] на Спасброски Отдыха.", "ПОТЕРЯ УВЕРЕННОСТИ. Новое Состояние: Выберите один Навык и потеряйте его бонус.", "УПАДОК СИЛ. Новое Состояние: Когда Близкий член экипажа проваливает Спасбросок, получайте 1 Стресс.", "ОБРЕЧЁННОСТЬ. Новое Состояние: Вы чувствуете себя проклятым. Все Критические Успехи становятся Критическими Провалами.", "ПОДОЗРИТЕЛЬНОСТЬ. В течение следующей недели при появлении нового члена экипажа делайте Спасбросок Страха или получайте 1 Стресс.", "ПРИЗРАКИ. Новое Состояние: Нечто начинает навещать персонажа ночью. В его снах. Краем глаза. И скоро оно начнёт предъявлять требования.", "ЖАЖДА СМЕРТИ. В течение следующих 24 часов при встрече с незнакомцем или известным врагом делайте Спасбросок Рассудка или немедленно нападайте.", "ПРОРОЧЕСКОЕ ВИДЕНИЕ. Персонаж переживает интенсивную галлюцинацию надвигающегося ужаса. Увеличьте Минимальный Стресс на 2.", "КАТАТОНИЯ. Персонаж неотзывчив и неподвижен 2d10 минут. Уменьшите Стресс на 1d10.", "ЯРОСТЬ. [+] на все броски Урона в течение 1d10 часов. Все члены экипажа получают 1 Стресс.", "НАРАСТАНИЕ. Новое Состояние: Проверки Паники с [-].", "НАГРОМОЖДЕНИЕ ПРОБЛЕМ. Бросьте дважды на этой таблице. Увеличьте Минимальный Стресс на 1.", "СЕРДЕЧНЫЙ ПРИСТУП / СБОЙ (АНДРОИДЫ). Уменьшите Максимальные Раны на 1. [-] на все броски 1d10 часов. Увеличьте Минимальный Стресс на 1.", "УЙТИ НА ПОКОЙ. Создайте нового персонажа."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(312,104,'ua','Перевірки Паніки','Киньте Кубик Паніки (1d20) і намагайтеся кинути більше поточного Стресу. При провалі (результат ≤ Стрес) дивіться результат нижче.

Коли робити Перевірку Паніки: при Критичному Провалі Перевірки або Порятунку; при загибелі іншого члена екіпажу; при вигляді 2+ тих, хто панікує одночасно; при Критичному Провалі корабля (панікують усі на борту); при першій зустрічі з жахливою істотою; коли все втрачено; в будь-який момент за бажанням.',NULL,'["ВИКИД АДРЕНАЛІНУ. [+] на всі кидки протягом 2d10 хвилин. Зменшіть Стрес на 1d5.", "НЕРВОЗНІСТЬ. Отримайте 1 Стрес.", "НАПРУГА. Отримайте 1 Стрес. Всі Близькі члени екіпажу отримують 2 Стресу.", "ПРИГНІЧЕНІСТЬ. [-] на всі кидки протягом 1d10 хвилин. Збільшіть Мінімальний Стрес на 1.", "БОЯГУЗТВО. Новий Стан: Ви повинні зробити Рятівний від Страху, щоб вступити в бій, інакше ви тікаєте.", "ПЕРЕЛЯК. Новий Стан: При зустрічі з тим, що вас налякало, робіть Рятівний від Страху [-] або отримуйте 1d5 Стресу.", "НІЧНІ ЖАХИ. Новий Стан: Сон порушений, [-] на Рятівні Відпочинку.", "ВТРАТА ВПЕВНЕНОСТІ. Новий Стан: Оберіть один Навик і втратьте його бонус.", "ЗАНЕПАД СИЛ. Новий Стан: Коли Близький член екіпажу провалює Рятівний, отримуйте 1 Стрес.", "ПРИРЕЧЕНІСТЬ. Новий Стан: Ви відчуваєте себе прокляутим. Всі Критичні Успіхи стають Критичними Провалами.", "ПІДОЗРІЛІСТЬ. Протягом наступного тижня при появі нового члена екіпажу робіть Рятівний від Страху або отримуйте 1 Стрес.", "ПРИВИДИ. Новий Стан: Щось починає відвідувати персонажа вночі. У його снах. Краєм ока. І незабаром воно почне висувати вимоги.", "ЖАГА СМЕРТІ. Протягом наступних 24 годин при зустрічі з незнайомцем або ворогом робіть Рятівний Розуму або негайно нападайте.", "ПРОРОЧЕ БАЧЕННЯ. Персонаж переживає інтенсивну галюцинацію жаху. Збільшіть Мінімальний Стрес на 2.", "КАТАТОНІЯ. Персонаж нерухомий і не реагує 2d10 хвилин. Зменшіть Стрес на 1d10.", "ЛЮТЬ. [+] на всі кидки Шкоди протягом 1d10 годин. Всі члени екіпажу отримують 1 Стрес.", "НАРОСТАННЯ. Новий Стан: Перевірки Паніки з [-].", "НАГРОМАДЖЕННЯ ПРОБЛЕМ. Кидайте двічі на цій таблиці. Збільшіть Мінімальний Стрес на 1.", "СЕРЦЕВИЙ НАПАД / ЗБІЙ (АНДРОЇДИ). Зменшіть Максимальні Рани на 1. [-] на всі кидки 1d10 годин. Збільшіть Мінімальний Стрес на 1.", "ВИЙТИ НА ПЕНСІЮ. Створіть нового персонажа."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(313,105,'en','Conditions','Some Panic Table results leave a lasting impression. These are called Conditions, and they affect you until treated.

Conditions from the Panic Table:
• Coward (5) — Fear Save to engage in violence, otherwise flee.
• Frightened (6) — Fear Save [-] or 1d5 Stress when encountering the trigger.
• Nightmares (7) — [-] on Rest Saves.
• Loss of Confidence (8) — One chosen Skill loses its bonus.
• Deflated (9) — Gain 1 Stress when a Close crewmember fails a Save.
• Doomed (10) — All Critical Successes become Critical Failures.
• Haunted (12) — Something is watching. It will start making demands.
• Spiraling (17) — Panic Checks at [-].

Conditions require professional medical treatment to remove.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(314,105,'ru','Состояния','Некоторые результаты Таблицы Паники оставляют глубокий след. Они называются Состояниями и действуют до получения лечения.

Состояния из Таблицы Паники:
• Трус (5) — Спасбросок Страха для участия в насилии, иначе бегство.
• Напуган (6) — Спасбросок Страха [-] или 1d5 Стресса при встрече с триггером.
• Кошмары (7) — [-] на Броски Отдыха.
• Потеря уверенности (8) — Выбранный Навык теряет бонус.
• Сломлен (9) — 1 Стресс при провале Спасброска близким товарищем.
• Проклят (10) — Все Критические Успехи становятся Критическими Провалами.
• Одержим (12) — Что-то наблюдает. Скоро начнёт требовать.
• Штопор (17) — Проверки Паники с Помехой [-].

Для снятия Состояния требуется профессиональная медицинская помощь.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(315,105,'ua','Стани','Деякі результати Таблиці Паніки залишають глибокий слід. Вони називаються Станами і діють до отримання лікування.

Стани з Таблиці Паніки:
• Боягуз (5) — Порятунок від Страху для участі у насильстві, інакше втеча.
• Наляканий (6) — Порятунок від Страху [-] або 1d5 Стресу при зустрічі з тригером.
• Кошмари (7) — [-] на Кидки Відпочинку.
• Втрата впевненості (8) — Обраний Навик втрачає бонус.
• Зламаний (9) — 1 Стрес при провалі Порятунку близьким товаришем.
• Проклятий (10) — Усі Критичні Успіхи стають Критичними Провалами.
• Переслідуваний (12) — Щось спостерігає. Незабаром почне вимагати.
• Штопор (17) — Перевірки Паніки з Перешкодою [-].

Для зняття Стану потрібна професійна медична допомога.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(316,106,'en','Linguistics','The study of languages (alive, dead, and undiscovered).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(317,106,'ru','Лингвистика','Изучение языков (живых, мёртвых и неоткрытых).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(318,106,'ua','Лінгвістика','Вивчення мов (живих, мертвих та нерозкритих).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(319,107,'en','Zoology','The study of animal life.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(320,107,'ru','Зоология','Изучение животной жизни.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(321,107,'ua','Зоологія','Вивчення тваринного життя.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(322,108,'en','Botany','The study of plant life.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(323,108,'ru','Ботаника','Изучение растительной жизни.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(324,108,'ua','Ботаніка','Вивчення рослинного життя.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(325,109,'en','Geology','The study of the solid features of any terrestrial planet or its satellites.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(326,109,'ru','Геология','Изучение твёрдых пород любой планеты земного типа или её спутников.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(327,109,'ua','Геологія','Вивчення твердих порід будь-якої планети земного типу або її супутників.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(328,110,'en','Industrial Equipment','The safe and proper use of heavy machinery and tools (exosuits, forklifts, drills, breakers, laser cutters, etc.).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(329,110,'ru','Промышленное Оборудование','Безопасное и правильное использование тяжёлой техники и инструментов (экзоскелеты, погрузчики, дрели, отбойники, лазерные резаки и т.д.).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(330,110,'ua','Промислове Обладнання','Безпечне та правильне використання важкої техніки та інструментів (екзоскелети, навантажувачі, дрилі, відбійники, лазерні різаки тощо).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(331,111,'en','Jury-Rigging','Makeshift repair using only the tools and materials at hand.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(332,111,'ru','Самоделки','Кустарный ремонт с использованием только подручных инструментов и материалов.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(333,111,'ua','Саморобки','Кустарний ремонт з використанням лише підручних інструментів і матеріалів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(334,112,'en','Chemistry','The study of matter and its chemical elements and compounds.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(335,112,'ru','Химия','Изучение материи, её химических элементов и соединений.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(336,112,'ua','Хімія','Вивчення матерії, її хімічних елементів і сполук.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(337,113,'en','Computers','Fluent use of computers and their networks.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(338,113,'ru','Компьютеры','Свободное владение компьютерами и их сетями.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(339,113,'ua','Комп''ютери','Вільне використання комп''ютерів та їх мереж.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(340,114,'en','Zero-G','Practice and know-how of working in a vacuum, orientation, vaccsuit operation, etc.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(341,114,'ru','Невесомость','Практика и навыки работы в вакууме, ориентирование, использование вакуумного костюма и т.д.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(342,114,'ua','Невагомість','Практика та навички роботи у вакуумі, орієнтування, використання вакуумного костюма тощо.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(343,115,'en','Mathematics','The study of numbers, quantity, and space.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(344,115,'ru','Математика','Изучение чисел, количества и пространства.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(345,115,'ua','Математика','Вивчення чисел, кількості та простору.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(346,116,'en','Art','The expression or application of a species'' creative ability and imagination.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(347,116,'ru','Искусство','Выражение или применение творческих способностей и воображения биологического вида.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(348,116,'ua','Мистецтво','Вираження або застосування творчих здібностей та уяви біологічного виду.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(349,117,'en','Archaeology','Ancient cultures and artifacts.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(350,117,'ru','Археология','Древние культуры и артефакты.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(351,117,'ua','Археологія','Давні культури та артефакти.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(352,118,'en','Theology','The study of the divine or devotion to a religion.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(353,118,'ru','Теология','Изучение божественного или преданность религии.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(354,118,'ua','Теологія','Вивчення божественного або відданість релігії.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(355,119,'en','Military Training','Basic training provided to all military personnel.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(356,119,'ru','Военная Подготовка','Базовая подготовка, предоставляемая всему военному персоналу.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(357,119,'ua','Військова Підготовка','Базова підготовка, що надається всьому військовому персоналу.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(358,120,'en','Rimwise','Practical knowledge and know-how regarding outer Rim colonies, their customs, and the seedier parts of the galaxy.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(359,120,'ru','Окраины','Практические знания об окраинных колониях, их обычаях и более тёмных уголках галактики.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(360,120,'ua','Окраїни','Практичні знання про окраїнні колонії, їх звичаї та темніші куточки галактики.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(361,121,'en','Athletics','Physical fitness, sports, and games.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(362,121,'ru','Атлетика','Физическая подготовка, спорт и игры.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(363,121,'ua','Атлетика','Фізична підготовка, спорт та ігри.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(364,122,'en','Psychology','The study of behavior and the human mind.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(365,122,'ru','Психология','Изучение поведения и человеческого разума.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(366,122,'ua','Психологія','Вивчення поведінки та людського розуму.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(367,123,'en','Pathology','Study of the causes and effects of diseases.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(368,123,'ru','Патология','Изучение причин и последствий заболеваний.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(369,123,'ua','Патологія','Вивчення причин та наслідків захворювань.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(370,124,'en','Field Medicine','Emergency medical care and treatment.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(371,124,'ru','Полевая Медицина','Экстренная медицинская помощь и лечение.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(372,124,'ua','Польова Медицина','Екстрена медична допомога та лікування.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(373,125,'en','Ecology','The study of organisms and how they relate to their environment.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(374,125,'ru','Экология','Изучение организмов и их связи с окружающей средой.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(375,125,'ua','Екологія','Вивчення організмів та їх зв''язку з навколишнім середовищем.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(376,126,'en','Asteroid Mining','Training in the tools and procedures used for mining asteroids.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(377,126,'ru','Добыча Астероидов','Подготовка к использованию инструментов и процедур добычи астероидов.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(378,126,'ua','Видобуток Астероїдів','Підготовка до використання інструментів та процедур видобутку астероїдів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(379,127,'en','Mechanical Repair','Fixing broken machines.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(380,127,'ru','Механический Ремонт','Ремонт неисправных машин.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(381,127,'ua','Механічний Ремонт','Ремонт несправних машин.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(382,128,'en','Explosives','Design and effective use of explosive devices (bombs, grenades, shells, land mines, etc.).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(383,128,'ru','Взрывчатые Вещества','Проектирование и эффективное применение взрывных устройств (бомбы, гранаты, снаряды, мины и т.д.).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(384,128,'ua','Вибухові Речовини','Проєктування та ефективне застосування вибухових пристроїв (бомби, гранати, снаряди, міни тощо).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(385,129,'en','Pharmacology','Study of drugs and medication.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(386,129,'ru','Фармакология','Изучение лекарственных препаратов и медикаментов.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(387,129,'ua','Фармакологія','Вивчення лікарських препаратів та медикаментів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(388,130,'en','Hacking','Unauthorized access to computer systems and networks.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(389,130,'ru','Взлом','Несанкционированный доступ к компьютерным системам и сетям.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(390,130,'ua','Злом','Несанкціонований доступ до комп''ютерних систем і мереж.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(391,131,'en','Piloting','Operation and control of aircraft, spacecraft, and other vehicles.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(392,131,'ru','Пилотирование','Управление и контроль самолётов, космических кораблей и других транспортных средств.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(393,131,'ua','Пілотування','Управління та контроль літаків, космічних кораблів та інших транспортних засобів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(394,132,'en','Physics','Study of matter, motion, energy, and their effects in space and time.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(395,132,'ru','Физика','Изучение материи, движения, энергии и их воздействия в пространстве и времени.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(396,132,'ua','Фізика','Вивчення матерії, руху, енергії та їх впливу в просторі та часі.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(397,133,'en','Mysticism','Spiritual apprehension of hidden knowledge.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(398,133,'ru','Мистика','Духовное постижение скрытого знания.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(399,133,'ua','Містика','Духовне осягнення прихованого знання.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(400,134,'en','Firearms','Safe and effective use of guns.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(401,134,'ru','Огнестрельное Оружие','Безопасное и эффективное использование огнестрельного оружия.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(402,134,'ua','Вогнепальна Зброя','Безпечне та ефективне використання вогнепальної зброї.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(403,135,'en','Hand-to-Hand Combat','Melee fighting, brawling, martial arts, etc.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(404,135,'ru','Рукопашный Бой','Ближний бой, драки, боевые искусства и т.д.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(405,135,'ua','Рукопашний Бій','Ближній бій, бійки, бойові мистецтва тощо.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(406,136,'en','Wilderness Survival','Applicable know-how regarding the basic necessities of life (food, water, shelter) in a natural environment.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(407,136,'ru','Выживание в Природе','Применимые знания об основных потребностях жизни (еда, вода, укрытие) в природных условиях.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(408,136,'ua','Виживання на Природі','Застосовувані знання про основні потреби для виживання (їжа, вода, укриття) в природних умовах.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(409,137,'en','Sophontology','The study of the behavior and mind of inhuman entities.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(410,137,'ru','Софонтология','Изучение поведения и разума нечеловеческих существ.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(411,137,'ua','Софонтологія','Вивчення поведінки та розуму нелюдських істот.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(412,138,'en','Exobiology','The study of and search for intelligent alien life.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(413,138,'ru','Экзобиология','Изучение и поиск разумной инопланетной жизни.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(414,138,'ua','Екзобіологія','Вивчення та пошук розумного інопланетного життя.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(415,139,'en','Surgery','Manually operating on living or dead biological subjects.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(416,139,'ru','Хирургия','Ручное оперирование живых или мёртвых биологических объектов.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(417,139,'ua','Хірургія','Ручне оперування живих або мертвих біологічних об''єктів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(418,140,'en','Planetology','Study of planets and other celestial bodies.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(419,140,'ru','Планетология','Изучение планет и других небесных тел.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(420,140,'ua','Планетологія','Вивчення планет та інших небесних тіл.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(421,141,'en','Robotics','Design, maintenance, and operation of robots, drones, and androids.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(422,141,'ru','Робототехника','Проектирование, обслуживание и управление роботами, дронами и андроидами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(423,141,'ua','Робототехніка','Проєктування, обслуговування та управління роботами, дронами та андроїдами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(424,142,'en','Engineering','The design, building, and use of engines, machines, and structures.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(425,142,'ru','Инженерия','Проектирование, строительство и использование двигателей, машин и конструкций.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(426,142,'ua','Інженерія','Проєктування, будівництво та використання двигунів, машин і конструкцій.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(427,143,'en','Cybernetics','The physical and neural interfaces between organisms and machines.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(428,143,'ru','Кибернетика','Физические и нейронные интерфейсы между организмами и машинами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(429,143,'ua','Кібернетика','Фізичні та нейронні інтерфейси між організмами та машинами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(430,144,'en','Artificial Intelligence','The study of intelligence as demonstrated by machines.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(431,144,'ru','Искусственный Интеллект','Изучение интеллекта, демонстрируемого машинами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(432,144,'ua','Штучний Інтелект','Вивчення інтелекту, що демонструється машинами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(433,145,'en','Hyperspace','Faster-than-light travel.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(434,145,'ru','Гиперпространство','Путешествие быстрее скорости света.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(435,145,'ua','Гіперпростір','Подорож швидше швидкості світла.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(436,146,'en','Xenoesotericism','Obscure beliefs, mysticism, and religion regarding non-human entities.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(437,146,'ru','Ксенотерика','Малоизвестные верования, мистика и религия, касающиеся нечеловеческих существ.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(438,146,'ua','Ксенотерика','Маловідомі вірування, містика та релігія щодо нелюдських істот.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(439,147,'en','Command','Leadership, management, and authority.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(440,147,'ru','Командование','Лидерство, управление и авторитет.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(441,147,'ua','Командування','Лідерство, управління та авторитет.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(442,148,'en','Train a Skill','To learn a new Skill you need time and credits:

• Trained Skill (+10): 2 years + 10kcr in materials.
• Expert Skill (+15): 4 years + 50kcr in materials.
• Master Skill (+20): 6 years + 200kcr in materials.

Expert Skills require one Trained Skill prerequisite. Master Skills require one Expert Skill prerequisite.

Training assumes working full-time on missions and living life. Studying full-time (e.g., school) halves the time. The Warden may allow other resources (tutoring, AI assistance, cybermods) to decrease the time required.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(443,148,'ru','Обучение Навыку','Для освоения нового Навыка необходимы время и кредиты:

• Начальный Навык (+10): 2 года + 10ккр в материалах.
• Экспертный Навык (+15): 4 года + 50ккр в материалах.
• Мастерский Навык (+20): 6 лет + 200ккр в материалах.

Для Экспертного Навыка требуется один Начальный предпосылочный Навык. Для Мастерского — один Экспертный.

Обучение предполагает работу на полную ставку с миссиями. Полноценная учёба (например, в школе) вдвое сокращает время. Надзиратель может разрешить другие ресурсы (репетиторство, ИИ, кибермоды) для сокращения необходимого времени.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(444,148,'ua','Навчання Навику','Для освоєння нового Навику необхідні час і кредити:

• Початковий Навик (+10): 2 роки + 10ккр у матеріалах.
• Експертний Навик (+15): 4 роки + 50ккр у матеріалах.
• Майстерний Навик (+20): 6 років + 200ккр у матеріалах.

Для Експертного Навику потрібен один Початковий передумовний Навик. Для Майстерного — один Експертний.

Навчання передбачає роботу на повну ставку з місіями. Повноцінне навчання (наприклад, у школі) вдвічі скорочує час. Охоронець може дозволити інші ресурси (репетиторство, ШІ, кіберзасоби) для скорочення необхідного часу.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(445,149,'en','Military Training Enlistment','Military Training is free but requires signing a 6-year contract with the local Colonial Marine regiment. Make a Combat Check to find out what happened during service:

• Success: Gain Military Training, Athletics, and 2 Trained Skills. +10 Combat, -10 to another Stat. Gain the Marine''s Trauma Response.
• Critical Success: As Success, but take an Expert Skill instead of 2 Trained Skills.
• Failure: Gain Military Training, Athletics, and 1 Trained Skill. Gain the Marine''s Trauma Response.
• Critical Failure: You were killed in action.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(446,149,'ru','Запись на Военную Службу','Военная Подготовка бесплатна, но требует подписания 6-летнего контракта с местным полком Колониальных Морских Пехотинцев. Совершите Проверку Боя, чтобы узнать, что произошло во время службы:

• Успех: Получите Военную Подготовку, Атлетику и 2 Начальных Навыка. +10 к Бою, -10 к другому Параметру. Приобретите Реакцию на Травму Морпеха.
• Критический Успех: Как Успех, но вместо 2 Начальных Навыков можно взять Экспертный.
• Провал: Получите Военную Подготовку, Атлетику и 1 Начальный Навык. Приобретите Реакцию на Травму Морпеха.
• Критический Провал: Убиты в бою.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(447,149,'ua','Запис на Військову Службу','Військова Підготовка безкоштовна, але вимагає підписання 6-річного контракту з місцевим полком Колоніальних Морських Піхотинців. Зробіть Перевірку Бою, щоб дізнатися, що відбулося під час служби:

• Успіх: Отримайте Військову Підготовку, Атлетику та 2 Початкових Навики. +10 до Бою, -10 до іншого Параметра. Отримайте Реакцію на Травму Морського Піхотинця.
• Критичний Успіх: Як Успіх, але замість 2 Початкових Навиків можна взяти Експертний.
• Провал: Отримайте Військову Підготовку, Атлетику та 1 Початковий Навик. Отримайте Реакцію на Травму Морського Піхотинця.
• Критичний Провал: Загинули у бою.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(448,150,'en','Atmospheres','Toxic Atmosphere: The planet''s atmosphere is not fit to breathe but is otherwise safe. A rebreather or armor with its own oxygen supply is required. Without these, characters take 1d10 DMG per round, Body Save for half.

Corrosive Atmosphere: The planet''s atmosphere is deadly and destructive. It deals Damage every round while on it. This ranges from 1 DMG/round (Mildly Corrosive) to 10 DMG/round (Highly Corrosive). Anything higher is simply impossible to safely traverse without specialized equipment and armor.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(449,150,'ru','Атмосферы','Токсичная атмосфера: Атмосфера планеты непригодна для дыхания, но в остальном безопасна. Требуется респиратор или броня с собственным запасом кислорода. Без них персонажи получают 1d10 урона в раунд, Спасбросок Тела для половины урона.

Разъедающая атмосфера: Атмосфера планеты смертоносна и разрушительна. Она наносит урон каждый раунд нахождения на ней. От 1 урона/раунд (Слегка разъедающая) до 10 урона/раунд (Сильно разъедающая). Всё, что выше, невозможно безопасно пройти без специального снаряжения и брони.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(450,150,'ua','Атмосфери','Токсична атмосфера: Атмосфера планети непридатна для дихання, але в іншому безпечна. Потрібен респіратор або броня з власним запасом кисню. Без них персонажі отримують 1d10 шкоди за раунд, Порятунок Тіла для половини шкоди.

Роз''їдаюча атмосфера: Атмосфера планети смертоносна і руйнівна. Вона завдає шкоди кожен раунд перебування на ній. Від 1 шкоди/раунд (Злегка роз''їдаюча) до 10 шкоди/раунд (Сильно роз''їдаюча). Все, що вище, неможливо безпечно пройти без спеціального спорядження та броні.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(451,151,'en','Bleeding','Some weapons or Wounds cause characters to Bleed. This means they take 1 Damage every round until the bleeding is stopped. Bleeding is cumulative — if a character is Bleeding 1 DMG/round and gains Bleeding +1, they now take 2 DMG/round.

Bleeding damage ignores armor and damage reduction.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(452,151,'ru','Кровотечение','Некоторое оружие или Раны заставляют персонажей Истекать кровью. Это означает, что они получают 1 урон каждый раунд, пока кровотечение не остановлено. Кровотечение суммируется — если персонаж получает 1 урон/раунд от кровотечения и получает Кровотечение +1, теперь он получает 2 урона/раунд.

Урон от кровотечения игнорирует броню и снижение урона.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(453,151,'ua','Кровотеча','Деяка зброя або Рани змушують персонажів Кровоточити. Це означає, що вони отримують 1 шкоди щороку, поки кровотечу не зупинено. Кровотеча сумується — якщо персонаж отримує 1 шкоди/раунд від кровотечі та отримує Кровотеча +1, тепер він отримує 2 шкоди/раунд.

Шкода від кровотечі ігнорує броню та зниження шкоди.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(454,152,'en','Cryosickness','To endure long space journeys or hyperspace jumps, crews use cryopods — coffin-like capsules that freeze them in suspended animation called cryosleep. While in cryosleep, vitals are preserved and aging slows down.

However, upon awakening, you experience a hangover-like feeling called cryosickness, which causes sluggishness and slow reflexes. While cryosick you suffer [-] on all rolls for 1 week. Upgraded cryochambers can help mitigate these effects, and a Stimpak can cure them instantly.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(455,152,'ru','Криозаморозка','Для длительных космических путешествий или прыжков сквозь гиперпространство экипажи используют криокапсулы — гробоподобные камеры, замораживающие их в состоянии криосна. Во время криосна жизненные показатели сохраняются, а старение замедляется.

Однако при пробуждении ощущается похмельеподобное состояние — криобользнь, вызывающая вялость и замедленные рефлексы. При криоболезни вы страдаете [-] на все броски в течение 1 недели. Улучшенные криокамеры помогают смягчить эти эффекты, а Стимпак излечивает их мгновенно.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(456,152,'ua','Кріохвороба','Для тривалих космічних подорожей або стрибків крізь гіперпростір екіпажі використовують кріокапсули — гробоподібні камери, що заморожують їх у стані кріосну. Під час кріосну життєві показники зберігаються, а старіння сповільнюється.

Однак при пробудженні відчувається схожий на похмілля стан — кріохвороба, що спричиняє млявість і сповільнені рефлекси. При кріохворобі ви страждаєте [-] на всі кидки протягом 1 тижня. Покращені кріокамери допомагають пом''якшити ці ефекти, а Стимпак лікує їх миттєво.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(457,153,'en','Food & Water','Humans can survive roughly 3 weeks without food. After 24 hours without food, roll at Disadvantage on all rolls.

For the bare minimum of survival you need 1 liter of water a day. However, at this level, any strenuous activity (e.g., running, combat, making mechanical repairs) forces you to make a Body Save or pass out. When water is scarce and you''re tracking it this closely, you''re at Disadvantage on all rolls.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(458,153,'ru','Еда и Вода','Люди могут прожить примерно 3 недели без еды. После 24 часов без еды бросайте с Помехой на все броски.

Для минимального выживания вам нужен 1 литр воды в день. Однако на этом уровне любая напряжённая деятельность (например, бег, бой, механические ремонты) вынуждает делать Спасбросок Тела или потерять сознание. Когда воды мало и вы тщательно её отслеживаете, вы бросаете с Помехой на все броски.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(459,153,'ua','Їжа та Вода','Люди можуть прожити приблизно 3 тижні без їжі. Після 24 годин без їжі кидайте з Перешкодою на всі кидки.

Для мінімального виживання вам потрібен 1 літр води на день. Однак на цьому рівні будь-яка напружена діяльність (наприклад, біг, бій, механічні ремонти) змушує робити Порятунок Тіла або знепритомніти. Коли води мало і ви ретельно її відстежуєте, ви кидаєте з Перешкодою на всі кидки.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(460,154,'en','Oxygen','In space you can last 15 seconds without oxygen before falling unconscious. After passing out, you can survive for 1d5 minutes before dying.

If all of a ship''s Life Support System goes offline, roll 1d10 and multiply it by the maximum crew capacity. This is the remaining oxygen supply.

Every 24 hours, subtract the total number of breathing crewmembers from the remaining oxygen supply. Crewmembers engaging in strenuous activity further reduce the supply by 2 each.

• When oxygen supply < 2× breathing passengers: all rolls at Disadvantage (headaches, fatigue, anxiety, clumsiness).
• When oxygen supply < total breathing passengers: every breathing passenger must make a Body Save or make a Death Save.
• When oxygen runs out: 15 seconds before unconscious, then 1d5 minutes before death.

Androids do not consume oxygen. Those in cryosleep do not reduce the oxygen supply.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(461,154,'ru','Кислород','В космосе без кислорода можно продержаться 15 секунд до потери сознания. После потери сознания можно прожить 1d5 минут.

Если вся система жизнеобеспечения корабля отключится, бросьте 1d10 и умножьте на максимальную вместимость экипажа. Это оставшийся запас кислорода.

Каждые 24 часа вычитайте из запаса кислорода общее число дышащих членов экипажа. Члены экипажа, занятые напряжённой деятельностью, дополнительно сокращают запас на 2 каждый.

• Когда запас < 2× дышащих пассажиров: все броски с Помехой.
• Когда запас < числа дышащих пассажиров: каждый делает Спасбросок Тела или Спасбросок от Смерти.
• Когда кислород заканчивается: 15 секунд до потери сознания, затем 1d5 минут до смерти.

Андроиды не потребляют кислород. Те, кто в криосне, не сокращают запас кислорода.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(462,154,'ua','Кисень','У космосі без кисню можна протриматися 15 секунд до втрати свідомості. Після втрати свідомості можна прожити 1d5 хвилин.

Якщо вся система життєзабезпечення корабля відключиться, киньте 1d10 і помножте на максимальну місткість екіпажу. Це залишковий запас кисню.

Кожні 24 години віднімайте від запасу кисню загальну кількість дихаючих членів екіпажу. Члени екіпажу, зайняті напруженою діяльністю, додатково скорочують запас на 2 кожен.

• Коли запас < 2× дихаючих пасажирів: всі кидки з Перешкодою.
• Коли запас < кількості дихаючих пасажирів: кожен робить Порятунок Тіла або Порятунок від Смерті.
• Коли кисень закінчується: 15 секунд до втрати свідомості, потім 1d5 хвилин до смерті.

Андроїди не споживають кисень. Ті, хто у кріосні, не скорочують запас кисню.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(463,155,'en','Radiation','Whether it''s cosmic rays, an engine leak, or some previously undiscovered asteroid ore, radiation can kill you if you''re not careful.

Armor with Radiation Shielding (e.g., the Hazard Suit) blocks all three levels of radiation.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(464,155,'ru','Радиация','Будь то космические лучи, утечка двигателя или неизвестная asteroiдная руда, радиация может убить вас, если вы не будете осторожны.

Броня с радиационной защитой (например, Защитный Костюм) блокирует все три уровня радиации.',NULL,'["Уровень 1 — Фоновое: Обычное повседневное излучение, космические лучи. Немедленного ущерба нет. Возможные долгосрочные последствия (рак и т. д.).", "Уровень 2 — Острое: Незащищённые реакторы, варп-ядра. Уменьшайте все Характеристики и Спасброски на 1 каждый раунд.", "Уровень 3 — Летальное: Ядерное оружие, прямой контакт с варп-ядрами. Каждый раунд: Спасбросок Тела или смертельная доза (смерть через 1d5 дней)."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(465,155,'ua','Радіація','Будь то космічні промені, витік двигуна або невідома астероїдна руда, радіація може вбити вас, якщо ви не будете обережні.

Броня з радіаційним захистом (наприклад, Захисний Костюм) блокує всі три рівні радіації.',NULL,'["Рівень 1 — Фонове: Звичайне повсякденне випромінювання, космічні промені. Негайної шкоди немає. Можливі довгострокові наслідки (рак тощо).", "Рівень 2 — Гостре: Незахищені реактори, варп-ядра. Зменшуйте всі Характеристики та Рятівні на 1 кожен раунд.", "Рівень 3 — Летальне: Ядерна зброя, прямий контакт з варп-ядрами. Кожен раунд: Рятівний Тіла або летальна доза (смерть через 1d5 днів)."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(466,156,'en','Stimpak Overdose','Excessive use of stimpaks (and other dangerous drugs) carries a risk of overdose. Whenever a character takes more than one stimpak in a day, roll 1d10. If you roll under the amount of doses taken in the past 24 hours, make a Death Save.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(467,156,'ru','Передозировка Стимпака','Чрезмерное использование стимпаков (и других опасных препаратов) несёт риск передозировки. Когда персонаж принимает более одного стимпака в день, бросьте 1d10. Если результат меньше количества доз, принятых за последние 24 часа, сделайте Спасбросок от Смерти.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(468,156,'ua','Передозування Стімпака','Надмірне використання стімпаків (та інших небезпечних препаратів) несе ризик передозування. Коли персонаж приймає більше одного стімпака на день, киньте 1d10. Якщо результат менше кількості доз, прийнятих за останні 24 години, зробіть Порятунок від Смерті.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(469,157,'en','Temperature','In most cases, a hot or cold climate has no notable effects. However, in places of extreme cold or heat, make Body Saves every hour or succumb to Extreme Cold/Heat.

Extreme Cold: In sub-zero temperatures, hypothermia and frostbite can set in within 10–30 minutes for those not dressed appropriately. To survive you must bring your body up to its normal temperature. Hypothermia can kill within 30 minutes to 6 hours.

Extreme Heat: Extreme heat over 100°F/40°C can cause heat stroke and kill within hours. Victims must move to a cooler location immediately to get their temperature down.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(470,157,'ru','Температура','В большинстве случаев жаркий или холодный климат не имеет заметных эффектов. Однако в местах с экстремальным холодом или жарой делайте Спасброски Тела каждый час или поддайтесь Экстремальному Холоду/Жаре.

Экстремальный холод: При температурах ниже нуля гипотермия и обморожение могут наступить в течение 10–30 минут у тех, кто не одет соответствующим образом. Для выживания нужно поднять температуру тела до нормы. Гипотермия может убить в течение 30 минут – 6 часов.

Экстремальная жара: Жара выше 40°C может вызвать тепловой удар и убить в течение часов. Пострадавшие должны немедленно перейти в более прохладное место.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(471,157,'ua','Температура','У більшості випадків спекотний або холодний клімат не має помітних ефектів. Однак у місцях з екстремальним холодом або спекою робіть Порятунки Тіла щогодини або піддайтеся Екстремальному Холоду/Спеці.

Екстремальний холод: При температурах нижче нуля гіпотермія та обмороження можуть настати протягом 10–30 хвилин у тих, хто не одягнений відповідно. Для виживання потрібно підняти температуру тіла до норми. Гіпотермія може вбити протягом 30 хвилин – 6 годин.

Екстремальна спека: Спека вище 40°C може спричинити тепловий удар і вбити протягом годин. Постраждалі повинні негайно перейти в більш прохолодне місце.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(472,158,'en','Short-Term Recovery','Once per day, whenever resting, a character''s body attempts to heal itself naturally. After 6+ hours of rest make a Body Save. If successful, reset Health to its Maximum. Wounds, however, remain the same.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(473,158,'ru','Краткосрочное Восстановление','Один раз в день, при отдыхе, тело персонажа пытается восстановиться естественным образом. После 6+ часов отдыха сделайте Спасбросок Тела. При успехе сбросьте Здоровье до максимума. Однако Раны остаются прежними.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(474,158,'ua','Короткострокове Відновлення','Один раз на день, під час відпочинку, тіло персонажа намагається відновитися природним чином. Після 6+ годин відпочинку зробіть Порятунок Тіла. При успіху скиньте Здоров''я до максимуму. Однак Рани залишаються незмінними.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(475,159,'en','Long-Term Recovery','Recovering Wounds, Conditions, or losses to Stats and Saves takes a longer time. See the Medical Treatments table for available treatments — these require professional facilities at a Port.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(476,159,'ru','Долгосрочное Восстановление','Восстановление Ран, Состояний или потерь Параметров и Спасбросков занимает больше времени. Смотрите таблицу Медицинских Процедур для доступных методов лечения — они требуют профессиональных учреждений в Порту.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(477,159,'ua','Довгострокове Відновлення','Відновлення Ран, Станів або втрат Параметрів та Порятунків займає більше часу. Дивіться таблицю Медичних Процедур для доступних методів лікування — вони вимагають професійних закладів у Порту.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(478,160,'en','Artificial Wellness Counselor','1 hour session (max 1 per week). Restores 1 Sanity Save. 1% chance you gain a random Condition.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(479,160,'ru','Искусственный Консультант по Благополучию','Сеанс 1 час (максимум 1 в неделю). Восстанавливает 1 Спасбросок Рассудка. 1% шанс получить случайное Состояние.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(480,160,'ua','Штучний Консультант з Добробуту','Сеанс 1 годину (максимум 1 на тиждень). Відновлює 1 Порятунок Розуму. 1% шанс отримати випадковий Стан.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(481,161,'en','Cognitive Defragmentation','24 hour surgical treatment. Removes 1 Condition. 1% chance of total amnesia. [-] on Intellect Checks, Sanity Saves, and Fear Saves for 4 weeks.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(482,161,'ru','Когнитивная Дефрагментация','24-часовая хирургическая процедура. Убирает 1 Состояние. 1% шанс полной амнезии. [-] на Проверки Интеллекта, Спасброски Рассудка и Страха на 4 недели.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(483,161,'ua','Когнітивна Дефрагментація','24-годинна хірургічна процедура. Прибирає 1 Стан. 1% шанс повної амнезії. [-] на Перевірки Інтелекту, Порятунки Розуму та Страху на 4 тижні.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(484,162,'en','Deep Tissue Nanogel Massage','1 hour session (max 1 per week). Reduces Minimum Stress by 1. [-] on all actions for 24 hours.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(485,162,'ru','Глубокотканный Наногелевый Массаж','Сеанс 1 час (максимум 1 в неделю). Уменьшает Минимальный Стресс на 1. [-] на все действия в течение 24 часов.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(486,162,'ua','Глибокотканинний Наногелевий Масаж','Сеанс 1 годину (максимум 1 на тиждень). Зменшує Мінімальний Стрес на 1. [-] на всі дії протягом 24 годин.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(487,163,'en','Immersive Slicksim Therapy','4 hour virtual treatment. Restores either 1d10 Combat or 1d10 Fear Save. 1% chance the character is stuck in the immersion for 1d10 days and loses 1d5 Sanity Save.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(488,163,'ru','Иммерсивная Слик-Сим Терапия','4-часовая виртуальная процедура. Восстанавливает либо 1d10 Бой, либо 1d10 Спасбросок Страха. 1% шанс, что персонаж застрянет в иммерсии на 1d10 дней и потеряет 1d5 Спасброска Рассудка.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(489,163,'ua','Іммерсивна Слік-Сім Терапія','4-годинна віртуальна процедура. Відновлює або 1d10 Бій, або 1d10 Порятунок Страху. 1% шанс, що персонаж застрягне в іммерсії на 1d10 днів і втратить 1d5 Порятунку Розуму.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(490,164,'en','Medpod','Week long treatment spent in the pod. Restores 1 Wound. Does not restore lost limbs or digits.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(491,164,'ru','Медкапсула','Недельное лечение в капсуле. Восстанавливает 1 Рану. Не восстанавливает утраченные конечности или пальцы.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(492,164,'ua','Медкапсула','Тижневе лікування в капсулі. Відновлює 1 Рану. Не відновлює втрачені кінцівки або пальці.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(493,165,'en','Pseudoflesh Injection','8 hour surgical treatment. Restores either 2d10 Speed, 2d10 Strength, 2d10 Body Save, or all Wounds. At [-] on all rolls for 2 weeks, plus an additional 4 weeks of convalescent recovery required.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(494,165,'ru','Инъекция Псевдоплоти','8-часовая хирургическая операция. Восстанавливает либо 2d10 Скорость, 2d10 Силу, 2d10 Спасбросок Тела, либо все Раны. [-] на все броски в течение 2 недель, плюс дополнительные 4 недели реабилитации.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(495,165,'ua','Ін''єкція Псевдоплоті','8-годинна хірургічна операція. Відновлює або 2d10 Швидкість, 2d10 Силу, 2d10 Порятунок Тіла, або всі Рани. [-] на всі кидки протягом 2 тижнів, плюс додаткові 4 тижні реабілітації.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(496,166,'en','Psychosurgery','8 hour surgical treatment. Restores either Intellect, Sanity Save, or Fear Save to their maximum, or reduces Minimum Stress to 2. At [-] on all rolls for 4 weeks.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(497,166,'ru','Психохирургия','8-часовая хирургическая операция. Восстанавливает Интеллект, Спасбросок Рассудка или Страха до максимума, либо снижает Минимальный Стресс до 2. [-] на все броски в течение 4 недель.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(498,166,'ua','Психохірургія','8-годинна хірургічна операція. Відновлює Інтелект, Порятунок Розуму або Страху до максимуму, або зменшує Мінімальний Стрес до 2. [-] на всі кидки протягом 4 тижнів.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(499,167,'en','Port Classes','There are five basic classes of Port based on their safety, importance, and affluence.

X-Class: Notorious criminal settlements and pirate bases. Beyond the reach of the Company — much more free and much more dangerous.

C-Class: Rundown, out-of-the-way outposts, refueling stations, and forward military posts. Found on any frontier settlement or Rimspace backworld, minimally staffed and minimally supplied.

B-Class: Blue-collar industrial stations and large-scale military installations. Build ships, garrison troops, mine ore, and handle all the heavy industry required to keep the galaxy spinning.

A-Class: Overpopulated metropolises, trading centers, and power brokers. House millions and contain everything you''d find in a planetside city, and more if you know where to look.

S-Class: Luxurious pleasure spas and restricted-access palatial estates of the uber-wealthy. The rare gems of the void. Heavily guarded, invite only.

Port classes can also designate planetside cities (or districts/neighborhoods) for the purposes of Shore Leave.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(500,167,'ru','Классы Портов','Существует пять основных классов портов, основанных на безопасности, важности и зажиточности.

X-класс: Печально известные криминальные поселения и пиратские базы. За пределами влияния Корпорации — много больше свободы и много больше опасности.

C-класс: Захолустые заставы на отшибе, заправочные станции, передовые военные посты.

B-класс: Рабочие промышленные станции и крупные военные установки. Строят корабли, добывают руду и обеспечивают тяжёлую промышленность.

A-класс: Перенаселённые мегаполисы, торговые центры и центры власти. Содержат миллионы жителей и всё, что вы ожидаете найти.

S-класс: Роскошные курорты и элитные поместья ультрабогатых. Редкие драгоценности пустоты. Сильная охрана, только по приглашениям.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(501,167,'ua','Класи Портів','Існує п''ять основних класів портів, заснованих на безпеці, важливості та зажитковості.

X-клас: Гучно відомі кримінальні поселення та піратські бази. За межами впливу Корпорації — багато більше свободи і багато більше небезпеци.

C-клас: Захолустілі форпости, заправні станції, передові військові пости.

B-клас: Робітничі промислові станції та великі військові установки. Будують кораблі, видобувають руду і забезпечують важку промисловість.

A-клас: Перенаселені мегаполіси, торгові центри та центри влади. Містять мільйони мешканців і все, що ви сподіваєтесь знайти.

S-клас: Розкішні курорти та елітні резиденції ультрабагатійських. Рідкісні драгоцінності порожнечини. Сильна охорона, тільки за запрошеннями.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(502,168,'en','Shore Leave','Between contracts, characters can take Shore Leave and attempt to convert accumulated Stress into improved Saves.

How to take Shore Leave:
1. Pay the Shore Leave cost at any relatively safe Port.
2. Make a Sanity Save.
   Success: Convert some Stress into improved Saves (each point of Stress = +1 to any Save). Whatever Stress you don''t convert is relieved, setting back to Minimum Stress.
   Critical Success: Convert the maximum amount for that port, relieve the rest.
   Failure: Don''t convert any Stress, but relieve all of it (back to Minimum Stress). Then gain 1 Stress for failing the Sanity Save.
   Critical Failure: Don''t convert or relieve any Stress. Make a Panic Check.

Shore Leave costs and Stress converted:
X-Class: 1d100 x 10kcr — convert 2d10[+] Stress
C-Class: 2d10 x 100cr — convert 1d5 Stress
B-Class: 2d10 x 1kcr  — convert 1d10 Stress
A-Class: 2d10 x 10kcr — convert 2d10 Stress
S-Class: 2d10 x 100kcr — convert All Stress

Duration: Characters need roughly 2d10 days (a long weekend to two-week vacation) to benefit from Shore Leave. Less time may incur penalties.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(503,168,'ru','Береговой Отпуск','Между контрактами персонажи могут взять Береговой Отпуск и попытаться преобразовать накопленный Стресс в улучшенные Спасброски.

Как взять Береговой Отпуск:
1. Оплатите стоимость Берегового Отпуска в любом относительно безопасном Порту.
2. Сделайте Спасбросок Рассудка.
   Успех: Преобразуйте часть Стресса в улучшенные Спасброски. Остаток Стресса снимается.
   Критический успех: Максимальное преобразование Стресса, остаток снимается.
   Провал: Стресс не преобразуется, но снимается до минимума. Получаете 1 Стресс за провальный Спасбросок.
   Критический провал: Ничего не преобразуется и не снимается. Сделайте Проверку на Панику.

Стоимость Берегового Отпуска:
X-класс: 1d100 x 10kcr — преобразует 2d10[+] Стресса
C-класс: 2d10 x 100cr — преобразует 1d5 Стресса
B-класс: 2d10 x 1kcr — преобразует 1d10 Стресса
A-класс: 2d10 x 10kcr — преобразует 2d10 Стресса
S-класс: 2d10 x 100kcr — преобразует весь Стресс',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(504,168,'ua','Берегова Відпустка','Між контрактами персонажі можуть взяти Берегову Відпустку і спробувати перетворити накопичений Стрес в поліпшені Порятунки.

Як взяти Берегову Відпустку:
1. Оплатіть вартість Берегової Відпустки в будь-якому відносно безпечному Порту.
2. Зробіть Порятунок Розуму.
   Успіх: Перетворіть частину Стресу в поліпшені Порятунки. Залишок Стресу знімається.
   Критичний успіх: Максимальне перетворення, залишок знімається.
   Провал: Стрес не перетворюється, але знімається до мінімуму. Отримуєте 1 Стрес за провалений Порятунок.
   Критичний провал: Нічого не перетворюється і не знімається. Зробіть Перевірку на Паніку.

Вартість Берегової Відпустки:
X-клас: 1d100 x 10kcr — перетворює 2d10[+] Стресу
C-клас: 2d10 x 100cr — перетворює 1d5 Стресу
B-клас: 2d10 x 1kcr — перетворює 1d10 Стресу
A-клас: 2d10 x 10kcr — перетворює 2d10 Стресу
S-клас: 2d10 x 100kcr — перетворює весь Стрес',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(505,169,'en','Contractor Stats','Contractors are much simpler characters with only four Stats:

Combat: Works exactly like the Combat Stat — how good they are in a fight.

Instinct: A catchall Stat for Fear, Sanity, Body, Speed, Intellect, and everything else.

Max Wounds: Contractors don''t track Health per Wound. Instead, any Damage they take counts as a Wound. If they take Wounds equal to their Max Wounds, they die.

Loyalty: A Save rolled whenever the contractor must choose between what''s best for them and what''s best for you. Success: they help you out. Failure: they help themselves. Each contractor starts with a Loyalty Save of 2d10+10, rolled after they are hired.

Motivation: A contractor''s motivation always supersedes any sense of loyalty. Not every contractor needs a motivation — just notable ones. Contractors always fail Loyalty Saves when their motivation conflicts with yours.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(506,169,'ru','Параметры Наемника','Наемники имеют только четыре Параметра:

Бой: Работает точно так же, как параметр Бой — насколько хорошо он воюет.

Инстинкт: Обобщённый параметр для Страха, Рассудка, Тела, Скорости, Интеллекта и всего остального.

Макс. Раны: Наемники не отслеживают Здоровье по Ранам. Любой полученный урон считается за Рану. Если полученные Раны равны Макс. Ранам — он умирает.

Лояльность: Спасбросок, брасаемый при конфликте интересов. Успех — помогает вам. Провал — помогает себе. Лояльность: 2d10+10 в начале.

Мотивация: Всегда превалирует над лояльностью. Наемники всегда проваливают Спасбросок Лояльности, когда мотивация в конфликте.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(507,169,'ua','Параметри Найманця','Найманці мають лише чотири Параметри:

Бій: Працює так само, як параметр Бій — наскільки добре він воює.

Інстинкт: Узагальнений параметр для Страху, Розуму, Тіла, Швидкості, Інтелекту та всього іншого.

Макс. Ран: Найманці не стежать Здоров''я за Ранами. Будь-яка отримана Шкода рахується як Рана. Якщо Рани рівні Макс. Ранам — вмирає.

Лояльність: Порятунок, що кидається при конфлікті інтересів. Успіх — допомагає вам. Провал — допомагає собі. Лояльність: 2d10+10 на початку.

Мотивація: Завжди переважає над лояльністю. Найманці завжди провалюють Порятунок Лояльності, коли мотивація конфліктує.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(508,170,'en','Hiring Contractors','Contractors are paid a monthly salary at the beginning of every month. Additionally, they usually demand hazard pay (1d5 months of extra pay) any time they engage in life-threatening danger as a result of the job.

Non-payment or partial payment results in a Loyalty Save [-].

Contractors always indicate a beneficiary who seeks any payments owed in the event of their death.

Improving Loyalty: Contractors who survive a job and are paid in full increase their Loyalty by 1. Increases of 1d5 or 1d10 should be reserved for extreme circumstances (like saving the Contractor''s life or splitting large paydays with them).

Equipping Contractors: Contractors generally have the basic tools, weapons, and armor required to do their job. If necessary, you can roll a Loadout for them.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(509,170,'ru','Найм Наемников','Наемники получают ежемесячную зарплату в начале каждого месяца. Кроме того, они обычно требуют хазардных выплат (1d5 мес. доп. оплаты) при участии в опасных для жизни операциях.

Невыплата или неполная оплата дают [-] на Спасбросок Лояльности.

Наемники всегда указывают лицо, которое получит выплаты в случае их гибели.

Повышение Лояльности: Выжившие и получившие полную оплату наемники получают +1 к Лояльности.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(510,170,'ua','Найм Найманців','Найманці отримують щомісячну зарплату на початку кожного місяця. Крім того, вони зазвичай вимагають надбавку за небезпечність (1d5 міс. дод. оплати) при участі в небезпечних операціях.

Невиплата або неповна оплата дають [-] на Порятунок Лояльності.

Найманці завжди вказують особу, яка отримає виплати у разі їхньої смерті.

Підвищення Лояльності: Найманці, які вижили і отримали повну оплату, отримують +1 до Лояльності.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(511,171,'en','Contractors Table','Roll d100 to hire a random contractor. Stats shown are typical; the Warden may adjust. Loyalty Save (2d10+10) is rolled after hiring.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(512,171,'ru','Таблица Наемников','Бросьте d100, чтобы нанять случайного наемника. Спасбросок Лояльности (2d10+10) бросается после найма.',NULL,'["Археолог (6 тыс. кр./мес. | Бой 20, Инстинкт 15, Раны 1) — Тайно расследует корпоративное сокрытие.", "Астероидный Шахтёр (2 тыс. кр./мес. | Бой 25, Инстинкт 25, Раны 2) — Отправляет деньги домой семье.", "Андроид (6 тыс. кр./мес. | Бой 20, Инстинкт 35, Раны 2) — Срочно нужно расплатиться с ростовщиком.", "Телохранитель (2 тыс. кр./мес. | Бой 30, Инстинкт 25, Раны 2) — Не может долго оставаться на одном месте.", "Капитан (10 тыс. кр./мес. | Бой 30, Инстинкт 40, Раны 3) — Слышит зов от существа, которое не может объяснить.", "Капеллан (750 кр./мес. | Бой 10, Инстинкт 20, Раны 2) — Использует вас/ваш корабль для контрабанды.", "Корпоративный Фиксер (24 тыс. кр./мес. | Бой 15, Инстинкт 30, Раны 1) — Месть.", "Доктор (8 тыс. кр./мес. | Бой 15, Инстинкт 25, Раны 1) — Тайно мошенник без других навыков.", "Инженер (7 тыс. кр./мес. | Бой 20, Инстинкт 25, Раны 2) — Оплачивает медицинские счета близкого человека.", "Хакер (8 тыс. кр./мес. | Бой 15, Инстинкт 30, Раны 1) — Тайно шпион конкурирующей корпорации.", "Морпех (рядовой) (1,5 тыс. кр./мес. | Бой 30, Инстинкт 25, Раны 2) — Нужно расплатиться со штрафом или судебным залогом.", "Морпех (офицер) (3,5 тыс. кр./мес. | Бой 35, Инстинкт 35, Раны 3) — Тайная полиция под прикрытием, расследует ваш экипаж.", "Пилот (3 тыс. кр./мес. | Бой 15, Инстинкт 25, Раны 1) — В огромном долгу перед могущественным преступным синдикатом.", "Первопроходец (1,5 тыс. кр./мес. | Бой 25, Инстинкт 25, Раны 1) — Взял деньги и сбежал с прошлой работы.", "Учёный (4 тыс. кр./мес. | Бой 15, Инстинкт 10, Раны 1) — Родственник взят в заложники, нужен выкуп.", "Выживший (3 тыс. кр./мес. | Бой 30, Инстинкт 35, Раны 2) — Тайно охотник за головами, ищет ваш экипаж.", "Хирург (12 тыс. кр./мес. | Бой 15, Инстинкт 20, Раны 1) — Ищет достойную и славную смерть.", "Грузчик (2 тыс. кр./мес. | Бой 25, Инстинкт 25, Раны 1) — Неосознанно является носителем смертельной болезни.", "Терапевт (3 тыс. кр./мес. | Бой 10, Инстинкт 20, Раны 1) — Сбежал из корпоративного исследовательского объекта.", "Пустотный Беспризорник (100 кр./мес. | Бой 30, Инстинкт 40, Раны 2) — Тайно разыскиваемый серийный убийца."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(513,171,'ua','Таблиця Найманців','Киньте d100, щоб найняти випадкового найманця. Порятунок Лояльності (2d10+10) кидається після найму.',NULL,'["Археолог (6 тис. кр./міс. | Бій 20, Інстинкт 15, Рани 1) — Таємно розслідує корпоративне приховування.", "Астероїдний Шахтар (2 тис. кр./міс. | Бій 25, Інстинкт 25, Рани 2) — Надсилає гроші додому сім''ї.", "Андроїд (6 тис. кр./міс. | Бій 20, Інстинкт 35, Рани 2) — Терміново потрібно розплатитися з лихварем.", "Охоронець (2 тис. кр./міс. | Бій 30, Інстинкт 25, Рани 2) — Не може довго залишатися на одному місці.", "Капітан (10 тис. кр./міс. | Бій 30, Інстинкт 40, Рани 3) — Чує поклик від істоти, яку не може пояснити.", "Капелан (750 кр./міс. | Бій 10, Інстинкт 20, Рани 2) — Використовує вас/ваш корабель для контрабанди.", "Корпоративний Виконавець (24 тис. кр./міс. | Бій 15, Інстинкт 30, Рани 1) — Помста.", "Лікар (8 тис. кр./міс. | Бій 15, Інстинкт 25, Рани 1) — Таємно шахрай без інших навичок.", "Інженер (7 тис. кр./міс. | Бій 20, Інстинкт 25, Рани 2) — Оплачує медичні рахунки близької людини.", "Хакер (8 тис. кр./міс. | Бій 15, Інстинкт 30, Рани 1) — Таємно шпигун конкуруючої корпорації.", "Морпіх (рядовий) (1,5 тис. кр./міс. | Бій 30, Інстинкт 25, Рани 2) — Потрібно розплатитися зі штрафом або судовою заставою.", "Морпіх (офіцер) (3,5 тис. кр./міс. | Бій 35, Інстинкт 35, Рани 3) — Таємна поліція під прикриттям, розслідує ваш екіпаж.", "Пілот (3 тис. кр./міс. | Бій 15, Інстинкт 25, Рани 1) — У величезному боргу перед могутнім злочинним синдикатом.", "Першопрохідець (1,5 тис. кр./міс. | Бій 25, Інстинкт 25, Рани 1) — Взяв гроші і втік з попередньої роботи.", "Вчений (4 тис. кр./міс. | Бій 15, Інстинкт 10, Рани 1) — Родич узятий у заручники, потрібен викуп.", "Той, хто Вижив (3 тис. кр./міс. | Бій 30, Інстинкт 35, Рани 2) — Таємно мисливець за головами, шукає ваш екіпаж.", "Хірург (12 тис. кр./міс. | Бій 15, Інстинкт 20, Рани 1) — Шукає гідну і славну смерть.", "Вантажник (2 тис. кр./міс. | Бій 25, Інстинкт 25, Рани 1) — Несвідомо є носієм смертельної хвороби.", "Терапевт (3 тис. кр./міс. | Бій 10, Інстинкт 20, Рани 1) — Втік з корпоративного дослідницького об''єкту.", "Пустотний Безпритульний (100 кр./міс. | Бій 30, Інстинкт 40, Рани 2) — Таємно розшукуваний серійний вбивця."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(514,172,'en','Starting Scenarios','Roll 1d10 (1–10) or pick a scenario type for your first session.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(515,172,'ru','Стартовые Сценарии','Бросьте 1d10 (1–10) или выберите тип сценария для первой сессии.',NULL,'["\u0418\u0441\u0441\u043b\u0435\u0434\u0443\u0439\u0442\u0435 \u041d\u0435\u0438\u0437\u0432\u0435\u0434\u0430\u043d\u043d\u043e\u0435 \u2014 \u0420\u0430\u0437\u0432\u0435\u0434\u043a\u0430 \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e\u0439 \u043f\u043b\u0430\u043d\u0435\u0442\u044b \u0438\u043b\u0438 \u0441\u0442\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u043a\u043e\u0440\u0430\u0431\u043b\u044f. \u0411\u0435\u0437 \u043f\u043e\u0434\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u0438\u044f. \u041f\u043e\u043c\u043e\u0433\u0430\u0439 \u0432\u0430\u043c \u0431\u043e\u0433.", "\u0420\u0430\u0441\u0441\u043b\u0435\u0434\u0443\u0439\u0442\u0435 \u0421\u0442\u0440\u0430\u043d\u043d\u043e\u0439 \u0421\u043b\u0443\u0445 \u2014 \u0427\u0442\u043e-\u0442\u043e \u0436\u0438\u0432\u0451\u0442 \u0432 \u0432\u0435\u043d\u0442\u0438\u043b\u044f\u0446\u0438\u0438. \u041a\u043e\u043b\u043e\u043d\u0438\u0441\u0442\u044b \u0438\u0441\u0447\u0435\u0437\u0430\u044e\u0442. \u041e\u0442\u0434\u0435\u043b\u0438\u0442\u044c \u043f\u0440\u0430\u0432\u0434\u0443 \u043e\u0442 \u0432\u044b\u043c\u044b\u0441\u043b\u0430 \u0431\u044b\u043b\u043e \u043b\u0451\u0433\u043a\u043e\u0439 \u0447\u0430\u0441\u0442\u044c\u044e.", "\u041c\u0430\u0440\u043e\u0434\u0451\u0440\u0441\u0442\u0432\u043e \u0414\u0435relict-\u043a\u043e\u0440\u0430\u0431\u043b\u044f \u2014 \u0421\u0438\u0433\u043d\u0430\u043b \u0431\u0435\u0434\u0441\u0442\u0432\u0438\u044f \u043f\u043e\u0432\u0442\u043e\u0440\u044f\u0435\u0442\u0441\u044f. \u0421\u043a\u0430\u043d\u0435\u0440\u044b \u043d\u0435 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u044e\u0442 \u0436\u0438\u0437\u043d\u0438. \u041a\u0430\u0436\u0434\u044b\u0439 \u0431\u0440\u043e\u0448\u0435\u043d\u043d\u044b\u0439 \u043a\u043e\u0440\u0430\u0431\u043b\u044c \u0431\u0440\u043e\u0448\u0435\u043d \u043d\u0435 \u0437\u0440\u044f.", "\u0423\u043d\u0438\u0447\u0442\u043e\u0436\u044c\u0442\u0435 \u041f\u043e\u0442\u0443\u0441\u0442\u043e\u0440\u043e\u043d\u043d\u044e\u044e \u0423\u0433\u0440\u043e\u0437\u0443 \u2014 \u041d\u0438\u043a\u0442\u043e \u0431\u043e\u043b\u044c\u0448\u0435 \u043d\u0435 \u0432\u044b\u0445\u043e\u0434\u0438\u0442 \u043d\u0430\u0440\u0443\u0436\u0443. \u0423\u043d\u0438\u0447\u0442\u043e\u0436\u0438\u0442\u044c \u043b\u044e\u0431\u044b\u043c\u0438 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430\u043c\u0438. \u041f\u0440\u0438\u043d\u0435\u0441\u0442\u0438 \u0436\u0438\u0432\u043e\u0439 \u043e\u0431\u0440\u0430\u0437\u0435\u0446.", "\u041f\u043e\u0441\u0435\u0442\u0438\u0442\u0435 \u0412\u043d\u0435\u0437\u0435\u043c\u043d\u0443\u044e \u041a\u043e\u043b\u043e\u043d\u0438\u044e \u2014 \u041a\u043e\u0440\u043f\u043e\u0440\u0430\u0446\u0438\u044f \u043d\u0435 \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439 \u0441 \u0448\u0430\u0445\u0442 PK-294. \u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e.", "\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u041e\u043f\u0430\u0441\u043d\u0443\u044e \u041c\u0438\u0441\u0441\u0438\u044e \u2014 \u0420\u0435\u0431\u0451\u043d\u043e\u043a \u0442\u043e\u043f-\u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u0430 \u043f\u043e\u0445\u0438\u0449\u0435\u043d \u0441\u0435\u043a\u0442\u043e\u0439. \u0410\u043d\u0434\u0440\u043e\u0438\u0434\u044b-\u0430\u043a\u0442\u0438\u0432\u0438\u0441\u0442\u044b \u0445\u043e\u0442\u044f\u0442 \u0441\u0430\u0431\u043e\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u0432\u043e\u0434. \u0411\u0435\u0437 \u0443\u0433\u0440\u044b\u0437\u0435\u043d\u0438\u0439 \u0441\u043e\u0432\u0435\u0441\u0442\u0438.", "\u041f\u0435\u0440\u0435\u0436\u0438\u0432\u0438\u0442\u0435 \u041a\u043e\u043b\u043e\u0441\u0441\u0430\u043b\u044c\u043d\u0443\u044e \u041a\u0430\u0442\u0430\u0441\u0442\u0440\u043e\u0444\u0443 \u2014 \u041f\u043e\u043a\u0438\u043d\u0443\u0442\u044c \u043a\u043e\u0440\u0430\u0431\u043b\u044c! \u0423\u0442\u0435\u0447\u043a\u0430 \u0440\u0430\u0434\u0438\u0430\u0446\u0438\u0438 \u0438 \u0430\u043d\u043e\u043c\u0430\u043b\u0438\u0438 \u0432\u0430\u0440\u043f-\u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f. \u0414\u043e\u0431\u0440\u0430\u0442\u044c\u0441\u044f \u0434\u043e \u043a\u0430\u043f\u0441\u0443\u043b \u0434\u043e \u0442\u043e\u0433\u043e, \u043a\u0430\u043a \u0441\u0442\u0430\u043d\u0446\u0438\u044f \u0440\u0443\u0445\u043d\u0435\u0442.", "\u041e\u0442\u043a\u043b\u0438\u043a\u043d\u0438\u0442\u0435\u0441\u044c \u043d\u0430 \u0421\u0438\u0433\u043d\u0430\u043b \u0411\u0435\u0434\u0441\u0442\u0432\u0438\u044f \u2014 \u041d\u0430 \u043e\u043a\u0440\u0430\u0438\u043d\u0435 \u043f\u043e\u043c\u043e\u0449\u044c \u043d\u0438\u043a\u043e\u0433\u0434\u0430 \u043d\u0435 \u0431\u043b\u0438\u0437\u043a\u043e. \u041d\u0435 \u0432\u0441\u0435\u0433\u0434\u0430 \u043f\u043e\u043d\u044f\u0442\u044c: \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0439 \u043a\u0440\u0438\u043a \u0438\u043b\u0438 \u043b\u043e\u0432\u0443\u0448\u043a\u0430.", "\u041f\u0435\u0440\u0435\u0432\u0435\u0437\u0438\u0442\u0435 \u0426\u0435\u043d\u043d\u044b\u0439 \u0413\u0440\u0443\u0437 \u2014 \u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u2014 \u0442\u0430\u0439\u043d\u0430. \u041d\u0435 \u043e\u0442\u043a\u0440\u044b\u0432\u0430\u0442\u044c, \u043d\u0435 \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c, \u043d\u0435 \u0441\u043b\u0443\u0448\u0430\u0442\u044c \u0442\u043e, \u0447\u0442\u043e \u0432\u043d\u0443\u0442\u0440\u0438 \u0433\u043e\u0432\u043e\u0440\u0438\u0442.", "\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435 \u041a\u043e\u043d\u0442\u0430\u043a\u0442 \u0441 \u0417\u0430\u043f\u0440\u0435\u0434\u0435\u043b\u044c\u043d\u044b\u043c \u2014 \u041d\u0430\u0439\u0434\u0435\u043d\u043e \u043d\u0430 \u043a\u0440\u0430\u044e \u0441\u0438\u0441\u0442\u0435\u043c\u044b. \u0422\u044b\u0441\u044f\u0447\u0435\u043b\u0435\u0442\u043d\u0435\u0439 \u0434\u0430\u0432\u043d\u043e\u0441\u0442\u0438. \u041a\u043e\u0433\u0434\u0430 \u043f\u0440\u0438\u043b\u0435\u0442\u0435\u043b \u0437\u043e\u043d\u0434, \u043e\u043d\u043e \u043d\u0430\u0447\u0430\u043b\u043e \u0433\u0443\u0434\u0435\u0442\u044c \u043c\u0435\u043b\u043e\u0434\u0438\u044e."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(516,172,'ua','Стартові Сценарії','Киньте 1d10 (1–10) або оберіть тип сценарію для першої сесії.',NULL,'["\u0414\u043e\u0441\u043b\u0456\u0434\u0436\u0443\u0439\u0442\u0435 \u041d\u0435\u0432\u0456\u0434\u043e\u043c\u0435 \u2014 \u0420\u043e\u0437\u0432\u0456\u0434\u043a\u0430 \u043d\u0435\u0432\u0456\u0434\u043e\u043c\u043e\u0457 \u043f\u043b\u0430\u043d\u0435\u0442\u0438 \u0430\u0431\u043e \u0434\u0438\u0432\u043d\u043e\u0433\u043e \u043a\u043e\u0440\u0430\u0431\u043b\u044f. \u0411\u0435\u0437 \u043f\u0456\u0434\u043a\u0440\u0456\u043f\u043b\u0435\u043d\u043d\u044f. \u0411\u0435\u0440\u0435\u0436\u0456\u0442\u044c \u0441\u0435\u0431\u0435.", "\u0420\u043e\u0437\u0441\u043b\u0456\u0434\u0443\u0439\u0442\u0435 \u0414\u0438\u0432\u043d\u0438\u0439 \u0421\u043b\u0443\u0445 \u2014 \u0429\u043e\u0441\u044c \u0436\u0438\u0432\u0435 \u0443 \u0432\u0435\u043d\u0442\u0438\u043b\u044f\u0446\u0456\u0457. \u041a\u043e\u043b\u043e\u043d\u0456\u0441\u0442\u0438 \u0437\u043d\u0438\u043a\u0430\u044e\u0442\u044c. \u0412\u0456\u0434\u043e\u043a\u0440\u0435\u043c\u0438\u0442\u0438 \u043f\u0440\u0430\u0432\u0434\u0443 \u0432\u0456\u0434 \u0432\u0438\u0433\u0430\u0434\u043a\u0438 \u0431\u0443\u043b\u043e \u043b\u0435\u0433\u043a\u043e\u044e \u0447\u0430\u0441\u0442\u0438\u043d\u043e\u044e.", "\u041c\u0430\u0440\u043e\u0434\u0435\u0440\u0441\u0442\u0432\u043e \u043d\u0430 \u041f\u043e\u043a\u0438\u043d\u0443\u0442\u043e\u043c\u0443 \u041a\u043e\u0440\u0430\u0431\u043b\u0456 \u2014 \u0421\u0438\u0433\u043d\u0430\u043b \u043b\u0438\u0445\u0430 \u043f\u043e\u0432\u0442\u043e\u0440\u044e\u0454\u0442\u044c\u0441\u044f. \u0421\u043a\u0430\u043d\u0435\u0440\u0438 \u043d\u0435 \u043f\u043e\u043a\u0430\u0437\u0443\u044e\u0442\u044c \u0436\u043e\u0434\u043d\u043e\u0433\u043e \u0436\u0438\u0442\u0442\u044f. \u041a\u043e\u0436\u0435\u043d \u043f\u043e\u043a\u0438\u043d\u0443\u0442\u0438\u0439 \u043a\u043e\u0440\u0430\u0431\u0435\u043b\u044c \u043f\u043e\u043a\u0438\u043d\u0443\u0442\u0438\u0439 \u043d\u0435 \u043f\u0440\u043e\u0441\u0442\u043e \u0442\u0430\u043a.", "\u0417\u043d\u0438\u0449\u0442\u0435 \u041f\u043e\u0442\u043e\u0439\u0431\u0456\u0447\u043d\u0443 \u0417\u0430\u0433\u0440\u043e\u0437\u0443 \u2014 \u041d\u0456\u0445\u0442\u043e \u0431\u0456\u043b\u044c\u0448\u0435 \u043d\u0435 \u0432\u0438\u0445\u043e\u0434\u0438\u0442\u044c \u043d\u0430\u0434\u0432\u0456\u0440. \u0417\u043d\u0438\u0449\u0438\u0442\u0438 \u0431\u0443\u0434\u044c-\u044f\u043a\u0438\u043c\u0438 \u0437\u0430\u0441\u043e\u0431\u0430\u043c\u0438. \u041f\u0440\u0438\u043d\u0435\u0441\u0442\u0438 \u0436\u0438\u0432\u0438\u0439 \u0437\u0440\u0430\u0437\u043e\u043a.", "\u0412\u0456\u0434\u0432\u0456\u0434\u0430\u0439\u0442\u0435 \u041f\u043e\u0437\u0430\u0437\u0435\u043c\u043d\u0443 \u041a\u043e\u043b\u043e\u043d\u0456\u044e \u2014 \u041a\u043e\u0440\u043f\u043e\u0440\u0430\u0446\u0456\u044f \u043d\u0435 \u043e\u0442\u0440\u0438\u043c\u0443\u0454 \u043d\u043e\u0432\u0438\u043d \u0437 \u0448\u0430\u0445\u0442 PK-294. \u0412\u0456\u0434\u043d\u043e\u0432\u0456\u0442\u044c \u0432\u0438\u0440\u043e\u0431\u043d\u0438\u0446\u0442\u0432\u043e.", "\u0412\u0438\u043a\u043e\u043d\u0430\u0439\u0442\u0435 \u041d\u0435\u0431\u0435\u0437\u043f\u0435\u0447\u043d\u0443 \u041c\u0456\u0441\u0456\u044e \u2014 \u0414\u0438\u0442\u0438\u043d\u0443 \u0442\u043e\u043f-\u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u0430 \u0432\u0438\u043a\u0440\u0430\u043b\u0430 \u0441\u0435\u043a\u0442\u0430. \u0410\u043d\u0434\u0440\u043e\u0457\u0434\u0438-\u0430\u043a\u0442\u0438\u0432\u0456\u0441\u0442\u0438 \u0445\u043e\u0447\u0443\u0442\u044c \u0441\u0430\u0431\u043e\u0442\u0443\u0432\u0430\u0442\u0438 \u0437\u0430\u0432\u043e\u0434. \u0411\u0435\u0437 \u0436\u043e\u0434\u043d\u0438\u0445 \u0434\u043e\u043a\u043e\u0440\u0456\u0432 \u0441\u0443\u043c\u043b\u0456\u043d\u043d\u044f.", "\u041f\u0435\u0440\u0435\u0436\u0438\u0432\u0456\u0442\u044c \u041a\u043e\u043b\u043e\u0441\u0430\u043b\u044c\u043d\u0443 \u041a\u0430\u0442\u0430\u0441\u0442\u0440\u043e\u0444\u0443 \u2014 \u041f\u043e\u043a\u0438\u043d\u0443\u0442\u0438 \u043a\u043e\u0440\u0430\u0431\u0435\u043b\u044c! \u0412\u0438\u0442\u0456\u043a \u0440\u0430\u0434\u0456\u0430\u0446\u0456\u0457 \u0442\u0430 \u0430\u043d\u043e\u043c\u0430\u043b\u0456\u0457 \u0432\u0430\u0440\u043f-\u0434\u0432\u0438\u0433\u0443\u043d\u0430. \u0414\u0456\u0441\u0442\u0430\u0442\u0438\u0441\u044f \u043a\u0430\u043f\u0441\u0443\u043b \u0434\u043e \u0442\u043e\u0433\u043e, \u044f\u043a \u0441\u0442\u0430\u043d\u0446\u0456\u044f \u0432\u043f\u0430\u0434\u0435.", "\u0412\u0456\u0434\u0433\u0443\u043a\u043d\u0456\u0442\u044c\u0441\u044f \u043d\u0430 \u0421\u0438\u0433\u043d\u0430\u043b \u041b\u0438\u0445\u0430 \u2014 \u041d\u0430 \u043e\u043a\u0440\u0430\u0457\u043d\u0456 \u0434\u043e\u043f\u043e\u043c\u043e\u0433\u0430 \u043d\u0456\u043a\u043e\u043b\u0438 \u043d\u0435 \u0431\u043b\u0438\u0437\u044c\u043a\u043e. \u041d\u0435\u043c\u043e\u0436\u043b\u0438\u0432\u043e \u0432\u0456\u0434\u0440\u0456\u0437\u043d\u0438\u0442\u0438 \u0441\u043f\u0440\u0430\u0432\u0436\u043d\u0456\u0439 \u043a\u0440\u0438\u043a \u0432\u0456\u0434 \u043f\u0430\u0441\u0442\u043a\u0438.", "\u041f\u0435\u0440\u0435\u0432\u0435\u0437\u0456\u0442\u044c \u0426\u0456\u043d\u043d\u0438\u0439 \u0412\u0430\u043d\u0442\u0430\u0436 \u2014 \u0412\u043c\u0456\u0441\u0442 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430 \u2014 \u0442\u0430\u0454\u043c\u043d\u0438\u0446\u044f. \u041d\u0435 \u0432\u0456\u0434\u043a\u0440\u0438\u0432\u0430\u0442\u0438, \u043d\u0435 \u0441\u043a\u0430\u043d\u0443\u0432\u0430\u0442\u0438, \u043d\u0435 \u0441\u043b\u0443\u0445\u0430\u0442\u0438 \u0442\u0435, \u0449\u043e \u0432\u0441\u0435\u0440\u0435\u0434\u0438\u043d\u0456 \u0433\u043e\u0432\u043e\u0440\u0438\u0442\u044c.", "\u0412\u0441\u0442\u0430\u043d\u043e\u0432\u0456\u0442\u044c \u041a\u043e\u043d\u0442\u0430\u043a\u0442 \u0456\u0437 \u041f\u043e\u0442\u043e\u0439\u0431\u0456\u0447\u043d\u0438\u043c \u2014 \u0417\u043d\u0430\u0439\u0434\u0435\u043d\u043e \u043d\u0430 \u043a\u0440\u0430\u044e \u0441\u0438\u0441\u0442\u0435\u043c\u0438. \u0422\u0438\u0441\u044f\u0447\u043e\u043b\u0456\u0442\u043d\u044c\u043e\u0457 \u0434\u0430\u0432\u043d\u0438\u043d\u0438. \u041a\u043e\u043b\u0438 \u043f\u0440\u0438\u043b\u0435\u0442\u0456\u0432 \u0437\u043e\u043d\u0434, \u0432\u043e\u043d\u043e \u043f\u043e\u0447\u0430\u043b\u043e \u043d\u0430\u0441\u043f\u0456\u0432\u0443\u0432\u0430\u0442\u0438 \u043c\u0435\u043b\u043e\u0434\u0456\u044e."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(517,173,'en','Setting Table','Roll 1d10 (0–9) for a starting location.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(518,173,'ru','Таблица Локаций','Бросьте 1d10 (0–9) для выбора стартовой локации.',NULL,'["\u041a\u043e\u0441\u043c\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0421\u0442\u0430\u043d\u0446\u0438\u044f", "\u041d\u0430 \u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u043c \u041a\u043e\u0440\u0430\u0431\u043b\u0435", "\u0412\u043e\u0435\u043d\u043d\u044b\u0439 \u0410\u0432\u0430\u043d\u043f\u043e\u0441\u0442", "\u0422\u044e\u0440\u0435\u043c\u043d\u044b\u0439 \u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441", "\u0411\u0440\u043e\u0448\u0435\u043d\u043d\u044b\u0439 \u041a\u043e\u0441\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u041a\u043e\u0440\u0430\u0431\u043b\u044c", "\u0420\u0435\u043b\u0438\u0433\u0438\u043e\u0437\u043d\u044b\u0439 \u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441", "\u0413\u043e\u0440\u043d\u043e\u0434\u043e\u0431\u044b\u0432\u0430\u044e\u0449\u0430\u044f \u041a\u043e\u043b\u043e\u043d\u0438\u044f", "\u0418\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u041e\u0431\u044a\u0435\u043a\u0442", "\u041f\u043e\u0434\u0432\u043e\u0434\u043d\u0430\u044f \u0411\u0430\u0437\u0430", "\u041c\u0430\u0442\u0435\u0440\u0438\u043d\u0441\u043a\u0438\u0439 \u041a\u043e\u0440\u0430\u0431\u043b\u044c"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(519,173,'ua','Таблиця Локацій','Киньте 1d10 (0–9) для вибору стартової локації.',NULL,'["\u041a\u043e\u0441\u043c\u0456\u0447\u043d\u0430 \u0421\u0442\u0430\u043d\u0446\u0456\u044f", "\u041d\u0430 \u0412\u043b\u0430\u0441\u043d\u043e\u043c\u0443 \u041a\u043e\u0440\u0430\u0431\u043b\u0456", "\u0412\u0456\u0439\u0441\u044c\u043a\u043e\u0432\u0438\u0439 \u0410\u0432\u0430\u043d\u043f\u043e\u0441\u0442", "\u0422\u044e\u0440\u0435\u043c\u043d\u0438\u0439 \u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441", "\u041f\u043e\u043a\u0438\u043d\u0443\u0442\u0438\u0439 \u041a\u043e\u0441\u043c\u0456\u0447\u043d\u0438\u0439 \u041a\u043e\u0440\u0430\u0431\u0435\u043b\u044c", "\u0420\u0435\u043b\u0456\u0433\u0456\u0439\u043d\u0438\u0439 \u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441", "\u0413\u0456\u0440\u043d\u0438\u0447\u043e\u0434\u043e\u0431\u0443\u0432\u043d\u0430 \u041a\u043e\u043b\u043e\u043d\u0456\u044f", "\u0414\u043e\u0441\u043b\u0456\u0434\u043d\u0438\u0446\u044c\u043a\u0438\u0439 \u041e\u0431''\u0454\u043a\u0442", "\u041f\u0456\u0434\u0432\u043e\u0434\u043d\u0430 \u0411\u0430\u0437\u0430", "\u041c\u0430\u0442\u0435\u0440\u0438\u043d\u0441\u044c\u043a\u0438\u0439 \u041a\u043e\u0440\u0430\u0431\u0435\u043b\u044c"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(520,174,'en','Something to Survive','Create obstacles that threaten the players'' survival. Vary the types:

Environmental Hazards — Space is the most inhospitable environment. Use as a palette cleanser for violence.
• Dangerous vegetation, toxic atmosphere, radiation, zero-gravity, volcanoes, underwater locations, caves, lack of oxygen.

Violent Encounters — The most common obstacle. Use sparingly and brutally so players learn to avoid them.
• Brawls, chases, ship-to-ship combat, sieges, tactical gunfights.

Psychological Trauma — Represented by Sanity, Fear, and Stress mechanics.
• Creepy environment, darkness, loneliness, isolation, splitting the group, evidence of violence, Omens.

Resource Scarcity — Keeping resources scarce and forcing hard choices amps up tension.
• Lack of oxygen, food, ammo. Destroyed equipment. Time. Fuel. Credits.

Social Pressures — Convincing others is often the difference between living and dying.
• Good planning, convincing arguments, negotiation, favors, allies, and enemies.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(521,174,'ru','Нечто, Чтобы Выжить','Создайте препятствия, угрожающие выживанию игроков. Варьируйте типы:

Экологические Опасности — Космос — самая негостеприимная среда. Используйте как контраст к насилию.
• Опасная растительность, токсичная атмосфера, радиация, невесомость, вулканы, подводные локации, пещеры, нехватка кислорода.

Насильственные Встречи — Самое распространённое препятствие. Используйте редко и жестоко.
• Потасовки, погони, бой корабль-корабль, осады, перестрелки.

Психологическая Травма — Отражается механиками Рассудка, Страха и Стресса.
• Жуткая обстановка, темнота, одиночество, изоляция, разделение группы, следы насилия, Знамения.

Нехватка Ресурсов — Дефицит ресурсов и трудный выбор накаляют обстановку.
• Нехватка кислорода, еды, патронов. Уничтоженное оборудование. Время. Топливо. Кредиты.

Социальное Давление — Убеждение других часто решает вопрос жизни и смерти.
• Хорошее планирование, убедительные аргументы, переговоры, услуги, союзники и враги.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(522,174,'ua','Щось, Щоб Вижити','Створіть перешкоди, що загрожують виживанню гравців. Варіюйте типи:

Екологічні Небезпеки — Космос — найнегостинніше середовище. Використовуйте як контраст до насилля.
• Небезпечна рослинність, токсична атмосфера, радіація, невагомість, вулкани, підводні локації, печери, брак кисню.

Насильницькі Зустрічі — Найпоширеніша перешкода. Використовуйте рідко і жорстоко.
• Бійки, погоні, бій корабель-корабель, облоги, перестрілки.

Психологічна Травма — Відображається механіками Розуму, Страху та Стресу.
• Моторошна обстановка, темрява, самотність, ізоляція, розділення групи, сліди насилля, Знамення.

Дефіцит Ресурсів — Дефіцит ресурсів і важкий вибір нагнітають обстановку.
• Брак кисню, їжі, набоїв. Знищене обладнання. Час. Пальне. Кредити.

Соціальний Тиск — Переконання інших часто вирішує питання життя і смерті.
• Хороше планування, переконливі аргументи, переговори, послуги, союзники та вороги.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(523,175,'en','Something to Solve','Every mystery has a Question. Every puzzle is an obstacle that, when defeated, reveals a new secret. Every answer points to a new lead.

Questions:
• What happened here? — Clues at the scene reveal the truth.
• Who did it? — Whoever did it doesn''t want to be found. Ever.
• Where are they? — From missing persons to entire disappeared colonies.

Puzzle Components: use 1–2 components per puzzle. Too many components = too complicated. (See Puzzle Components table.)

Tips for good answers:
• Show the lock before the key.
• Call the same thing by two or three different names — players fill in their own backstory.
• Answers lead to new questions.
• Reveal facts, not conclusions.
• More clues than you think you need.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(524,175,'ru','Нечто, Что Решить','У каждой тайны есть Вопрос. Каждая головоломка — препятствие, которое при решении раскрывает новый секрет. Каждый ответ указывает на новую зацепку.

Вопросы:
• Что здесь произошло? — Улики на месте событий раскрывают правду.
• Кто это сделал? — Тот, кто это сделал, не хочет быть найденным. Никогда.
• Где они? — От пропавших людей до исчезнувших колоний.

Компоненты головоломки: используйте 1–2 компонента на головоломку. Слишком много = слишком сложно. (См. таблицу Компонентов Головоломок.)

Советы по хорошим ответам:
• Покажите замок до ключа.
• Называйте одно и то же разными именами — игроки сами придумают историю.
• Ответы ведут к новым вопросам.
• Раскрывайте факты, а не выводы.
• Больше улик, чем вам кажется нужным.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(525,175,'ua','Щось, Що Вирішити','У кожної таємниці є Питання. Кожна головоломка — перешкода, яка при вирішенні розкриває новий секрет. Кожна відповідь вказує на нову зачіпку.

Питання:
• Що тут сталося? — Докази на місці події розкривають правду.
• Хто це зробив? — Той, хто це зробив, не хоче бути знайденим. Ніколи.
• Де вони? — Від зниклих людей до зниклих колоній.

Компоненти головоломки: використовуйте 1–2 компоненти на головоломку. Занадто багато = занадто складно. (Дивіться таблицю Компонентів Головоломок.)

Поради щодо хороших відповідей:
• Покажіть замок до ключа.
• Називайте одне й те саме різними іменами — гравці самі придумають історію.
• Відповіді ведуть до нових питань.
• Розкривайте факти, а не висновки.
• Більше підказок, ніж вам здається потрібним.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(526,176,'en','Someone to Save','Every scenario needs someone worth saving. Design characters with clear wants and put them in peril.

Define each character by:
1. What do they think with? (fists, wallet, heart, watch?)
2. What do they want? (concrete, attainable, material goal)
3. How do the players interact with them?

Character matrix (Powerful ↔ Powerless / Helpful ↔ Unhelpful):
• Gatekeeper — powerful, unhelpful. Blocks what you want.
• Employer — powerful, neutral. You work for them.
• Benefactor — powerful, helpful. Rarest ally.
• Traitor — could be anyone. The more helpful, the worse the betrayal.
• Survivor — only cares about themselves. Help them or get out of the way.
• Expert — their power is their expertise.
• Coward — powerless, unhelpful. Completely useless.
• Victim — needs you the most.
• Drinking Buddy — would do anything; just not much they can do.
• Wildcard — unpredictable. Use sparingly.

For your first session: one Gatekeeper, one Drinking Buddy, one Survivor.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(527,176,'ru','Кого-то Спасти','Каждому сценарию нужен кто-то, кого стоит спасти. Создавайте персонажей с чёткими желаниями и ставьте их в опасность.

Определите каждого персонажа через:
1. Чем он думает? (кулаки, кошелёк, сердце, часы?)
2. Чего он хочет? (конкретная, достижимая, материальная цель)
3. Как игроки взаимодействуют с ним?

Матрица персонажей (Сильный ↔ Слабый / Полезный ↔ Бесполезный):
• Привратник — сильный, бесполезный. Блокирует то, что вам нужно.
• Работодатель — сильный, нейтральный. Вы работаете на него.
• Благодетель — сильный, полезный. Редчайший союзник.
• Предатель — может быть кем угодно. Чем полезнее, тем хуже предательство.
• Выживший — думает только о себе. Помогите или уйдите с дороги.
• Эксперт — его сила в его знаниях.
• Трус — слабый, бесполезный. Совершенно бесполезен.
• Жертва — нуждается в вас больше всего.
• Собутыльник — сделает всё, что угодно; просто мало что может.
• Непредсказуемый — хаотичен. Используйте редко.

Для первой сессии: один Привратник, один Собутыльник, один Выживший.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(528,176,'ua','Когось Врятувати','Кожен сценарій потребує когось, кого варто врятувати. Створюйте персонажів із чіткими бажаннями і ставте їх у небезпеку.

Визначте кожного персонажа через:
1. Чим він думає? (кулаки, гаманець, серце, годинник?)
2. Чого він хоче? (конкретна, досяжна, матеріальна мета)
3. Як гравці взаємодіють із ним?

Матриця персонажів (Сильний ↔ Слабкий / Корисний ↔ Некорисний):
• Воротар — сильний, некорисний. Блокує те, що вам потрібно.
• Роботодавець — сильний, нейтральний. Ви працюєте на нього.
• Благодійник — сильний, корисний. Найрідкісніший союзник.
• Зрадник — може бути ким завгодно. Що корисніший, то гірше зрадництво.
• Той, хто виживає — думає лише про себе. Допоможіть або йдіть з дороги.
• Експерт — його сила в його знаннях.
• Боягуз — слабкий, некорисний. Абсолютно марний.
• Жертва — потребує вас найбільше.
• Приятель — зробить усе що завгодно; просто мало що може.
• Непередбачуваний — хаотичний. Використовуйте рідко.

Для першої сесії: один Воротар, один Приятель, один Той, хто виживає.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(529,177,'en','Tactical Considerations','Roll 1d12 to add a tactical wrinkle to a violent encounter.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(530,177,'ru','Тактические Соображения','Бросьте 1d12, чтобы добавить тактическую изюминку к насильственной встрече.',NULL,'["\u0412\u044b\u0441\u043e\u043a\u0430\u044f \u041f\u043e\u0437\u0438\u0446\u0438\u044f \u2014 \u041e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0432\u044b\u0448\u0435 \u0434\u0440\u0443\u0433\u043e\u0439 \u0438 \u0438\u043c\u0435\u0435\u0442 \u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0438 \u0430\u0442\u0430\u043a\u0435 \u0438 \u043e\u0431\u043e\u0440\u043e\u043d\u0435.", "\u041a\u0438\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u041f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b \u2014 \u041e\u0431\u044a\u0435\u043a\u0442\u044b \u0432 \u0437\u043e\u043d\u0435 \u043c\u043e\u0433\u0443\u0442 \u043d\u0430\u043d\u0435\u0441\u0442\u0438 \u043e\u0433\u0440\u043e\u043c\u043d\u044b\u0439 \u0443\u0440\u043e\u043d, \u0440\u0435\u0437\u043a\u043e \u0438\u0437\u043c\u0435\u043d\u0438\u0432 \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u044e.", "\u041f\u0440\u043e\u0440\u044b\u0432 \u2014 \u0412\u0440\u0430\u0433 \u0433\u043b\u0443\u0431\u043e\u043a\u043e \u043e\u043a\u043e\u043f\u0430\u043b\u0441\u044f \u043d\u0430 \u0445\u043e\u0440\u043e\u0448\u043e \u0437\u0430\u0449\u0438\u0449\u0451\u043d\u043d\u043e\u0439 \u043f\u043e\u0437\u0438\u0446\u0438\u0438, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043d\u0443\u0436\u043d\u043e \u0441\u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0440\u0435\u043e\u0434\u043e\u043b\u0435\u0442\u044c.", "\u0417\u0430\u0445\u0432\u0430\u0442 \u0438 \u0423\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u2014 \u041e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0434\u043e\u043b\u0436\u043d\u0430 \u0437\u0430\u0445\u0432\u0430\u0442\u0438\u0442\u044c \u0446\u0435\u043b\u044c \u0438 \u0437\u0430\u0449\u0438\u0449\u0430\u0442\u044c \u0435\u0451 \u0434\u043e \u043f\u0440\u0438\u0445\u043e\u0434\u0430 \u043f\u043e\u0434\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u0438\u044f.", "\u0420\u0438\u0441\u043a \u042d\u0441\u043a\u0430\u043b\u0430\u0446\u0438\u0438 \u2014 \u0427\u0435\u043c \u0434\u043e\u043b\u044c\u0448\u0435 \u0434\u043b\u0438\u0442\u0441\u044f \u0441\u0442\u043e\u043b\u043a\u043d\u043e\u0432\u0435\u043d\u0438\u0435, \u0442\u0435\u043c \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u0435\u0435, \u0447\u0442\u043e \u043e\u043d\u043e \u0432\u044b\u0439\u0434\u0435\u0442 \u0438\u0437-\u043f\u043e\u0434 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044f.", "\u0417\u0430\u0441\u0430\u0434\u0430 \u2014 \u0415\u0441\u043b\u0438 \u043e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0437\u0430\u0441\u0442\u0438\u0433\u043d\u0443\u0442\u0430 \u0432\u0440\u0430\u0441\u043f\u043b\u043e\u0445, \u0441\u0442\u043e\u043b\u043a\u043d\u043e\u0432\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u0441\u044f \u0431\u044b\u0441\u0442\u0440\u043e.", "\u0421\u043a\u0440\u044b\u0442\u043d\u0430\u044f \u041c\u0438\u0441\u0441\u0438\u044f \u2014 \u0414\u043b\u044f \u043f\u0440\u0435\u0434\u043e\u0442\u0432\u0440\u0430\u0449\u0435\u043d\u0438\u044f \u044d\u0441\u043a\u0430\u043b\u0430\u0446\u0438\u0438 \u0442\u0440\u0435\u0431\u0443\u044e\u0442\u0441\u044f \u0441\u043a\u0440\u044b\u0442\u043d\u043e\u0441\u0442\u044c \u0438 \u0442\u0438\u0448\u0438\u043d\u0430.", "\u0421\u043e\u043f\u0443\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439 \u0423\u0449\u0435\u0440\u0431 \u2014 \u0412 \u0437\u043e\u043d\u0435 \u043f\u0440\u0438\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u044e\u0442 \u043c\u0438\u0440\u043d\u044b\u0435 \u0436\u0438\u0442\u0435\u043b\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043d\u0443\u0436\u043d\u043e \u0443\u0447\u0438\u0442\u044b\u0432\u0430\u0442\u044c \u2014 \u0432\u0440\u0430\u0433\u0438 \u043c\u043e\u0433\u0443\u0442 \u0438\u0445 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c.", "\u041e\u043f\u0430\u0441\u043d\u0430\u044f \u0417\u043e\u043d\u0430 \u2014 \u0421\u0442\u043e\u043b\u043a\u043d\u043e\u0432\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0438\u0441\u0445\u043e\u0434\u0438\u0442 \u0432 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e\u0439 \u0437\u043e\u043d\u0435; \u0432\u044b\u0445\u043e\u0434 \u0437\u0430 \u0435\u0451 \u043f\u0440\u0435\u0434\u0435\u043b\u044b \u0433\u0440\u043e\u0437\u0438\u0442 \u0443\u0440\u043e\u043d\u043e\u043c \u0438\u043b\u0438 \u0441\u043c\u0435\u0440\u0442\u044c\u044e.", "\u041a\u043b\u044e\u0447\u0435\u0432\u0430\u044f \u0426\u0435\u043b\u044c \u2014 \u0421\u0442\u043e\u043b\u043a\u043d\u043e\u0432\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u043d\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f, \u043a\u0430\u043a \u0442\u043e\u043b\u044c\u043a\u043e \u043a\u043b\u044e\u0447\u0435\u0432\u0430\u044f \u0446\u0435\u043b\u044c \u0434\u043e\u0441\u0442\u0438\u0433\u043d\u0443\u0442\u0430, \u0437\u0430\u0445\u0432\u0430\u0447\u0435\u043d\u0430 \u0438\u043b\u0438 \u0443\u043d\u0438\u0447\u0442\u043e\u0436\u0435\u043d\u0430.", "\u041f\u043e\u0433\u043e\u043d\u044f \u0438 \u0423\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u2014 \u041e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0441\u0442\u0440\u0435\u043c\u0438\u0442\u0441\u044f \u043f\u043e\u043f\u0430\u0441\u0442\u044c \u0432 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0451\u043d\u043d\u043e\u0435 \u043c\u0435\u0441\u0442\u043e, \u0434\u0440\u0443\u0433\u0430\u044f \u0434\u043e\u043b\u0436\u043d\u0430 \u0435\u0451 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c.", "\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0412\u0435\u0434\u0435\u043d\u0438\u044f \u0411\u043e\u044f \u2014 \u041e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043e\u0431\u044f\u0437\u0430\u043d\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u043d\u0435\u043b\u0435\u0442\u0430\u043b\u044c\u043d\u043e, \u0447\u0442\u043e \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0438\u0432\u0430\u0435\u0442 \u0435\u0451 \u0430\u0440\u0441\u0435\u043d\u0430\u043b."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(531,177,'ua','Тактичні Міркування','Киньте 1d12, щоб додати тактичну родзинку до насильницької зустрічі.',NULL,'["\u0412\u0438\u0441\u043e\u043a\u0430 \u041f\u043e\u0437\u0438\u0446\u0456\u044f \u2014 \u041e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0437\u043d\u0430\u0445\u043e\u0434\u0438\u0442\u044c\u0441\u044f \u0437\u043d\u0430\u0447\u043d\u043e \u0432\u0438\u0449\u0435 \u0456\u043d\u0448\u043e\u0457 \u0456 \u043c\u0430\u0454 \u043f\u0435\u0440\u0435\u0432\u0430\u0433\u0443 \u043f\u0440\u0438 \u0430\u0442\u0430\u0446\u0456 \u0442\u0430 \u043e\u0431\u043e\u0440\u043e\u043d\u0456.", "\u041a\u0456\u043d\u0435\u0442\u0438\u0447\u043d\u0438\u0439 \u041f\u043e\u0442\u0435\u043d\u0446\u0456\u0430\u043b \u2014 \u041e\u0431''\u0454\u043a\u0442\u0438 \u0432 \u0437\u043e\u043d\u0456 \u0437\u0434\u0430\u0442\u043d\u0456 \u0437\u0430\u0432\u0434\u0430\u0442\u0438 \u0432\u0435\u043b\u0438\u0447\u0435\u0437\u043d\u043e\u0457 \u0448\u043a\u043e\u0434\u0438, \u0440\u0456\u0437\u043a\u043e \u0437\u043c\u0456\u043d\u0438\u0432\u0448\u0438 \u0441\u0438\u0442\u0443\u0430\u0446\u0456\u044e.", "\u041f\u0440\u043e\u0440\u0438\u0432 \u2014 \u0412\u043e\u0440\u043e\u0433 \u0433\u043b\u0438\u0431\u043e\u043a\u043e \u0437\u0430\u043a\u043e\u043f\u0430\u0432\u0441\u044f \u043d\u0430 \u0434\u043e\u0431\u0440\u0435 \u0437\u0430\u0445\u0438\u0449\u0435\u043d\u0456\u0439 \u043f\u043e\u0437\u0438\u0446\u0456\u0457, \u044f\u043a\u0443 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0441\u043f\u043e\u0447\u0430\u0442\u043a\u0443 \u043f\u043e\u0434\u043e\u043b\u0430\u0442\u0438.", "\u0417\u0430\u0445\u043e\u043f\u043b\u0435\u043d\u043d\u044f \u0456 \u0423\u0442\u0440\u0438\u043c\u0430\u043d\u043d\u044f \u2014 \u041e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043f\u043e\u0432\u0438\u043d\u043d\u0430 \u0437\u0430\u0445\u043e\u043f\u0438\u0442\u0438 \u0446\u0456\u043b\u044c \u0456 \u043e\u0431\u043e\u0440\u043e\u043d\u044f\u0442\u0438 \u0457\u0457 \u0434\u043e \u043f\u0440\u0438\u0445\u043e\u0434\u0443 \u043f\u0456\u0434\u043a\u0440\u0456\u043f\u043b\u0435\u043d\u043d\u044f.", "\u0420\u0438\u0437\u0438\u043a \u0415\u0441\u043a\u0430\u043b\u0430\u0446\u0456\u0457 \u2014 \u0427\u0438\u043c \u0434\u043e\u0432\u0448\u0435 \u0442\u0440\u0438\u0432\u0430\u043b\u043e \u0437\u0456\u0442\u043a\u043d\u0435\u043d\u043d\u044f, \u0442\u0438\u043c \u0456\u043c\u043e\u0432\u0456\u0440\u043d\u0456\u0448\u0435, \u0449\u043e \u0432\u043e\u043d\u043e \u0432\u0438\u0439\u0434\u0435 \u0437-\u043f\u0456\u0434 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044e.", "\u0417\u0430\u0441\u0456\u0434\u043a\u0430 \u2014 \u042f\u043a\u0449\u043e \u043e\u0434\u043d\u0443 \u0441\u0442\u043e\u0440\u043e\u043d\u0443 \u0437\u0430\u0441\u0442\u0430\u043b\u0438 \u0437\u043d\u0435\u043d\u0430\u0446\u044c\u043a\u0430, \u0437\u0456\u0442\u043a\u043d\u0435\u043d\u043d\u044f \u0437\u0430\u043a\u0456\u043d\u0447\u0438\u0442\u044c\u0441\u044f \u0448\u0432\u0438\u0434\u043a\u043e.", "\u041f\u0440\u0438\u0445\u043e\u0432\u0430\u043d\u0430 \u041c\u0456\u0441\u0456\u044f \u2014 \u0414\u043b\u044f \u0437\u0430\u043f\u043e\u0431\u0456\u0433\u0430\u043d\u043d\u044f \u0435\u0441\u043a\u0430\u043b\u0430\u0446\u0456\u0457 \u043d\u0435\u043e\u0431\u0445\u0456\u0434\u043d\u0456 \u0441\u043a\u0440\u0438\u0442\u043d\u0456\u0441\u0442\u044c \u0456 \u0442\u0438\u0448\u0430.", "\u0421\u0443\u043f\u0443\u0442\u043d\u0456 \u0412\u0442\u0440\u0430\u0442\u0438 \u2014 \u0423 \u0437\u043e\u043d\u0456 \u043f\u0440\u0438\u0441\u0443\u0442\u043d\u0456 \u043c\u0438\u0440\u043d\u0456 \u0436\u0438\u0442\u0435\u043b\u0456, \u044f\u043a\u0438\u0445 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0440\u0430\u0445\u043e\u0432\u0443\u0432\u0430\u0442\u0438 \u2014 \u0432\u043e\u0440\u043e\u0433\u0438 \u043c\u043e\u0436\u0443\u0442\u044c \u0457\u0445 \u0432\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u0430\u0442\u0438.", "\u041d\u0435\u0431\u0435\u0437\u043f\u0435\u0447\u043d\u0430 \u0417\u043e\u043d\u0430 \u2014 \u0417\u0456\u0442\u043a\u043d\u0435\u043d\u043d\u044f \u0432\u0456\u0434\u0431\u0443\u0432\u0430\u0454\u0442\u044c\u0441\u044f \u0432 \u043e\u0431\u043c\u0435\u0436\u0435\u043d\u0456\u0439 \u0437\u043e\u043d\u0456; \u0432\u0438\u0445\u0456\u0434 \u0437\u0430 \u0457\u0457 \u043c\u0435\u0436\u0456 \u0437\u0430\u0433\u0440\u043e\u0436\u0443\u0454 \u0448\u043a\u043e\u0434\u043e\u044e \u0430\u0431\u043e \u0441\u043c\u0435\u0440\u0442\u044e.", "\u041a\u043b\u044e\u0447\u043e\u0432\u0430 \u0426\u0456\u043b\u044c \u2014 \u0417\u0456\u0442\u043a\u043d\u0435\u043d\u043d\u044f \u0437\u0430\u043a\u0456\u043d\u0447\u0443\u0454\u0442\u044c\u0441\u044f, \u0449\u043e\u0439\u043d\u043e \u043a\u043b\u044e\u0447\u043e\u0432\u0430 \u0446\u0456\u043b\u044c \u0434\u043e\u0441\u044f\u0433\u043d\u0443\u0442\u0430, \u0437\u0430\u0445\u043e\u043f\u043b\u0435\u043d\u0430 \u0430\u0431\u043e \u0437\u043d\u0438\u0449\u0435\u043d\u0430.", "\u041f\u043e\u0433\u043e\u043d\u044f \u0456 \u0423\u0445\u0438\u043b\u0435\u043d\u043d\u044f \u2014 \u041e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043f\u0440\u0430\u0433\u043d\u0435 \u043f\u043e\u0442\u0440\u0430\u043f\u0438\u0442\u0438 \u0434\u043e \u043f\u0435\u0432\u043d\u043e\u0433\u043e \u043c\u0456\u0441\u0446\u044f, \u0456\u043d\u0448\u0430 \u043f\u043e\u0432\u0438\u043d\u043d\u0430 \u0457\u0457 \u0437\u0443\u043f\u0438\u043d\u0438\u0442\u0438.", "\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0412\u0435\u0434\u0435\u043d\u043d\u044f \u0411\u043e\u044e \u2014 \u041e\u0434\u043d\u0430 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u0437\u043e\u0431\u043e\u0432''\u044f\u0437\u0430\u043d\u0430 \u0434\u0456\u044f\u0442\u0438 \u043d\u0435\u043b\u0435\u0442\u0430\u043b\u044c\u043d\u043e, \u0449\u043e \u0441\u0443\u0442\u0442\u0454\u0432\u043e \u043e\u0431\u043c\u0435\u0436\u0443\u0454 \u0457\u0457 \u0430\u0440\u0441\u0435\u043d\u0430\u043b."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(532,178,'en','Map It Out','Draw a simple flowchart — not a beautiful map, just a usable one.

Steps:
1. Draw 10 numbered boxes. Each box = one location.
2. Box 1 = players'' starting location.
3. Lines between boxes = routes (corridors, maintenance shafts, hyperspace jumps).
4. Note the most important detail from each location on the map itself.
5. On the opposite page, write a key: list 1–10, label each location, then bullet the most important interactive elements.

Each path is a choice. Don''t label routes just ''hallway'' — note what makes them meaningful (guards, exposure, danger, opportunity).

Put everything on the map. If it''s not on the map, it won''t come up in the game.

When are you done? When you can run the scenario from the map without flipping through notes.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(533,178,'ru','Составьте Карту','Нарисуйте простую блок-схему — не красивую карту, а рабочий инструмент.

Шаги:
1. Нарисуйте 10 пронумерованных прямоугольников. Каждый = одна локация.
2. Прямоугольник 1 = стартовая локация игроков.
3. Линии между прямоугольниками = маршруты (коридоры, технические шахты, прыжки в гиперпространство).
4. На самой карте отметьте самую важную деталь каждой локации.
5. На обратной странице напишите легенду: пронумеруйте 1–10, дайте каждой локации название, затем маркером отметьте ключевые интерактивные элементы.

Каждый маршрут — это выбор. Не называйте пути просто «коридор» — отметьте, что делает их значимыми (охрана, открытость, опасность, возможности).

Всё должно быть на карте. Если этого нет на карте — это не появится в игре.

Когда готово? Когда вы можете провести сценарий по карте, не перелистывая заметки.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(534,178,'ua','Складіть Карту','Намалюйте просту блок-схему — не красиву карту, а робочий інструмент.

Кроки:
1. Намалюйте 10 пронумерованих прямокутників. Кожен = одна локація.
2. Прямокутник 1 = стартова локація гравців.
3. Лінії між прямокутниками = маршрути (коридори, технічні шахти, стрибки в гіперпростір).
4. На самій карті відзначте найважливішу деталь кожної локації.
5. На зворотній сторінці напишіть легенду: пронумеруйте 1–10, дайте кожній локації назву, потім маркером відзначте ключові інтерактивні елементи.

Кожен маршрут — це вибір. Не називайте шляхи просто ''коридор'' — відзначте, що робить їх значущими (охорона, відкритість, небезпека, можливості).

Все повинно бути на карті. Якщо цього немає на карті — цього не з''явиться в грі.

Коли готово? Коли ви можете провести сценарій по карті, не гортаючи нотатки.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(535,179,'en','Random Horrors','Roll d100 for each column or roll once and read across:
T = Transgression (what awakens it)
O = Omens (signs of its arrival)
M = Manifestation (its form)
B = Banishment (how to defeat it)
S = Slumber (what it does if not defeated)',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(536,179,'ru','Случайные Ужасы','Бросьте d100 для каждого столбца или один раз и читайте по строке:
П = Проступок (что его пробуждает)
З = Знамения (признаки прихода)
П = Проявление (его форма)
И = Изгнание (как победить)
Д = Дремота (что происходит, если не победить)',NULL,'["\u041f: \u041f\u0435\u0440\u0432\u044b\u0439 \u043a\u043e\u043d\u0442\u0430\u043a\u0442 | \u0417: \u041c\u0451\u0440\u0442\u0432\u044b\u0435 \u0436\u0438\u0432\u043e\u0442\u043d\u044b\u0435 | \u041f: \u0418\u043d\u043e\u043f\u043b\u0430\u043d\u0435\u0442\u043d\u043e\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043e | \u0418: \u0418\u0441\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043e\u0448\u0438\u0431\u043a\u0443 | \u0414: \u0412\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0435\u0442\u0441\u044f \u0447\u0435\u0440\u0435\u0437 100 \u043b\u0435\u0442", "\u041f: \u0418\u0437\u0443\u0447\u0435\u043d\u0438\u0435 \u0442\u0430\u0439\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430 | \u0417: \u0412\u0438\u0434\u0435\u043d\u0438\u044f \u0431\u0443\u0434\u0443\u0449\u0438\u0445 \u0436\u0435\u0440\u0442\u0432 | \u041f: \u0411\u0435\u0437\u0443\u043c\u043d\u044b\u0439 \u0443\u0431\u0438\u0439\u0446\u0430 | \u0418: \u0427\u0435\u043b\u043e\u0432\u0435\u0447\u0435\u0441\u043a\u0430\u044f \u0436\u0435\u0440\u0442\u0432\u0430 | \u0414: \u041f\u043e\u0432\u0442\u043e\u0440\u044f\u044e\u0449\u0438\u0435\u0441\u044f \u0433\u0430\u043b\u043b\u044e\u0446\u0438\u043d\u0430\u0446\u0438\u0438", "\u041f: \u041f\u043e\u0441\u0430\u0434\u043a\u0430 \u043d\u0430 \u043a\u043e\u0440\u0430\u0431\u043b\u044c | \u0417: \u041d\u0430\u0434\u043f\u0438\u0441\u0438 \u043d\u0430 \u0441\u0442\u0435\u043d\u0430\u0445 | \u041f: \u0412\u0435\u0440\u043d\u0443\u0432\u0448\u0435\u0435\u0441\u044f \u0434\u0440\u0435\u0432\u043d\u0435\u0435 \u0437\u043b\u043e | \u0418: \u0412\u0430\u043a\u0446\u0438\u043d\u0430 | \u0414: \u0416\u0435\u0440\u0442\u0432\u044b \u043d\u0430\u0432\u0441\u0435\u0433\u0434\u0430 \u0438\u0441\u043a\u0430\u043b\u0435\u0447\u0435\u043d\u044b", "\u041f: \u0412\u0441\u043a\u0440\u044b\u0442\u0438\u0435 \u043c\u043e\u0433\u0438\u043b\u044b | \u0417: \u0421\u0442\u0438\u0433\u043c\u0430\u0442\u044b | \u041f: \u041a\u0443\u043b\u044c\u0442 | \u0418: \u0423\u044f\u0437\u0432\u0438\u043c \u0442\u043e\u043b\u044c\u043a\u043e \u043a \u043e\u0433\u043d\u044e | \u0414: \u0421\u043f\u0438\u0442 \u0434\u043e \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u043f\u0440\u044b\u0436\u043a\u0430", "\u041f: \u0414\u043e\u0431\u044b\u0447\u0430 \u0441\u0442\u0440\u0430\u043d\u043d\u043e\u0439 \u0440\u0443\u0434\u044b | \u0417: \u041d\u0435\u043e\u0431\u044a\u044f\u0441\u043d\u0438\u043c\u044b\u0435 \u0441\u0430\u043c\u043e\u0443\u0431\u0438\u0439\u0441\u0442\u0432\u0430 | \u041f: \u0417\u0430\u0440\u0430\u0436\u0451\u043d\u043d\u044b\u0435 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438 | \u0418: \u042f\u0434\u0435\u0440\u043d\u044b\u0439 \u0443\u0434\u0430\u0440 \u0441 \u043e\u0440\u0431\u0438\u0442\u044b | \u0414: \u041e\u0442\u0441\u0442\u0443\u043f\u0430\u0435\u0442 \u0432 \u0443\u043a\u0440\u044b\u0442\u0438\u0435", "\u041f: \u0412\u0442\u043e\u0440\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0447\u0443\u0436\u0443\u044e \u0442\u0435\u0440\u0440\u0438\u0442\u043e\u0440\u0438\u044e | \u0417: \u0421\u0438\u0433\u043d\u0430\u043b \u0431\u0435\u0434\u0441\u0442\u0432\u0438\u044f | \u041f: \u041a\u043e\u043b\u043e\u0441\u0441\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u0441\u043c\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043e | \u0418: \u0422\u0430\u0439\u043d\u044b\u0439 \u043e\u043a\u043a\u0443\u043b\u044c\u0442\u043d\u044b\u0439 \u0440\u0438\u0442\u0443\u0430\u043b | \u0414: \u041f\u0440\u0438\u0442\u0432\u043e\u0440\u044f\u0435\u0442\u0441\u044f \u043c\u0451\u0440\u0442\u0432\u044b\u043c, \u0431\u0435\u0436\u0438\u0442", "\u041f: \u0413\u0440\u0443\u0431\u0430\u044f \u0445\u0430\u043b\u0430\u0442\u043d\u043e\u0441\u0442\u044c | \u0417: \u041f\u043e\u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043d\u0435\u0437\u043d\u0430\u043a\u043e\u043c\u0435\u0446 | \u041f: \u0411\u0435\u0437\u0436\u0430\u043b\u043e\u0441\u0442\u043d\u044b\u0439 \u0445\u0438\u0449\u043d\u0438\u043a | \u0418: \u0412\u0435\u0440\u043d\u0443\u0442\u044c \u0435\u0433\u043e \u0434\u043e\u043c\u043e\u0439 | \u0414: \u0416\u0434\u0451\u0442 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u041f\u0440\u043e\u0441\u0442\u0443\u043f\u043a\u0430", "\u041f: \u0412\u043c\u0435\u0448\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e \u0432 \u0431\u0438\u043e\u043b\u043e\u0433\u0438\u044e | \u0417: \u0423\u0440\u043e\u0434\u043b\u0438\u0432\u044b\u0435 \u0440\u043e\u0434\u044b | \u041f: \u041f\u0440\u0438\u0437\u0440\u0430\u043a \u0438\u043b\u0438 \u0434\u0443\u0445 | \u0418: \u041a\u0440\u0435\u043f\u043a\u0438\u0439, \u043d\u043e \u0441\u043c\u0435\u0440\u0442\u043d\u044b\u0439 | \u0414: \u041f\u043e\u0432\u0442\u043e\u0440\u044f\u044e\u0449\u0438\u0435\u0441\u044f \u043a\u043e\u0448\u043c\u0430\u0440\u044b", "\u041f: \u041d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0435 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0430 | \u0417: \u041d\u0435\u0441\u0447\u0430\u0441\u0442\u043b\u0438\u0432\u044b\u0435 \u0447\u0438\u0441\u043b\u0430 | \u041f: \u041a\u043b\u0443\u0431\u043e\u043a \u043f\u0435\u0440\u0435\u043f\u043b\u0435\u0442\u0451\u043d\u043d\u043e\u0439 \u043f\u043b\u043e\u0442\u0438 | \u0418: \u0414\u0430\u0442\u044c \u0435\u043c\u0443 \u0442\u043e, \u0447\u0435\u0433\u043e \u043e\u043d\u043e \u0445\u043e\u0447\u0435\u0442 | \u0414: \u0412\u0441\u0435\u043b\u044f\u0435\u0442\u0441\u044f \u0432 \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0443\u044e \u0436\u0435\u0440\u0442\u0432\u0443", "\u041f: \u041e\u0441\u043a\u0432\u0435\u0440\u043d\u0435\u043d\u0438\u0435 \u0441\u0432\u044f\u0449\u0435\u043d\u043d\u043e\u0433\u043e \u043c\u0435\u0441\u0442\u0430 | \u0417: \u0414\u0440\u0435\u0432\u043d\u0438\u0439 \u043c\u0430\u044f\u043a \u0431\u0435\u0434\u0441\u0442\u0432\u0438\u044f | \u041f: \u041c\u0443\u0442\u0438\u0440\u043e\u0432\u0430\u0432\u0448\u0435\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043e | \u0418: \u041e\u0441\u043e\u0431\u043e\u0435 \u043e\u0440\u0443\u0436\u0438\u0435 | \u0414: \u041f\u0440\u043e\u0431\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f \u043f\u0440\u0438 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0438 \u041f\u0440\u043e\u0441\u0442\u0443\u043f\u043a\u0430", "\u041f: \u041e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u0433\u043e-\u0442\u043e \u043f\u043e\u0437\u0430\u0434\u0438 | \u0417: \u0412\u0438\u0434\u0435\u043d\u0438\u044f \u0443 \u0430\u043d\u0434\u0440\u043e\u0438\u0434\u0430 | \u041f: \u0420\u0435\u0431\u0451\u043d\u043e\u043a | \u0418: \u0417\u0430\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0441 \u043d\u0438\u043c \u043f\u0430\u043a\u0442 | \u0414: \u0421\u043f\u0438\u0442 \u0433\u043b\u0443\u0431\u043e\u043a\u043e \u043f\u043e\u0434 \u0437\u0435\u043c\u043b\u0451\u0439", "\u041f: \u0418\u0437\u0443\u0447\u0435\u043d\u0438\u0435 \u0441\u0442\u0440\u0430\u043d\u043d\u043e\u0439 \u0440\u0435\u043b\u0438\u043a\u0432\u0438\u0438 | \u0417: \u0414\u0440\u0435\u0432\u043d\u0435\u0435 \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u043d\u043e\u0435 \u043f\u0440\u0435\u0434\u0443\u043f\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435 | \u041f: \u0411\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442 | \u0418: \u0421\u043b\u0443\u0436\u0438\u0442\u044c \u0435\u043c\u0443 | \u0414: \u0428\u0451\u043f\u043e\u0442 \u0438\u0437 \u0442\u0435\u043d\u0435\u0439", "\u041f: \u0417\u0430\u0431\u044b\u0442\u043e\u0435 \u0437\u043b\u043e\u0434\u0435\u044f\u043d\u0438\u0435 | \u0417: \u0411\u0435\u0441\u0441\u0432\u044f\u0437\u043d\u044b\u0435 \u0437\u0430\u043f\u0438\u0441\u043a\u0438 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044f | \u041f: \u0420\u0430\u0437\u0443\u043c\u043d\u0430\u044f \u0441\u0440\u0435\u0434\u0430 | \u0418: \u0420\u0430\u0441\u043a\u0440\u044b\u0442\u044c \u0435\u0433\u043e \u0438\u0441\u0442\u0438\u043d\u043d\u0443\u044e \u0441\u0443\u0449\u043d\u043e\u0441\u0442\u044c | \u0414: \u042d\u0432\u043e\u043b\u044e\u0446\u0438\u043e\u043d\u0438\u0440\u0443\u0435\u0442 \u0432 \u0431\u043e\u043b\u0435\u0435 \u043c\u043e\u0449\u043d\u0443\u044e \u0444\u043e\u0440\u043c\u0443", "\u041f: \u041a\u043e\u043d\u0442\u0430\u043a\u0442 \u0441 \u0437\u0430\u043f\u0440\u0435\u0449\u0451\u043d\u043d\u044b\u043c\u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u044f\u043c\u0438 | \u0417: \u0418\u0440\u0440\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430 | \u041f: \u0412\u0440\u0430\u0442\u0430 \u0438\u043b\u0438 \u043f\u043e\u0440\u0442\u0430\u043b | \u0418: \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0451\u043d\u043d\u044b\u0435 \u0432\u0438\u0434\u044b \u0441\u0432\u0435\u0442\u0430 | \u0414: \u0421\u043a\u0440\u044b\u0442\u043e \u043d\u0430 \u0444\u043e\u043d\u0435 \u044d\u043a\u0440\u0430\u043d\u043e\u0432", "\u041f: \u041f\u043e\u0441\u0430\u0434\u043a\u0430 \u043d\u0430 \u043d\u0435\u0438\u0437\u0432\u0435\u0434\u0430\u043d\u043d\u0443\u044e \u043f\u043b\u0430\u043d\u0435\u0442\u0443 | \u0417: \u0417\u043d\u0430\u043a\u043e\u0432\u043e\u0435 \u0430\u0441\u0442\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0441\u043e\u0432\u043f\u0430\u0434\u0435\u043d\u0438\u0435 | \u041f: \u0421\u043e\u043d | \u0418: \u0415\u0433\u043e \u043d\u0435\u043b\u044c\u0437\u044f \u0443\u0431\u0438\u0442\u044c, \u0442\u043e\u043b\u044c\u043a\u043e \u0438\u0437\u0431\u0435\u0436\u0430\u0442\u044c | \u0414: \u0421\u043f\u0438\u0442 \u0432 \u0440\u0430\u0437\u0443\u043c\u0435 \u0441\u0432\u043e\u0435\u0433\u043e \u0443\u0431\u0438\u0439\u0446\u044b", "\u041f: \u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u0440\u043e\u0434\u043d\u043e\u0439 \u0441\u0440\u0435\u0434\u044b \u043e\u0431\u0438\u0442\u0430\u043d\u0438\u044f | \u0417: \u0413\u043e\u0432\u043e\u0440\u0435\u043d\u0438\u0435 \u043d\u0430 \u044f\u0437\u044b\u043a\u0430\u0445 | \u041f: \u041a\u0438\u0431\u0435\u0440\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u043c | \u0418: \u0417\u0430\u0445\u043e\u0440\u043e\u043d\u0435\u043d\u0438\u0435 \u043d\u0430 \u0437\u0430\u043a\u043e\u043d\u043d\u043e\u043c \u043c\u0435\u0441\u0442\u0435 | \u0414: \u041f\u0440\u0435\u0434\u0432\u0435\u0441\u0442\u043d\u0438\u043a \u0431\u043e\u043b\u0435\u0435 \u0433\u0440\u043e\u0437\u043d\u043e\u0433\u043e \u0423\u0436\u0430\u0441\u0430", "\u041f: \u041d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0435 \u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0433\u043e \u0442\u0430\u0431\u0443 | \u0417: \u0422\u0430\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0438\u0441\u0447\u0435\u0437\u043d\u043e\u0432\u0435\u043d\u0438\u044f | \u041f: \u041f\u0440\u043e\u043a\u043b\u044f\u0442\u043e\u0435 \u043c\u0435\u0441\u0442\u043e | \u0418: \u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u043e\u0440\u0442\u0430\u043b/\u0432\u0440\u0430\u0442\u0430 | \u0414: \u0417\u0430\u0433\u0440\u0443\u0436\u0430\u0435\u0442\u0441\u044f \u0432 \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0438\u0439 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440", "\u041f: \u041d\u0435\u0443\u0434\u0430\u0447\u0430 \u0432 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0435 \u043f\u0440\u043e\u0448\u043b\u043e\u0433\u043e \u041f\u0440\u043e\u0441\u0442\u0443\u043f\u043a\u0430 | \u0417: \u0421\u0442\u0440\u0430\u043d\u043d\u044b\u0435 \u043f\u043e\u0433\u043e\u0434\u043d\u044b\u0435 \u044f\u0432\u043b\u0435\u043d\u0438\u044f | \u041f: \u0414\u0432\u043e\u0439\u043d\u0438\u043a | \u0418: \u0422\u0440\u0435\u0431\u0443\u0435\u0442 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0451\u043d\u043d\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438/\u043c\u0435\u0441\u0442\u0430 | \u0414: \u041d\u0435 \u0437\u0430\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0439\u0441\u044f \u043d\u0438\u0433\u0434\u0435 \u2014 \u043e\u043d\u043e \u043d\u0430\u0439\u0434\u0451\u0442 \u0442\u0435\u0431\u044f", "\u041f: \u041f\u043e\u0433\u043b\u043e\u0449\u0435\u043d\u0438\u0435 \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e\u0433\u043e \u0432\u0435\u0449\u0435\u0441\u0442\u0432\u0430 | \u0417: \u0414\u0440\u0435\u0432\u043d\u0438\u0439 \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c \u043f\u0440\u0435\u0434\u0432\u0435\u0449\u0430\u0435\u0442 \u043f\u0440\u0438\u0445\u043e\u0434 | \u041f: \u041d\u0435\u0432\u0438\u0434\u0438\u043c\u043e\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u043e | \u0418: \u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0432 \u0434\u0440\u0443\u0433\u043e\u0435 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0435 | \u0414: \u0421\u0443\u0449\u043d\u043e\u0441\u0442\u044c-\u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u0438\u0449\u0435\u0442 \u043e\u0442\u0432\u0435\u0442\u044b", "\u041f: \u0414\u043e\u043f\u0443\u0449\u0435\u043d\u0438\u0435 \u0432\u0440\u0435\u0434\u0430 \u043d\u0435\u0432\u0438\u043d\u043d\u043e\u043c\u0443 | \u0417: \u0416\u0443\u0442\u043a\u043e \u0432\u044b\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043d\u044b\u0435 \u043d\u0430 \u043f\u043e\u043a\u0430\u0437 \u0442\u0440\u0443\u043f\u044b | \u041f: \u041c\u0430\u0442\u0435\u0440\u0438\u043d\u0441\u043a\u0438\u0439 \u041a\u043e\u0440\u0430\u0431\u043b\u044c | \u0418: \u0417\u0430\u043f\u0435\u0440\u0435\u0442\u044c \u0432 \u043c\u043e\u0449\u043d\u043e\u043c \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0435 | \u0414: \u0410\u043f\u043e\u043a\u0430\u043b\u0438\u043f\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0441\u043e\u0431\u044b\u0442\u0438\u044f \u0437\u0430\u043f\u0443\u0449\u0435\u043d\u044b"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(537,179,'ua','Випадкові Жахи','Киньте d100 для кожного стовпця або один раз і читайте по рядку:
П = Проступок (що його пробуджує)
З = Знамення (ознаки приходу)
П = Прояв (його форма)
В = Вигнання (як перемогти)
С = Сон (що відбувається, якщо не перемогти)',NULL,'["\u041f: \u041f\u0435\u0440\u0448\u0438\u0439 \u043a\u043e\u043d\u0442\u0430\u043a\u0442 | \u0417: \u041c\u0435\u0440\u0442\u0432\u0456 \u0442\u0432\u0430\u0440\u0438\u043d\u0438 | \u041f: \u0406\u043d\u043e\u043f\u043b\u0430\u043d\u0435\u0442\u043d\u0430 \u0456\u0441\u0442\u043e\u0442\u0430 | \u0412: \u0412\u0438\u043f\u0440\u0430\u0432\u0438\u0442\u0438 \u043f\u043e\u043c\u0438\u043b\u043a\u0443 | \u0421: \u041f\u043e\u0432\u0435\u0440\u0442\u0430\u0454\u0442\u044c\u0441\u044f \u0447\u0435\u0440\u0435\u0437 100 \u0440\u043e\u043a\u0456\u0432", "\u041f: \u0412\u0438\u0432\u0447\u0435\u043d\u043d\u044f \u0442\u0430\u0454\u043c\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0443 | \u0417: \u0412\u0438\u0434\u0456\u043d\u043d\u044f \u043c\u0430\u0439\u0431\u0443\u0442\u043d\u0456\u0445 \u0436\u0435\u0440\u0442\u0432 | \u041f: \u0411\u043e\u0436\u0435\u0432\u0456\u043b\u044c\u043d\u0438\u0439 \u0432\u0431\u0438\u0432\u0446\u044f | \u0412: \u041b\u044e\u0434\u0441\u044c\u043a\u0430 \u0436\u0435\u0440\u0442\u0432\u0430 | \u0421: \u041f\u043e\u0432\u0442\u043e\u0440\u044e\u0432\u0430\u043d\u0456 \u0433\u0430\u043b\u044e\u0446\u0438\u043d\u0430\u0446\u0456\u0457", "\u041f: \u041f\u043e\u0441\u0430\u0434\u043a\u0430 \u043d\u0430 \u043a\u043e\u0440\u0430\u0431\u0435\u043b\u044c | \u0417: \u041d\u0430\u043f\u0438\u0441\u0438 \u043d\u0430 \u0441\u0442\u0456\u043d\u0430\u0445 | \u041f: \u0414\u0430\u0432\u043d\u0454 \u0437\u043b\u043e \u043f\u043e\u0432\u0435\u0440\u043d\u0443\u043b\u043e\u0441\u044c | \u0412: \u0412\u0430\u043a\u0446\u0438\u043d\u0430 | \u0421: \u0416\u0435\u0440\u0442\u0432\u0438 \u043d\u0430\u0437\u0430\u0432\u0436\u0434\u0438 \u0441\u043a\u0430\u043b\u0456\u0447\u0435\u043d\u0456", "\u041f: \u0420\u043e\u0437\u043a\u0440\u0438\u0442\u0442\u044f \u043c\u043e\u0433\u0438\u043b\u0438 | \u0417: \u0421\u0442\u0438\u0433\u043c\u0430\u0442\u0438 | \u041f: \u041a\u0443\u043b\u044c\u0442 | \u0412: \u0412\u0440\u0430\u0437\u043b\u0438\u0432\u0438\u0439 \u043b\u0438\u0448\u0435 \u0434\u043e \u0432\u043e\u0433\u043d\u044e | \u0421: \u0421\u043f\u0438\u0442\u044c \u0434\u043e \u043d\u0430\u0441\u0442\u0443\u043f\u043d\u043e\u0433\u043e \u0441\u0442\u0440\u0438\u0431\u043a\u0430", "\u041f: \u0412\u0438\u0434\u043e\u0431\u0443\u0442\u043e\u043a \u0434\u0438\u0432\u043d\u043e\u0457 \u0440\u0443\u0434\u0438 | \u0417: \u041d\u0435\u0437\u0440\u043e\u0437\u0443\u043c\u0456\u043b\u0456 \u0441\u0430\u043c\u043e\u0433\u0443\u0431\u0441\u0442\u0432\u0430 | \u041f: \u0417\u0430\u0440\u0430\u0436\u0435\u043d\u0456 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0456\u0457 | \u0412: \u042f\u0434\u0435\u0440\u043d\u0438\u0439 \u0443\u0434\u0430\u0440 \u0437 \u043e\u0440\u0431\u0456\u0442\u0438 | \u0421: \u0412\u0456\u0434\u0441\u0442\u0443\u043f\u0430\u0454 \u0432 \u0443\u043a\u0440\u0438\u0442\u0442\u044f", "\u041f: \u0412\u0442\u043e\u0440\u0433\u043d\u0435\u043d\u043d\u044f \u043d\u0430 \u0447\u0443\u0436\u0443 \u0442\u0435\u0440\u0438\u0442\u043e\u0440\u0456\u044e | \u0417: \u0421\u0438\u0433\u043d\u0430\u043b \u043b\u0438\u0445\u0430 | \u041f: \u041a\u043e\u043b\u043e\u0441\u0430\u043b\u044c\u043d\u0430 \u043a\u043e\u0441\u043c\u0456\u0447\u043d\u0430 \u0456\u0441\u0442\u043e\u0442\u0430 | \u0412: \u0422\u0430\u0454\u043c\u043d\u0438\u0439 \u043e\u043a\u0443\u043b\u044c\u0442\u043d\u0438\u0439 \u0440\u0438\u0442\u0443\u0430\u043b | \u0421: \u0412\u0434\u0430\u0454, \u0449\u043e \u043c\u0435\u0440\u0442\u0432\u0430, \u0442\u0456\u043a\u0430\u0454", "\u041f: \u0413\u0440\u0443\u0431\u0430 \u0445\u0430\u043b\u0430\u0442\u043d\u0456\u0441\u0442\u044c | \u0417: \u0417''\u044f\u0432\u043b\u044f\u0454\u0442\u044c\u0441\u044f \u043d\u0435\u0437\u043d\u0430\u0439\u043e\u043c\u0435\u0446\u044c | \u041f: \u0411\u0435\u0437\u0436\u0430\u043b\u044c\u043d\u0438\u0439 \u0445\u0438\u0436\u0430\u043a | \u0412: \u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u0438 \u0439\u043e\u0433\u043e \u0434\u043e\u0434\u043e\u043c\u0443 | \u0421: \u0427\u0435\u043a\u0430\u0454 \u043d\u0430 \u043d\u0430\u0441\u0442\u0443\u043f\u043d\u0438\u0439 \u041f\u0440\u043e\u0441\u0442\u0443\u043f\u043e\u043a", "\u041f: \u0412\u0442\u0440\u0443\u0447\u0430\u043d\u043d\u044f \u0432 \u0431\u0456\u043e\u043b\u043e\u0433\u0456\u044e | \u0417: \u041f\u043e\u0442\u0432\u043e\u0440\u043d\u0456 \u043f\u043e\u043b\u043e\u0433\u0438 | \u041f: \u041f\u0440\u0438\u0432\u0438\u0434 \u0430\u0431\u043e \u0434\u0443\u0445 | \u0412: \u041c\u0456\u0446\u043d\u0438\u0439, \u0430\u043b\u0435 \u0441\u043c\u0435\u0440\u0442\u043d\u0438\u0439 | \u0421: \u041f\u043e\u0432\u0442\u043e\u0440\u044e\u0432\u0430\u043d\u0456 \u043a\u043e\u0448\u043c\u0430\u0440\u0438", "\u041f: \u041f\u043e\u0440\u0443\u0448\u0435\u043d\u043d\u044f \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u0443 | \u0417: \u041d\u0435\u0449\u0430\u0441\u043b\u0438\u0432\u0456 \u0447\u0438\u0441\u043b\u0430 | \u041f: \u041a\u043b\u0443\u0431\u043e\u043a \u043f\u0435\u0440\u0435\u043f\u043b\u0435\u0442\u0435\u043d\u043e\u0457 \u043f\u043b\u043e\u0442\u0456 | \u0412: \u0414\u0430\u0442\u0438 \u0439\u043e\u043c\u0443 \u0442\u0435, \u0447\u043e\u0433\u043e \u0432\u043e\u043d\u043e \u0445\u043e\u0447\u0435 | \u0421: \u0412\u0441\u0435\u043b\u044f\u0454\u0442\u044c\u0441\u044f \u0432 \u043d\u0430\u0439\u0431\u043b\u0438\u0436\u0447\u0443 \u0436\u0435\u0440\u0442\u0432\u0443", "\u041f: \u041e\u0441\u043a\u0432\u0435\u0440\u043d\u0435\u043d\u043d\u044f \u0441\u0432\u044f\u0442\u043e\u0433\u043e \u043c\u0456\u0441\u0446\u044f | \u0417: \u0414\u0430\u0432\u043d\u0456\u0439 \u043c\u0430\u044f\u043a \u043b\u0438\u0445\u0430 | \u041f: \u041c\u0443\u0442\u043e\u0432\u0430\u043d\u0430 \u0456\u0441\u0442\u043e\u0442\u0430 | \u0412: \u041e\u0441\u043e\u0431\u043b\u0438\u0432\u0430 \u0437\u0431\u0440\u043e\u044f | \u0421: \u041f\u0440\u043e\u043a\u0438\u0434\u0430\u0454\u0442\u044c\u0441\u044f \u043f\u0440\u0438 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u0456 \u041f\u0440\u043e\u0441\u0442\u0443\u043f\u043a\u0443", "\u041f: \u0417\u0430\u043b\u0438\u0448\u0438\u0442\u0438 \u043a\u043e\u0433\u043e\u0441\u044c \u043f\u043e\u0437\u0430\u0434\u0443 | \u0417: \u0412\u0438\u0434\u0456\u043d\u043d\u044f \u0432 \u0430\u043d\u0434\u0440\u043e\u0457\u0434\u0430 | \u041f: \u0414\u0438\u0442\u0438\u043d\u0430 | \u0412: \u0423\u043a\u043b\u0430\u0441\u0442\u0438 \u0437 \u043d\u0438\u043c \u043f\u0430\u043a\u0442 | \u0421: \u0421\u043f\u0438\u0442\u044c \u0433\u043b\u0438\u0431\u043e\u043a\u043e \u043f\u0456\u0434 \u0437\u0435\u043c\u043b\u0435\u044e", "\u041f: \u0412\u0438\u0432\u0447\u0435\u043d\u043d\u044f \u0434\u0438\u0432\u043d\u043e\u0457 \u0440\u0435\u043b\u0456\u043a\u0432\u0456\u0457 | \u0417: \u0414\u0430\u0432\u043d\u0454 \u0437\u0430\u043f\u0438\u0441\u0430\u043d\u0435 \u043f\u043e\u043f\u0435\u0440\u0435\u0434\u0436\u0435\u043d\u043d\u044f | \u041f: \u0411\u0456\u043e\u043b\u043e\u0433\u0456\u0447\u043d\u0438\u0439 \u0435\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442 | \u0412: \u0421\u043b\u0443\u0436\u0438\u0442\u0438 \u0439\u043e\u043c\u0443 | \u0421: \u0428\u0435\u043f\u0456\u0442 \u0456\u0437 \u0442\u0456\u043d\u0435\u0439", "\u041f: \u0417\u0430\u0431\u0443\u0442\u0435 \u0437\u043b\u043e\u0434\u0456\u044f\u043d\u043d\u044f | \u0417: \u0411\u0435\u0437\u043b\u0430\u0434\u043d\u0456 \u043d\u043e\u0442\u0430\u0442\u043a\u0438 \u0434\u043e\u0441\u043b\u0456\u0434\u043d\u0438\u043a\u0430 | \u041f: \u0420\u043e\u0437\u0443\u043c\u043d\u0435 \u0441\u0435\u0440\u0435\u0434\u043e\u0432\u0438\u0449\u0435 | \u0412: \u0420\u043e\u0437\u043a\u0440\u0438\u0442\u0438 \u0439\u043e\u0433\u043e \u0441\u043f\u0440\u0430\u0432\u0436\u043d\u044e \u0441\u0443\u0442\u043d\u0456\u0441\u0442\u044c | \u0421: \u0415\u0432\u043e\u043b\u044e\u0446\u0456\u043e\u043d\u0443\u0454 \u0443 \u0431\u0456\u043b\u044c\u0448 \u043f\u043e\u0442\u0443\u0436\u043d\u0443 \u0444\u043e\u0440\u043c\u0443", "\u041f: \u041a\u043e\u043d\u0442\u0430\u043a\u0442 \u0456\u0437 \u0437\u0430\u0431\u043e\u0440\u043e\u043d\u0435\u043d\u0438\u043c\u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0456\u044f\u043c\u0438 | \u0417: \u0406\u0440\u0440\u0430\u0446\u0456\u043e\u043d\u0430\u043b\u044c\u043d\u0430 \u043f\u043e\u0432\u0435\u0434\u0456\u043d\u043a\u0430 \u043a\u043e\u043c\u043f''\u044e\u0442\u0435\u0440\u0430 | \u041f: \u0412\u043e\u0440\u043e\u0442\u0430 \u0430\u0431\u043e \u043f\u043e\u0440\u0442\u0430\u043b | \u0412: \u041f\u0435\u0432\u043d\u0456 \u0432\u0438\u0434\u0438 \u0441\u0432\u0456\u0442\u043b\u0430 | \u0421: \u041f\u0440\u0438\u0445\u043e\u0432\u0430\u043d\u0438\u0439 \u043d\u0430 \u0444\u043e\u043d\u0456 \u0435\u043a\u0440\u0430\u043d\u0456\u0432", "\u041f: \u041f\u043e\u0441\u0430\u0434\u043a\u0430 \u043d\u0430 \u043d\u0435\u0432\u0456\u0434\u043e\u043c\u0443 \u043f\u043b\u0430\u043d\u0435\u0442\u0443 | \u0417: \u0417\u043d\u0430\u043a\u043e\u0432\u0435 \u0430\u0441\u0442\u0440\u043e\u043b\u043e\u0433\u0456\u0447\u043d\u0435 \u0437\u0431\u0456\u0433 | \u041f: \u0421\u043e\u043d | \u0412: \u0419\u043e\u0433\u043e \u043d\u0435 \u043c\u043e\u0436\u043d\u0430 \u0432\u0431\u0438\u0442\u0438, \u043b\u0438\u0448\u0435 \u0443\u043d\u0438\u043a\u043d\u0443\u0442\u0438 | \u0421: \u0421\u043f\u0438\u0442\u044c \u0443 \u0440\u043e\u0437\u0443\u043c\u0456 \u0441\u0432\u043e\u0433\u043e \u0432\u0431\u0438\u0432\u0446\u0456", "\u041f: \u0417\u043c\u0456\u043d\u0430 \u043f\u0440\u0438\u0440\u043e\u0434\u043d\u043e\u0433\u043e \u0441\u0435\u0440\u0435\u0434\u043e\u0432\u0438\u0449\u0430 \u0456\u0441\u043d\u0443\u0432\u0430\u043d\u043d\u044f | \u0417: \u0413\u043e\u0432\u043e\u0440\u0456\u043d\u043d\u044f \u043c\u043e\u0432\u0430\u043c\u0438 | \u041f: \u041a\u0456\u0431\u0435\u0440\u043d\u0435\u0442\u0438\u0447\u043d\u0438\u0439 \u043e\u0440\u0433\u0430\u043d\u0456\u0437\u043c | \u0412: \u041f\u043e\u0445\u043e\u0432\u0430\u043d\u043d\u044f \u043d\u0430 \u0437\u0430\u043a\u043e\u043d\u043d\u043e\u043c\u0443 \u043c\u0456\u0441\u0446\u0456 | \u0421: \u041f\u0440\u043e\u0432\u0456\u0441\u043d\u0438\u043a \u0431\u0456\u043b\u044c\u0448 \u0433\u0440\u0456\u0437\u043d\u043e\u0433\u043e \u0416\u0430\u0445\u0443", "\u041f: \u041f\u043e\u0440\u0443\u0448\u0435\u043d\u043d\u044f \u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0433\u043e \u0442\u0430\u0431\u0443 | \u0417: \u0422\u0430\u0454\u043c\u043d\u0438\u0447\u0456 \u0437\u043d\u0438\u043a\u043d\u0435\u043d\u043d\u044f | \u041f: \u041f\u0440\u043e\u043a\u043b\u044f\u0442e \u043c\u0456\u0441\u0446\u0435 | \u0412: \u0417\u0430\u043a\u0440\u0438\u0442\u0438 \u043f\u043e\u0440\u0442\u0430\u043b/\u0432\u043e\u0440\u043e\u0442\u0430 | \u0421: \u0417\u0430\u0432\u0430\u043d\u0442\u0430\u0436\u0443\u0454\u0442\u044c\u0441\u044f \u0432 \u043d\u0430\u0439\u0431\u043b\u0438\u0436\u0447\u0438\u0439 \u043a\u043e\u043c\u043f''\u044e\u0442\u0435\u0440", "\u041f: \u041d\u0435\u0432\u0434\u0430\u0447\u0430 \u0443 \u0437\u0443\u043f\u0438\u043d\u0446\u0456 \u043c\u0438\u043d\u0443\u043b\u043e\u0433\u043e \u041f\u0440\u043e\u0441\u0442\u0443\u043f\u043a\u0443 | \u0417: \u0414\u0438\u0432\u043d\u0456 \u043f\u043e\u0433\u043e\u0434\u043d\u0456 \u044f\u0432\u0438\u0449\u0430 | \u041f: \u0414\u0432\u0456\u0439\u043d\u0438\u043a | \u0412: \u041f\u043e\u0442\u0440\u0435\u0431\u0443\u0454 \u043f\u0435\u0432\u043d\u043e\u0433\u043e \u0447\u0430\u0441\u0443/\u043c\u0456\u0441\u0446\u044f | \u0421: \u041d\u0435 \u0437\u0430\u0442\u0440\u0438\u043c\u0443\u0439\u0441\u044f \u043d\u0456\u0434\u0435 \u2014 \u0432\u043e\u043d\u043e \u0437\u043d\u0430\u0439\u0434\u0435 \u0442\u0435\u0431\u0435", "\u041f: \u041f\u043e\u0433\u043b\u0438\u043d\u0430\u043d\u043d\u044f \u043d\u0435\u0432\u0456\u0434\u043e\u043c\u043e\u0457 \u0440\u0435\u0447\u043e\u0432\u0438\u043d\u0438 | \u0417: \u0414\u0430\u0432\u043d\u0456\u0439 \u043a\u0430\u043b\u0435\u043d\u0434\u0430\u0440 \u043f\u0440\u043e\u0432\u0456\u0449\u0430\u0454 \u043f\u0440\u0438\u0445\u0456\u0434 | \u041f: \u041d\u0435\u0432\u0438\u0434\u0438\u043c\u0430 \u0456\u0441\u0442\u043e\u0442\u0430 | \u0412: \u0412\u0456\u0434\u0456\u0441\u043b\u0430\u0442\u0438 \u0432 \u0456\u043d\u0448\u0438\u0439 \u0432\u0438\u043c\u0456\u0440 | \u0421: \u0411\u0430\u0442\u044c\u043a\u0456\u0432\u0441\u044c\u043a\u0430 \u0441\u0443\u0442\u043d\u0456\u0441\u0442\u044c \u0448\u0443\u043a\u0430\u0454 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0456", "\u041f: \u0414\u043e\u043f\u0443\u0449\u0435\u043d\u043d\u044f \u0448\u043a\u043e\u0434\u0438 \u043d\u0435\u0432\u0438\u043d\u043d\u043e\u043c\u0443 | \u0417: \u0416\u0430\u0445\u043b\u0438\u0432\u043e \u0432\u0438\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0456 \u043d\u0430\u043f\u043e\u043a\u0430\u0437 \u0442\u0440\u0443\u043f\u0438 | \u041f: \u041c\u0430\u0442\u0435\u0440\u0438\u043d\u0441\u044c\u043a\u0438\u0439 \u041a\u043e\u0440\u0430\u0431\u0435\u043b\u044c | \u0412: \u0417\u0430\u043c\u043a\u043d\u0443\u0442\u0438 \u0443 \u043f\u043e\u0442\u0443\u0436\u043d\u043e\u043c\u0443 \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0456 | \u0421: \u0410\u043f\u043e\u043a\u0430\u043b\u0456\u043f\u0442\u0438\u0447\u043d\u0456 \u043f\u043e\u0434\u0456\u0457 \u0437\u0430\u043f\u0443\u0449\u0435\u043d\u0456"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(538,180,'en','Horror Themes','Roll d100 for a thematic direction. Use it to name characters, places, and add evocative descriptions.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(539,180,'ru','Темы Ужаса','Бросьте d100 для тематического направления. Используйте для имён персонажей, мест и красочных описаний.',NULL,'["\u0421\u043c\u0435\u0440\u0442\u044c, \u0434\u0440\u0435\u0432\u043d\u043e\u0441\u0442\u044c, \u0432\u043e\u0441\u043a\u0440\u0435\u0448\u0435\u043d\u0438\u0435", "\u0412\u043e\u0434\u0430, \u0437\u0430\u0442\u043e\u043f\u043b\u0435\u043d\u043d\u043e\u0435, \u0443\u0442\u043e\u043f\u043b\u0435\u043d\u0438\u0435", "\u041f\u043e\u043b\u0438\u0442\u0438\u043a\u0430, \u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e, \u043d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u0438\u0437\u043c", "\u0427\u0435\u043b\u043e\u0432\u0435\u0447\u043d\u043e\u0441\u0442\u044c, \u043b\u044e\u0431\u043e\u0432\u044c, \u043f\u0430\u043c\u044f\u0442\u044c", "\u0421\u043e\u043f\u0440\u043e\u0442\u0438\u0432\u043b\u0435\u043d\u0438\u0435, \u0431\u043e\u0440\u044c\u0431\u0430, \u0441\u0442\u0440\u0430\u0434\u0430\u043d\u0438\u0435", "\u041f\u0443\u0442\u0435\u0448\u0435\u0441\u0442\u0432\u0438\u0435, \u0443\u0441\u0442\u0430\u043b\u043e\u0441\u0442\u044c \u0434\u043e\u0440\u043e\u0433\u0438, \u0441\u0435\u043b\u044c\u0441\u043a\u043e\u0435", "\u0422\u044c\u043c\u0430, \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435, \u043f\u0443\u0441\u0442\u043e\u0442\u0430", "\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0430, \u0431\u043e\u043b\u044c\u043d\u0438\u0446\u044b, \u0445\u0438\u0440\u0443\u0440\u0433\u0438\u044f", "\u0420\u0436\u0430\u0432\u0447\u0438\u043d\u0430, \u041c\u0430\u0448\u0438\u043d\u0430, \u0448\u0443\u043c", "\u0422\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f, \u043f\u0435\u0440\u0435\u0440\u043e\u0436\u0434\u0435\u043d\u0438\u0435", "\u0414\u0435\u0442\u0441\u0442\u0432\u043e, \u043d\u0435\u0432\u0438\u043d\u043d\u043e\u0441\u0442\u044c, \u0432\u0440\u0435\u043c\u044f", "\u041f\u043e\u0434\u0437\u0435\u043c\u0435\u043b\u044c\u0435, \u043f\u0440\u0435\u0441\u0442\u0443\u043f\u043d\u043e\u0441\u0442\u044c, \u043f\u043e\u0433\u0440\u0435\u0431\u0451\u043d\u043d\u043e\u0435", "\u0423\u0433\u0430\u0441\u0430\u044e\u0449\u0430\u044f \u043a\u0440\u0430\u0441\u043e\u0442\u0430, \u0432\u043e\u0437\u0440\u0430\u0441\u0442, \u0441\u043b\u0430\u0432\u0430", "\u0422\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438, \u0438\u0437\u043b\u0438\u0448\u0435\u0441\u0442\u0432\u0430, \u0440\u0430\u0437\u043b\u043e\u0436\u0435\u043d\u0438\u0435", "\u041f\u043e\u0445\u0438\u0449\u0435\u043d\u0438\u0435, \u0438\u0434\u0435\u043d\u0442\u0438\u0447\u043d\u043e\u0441\u0442\u044c, \u0442\u0438\u0448\u0438\u043d\u0430", "\u0413\u043e\u0440\u043e\u0434, \u0434\u043e\u0436\u0434\u044c, \u043d\u0430\u0432\u043e\u0434\u043d\u0435\u043d\u0438\u0435", "\u0421\u0442\u0440\u0430\u0445, \u0437\u0430\u0433\u0440\u043e\u0431\u043d\u0430\u044f \u0436\u0438\u0437\u043d\u044c, \u043f\u0440\u043e\u0440\u043e\u0447\u0435\u0441\u0442\u0432\u043e", "\u0424\u0430\u0431\u0440\u0438\u043a\u0438, \u0442\u0440\u0443\u0434, \u0443\u0433\u043d\u0435\u0442\u0435\u043d\u0438\u0435", "\u0412\u0435\u0440\u0430, \u0431\u043e\u0433, \u0430\u0434", "\u0425\u043e\u043b\u043e\u0434, \u0441\u043e\u043d, \u0441\u043d\u0435\u0433", "\u041e\u0433\u043e\u043d\u044c, \u043f\u0435\u043f\u0435\u043b, \u0432\u043e\u0439\u043d\u0430", "\u0413\u043e\u043b\u043e\u0434, \u0433\u043e\u043b\u043e\u0434\u043e\u043c\u043e\u0440, \u0435\u0434\u0430", "\u0423\u0434\u043e\u0432\u043e\u043b\u044c\u0441\u0442\u0432\u0438\u0435, \u043f\u0440\u0438\u043a\u043e\u0441\u043d\u043e\u0432\u0435\u043d\u0438\u0435, \u0441\u0442\u0440\u0430\u0441\u0442\u044c", "\u0418\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435, \u043a\u0443\u043a\u043b\u044b, \u0438\u0433\u0440\u0443\u0448\u043a\u0438", "\u041c\u044f\u0441\u043e, \u0431\u043e\u0439\u043d\u044f, \u0436\u0438\u0432\u043e\u0442\u043d\u043e\u0435", "\u041f\u0440\u0430\u0432\u0434\u0430, \u0443\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435, \u043e\u0434\u0438\u043d\u043e\u0447\u0435\u0441\u0442\u0432\u043e", "\u0414\u0438\u043a\u0430\u044f \u043f\u0440\u0438\u0440\u043e\u0434\u0430, \u043f\u0440\u0438\u0440\u043e\u0434\u0430, \u0440\u043e\u0441\u0442", "\u041a\u0430\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u043c, \u0436\u0430\u0434\u043d\u043e\u0441\u0442\u044c, \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", "\u0425\u0430\u043e\u0441, \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u044b, \u0441\u043c\u0435\u0445", "\u041f\u043e\u043a\u0438\u043d\u0443\u0442\u043e\u0435, \u043f\u0443\u0441\u0442\u043e\u0435, \u0437\u0430\u0431\u044b\u0442\u043e\u0435"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(540,180,'ua','Теми Жаху','Киньте d100 для тематичного напрямку. Використовуйте для імен персонажів, місць і виразних описів.',NULL,'["\u0421\u043c\u0435\u0440\u0442\u044c, \u0434\u0430\u0432\u043d\u0438\u043d\u0430, \u0432\u043e\u0441\u043a\u0440\u0435\u0441\u0456\u043d\u043d\u044f", "\u0412\u043e\u0434\u0430, \u0437\u0430\u0442\u043e\u043f\u043b\u0435\u043d\u0435, \u043f\u043e\u0442\u043e\u043f\u043b\u0435\u043d\u043d\u044f", "\u041f\u043e\u043b\u0456\u0442\u0438\u043a\u0430, \u0443\u0440\u044f\u0434, \u043d\u0430\u0446\u0456\u043e\u043d\u0430\u043b\u0456\u0437\u043c", "\u041b\u044e\u0434\u044f\u043d\u0456\u0441\u0442\u044c, \u043b\u044e\u0431\u043e\u0432, \u043f\u0430\u043c''\u044f\u0442\u044c", "\u041e\u043f\u0456\u0440, \u0431\u043e\u0440\u043e\u0442\u044c\u0431\u0430, \u0441\u0442\u0440\u0430\u0436\u0434\u0430\u043d\u043d\u044f", "\u041c\u0430\u043d\u0434\u0440\u0456\u0432\u043a\u0430, \u0432\u0442\u043e\u043c\u0430 \u0434\u043e\u0440\u043e\u0433\u0438, \u0441\u0456\u043b\u044c\u0441\u044c\u043a\u0435", "\u0422\u0435\u043c\u0440\u044f\u0432\u0430, \u0432\u0456\u0434\u0441\u0443\u0442\u043d\u0456\u0441\u0442\u044c, \u043f\u043e\u0440\u043e\u0436\u043d\u0435\u0447\u0430", "\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0430, \u043b\u0456\u043a\u0430\u0440\u043d\u0456, \u0445\u0456\u0440\u0443\u0440\u0433\u0456\u044f", "\u0406\u0440\u0436\u0430, \u041c\u0430\u0448\u0438\u043d\u0430, \u0448\u0443\u043c", "\u0422\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0456\u044f, \u043f\u0435\u0440\u0435\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f", "\u0414\u0438\u0442\u0438\u043d\u0441\u0442\u0432\u043e, \u043d\u0435\u0432\u0438\u043d\u043d\u0456\u0441\u0442\u044c, \u0447\u0430\u0441", "\u041f\u0456\u0434\u0437\u0435\u043c\u0435\u043b\u043b\u044f, \u0437\u043b\u043e\u0447\u0438\u043d\u043d\u0456\u0441\u0442\u044c, \u043f\u043e\u0445\u043e\u0432\u0430\u043d\u0435", "\u041a\u0440\u0430\u0441\u0430, \u0449\u043e \u0437\u0433\u0430\u0441\u0430\u0454, \u0432\u0456\u043a, \u0441\u043b\u0430\u0432\u0430", "\u0422\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0456\u0457, \u043d\u0430\u0434\u043c\u0456\u0440\u043d\u0456\u0441\u0442\u044c, \u0440\u043e\u0437\u043a\u043b\u0430\u0434\u0430\u043d\u043d\u044f", "\u0412\u0438\u043a\u0440\u0430\u0434\u0435\u043d\u043d\u044f, \u0456\u0434\u0435\u043d\u0442\u0438\u0447\u043d\u0456\u0441\u0442\u044c, \u0442\u0438\u0448\u0430", "\u041c\u0456\u0441\u0442\u043e, \u0434\u043e\u0449, \u043f\u043e\u0432\u0456\u043d\u044c", "\u0421\u0442\u0440\u0430\u0445, \u0437\u0430\u0433\u0440\u043e\u0431\u043d\u0435 \u0436\u0438\u0442\u0442\u044f, \u043f\u0440\u043e\u0440\u043e\u0446\u0442\u0432\u043e", "\u0424\u0430\u0431\u0440\u0438\u043a\u0438, \u043f\u0440\u0430\u0446\u044f, \u0433\u043d\u043e\u0431\u043b\u0435\u043d\u043d\u044f", "\u0412\u0456\u0440\u0430, \u0431\u043e\u0433, \u043f\u0435\u043a\u043b\u043e", "\u0425\u043e\u043b\u043e\u0434, \u0441\u043e\u043d, \u0441\u043d\u0456\u0433", "\u0412\u043e\u0433\u043e\u043d\u044c, \u043f\u043e\u043f\u0456\u043b, \u0432\u0456\u0439\u043d\u0430", "\u0413\u043e\u043b\u043e\u0434, \u0433\u043e\u043b\u043e\u0434\u043e\u043c\u043e\u0440, \u0457\u0436\u0430", "\u0417\u0430\u0434\u043e\u0432\u043e\u043b\u0435\u043d\u043d\u044f, \u0434\u043e\u0442\u0438\u043a, \u043f\u0440\u0438\u0441\u0442\u0440\u0430\u0441\u0442\u044c", "\u0428\u0442\u0443\u0447\u043d\u0435, \u043b\u044f\u043b\u044c\u043a\u0438, \u0456\u0433\u0440\u0430\u0448\u043a\u0438", "\u041c''\u044f\u0441\u043e, \u0431\u0456\u0439\u043d\u044f, \u0442\u0432\u0430\u0440\u0438\u043d\u0430", "\u041f\u0440\u0430\u0432\u0434\u0430, \u0443\u0441\u0430\u043c\u0456\u0442\u043d\u0435\u043d\u043d\u044f, \u0441\u0430\u043c\u043e\u0442\u043d\u0456\u0441\u0442\u044c", "\u0414\u0438\u043a\u0430 \u043f\u0440\u0438\u0440\u043e\u0434\u0430, \u043f\u0440\u0438\u0440\u043e\u0434\u0430, \u0437\u0440\u043e\u0441\u0442\u0430\u043d\u043d\u044f", "\u041a\u0430\u043f\u0456\u0442\u0430\u043b\u0456\u0437\u043c, \u0436\u0430\u0434\u0456\u0431\u043d\u0456\u0441\u0442\u044c, \u0441\u0442\u0430\u0442\u043e\u043a", "\u0425\u0430\u043e\u0441, \u0437\u043c\u0456\u043d\u0438, \u0441\u043c\u0456\u0445", "\u041f\u043e\u043a\u0438\u043d\u0443\u0442\u0435, \u043f\u043e\u0440\u043e\u0436\u043d\u0454, \u0437\u0430\u0431\u0443\u0442\u0435"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(541,181,'en','The TOMBS Cycle','The TOMBS Cycle describes how a Horror originates, arrives, and is (temporarily) defeated.

Act I — Transgression
Someone knowingly or unknowingly awakens the Horror. A line is crossed — a moral boundary, a forbidden place, a past atrocity. Players usually only realise they have Transgressed when it is too late.

Act II — Omens
The Horror heralds its arrival through signs: nightmares, a trail of victims, strange rumors. Omens build tension and act as clues. Once solved (or time runs out) the Horror appears.

Act III — Manifestation
The Horror reveals its true form. This is the big moment. Think about its smells, sounds, and tactics. A Manifestation is a symptom — once it appears, the players are on the defensive.

Act IV — Banishment
Players race to fight back. The Horror must be dealt with or all hell breaks loose. Banishment can mean killing it, appeasing it, or freeing it from torment. Things ramp up fast.

Act V — Slumber
The Horror relents… for now. If players succeed it goes dormant, awaiting the next Transgression. If they fail it completes its plan and evolves. It is never permanently defeated — just kept at bay for another day.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(542,181,'ru','Цикл TOMBS','Цикл TOMBS описывает, как Ужас возникает, приходит и (временно) побеждается.

Акт I — Проступок
Кто-то сознательно или нет пробуждает Ужас. Переходится черта — моральная граница, запретное место, прошлое злодеяние. Игроки осознают Проступок, как правило, слишком поздно.

Акт II — Знамения
Ужас предвещает своё прибытие: кошмары, след жертв, странные слухи. Знамения нагнетают напряжение и служат уликами. Как только они разгаданы (или время истекает), Ужас появляется.

Акт III — Проявление
Ужас раскрывает свою истинную форму. Это ключевой момент. Подумайте о его запахах, звуках и тактике. Проявление — это симптом: когда он появляется, игроки переходят в оборону.

Акт IV — Изгнание
Игроки спешат дать отпор. С Ужасом нужно справиться, иначе всё рухнет. Изгнание может означать убийство, умиротворение или освобождение от страданий. Темп нарастает стремительно.

Акт V — Дремота
Ужас затихает… на время. При победе игроков он дремлет в ожидании следующего Проступка. При поражении — завершает план и эволюционирует. Его невозможно победить навсегда — лишь сдержать ещё на один день.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(543,181,'ua','Цикл TOMBS','Цикл TOMBS описує, як Жах виникає, приходить і (тимчасово) перемагається.

Акт I — Проступок
Хтось свідомо або ні пробуджує Жах. Перетинається межа — моральна границя, заборонене місце, минуле злодіяння. Гравці усвідомлюють Проступок, як правило, надто пізно.

Акт II — Знамення
Жах провіщає своє прибуття: кошмари, слід жертв, дивні чутки. Знамення нагнітають напругу і слугують підказками. Як тільки вони розгадані (або час вичерпаний), Жах з''являється.

Акт III — Прояв
Жах розкриває свою справжню форму. Це ключовий момент. Подумайте про його запахи, звуки і тактику. Прояв — це симптом: коли він з''являється, гравці переходять в оборону.

Акт IV — Вигнання
Гравці поспішають дати відсіч. З Жахом потрібно впоратись, інакше все рухне. Вигнання може означати вбивство, умиротворення або звільнення від страждань. Темп наростає стрімко.

Акт V — Сон
Жах затихає… на час. При перемозі гравців він дрімає в очікуванні наступного Проступку. При поразці — завершує план і еволюціонує. Його неможливо перемогти назавжди — лише стримати ще на один день.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(544,182,'en','Puzzle Components','Roll d100 for a puzzle type. Use 1–2 components per puzzle — more = too complicated. Every puzzle should allow multiple solutions and leave open the possibility of failure.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(545,182,'ru','Компоненты Головоломок','Бросьте d100 для типа головоломки. Используйте 1–2 компонента — больше = слишком сложно. Каждая головоломка должна допускать несколько решений и возможность провала.',NULL,'["\u0422\u0440\u0435\u0432\u043e\u0433\u0430 \u2014 \u041d\u0435\u0432\u0435\u0440\u043d\u043e\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043f\u043e\u0434\u043d\u0438\u043c\u0430\u0435\u0442 \u0442\u0440\u0435\u0432\u043e\u0433\u0443, \u043e\u043f\u043e\u0432\u0435\u0449\u0430\u044f \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0438\u0445 \u0432\u0440\u0430\u0433\u043e\u0432.", "\u0421\u043e\u0435\u0434\u0438\u043d\u0438\u0442\u044c \u0442\u043e\u0447\u043a\u0438 \u2014 \u0421\u043e\u0435\u0434\u0438\u043d\u0438\u0442\u044c \u0441\u0435\u0440\u0438\u044e \u00ab\u0442\u043e\u0447\u0435\u043a\u00bb \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430 (\u043f\u0440\u043e\u0432\u043e\u0434\u043e\u0432, \u0441\u0432\u0435\u0442\u0430, \u0432\u043e\u0434\u044b, \u043a\u0440\u043e\u0432\u0438).", "\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u2014 \u0421\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u0438\u0437 \u0434\u0435\u0442\u0430\u043b\u0435\u0439, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0443\u0436\u043d\u043e \u043d\u0430\u0439\u0442\u0438 \u0438\u043b\u0438 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c.", "\u0414\u0438\u043b\u0435\u043c\u043c\u0430 \u2014 \u0412\u044b\u0431\u043e\u0440 \u043c\u0435\u0436\u0434\u0443 \u043c\u0435\u043d\u044c\u0448\u0438\u043c \u0438\u0437 \u0434\u0432\u0443\u0445 \u0437\u043e\u043b \u0438\u043b\u0438 \u0431\u043e\u043b\u044c\u0448\u0438\u043c \u0438\u0437 \u0434\u0432\u0443\u0445 \u0431\u043b\u0430\u0433.", "\u041f\u0435\u0440\u0435\u043d\u043e\u0441 \u044f\u0439\u0446\u0430 \u2014 \u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e \u0434\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0445\u0440\u0443\u043f\u043a\u0438\u0439 \u0438\u043b\u0438 \u0443\u044f\u0437\u0432\u0438\u043c\u044b\u0439 \u043f\u0440\u0435\u0434\u043c\u0435\u0442/\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u043c \u0432 \u043d\u0443\u0436\u043d\u043e\u0435 \u043c\u0435\u0441\u0442\u043e.", "\u041d\u0430\u0439\u0442\u0438 \u0443\u043b\u0438\u043a\u0443 \u2014 \u041f\u043e\u0438\u0441\u043a \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043e\u0432, \u0432\u0435\u0434\u0443\u0449\u0438\u0445 \u043a \u043d\u043e\u0432\u044b\u043c \u0412\u043e\u043f\u0440\u043e\u0441\u0430\u043c, \u0413\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043a\u0430\u043c \u0438\u043b\u0438 \u041e\u0442\u0432\u0435\u0442\u0430\u043c.", "\u0421\u0442\u0440\u0430\u0436 \u2014 \u041f\u043e\u0431\u0435\u0434\u0438\u0442\u044c, \u0443\u043c\u0438\u0440\u043e\u0442\u0432\u043e\u0440\u0438\u0442\u044c \u0438\u043b\u0438 \u043e\u0431\u043e\u0439\u0442\u0438 \u0441\u0442\u0440\u0430\u0436\u0430, \u043f\u0440\u0435\u0433\u0440\u0430\u0436\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u043f\u0443\u0442\u044c.", "\u041e\u043f\u0430\u0441\u043d\u044b\u0439 \u043c\u0430\u0440\u0448\u0440\u0443\u0442 \u2014 \u041f\u0443\u0442\u044c \u0437\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u043d \u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c\u044e, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043d\u0443\u0436\u043d\u043e \u043e\u0431\u043e\u0439\u0442\u0438 \u0438\u043b\u0438 \u043f\u0440\u0435\u043e\u0434\u043e\u043b\u0435\u0442\u044c.", "\u0418\u043b\u043b\u044e\u0437\u0438\u044f \u2014 \u0421\u043e\u0434\u0435\u0440\u0436\u0438\u0442 \u044d\u043b\u0435\u043c\u0435\u043d\u0442, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u044b\u0433\u043b\u044f\u0434\u0438\u0442 \u0438\u043d\u0430\u0447\u0435, \u0447\u0435\u043c \u0435\u0441\u0442\u044c \u043d\u0430 \u0441\u0430\u043c\u043e\u043c \u0434\u0435\u043b\u0435.", "\u041b\u0430\u0431\u0438\u0440\u0438\u043d\u0442 \u2014 \u0418\u0433\u0440\u043e\u043a\u0438 \u0434\u043e\u043b\u0436\u043d\u044b \u043f\u0440\u043e\u0439\u0442\u0438 \u0441\u043b\u043e\u0436\u043d\u044b\u0439 \u043b\u0430\u0431\u0438\u0440\u0438\u043d\u0442 \u0438\u043b\u0438 \u0437\u0430\u043f\u0443\u0442\u0430\u043d\u043d\u044b\u0439 \u043f\u0443\u0442\u044c.", "\u0417\u0430\u043c\u043e\u043a \u0438 \u043a\u043b\u044e\u0447 \u2014 \u041d\u0430\u0439\u0442\u0438 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 (\u043a\u043b\u044e\u0447) \u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0435\u0433\u043e, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f \u043a \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u043c\u0443 \u0437\u0430\u043c\u043a\u0430.", "\u041d\u0435\u0434\u043e\u0441\u0442\u0430\u044e\u0449\u0430\u044f \u0447\u0430\u0441\u0442\u044c \u2014 \u041d\u0430\u0439\u0442\u0438 \u043d\u0435\u0434\u043e\u0441\u0442\u0430\u044e\u0449\u0438\u0439 \u043f\u0440\u0435\u0434\u043c\u0435\u0442, \u0447\u0442\u043e\u0431\u044b \u0433\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043a\u0430 \u0437\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u043b\u0430.", "\u041e\u0431\u044b\u0447\u043d\u043e\u0435 \u043f\u0440\u0435\u043f\u044f\u0442\u0441\u0442\u0432\u0438\u0435 \u2014 \u0420\u0435\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430 (\u0441\u043b\u043e\u043c\u0430\u043d\u043d\u044b\u0439 \u043b\u0438\u0444\u0442, \u0443\u043f\u0430\u0432\u0448\u0430\u044f \u043e\u043f\u043e\u0440\u0430 \u0438 \u0442.\u043f.).", "\u041d\u0435\u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0435 \u043c\u044b\u0448\u043b\u0435\u043d\u0438\u0435 \u2014 \u041d\u0435\u0442 \u043e\u0447\u0435\u0432\u0438\u0434\u043d\u043e\u0433\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u044f; \u043d\u0443\u0436\u043d\u043e \u0437\u0430\u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0432\u043d\u0435\u0448\u043d\u0438\u0435 \u0440\u0435\u0441\u0443\u0440\u0441\u044b.", "\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0442\u0442\u0435\u0440\u043d\u0430 \u2014 \u041d\u0443\u0436\u043d\u043e \u0437\u0430\u043c\u0435\u0442\u0438\u0442\u044c \u043f\u043e\u0432\u0442\u043e\u0440\u044f\u044e\u0449\u0438\u0435\u0441\u044f \u0441\u0438\u043c\u0432\u043e\u043b\u044b \u0438\u043b\u0438 \u0434\u0440\u0443\u0433\u0443\u044e \u043f\u043e\u0432\u0442\u043e\u0440\u044f\u044e\u0449\u0443\u044e\u0441\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e.", "\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0430\u0442\u0435\u043b\u044c \u2014 \u0410\u043a\u0442\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0430\u0442\u0435\u043b\u044c \u0432 \u0434\u0440\u0443\u0433\u043e\u043c \u043c\u0435\u0441\u0442\u0435 \u0434\u043b\u044f \u043e\u0431\u0445\u043e\u0434\u0430 \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u043f\u0440\u0435\u043f\u044f\u0442\u0441\u0442\u0432\u0438\u044f.", "\u0417\u0430\u0433\u0430\u0434\u043a\u0430 \u2014 \u041d\u0443\u0436\u043d\u043e \u043f\u0440\u043e\u0438\u0437\u043d\u0435\u0441\u0442\u0438 \u0437\u0430\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0443\u044e \u0444\u0440\u0430\u0437\u0443 \u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c.", "\u041d\u0430\u0440\u0430\u0441\u0442\u0430\u044e\u0449\u0430\u044f \u0443\u0433\u0440\u043e\u0437\u0430 \u2014 \u041e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u043d\u0430\u0440\u0430\u0441\u0442\u0430\u0435\u0442 \u0441\u0430\u043c\u0430 \u043f\u043e \u0441\u0435\u0431\u0435, \u0432\u044b\u043d\u0443\u0436\u0434\u0430\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0431\u044b\u0441\u0442\u0440\u043e.", "\u0416\u0435\u0440\u0442\u0432\u0430 \u2014 \u0418\u0433\u0440\u043e\u043a\u0438 \u0434\u043e\u043b\u0436\u043d\u044b \u043f\u043e\u0436\u0435\u0440\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0447\u0435\u043c-\u0442\u043e \u0446\u0435\u043d\u043d\u044b\u043c.", "\u041f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u2014 \u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0451\u043d\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0448\u0430\u0433\u043e\u0432 \u0432 \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u043c \u043f\u043e\u0440\u044f\u0434\u043a\u0435.", "\u041a\u043e\u043c\u0430\u043d\u0434\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u2014 \u041d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u0434\u043e\u043b\u0436\u043d\u044b \u043e\u0434\u043d\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0451\u043d\u043d\u043e\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435.", "\u0422\u0430\u0439\u043c\u043b\u043e\u043a \u2014 \u0420\u0435\u0448\u0438\u0442\u044c \u0437\u0430 \u043e\u0442\u0432\u0435\u0434\u0451\u043d\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0438\u043b\u0438 \u043f\u0440\u043e\u0432\u0430\u043b\u0438\u0442\u044c\u0441\u044f (\u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u043f\u044b\u0442\u043a\u0443).", "\u041b\u043e\u0432\u0443\u0448\u043a\u0430 \u2014 \u0413\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043a\u0430 \u043d\u0430\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u0437\u0430 \u043d\u0435\u0443\u0434\u0430\u0447\u043d\u044b\u0435 \u043f\u043e\u043f\u044b\u0442\u043a\u0438.", "\u041c\u0435\u0442\u043e\u0434 \u043f\u0440\u043e\u0431 \u0438 \u043e\u0448\u0438\u0431\u043e\u043a \u2014 \u0418\u0433\u0440\u043e\u043a\u0438 \u0434\u043e\u043b\u0436\u043d\u044b \u044d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441 \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u0438\u043c\u0438 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c\u0438 \u0434\u043b\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(546,182,'ua','Компоненти Головоломок','Киньте d100 для типу головоломки. Використовуйте 1–2 компоненти — більше = занадто складно. Кожна головоломка повинна допускати кілька рішень і можливість провалу.',NULL,'["\u0422\u0440\u0438\u0432\u043e\u0433\u0430 \u2014 \u041d\u0435\u0432\u0456\u0440\u043d\u0435 \u0440\u0456\u0448\u0435\u043d\u043d\u044f \u043f\u0456\u0434\u043d\u0456\u043c\u0430\u0454 \u0442\u0440\u0438\u0432\u043e\u0433\u0443, \u0441\u043f\u043e\u0432\u0456\u0449\u0430\u044e\u0447\u0438 \u043d\u0430\u0439\u0431\u043b\u0438\u0436\u0447\u0438\u0445 \u0432\u043e\u0440\u043e\u0433\u0456\u0432.", "\u0417''\u0454\u0434\u043d\u0430\u0442\u0438 \u0442\u043e\u0447\u043a\u0438 \u2014 \u0417''\u0454\u0434\u043d\u0430\u0442\u0438 \u0441\u0435\u0440\u0456\u044e \u00ab\u0442\u043e\u0447\u043e\u043a\u00bb \u0437\u0430 \u0434\u043e\u043f\u043e\u043c\u043e\u0433\u043e\u044e \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430 (\u0434\u0440\u043e\u0442\u0438, \u0441\u0432\u0456\u0442\u043b\u043e, \u0432\u043e\u0434\u0430, \u043a\u0440\u043e\u0432).", "\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0456\u044f \u2014 \u0417\u0456\u0431\u0440\u0430\u0442\u0438 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 \u0437 \u0434\u0435\u0442\u0430\u043b\u0435\u0439, \u044f\u043a\u0456 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0437\u043d\u0430\u0439\u0442\u0438 \u0430\u0431\u043e \u043d\u0430\u0434\u0430\u0442\u0438.", "\u0414\u0438\u043b\u0435\u043c\u0430 \u2014 \u0412\u0438\u0431\u0456\u0440 \u043c\u0456\u0436 \u043c\u0435\u043d\u0448\u0438\u043c \u0456\u0437 \u0434\u0432\u043e\u0445 \u0437\u043e\u043b \u0430\u0431\u043e \u0431\u0456\u043b\u044c\u0448\u0438\u043c \u0456\u0437 \u0434\u0432\u043e\u0445 \u0431\u043b\u0430\u0433.", "\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0435\u043d\u043d\u044f \u044f\u0439\u0446\u044f \u2014 \u0411\u0435\u0437\u043f\u0435\u0447\u043d\u043e \u0434\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u0438 \u043a\u0440\u0438\u0445\u043a\u0438\u0439 \u0430\u0431\u043e \u0432\u0440\u0430\u0437\u043b\u0438\u0432\u0438\u0439 \u043f\u0440\u0435\u0434\u043c\u0435\u0442/\u043e\u0440\u0433\u0430\u043d\u0456\u0437\u043c \u0443 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u0435 \u043c\u0456\u0441\u0446\u0435.", "\u0417\u043d\u0430\u0439\u0442\u0438 \u043f\u0456\u0434\u043a\u0430\u0437\u043a\u0443 \u2014 \u041f\u043e\u0448\u0443\u043a \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0456\u0432, \u0449\u043e \u0432\u0435\u0434\u0443\u0442\u044c \u0434\u043e \u043d\u043e\u0432\u0438\u0445 \u041f\u0438\u0442\u0430\u043d\u044c, \u0413\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043e\u043a \u0430\u0431\u043e \u0412\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0435\u0439.", "\u0412\u0430\u0440\u0442\u043e\u0432\u0438\u0439 \u2014 \u041f\u0435\u0440\u0435\u043c\u043e\u0433\u0442\u0438, \u0437\u0430\u0441\u043f\u043e\u043a\u043e\u0457\u0442\u0438 \u0430\u0431\u043e \u043e\u0431\u0456\u0439\u0442\u0438 \u0432\u0430\u0440\u0442\u043e\u0432\u043e\u0433\u043e, \u0449\u043e \u043f\u0435\u0440\u0435\u0433\u043e\u0440\u043e\u0434\u0436\u0443\u0454 \u0448\u043b\u044f\u0445.", "\u041d\u0435\u0431\u0435\u0437\u043f\u0435\u0447\u043d\u0438\u0439 \u043c\u0430\u0440\u0448\u0440\u0443\u0442 \u2014 \u0428\u043b\u044f\u0445 \u0437\u0430\u0431\u043b\u043e\u043a\u043e\u0432\u0430\u043d\u0438\u0439 \u043d\u0435\u0431\u0435\u0437\u043f\u0435\u043a\u043e\u044e, \u044f\u043a\u0443 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u043e\u0431\u0456\u0439\u0442\u0438 \u0430\u0431\u043e \u043f\u043e\u0434\u043e\u043b\u0430\u0442\u0438.", "\u0406\u043b\u044e\u0437\u0456\u044f \u2014 \u041c\u0456\u0441\u0442\u0438\u0442\u044c \u0435\u043b\u0435\u043c\u0435\u043d\u0442, \u0449\u043e \u0432\u0438\u0433\u043b\u044f\u0434\u0430\u0454 \u0456\u043d\u0430\u043a\u0448\u0435, \u043d\u0456\u0436 \u0454 \u043d\u0430\u0441\u043f\u0440\u0430\u0432\u0434\u0456.", "\u041b\u0430\u0431\u0456\u0440\u0438\u043d\u0442 \u2014 \u0413\u0440\u0430\u0432\u0446\u0456 \u043f\u043e\u0432\u0438\u043d\u043d\u0456 \u043f\u0440\u043e\u0439\u0442\u0438 \u0441\u043a\u043b\u0430\u0434\u043d\u0438\u0439 \u043b\u0430\u0431\u0456\u0440\u0438\u043d\u0442 \u0430\u0431\u043e \u0437\u0430\u043f\u043b\u0443\u0442\u0430\u043d\u0438\u0439 \u0448\u043b\u044f\u0445.", "\u0417\u0430\u043c\u043e\u043a \u0456 \u043a\u043b\u044e\u0447 \u2014 \u0417\u043d\u0430\u0439\u0442\u0438 \u043f\u0440\u0435\u0434\u043c\u0435\u0442 (\u043a\u043b\u044e\u0447) \u0456 \u0432\u0438\u043a\u043e\u0440\u0438\u0441\u0442\u0430\u0442\u0438 \u0439\u043e\u0433\u043e, \u0449\u043e\u0431 \u043e\u0442\u0440\u0438\u043c\u0430\u0442\u0438 \u0434\u043e\u0441\u0442\u0443\u043f \u0434\u043e \u0432\u043c\u0456\u0441\u0442\u0443 \u0437\u0430\u043c\u043a\u0430.", "\u0412\u0456\u0434\u0441\u0443\u0442\u043d\u044f \u0447\u0430\u0441\u0442\u0438\u043d\u0430 \u2014 \u0417\u043d\u0430\u0439\u0442\u0438 \u0432\u0456\u0434\u0441\u0443\u0442\u043d\u0456\u0439 \u043f\u0440\u0435\u0434\u043c\u0435\u0442, \u0449\u043e\u0431 \u0433\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043a\u0430 \u0437\u0430\u043f\u0440\u0430\u0446\u044e\u0432\u0430\u043b\u0430.", "\u0417\u0432\u0438\u0447\u0430\u0439\u043d\u0430 \u043f\u0435\u0440\u0435\u0448\u043a\u043e\u0434\u0430 \u2014 \u0420\u0435\u0430\u043b\u044c\u043d\u0430 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0430 (\u0437\u043b\u0430\u043c\u0430\u043d\u0438\u0439 \u043b\u0456\u0444\u0442, \u0432\u043f\u0430\u043b\u0430 \u043e\u043f\u043e\u0440\u0430 \u0442\u043e\u0449\u043e).", "\u041d\u0435\u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0435 \u043c\u0438\u0441\u043b\u0435\u043d\u043d\u044f \u2014 \u041d\u0435\u043c\u0430\u0454 \u043e\u0447\u0435\u0432\u0438\u0434\u043d\u043e\u0433\u043e \u0440\u0456\u0448\u0435\u043d\u043d\u044f; \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0437\u0430\u043b\u0443\u0447\u0438\u0442\u0438 \u0437\u043e\u0432\u043d\u0456\u0448\u043d\u0456 \u0440\u0435\u0441\u0443\u0440\u0441\u0438.", "\u0420\u043e\u0437\u043f\u0456\u0437\u043d\u0430\u0432\u0430\u043d\u043d\u044f \u043f\u0430\u0442\u0442\u0435\u0440\u043d\u0443 \u2014 \u041f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u043f\u043e\u043c\u0456\u0442\u0438\u0442\u0438 \u043f\u043e\u0432\u0442\u043e\u0440\u044e\u0432\u0430\u043d\u0456 \u0441\u0438\u043c\u0432\u043e\u043b\u0438 \u0430\u0431\u043e \u0456\u043d\u0448\u0443 \u043f\u043e\u0432\u0442\u043e\u0440\u044e\u0432\u0430\u043d\u0443 \u0456\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0456\u044e.", "\u0414\u0438\u0441\u0442\u0430\u043d\u0446\u0456\u0439\u043d\u0438\u0439 \u043f\u0435\u0440\u0435\u043c\u0438\u043a\u0430\u0447 \u2014 \u0410\u043a\u0442\u0438\u0432\u0443\u0432\u0430\u0442\u0438 \u043f\u0435\u0440\u0435\u043c\u0438\u043a\u0430\u0447 \u0432 \u0456\u043d\u0448\u043e\u043c\u0443 \u043c\u0456\u0441\u0446\u0456 \u0434\u043b\u044f \u043e\u0431\u0445\u043e\u0434\u0443 \u043f\u043e\u0442\u043e\u0447\u043d\u043e\u0457 \u043f\u0435\u0440\u0435\u0448\u043a\u043e\u0434\u0438.", "\u0417\u0430\u0433\u0430\u0434\u043a\u0430 \u2014 \u041f\u043e\u0442\u0440\u0456\u0431\u043d\u043e \u0432\u0438\u043c\u043e\u0432\u0438\u0442\u0438 \u0437\u0430\u043a\u043e\u0434\u043e\u0432\u0430\u043d\u0443 \u0444\u0440\u0430\u0437\u0443 \u0430\u0431\u043e \u043f\u0430\u0440\u043e\u043b\u044c.", "\u041d\u0430\u0440\u043e\u0441\u0442\u0430\u044e\u0447\u0430 \u0437\u0430\u0433\u0440\u043e\u0437\u0430 \u2014 \u041d\u0435\u0431\u0435\u0437\u043f\u0435\u043a\u0430 \u043d\u0430\u0440\u043e\u0441\u0442\u0430\u0454 \u0441\u0430\u043c\u0430 \u043f\u043e \u0441\u043e\u0431\u0456, \u0437\u043c\u0443\u0448\u0443\u044e\u0447\u0438 \u0434\u0456\u044f\u0442\u0438 \u0448\u0432\u0438\u0434\u043a\u043e.", "\u0416\u0435\u0440\u0442\u0432\u0430 \u2014 \u0413\u0440\u0430\u0432\u0446\u0456 \u043f\u043e\u0432\u0438\u043d\u043d\u0456 \u043f\u043e\u0436\u0435\u0440\u0442\u0432\u0443\u0432\u0430\u0442\u0438 \u0447\u0438\u043c\u043e\u0441\u044c \u0446\u0456\u043d\u043d\u0438\u043c.", "\u041f\u043e\u0441\u043b\u0456\u0434\u043e\u0432\u043d\u0456\u0441\u0442\u044c \u2014 \u0412\u0438\u043a\u043e\u043d\u0430\u0442\u0438 \u043f\u0435\u0432\u043d\u0443 \u043a\u0456\u043b\u044c\u043a\u0456\u0441\u0442\u044c \u043a\u0440\u043e\u043a\u0456\u0432 \u0443 \u0437\u0430\u0434\u0430\u043d\u043e\u043c\u0443 \u043f\u043e\u0440\u044f\u0434\u043a\u0443.", "\u041a\u043e\u043c\u0430\u043d\u0434\u043d\u0430 \u0440\u043e\u0431\u043e\u0442\u0430 \u2014 \u041a\u0456\u043b\u044c\u043a\u0430 \u0433\u0440\u0430\u0432\u0446\u0456\u0432 \u043f\u043e\u0432\u0438\u043d\u043d\u0456 \u043e\u0434\u043d\u043e\u0447\u0430\u0441\u043d\u043e \u0432\u0438\u043a\u043e\u043d\u0430\u0442\u0438 \u043f\u0435\u0432\u043d\u0443 \u0434\u0456\u044e.", "\u0422\u0430\u0439\u043c\u043b\u043e\u043a \u2014 \u0412\u0438\u0440\u0456\u0448\u0438\u0442\u0438 \u0437\u0430 \u0432\u0456\u0434\u0432\u0435\u0434\u0435\u043d\u0438\u0439 \u0447\u0430\u0441 \u0430\u0431\u043e \u043f\u0440\u043e\u0432\u0430\u043b\u0438\u0442\u0438\u0441\u044c (\u043f\u0435\u0440\u0435\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0438 \u0441\u043f\u0440\u043e\u0431\u0443).", "\u041f\u0430\u0441\u0442\u043a\u0430 \u2014 \u0413\u043e\u043b\u043e\u0432\u043e\u043b\u043e\u043c\u043a\u0430 \u043a\u0430\u0440\u0430\u0454 \u0433\u0440\u0430\u0432\u0446\u0456\u0432 \u0437\u0430 \u043d\u0435\u0432\u0434\u0430\u043b\u0456 \u0441\u043f\u0440\u043e\u0431\u0438.", "\u041c\u0435\u0442\u043e\u0434 \u0441\u043f\u0440\u043e\u0431 \u0456 \u043f\u043e\u043c\u0438\u043b\u043e\u043a \u2014 \u0413\u0440\u0430\u0432\u0446\u0456 \u043f\u043e\u0432\u0438\u043d\u043d\u0456 \u0435\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0443\u0432\u0430\u0442\u0438 \u0437 \u043a\u0456\u043b\u044c\u043a\u043e\u043c\u0430 \u0435\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c\u0438 \u0434\u043b\u044f \u0432\u0438\u0440\u0456\u0448\u0435\u043d\u043d\u044f."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(547,183,'en','How the Game Works','The core loop:
1. Warden describes the situation — honestly and evocatively. Use all five senses. Smell is particularly good for horror. Only describe the horror a little at a time.
2. Players ask questions — encourage as many as needed. The more information they have, the better decisions they make.
3. Players make a decision — everything follows from their choices.
4. Warden sets the stakes — clearly tell players what failure looks like before they commit.
5. Players commit to action.
6. Resolve the action — if it''s obvious, it just happens. If stakes are high and outcome uncertain, roll dice.

Key principles:
• Roll as little as possible.
• Stats and Saves represent capability under extreme pressure, not personality.
• Most rolls have a 30–40% success rate — failure is expected. Never say ''you miss,'' instead describe how the situation gets worse.
• Be impartial. Your job is to create interesting situations, not dramatic stories.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(548,183,'ru','Как Работает Игра','Основной цикл:
1. Судья описывает ситуацию — честно и образно. Задействуйте все пять чувств. Запах особенно хорош для ужаса. Раскрывайте Ужас постепенно.
2. Игроки задают вопросы — поощряйте любые. Чем больше информации, тем лучше решения.
3. Игроки принимают решение — всё следует из их выборов.
4. Судья устанавливает ставки — чётко говорите, как выглядит провал, до подтверждения действия.
5. Игроки подтверждают действие.
6. Разрешение действия — если очевидно, просто происходит. При высоких ставках и неясном исходе — бросайте кубики.

Ключевые принципы:
• Бросайте кубики как можно реже.
• Параметры и Спасброски отражают способности под сильным давлением, а не личность.
• Большинство бросков имеют шанс успеха 30–40% — провал ожидаем. Никогда не говорите ''вы промахнулись'' — описывайте, как ситуация ухудшается.
• Будьте беспристрастны. Ваша задача — создавать интересные ситуации, а не драматические истории.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(549,183,'ua','Як Працює Гра','Основний цикл:
1. Суддя описує ситуацію — чесно і образно. Залучайте всі п''ять чуттів. Запах особливо добрий для жаху. Розкривайте Жах поступово.
2. Гравці ставлять питання — заохочуйте будь-які. Що більше інформації, то кращі рішення.
3. Гравці приймають рішення — все випливає з їхніх виборів.
4. Суддя встановлює ставки — чітко кажіть, як виглядає провал, до підтвердження дії.
5. Гравці підтверджують дію.
6. Вирішення дії — якщо очевидно, просто відбувається. При високих ставках і незрозумілому результаті — кидайте кубики.

Ключові принципи:
• Кидайте кубики якомога рідше.
• Параметри та Порятунки відображають здібності під сильним тиском, а не особистість.
• Більшість кидків мають шанс успіху 30–40% — провал очікуваний. Ніколи не кажіть ''ви промахнулися'' — описуйте, як ситуація погіршується.
• Будьте неупередженими. Ваше завдання — створювати цікаві ситуації, а не драматичні історії.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(550,184,'en','Setting the Stakes','Before every roll, clearly tell the players what failure looks like.

When to set stakes:
• Whenever players come in conflict with people, creatures, or their environment.
• Any time life or death hangs in the balance.
• Skip it for low-stakes routine actions.

What to communicate:
• The likely outcome if they fail (ballpark is enough — no need to be exact).
• Whether there are degrees of success/failure (''barely failed'' can mean something).
• That actions doomed to failure still have stakes — how badly do they fail?

Why this works:
Players can now weigh the risks, change plans, and make informed decisions. Setting stakes doesn''t ruin the surprise — it creates a real gamble. It also lets players correct your logic before the dice fly.

When NOT to roll dice:
• Stakes are low.
• The outcome is obvious.
• They have the right tool, skill, or class.
• They have a good plan — the reward is enacting it.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(551,184,'ru','Установка Ставок','Перед каждым броском чётко говорите игрокам, как выглядит провал.

Когда устанавливать ставки:
• Когда игроки вступают в конфликт с людьми, существами или средой.
• Всякий раз, когда речь идёт о жизни и смерти.
• Пропускайте для рутинных действий с низкими ставками.

Что нужно сообщить:
• Вероятный исход при провале (приблизительно — точность не нужна).
• Есть ли степени успеха/провала (''едва провалился'' может что-то значить).
• Что даже обречённые на провал действия имеют ставки — насколько плохо они провалятся?

Почему это работает:
Игроки могут взвесить риски, изменить планы и принять взвешенные решения. Установка ставок не портит сюрприз — она создаёт настоящий азарт. Кроме того, игроки могут поправить вашу логику до броска.

Когда НЕ бросать кубики:
• Ставки низкие.
• Исход очевиден.
• У них есть нужный инструмент, навык или класс.
• У них хороший план — наградой служит его выполнение.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(552,184,'ua','Встановлення Ставок','Перед кожним кидком чітко кажіть гравцям, як виглядає провал.

Коли встановлювати ставки:
• Коли гравці вступають у конфлікт із людьми, істотами або середовищем.
• Щоразу, коли йдеться про життя і смерть.
• Пропускайте для рутинних дій із низькими ставками.

Що потрібно повідомити:
• Ймовірний результат при провалі (приблизно — точність не потрібна).
• Чи є ступені успіху/провалу (''ледь провалився'' може щось означати).
• Що навіть приречені на провал дії мають ставки — наскільки погано вони провалюються?

Чому це працює:
Гравці можуть зважити ризики, змінити плани і прийняти зважені рішення. Встановлення ставок не псує сюрприз — воно створює справжній азарт. Крім того, гравці можуть виправити вашу логіку до кидка.

Коли НЕ кидати кубики:
• Ставки низькі.
• Результат очевидний.
• У них є потрібний інструмент, навик або клас.
• У них хороший план — нагородою слугує його виконання.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(553,185,'en','Interpreting Failure','A failed roll does not mean ''nothing happens.'' It means the situation gets worse in some way. Every roll moves the game forward. Instead of ''you fail,'' describe how the situation changes.

Four ways to interpret failure:

1. Action succeeds, but costs more time or resources
• Fail a Piloting Check to outmaneuver an enemy? They pull it off, but burn extra fuel.
• Fail to find a ship''s manifest in time? They find it — 20 minutes later, now enemies are coming.

2. Action succeeds, but causes harm
• Fail a Repair Check? Hull fixed, but they injure themselves (1d10 DMG).
• Fail a Combat Check at Close range? Player rolls damage — so does the enemy.

3. Action succeeds, but leaves a tactical disadvantage
• Fail to scavenge parts? Found after an hour — now they''re lost.
• Fail a Strength Check on a stuck airlock while being chased? Got it open, but now they''re stuck.

4. Action fails and the situation gets much worse
• Fail to stop bleeding? Complication — patient takes 1d10 DMG, bleeding worsens.
• Fail to fire at an enemy in a crowded corridor? Bullets ricochet — whole party makes a Body Save.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(554,185,'ru','Интерпретация Провала','Провальный бросок не означает «ничего не происходит». Он означает, что ситуация ухудшается. Каждый бросок двигает игру вперёд. Вместо ''вы провалились'' описывайте, как изменилась ситуация.

Четыре способа интерпретировать провал:

1. Действие удаётся, но требует больше времени или ресурсов
• Провал Проверки Пилотирования? Манёвр выполнен, но сожжено лишнее топливо.
• Не успел найти манифест груза? Нашёл — через 20 минут, враги уже идут.

2. Действие удаётся, но наносит вред
• Провал Проверки Ремонта? Корпус отремонтирован, но получена травма (1d10 урона).
• Провал Проверки Боя на Ближней дистанции? Игрок бросает урон — враг тоже.

3. Действие удаётся, но создаёт тактический проигрыш
• Провал добычи запчастей? Нашёл через час — и потерялся.
• Провал Проверки Силы на заклинившем шлюзе во время погони? Открыл, но застрял.

4. Действие проваливается, и ситуация резко ухудшается
• Провал остановки кровотечения? Осложнение — пациент получает 1d10 урона, кровотечение усиливается.
• Провал атаки в переполненном коридоре? Рикошет — вся группа делает Спасбросок Тела.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(555,185,'ua','Інтерпретація Провалу','Провальний кидок не означає «нічого не відбувається». Він означає, що ситуація погіршується. Кожен кидок рухає гру вперед. Замість ''ви провалилися'' описуйте, як змінилася ситуація.

Чотири способи інтерпретувати провал:

1. Дія вдається, але потребує більше часу або ресурсів
• Провал Перевірки Пілотування? Маневр виконаний, але спалено зайве паливо.
• Не встиг знайти маніфест вантажу? Знайшов — через 20 хвилин, вороги вже йдуть.

2. Дія вдається, але завдає шкоди
• Провал Перевірки Ремонту? Корпус відремонтований, але отримана травма (1d10 шкоди).
• Провал Перевірки Бою на Близькій дистанції? Гравець кидає шкоду — ворог теж.

3. Дія вдається, але створює тактичний програш
• Провал видобутку запчастин? Знайшов через годину — і заблукав.
• Провал Перевірки Сили на заклиненому шлюзі під час погоні? Відкрив, але застряг.

4. Дія провалюється, і ситуація різко погіршується
• Провал зупинки кровотечі? Ускладнення — пацієнт отримує 1d10 шкоди, кровотеча посилюється.
• Провал атаки в переповненому коридорі? Рикошет — вся група робить Порятунок Тіла.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(556,186,'en','Difficulty Settings','Optional house rules to tune difficulty up or down. Add any to your Campaign Notebook.

Ablative Wounds — Players gain 1 extra Wound that doesn''t trigger the Wound table; regained with 30 min rest.
Armor Degradation — AP reduced by 1 whenever excess damage is dealt; armor destroyed at 0 AP.
Critical Stress Relief — On a Critical Success, reduce Stress by 1.
Exhaustable Skills — Auto-succeed one Skill Check per skill per session.
Fragility — All players get 1 Wound (androids get 5).
High Score Breaker — Beat your player High Score → gain 20 points to divide between Stats and Saves.
Impenetrable Wounds — Damage does not carry over after receiving a Wound.
Improved Advancement — Stats and Saves can both improve from Shore Leave.
Lethality — Ignore Health; all weapons deal 1+ Wounds directly.
Light Ammo Tracking — Only track ammo when narratively relevant; assume 1d5 shots remaining.
One Time Advancement — After surviving the first session, add 10 to any 1 Stat or Save.
Opt-In Stress — Players volunteer to take Stress and make Panic Checks when they feel it''s appropriate.
Player Facing Rolls — Players make all rolls; a miss in combat means they might be hit instead.
Rapid Skill Learning — Trained Skill in 3 sessions, Expert in 5, Master in 10.
Resolve — Each session survived grants 1 Resolve, spendable as a free reroll.
Simple Skills — Ignore Skill bonuses; all Skills grant Advantage instead.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(557,186,'ru','Настройки Сложности','Опциональные домашние правила для настройки сложности. Добавьте нужные в Кампейн Ноутбук.

Абляционные Ранения — Игроки получают 1 дополнительное Ранение без броска по таблице; восстанавливается за 30 мин отдыха.
Деградация Брони — КБ снижается на 1 при каждом избыточном уроне; броня уничтожается при 0 КБ.
Снятие Критического Стресса — При Критическом Успехе снизить Стресс на 1.
Исчерпаемые Навыки — Раз в сессию автоматически успешная Проверка Навыка для каждого навыка.
Хрупкость — Все игроки получают 1 Ранение (андроиды — 5).
Рекордсмен — Побить личный рекорд → получить 20 очков для распределения между Параметрами и Спасбросками.
Непроницаемые Ранения — Урон не переносится после получения Ранения.
Улучшенное Развитие — Параметры и Спасброски могут улучшаться во время Берегового Отпуска.
Летальность — Игнорировать Здоровье; все оружия наносят 1+ Ранений напрямую.
Упрощённый Учёт Патронов — Отслеживать только когда нарративно важно; считать 1d5 выстрелов остатком.
Одноразовое Развитие — После выживания в первой сессии добавить 10 к любому 1 Параметру или Спасброску.
Добровольный Стресс — Игроки сами решают, когда получать Стресс и делать Проверки Паники.
Броски Игроков — Игроки делают все броски; промах в бою может означать, что попали по ним.
Быстрое Обучение — Обученный Навык за 3 сессии, Экспертный за 5, Мастерский за 10.
Решимость — Каждая пережитая сессия даёт 1 Решимость — можно потратить как бесплатный перебросок.
Простые Навыки — Игнорировать бонусы Навыков; все Навыки дают Преимущество.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(558,186,'ua','Налаштування Складності','Опціональні домашні правила для налаштування складності. Додайте потрібні до Кампейн Ноутбуку.

Абляційні Поранення — Гравці отримують 1 додаткове Поранення без кидка по таблиці; відновлюється за 30 хв відпочинку.
Деградація Броні — КБ знижується на 1 при кожній надлишковій шкоді; броня знищується при 0 КБ.
Зняття Критичного Стресу — При Критичному Успіху знизити Стрес на 1.
Вичерпні Навики — Раз на сесію автоматично успішна Перевірка Навику для кожного навику.
Крихкість — Усі гравці отримують 1 Поранення (андроїди — 5).
Рекордсмен — Побити особистий рекорд → отримати 20 очок для розподілу між Параметрами та Порятунками.
Непроникні Поранення — Шкода не переноситься після отримання Поранення.
Поліпшений Розвиток — Параметри та Порятунки можуть покращуватися під час Берегової Відпустки.
Летальність — Ігнорувати Здоров''я; вся зброя завдає 1+ Поранень напряму.
Спрощений Облік Патронів — Відстежувати тільки коли нараційно важливо; вважати 1d5 пострілів залишком.
Одноразовий Розвиток — Після виживання в першій сесії додати 10 до будь-якого 1 Параметра або Порятунку.
Добровільний Стрес — Гравці самі вирішують, коли отримувати Стрес і робити Перевірки Паніки.
Кидки Гравців — Гравці роблять усі кидки; промах у бою може означати, що влучили по них.
Швидке Навчання — Навчений Навик за 3 сесії, Експертний за 5, Майстерний за 10.
Рішучість — Кожна пережита сесія дає 1 Рішучість — можна витратити як безкоштовний перекид.
Прості Навики — Ігнорувати бонуси Навиків; усі Навики дають Перевагу.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(559,187,'en','Social Encounters','Subtlety is your worst enemy. Say the quiet part loud. A cookie-cutter character with clear wants beats a mysterious one whose motivations are a mystery.

Lying & Deception
When an NPC lies to the players, just tell them — ''it seems like this person is lying.'' This leads to better play as they try to prove it. When players lie to NPCs, let it work until consequences catch up. Only call for an Instinct Check if the lie is really bad.

Negotiation
• Most people would rather talk than fight.
• A reputation for violence will follow the players.
• Negotiation requires leverage — blackmail, solving a problem, favors.
• In life-or-death situations, remind players that talking may buy escape time.
• Don''t kill surrendered players — take them to their captors'' leader instead.

There are no social rolls. Handle social encounters through roleplay. Let players talk, plan, scheme, and have access to knowledge they shouldn''t.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(560,187,'ru','Социальные Встречи','Тонкость — ваш худший враг. Говорите прямо. Шаблонный персонаж с чёткими желаниями лучше загадочного с непонятными мотивами.

Ложь и Обман
Когда персонаж лжёт игрокам, просто скажите им — ''кажется, этот человек лжёт.'' Это ведёт к лучшей игре. Когда игроки врут персонажам — пусть проходит, пока последствия не настигнут. Бросайте Проверку Инстинкта только при очень плохой лжи.

Переговоры
• Большинство предпочитает разговор драке.
• Репутация насилия будет преследовать игроков.
• Переговоры требуют рычагов влияния — шантаж, решение проблемы, услуги.
• В ситуации жизни и смерти напомните, что разговор может дать время сбежать.
• Не убивайте сдавшихся — ведите их к предводителю захватчиков.

Социальных бросков нет. Социальные встречи разыгрываются в ролевом отыгрыше. Позволяйте игрокам говорить, планировать, строить схемы.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(561,187,'ua','Соціальні Зустрічі','Тонкість — ваш найгірший ворог. Кажіть прямо. Шаблонний персонаж із чіткими бажаннями кращий за таємничого з незрозумілими мотивами.

Брехня та Обман
Коли персонаж бреше гравцям, просто скажіть їм — ''схоже, ця людина бреше.'' Це веде до кращої гри. Коли гравці брешуть персонажам — нехай проходить, поки наслідки не наздоженуть. Кидайте Перевірку Інстинкту тільки при дуже поганій брехні.

Переговори
• Більшість воліє розмову бійці.
• Репутація насилля переслідуватиме гравців.
• Переговори потребують важелів — шантаж, вирішення проблеми, послуги.
• У ситуації життя і смерті нагадайте, що розмова може дати час втекти.
• Не вбивайте тих, хто здався — ведіть їх до ватажка загарбників.

Соціальних кидків немає. Соціальні зустрічі розігруються в рольовому відіграванні. Дозволяйте гравцям говорити, планувати, будувати схеми.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(562,188,'en','Violent Encounters','Think of violent encounters as disasters happening in real time to real people, not a tactical mini-game.

Every monster is a boss monster.
Treat horrors as forces to be reckoned with over a session or more. Players learn their weaknesses gradually and eventually defeat them — or don''t.

Never say ''You miss.''
Whenever someone attacks, something interesting happens. Failed attacks destroy environmental obstacles, kill bystanders, or leave the attacker exposed.

Every violent encounter is the worst day of someone''s life.
In real life, attempted murder is traumatic with long-term consequences. Most intelligent beings de-escalate or flee rather than fight to the death.

Smart enemies are deadly.
When an enemy takes a Wound, it changes tactics — retreats, sets traps, targets the weak.

Defeat ≠ death.
Drag players back to a lair. Lock them in a brig. Cocoon them and leave them for dead.

Death — if a character might die, say so: ''If you do this and fail, you could die.'' When they are going to die, ask what their final action will be. Add their name to the Roster page in your Campaign Notebook.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(563,188,'ru','Насильственные Встречи','Воспринимайте насильственные встречи как катастрофу в реальном времени с реальными людьми, а не как тактическую мини-игру.

Каждый монстр — это босс.
Воспринимайте Ужасы как силы, с которыми нужно бороться на протяжении сессии или больше. Игроки постепенно узнают их слабости и в итоге побеждают — или нет.

Никогда не говорите ''Вы промахнулись.''
Каждая атака — это что-то интересное. Промахи уничтожают укрытия, убивают свидетелей или оставляют атакующего в уязвимом положении.

Каждая насильственная встреча — худший день в чьей-то жизни.
В реальной жизни попытка убийства — это травма с долгосрочными последствиями. Большинство разумных существ скорее отступит, чем будет биться насмерть.

Умные враги смертельно опасны.
После Ранения враг меняет тактику — отступает, ставит ловушки, выбирает слабых.

Поражение ≠ смерть.
Утащите игроков в логово. Закройте в камере. Обмотайте паутиной и бросьте умирать.

Смерть — если персонаж может умереть, скажите об этом: ''Если ты это сделаешь и провалишься, ты можешь умереть.'' Когда персонаж умирает, спросите, каким будет его последнее действие. Занесите имя в Ростер.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(564,188,'ua','Насильницькі Зустрічі','Сприймайте насильницькі зустрічі як катастрофу в реальному часі з реальними людьми, а не як тактичну міні-гру.

Кожен монстр — це бос.
Сприймайте Жахи як сили, з якими потрібно боротися протягом сесії або більше. Гравці поступово дізнаються їхні слабкості і врешті перемагають — або ні.

Ніколи не кажіть ''Ви промахнулися.''
Кожна атака — це щось цікаве. Промахи знищують укриття, вбивають свідків або залишають атакуючого у вразливому становищі.

Кожна насильницька зустріч — найгірший день у чиємусь житті.
У реальному житті спроба вбивства — це травма з довгостроковими наслідками. Більшість розумних істот скоріше відступить, ніж битиметься насмерть.

Розумні вороги смертельно небезпечні.
Після Поранення ворог змінює тактику — відступає, ставить пастки, вибирає слабких.

Поразка ≠ смерть.
Затягніть гравців у лігво. Замкніть у камері. Обмотайте павутиною і залиште вмирати.

Смерть — якщо персонаж може померти, скажіть про це: ''Якщо ти це зробиш і провалишся, ти можеш померти.'' Коли персонаж вмирає, запитайте, якою буде його остання дія. Занесіть ім''я до Ростеру.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(565,189,'en','Running Investigations','Treat Mothership like the ultimate game of Twenty Questions: answer everything truthfully without regard to the outcome.

Never make players roll to find clues.
If they look in the right place or ''search the room,'' they find what''s there. The game is about what they do with the information — not the roll.

Don''t hint, but do remind.
Don''t drop hints to ''help'' them. The game is fun whether they solve it or not. But if they''ve already found a clue and forgotten it, just remind them.

Use Skills.
A Scientist and a Marine examining the same corpse should get different information. Use class, skills, and background to colour the details you reveal.

Only roll when there isn''t time.
Under normal conditions, players get the information they need. Only roll when they''re working against a hard deadline or without resources (lab out of power, guard approaching).

Types of evidence:
• Physical — blood, DNA, organisms, crashed vessels, ancient idols, murder weapons.
• Documentary — corporate memos, deck plans, handwritten notes, distress signals.
• Testimonial — anything someone says under questioning. Can be hearsay or lies.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(566,189,'ru','Расследования','Воспринимайте Mothership как игру в «Двадцать вопросов»: отвечайте честно, не думая о результате.

Никогда не заставляйте игроков бросать кубики для поиска улик.
Если они смотрят в нужном месте или ''обыскивают комнату'' — они находят то, что там есть. Игра — в том, что они делают с информацией, а не в броске.

Не подсказывайте, но напоминайте.
Не давайте подсказок ''на помощь''. Игра интересна вне зависимости от того, решат ли они загадку. Но если они уже нашли улику и забыли — просто напомните.

Используйте Навыки.
Учёный и Морпех, осматривающие один труп, должны получить разную информацию. Используйте класс, навыки и биографию для окраски деталей.

Бросайте кубики только при нехватке времени.
В нормальных условиях игроки получают нужную информацию. Бросок нужен только при жёстком дедлайне или нехватке ресурсов (нет электричества в лаборатории, приближается охрана).

Типы улик:
• Физические — кровь, ДНК, организмы, разбитые корабли, древние идолы, орудия убийства.
• Документальные — корпоративные меморандумы, планы палуб, рукописные заметки, сигналы бедствия.
• Свидетельские — всё, что кто-то говорит на допросе. Могут быть слухами или ложью.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(567,189,'ua','Розслідування','Сприймайте Mothership як гру в ''Двадцять питань'': відповідайте чесно, не думаючи про результат.

Ніколи не змушуйте гравців кидати кубики для пошуку підказок.
Якщо вони дивляться в потрібному місці або ''обшукують кімнату'' — вони знаходять те, що там є. Гра — у тому, що вони роблять з інформацією, а не в кидку.

Не підказуйте, але нагадуйте.
Не давайте підказок ''на допомогу''. Гра цікава незалежно від того, чи розгадають вони таємницю. Але якщо вони вже знайшли підказку і забули — просто нагадайте.

Використовуйте Навики.
Вчений і Морський піхотинець, що оглядають один труп, повинні отримати різну інформацію. Використовуйте клас, навики і біографію для забарвлення деталей.

Кидайте кубики тільки при браку часу.
У нормальних умовах гравці отримують потрібну інформацію. Кидок потрібен тільки при жорсткому дедлайні або браку ресурсів (немає електрики в лабораторії, наближається охорона).

Типи доказів:
• Фізичні — кров, ДНК, організми, розбиті кораблі, давні ідоли, знаряддя вбивства.
• Документальні — корпоративні меморандуми, плани палуб, рукописні нотатки, сигнали лиха.
• Свідчення — все, що хтось каже на допиті. Можуть бути чутками або брехнею.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(568,190,'en','Ship-to-Ship Combat','Ship combat is one of the most horrifying things in space. Treat it as a natural disaster, not a tactical encounter.

Key principles:
• It''s a natural disaster — treat any ship damage as an environmental hazard spiralling out of control.
• Players make decisions; the Computer handles targeting, aiming, and firing.
• It''s a last resort — ships are astronomical investments. Factions would rather lose a crew than pay for a new ship.
• It''s a social encounter — what does the enemy want? Use hailing frequently.

Ship combat is a scenario, not an encounter.
The ideal scenario: a creature loose on the players'' ship, a patrol craft attacking for being in restricted space, life support down, a toxic atmosphere, and marines boarding — just as the thing in the vents finally attacks.

Pace with Ship Turns.
Call a Ship Turn after a few rounds of player action. No ship combat should last more than 2–3 rounds at the absolute maximum. Most should end after one.

Ship economics:
• Players work on a ship — best for short campaigns.
• Players don''t have a ship — travel becomes another problem to solve.
• Players are owner-operators — give them a beat-up raider with Profit Save 2d10+20 and roll annually for financial health.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(569,190,'ru','Бой Корабль-Корабль','Бой корабль-корабль — одна из самых страшных вещей в космосе. Воспринимайте его как стихийное бедствие, а не тактическую встречу.

Ключевые принципы:
• Это стихийное бедствие — любой ущерб кораблю превращается в неуправляемую экологическую угрозу.
• Игроки принимают решения; Компьютер управляет наведением и стрельбой.
• Это крайняя мера — корабли стоят астрономических денег. Фракции предпочтут потерять команду.
• Это социальная встреча — чего хочет враг? Чаще используйте связь.

Бой — это сценарий, а не встреча.
Идеальный сценарий: существо на борту корабля игроков, патрульный корабль атакует за нарушение запретной зоны, система жизнеобеспечения отключена, токсичная атмосфера и десант — как раз когда тварь из вентиляции наконец атакует.

Темп через Ходы Корабля.
Объявляйте Ход Корабля после нескольких раундов действий игроков. Никакой бой не должен длиться более 2–3 раундов. Большинство заканчивается после одного.

Экономика кораблей:
• Игроки работают на корабле — лучший вариант для коротких кампаний.
• У игроков нет корабля — путешествия становятся ещё одной проблемой.
• Игроки — владельцы-операторы — дайте им потрёпанный рейдер с Спасброском Прибыли 2d10+20.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(570,190,'ua','Бій Корабель-Корабель','Бій корабель-корабель — одна з найстрашніших речей у космосі. Сприймайте його як стихійне лихо, а не тактичну зустріч.

Ключові принципи:
• Це стихійне лихо — будь-яка шкода кораблю перетворюється на некеровану екологічну загрозу.
• Гравці приймають рішення; Комп''ютер керує прицілюванням і стріляниною.
• Це крайній захід — кораблі коштують астрономічних грошей. Фракції воліють втратити команду.
• Це соціальна зустріч — чого хоче ворог? Частіше використовуйте зв''язок.

Бій — це сценарій, а не зустріч.
Ідеальний сценарій: істота на борту корабля гравців, патрульний корабель атакує за порушення забороненої зони, система життєзабезпечення відключена, токсична атмосфера і десант — саме коли тварина з вентиляції нарешті атакує.

Темп через Ходи Корабля.
Оголошуйте Хід Корабля після кількох раундів дій гравців. Жоден бій не повинен тривати більше 2–3 раундів. Більшість закінчується після одного.

Економіка кораблів:
• Гравці працюють на кораблі — найкращий варіант для коротких кампаній.
• У гравців немає корабля — подорожі стають ще однією проблемою.
• Гравці — власники-оператори — дайте їм потрепаний рейдер із Порятунком Прибутку 2d10+20.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(571,191,'en','Campaign Style','How your campaign is structured and the style of play your players can expect.

ANTHOLOGY — Sessions have little (if any) narrative cohesion. Each adventure stands alone.
APOCALYPSE — Play centres around a massive threat to all life (alien invasion, interstellar war, plague, AI revolt, etc.).
ENSEMBLE — Players routinely control multiple characters and switch between them as play dictates.
EPISODIC — Sessions emphasise downtime and roleplaying, with frequent time skips and slice-of-life encounters.
HEROIC — Players are key figures in a large-scale epic struggle with stakes that affect millions.
NARRATIVE — Players unravel a cohesive narrative as part of the background or foreground of play.
OPEN TABLE — A large pool of potential players may drop in or out on a session-by-session basis.
SANDBOX — Players are given a large area with several leads on potential work in any order they wish.
SERIAL — Play takes place from moment to moment, day to day, with infrequent time skips.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(572,191,'ru','Стиль кампании','Как структурирована ваша кампания и какого стиля игры ждать игрокам.

АНТОЛОГИЯ — Сессии почти не связаны нарративно. Каждое приключение самостоятельно.
АПОКАЛИПСИС — Игра вращается вокруг массовой угрозы жизни (вторжение, межзвёздная война, чума, бунт ИИ и т.д.).
АНСАМБЛЬ — Игроки регулярно управляют несколькими персонажами, переключаясь между ними.
ЭПИЗОДИЧЕСКАЯ — Упор на отдых и отыгрыш, частые прыжки во времени и бытовые сцены.
ГЕРОИЧЕСКАЯ — Игроки — ключевые фигуры масштабной эпической борьбы с судьбами миллионов.
НАРРАТИВНАЯ — Игроки распутывают связный нарратив на переднем или заднем плане игры.
ОТКРЫТЫЙ СТОЛ — Большой пул игроков может входить и выходить сессия за сессией.
ПЕСОЧНИЦА — Игрокам дан большой регион с множеством зацепок для работы в любом порядке.
СЕРИАЛЬНАЯ — Игра идёт момент за моментом, день за днём, с редкими прыжками во времени.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(573,191,'ua','Стиль кампанії','Як структурована ваша кампанія і якого стилю гри очікувати гравцям.

АНТОЛОГІЯ — Сесії майже не пов''язані наративно. Кожна пригода самостійна.
АПОКАЛІПСИС — Гра обертається навколо масової загрози всьому живому (вторгнення, міжзоряна війна, чума, бунт ШІ тощо).
АНСАМБЛЬ — Гравці регулярно керують кількома персонажами, перемикаючись між ними.
ЕПІЗОДИЧНА — Упор на відпочинок і відіграш, часті стрибки у часі та побутові сцени.
ГЕРОЇЧНА — Гравці — ключові фігури масштабної епічної боротьби з долями мільйонів.
НАРАТИВНА — Гравці розплутують зв''язний наратив на передньому або задньому плані гри.
ВІДКРИТИЙ СТІЛ — Великий пул гравців може входити й виходити сесія за сесією.
ПІСОЧНИЦЯ — Гравцям дано великий регіон з безліччю зачіпок для роботи у будь-якому порядку.
СЕРІАЛЬНА — Гра йде момент за моментом, день за днем, з рідкими стрибками у часі.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(574,192,'en','Campaign Frames','Your campaign''s frame tells players who they are, what kind of work they do, and what kinds of things they might encounter.

00 — SPACE TRUCKERS: Blockade running, smuggling contraband, or working as a certified owner-operator. Watch out for stowaways and customs patrols.
01 — PRIVATE MERCENARIES: Jump and drop. Sweep and clear. Seek and destroy. You go where the Company sends you.
02 — EXPLORERS: You wanted to go where no one had gone before. Turns out there''s a reason why.
03 — DOGS OF WAR: Humanity was in trouble and you answered the call. You''ve looked into the yawning maw of destruction.
04 — CORPORATE INSPECTORS: Production has shut down, vessels have gone missing, strikes are brewing. The C-Levels have questions and it''s your job to get answers.
05 — OFFWORLD COLONISTS: Planting terraformers in inhospitable environments, researching planetary phenomena, defending against local flora and fauna.
06 — CRASHLANDERS: You scraped together money for a ticket to a new life off-world. Now the sirens are blaring and you''re waking up from cryosleep amongst chaos.
07 — HYPERSPACE RAIDERS: Stealing from the rich and giving to whomever you please. Make sure you Jump before the Marshalls close in.
08 — MINING & SALVAGE: Asteroid mining, skimming gas giants, or salvaging derelicts. Steady pay and no suit and tie required.
09 — BOUNTY HUNTERS: There is no law on the Rim, just Corporate Policy. Check the bounty boards, bring in your charge, stay alive.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(575,192,'ru','Рамки кампании','Рамка кампании говорит игрокам, кто они, какую работу выполняют и что их ожидает.

00 — КОСМИЧЕСКИЕ ДАЛЬНОБОЙЩИКИ: Прорыв блокады, контрабанда или работа сертифицированного перевозчика-собственника.
01 — ЧАСТНЫЕ НАЁМНИКИ: Прыжок и высадка. Зачистка. Ликвидация. Вы идёте туда, куда посылает Компания.
02 — ИССЛЕДОВАТЕЛИ: Вы хотели пойти туда, куда не ступала нога человека. Оказывается, на это есть причина.
03 — ПСЫ ВОЙНЫ: Человечество было в беде, и вы откликнулись на призыв. Вы заглянули в разверзшуюся пасть уничтожения.
04 — КОРПОРАТИВНЫЕ ИНСПЕКТОРЫ: Производство остановлено, суда пропали, забастовки назревают. У топ-менеджеров вопросы — вы обязаны дать ответы.
05 — КОЛОНИСТЫ ВНЕ МИРА: Установка терраформеров в негостеприимной среде, изучение планетарных явлений, защита от местной флоры и фауны.
06 — ПОТЕРПЕВШИЕ КРУШЕНИЕ: Вы скопили деньги на билет к новой жизни за пределами Земли. Но сирены уже воют, а вы просыпаетесь из криосна в хаосе.
07 — РЕЙДЕРЫ ГИПЕРПРОСТРАНСТВА: Воровство у богатых и раздача кому придётся. Успейте прыгнуть до того, как Маршалы настигнут вас.
08 — ДОБЫЧА И УТИЛИЗАЦИЯ: Добыча астероидов, скимминг газовых гигантов или подъём деrelict-кораблей. Стабильная зарплата — галстук не нужен.
09 — ОХОТНИКИ ЗА ГОЛОВАМИ: На Окраине нет закона, только корпоративная политика. Проверьте доски объявлений и живите.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(576,192,'ua','Рамки кампанії','Рамка кампанії говорить гравцям, хто вони, яку роботу виконують і що на них чекає.

00 — КОСМІЧНІ ДАЛЕКОБІЙНИКИ: Прорив блокади, контрабанда або робота сертифікованого перевізника-власника.
01 — ПРИВАТНІ НАЙМАНЦІ: Стрибок і висадка. Зачистка. Ліквідація. Ви йдете туди, куди посилає Компанія.
02 — ДОСЛІДНИКИ: Ви хотіли піти туди, куди ще не ступала нога людини. Виявляється, на це є причина.
03 — ПСИ ВІЙНИ: Людство було в біді, і ви відгукнулися на заклик. Ви зазирнули у разверзлу пащу знищення.
04 — КОРПОРАТИВНІ ІНСПЕКТОРИ: Виробництво зупинено, судна зникли, страйки назрівають. У топ-менеджерів питання — ви зобов''язані дати відповіді.
05 — КОЛОНІСТИ ЗА МЕЖЕЮ СВІТУ: Встановлення терраформерів у негостинному середовищі, вивчення планетарних явищ, захист від місцевої флори й фауни.
06 — ПОТЕРПІЛІ АВАРІЮ: Ви назбирали грошей на квиток до нового життя поза Землею. Але сирени вже виють, а ви прокидаєтесь із кріосну в хаосі.
07 — РЕЙДЕРИ ГІПЕРПРОСТОРУ: Крадіжка у багатих і роздача кому завгодно. Встигніть стрибнути до того, як Маршали наздоженуть вас.
08 — ВИДОБУТОК І УТИЛІЗАЦІЯ: Добуток астероїдів, скімінг газових гігантів або підйом derelict-кораблів. Стабільна зарплата — краватка не потрібна.
09 — МИСЛИВЦІ ЗА ГОЛОВАМИ: На Окраїні немає закону, лише корпоративна політика. Перевірте дошки оголошень і живіть.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(577,193,'en','The Company','Design the Company as your campaign''s interstellar megacorporation. It can serve as:

• PRIMARY EMPLOYER or CLIENT: The players have to work for someone, and the Company has resources to operate far from the Core. Stable pay — but you''re first in line to be discarded when things go sideways.
• PRINCIPAL ANTAGONIST or RIVAL: A persistent threat, faceless and inexhaustible. Its resources are so infinite it could take one or more campaigns to uncover all of its schemes.
• FRAMING DEVICE or SETTING: Your Company tells you what kind of work players will be doing and what technologies will define the setting.

CORPORATE POWER: Assume unlimited resources. Assume it''s above the law. Assume permanent blackmail records on every crew member. Assume anything the crew owns is actually leased through the Company. Assume illegal research, flagrant violations, price fixing, espionage, extortion, bribery, embezzlement. Assume invasive tracking, disinformation, industrial sabotage, proxy wars, human experimentation, environmental collapse. Assume they''ve done all this before. Assume they''ll never stop.

CORPORATE MIND MAP: Label a page ''The Company.'' Write it in the centre and circle it. Draw connections to important people, subsidiaries, and secret projects. Add to it as play goes on.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(578,193,'ru','Компания','Создайте Компанию как межзвёздную мегакорпорацию вашей кампании. Она может служить:

• ОСНОВНЫМ РАБОТОДАТЕЛЕМ или КЛИЕНТОМ: Игрокам нужно на кого-то работать, а у Компании есть ресурсы на Окраине. Стабильная зарплата — но вы первые на вылет, когда всё идёт наперекосяк.
• ГЛАВНЫМ АНТАГОНИСТОМ или СОПЕРНИКОМ: Постоянная угроза, безликая и неистощимая. Её ресурсы столь бесконечны, что потребуется несколько кампаний, чтобы раскрыть все схемы.
• ОБРАМЛЯЮЩИМ УСТРОЙСТВОМ или НАСТРОЙКОЙ: Ваша Компания показывает, какую работу будут выполнять игроки и какие технологии будут определять сеттинг.

КОРПОРАТИВНАЯ ВЛАСТЬ: Предположите неограниченные ресурсы. Она выше закона. Постоянные досье с компроматом на каждого члена команды. Всё, чем владеет команда, фактически арендовано у Компании. Незаконные исследования, нарушения, манипуляции ценами, шпионаж, вымогательство, взятки, хищения. Слежка, дезинформация, промышленный саботаж, войны по доверенности, опыты над людьми, экологические катастрофы. Это всё уже было. И будет снова.

МЕНТАЛЬНАЯ КАРТА КОМПАНИИ: Назовите страницу ''Компания.'' Напишите её в центре и обведите. Рисуйте связи с важными людьми, дочерними структурами и секретными проектами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(579,193,'ua','Компанія','Створіть Компанію як міжзоряну мегакорпорацію вашої кампанії. Вона може служити:

• ОСНОВНИМ РОБОТОДАВЦЕМ або КЛІЄНТОМ: Гравцям потрібно на когось працювати, а у Компанії є ресурси на Окраїні. Стабільна зарплата — але ви перші на вихід, коли все йде не так.
• ГОЛОВНИМ АНТАГОНІСТОМ або СУПЕРНИКОМ: Постійна загроза, безлика й невичерпна. Її ресурси настільки нескінченні, що знадобиться кілька кампаній, щоб розкрити всі схеми.
• ОБРАМЛЮЮЧИМ ПРИСТРОЄМ або НАЛАШТУВАННЯМ: Ваша Компанія показує, яку роботу виконуватимуть гравці і які технології визначатимуть сеттинг.

КОРПОРАТИВНА ВЛАДА: Припустіть необмежені ресурси. Вона вище закону. Постійні досьє з компроматом на кожного члена команди. Все, чим володіє команда, фактично орендоване у Компанії. Незаконні дослідження, порушення, маніпуляції цінами, шпигунство, вимагання, хабарі, розкрадання. Слідкування, дезінформація, промисловий саботаж, проксі-війни, досліди над людьми, екологічні катастрофи. Це все вже було. І буде знову.

МЕНТАЛЬНА КАРТА КОМПАНІЇ: Назвіть сторінку ''Компанія.'' Напишіть її в центрі й обведіть. Малюйте зв''язки з важливими людьми, дочірніми структурами та секретними проектами.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(580,194,'en','How to Create Factions','Factions are the organisations, corporations, cults, gangs, and other groups your players interact with.

CREATE A FACTION: Turn to a new page in your Campaign Notebook, title it with the faction''s name, and write a short description. Note their:
• VIPs: Important members with short descriptions and page references.
• Locations: Notable locations with page references.
• Goals: Compelling goals that will affect the players.

USING FACTIONS: Factions become useful once players have encountered two or three, creating situations where they must choose between competing interests. Ally factions offer work, safe ports, and resources. Enemy factions hunt players down and cut them off from supplies.

FACTION GOALS: Assign each goal a number of boxes (easy = 1–2, long/challenging = 5–10). Roll 1d100 at regular intervals:
• Evens: Forward progress — fill in a box.
• Odds: Obstacle or roadblock — mark a box with an X.
• Even doubles: Breakthrough — fill in two boxes (or clear an X).
• Odd doubles: Catastrophic event — erase a filled box.
When all boxes are filled, the faction achieves their goal.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(581,194,'ru','Как создать фракции','Фракции — это организации, корпорации, культы, банды и другие группы, с которыми взаимодействуют игроки.

СОЗДАНИЕ ФРАКЦИИ: Откройте новую страницу в Блокноте Кампании, назовите её именем фракции и напишите краткое описание. Укажите:
• ВИП: Важных членов с кратким описанием и ссылками на страницы.
• Локации: Примечательные места со ссылками на страницы.
• Цели: Значимые цели, которые затронут игроков.

ИСПОЛЬЗОВАНИЕ ФРАКЦИЙ: Фракции становятся наиболее полезными, когда игроки столкнулись с двумя-тремя, создавая ситуации с конкурирующими интересами. Союзные фракции предлагают работу, безопасные порты и ресурсы. Враждебные — преследуют игроков и отрезают от снаряжения.

ЦЕЛИ ФРАКЦИЙ: Назначьте каждой цели количество клеточек (лёгкая = 1–2, трудная/долгая = 5–10). Бросайте 1d100 через регулярные промежутки:
• Чётные: Прогресс — закрасьте клетку.
• Нечётные: Препятствие — отметьте клетку крестом.
• Чётные дубли: Прорыв — закройте две клетки (или сотрите крест).
• Нечётные дубли: Катастрофа — сотрите закрашенную клетку.
Когда все клетки закрашены, фракция достигает цели.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(582,194,'ua','Як створити фракції','Фракції — це організації, корпорації, культи, банди та інші групи, з якими взаємодіють гравці.

СТВОРЕННЯ ФРАКЦІЇ: Відкрийте нову сторінку в Блокноті Кампанії, назвіть її ім''ям фракції та напишіть короткий опис. Вкажіть:
• ВІП: Важливих членів із коротким описом і посиланнями на сторінки.
• Локації: Примітні місця з посиланнями на сторінки.
• Цілі: Значущі цілі, які зачеплять гравців.

ВИКОРИСТАННЯ ФРАКЦІЙ: Фракції стають найкориснішими, коли гравці зіткнулися з двома-трьома, створюючи ситуації з конкуруючими інтересами. Союзні фракції пропонують роботу, безпечні порти та ресурси. Ворожі — переслідують гравців і відрізають від спорядження.

ЦІЛІ ФРАКЦІЙ: Призначте кожній цілі кількість клітинок (легка = 1–2, складна/тривала = 5–10). Кидайте 1d100 через регулярні проміжки:
• Парні: Прогрес — зафарбуйте клітинку.
• Непарні: Перешкода — позначте клітинку хрестом.
• Парні дублі: Прорив — закрийте дві клітинки (або зітріть хрест).
• Непарні дублі: Катастрофа — зітріть зафарбовану клітинку.
Коли всі клітинки зафарбовані, фракція досягає цілі.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(583,195,'en','Contract Work','Roll to determine the department offering contract work. See Pay Scale for payment.

0–1: PRODUCTION & MANUFACTURE
2–3: SHIPPING & HANDLING
4–5: RESEARCH & DEVELOPMENT
6–7: RISK MANAGEMENT
8: HUMAN RESOURCES
9: MERGERS & ACQUISITIONS',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(584,195,'ru','Контрактная работа','Бросьте, чтобы определить отдел, предлагающий контрактную работу. Оплата — по Шкале оплаты.

0–1: ПРОИЗВОДСТВО И ДОБЫЧА
2–3: ТРАНСПОРТИРОВКА
4–5: ИССЛЕДОВАНИЯ И РАЗРАБОТКИ
6–7: УПРАВЛЕНИЕ РИСКАМИ
8: КАДРОВЫЕ РЕСУРСЫ
9: СЛИЯНИЯ И ПОГЛОЩЕНИЯ',NULL,'["ПРОИЗВОДСТВО И ДОБЫЧА — Горная добыча астероидов, утилизация дрейфующих кораблей, срыв забастовок, установка терраформеров, обслуживание андроидов.", "ТРАНСПОРТИРОВКА — Доставка грузов, сопровождение ВИП, вывоз лома, перевозка заключённых, обработка чувствительных материалов, транспорт пассажиров, контрабанда.", "ИССЛЕДОВАНИЯ И РАЗРАБОТКИ — Сбор образцов, планетарная разведка, полевые испытания, саботаж, ликвидация утечки, археологические раскопки, корпоративный шпионаж.", "УПРАВЛЕНИЕ РИСКАМИ — Зачистка, ликвидация, защита активов, соблюдение карантина, охота за головами, реагирование на сигнал бедствия, патрулирование системы.", "КАДРОВЫЕ РЕСУРСЫ — Поиск пропавших, подозрительная смерть, сбой связи, устранение неполадок, переговоры с ИИ, эвакуация поселений.", "СЛИЯНИЯ И ПОГЛОЩЕНИЯ — Возврат активов, удержание утилизации, подбор персонала, протокол первого контакта, изъятие имущества, пиратство."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(585,195,'ua','Контрактна робота','Киньте, щоб визначити відділ, що пропонує контрактну роботу. Оплата — за Шкалою оплати.

0–1: ВИРОБНИЦТВО ТА ВИДОБУТОК
2–3: ТРАНСПОРТУВАННЯ
4–5: ДОСЛІДЖЕННЯ ТА РОЗРОБКИ
6–7: УПРАВЛІННЯ РИЗИКАМИ
8: КАДРОВІ РЕСУРСИ
9: ЗЛИТТЯ ТА ПОГЛИНАННЯ',NULL,'["ВИРОБНИЦТВО ТА ВИДОБУТОК — Гірська розробка астероїдів, утилізація дрейфуючих кораблів, зрив страйків, встановлення терраформерів, обслуговування андроїдів.", "ТРАНСПОРТУВАННЯ — Доставка вантажів, супровід ВІП, вивіз металобрухту, перевезення ув''язнених, обробка чутливих матеріалів, транспорт пасажирів, контрабанда.", "ДОСЛІДЖЕННЯ ТА РОЗРОБКИ — Збір зразків, планетарна розвідка, польові випробування, саботаж, ліквідація витоку, археологічні розкопки, корпоративний шпіонаж.", "УПРАВЛІННЯ РИЗИКАМИ — Зачистка, ліквідація, захист активів, дотримання карантину, полювання за головами, реагування на сигнал лиха, патрулювання системи.", "КАДРОВІ РЕСУРСИ — Пошук зниклих, підозріла смерть, збій зв''язку, усунення несправностей, переговори зі ШІ, евакуація поселень.", "ЗЛИТТЯ ТА ПОГЛИНАННЯ — Повернення активів, утримання утилізації, підбір персоналу, протокол першого контакту, вилучення майна, піратство."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(586,196,'en','Pay Scale','Salary: 500cr/month per Trained Skill, 1,000cr/month per Expert Skill, 2,000cr/month per Master Skill.
Jump Pay: flat bonus equal to Jump × 1,000cr.
Hazard Pay: 1d5 months of salary as a bonus (not an admission of liability).',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(587,196,'ru','Шкала оплаты','Зарплата: 500 кр./мес. за каждый Обученный навык, 1 000 кр./мес. за Экспертный, 2 000 кр./мес. за Мастерский.
Надбавка за прыжок: фиксированный бонус равный Прыжку × 1 000 кр.
Боевые: 1d5 месяца зарплаты в качестве бонуса (не признание ответственности).',NULL,'["ВЛИЯТЕЛЬНОЕ ОДОЛЖЕНИЕ — Клиент не может заплатить, но должен команде большое одолжение. Образ жизни: ПО НУЛЯМ — 1d10 дней расходов на жизнь или одна дешёвая вещь.", "ОТЧАЯНИЕ — Платит 1d10×100 кр. авансом. Это всё, что есть у клиента. Выполнение работы делает его долгосрочным союзником. Образ жизни: ЕДВА СВОДИТ КОНЦЫ — 1d10 недель расходов или одна приличная вещь.", "БАРТЕР — Только обмен: данные астронавигации, ремонт корабля, оружие, снаряжение или проживание. Образ жизни: НУЖНА РАБОТА — 1d10 месяцев расходов или одна дорогая вещь.", "РУТИННАЯ РАБОТА — Платит зарплаты команды; расходы за счёт команды. Никакой надбавки за прыжок или риск. Образ жизни: ВЫПЛАТА ДОЛГОВ — Берег. отпуск C/B/A, дешёвый киберрм, мед. помощь, небольшая взятка или обучение навыку.", "ХОРОШАЯ ОПЛАТА — Платит 1d10×10 000 кр. по завершению и до 10% аванса. Все расходы на дорогу покрыты; до 1d10 Подрядчиков. Образ жизни: В ДЕНЬГАХ — Берег. отпуск X/S, приличный кибермод или апгрейд корабля.", "ДЖЕКПОТ — Платит 1d10×1 000 000 кр. по завершению и до 1d10×10 000 кр. аванса. Все расходы покрыты; частные подрядчики доступны. Образ жизни: МОЖНО НА ПЕНСИЮ — Хватит на корабль, малый бизнес или выход на пенсию."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(588,196,'ua','Шкала оплати','Зарплата: 500 кр./міс. за кожну Навчену навичку, 1 000 кр./міс. за Експертну, 2 000 кр./міс. за Майстерну.
Надбавка за стрибок: фіксований бонус рівний Стрибку × 1 000 кр.
Бойові: 1d5 місяця зарплати як бонус (не визнання відповідальності).',NULL,'["ВПЛИВОВА ПОСЛУГА — Клієнт не може заплатити, але завдячує команді велику послугу. Спосіб життя: НА НУЛЯХ — 1d10 днів витрат на прожиток або одна дешева річ.", "ВІДЧАЙ — Платить 1d10×100 кр. авансом. Це все, що є у клієнта. Виконання роботи робить його довгостроковим союзником. Спосіб життя: ЛЕДВЕ ЗВОДИТЬ КІНЦІ — 1d10 тижнів витрат або одна пристойна річ.", "БАРТЕР — Лише обмін: дані астронавігації, ремонт корабля, зброя, спорядження або проживання. Спосіб життя: ПОТРІБНА РОБОТА — 1d10 місяців витрат або одна дорога річ.", "БУДЕННА РОБОТА — Платить зарплати команди; витрати за рахунок команди. Жодної надбавки за стрибок або ризик. Спосіб життя: ВИПЛАТА БОРГІВ — Берег. відпустка C/B/A, дешевий кіберм, мед. допомога, невелика хабара або навчання навичці.", "ХОРОША ОПЛАТА — Платить 1d10×10 000 кр. після завершення і до 10% авансу. Усі дорожні витрати покриті; до 1d10 Підрядників. Спосіб життя: У ГРОШАХ — Берег. відпустка X/S, пристойний кібермод або апгрейд корабля.", "ДЖЕКПОТ — Платить 1d10×1 000 000 кр. після завершення і до 1d10×10 000 кр. авансу. Усі витрати покриті; приватні підрядники доступні. Спосіб життя: МОЖНА НА ПЕНСІЮ — Вистачить на корабель, малий бізнес або вихід на пенсію."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(589,197,'en','Campaign Economics','Money in Mothership limits players'' options — another resource like Health and Stress to manage.

NET WORTH TABLE:
Nothing — Everything.
Hundreds — Basic living: food, shelter.
Thousands — Weapons, equipment, Shore Leave, rent, space travel.
Hundreds of thousands — Cybermods, private contractors, skill training, land vehicles.
Millions — Ship repairs, fuel, and maintenance.
Tens of millions — Mechs, small spacecraft, small businesses.
Hundreds of millions — Ships, asteroids, small fleets.
Billions — Companies, R&D, moons, private armies.
Trillions — War, colonisation, planets, space stations.

DEBT: In Mothership, debt means owing violent people non-trivial money. Players increase minimum Stress by 1 for every significant debtor. Loan terms: 1d5×10% downpayment, interest equal to the amount borrowed (pay back double), term of 2d10 months.

KEY PRINCIPLES:
• The shorter the campaign, the less important the economics.
• Favours and information are more interesting rewards than credits.
• Upper mobility is statistically impossible. Vast wealth is held by a small number of generationally wealthy companies and families.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(590,197,'ru','Экономика кампании','Деньги в Mothership ограничивают возможности игроков — ещё один ресурс наряду со Здоровьем и Стрессом.

ТАБЛИЦА СОСТОЯНИЯ:
Ничего — Буквально всё.
Сотни — Базовое проживание: еда, кров.
Тысячи — Оружие, снаряжение, береговой отпуск, аренда, перелёты.
Сотни тысяч — Кибермоды, подрядчики, обучение навыкам, наземный транспорт.
Миллионы — Ремонт корабля, топливо и обслуживание.
Десятки миллионов — Мехи, малые корабли, малый бизнес.
Сотни миллионов — Корабли, астероиды, малые флоты.
Миллиарды — Компании, НИОКР, луны, частные армии.
Триллионы — Война, колонизация, планеты, космические станции.

ДОЛГ: В Mothership долг означает задолженность перед жестокими людьми. Игроки увеличивают минимальный Стресс на 1 за каждого значимого кредитора. Условия займа: первоначальный взнос 1d5×10%, проценты равные сумме займа (выплата двойной суммы), срок 2d10 месяцев.

КЛЮЧЕВЫЕ ПРИНЦИПЫ:
• Чем короче кампания, тем менее важна экономика.
• Услуги и информация — более интересные награды, чем кредиты.
• Социальная мобильность статистически невозможна. Большинство богатства сосредоточено в руках немногих.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(591,197,'ua','Економіка кампанії','Гроші в Mothership обмежують можливості гравців — ще один ресурс поряд зі Здоров''ям і Стресом.

ТАБЛИЦЯ СТАТКУ:
Нічого — Буквально все.
Сотні — Базове проживання: їжа, дах над головою.
Тисячі — Зброя, спорядження, береговий відпочинок, оренда, перельоти.
Сотні тисяч — Кібермоди, підрядники, навчання навичкам, наземний транспорт.
Мільйони — Ремонт корабля, пальне та обслуговування.
Десятки мільйонів — Мехи, малі кораблі, малий бізнес.
Сотні мільйонів — Кораблі, астероїди, малі флоти.
Мільярди — Компанії, НДДКР, місяці, приватні армії.
Трильйони — Війна, колонізація, планети, космічні станції.

БОРГ: У Mothership борг означає заборгованість перед жорстокими людьми. Гравці збільшують мінімальний Стрес на 1 за кожного значного кредитора. Умови позики: перший внесок 1d5×10%, відсотки рівні сумі позики (виплата подвійної суми), строк 2d10 місяців.

КЛЮЧОВІ ПРИНЦИПИ:
• Чим коротша кампанія, тим менш важлива економіка.
• Послуги та інформація — більш цікаві нагороди, ніж кредити.
• Соціальна мобільність статистично неможлива. Більшість багатства сконцентровано в руках небагатьох.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(592,198,'en','Ending Your Campaign','Sooner or later every campaign ends. Knowing how and when to end it gives players closure and a sense of accomplishment.

RUN SHORTER CAMPAIGNS & SEQUELS: Set a clear goal up front. Ask a question and end the campaign when your players have the answer. Ask whose characters survived what they plan to do next, then start a sequel with some of the same characters and a few new ones.

OMEGA SESSIONS: When you see the symptoms (players missing more sessions, people can''t remember what happened last time, longer breaks between games), schedule an Omega Session. Cut right to the end — drop your players into one last session that brings the house down. Everyone finds out who lives and who dies, what the mystery was all about, and everyone goes home with an ending.

CAMPAIGN MAINTENANCE:
• Skip 1d10 months between adventures to avoid non-stop struggle.
• Run slice-of-life sessions where players visit friends, shop, and pursue relationships.
• Threats page: three major Threats with three escalating events each, on a calendar.
• Fallout page: track consequences of players'' actions between sessions.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(593,198,'ru','Завершение кампании','Рано или поздно каждая кампания заканчивается. Знание того, как и когда завершить её, даёт игрокам ощущение завершённости.

КОРОТКИЕ КАМПАНИИ И СИКВЕЛЫ: Установите чёткую цель с самого начала. Задайте вопрос и завершите кампанию, когда игроки найдут ответ. Спросите, чьи персонажи выжили и что планируют дальше, затем начните сиквел с частью старых персонажей и несколькими новыми.

ОМЕГА-СЕССИИ: Когда появляются признаки угасания (игроки пропускают сессии, никто не помнит, что было в прошлый раз, перерывы всё длиннее), запланируйте Омега-сессию. Прыжок к финалу — бросьте игроков в последнюю сессию, которая всё решит. Все узнают, кто выжил и кто умер, в чём была тайна, и все уходят с концовкой.

СОПРОВОЖДЕНИЕ КАМПАНИИ:
• Пропускайте 1d10 месяцев между приключениями.
• Проводите бытовые сессии, где игроки встречаются с друзьями, ходят по магазинам и развивают отношения.
• Страница Угроз: три основные Угрозы с тремя нарастающими событиями каждая, на календаре.
• Страница Последствий: отслеживайте последствия действий игроков между сессиями.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(594,198,'ua','Завершення кампанії','Рано чи пізно кожна кампанія закінчується. Знання того, як і коли завершити її, дає гравцям відчуття завершеності.

КОРОТКІ КАМПАНІЇ ТА СИКВЕЛИ: Встановіть чітку мету з самого початку. Поставте питання і завершіть кампанію, коли гравці знайдуть відповідь. Запитайте, чиї персонажі вижили і що планують далі, потім почніть сиквел із частиною старих персонажів і кількома новими.

ОМЕГА-СЕСІЇ: Коли з''являються ознаки згасання (гравці пропускають сесії, ніхто не пам''ятає, що було минулого разу, перерви все довші), заплануйте Омега-сесію. Стрибок до фіналу — киньте гравців в останню сесію, яка вирішить усе. Всі дізнаються, хто вижив і хто помер, у чому була таємниця, і всі йдуть із кінцівкою.

СУПРОВІД КАМПАНІЇ:
• Пропускайте 1d10 місяців між пригодами.
• Проводьте побутові сесії, де гравці зустрічаються з друзями, ходять по магазинах і розвивають стосунки.
• Сторінка Загроз: три основні Загрози з трьома наростаючими подіями кожна, на календарі.
• Сторінка Наслідків: відстежуйте наслідки дій гравців між сесіями.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(595,199,'en','Planet Surface','Roll separately for each planet column: Surface / Size & Gravity / Atmosphere / Climate.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(596,199,'ru','Поверхность планеты','Бросайте отдельно для каждого столбца: Поверхность / Размер и гравитация / Атмосфера / Климат.',NULL,'["Жидкая", "Твёрдая", "Газовая"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(597,199,'ua','Поверхня планети','Кидайте окремо для кожного стовпця: Поверхня / Розмір і гравітація / Атмосфера / Клімат.',NULL,'["Рідка", "Тверда", "Газова"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(598,200,'en','Settlement Locale','Geological features that serve as settlement locales on planets and moons.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(599,200,'ru','Местоположение поселения','Геологические объекты, служащие локациями поселений на планетах и спутниках.',NULL,'["КАТЕНА — цепочка кратеров", "ХАОС — разломанный рельеф", "КОЛЛИС — небольшой холм", "КРАТЕР — ударная долина", "ДОРСУМ — гряда", "ВУЛКАНИЧЕСКИЙ ЦЕНТР — вулкан", "ФОССА — впадина", "ЛАБЕС — оползень", "ЛАБИРИНТ — комплекс пересекающихся долин/гряд", "ЛАКУС — ''озеро'' или малая равнина", "ПОСАДОЧНАЯ ПЛОЩАДКА", "МАРЕ — ''море'' на спутнике", "МЕНСА — меса", "МОНС — гора", "МОНТЕС — горный хребет", "ПАТЕРА — неправильный кратер", "ПЛАНИЦИЯ — низкая равнина", "ПЛАНУМ — высокая равнина или плато", "РУПЕС — обрыв или эскарп", "РИМА — трещина", "САКСУМ — валун", "ТЕРРА — обширный материк", "ТОЛУС — небольшая гора", "УНДАЕ — поле дюн"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(600,200,'ua','Розташування поселення','Геологічні об''єкти, що служать локаціями поселень на планетах і супутниках.',NULL,'["КАТЕНА — ланцюжок кратерів", "ХАОС — розламаний рельєф", "КОЛЛІС — невеликий пагорб", "КРАТЕР — ударна долина", "ДОРСУМ — гряда", "ВУЛКАНІЧНИЙ ЦЕНТР — вулкан", "ФОССА — западина", "ЛАБЕС — зсув", "ЛАБІРИНТ — комплекс пересічних долин/гряд", "ЛАКУС — ''озеро'' або мала рівнина", "МАЙДАНЧИК ДЛЯ ПОСАДКИ", "МАРЕ — ''море'' на супутнику", "МЕНСА — меса", "МОНС — гора", "МОНТЕС — гірський хребет", "ПАТЕРА — нерегулярний кратер", "ПЛАНІЦІЯ — низька рівнина", "ПЛАНУМ — висока рівнина або плато", "РУПЕС — обрив або ескарп", "РІМА — тріщина", "САКСУМ — валун", "ТЕРРА — обширний материк", "ТОЛУС — невелика гора", "УНДАЕ — поле дюн"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(601,201,'en','Control Faction','Roll to determine which type of organisation controls this settlement.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(602,201,'ru','Управляющая фракция','Бросьте, чтобы определить тип организации, контролирующей поселение.',NULL,'["Религиозная организация", "Корпорация", "Правительство", "Профсоюз", "Преступная организация"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(603,201,'ua','Керуюча фракція','Киньте, щоб визначити тип організації, що контролює поселення.',NULL,'["Релігійна організація", "Корпорація", "Уряд", "Профспілка", "Злочинна організація"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(604,202,'en','Population','Roll to determine the population of a settlement.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(605,202,'ru','Население','Бросьте, чтобы определить население поселения.',NULL,'["Один человек.", "Небольшая горстка людей.", "Несколько десятков человек.", "Около сотни людей.", "Несколько сотен человек.", "Около тысячи человек.", "Перенаселено."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(606,202,'ua','Населення','Киньте, щоб визначити населення поселення.',NULL,'["Одна людина.", "Невелика жменька людей.", "Кілька десятків людей.", "Близько сотні людей.", "Кілька сотень людей.", "Близько тисячі людей.", "Перенаселено."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(607,203,'en','Factions Table','Roll to determine a faction present or relevant in the current setting.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(608,203,'ru','Таблица фракций','Бросьте, чтобы определить фракцию, присутствующую или актуальную в текущем сеттинге.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(609,203,'ua','Таблиця фракцій','Киньте, щоб визначити фракцію, присутню або актуальну у поточному сеттингу.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(610,204,'en','Port Class','Roll to determine the class of a port encountered by the crew.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(611,204,'ru','Класс порта','Бросьте, чтобы определить класс порта, с которым столкнулась команда.',NULL,'["Порт X-класса — Заброшен. Без сервиса. Опасен.", "Порт C-класса — Базовая стыковка и заправка. Минимальные удобства.", "Порт B-класса — Стандартные услуги, местные рынки, некоторые варианты берегового отпуска.", "Порт A-класса — Хорошо оснащённый узел. Хорошее медобслуживание, береговой отпуск и торговля.", "Порт S-класса — Крупный транзитный узел. Полный сервис. Доступен люксовый береговой отпуск."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(612,204,'ua','Клас порту','Киньте, щоб визначити клас порту, з яким зіткнулася команда.',NULL,'["Порт X-класу — Покинутий. Без сервісу. Небезпечний.", "Порт C-класу — Базове стикування та заправка. Мінімальні зручності.", "Порт B-класу — Стандартні послуги, місцеві ринки, деякі варіанти берегового відпочинку.", "Порт A-класу — Добре обладнаний вузол. Хороше медобслуговування, береговий відпочинок і торгівля.", "Порт S-класу — Великий транзитний вузол. Повний сервіс. Доступний розкішний береговий відпочинок."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(613,205,'en','Settlement Type','Roll for the settlement''s type, then separately for Conditions and Weird.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(614,205,'ru','Тип поселения','Бросьте для типа поселения, затем отдельно для Условий и Странностей.',NULL,'["Трущобы принудительного переселения", "Колония терраформеров", "Горная колония", "Колониальное поселение", "Морской гарнизон", "Исследовательский центр", "Корпоративный операционный центр", "Производственный комплекс", "Глубоководная исследовательская база", "Комплекс тяжёлой промышленности", "Центр логистики и перевозок", "Рудный завод", "Передовая военная база", "Захолустная установка", "Корпоративный склад снабжения", "Наблюдательный пост", "Внеземная учебная установка", "Полярная исследовательская станция", "Закрытый испытательный полигон", "Комплекс тюрьмы строгого режима", "Лагерь акционеров", "Фермерская колония", "Бывшая тюрьма, ранее… (бросьте ещё раз)", "Зона автономного завода", "Независимое фронтирное поселение", "Тайная пиратская база", "Засекреченная корпоративная установка", "Безлюдный свалочный мир", "Крупное колониальное поселение", "Религиозная резиденция", "База антикорпоративных повстанцев", "Нераскрытый чёрный объект", "Частный игровой заповедник C-Suite"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(615,205,'ua','Тип поселення','Киньте для типу поселення, потім окремо для Умов і Дивацтв.',NULL,'["Нетрі примусового переселення", "Колонія терраформерів", "Гірська колонія", "Колоніальне поселення", "Морський гарнізон", "Дослідницький центр", "Корпоративний операційний центр", "Виробничий комплекс", "Глибоководна дослідницька база", "Комплекс важкої промисловості", "Центр логістики та перевезень", "Рудний завод", "Передова військова база", "Захолустна установка", "Корпоративний склад постачання", "Спостережний пост", "Позаземна навчальна установка", "Полярна дослідницька станція", "Закритий випробувальний полігон", "Комплекс тюрми суворого режиму", "Табір акціонерів", "Фермерська колонія", "Колишня тюрма, раніше… (киньте ще раз)", "Зона автономного заводу", "Незалежне фронтирне поселення", "Таємна піратська база", "Засекречена корпоративна установка", "Безлюдний смітниковий світ", "Велике колоніальне поселення", "Релігійна садиба", "База антикорпоративних повстанців", "Нерозкритий чорний об''єкт", "Приватний ігровий заповідник C-Suite"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(616,206,'en','Random Lore','Roll for a cryptic piece of galactic lore — a rumour, legend, or whispered name that can inspire an adventure or haunt the setting.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(617,206,'ru','Случайный лор','Бросьте для случайного фрагмента галактического предания — слуха, легенды или таинственного имени, способного вдохновить на приключение.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(618,206,'ua','Випадковий лор','Киньте для випадкового фрагменту галактичного переказу — чутки, легенди або загадкового імені, що може надихнути на пригоду.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(619,207,'en','Planet Size & Gravity','Roll separately for each planet column: Surface / Size & Gravity / Atmosphere / Climate.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(620,207,'ru','Размер и гравитация планеты','Бросайте отдельно для каждого столбца: Поверхность / Размер и гравитация / Атмосфера / Климат.',NULL,'["Гигант (Дробящая гравитация)", "Мини-гигант (Тяжёлая гравитация)", "Земного размера (Нормальная гравитация)", "Карликовая (Лёгкая гравитация)"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(621,207,'ua','Розмір і гравітація планети','Кидайте окремо для кожного стовпця: Поверхня / Розмір і гравітація / Атмосфера / Клімат.',NULL,'["Гігант (Роздроблювальна гравітація)", "Міні-гігант (Важка гравітація)", "Земного розміру (Нормальна гравітація)", "Карликова (Легка гравітація)"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(622,208,'en','Planet Atmosphere','Roll separately for each planet column: Surface / Size & Gravity / Atmosphere / Climate.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(623,208,'ru','Атмосфера планеты','Бросайте отдельно для каждого столбца: Поверхность / Размер и гравитация / Атмосфера / Климат.',NULL,'["Едкая", "Токсичная", "Разреженная", "Терраформированная", "Первозданная"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(624,208,'ua','Атмосфера планети','Кидайте окремо для кожного стовпця: Поверхня / Розмір і гравітація / Атмосфера / Клімат.',NULL,'["Їдка", "Токсична", "Розріджена", "Терраформована", "Первозданна"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(625,209,'en','Planet Climate','Roll separately for each planet column: Surface / Size & Gravity / Atmosphere / Climate.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(626,209,'ru','Климат планеты','Бросайте отдельно для каждого столбца: Поверхность / Размер и гравитация / Атмосфера / Климат.',NULL,'["Адский", "Горячий", "Тёплый", "Умеренный", "Небесный", "Дождливый", "Бурный", "Холодный", "Морозный"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(627,209,'ua','Клімат планети','Кидайте окремо для кожного стовпця: Поверхня / Розмір і гравітація / Атмосфера / Клімат.',NULL,'["Пекельний", "Гарячий", "Теплий", "Помірний", "Небесний", "Дощовий", "Бурхливий", "Холодний", "Морозний"]');
INSERT OR IGNORE INTO "content_i18n" VALUES(628,210,'en','Settlement Conditions','Roll for current conditions in this settlement.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(629,210,'ru','Условия в поселении','Бросьте для текущих условий в поселении.',NULL,'["На карантине.", "Перегружены, устали, низкий моральный дух.", "Всё как обычно.", "Рабочие бастуют.", "Опасные условия труда.", "Контроль у сил безопасности.", "Грубое управленческое нарушение.", "Частые бури.", "Низкая производительность.", "Вызваны корпоративные штрейкбрехеры.", "Враждебная дикая природа.", "Военная блокада.", "Буйные джунгли.", "В отчаянной нужде в помощи.", "Пугающе нестабильная погода.", "Нехватка еды.", "Колонисты говорят о вступлении в профсоюз.", "Ждут приказов от корпоратов.", "Местные выборы в профсоюз.", "Срыв переговоров по контракту.", "Мало запасов.", "Массовый неурожай.", "Связь отрезана.", "Корпоративные праздничные торжества.", "Под постоянной угрозой террористических атак.", "Местное правительство рушится.", "Слухи о сокращениях.", "Проблема перенаселения.", "Поселение закрывается корпоратами.", "Мелкие склоки выходят из-под контроля.", "Население полностью синтетическое.", "Занят военными как временная база.", "Назревает мятеж."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(630,210,'ua','Умови в поселенні','Киньте для поточних умов у поселенні.',NULL,'["На карантині.", "Перевантажені, втомлені, низький моральний дух.", "Все як завжди.", "Робітники страйкують.", "Небезпечні умови праці.", "Контроль у сил безпеки.", "Грубе управлінське порушення.", "Часті бурі.", "Низька продуктивність.", "Викликані корпоративні страйкбрехери.", "Ворожа дика природа.", "Військова блокада.", "Буйні джунглі.", "У відчайдушній потребі допомоги.", "Лячно нестабільна погода.", "Нестача їжі.", "Колоністи говорять про вступ у профспілку.", "Чекають наказів від корпорацій.", "Місцеві вибори у профспілку.", "Зрив переговорів за контрактом.", "Мало запасів.", "Масовий неврожай.", "Зв''язок відрізаний.", "Корпоративні святкові урочистості.", "Під постійною загрозою терористичних атак.", "Місцевий уряд руйнується.", "Чутки про скорочення.", "Проблема перенаселення.", "Поселення закривається корпораціями.", "Дрібні сварки виходять з-під контролю.", "Населення повністю синтетичне.", "Зайнятий військовими як тимчасова база.", "Назріває бунт."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(631,211,'en','Settlement Weird','Roll for a weird element unique to this settlement.',NULL,NULL);
INSERT OR IGNORE INTO "content_i18n" VALUES(632,211,'ru','Странности поселения','Бросьте для странного элемента, присущего этому поселению.',NULL,'["Провалившаяся утопия.", "Нераскрытая серия жестоких убийств.", "Здесь орудует мощный криминальный синдикат.", "Местные обычаи странные, чужаков опасаются.", "Покинут.", "Втайне является корпоративным лагерем перевоспитания.", "Поселение обрело новое религиозное значение.", "Компания тайно добавляет что-то в воду.", "Активная ситуация с заложниками.", "Местная среда — радиоактивная пустошь.", "Стремительно растущий апокалиптический культ.", "Под контролем сепаратистской милиции.", "Распад местного общественного порядка.", "Кризис беженцев.", "Событие вымирания.", "Поселение скатилось в анархию.", "Колонисты сообщают, что их заменяют самозванцами.", "Недавно прибыла тайная военная операция.", "Смертельная вирусная вспышка.", "Надвигается экологический коллапс.", "Недавнее прорывное открытие.", "В поселении обитает декадентская корпоративная знать.", "Колонисты медленно исчезают.", "Обнаружен странный чёрный монолит.", "Слухи о вмешательстве мощного ИИ.", "Колонисты верят, что поселение проклято.", "Восстание андроидов вот-вот произойдёт.", "Гигантские неопознанные окаменелые останки.", "Сообщения о вмешательстве «Небожителей».", "Обломки космического корабля неизвестного происхождения.", "Обнаружены руины звёздной цивилизации предшественников.", "Недавно обнаружен древний портал.", "Событие Первого Контакта."]');
INSERT OR IGNORE INTO "content_i18n" VALUES(633,211,'ua','Дивацтва поселення','Киньте для дивного елементу, притаманного цьому поселенню.',NULL,'["Провалена утопія.", "Нерозкрита серія жорстоких вбивств.", "Тут діє потужний злочинний синдикат.", "Місцеві звичаї дивні, чужинців остерігаються.", "Покинутий.", "Таємно є корпоративним табором перевиховання.", "Поселення набуло нового релігійного значення.", "Компанія таємно додає щось у воду.", "Активна ситуація з заручниками.", "Місцеве середовище — радіоактивне пустище.", "Стрімко зростаючий апокаліптичний культ.", "Під контролем сепаратистської міліції.", "Розпад місцевого суспільного порядку.", "Криза біженців.", "Подія вимирання.", "Поселення скотилося в анархію.", "Колоністи повідомляють, що їх замінюють самозванцями.", "Нещодавно прибула таємна військова операція.", "Смертельний вірусний спалах.", "Наближається екологічний колапс.", "Нещодавнє проривне відкриття.", "У поселенні живе декадентська корпоративна знать.", "Колоністи повільно зникають.", "Виявлено дивний чорний моноліт.", "Чутки про втручання потужного ШІ.", "Колоністи вважають, що поселення проклято.", "Повстання андроїдів ось-ось станеться.", "Гігантські невпізнані скам''янілі залишки.", "Повідомлення про втручання «Небожителів».", "Уламки космічного корабля невідомого походження.", "Виявлено руїни зіркової цивілізації попередників.", "Нещодавно виявлено стародавні ворота.", "Подія Першого Контакту."]');
-- page_contents
INSERT OR IGNORE INTO "page_contents" VALUES(3,23,0);
INSERT OR IGNORE INTO "page_contents" VALUES(3,24,1);
INSERT OR IGNORE INTO "page_contents" VALUES(3,25,2);
INSERT OR IGNORE INTO "page_contents" VALUES(3,26,3);
INSERT OR IGNORE INTO "page_contents" VALUES(3,27,4);
INSERT OR IGNORE INTO "page_contents" VALUES(3,28,5);
INSERT OR IGNORE INTO "page_contents" VALUES(3,29,6);
INSERT OR IGNORE INTO "page_contents" VALUES(4,30,7);
INSERT OR IGNORE INTO "page_contents" VALUES(4,31,8);
INSERT OR IGNORE INTO "page_contents" VALUES(4,32,9);
INSERT OR IGNORE INTO "page_contents" VALUES(4,33,10);
INSERT OR IGNORE INTO "page_contents" VALUES(4,34,11);
INSERT OR IGNORE INTO "page_contents" VALUES(4,35,12);
INSERT OR IGNORE INTO "page_contents" VALUES(4,36,13);
INSERT OR IGNORE INTO "page_contents" VALUES(5,37,14);
INSERT OR IGNORE INTO "page_contents" VALUES(5,38,15);
INSERT OR IGNORE INTO "page_contents" VALUES(5,39,16);
INSERT OR IGNORE INTO "page_contents" VALUES(5,40,17);
INSERT OR IGNORE INTO "page_contents" VALUES(2,1,1);
INSERT OR IGNORE INTO "page_contents" VALUES(2,2,2);
INSERT OR IGNORE INTO "page_contents" VALUES(2,3,3);
INSERT OR IGNORE INTO "page_contents" VALUES(2,4,4);
INSERT OR IGNORE INTO "page_contents" VALUES(2,5,5);
INSERT OR IGNORE INTO "page_contents" VALUES(2,6,6);
INSERT OR IGNORE INTO "page_contents" VALUES(2,7,7);
INSERT OR IGNORE INTO "page_contents" VALUES(2,8,8);
INSERT OR IGNORE INTO "page_contents" VALUES(2,9,9);
INSERT OR IGNORE INTO "page_contents" VALUES(2,10,10);
INSERT OR IGNORE INTO "page_contents" VALUES(2,11,11);
INSERT OR IGNORE INTO "page_contents" VALUES(2,12,12);
INSERT OR IGNORE INTO "page_contents" VALUES(2,13,13);
INSERT OR IGNORE INTO "page_contents" VALUES(2,14,14);
INSERT OR IGNORE INTO "page_contents" VALUES(2,15,15);
INSERT OR IGNORE INTO "page_contents" VALUES(2,16,16);
INSERT OR IGNORE INTO "page_contents" VALUES(2,17,17);
INSERT OR IGNORE INTO "page_contents" VALUES(2,18,18);
INSERT OR IGNORE INTO "page_contents" VALUES(2,19,19);
INSERT OR IGNORE INTO "page_contents" VALUES(2,20,20);
INSERT OR IGNORE INTO "page_contents" VALUES(2,21,21);
INSERT OR IGNORE INTO "page_contents" VALUES(2,22,22);
INSERT OR IGNORE INTO "page_contents" VALUES(6,41,41);
INSERT OR IGNORE INTO "page_contents" VALUES(6,42,42);
INSERT OR IGNORE INTO "page_contents" VALUES(6,43,43);
INSERT OR IGNORE INTO "page_contents" VALUES(6,44,44);
INSERT OR IGNORE INTO "page_contents" VALUES(6,45,45);
INSERT OR IGNORE INTO "page_contents" VALUES(7,46,46);
INSERT OR IGNORE INTO "page_contents" VALUES(8,47,47);
INSERT OR IGNORE INTO "page_contents" VALUES(8,48,48);
INSERT OR IGNORE INTO "page_contents" VALUES(8,49,49);
INSERT OR IGNORE INTO "page_contents" VALUES(8,50,50);
INSERT OR IGNORE INTO "page_contents" VALUES(9,51,51);
INSERT OR IGNORE INTO "page_contents" VALUES(9,52,52);
INSERT OR IGNORE INTO "page_contents" VALUES(9,53,53);
INSERT OR IGNORE INTO "page_contents" VALUES(9,54,54);
INSERT OR IGNORE INTO "page_contents" VALUES(10,57,57);
INSERT OR IGNORE INTO "page_contents" VALUES(10,58,58);
INSERT OR IGNORE INTO "page_contents" VALUES(10,59,59);
INSERT OR IGNORE INTO "page_contents" VALUES(10,60,60);
INSERT OR IGNORE INTO "page_contents" VALUES(10,61,61);
INSERT OR IGNORE INTO "page_contents" VALUES(10,62,62);
INSERT OR IGNORE INTO "page_contents" VALUES(10,63,63);
INSERT OR IGNORE INTO "page_contents" VALUES(10,64,64);
INSERT OR IGNORE INTO "page_contents" VALUES(10,65,65);
INSERT OR IGNORE INTO "page_contents" VALUES(10,66,66);
INSERT OR IGNORE INTO "page_contents" VALUES(10,67,67);
INSERT OR IGNORE INTO "page_contents" VALUES(10,68,68);
INSERT OR IGNORE INTO "page_contents" VALUES(10,69,69);
INSERT OR IGNORE INTO "page_contents" VALUES(10,70,70);
INSERT OR IGNORE INTO "page_contents" VALUES(10,71,71);
INSERT OR IGNORE INTO "page_contents" VALUES(10,72,72);
INSERT OR IGNORE INTO "page_contents" VALUES(10,73,73);
INSERT OR IGNORE INTO "page_contents" VALUES(10,74,74);
INSERT OR IGNORE INTO "page_contents" VALUES(10,75,75);
INSERT OR IGNORE INTO "page_contents" VALUES(10,76,76);
INSERT OR IGNORE INTO "page_contents" VALUES(10,77,77);
INSERT OR IGNORE INTO "page_contents" VALUES(10,78,78);
INSERT OR IGNORE INTO "page_contents" VALUES(10,79,79);
INSERT OR IGNORE INTO "page_contents" VALUES(10,80,80);
INSERT OR IGNORE INTO "page_contents" VALUES(10,81,81);
INSERT OR IGNORE INTO "page_contents" VALUES(10,82,82);
INSERT OR IGNORE INTO "page_contents" VALUES(10,83,83);
INSERT OR IGNORE INTO "page_contents" VALUES(10,84,84);
INSERT OR IGNORE INTO "page_contents" VALUES(10,85,85);
INSERT OR IGNORE INTO "page_contents" VALUES(10,86,86);
INSERT OR IGNORE INTO "page_contents" VALUES(10,87,87);
INSERT OR IGNORE INTO "page_contents" VALUES(10,88,88);
INSERT OR IGNORE INTO "page_contents" VALUES(10,89,89);
INSERT OR IGNORE INTO "page_contents" VALUES(10,90,90);
INSERT OR IGNORE INTO "page_contents" VALUES(10,91,91);
INSERT OR IGNORE INTO "page_contents" VALUES(10,92,92);
INSERT OR IGNORE INTO "page_contents" VALUES(10,93,93);
INSERT OR IGNORE INTO "page_contents" VALUES(10,94,94);
INSERT OR IGNORE INTO "page_contents" VALUES(10,95,95);
INSERT OR IGNORE INTO "page_contents" VALUES(10,96,96);
INSERT OR IGNORE INTO "page_contents" VALUES(10,97,97);
INSERT OR IGNORE INTO "page_contents" VALUES(10,98,98);
INSERT OR IGNORE INTO "page_contents" VALUES(10,99,99);
INSERT OR IGNORE INTO "page_contents" VALUES(11,100,100);
INSERT OR IGNORE INTO "page_contents" VALUES(11,101,101);
INSERT OR IGNORE INTO "page_contents" VALUES(11,102,102);
INSERT OR IGNORE INTO "page_contents" VALUES(12,103,103);
INSERT OR IGNORE INTO "page_contents" VALUES(12,104,104);
INSERT OR IGNORE INTO "page_contents" VALUES(12,105,105);
INSERT OR IGNORE INTO "page_contents" VALUES(16,106,106);
INSERT OR IGNORE INTO "page_contents" VALUES(16,107,107);
INSERT OR IGNORE INTO "page_contents" VALUES(16,108,108);
INSERT OR IGNORE INTO "page_contents" VALUES(16,109,109);
INSERT OR IGNORE INTO "page_contents" VALUES(16,110,110);
INSERT OR IGNORE INTO "page_contents" VALUES(16,111,111);
INSERT OR IGNORE INTO "page_contents" VALUES(16,112,112);
INSERT OR IGNORE INTO "page_contents" VALUES(16,113,113);
INSERT OR IGNORE INTO "page_contents" VALUES(16,114,114);
INSERT OR IGNORE INTO "page_contents" VALUES(16,115,115);
INSERT OR IGNORE INTO "page_contents" VALUES(16,116,116);
INSERT OR IGNORE INTO "page_contents" VALUES(16,117,117);
INSERT OR IGNORE INTO "page_contents" VALUES(16,118,118);
INSERT OR IGNORE INTO "page_contents" VALUES(16,119,119);
INSERT OR IGNORE INTO "page_contents" VALUES(16,120,120);
INSERT OR IGNORE INTO "page_contents" VALUES(16,121,121);
INSERT OR IGNORE INTO "page_contents" VALUES(17,122,122);
INSERT OR IGNORE INTO "page_contents" VALUES(17,123,123);
INSERT OR IGNORE INTO "page_contents" VALUES(17,124,124);
INSERT OR IGNORE INTO "page_contents" VALUES(17,125,125);
INSERT OR IGNORE INTO "page_contents" VALUES(17,126,126);
INSERT OR IGNORE INTO "page_contents" VALUES(17,127,127);
INSERT OR IGNORE INTO "page_contents" VALUES(17,128,128);
INSERT OR IGNORE INTO "page_contents" VALUES(17,129,129);
INSERT OR IGNORE INTO "page_contents" VALUES(17,130,130);
INSERT OR IGNORE INTO "page_contents" VALUES(17,131,131);
INSERT OR IGNORE INTO "page_contents" VALUES(17,132,132);
INSERT OR IGNORE INTO "page_contents" VALUES(17,133,133);
INSERT OR IGNORE INTO "page_contents" VALUES(17,134,134);
INSERT OR IGNORE INTO "page_contents" VALUES(17,135,135);
INSERT OR IGNORE INTO "page_contents" VALUES(17,136,136);
INSERT OR IGNORE INTO "page_contents" VALUES(18,137,137);
INSERT OR IGNORE INTO "page_contents" VALUES(18,138,138);
INSERT OR IGNORE INTO "page_contents" VALUES(18,139,139);
INSERT OR IGNORE INTO "page_contents" VALUES(18,140,140);
INSERT OR IGNORE INTO "page_contents" VALUES(18,141,141);
INSERT OR IGNORE INTO "page_contents" VALUES(18,142,142);
INSERT OR IGNORE INTO "page_contents" VALUES(18,143,143);
INSERT OR IGNORE INTO "page_contents" VALUES(18,144,144);
INSERT OR IGNORE INTO "page_contents" VALUES(18,145,145);
INSERT OR IGNORE INTO "page_contents" VALUES(18,146,146);
INSERT OR IGNORE INTO "page_contents" VALUES(18,147,147);
INSERT OR IGNORE INTO "page_contents" VALUES(19,148,148);
INSERT OR IGNORE INTO "page_contents" VALUES(19,149,149);
INSERT OR IGNORE INTO "page_contents" VALUES(14,150,0);
INSERT OR IGNORE INTO "page_contents" VALUES(14,151,1);
INSERT OR IGNORE INTO "page_contents" VALUES(14,152,2);
INSERT OR IGNORE INTO "page_contents" VALUES(14,153,3);
INSERT OR IGNORE INTO "page_contents" VALUES(14,154,4);
INSERT OR IGNORE INTO "page_contents" VALUES(14,155,5);
INSERT OR IGNORE INTO "page_contents" VALUES(14,156,6);
INSERT OR IGNORE INTO "page_contents" VALUES(14,157,7);
INSERT OR IGNORE INTO "page_contents" VALUES(15,158,0);
INSERT OR IGNORE INTO "page_contents" VALUES(15,159,1);
INSERT OR IGNORE INTO "page_contents" VALUES(15,160,2);
INSERT OR IGNORE INTO "page_contents" VALUES(15,161,3);
INSERT OR IGNORE INTO "page_contents" VALUES(15,162,4);
INSERT OR IGNORE INTO "page_contents" VALUES(15,163,5);
INSERT OR IGNORE INTO "page_contents" VALUES(15,164,6);
INSERT OR IGNORE INTO "page_contents" VALUES(15,165,7);
INSERT OR IGNORE INTO "page_contents" VALUES(15,166,8);
INSERT OR IGNORE INTO "page_contents" VALUES(20,167,0);
INSERT OR IGNORE INTO "page_contents" VALUES(20,168,1);
INSERT OR IGNORE INTO "page_contents" VALUES(21,169,0);
INSERT OR IGNORE INTO "page_contents" VALUES(21,170,1);
INSERT OR IGNORE INTO "page_contents" VALUES(21,171,2);
INSERT OR IGNORE INTO "page_contents" VALUES(7,55,55);
INSERT OR IGNORE INTO "page_contents" VALUES(7,56,56);
INSERT OR IGNORE INTO "page_contents" VALUES(24,172,172);
INSERT OR IGNORE INTO "page_contents" VALUES(24,173,173);
INSERT OR IGNORE INTO "page_contents" VALUES(24,174,174);
INSERT OR IGNORE INTO "page_contents" VALUES(24,175,175);
INSERT OR IGNORE INTO "page_contents" VALUES(24,176,176);
INSERT OR IGNORE INTO "page_contents" VALUES(24,177,177);
INSERT OR IGNORE INTO "page_contents" VALUES(24,178,178);
INSERT OR IGNORE INTO "page_contents" VALUES(25,179,179);
INSERT OR IGNORE INTO "page_contents" VALUES(25,180,180);
INSERT OR IGNORE INTO "page_contents" VALUES(25,181,181);
INSERT OR IGNORE INTO "page_contents" VALUES(25,182,182);
INSERT OR IGNORE INTO "page_contents" VALUES(26,183,183);
INSERT OR IGNORE INTO "page_contents" VALUES(26,184,184);
INSERT OR IGNORE INTO "page_contents" VALUES(26,185,185);
INSERT OR IGNORE INTO "page_contents" VALUES(26,186,186);
INSERT OR IGNORE INTO "page_contents" VALUES(26,187,187);
INSERT OR IGNORE INTO "page_contents" VALUES(26,188,188);
INSERT OR IGNORE INTO "page_contents" VALUES(26,189,189);
INSERT OR IGNORE INTO "page_contents" VALUES(26,190,190);
INSERT OR IGNORE INTO "page_contents" VALUES(27,191,191);
INSERT OR IGNORE INTO "page_contents" VALUES(27,192,192);
INSERT OR IGNORE INTO "page_contents" VALUES(27,193,193);
INSERT OR IGNORE INTO "page_contents" VALUES(27,194,194);
INSERT OR IGNORE INTO "page_contents" VALUES(27,195,195);
INSERT OR IGNORE INTO "page_contents" VALUES(27,196,196);
INSERT OR IGNORE INTO "page_contents" VALUES(27,197,197);
INSERT OR IGNORE INTO "page_contents" VALUES(27,198,198);
INSERT OR IGNORE INTO "page_contents" VALUES(28,206,13);
INSERT OR IGNORE INTO "page_contents" VALUES(29,199,1);
INSERT OR IGNORE INTO "page_contents" VALUES(29,207,2);
INSERT OR IGNORE INTO "page_contents" VALUES(29,208,3);
INSERT OR IGNORE INTO "page_contents" VALUES(29,209,4);
INSERT OR IGNORE INTO "page_contents" VALUES(30,200,1);
INSERT OR IGNORE INTO "page_contents" VALUES(30,201,2);
INSERT OR IGNORE INTO "page_contents" VALUES(30,202,3);
INSERT OR IGNORE INTO "page_contents" VALUES(30,203,4);
INSERT OR IGNORE INTO "page_contents" VALUES(30,204,5);
INSERT OR IGNORE INTO "page_contents" VALUES(30,205,6);
INSERT OR IGNORE INTO "page_contents" VALUES(30,210,7);
INSERT OR IGNORE INTO "page_contents" VALUES(30,211,8);
-- content_links
INSERT OR IGNORE INTO "content_links" VALUES(26,29,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(26,27,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(27,30,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(30,31,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(30,32,'see_also',1);
INSERT OR IGNORE INTO "content_links" VALUES(30,33,'see_also',2);
INSERT OR IGNORE INTO "content_links" VALUES(30,34,'see_also',3);
INSERT OR IGNORE INTO "content_links" VALUES(30,35,'see_also',4);
INSERT OR IGNORE INTO "content_links" VALUES(30,36,'see_also',5);
INSERT OR IGNORE INTO "content_links" VALUES(2,37,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(2,35,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(3,38,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(3,33,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(4,37,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(4,31,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(5,38,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(5,34,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(6,39,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(6,34,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(7,38,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(7,31,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(8,38,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(8,34,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(9,39,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(9,33,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(10,37,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(10,32,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(11,39,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(11,32,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(11,35,'related',2);
INSERT OR IGNORE INTO "content_links" VALUES(12,38,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(12,32,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(13,39,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(13,33,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(14,38,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(14,33,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(15,38,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(15,32,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(16,37,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(16,32,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(17,40,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(17,33,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(18,39,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(18,33,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(19,37,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(19,31,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(20,38,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(20,31,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(21,37,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(21,31,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(22,37,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(22,32,'related',1);
INSERT OR IGNORE INTO "content_links" VALUES(22,35,'related',2);
INSERT OR IGNORE INTO "content_links" VALUES(41,28,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(42,28,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(43,28,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(44,28,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(45,28,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(103,104,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(104,105,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(106,122,'prerequisite',0);
INSERT OR IGNORE INTO "content_links" VALUES(107,122,'prerequisite',1);
INSERT OR IGNORE INTO "content_links" VALUES(107,123,'prerequisite',2);
INSERT OR IGNORE INTO "content_links" VALUES(107,124,'prerequisite',3);
INSERT OR IGNORE INTO "content_links" VALUES(108,123,'prerequisite',4);
INSERT OR IGNORE INTO "content_links" VALUES(108,125,'prerequisite',5);
INSERT OR IGNORE INTO "content_links" VALUES(108,136,'prerequisite',6);
INSERT OR IGNORE INTO "content_links" VALUES(109,125,'prerequisite',7);
INSERT OR IGNORE INTO "content_links" VALUES(109,126,'prerequisite',8);
INSERT OR IGNORE INTO "content_links" VALUES(110,126,'prerequisite',9);
INSERT OR IGNORE INTO "content_links" VALUES(110,127,'prerequisite',10);
INSERT OR IGNORE INTO "content_links" VALUES(111,127,'prerequisite',11);
INSERT OR IGNORE INTO "content_links" VALUES(111,128,'prerequisite',12);
INSERT OR IGNORE INTO "content_links" VALUES(112,128,'prerequisite',13);
INSERT OR IGNORE INTO "content_links" VALUES(112,129,'prerequisite',14);
INSERT OR IGNORE INTO "content_links" VALUES(113,130,'prerequisite',15);
INSERT OR IGNORE INTO "content_links" VALUES(114,131,'prerequisite',16);
INSERT OR IGNORE INTO "content_links" VALUES(115,132,'prerequisite',17);
INSERT OR IGNORE INTO "content_links" VALUES(116,133,'prerequisite',18);
INSERT OR IGNORE INTO "content_links" VALUES(117,133,'prerequisite',19);
INSERT OR IGNORE INTO "content_links" VALUES(118,133,'prerequisite',20);
INSERT OR IGNORE INTO "content_links" VALUES(119,128,'prerequisite',21);
INSERT OR IGNORE INTO "content_links" VALUES(119,134,'prerequisite',22);
INSERT OR IGNORE INTO "content_links" VALUES(119,135,'prerequisite',23);
INSERT OR IGNORE INTO "content_links" VALUES(120,134,'prerequisite',24);
INSERT OR IGNORE INTO "content_links" VALUES(120,135,'prerequisite',25);
INSERT OR IGNORE INTO "content_links" VALUES(121,135,'prerequisite',26);
INSERT OR IGNORE INTO "content_links" VALUES(122,137,'prerequisite',27);
INSERT OR IGNORE INTO "content_links" VALUES(123,138,'prerequisite',28);
INSERT OR IGNORE INTO "content_links" VALUES(123,139,'prerequisite',29);
INSERT OR IGNORE INTO "content_links" VALUES(124,139,'prerequisite',30);
INSERT OR IGNORE INTO "content_links" VALUES(125,140,'prerequisite',31);
INSERT OR IGNORE INTO "content_links" VALUES(126,140,'prerequisite',32);
INSERT OR IGNORE INTO "content_links" VALUES(127,141,'prerequisite',33);
INSERT OR IGNORE INTO "content_links" VALUES(127,142,'prerequisite',34);
INSERT OR IGNORE INTO "content_links" VALUES(127,143,'prerequisite',35);
INSERT OR IGNORE INTO "content_links" VALUES(130,144,'prerequisite',36);
INSERT OR IGNORE INTO "content_links" VALUES(131,145,'prerequisite',37);
INSERT OR IGNORE INTO "content_links" VALUES(131,147,'prerequisite',38);
INSERT OR IGNORE INTO "content_links" VALUES(132,145,'prerequisite',39);
INSERT OR IGNORE INTO "content_links" VALUES(133,145,'prerequisite',40);
INSERT OR IGNORE INTO "content_links" VALUES(133,146,'prerequisite',41);
INSERT OR IGNORE INTO "content_links" VALUES(134,147,'prerequisite',42);
INSERT OR IGNORE INTO "content_links" VALUES(148,149,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(27,36,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(31,36,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(32,36,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(33,36,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(34,36,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(35,36,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(32,151,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(33,151,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(35,151,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(154,36,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(156,36,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(100,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(101,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(26,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(102,104,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(24,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(150,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(153,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(154,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(155,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(157,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(158,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(159,105,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(159,160,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(159,161,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(159,162,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(159,163,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(159,164,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(159,165,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(159,166,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(161,105,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(164,30,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(165,30,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(152,98,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(155,43,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(103,168,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(29,28,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(47,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(47,104,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(47,119,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(47,121,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(48,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(48,106,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(48,113,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(48,115,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(49,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(49,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(50,104,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(50,110,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(50,114,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(46,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(58,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(58,158,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(67,30,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(68,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(68,34,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(68,91,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(69,151,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(72,155,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(82,157,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(83,42,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(83,154,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(85,42,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(87,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(87,104,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(88,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(88,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(90,155,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(92,150,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(98,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(98,152,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(98,156,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(98,36,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(167,168,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(168,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(168,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(168,104,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(169,30,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(170,169,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(171,169,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(171,170,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(66,91,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(91,96,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(73,97,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(172,173,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(172,174,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(172,175,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(172,176,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(174,36,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(175,189,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(177,188,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(178,199,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(178,200,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(179,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(179,104,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(180,179,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(181,179,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(182,181,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(183,100,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(183,101,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(184,183,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(185,183,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(185,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(186,100,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(186,102,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(187,184,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(188,23,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(188,184,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(188,30,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(189,185,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(190,188,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(190,23,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(191,192,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(193,194,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(194,203,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(195,196,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(195,168,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(196,168,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(196,169,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(197,196,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(197,167,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(198,168,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(198,103,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(199,200,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(199,150,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(200,201,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(200,202,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(200,205,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(201,203,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(202,205,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(203,194,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(204,167,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(204,168,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(205,199,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(205,204,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(206,179,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(206,180,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(199,207,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(199,208,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(199,209,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(205,210,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(205,211,'see_also',0);
INSERT OR IGNORE INTO "content_links" VALUES(42,154,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(42,150,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(42,96,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(43,154,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(43,155,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(43,150,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(43,96,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(43,92,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(154,42,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(154,43,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(155,90,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,44,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,45,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,41,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,42,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,43,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,44,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,41,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,42,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,43,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,41,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,42,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,43,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,2,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,3,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,5,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,8,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,9,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,13,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,14,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,16,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,17,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,18,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,73,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,74,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(51,98,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,7,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,8,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,14,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,16,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,17,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,19,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,20,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,61,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,69,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(52,77,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,5,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,7,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,15,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,16,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,20,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,58,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,61,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,64,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,83,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(53,90,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,3,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,4,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,6,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,11,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,12,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,14,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,15,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,22,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,57,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,68,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,85,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,94,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(54,99,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(44,96,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(45,96,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(45,62,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(45,73,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(45,155,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(45,154,'related',0);
INSERT OR IGNORE INTO "content_links" VALUES(45,150,'related',0);
