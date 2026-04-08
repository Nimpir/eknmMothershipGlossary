"""
formatters.py — Message text formatters for every content type.
All output uses HTML parse mode (simpler escaping for arbitrary text).
"""

import json

from .i18n import t


def _src(book_code: str | None, page: int | None) -> str:
    if book_code and page:
        return f"\n<i>[{book_code} p.{page}]</i>"
    if book_code:
        return f"\n<i>[{book_code}]</i>"
    return ""


def _stat(label: str, value) -> str:
    if value is None:
        return ""
    return f"<b>{label}:</b> {value}\n"


# ─────────────────────────────────────────────
# CATEGORY
# ─────────────────────────────────────────────

def category_header(cat: dict, breadcrumb: list[dict]) -> str:
    path = " › ".join(c["name"] for c in breadcrumb)
    icon = f"{cat['icon']} " if cat.get("icon") else ""
    return f"<b>{icon}{cat['name']}</b>\n<i>{path}</i>"


# ─────────────────────────────────────────────
# RULE
# ─────────────────────────────────────────────

def format_rule(rule: dict, lang: str = "en") -> str:
    src = _src(rule.get("book_code"), rule.get("page_number"))
    body = _md_to_html(rule["body"])
    return f"<b>{rule['title']}</b>{src}\n\n{body}"


# ─────────────────────────────────────────────
# TERM
# ─────────────────────────────────────────────

def format_term(term: dict, lang: str = "en") -> str:
    src = _src(term.get("book_code"), term.get("page_number"))
    aliases = ""
    if term.get("aliases"):
        try:
            alias_list = json.loads(term["aliases"])
            if alias_list:
                aliases = f"\n<i>{t(lang, 'also_known_as', aliases=', '.join(alias_list))}</i>"
        except (json.JSONDecodeError, TypeError):
            pass
    body = _md_to_html(term["body"])
    return f"📖 <b>{term['name']}</b>{src}{aliases}\n\n{body}"


# ─────────────────────────────────────────────
# ITEM (EQUIPMENT)
# ─────────────────────────────────────────────

def format_item(item: dict, lang: str = "en") -> str:
    src = _src(item.get("book_code"), item.get("page_number"))
    lines = [f"<b>{item['name']}</b>  <i>[{item['item_type'].upper()}]</i>{src}\n"]

    if item.get("cost_display"):
        lines.append(f"<b>{t(lang, 'item_cost')}:</b> {item['cost_display']}")

    if item["item_type"] == "weapon":
        dmg = item.get("damage_dice", "—")
        if item.get("damage_modifier"):
            dmg += item["damage_modifier"]
        lines.append(f"<b>{t(lang, 'item_damage')}:</b> {dmg}")
        if item.get("range_band"):
            lines.append(f"<b>{t(lang, 'item_range')}:</b> {item['range_band']}")
        if item.get("shots"):
            lines.append(f"<b>{t(lang, 'item_shots')}:</b> {item['shots']}")
        wound = item.get("wound_type", "—")
        if item.get("wound_modifier"):
            wound += f" {item['wound_modifier']}"
        lines.append(f"<b>{t(lang, 'item_wound')}:</b> {wound}")
        if item.get("is_auto_attack"):
            lines.append(t(lang, "item_auto_attack"))
        if item.get("special_rules"):
            lines.append(f"<b>{t(lang, 'item_special')}:</b> {item['special_rules']}")

    elif item["item_type"] == "armor":
        lines.append(f"<b>{t(lang, 'item_ap')}:</b> {item.get('armor_points', '—')}")
        if item.get("o2_hours"):
            lines.append(f"<b>{t(lang, 'item_o2')}:</b> {item['o2_hours']} hours")
        else:
            lines.append(t(lang, "item_o2_none"))
        if item.get("speed_penalty"):
            lines.append(t(lang, "item_speed_penalty"))
        if item.get("damage_reduction", 0) > 0:
            lines.append(f"<b>{t(lang, 'item_damage_reduction')}:</b> {item['damage_reduction']}")
        if item.get("special_rules"):
            lines.append(f"<b>{t(lang, 'item_special')}:</b> {item['special_rules']}")

    elif item["item_type"] in ("gear", "trinket"):
        if item.get("description"):
            lines.append(f"\n{item['description']}")
        if item.get("special_rules"):
            lines.append(f"<b>{t(lang, 'item_special')}:</b> {item['special_rules']}")

    if item.get("description") and item["item_type"] == "weapon":
        lines.append(f"\n<i>{item['description']}</i>")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# ROLL TABLE
# ─────────────────────────────────────────────

def format_roll_table(table: dict, lang: str = "en") -> str:
    src = _src(table.get("book_code"), table.get("page_number"))
    desc = f"\n\n{table['description']}" if table.get("description") else ""
    return (
        f"🎲 <b>{table['name']}</b>{src}{desc}\n\n"
        f"<b>{t(lang, 'table_dice')}:</b> {table['dice_notation'].upper()}\n\n"
        f"{t(lang, 'table_usage')}"
    )


def format_roll_table_header(table: dict, total_entries: int, lang: str = "en") -> str:
    """Compact header shown above the selectable entries list."""
    src = _src(table.get("book_code"), table.get("page_number"))
    return (
        f"🎲 <b>{table['name']}</b> ({table['dice_notation'].upper()}){src}\n\n"
        f"<i>{t(lang, 'table_entries_hint', n=total_entries)}</i>"
    )


def format_roll_result(table: dict, entry: dict, roll_value: int, lang: str = "en") -> str:
    src = _src(table.get("book_code"), table.get("page_number"))
    label = entry.get("label") or str(roll_value)
    result = entry["result_text"]

    extra = ""
    if entry.get("extra_data"):
        try:
            data = json.loads(entry["extra_data"])
            extra_lines = [f"<b>{k.replace('_', ' ').title()}:</b> {v}" for k, v in data.items()]
            extra = "\n" + "\n".join(extra_lines)
        except (json.JSONDecodeError, TypeError):
            pass

    return (
        f"🎲 <b>{table['name']}</b>{src}\n"
        f"<b>{t(lang, 'roll_result_label')}:</b> {roll_value} → <code>{label}</code>\n\n"
        f"{result}{extra}"
    )


def format_entries_list(table: dict, entries: list[dict], lang: str = "en") -> str:
    src = _src(table.get("book_code"), table.get("page_number"))
    lines = [f"🎲 <b>{table['name']}</b> ({table['dice_notation'].upper()}){src}\n"]

    for e in entries:
        label = e.get("label") or f"{e['roll_min']}"
        lines.append(f"<b>{label}</b> — {e['result_text']}")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# CLASS
# ─────────────────────────────────────────────

def format_class(cls: dict, lang: str = "en") -> str:
    lines = [f"<b>{cls['name']}</b>  <i>[{t(lang, 'class_label')}]</i>"]
    if cls.get("description"):
        lines.append(f"\n{cls['description']}\n")

    try:
        stat_b = json.loads(cls["stat_bonuses"])
        sb_str = ", ".join(f"{k} {'+' if v >= 0 else ''}{v}" for k, v in stat_b.items())
        lines.append(f"<b>{t(lang, 'class_stat_bonuses')}:</b> {sb_str}")
    except (json.JSONDecodeError, TypeError):
        pass

    try:
        save_b = json.loads(cls["save_bonuses"])
        sv_str = ", ".join(f"{k} {'+' if v >= 0 else ''}{v}" for k, v in save_b.items())
        lines.append(f"<b>{t(lang, 'class_save_bonuses')}:</b> {sv_str}")
    except (json.JSONDecodeError, TypeError):
        pass

    if cls.get("max_wounds_bonus", 0) > 0:
        lines.append(f"<b>{t(lang, 'class_max_wounds')}:</b> +{cls['max_wounds_bonus']} (total {2 + cls['max_wounds_bonus']})")
    lines.append(f"<b>{t(lang, 'class_health')}:</b> {cls.get('health_dice', '1d10+10')}")
    if cls.get("special_abilities"):
        lines.append(f"<b>{t(lang, 'class_special')}:</b> {cls['special_abilities']}")
    if cls.get("trauma_response"):
        lines.append(f"<b>{t(lang, 'class_trauma')}:</b> {cls['trauma_response']}")

    try:
        sk = json.loads(cls["starting_skills"])
        preloaded = sk.get("preloaded")
        bonus = sk.get("bonus")
        if isinstance(preloaded, list):
            lines.append(f"<b>{t(lang, 'class_preloaded_skills')}:</b> {', '.join(preloaded)}")
        elif preloaded:
            lines.append(f"<b>{t(lang, 'class_starting_skills')}:</b> {preloaded}")
        if bonus:
            lines.append(f"<b>{t(lang, 'class_bonus_skills')}:</b> {bonus}")
    except (json.JSONDecodeError, TypeError):
        pass

    return "\n".join(lines)


# ─────────────────────────────────────────────
# SKILL
# ─────────────────────────────────────────────

def format_skill(skill: dict, lang: str = "en") -> str:
    tier_map = {
        "trained": t(lang, "skill_trained"),
        "expert":  t(lang, "skill_expert"),
        "master":  t(lang, "skill_master"),
    }
    tier_label = tier_map.get(skill["tier"], skill["tier"])
    lines = [f"<b>{skill['name']}</b>  <i>[{tier_label}]</i>"]
    prereqs = skill.get("prerequisite_names") or []
    if prereqs:
        lines.append(f"<b>{t(lang, 'skill_prerequisite')}:</b> {' or '.join(prereqs)}")
    if skill.get("description"):
        lines.append(f"\n{skill['description']}")
    return "\n".join(lines)


# ─────────────────────────────────────────────
# SHIP
# ─────────────────────────────────────────────

def format_ship(ship: dict, lang: str = "en") -> str:
    src = _src(ship.get("book_code"), ship.get("page_number"))
    cls = f"Class-{ship['class']}" if ship.get("class") else ""
    type_str = ship.get("ship_type", "")
    header = " | ".join(filter(None, [cls, type_str, ship.get("manufacturer")]))

    lines = [f"<b>{ship['name']}</b>{src}"]
    if header:
        lines.append(f"<i>{header}</i>\n")

    stats = [
        (t(lang, "ship_thrusters"), ship.get("thrusters_stat")),
        (t(lang, "ship_weapons"),   ship.get("weapons_stat")),
        (t(lang, "ship_systems"),   ship.get("systems_stat")),
    ]
    stat_parts = [f"{k}: {v}" for k, v in stats if v is not None]
    if stat_parts:
        lines.append(f"<b>{t(lang, 'ship_stats')}:</b> {' | '.join(stat_parts)}")

    if ship.get("hull_points"):
        lines.append(f"<b>{t(lang, 'ship_hull')}:</b> {ship['hull_points']}")
    if ship.get("megadamage_dice"):
        lines.append(f"<b>{t(lang, 'ship_megadamage')}:</b> {ship['megadamage_dice']}")
    if ship.get("fuel_capacity"):
        lines.append(f"<b>{t(lang, 'ship_fuel')}:</b> {ship['fuel_capacity']}")
    if ship.get("crew_capacity"):
        lines.append(f"<b>{t(lang, 'ship_crew')}:</b> {ship['crew_capacity']}")
    if ship.get("cryopod_count"):
        lines.append(f"<b>{t(lang, 'ship_cryopods')}:</b> {ship['cryopod_count']}")
    if ship.get("escape_pod_count"):
        lines.append(f"<b>{t(lang, 'ship_escape_pods')}:</b> {ship['escape_pod_count']}")
    if ship.get("hardpoints") is not None:
        lines.append(f"<b>{t(lang, 'ship_hardpoints')}:</b> {ship['hardpoints']}")
    if ship.get("upgrade_slots") is not None:
        lines.append(f"<b>{t(lang, 'ship_upgrade_slots')}:</b> {ship['upgrade_slots']}")
    if ship.get("description"):
        lines.append(f"\n<i>{ship['description']}</i>")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# LOCATION
# ─────────────────────────────────────────────

def format_location(loc: dict, lang: str = "en") -> str:
    src = _src(loc.get("book_code"), loc.get("page_number"))
    type_str = f" <i>[{loc['location_type']}]</i>" if loc.get("location_type") else ""
    parent_str = f"\n<i>{t(lang, 'loc_in')}: {loc['parent_name']}</i>" if loc.get("parent_name") else ""
    desc = f"\n\n{loc['description']}" if loc.get("description") else ""
    return f"📍 <b>{loc['name']}</b>{type_str}{src}{parent_str}{desc}"


# ─────────────────────────────────────────────
# NPC
# ─────────────────────────────────────────────

def format_npc(npc: dict, lang: str = "en") -> str:
    src = _src(npc.get("book_code"), npc.get("page_number"))
    role = f" <i>[{npc['role']}]</i>" if npc.get("role") else ""
    loc = f"\n<i>{t(lang, 'npc_location')}: {npc['location_name']}</i>" if npc.get("location_name") else ""

    lines = [f"<b>{npc['name']}</b>{role}{src}{loc}"]
    if npc.get("description"):
        lines.append(f"\n{npc['description']}\n")

    has_stats = any(npc.get(k) for k in ("combat_stat", "speed_stat", "instinct_stat"))
    if has_stats:
        stats = []
        if npc.get("combat_stat"):
            stats.append(f"Combat {npc['combat_stat']}")
        if npc.get("speed_stat"):
            stats.append(f"Speed {npc['speed_stat']}")
        if npc.get("instinct_stat"):
            stats.append(f"Instinct {npc['instinct_stat']}")
        lines.append(f"<b>{t(lang, 'npc_stats')}:</b> {' | '.join(stats)}")

    if npc.get("wounds") is not None and npc.get("health") is not None:
        lines.append(f"<b>{t(lang, 'npc_wounds')}:</b> {npc['wounds']} ({npc['health']} {t(lang, 'npc_hp_each')})")
    if npc.get("armor_points") is not None:
        lines.append(f"<b>{t(lang, 'npc_ap')}:</b> {npc['armor_points']}")

    if npc.get("attacks"):
        try:
            attacks = json.loads(npc["attacks"])
            atk_lines = []
            for a in attacks:
                atk = f"• {a['name']}: {a.get('damage', '—')} ({a.get('wound_type', '—')})"
                if a.get("special"):
                    atk += f" — {a['special']}"
                atk_lines.append(atk)
            lines.append(f"<b>{t(lang, 'npc_attacks')}:</b>\n" + "\n".join(atk_lines))
        except (json.JSONDecodeError, TypeError, KeyError):
            pass

    if npc.get("special_rules"):
        lines.append(f"<b>{t(lang, 'npc_special')}:</b> {npc['special_rules']}")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# SEARCH
# ─────────────────────────────────────────────

def format_search_results(query: str, results: dict, lang: str = "en") -> str:
    section_keys = {
        "Rules":       "search_section_rules",
        "Glossary":    "search_section_glossary",
        "Equipment":   "search_section_equipment",
        "NPCs":        "search_section_npcs",
        "Locations":   "search_section_locations",
        "Roll Tables": "search_section_tables",
    }
    if not results:
        return t(lang, "search_no_results", query=query)
    total = sum(len(v) for v in results.values())
    lines = [t(lang, "search_results_header", query=query, total=total) + "\n"]
    for section, items in results.items():
        section_label = t(lang, section_keys.get(section, "search_section_rules"))
        lines.append(f"<b>{section_label}:</b>")
        for item in items[:5]:
            lines.append(f"  • {item['title']}")
        if len(items) > 5:
            lines.append(f"  <i>{t(lang, 'search_more', n=len(items) - 5)}</i>")
    return "\n".join(lines)


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def _md_to_html(text: str) -> str:
    """Escape HTML special chars then convert *bold* markers to <b> tags."""
    import re
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r'\*([^*]+)\*', r'<b>\1</b>', text)
