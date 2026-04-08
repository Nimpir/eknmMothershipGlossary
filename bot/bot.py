"""
bot.py — Mothership RPG Telegram Bot
Entry point. Registers all handlers and starts polling.

Usage:
    python -m bot.bot
    (from C:/Git/mothership, with .env containing BOT_TOKEN)
"""

import logging
import os
import random
import re

from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from . import db, formatters as fmt, keyboards as kb
from .logging_setup import setup_logging

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

_GLOSSARY_CAT_ID = 21

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

async def _edit(update: Update, text: str, keyboard, parse_mode=ParseMode.HTML) -> None:
    """Edit the current message in-place."""
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=keyboard,
        parse_mode=parse_mode,
    )


async def _reply(update: Update, text: str, keyboard, parse_mode=ParseMode.HTML) -> None:
    """Send a new message (used for /commands)."""
    await update.message.reply_text(
        text=text,
        reply_markup=keyboard,
        parse_mode=parse_mode,
    )


def _roll_dice(notation: str) -> int:
    """Parse dice notation like d10, d100, 2d10 and return a random result."""
    notation = notation.lower().strip()
    m = re.match(r"^(\d*)d(\d+)$", notation)
    if not m:
        return 1
    count = int(m.group(1)) if m.group(1) else 1
    sides = int(m.group(2))
    return sum(random.randint(1, sides) for _ in range(count))


# ─────────────────────────────────────────────
# MENU DISPLAY
# ─────────────────────────────────────────────

async def _show_main_menu(update: Update, edit: bool = False) -> None:
    cats = db.get_top_level_categories()
    text = (
        "🚀 <b>Mothership RPG Reference</b>\n\n"
        "Your table-side handbook. Browse rules, roll tables, look up gear "
        "and NPCs — all from the source books.\n\n"
        "Select a category:"
    )
    keyboard = kb.main_menu(cats)
    if edit:
        await _edit(update, text, keyboard)
    else:
        await _reply(update, text, keyboard)


async def _show_category(update: Update, cat_id: int, page: int = 0) -> None:
    cat = db.get_category(cat_id)
    if not cat:
        await update.callback_query.answer("Category not found.")
        return

    breadcrumb = db.get_category_breadcrumb(cat_id)
    header = fmt.category_header(cat, breadcrumb)

    subcats = db.get_subcategories(cat_id)
    rules = db.get_rules_by_category(cat_id)
    tables = db.get_roll_tables_by_category(cat_id)

    # Specialised content per category slug
    items = None
    npcs = None
    locations = None
    classes = None
    ships = None
    skills = None

    slug = cat.get("slug", "")

    if slug == "weapons":
        items = db.get_items_by_type("weapon")
    elif slug == "armor":
        items = db.get_items_by_type("armor")
    elif slug == "gear-tools":
        items = db.get_items_by_type("gear")
    elif slug == "classes":
        classes = db.get_all_classes()
    elif slug == "ship-catalogue" or slug == "st-catalogue":
        ships = db.get_all_ships()
    elif slug == "skills":
        skills = db.get_all_skills()
    elif slug == "glossary":
        terms = db.get_all_terms()
        await _edit(update, f"{header}\n\nSelect a term:", kb.glossary_keyboard(terms, 0))
        return

    # Module NPC and location sub-categories
    elif slug in ("abh-npcs", "dp-npcs", "gd-npcs", "apf-npcs"):
        book_map = {"abh-npcs": 3, "dp-npcs": 7, "gd-npcs": 4, "apf-npcs": 6}
        npcs = db.get_npcs_by_book(book_map[slug])
    elif slug in ("abh-locations", "dp-locations", "gd-locations", "apf-locations"):
        book_map = {"abh-locations": 3, "dp-locations": 7, "gd-locations": 4, "apf-locations": 6}
        locations = db.get_locations_by_book(book_map[slug])

    keyboard = kb.category_menu(
        cat, subcats, rules, tables,
        items=items, npcs=npcs, locations=locations,
        classes=classes, ships=ships, skills=skills,
        page=page,
    )
    await _edit(update, header, keyboard)


# ─────────────────────────────────────────────
# COMMAND HANDLERS
# ─────────────────────────────────────────────

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info("/start  user_id=%s username=%s", user.id, user.username)
    await _show_main_menu(update, edit=False)


async def cmd_search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    query = " ".join(context.args) if context.args else ""
    if not query:
        await update.message.reply_text(
            "Usage: <code>/search &lt;term&gt;</code>\nExample: <code>/search wound</code>",
            parse_mode=ParseMode.HTML,
        )
        return
    logger.info("/search  user_id=%s query=%r", user.id, query)
    results = db.search_all(query)
    text = fmt.format_search_results(query, results)
    keyboard = kb.search_results(results)
    await _reply(update, text, keyboard)


async def cmd_roll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Quick dice roller: /roll d10, /roll 2d10, /roll d100"""
    user = update.effective_user
    notation = context.args[0] if context.args else "d10"
    result = _roll_dice(notation)
    logger.info("/roll  user_id=%s notation=%s result=%s", user.id, notation, result)
    await update.message.reply_text(
        f"🎲 <b>{notation.upper()}</b> → <code>{result}</code>",
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# CALLBACK ROUTER
# ─────────────────────────────────────────────

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data
    user = update.effective_user
    logger.info("callback  user_id=%s data=%r", user.id, data)

    try:
        await _dispatch_callback(update, query, data)
    except Exception:
        logger.exception("Unhandled error in callback  user_id=%s data=%r", user.id, data)
        try:
            await query.edit_message_text(
                "⚠️ Something went wrong. Please try again or return to the main menu.",
                reply_markup=kb.back_only("menu"),
                parse_mode=ParseMode.HTML,
            )
        except Exception:
            pass


async def _dispatch_callback(update: Update, query, data: str) -> None:
    # ── Main menu ──────────────────────────────
    if data == "menu":
        await _show_main_menu(update, edit=True)
        return

    # ── Search prompt ──────────────────────────
    if data == "search":
        await _edit(update,
            "🔍 <b>Search</b>\n\nSend: <code>/search &lt;term&gt;</code>\n\nExample: <code>/search stress</code>",
            kb.back_only("menu")
        )
        return

    # ── Category navigation ────────────────────
    if data.startswith("cat:"):
        parts = data.split(":")
        cat_id = int(parts[1])
        page = int(parts[3]) if len(parts) == 4 and parts[2] == "page" else 0
        await _show_category(update, cat_id, page)
        return

    # ── Glossary pagination ────────────────────
    if data.startswith("glossary:page:"):
        page = int(data.split(":")[-1])
        terms = db.get_all_terms()
        cat = db.get_category(_GLOSSARY_CAT_ID)
        breadcrumb = db.get_category_breadcrumb(_GLOSSARY_CAT_ID)
        header = fmt.category_header(cat, breadcrumb)
        await _edit(update, f"{header}\n\nSelect a term:", kb.glossary_keyboard(terms, page))
        return

    # ── Rule ───────────────────────────────────
    if data.startswith("rule:"):
        rule_id = int(data.split(":")[1])
        rule = db.get_rule(rule_id)
        if not rule:
            await query.answer("Rule not found.")
            return
        terms = db.get_linked_terms("rule", rule_id)
        text = fmt.format_rule(rule)
        back = f"cat:{rule['category_id']}"
        keyboard = kb.term_buttons(terms, back)
        await _edit(update, text, keyboard)
        return

    # ── Term ───────────────────────────────────
    if data.startswith("term:"):
        term_id = int(data.split(":")[1])
        term = db.get_term(term_id)
        if not term:
            await query.answer("Term not found.")
            return
        text = fmt.format_term(term)
        # Generic back to glossary
        await _edit(update, text, kb.back_only(f"cat:{_GLOSSARY_CAT_ID}"))
        return

    # ── Item ───────────────────────────────────
    if data.startswith("item:"):
        item_id = int(data.split(":")[1])
        item = db.get_item(item_id)
        if not item:
            await query.answer("Item not found.")
            return
        terms = db.get_linked_terms("item", item_id)
        text = fmt.format_item(item)
        # Back to the appropriate sub-category
        type_cat_map = {"weapon": 13, "armor": 14, "gear": 15, "trinket": 15}
        back_cat = type_cat_map.get(item["item_type"], 12)
        keyboard = kb.term_buttons(terms, f"cat:{back_cat}")
        await _edit(update, text, keyboard)
        return

    # ── Roll Table — show table ────────────────
    if data.startswith("table:"):
        table_id = int(data.split(":")[1])
        table = db.get_roll_table(table_id)
        if not table:
            await query.answer("Table not found.")
            return
        text = fmt.format_roll_table(table)
        keyboard = kb.roll_table_keyboard(table, table.get("category_id"))
        await _edit(update, text, keyboard)
        return

    # ── Roll Table — perform roll ──────────────
    if data.startswith("roll:"):
        table_id = int(data.split(":")[1])
        table = db.get_roll_table(table_id)
        if not table:
            await query.answer("Table not found.")
            return
        roll_value = _roll_dice(table["dice_notation"])
        entry = db.get_entry_for_roll(table_id, roll_value)
        if not entry:
            # Fallback: find closest entry
            entries = db.get_table_entries(table_id)
            if entries:
                entry = min(entries, key=lambda e: abs(e["roll_min"] - roll_value))
        if not entry:
            await query.answer("No entry found for this roll.")
            return
        linked_term = db.get_term(entry["linked_term_id"]) if entry.get("linked_term_id") else None
        text = fmt.format_roll_result(table, entry, roll_value)
        keyboard = kb.roll_result_keyboard(table, entry, linked_term)
        await _edit(update, text, keyboard)
        return

    # ── Roll Table — show all entries ──────────
    if data.startswith("entries:"):
        table_id = int(data.split(":")[1])
        table = db.get_roll_table(table_id)
        entries = db.get_table_entries(table_id)
        if not table or not entries:
            await query.answer("No entries found.")
            return
        text = fmt.format_entries_list(table, entries)
        # Telegram message limit: truncate if too long
        if len(text) > 4000:
            text = text[:3950] + "\n\n<i>…[truncated — see source book for full table]</i>"
        keyboard = kb.entries_list(table, entries)
        await _edit(update, text, keyboard)
        return

    # ── Class ──────────────────────────────────
    if data.startswith("cls:"):
        class_id = int(data.split(":")[1])
        cls = db.get_class(class_id)
        if not cls:
            await query.answer("Class not found.")
            return
        terms = db.get_linked_terms("class", class_id)
        text = fmt.format_class(cls)
        keyboard = kb.term_buttons(terms, "cat:3")
        await _edit(update, text, keyboard)
        return

    # ── Skill ──────────────────────────────────
    if data.startswith("skill:"):
        skill_id = int(data.split(":")[1])
        skill = db.get_skill(skill_id)
        if not skill:
            await query.answer("Skill not found.")
            return
        text = fmt.format_skill(skill)
        await _edit(update, text, kb.back_only("cat:4"))
        return

    # ── Ship ───────────────────────────────────
    if data.startswith("ship:"):
        ship_id = int(data.split(":")[1])
        ship = db.get_ship(ship_id)
        if not ship:
            await query.answer("Ship not found.")
            return
        terms = db.get_linked_terms("ship", ship_id)
        text = fmt.format_ship(ship)
        keyboard = kb.term_buttons(terms, "cat:19")
        await _edit(update, text, keyboard)
        return

    # ── Location ───────────────────────────────
    if data.startswith("loc:"):
        loc_id = int(data.split(":")[1])
        loc = db.get_location(loc_id)
        if not loc:
            await query.answer("Location not found.")
            return
        children = db.get_child_locations(loc_id)
        terms = db.get_linked_terms("location", loc_id)
        text = fmt.format_location(loc)

        # If location has child rooms/areas, offer them as buttons
        if children:
            child_btns = [[kb._btn(f"📍 {c['name']}", f"loc:{c['id']}")] for c in children]
            term_btns = [[kb._btn(f"📖 {t['name']}", f"term:{t['id']}")] for t in terms]
            back_btn = [kb._btn("← Back", f"cat:{_loc_back_cat(loc)}")] if True else []
            from telegram import InlineKeyboardMarkup
            keyboard = InlineKeyboardMarkup(child_btns + term_btns + [back_btn])
        else:
            back = f"cat:{_loc_back_cat(loc)}"
            keyboard = kb.term_buttons(terms, back)

        await _edit(update, text, keyboard)
        return

    # ── NPC ────────────────────────────────────
    if data.startswith("npc:"):
        npc_id = int(data.split(":")[1])
        npc = db.get_npc(npc_id)
        if not npc:
            await query.answer("NPC not found.")
            return
        terms = db.get_linked_terms("npc", npc_id)
        text = fmt.format_npc(npc)
        back = f"cat:{_npc_back_cat(npc)}"
        keyboard = kb.npc_with_terms(npc, terms, back)
        await _edit(update, text, keyboard)
        return

    # ── Unknown ────────────────────────────────
    logger.warning("Unhandled callback  data=%r", data)
    await query.answer("Not implemented yet.")


# ─────────────────────────────────────────────
# APPLICATION-LEVEL ERROR HANDLER
# ─────────────────────────────────────────────

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors raised by the PTB framework (network issues, timeouts, etc.)."""
    logger.error("PTB error  update=%s", update, exc_info=context.error)


# ─────────────────────────────────────────────
# BACK-ROUTE HELPERS
# ─────────────────────────────────────────────

_BOOK_NPC_CAT = {3: 30, 7: 36, 4: 42, 6: 48}  # source_book_id → NPC category_id
_BOOK_LOC_CAT = {3: 29, 7: 35, 4: 41, 6: 47}


def _npc_back_cat(npc: dict) -> int:
    return _BOOK_NPC_CAT.get(npc.get("source_book_id"), 26)


def _loc_back_cat(loc: dict) -> int:
    return _BOOK_LOC_CAT.get(loc.get("source_book_id"), 26)


# ─────────────────────────────────────────────
# APPLICATION SETUP
# ─────────────────────────────────────────────

def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN not set. Add it to your .env file.")

    app = Application.builder().token(token).build()

    # Commands
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("search", cmd_search))
    app.add_handler(CommandHandler("roll", cmd_roll))

    # Inline keyboard callbacks
    app.add_handler(CallbackQueryHandler(callback_handler))

    # Application-level error handler
    app.add_error_handler(error_handler)

    logger.info("Mothership bot starting…")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
