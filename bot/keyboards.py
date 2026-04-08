"""
keyboards.py — All inline keyboard builders for the Mothership bot.
Callback data format: "type:id"  e.g. "cat:5", "rule:12", "term:3"
Back navigation is handled by the nav stack — all back buttons use "back".
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Maximum items before pagination (Telegram message limit ~4096 chars)
PAGE_SIZE = 15
# Entries per page in roll table entry lists
ENTRIES_PAGE_SIZE = 10
# Max chars of result_text shown in an entry button
ENTRY_LABEL_MAX = 45


def _btn(label: str, data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(label, callback_data=data)


def _back() -> list[InlineKeyboardButton]:
    return [_btn("← Back", "back")]


def main_menu(categories: list[dict]) -> InlineKeyboardMarkup:
    rows = []
    for cat in categories:
        icon = f"{cat['icon']} " if cat.get("icon") else ""
        rows.append([_btn(f"{icon}{cat['name']}", f"cat:{cat['id']}")])
    rows.append([_btn("🔍 Search", "search")])
    return InlineKeyboardMarkup(rows)


def category_menu(
    category: dict,
    subcategories: list[dict],
    rules: list[dict],
    tables: list[dict],
    items: list[dict] | None = None,
    npcs: list[dict] | None = None,
    locations: list[dict] | None = None,
    classes: list[dict] | None = None,
    ships: list[dict] | None = None,
    skills: list[dict] | None = None,
    page: int = 0,
) -> InlineKeyboardMarkup:
    rows = []

    for sub in subcategories:
        icon = f"{sub['icon']} " if sub.get("icon") else "  "
        rows.append([_btn(f"{icon}{sub['name']}", f"cat:{sub['id']}")])

    content: list[tuple[str, str, str]] = []

    for r in rules:
        content.append((f"📄 {r['title']}", "rule", str(r["id"])))
    for t in tables:
        content.append((f"🎲 {t['name']}", "table", str(t["id"])))
    if items:
        for i in items:
            content.append((f"⚙️ {i['name']}", "item", str(i["id"])))
    if npcs:
        for n in npcs:
            content.append((f"👤 {n['name']}", "npc", str(n["id"])))
    if locations:
        for l in locations:
            content.append((f"📍 {l['name']}", "loc", str(l["id"])))
    if classes:
        for c in classes:
            content.append((f"🪖 {c['name']}", "cls", str(c["id"])))
    if ships:
        for s in ships:
            content.append((f"🚀 {s['name']}", "ship", str(s["id"])))
    if skills:
        for sk in skills:
            content.append((f"🔧 {sk['name']} ({sk['tier'][0].upper()}+{sk['bonus']})", "skill", str(sk["id"])))

    total = len(content)
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_items = content[start:end]

    for label, cb_type, id_str in page_items:
        rows.append([_btn(label, f"{cb_type}:{id_str}")])

    nav = []
    if page > 0:
        nav.append(_btn("◀ Prev", f"cat:{category['id']}:page:{page - 1}"))
    if end < total:
        nav.append(_btn("Next ▶", f"cat:{category['id']}:page:{page + 1}"))
    if nav:
        rows.append(nav)

    rows.append(_back())
    return InlineKeyboardMarkup(rows)


def term_buttons(terms: list[dict]) -> InlineKeyboardMarkup:
    """Term quick-access buttons shown below content entries."""
    rows = [[_btn(f"📖 {t['name']}", f"term:{t['id']}")] for t in terms]
    rows.append(_back())
    return InlineKeyboardMarkup(rows)


def back_only() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([_back()])


def term_with_tables(tables: list[dict]) -> InlineKeyboardMarkup:
    """Term detail keyboard — optional roll table shortcuts + back."""
    rows = [[_btn(f"🎲 {t['name']} ({t['dice_notation'].upper()})", f"table:{t['id']}")] for t in tables]
    rows.append(_back())
    return InlineKeyboardMarkup(rows)


def roll_table_keyboard(table: dict) -> InlineKeyboardMarkup:
    rows = [
        [_btn(f"🎲 Roll on {table['dice_notation'].upper()}!", f"roll:{table['id']}")],
        [_btn("📋 Show All Entries", f"entries:{table['id']}")],
        _back(),
    ]
    return InlineKeyboardMarkup(rows)


def roll_result_keyboard(
    table: dict,
    entry: dict,
    linked_term: dict | None,
    items: list[dict] | None = None,
) -> InlineKeyboardMarkup:
    rows = [
        [_btn(f"🎲 Roll Again ({table['dice_notation'].upper()})", f"roll:{table['id']}")],
    ]
    if items:
        icon_map = {"weapon": "🔫", "armor": "🛡️", "gear": "⚙️", "trinket": "✨"}
        for item in items:
            icon = icon_map.get(item["item_type"], "⚙️")
            rows.append([_btn(f"{icon} {item['name']}", f"item:{item['id']}")])
    if linked_term:
        rows.append([_btn(f"📖 {linked_term['name']}", f"term:{linked_term['id']}")])
    rows.append(_back())
    return InlineKeyboardMarkup(rows)


def glossary_keyboard(terms: list[dict], page: int = 0) -> InlineKeyboardMarkup:
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_terms = terms[start:end]

    rows = [[_btn(f"📖 {t['name']}", f"term:{t['id']}")] for t in page_terms]

    nav = []
    if page > 0:
        nav.append(_btn("◀ Prev", f"glossary:page:{page - 1}"))
    if end < len(terms):
        nav.append(_btn("Next ▶", f"glossary:page:{page + 1}"))
    if nav:
        rows.append(nav)

    rows.append(_back())
    return InlineKeyboardMarkup(rows)


def npc_with_terms(npc: dict, terms: list[dict]) -> InlineKeyboardMarkup:
    rows = [[_btn(f"📖 {t['name']}", f"term:{t['id']}")] for t in terms]
    rows.append(_back())
    return InlineKeyboardMarkup(rows)


def search_results(results: dict[str, list[dict]]) -> InlineKeyboardMarkup:
    rows = []
    type_map = {
        "Rules": "rule",
        "Glossary": "term",
        "Equipment": "item",
        "NPCs": "npc",
        "Locations": "loc",
        "Roll Tables": "table",
    }
    for section, items in results.items():
        cb_type = type_map.get(section, "rule")
        for item in items[:5]:
            rows.append([_btn(f"[{section}] {item['title']}", f"{cb_type}:{item['id']}")])
    rows.append([_btn("← Main Menu", "menu")])
    return InlineKeyboardMarkup(rows)


def entries_list(table: dict, entries: list[dict], page: int = 0) -> InlineKeyboardMarkup:
    """Selectable entry list with pagination, roll button, and back."""
    start = page * ENTRIES_PAGE_SIZE
    end = start + ENTRIES_PAGE_SIZE
    page_entries = entries[start:end]

    rows = []
    for e in page_entries:
        if e["roll_min"] == e["roll_max"]:
            range_str = str(e["roll_min"])
        else:
            range_str = f"{e['roll_min']}–{e['roll_max']}"
        desc = e.get("result_text", "") or ""
        if len(desc) > ENTRY_LABEL_MAX:
            desc = desc[:ENTRY_LABEL_MAX].rstrip() + "…"
        btn_label = f"{range_str} — {desc}" if desc else range_str
        rows.append([_btn(btn_label, f"entry:{table['id']}:{e['id']}")])

    nav = []
    if page > 0:
        nav.append(_btn("◀ Prev", f"entries:{table['id']}:page:{page - 1}"))
    if end < len(entries):
        nav.append(_btn("Next ▶", f"entries:{table['id']}:page:{page + 1}"))
    if nav:
        rows.append(nav)

    total_pages = (len(entries) + ENTRIES_PAGE_SIZE - 1) // ENTRIES_PAGE_SIZE
    if total_pages > 1:
        rows.append([_btn(f"Page {page + 1} / {total_pages}", "noop")])

    rows.append([_btn(f"🎲 Roll ({table['dice_notation'].upper()})", f"roll:{table['id']}")])
    rows.append(_back())
    return InlineKeyboardMarkup(rows)
