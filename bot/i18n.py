"""
i18n.py — UI string translations for the Mothership bot.

Content data translations live in the seed JSON files as _ua / _ru columns.
This module handles static UI strings only.

Usage:
    from .i18n import t
    t("ua", "btn_back")           → "← Назад"
    t("ua", "btn_roll", dice="D10") → "🎲 Кинути D10!"
"""

SUPPORTED_LANGS = ("en", "ua", "ru")
DEFAULT_LANG = "en"

_STRINGS: dict[str, dict[str, str]] = {
    "en": {
        # ── Main menu ──────────────────────────────
        "main_menu_title": "🚀 <b>Mothership RPG Reference</b>",
        "main_menu_desc": (
            "Your table-side handbook. Browse rules, roll tables, look up gear "
            "and NPCs — all from the source books."
        ),
        "main_menu_select": "Select a category:",

        # ── Language selection ─────────────────────
        "lang_title": "🌐 <b>Language / Мова / Язык</b>",
        "lang_select": "Select your language:",
        "lang_set_en": "✅ Language set to English.",
        "lang_set_ua": "✅ Language set to English.",
        "lang_set_ru": "✅ Language set to English.",

        # ── Search ────────────────────────────────
        "search_btn": "🔍 Search",
        "search_usage": (
            "Usage: <code>/search &lt;term&gt;</code>\n"
            "Example: <code>/search wound</code>"
        ),
        "search_prompt_title": "🔍 <b>Search</b>",
        "search_prompt_body": (
            "Send: <code>/search &lt;term&gt;</code>\n\n"
            "Example: <code>/search stress</code>"
        ),
        "search_no_results": (
            "🔍 No results found for <b>{query}</b>.\n\n"
            "Try a shorter term or different spelling."
        ),
        "search_results_header": "🔍 <b>Results for \"{query}\"</b> ({total} found)",
        "search_more": "…and {n} more",
        "search_section_rules": "Rules",
        "search_section_glossary": "Glossary",
        "search_section_equipment": "Equipment",
        "search_section_npcs": "NPCs",
        "search_section_locations": "Locations",
        "search_section_tables": "Roll Tables",

        # ── Nav buttons ────────────────────────────
        "btn_back": "← Back",
        "btn_main_menu": "← Main Menu",
        "btn_prev": "◀ Prev",
        "btn_next": "Next ▶",
        "btn_show_entries": "📋 Show All Entries",
        "btn_roll": "🎲 Roll on {dice}!",
        "btn_roll_again": "🎲 Roll Again ({dice})",
        "btn_page": "Page {page} / {total}",

        # ── Glossary ───────────────────────────────
        "glossary_select": "Select a term:",

        # ── Error / status messages ────────────────
        "err_category": "Category not found.",
        "err_rule": "Rule not found.",
        "err_term": "Term not found.",
        "err_item": "Item not found.",
        "err_table": "Table not found.",
        "err_no_roll": "No entry found for this roll.",
        "err_no_entries": "No entries found.",
        "err_entry": "Entry not found.",
        "err_class": "Class not found.",
        "err_skill": "Skill not found.",
        "err_ship": "Ship not found.",
        "err_location": "Location not found.",
        "err_npc": "NPC not found.",
        "err_not_implemented": "Not implemented yet.",

        # ── Formatters — term ──────────────────────
        "also_known_as": "Also known as: {aliases}",

        # ── Formatters — item ──────────────────────
        "item_cost": "Cost",
        "item_damage": "Damage",
        "item_range": "Range",
        "item_shots": "Shots",
        "item_wound": "Wound",
        "item_auto_attack": "⚡ <b>Auto-Attack (AA)</b> — no Combat Check needed",
        "item_special": "Special",
        "item_ap": "AP",
        "item_o2": "O2",
        "item_o2_none": "<b>O2:</b> None",
        "item_speed_penalty": "<b>Speed:</b> Disadvantage [-] on Speed checks",
        "item_damage_reduction": "Damage Reduction",

        # ── Formatters — roll table ────────────────
        "table_dice": "Dice",
        "table_usage": "Use the buttons below to roll or view all entries.",
        "table_entries_hint": "{n} entries — tap one to view details.",
        "roll_result_label": "Roll",

        # ── Formatters — class ─────────────────────
        "class_label": "Class",
        "class_stat_bonuses": "Stat Bonuses",
        "class_save_bonuses": "Save Bonuses",
        "class_max_wounds": "Max Wounds",
        "class_health": "Health",
        "class_special": "Special",
        "class_trauma": "Trauma Response",
        "class_preloaded_skills": "Preloaded Skills",
        "class_starting_skills": "Starting Skills",
        "class_bonus_skills": "Bonus Skills",

        # ── Formatters — skill ─────────────────────
        "skill_trained": "Trained (+10)",
        "skill_expert": "Expert (+15)",
        "skill_master": "Master (+20)",
        "skill_prerequisite": "Prerequisite",

        # ── Formatters — ship ──────────────────────
        "ship_stats": "Stats",
        "ship_thrusters": "Thrusters",
        "ship_weapons": "Weapons",
        "ship_systems": "Systems",
        "ship_hull": "Hull Points",
        "ship_megadamage": "Megadamage",
        "ship_fuel": "Fuel",
        "ship_crew": "Crew Capacity",
        "ship_cryopods": "Cryopods",
        "ship_escape_pods": "Escape Pods",
        "ship_hardpoints": "Hardpoints",
        "ship_upgrade_slots": "Upgrade Slots",

        # ── Formatters — location ──────────────────
        "loc_in": "In",

        # ── Formatters — NPC ──────────────────────
        "npc_location": "Location",
        "npc_stats": "Stats",
        "npc_wounds": "Wounds",
        "npc_hp_each": "HP each",
        "npc_ap": "AP",
        "npc_attacks": "Attacks",
        "npc_special": "Special",
    },

    "ua": {
        # ── Main menu ──────────────────────────────
        "main_menu_title": "🚀 <b>Mothership RPG — Довідник</b>",
        "main_menu_desc": (
            "Ваш настільний довідник. Правила, таблиці, спорядження та НПС — "
            "прямо з книг."
        ),
        "main_menu_select": "Оберіть категорію:",

        # ── Language selection ─────────────────────
        "lang_title": "🌐 <b>Language / Мова / Язык</b>",
        "lang_select": "Оберіть мову:",
        "lang_set_en": "✅ Мову встановлено: English.",
        "lang_set_ua": "✅ Мову встановлено: Українська.",
        "lang_set_ru": "✅ Мову встановлено: Русский.",

        # ── Search ────────────────────────────────
        "search_btn": "🔍 Пошук",
        "search_usage": (
            "Використання: <code>/search &lt;термін&gt;</code>\n"
            "Приклад: <code>/search wound</code>"
        ),
        "search_prompt_title": "🔍 <b>Пошук</b>",
        "search_prompt_body": (
            "Надішліть: <code>/search &lt;термін&gt;</code>\n\n"
            "Приклад: <code>/search stress</code>"
        ),
        "search_no_results": (
            "🔍 Нічого не знайдено за запитом <b>{query}</b>.\n\n"
            "Спробуйте коротший термін або іншу форму слова."
        ),
        "search_results_header": "🔍 <b>Результати для \"{query}\"</b> ({total} знайдено)",
        "search_more": "…ще {n}",
        "search_section_rules": "Правила",
        "search_section_glossary": "Глосарій",
        "search_section_equipment": "Спорядження",
        "search_section_npcs": "НПС",
        "search_section_locations": "Локації",
        "search_section_tables": "Таблиці",

        # ── Nav buttons ────────────────────────────
        "btn_back": "← Назад",
        "btn_main_menu": "← Головне меню",
        "btn_prev": "◀ Попередня",
        "btn_next": "Наступна ▶",
        "btn_show_entries": "📋 Всі записи",
        "btn_roll": "🎲 Кинути {dice}!",
        "btn_roll_again": "🎲 Кинути ще раз ({dice})",
        "btn_page": "Сторінка {page} / {total}",

        # ── Glossary ───────────────────────────────
        "glossary_select": "Оберіть термін:",

        # ── Error / status messages ────────────────
        "err_category": "Категорію не знайдено.",
        "err_rule": "Правило не знайдено.",
        "err_term": "Термін не знайдено.",
        "err_item": "Предмет не знайдено.",
        "err_table": "Таблицю не знайдено.",
        "err_no_roll": "Запис для цього кидка не знайдено.",
        "err_no_entries": "Записи не знайдено.",
        "err_entry": "Запис не знайдено.",
        "err_class": "Клас не знайдено.",
        "err_skill": "Навичку не знайдено.",
        "err_ship": "Корабель не знайдено.",
        "err_location": "Локацію не знайдено.",
        "err_npc": "НПС не знайдено.",
        "err_not_implemented": "Ще не реалізовано.",

        # ── Formatters — term ──────────────────────
        "also_known_as": "Також відомий як: {aliases}",

        # ── Formatters — item ──────────────────────
        "item_cost": "Вартість",
        "item_damage": "Пошкодження",
        "item_range": "Дальність",
        "item_shots": "Набої",
        "item_wound": "Поранення",
        "item_auto_attack": "⚡ <b>Авто-атака (AA)</b> — перевірка бою не потрібна",
        "item_special": "Особливе",
        "item_ap": "ЗБ",
        "item_o2": "Кисень",
        "item_o2_none": "<b>Кисень:</b> Немає",
        "item_speed_penalty": "<b>Швидкість:</b> Перешкода [-] на перевірки швидкості",
        "item_damage_reduction": "Зниження пошкоджень",

        # ── Formatters — roll table ────────────────
        "table_dice": "Кубик",
        "table_usage": "Використовуйте кнопки нижче для кидка або перегляду всіх записів.",
        "table_entries_hint": "{n} записів — натисніть для перегляду.",
        "roll_result_label": "Кидок",

        # ── Formatters — class ─────────────────────
        "class_label": "Клас",
        "class_stat_bonuses": "Бонуси до характеристик",
        "class_save_bonuses": "Бонуси до рятівних кидків",
        "class_max_wounds": "Макс. поранень",
        "class_health": "Здоров'я",
        "class_special": "Особливе",
        "class_trauma": "Реакція на травму",
        "class_preloaded_skills": "Початкові навички",
        "class_starting_skills": "Початкові навички",
        "class_bonus_skills": "Бонусні навички",

        # ── Formatters — skill ─────────────────────
        "skill_trained": "Навчений (+10)",
        "skill_expert": "Досвідчений (+15)",
        "skill_master": "Майстер (+20)",
        "skill_prerequisite": "Передумова",

        # ── Formatters — ship ──────────────────────
        "ship_stats": "Характеристики",
        "ship_thrusters": "Двигуни",
        "ship_weapons": "Зброя",
        "ship_systems": "Системи",
        "ship_hull": "Очки корпусу",
        "ship_megadamage": "Мегашкода",
        "ship_fuel": "Паливо",
        "ship_crew": "Екіпаж",
        "ship_cryopods": "Кріокапсули",
        "ship_escape_pods": "Рятувальні капсули",
        "ship_hardpoints": "Точки монтажу",
        "ship_upgrade_slots": "Слоти модернізації",

        # ── Formatters — location ──────────────────
        "loc_in": "У",

        # ── Formatters — NPC ──────────────────────
        "npc_location": "Локація",
        "npc_stats": "Характеристики",
        "npc_wounds": "Поранення",
        "npc_hp_each": "ОЗ кожне",
        "npc_ap": "ЗБ",
        "npc_attacks": "Атаки",
        "npc_special": "Особливе",
    },

    "ru": {
        # ── Main menu ──────────────────────────────
        "main_menu_title": "🚀 <b>Mothership RPG — Справочник</b>",
        "main_menu_desc": (
            "Ваш настольный справочник. Правила, таблицы, снаряжение и НПС — "
            "из книг."
        ),
        "main_menu_select": "Выберите категорию:",

        # ── Language selection ─────────────────────
        "lang_title": "🌐 <b>Language / Мова / Язык</b>",
        "lang_select": "Выберите язык:",
        "lang_set_en": "✅ Язык установлен: English.",
        "lang_set_ua": "✅ Язык установлен: Українська.",
        "lang_set_ru": "✅ Язык установлен: Русский.",

        # ── Search ────────────────────────────────
        "search_btn": "🔍 Поиск",
        "search_usage": (
            "Использование: <code>/search &lt;термин&gt;</code>\n"
            "Пример: <code>/search wound</code>"
        ),
        "search_prompt_title": "🔍 <b>Поиск</b>",
        "search_prompt_body": (
            "Отправьте: <code>/search &lt;термин&gt;</code>\n\n"
            "Пример: <code>/search stress</code>"
        ),
        "search_no_results": (
            "🔍 Ничего не найдено по запросу <b>{query}</b>.\n\n"
            "Попробуйте более короткий термин или другое написание."
        ),
        "search_results_header": "🔍 <b>Результаты для \"{query}\"</b> ({total} найдено)",
        "search_more": "…ещё {n}",
        "search_section_rules": "Правила",
        "search_section_glossary": "Глоссарий",
        "search_section_equipment": "Снаряжение",
        "search_section_npcs": "НПС",
        "search_section_locations": "Локации",
        "search_section_tables": "Таблицы",

        # ── Nav buttons ────────────────────────────
        "btn_back": "← Назад",
        "btn_main_menu": "← Главное меню",
        "btn_prev": "◀ Пред.",
        "btn_next": "След. ▶",
        "btn_show_entries": "📋 Все записи",
        "btn_roll": "🎲 Бросить {dice}!",
        "btn_roll_again": "🎲 Бросить ещё раз ({dice})",
        "btn_page": "Страница {page} / {total}",

        # ── Glossary ───────────────────────────────
        "glossary_select": "Выберите термин:",

        # ── Error / status messages ────────────────
        "err_category": "Категория не найдена.",
        "err_rule": "Правило не найдено.",
        "err_term": "Термин не найден.",
        "err_item": "Предмет не найден.",
        "err_table": "Таблица не найдена.",
        "err_no_roll": "Запись для этого броска не найдена.",
        "err_no_entries": "Записи не найдены.",
        "err_entry": "Запись не найдена.",
        "err_class": "Класс не найден.",
        "err_skill": "Навык не найден.",
        "err_ship": "Корабль не найден.",
        "err_location": "Локация не найдена.",
        "err_npc": "НПС не найден.",
        "err_not_implemented": "Ещё не реализовано.",

        # ── Formatters — term ──────────────────────
        "also_known_as": "Также известен как: {aliases}",

        # ── Formatters — item ──────────────────────
        "item_cost": "Стоимость",
        "item_damage": "Урон",
        "item_range": "Дальность",
        "item_shots": "Патроны",
        "item_wound": "Ранение",
        "item_auto_attack": "⚡ <b>Авто-атака (AA)</b> — проверка боя не нужна",
        "item_special": "Особое",
        "item_ap": "ЗБ",
        "item_o2": "Кислород",
        "item_o2_none": "<b>Кислород:</b> Нет",
        "item_speed_penalty": "<b>Скорость:</b> Помеха [-] на проверки скорости",
        "item_damage_reduction": "Снижение урона",

        # ── Formatters — roll table ────────────────
        "table_dice": "Кубик",
        "table_usage": "Используйте кнопки ниже для броска или просмотра всех записей.",
        "table_entries_hint": "{n} записей — нажмите для просмотра.",
        "roll_result_label": "Бросок",

        # ── Formatters — class ─────────────────────
        "class_label": "Класс",
        "class_stat_bonuses": "Бонусы к характеристикам",
        "class_save_bonuses": "Бонусы к спасброскам",
        "class_max_wounds": "Макс. ранений",
        "class_health": "Здоровье",
        "class_special": "Особое",
        "class_trauma": "Реакция на травму",
        "class_preloaded_skills": "Начальные навыки",
        "class_starting_skills": "Начальные навыки",
        "class_bonus_skills": "Бонусные навыки",

        # ── Formatters — skill ─────────────────────
        "skill_trained": "Обученный (+10)",
        "skill_expert": "Опытный (+15)",
        "skill_master": "Мастер (+20)",
        "skill_prerequisite": "Предпосылка",

        # ── Formatters — ship ──────────────────────
        "ship_stats": "Характеристики",
        "ship_thrusters": "Двигатели",
        "ship_weapons": "Оружие",
        "ship_systems": "Системы",
        "ship_hull": "Очки корпуса",
        "ship_megadamage": "Мегаурон",
        "ship_fuel": "Топливо",
        "ship_crew": "Экипаж",
        "ship_cryopods": "Криокапсулы",
        "ship_escape_pods": "Спасательные капсулы",
        "ship_hardpoints": "Точки монтажа",
        "ship_upgrade_slots": "Слоты улучшений",

        # ── Formatters — location ──────────────────
        "loc_in": "В",

        # ── Formatters — NPC ──────────────────────
        "npc_location": "Локация",
        "npc_stats": "Характеристики",
        "npc_wounds": "Ранения",
        "npc_hp_each": "ОЗ каждое",
        "npc_ap": "ЗБ",
        "npc_attacks": "Атаки",
        "npc_special": "Особое",
    },
}


def t(lang: str, key: str, **kwargs) -> str:
    """Return translated string for key. Falls back to English if missing."""
    strings = _STRINGS.get(lang, _STRINGS[DEFAULT_LANG])
    text = strings.get(key) or _STRINGS[DEFAULT_LANG].get(key, key)
    if kwargs:
        text = text.format(**kwargs)
    return text
