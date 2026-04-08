"""
keyboards.py — All inline keyboard builders for the Mothership bot.
Callback data format: "type:id"  e.g. "cat:5", "rule:12", "term:3"
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Maximum buttons per row for content lists
COLS = 1
# Maximum items before pagination (Telegram message limit ~4096 chars)
PAGE_SIZE = 15


def _btn(label: str, data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(label, callback_data=data)


def _back_btn(cat_id: int | None) -> InlineKeyboardButton:
    if cat_id is not None:
        return _btn("← Back", f"cat:{cat_id}")
    return _btn("← Main Menu", "menu")


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

    # Sub-categories first
    for sub in subcategories:
        icon = f"{sub['icon']} " if sub.get("icon") else "  "
        rows.append([_btn(f"{icon}{sub['name']}", f"cat:{sub['id']}")])

    # Collect all content items
    content: list[tuple[str, str, str]] = []  # (label, cb_type, id_str)

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

    # Paginate
    total = len(content)
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    page_items = content[start:end]

    for label, cb_type, id_str in page_items:
        rows.append([_btn(label, f"{cb_type}:{id_str}")])

    # Pagination controls
    nav = []
    if page > 0:
        nav.append(_btn("◀ Prev", f"cat:{category['id']}:page:{page - 1}"))
    if end < total:
        nav.append(_btn("Next ▶", f"cat:{category['id']}:page:{page + 1}"))
    if nav:
        rows.append(nav)

    # Back button
    if category.get("parent_id"):
        rows.append([_back_btn(category["parent_id"])])
    else:
        rows.append([_btn("← Main Menu", "menu")])

    return InlineKeyboardMarkup(rows)


def term_buttons(terms: list[dict], back_data: str) -> InlineKeyboardMarkup:
    """Inline term quick-access buttons shown below content entries."""
    rows = []
    for t in terms:
        rows.append([_btn(f"📖 {t['name']}", f"term:{t['id']}")])
    rows.append([_btn("← Back", back_data)])
    return InlineKeyboardMarkup(rows)


def back_only(back_data: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[_btn("← Back", back_data)]])


def roll_table_keyboard(table: dict, back_cat_id: int | None) -> InlineKeyboardMarkup:
    rows = [
        [_btn(f"🎲 Roll on {table['dice_notation'].upper()}!", f"roll:{table['id']}")],
        [_btn("📋 Show All Entries", f"entries:{table['id']}")],
    ]
    if back_cat_id:
        rows.append([_back_btn(back_cat_id)])
    else:
        rows.append([_btn("← Main Menu", "menu")])
    return InlineKeyboardMarkup(rows)


def roll_result_keyboard(table: dict, entry: dict, linked_term: dict | None) -> InlineKeyboardMarkup:
    rows = [
        [_btn(f"🎲 Roll Again ({table['dice_notation'].upper()})", f"roll:{table['id']}")],
    ]
    if linked_term:
        rows.append([_btn(f"📖 {linked_term['name']}", f"term:{linked_term['id']}")])
    rows.append([_btn("← Back to Table", f"table:{table['id']}")])
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

    rows.append([_btn("← Main Menu", "menu")])
    return InlineKeyboardMarkup(rows)


def npc_with_terms(npc: dict, terms: list[dict], back_data: str) -> InlineKeyboardMarkup:
    rows = []
    for t in terms:
        rows.append([_btn(f"📖 {t['name']}", f"term:{t['id']}")])
    rows.append([_btn("← Back", back_data)])
    return InlineKeyboardMarkup(rows)


def search_results(results: dict[str, list[dict]]) -> InlineKeyboardMarkup:
    """Keyboard for search results."""
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
        for item in items[:5]:  # cap at 5 per section to avoid huge keyboards
            rows.append([_btn(f"[{section}] {item['title']}", f"{cb_type}:{item['id']}")])
    rows.append([_btn("← Main Menu", "menu")])
    return InlineKeyboardMarkup(rows)


def entries_list(table: dict, entries: list[dict]) -> InlineKeyboardMarkup:
    """Show all entries of a table with a roll button and back."""
    rows = [
        [_btn(f"🎲 Roll ({table['dice_notation'].upper()})", f"roll:{table['id']}")],
        [_btn("← Back to Table", f"table:{table['id']}")],
    ]
    return InlineKeyboardMarkup(rows)
