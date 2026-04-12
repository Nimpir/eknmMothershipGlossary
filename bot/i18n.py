"""
i18n.py — UI strings and label_key translations for the Mothership bot.

Content translations live in content_i18n / page_i18n database rows.
This module handles static UI strings and the label_key → display name map.
"""

from typing import Any

DEFAULT_LANG = "en"
SUPPORTED_LANGS = ("en", "ru", "ua")

# ─────────────────────────────────────────────
# UI STRINGS
# ─────────────────────────────────────────────

_STRINGS: dict[str, dict[str, str]] = {
    "en": {
        # Main menu
        "main_menu_title":   "<b>Mothership RPG</b>",
        "main_menu_desc":    "Quick reference for the Mothership RPG.",
        "main_menu_select":  "Choose a section:",
        # Navigation
        "btn_back":          "◀ Back",
        "btn_home":          "🏠 Menu",
        "btn_roll":          "🎲 Roll",
        "btn_roll_all":      "🎲 Roll All",
        "btn_reroll_all":    "🔄 Roll Again",
        # Language
        "lang_title":        "<b>Language / Мова / Язык</b>",
        "lang_select":       "Choose your language:",
        "lang_set_en":       "Language set to English.",
        "lang_set_ru":       "Язык изменён на русский.",
        "lang_set_ua":       "Мову змінено на українську.",
        # Search
        "search_usage":      "Usage: /search &lt;query&gt;",
        "search_no_results": "No results for <b>{query}</b>.",
        "search_results":    "Results for <b>{query}</b>:",
        # Roll
        "dmg":               "DMG",
        "roll_result":       "🎲 <b>{notation}</b> → <code>{value}</code>",
        "roll_on":           "Rolled <b>{value}</b> on {name}:",
        "pick_on":           "Picked <b>{range}</b> on {name}:",
        "roll_result_entry": "<b>{result}</b>",
        # Errors
        "dice_table":        "Table:",
        "err_not_found":     "Not found.",
        "err_not_impl":      "Not implemented.",
    },
    "ru": {
        "main_menu_title":   "<b>Mothership RPG</b>",
        "main_menu_desc":    "Справочник по Mothership RPG.",
        "main_menu_select":  "Выберите раздел:",
        "btn_back":          "◀ Назад",
        "btn_home":          "🏠 Меню",
        "btn_roll":          "🎲 Бросить",
        "btn_roll_all":      "🎲 Бросить всё",
        "btn_reroll_all":    "🔄 Ещё раз",
        "lang_title":        "<b>Language / Мова / Язык</b>",
        "lang_select":       "Выберите язык:",
        "lang_set_en":       "Language set to English.",
        "lang_set_ru":       "Язык изменён на русский.",
        "lang_set_ua":       "Мову змінено на українську.",
        "search_usage":      "Использование: /search &lt;запрос&gt;",
        "search_no_results": "Ничего не найдено: <b>{query}</b>.",
        "search_results":    "Результаты для <b>{query}</b>:",
        "dmg":               "урон",
        "roll_result":       "🎲 <b>{notation}</b> → <code>{value}</code>",
        "roll_on":           "Выпало <b>{value}</b> на {name}:",
        "pick_on":           "Выбрано <b>{range}</b> на {name}:",
        "roll_result_entry": "<b>{result}</b>",
        "dice_table":        "Таблица:",
        "err_not_found":     "Не найдено.",
        "err_not_impl":      "Не реализовано.",
    },
    "ua": {
        "main_menu_title":   "<b>Mothership RPG</b>",
        "main_menu_desc":    "Довідник по Mothership RPG.",
        "main_menu_select":  "Оберіть розділ:",
        "btn_back":          "◀ Назад",
        "btn_home":          "🏠 Меню",
        "btn_roll":          "🎲 Кинути",
        "btn_roll_all":      "🎲 Кинути все",
        "btn_reroll_all":    "🔄 Ще раз",
        "lang_title":        "<b>Language / Мова / Язык</b>",
        "lang_select":       "Оберіть мову:",
        "lang_set_en":       "Language set to English.",
        "lang_set_ru":       "Язык изменён на русский.",
        "lang_set_ua":       "Мову змінено на українську.",
        "search_usage":      "Використання: /search &lt;запит&gt;",
        "search_no_results": "Нічого не знайдено: <b>{query}</b>.",
        "search_results":    "Результати для <b>{query}</b>:",
        "dmg":               "шкода",
        "roll_result":       "🎲 <b>{notation}</b> → <code>{value}</code>",
        "roll_on":           "Випало <b>{value}</b> на {name}:",
        "pick_on":           "Обрано <b>{range}</b> на {name}:",
        "roll_result_entry": "<b>{result}</b>",
        "dice_table":        "Таблиця:",
        "err_not_found":     "Не знайдено.",
        "err_not_impl":      "Не реалізовано.",
    },
}

# ─────────────────────────────────────────────
# LABEL KEYS
# label_key values come from subinfo_fixed and subinfo_text JSON fields.
# Translated at render time — not stored in the database.
# ─────────────────────────────────────────────

_LABEL_KEYS: dict[str, dict[str, str]] = {
    "en": {
        # Weapons
        "damage":       "Damage",
        "range":        "Range",
        "shots":        "Shots",
        "wound_type":   "Wound Type",
        "special":      "Special",
        # Armour
        "ap":           "Armour Points",
        "speed":        "Speed",
        "o2":           "O2 Supply",
        # Equipment
        "cost":         "Cost",
        "mass":         "Mass",
        # Cover
        "cover_insignificant": "Insignificant Cover",
        "cover_light":         "Light Cover",
        "cover_heavy":         "Heavy Cover",
        # Creatures
        "health":       "Health",
        "armor":        "Armour",
        "combat":       "Combat",
        "instinct":     "Instinct",
        "wounds":       "Wounds",
        "attacks":      "Attacks",
        # Ships
        "hull_points":  "Hull Points",
        "thrusters":    "Thrusters",
        "weapons":      "Weapons",
        "systems":      "Systems",
        "crew":         "Crew",
        "passengers":   "Passengers",
        "cargo":        "Cargo (tons)",
        "jump_range":   "Jump Range",
        # Skills / classes
        "bonus":        "Bonus",
        "tier":         "Tier",
        "saves":        "Saves",
        # Links
        "see_also":     "See Also",
        "related":      "Related",
    },
    "ru": {
        "damage":       "Урон",
        "range":        "Дальность",
        "shots":        "Выстрелы",
        "wound_type":   "Тип ранения",
        "special":      "Особое",
        "ap":           "Очки брони",
        "speed":        "Скорость",
        "o2":           "Запас О₂",
        "cost":         "Цена",
        "mass":         "Масса",
        "cover_insignificant": "Незначительное укрытие",
        "cover_light":         "Лёгкое укрытие",
        "cover_heavy":         "Тяжёлое укрытие",
        "health":       "Здоровье",
        "armor":        "Броня",
        "combat":       "Бой",
        "instinct":     "Инстинкт",
        "wounds":       "Ранения",
        "attacks":      "Атаки",
        "hull_points":  "Корпус",
        "thrusters":    "Двигатели",
        "weapons":      "Вооружение",
        "systems":      "Системы",
        "crew":         "Экипаж",
        "passengers":   "Пассажиры",
        "cargo":        "Груз (т.)",
        "jump_range":   "Дальность прыжка",
        "bonus":        "Бонус",
        "tier":         "Уровень",
        "saves":        "Спасброски",
        "see_also":     "См. также",
        "related":      "Связано",
    },
    "ua": {
        "damage":       "Шкода",
        "range":        "Дальність",
        "shots":        "Постріли",
        "wound_type":   "Тип поранення",
        "special":      "Особливе",
        "ap":           "Очки броні",
        "speed":        "Швидкість",
        "o2":           "Запас О₂",
        "cost":         "Ціна",
        "mass":         "Маса",
        "cover_insignificant": "Незначне укриття",
        "cover_light":         "Легке укриття",
        "cover_heavy":         "Важке укриття",
        "health":       "Здоров'я",
        "armor":        "Броня",
        "combat":       "Бій",
        "instinct":     "Інстинкт",
        "wounds":       "Поранення",
        "attacks":      "Атаки",
        "hull_points":  "Корпус",
        "thrusters":    "Двигуни",
        "weapons":      "Озброєння",
        "systems":      "Системи",
        "crew":         "Екіпаж",
        "passengers":   "Пасажири",
        "cargo":        "Вантаж (т.)",
        "jump_range":   "Дальність стрибка",
        "bonus":        "Бонус",
        "tier":         "Рівень",
        "saves":        "Рятівні кидки",
        "see_also":     "Дивись також",
        "related":      "Пов'язано",
    },
}


# ─────────────────────────────────────────────
# VALUE MAPS
# Translate subinfo_fixed values that are game terms (range bands, wound types).
# Keyed by label_key so only relevant fields are translated.
# ─────────────────────────────────────────────

_VALUE_MAPS: dict[str, dict[str, dict[str, str]]] = {
    "cost": {
        "en": {"Free": "Free"},
        "ru": {"Free": "Бесплатно"},
        "ua": {"Free": "Безкоштовно"},
    },
    "damage": {
        "en": {"Str/10 DMG": "Str/10 DMG", "—": "—"},
        "ru": {"Str/10 DMG": "Сил/10 урона", "—": "—"},
        "ua": {"Str/10 DMG": "Сил/10 шкоди", "—": "—"},
    },
    "range": {
        "en": {
            "Adjacent": "Adjacent", "Close": "Close",
            "Long": "Long",         "Extreme": "Extreme",
        },
        "ru": {
            "Adjacent": "Рядом",    "Close": "Близко",
            "Long": "Далеко",       "Extreme": "Экстрем",
        },
        "ua": {
            "Adjacent": "Поруч",    "Close": "Близько",
            "Long": "Далеко",       "Extreme": "Екстрем",
        },
    },
    "speed": {
        "en": {"Normal": "Normal", "[-]": "[-]"},
        "ru": {"Normal": "Нормальная", "[-]": "[-]"},
        "ua": {"Normal": "Нормальна", "[-]": "[-]"},
    },
    "o2": {
        "en": {"—": "—", "12 hrs": "12 hrs", "1 hr": "1 hr"},
        "ru": {"—": "—", "12 hrs": "12 часов", "1 hr": "1 час"},
        "ua": {"—": "—", "12 hrs": "12 годин", "1 hr": "1 година"},
    },
    "damage_condition": {
        "en": {"when removed": "when removed"},
        "ru": {"when removed": "при извлечении"},
        "ua": {"when removed": "при видаленні"},
    },
    "wound_type": {
        "en": {
            "Blunt Force":              "Blunt Force",
            "Blunt Force [+]":          "Blunt Force [+]",
            "Bleeding":                 "Bleeding",
            "Bleeding [+]":             "Bleeding [+]",
            "Gunshot":                  "Gunshot",
            "Gunshot [+]":              "Gunshot [+]",
            "Fire/Explosives":          "Fire/Explosives",
            "Fire/Explosives [+]":      "Fire/Explosives [+]",
            "Fire/Explosives [-]":      "Fire/Explosives [-]",
            "Fire & Explosives":        "Fire & Explosives",
            "Gore [+]":                 "Gore [+]",
            "Gore & Massive":           "Gore & Massive",
            "Bleeding [+] or Gore [+]": "Bleeding [+] or Gore [+]",
            "Bleeding + Gore":          "Bleeding + Gore",
        },
        "ru": {
            "Blunt Force":              "Тупой удар",
            "Blunt Force [+]":          "Тупой удар [+]",
            "Bleeding":                 "Кровотечение",
            "Bleeding [+]":             "Кровотечение [+]",
            "Gunshot":                  "Огнестрел",
            "Gunshot [+]":              "Огнестрел [+]",
            "Fire/Explosives":          "Огонь/Взрыв",
            "Fire/Explosives [+]":      "Огонь/Взрыв [+]",
            "Fire/Explosives [-]":      "Огонь/Взрыв [-]",
            "Fire & Explosives":        "Огонь и Взрывы",
            "Gore [+]":                 "Расчленение [+]",
            "Gore & Massive":           "Расчленение",
            "Bleeding [+] or Gore [+]": "Кровотечение [+] или Расчленение [+]",
            "Bleeding + Gore":          "Кровотечение + Расчленение",
        },
        "ua": {
            "Blunt Force":              "Тупий удар",
            "Blunt Force [+]":          "Тупий удар [+]",
            "Bleeding":                 "Кровотеча",
            "Bleeding [+]":             "Кровотеча [+]",
            "Gunshot":                  "Вогнепальне",
            "Gunshot [+]":              "Вогнепальне [+]",
            "Fire/Explosives":          "Вогонь/Вибух",
            "Fire/Explosives [+]":      "Вогонь/Вибух [+]",
            "Fire/Explosives [-]":      "Вогонь/Вибух [-]",
            "Fire & Explosives":        "Вогонь та Вибухи",
            "Gore [+]":                 "Масивний урон [+]",
            "Gore & Massive":           "Масивний урон",
            "Bleeding [+] or Gore [+]": "Кровотеча [+] або Масивний урон [+]",
            "Bleeding + Gore":          "Кровотеча + Масивний урон",
        },
    },
}


def value_t(lang: str, label_key: str, value: str) -> str:
    """Translate a subinfo_fixed value if a map exists for its label_key. Falls back to the raw value."""
    return _VALUE_MAPS.get(label_key, {}).get(lang, {}).get(value, value)


def t(lang: str, key: str, **kwargs: Any) -> str:
    """Return the UI string for key in lang, formatted with kwargs. Falls back to 'en'."""
    lang_strings = _STRINGS.get(lang, _STRINGS[DEFAULT_LANG])
    template = lang_strings.get(key) or _STRINGS[DEFAULT_LANG].get(key, f"[{key}]")
    return template.format(**kwargs) if kwargs else template


def label(lang: str, key: str) -> str:
    """Return the display name for a label_key. Falls back to the key itself."""
    lang_labels = _LABEL_KEYS.get(lang, _LABEL_KEYS[DEFAULT_LANG])
    return lang_labels.get(key) or _LABEL_KEYS[DEFAULT_LANG].get(key, key)
