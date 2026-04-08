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
from telegram.error import BadRequest
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from . import db, formatters as fmt, keyboards as kb
from .i18n import t, SUPPORTED_LANGS, DEFAULT_LANG
from .logging_setup import setup_logging

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

_GLOSSARY_CAT_ID = 21
DEV_MODE = os.getenv("DEV_MODE", "").lower() == "true"

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def _lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    """Return the active language for this user session."""
    return context.user_data.get("language", DEFAULT_LANG)


async def _edit(update: Update, text: str, keyboard, parse_mode=ParseMode.HTML, context=None) -> None:
    """Edit the current message in-place."""
    if DEV_MODE and context is not None:
        stack: list = context.user_data.get("nav_stack", [])
        current = context.user_data.get("nav_current", "—")
        stack_lines = "\n".join(f"  {i+1}. {s}" for i, s in enumerate(reversed(stack))) or "  (empty)"
        text += f"\n\n<code>🛠 DEV MODE\ncurrent: {current}\nstack (top→bottom):\n{stack_lines}</code>"
    try:
        await update.callback_query.edit_message_text(
            text=text,
            reply_markup=keyboard,
            parse_mode=parse_mode,
        )
    except BadRequest as e:
        if "Message is not modified" not in str(e):
            raise


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

async def _show_main_menu(update: Update, edit: bool = False, context=None) -> None:
    lang = _lang(context) if context else DEFAULT_LANG
    cats = db.get_top_level_categories(lang)
    text = (
        f"{t(lang, 'main_menu_title')}\n\n"
        f"{t(lang, 'main_menu_desc')}\n\n"
        f"{t(lang, 'main_menu_select')}"
    )
    keyboard = kb.main_menu(cats, lang)
    if edit:
        await _edit(update, text, keyboard, context=context)
    else:
        await _reply(update, text, keyboard)


async def _show_category(update: Update, cat_id: int, page: int = 0, context=None) -> None:
    lang = _lang(context) if context else DEFAULT_LANG

    cat = db.get_category(cat_id, lang)
    if not cat:
        await update.callback_query.answer(t(lang, "err_category"))
        return

    breadcrumb = db.get_category_breadcrumb(cat_id, lang)
    header = fmt.category_header(cat, breadcrumb)

    subcats = db.get_subcategories(cat_id, lang)
    rules = db.get_rules_by_category(cat_id, lang)
    tables = db.get_roll_tables_by_category(cat_id, lang)

    items = None
    npcs = None
    locations = None
    classes = None
    ships = None
    skills = None

    slug = cat.get("slug", "")

    if slug == "weapons":
        items = db.get_items_by_type("weapon", lang)
    elif slug == "armor":
        items = db.get_items_by_type("armor", lang)
    elif slug == "gear-tools":
        items = db.get_items_by_type("gear", lang)
    elif slug == "classes":
        classes = db.get_all_classes(lang)
    elif slug == "ship-catalogue" or slug == "st-catalogue":
        ships = db.get_all_ships(lang)
    elif slug == "skills":
        skills = db.get_all_skills(lang)
    elif slug == "glossary":
        terms = db.get_all_terms(lang)
        await _edit(update, f"{header}\n\n{t(lang, 'glossary_select')}", kb.glossary_keyboard(terms, 0, lang), context=context)
        return
    elif slug == "roll-tables":
        tables = db.get_all_roll_tables(lang)
    elif slug in ("abh-npcs", "dp-npcs", "gd-npcs", "apf-npcs"):
        book_map = {"abh-npcs": 3, "dp-npcs": 7, "gd-npcs": 4, "apf-npcs": 6}
        npcs = db.get_npcs_by_book(book_map[slug], lang)
    elif slug in ("abh-locations", "dp-locations", "gd-locations", "apf-locations"):
        book_map = {"abh-locations": 3, "dp-locations": 7, "gd-locations": 4, "apf-locations": 6}
        locations = db.get_locations_by_book(book_map[slug], lang=lang)

    # Single-item auto-navigation
    if not subcats and page == 0:
        all_content: list[tuple[str, int]] = (
            [("rule", r["id"]) for r in rules]
            + [("table", tb["id"]) for tb in tables]
            + [("item", i["id"]) for i in (items or [])]
            + [("npc", n["id"]) for n in (npcs or [])]
            + [("loc", l["id"]) for l in (locations or [])]
            + [("cls", c["id"]) for c in (classes or [])]
            + [("ship", s["id"]) for s in (ships or [])]
            + [("skill", sk["id"]) for sk in (skills or [])]
        )
        if len(all_content) == 1:
            cb_type, item_id = all_content[0]
            await _dispatch_callback(update, update.callback_query, f"{cb_type}:{item_id}", context=context)
            return

    keyboard = kb.category_menu(
        cat, subcats, rules, tables,
        items=items, npcs=npcs, locations=locations,
        classes=classes, ships=ships, skills=skills,
        page=page, lang=lang,
    )
    await _edit(update, header, keyboard, context=context)


# ─────────────────────────────────────────────
# COMMAND HANDLERS
# ─────────────────────────────────────────────

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info("/start  user_id=%s username=%s", user.id, user.username)
    _ensure_nav_loaded(user.id, context)
    await _show_main_menu(update, edit=False, context=context)


async def cmd_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show language selection keyboard."""
    user = update.effective_user
    logger.info("/lang  user_id=%s", user.id)
    lang = _lang(context)
    text = f"{t(lang, 'lang_title')}\n\n{t(lang, 'lang_select')}"
    await _reply(update, text, kb.lang_keyboard())


async def cmd_search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    lang = _lang(context)
    query = " ".join(context.args) if context.args else ""
    if not query:
        await update.message.reply_text(t(lang, "search_usage"), parse_mode=ParseMode.HTML)
        return
    logger.info("/search  user_id=%s query=%r", user.id, query)
    results = db.search_all(query)
    text = fmt.format_search_results(query, results, lang)
    keyboard = kb.search_results(results, lang)
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
# NAVIGATION STACK
# ─────────────────────────────────────────────

_NAV_STACK_MAX = 10

_NAV_SKIP = {"noop", "back", "menu", "search"}

_PAGINATION_RE = re.compile(r'^(cat:\d+:page:\d+|entries:\d+:page:\d+|glossary:page:\d+)$')


def _push_page(context: ContextTypes.DEFAULT_TYPE, new_data: str) -> None:
    """Push the current page onto the history stack, then update current."""
    current = context.user_data.get("nav_current")
    if current:
        stack: list = context.user_data.setdefault("nav_stack", [])
        if not stack or stack[-1] != current:
            stack.append(current)
        if len(stack) > _NAV_STACK_MAX:
            stack.pop(0)
    if new_data.startswith("roll:"):
        context.user_data["nav_current"] = f"table:{new_data.split(':')[1]}"
    else:
        context.user_data["nav_current"] = new_data


def _pop_page(context: ContextTypes.DEFAULT_TYPE) -> str | None:
    stack: list = context.user_data.get("nav_stack", [])
    if stack:
        prev = stack.pop()
        context.user_data["nav_current"] = prev
        return prev
    return None


# ─────────────────────────────────────────────
# NAV STATE PERSISTENCE
# ─────────────────────────────────────────────

def _save_nav(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Write the current nav state and language to DB immediately."""
    db.save_nav_state(
        user_id,
        context.user_data.get("nav_current"),
        context.user_data.get("nav_stack", []),
        context.user_data.get("language", DEFAULT_LANG),
    )


def _ensure_nav_loaded(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Lazy-load nav state + language from DB on first interaction."""
    if "nav_loaded" not in context.user_data:
        saved = db.load_nav_state(user_id)
        if saved:
            context.user_data.setdefault("nav_stack", saved["nav_stack"])
            context.user_data.setdefault("nav_current", saved["nav_current"])
            context.user_data.setdefault("language", saved.get("language", DEFAULT_LANG))
            logger.debug("nav restore  user_id=%s current=%s depth=%d lang=%s",
                         user_id, saved["nav_current"], len(saved["nav_stack"]),
                         saved.get("language", DEFAULT_LANG))
        context.user_data["nav_loaded"] = True


# ─────────────────────────────────────────────
# CALLBACK ROUTER
# ─────────────────────────────────────────────

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    try:
        await query.answer()
    except BadRequest:
        pass
    data = query.data
    user = update.effective_user
    logger.info("callback  user_id=%s data=%r", user.id, data)

    _ensure_nav_loaded(user.id, context)

    # ── Language selection ─────────────────────────
    if data.startswith("setlang:"):
        new_lang = data.split(":")[1]
        if new_lang in SUPPORTED_LANGS:
            context.user_data["language"] = new_lang
            db.set_user_language(user.id, new_lang)
            confirm_key = f"lang_set_{new_lang}"
            try:
                await query.answer(t(new_lang, confirm_key), show_alert=False)
            except BadRequest:
                pass
            # Re-render main menu in the new language
            context.user_data["nav_stack"] = []
            context.user_data["nav_current"] = None
            _save_nav(user.id, context)
            await _show_main_menu(update, edit=True, context=context)
        return

    # ── Stack management ───────────────────────────
    if data == "noop":
        return

    if data == "back":
        prev = _pop_page(context)
        if prev:
            data = prev
        else:
            context.user_data["nav_current"] = None
            _save_nav(user.id, context)
            await _show_main_menu(update, edit=True, context=context)
            return
    elif data == "menu":
        context.user_data["nav_stack"] = []
        context.user_data["nav_current"] = None
    elif data not in _NAV_SKIP:
        if _PAGINATION_RE.match(data):
            context.user_data["nav_current"] = data
        else:
            _push_page(context, data)

    _save_nav(user.id, context)

    try:
        await _dispatch_callback(update, query, data, context=context)
    except Exception:
        logger.exception(
            "Unhandled error in callback  user_id=%s username=%s data=%r",
            user.id, user.username, data,
        )
        context.user_data["nav_stack"] = []
        context.user_data["nav_current"] = None
        _save_nav(user.id, context)
        try:
            await _show_main_menu(update, edit=True, context=context)
        except Exception:
            pass


async def _dispatch_callback(update: Update, query, data: str, context=None) -> None:
    lang = _lang(context) if context else DEFAULT_LANG

    # ── Main menu ──────────────────────────────────
    if data == "menu":
        await _show_main_menu(update, edit=True, context=context)
        return

    # ── Search prompt ──────────────────────────────
    if data == "search":
        await _edit(update,
            f"{t(lang, 'search_prompt_title')}\n\n{t(lang, 'search_prompt_body')}",
            kb.back_only(lang),
            context=context,
        )
        return

    # ── Category navigation ────────────────────────
    if data.startswith("cat:"):
        parts = data.split(":")
        cat_id = int(parts[1])
        page = int(parts[3]) if len(parts) == 4 and parts[2] == "page" else 0
        await _show_category(update, cat_id, page, context=context)
        return

    # ── Glossary pagination ────────────────────────
    if data.startswith("glossary:page:"):
        page = int(data.split(":")[-1])
        terms = db.get_all_terms(lang)
        cat = db.get_category(_GLOSSARY_CAT_ID, lang)
        breadcrumb = db.get_category_breadcrumb(_GLOSSARY_CAT_ID, lang)
        header = fmt.category_header(cat, breadcrumb)
        await _edit(update, f"{header}\n\n{t(lang, 'glossary_select')}", kb.glossary_keyboard(terms, page, lang), context=context)
        return

    # ── Rule ───────────────────────────────────────
    if data.startswith("rule:"):
        rule_id = int(data.split(":")[1])
        rule = db.get_rule(rule_id, lang)
        if not rule:
            await query.answer(t(lang, "err_rule"))
            return
        terms = db.get_linked_terms("rule", rule_id, lang)
        text = fmt.format_rule(rule, lang)
        keyboard = kb.term_buttons(terms, lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Term ───────────────────────────────────────
    if data.startswith("term:"):
        term_id = int(data.split(":")[1])
        term = db.get_term(term_id, lang)
        if not term:
            await query.answer(t(lang, "err_term"))
            return
        text = fmt.format_term(term, lang)
        tables = db.get_roll_tables_for_term(term["id"], lang)
        keyboard = kb.term_with_tables(tables, lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Item ───────────────────────────────────────
    if data.startswith("item:"):
        item_id = int(data.split(":")[1])
        item = db.get_item(item_id, lang)
        if not item:
            await query.answer(t(lang, "err_item"))
            return
        terms = db.get_linked_terms("item", item_id, lang)
        if item["item_type"] == "weapon":
            if item.get("wound_type"):
                wound_term = db.get_term_by_name(item["wound_type"], lang)
                if wound_term and not any(tr["id"] == wound_term["id"] for tr in terms):
                    terms = [wound_term] + terms
            if item.get("range_band"):
                range_term = db.get_term_by_name("Range Band", lang)
                if range_term and not any(tr["id"] == range_term["id"] for tr in terms):
                    terms = terms + [range_term]
        text = fmt.format_item(item, lang)
        keyboard = kb.term_buttons(terms, lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Roll Table — show table ────────────────────
    if data.startswith("table:"):
        table_id = int(data.split(":")[1])
        table = db.get_roll_table(table_id, lang)
        if not table:
            await query.answer(t(lang, "err_table"))
            return
        text = fmt.format_roll_table(table, lang)
        keyboard = kb.roll_table_keyboard(table, lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Roll Table — perform roll ──────────────────
    if data.startswith("roll:"):
        table_id = int(data.split(":")[1])
        table = db.get_roll_table(table_id, lang)
        if not table:
            await query.answer(t(lang, "err_table"))
            return
        roll_value = _roll_dice(table["dice_notation"])
        entry = db.get_entry_for_roll(table_id, roll_value, lang)
        if not entry:
            entries = db.get_table_entries(table_id, lang)
            if entries:
                entry = min(entries, key=lambda e: abs(e["roll_min"] - roll_value))
        if not entry:
            await query.answer(t(lang, "err_no_roll"))
            return
        linked_term = db.get_term(entry["linked_term_id"], lang) if entry.get("linked_term_id") else None
        items = db.find_items_in_text(entry["result_text"], lang) if table.get("category_id") == 5 else None
        text = fmt.format_roll_result(table, entry, roll_value, lang)
        keyboard = kb.roll_result_keyboard(table, entry, linked_term, items=items, lang=lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Roll Table — show all entries ──────────────
    if data.startswith("entries:"):
        parts = data.split(":")
        table_id = int(parts[1])
        page = int(parts[3]) if len(parts) == 4 and parts[2] == "page" else 0
        table = db.get_roll_table(table_id, lang)
        entries = db.get_table_entries(table_id, lang)
        if not table or not entries:
            await query.answer(t(lang, "err_no_entries"))
            return
        total = len(entries)
        text = fmt.format_roll_table_header(table, total, lang)
        keyboard = kb.entries_list(table, entries, page, lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Roll Table — single entry detail ───────────
    if data.startswith("entry:"):
        _, table_id_str, entry_id_str = data.split(":")
        table_id = int(table_id_str)
        entry_id = int(entry_id_str)
        table = db.get_roll_table(table_id, lang)
        entry = db.get_entry(entry_id, lang)
        if not table or not entry:
            await query.answer(t(lang, "err_entry"))
            return
        linked_term = db.get_term(entry["linked_term_id"], lang) if entry.get("linked_term_id") else None
        items = db.find_items_in_text(entry["result_text"], lang) if table.get("category_id") == 5 else None
        text = fmt.format_roll_result(table, entry, entry["roll_min"], lang)
        keyboard = kb.roll_result_keyboard(table, entry, linked_term, items=items, lang=lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Class ──────────────────────────────────────
    if data.startswith("cls:"):
        class_id = int(data.split(":")[1])
        cls = db.get_class(class_id, lang)
        if not cls:
            await query.answer(t(lang, "err_class"))
            return
        terms = db.get_linked_terms("class", class_id, lang)
        text = fmt.format_class(cls, lang)
        keyboard = kb.term_buttons(terms, lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Skill ──────────────────────────────────────
    if data.startswith("skill:"):
        skill_id = int(data.split(":")[1])
        skill = db.get_skill(skill_id, lang)
        if not skill:
            await query.answer(t(lang, "err_skill"))
            return
        text = fmt.format_skill(skill, lang)
        await _edit(update, text, kb.back_only(lang), context=context)
        return

    # ── Ship ───────────────────────────────────────
    if data.startswith("ship:"):
        ship_id = int(data.split(":")[1])
        ship = db.get_ship(ship_id, lang)
        if not ship:
            await query.answer(t(lang, "err_ship"))
            return
        terms = db.get_linked_terms("ship", ship_id, lang)
        text = fmt.format_ship(ship, lang)
        keyboard = kb.term_buttons(terms, lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Location ───────────────────────────────────
    if data.startswith("loc:"):
        loc_id = int(data.split(":")[1])
        loc = db.get_location(loc_id, lang)
        if not loc:
            await query.answer(t(lang, "err_location"))
            return
        children = db.get_child_locations(loc_id, lang)
        terms = db.get_linked_terms("location", loc_id, lang)
        text = fmt.format_location(loc, lang)

        if children:
            from telegram import InlineKeyboardMarkup
            child_btns = [[kb._btn(f"📍 {c['name']}", f"loc:{c['id']}")] for c in children]
            term_btns = [[kb._btn(f"📖 {tr['name']}", f"term:{tr['id']}")] for tr in terms]
            keyboard = InlineKeyboardMarkup(child_btns + term_btns + [kb._back(lang)])
        else:
            keyboard = kb.term_buttons(terms, lang)

        await _edit(update, text, keyboard, context=context)
        return

    # ── NPC ────────────────────────────────────────
    if data.startswith("npc:"):
        npc_id = int(data.split(":")[1])
        npc = db.get_npc(npc_id, lang)
        if not npc:
            await query.answer(t(lang, "err_npc"))
            return
        terms = db.get_linked_terms("npc", npc_id, lang)
        text = fmt.format_npc(npc, lang)
        keyboard = kb.npc_with_terms(npc, terms, lang)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Unknown ────────────────────────────────────
    logger.warning("Unhandled callback  data=%r", data)
    await query.answer(t(lang, "err_not_implemented"))


# ─────────────────────────────────────────────
# APPLICATION-LEVEL ERROR HANDLER
# ─────────────────────────────────────────────

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log PTB framework errors (network issues, timeouts, etc.) with full traceback."""
    logger.exception(
        "PTB framework error  update=%s",
        update,
        exc_info=context.error,
    )
    if isinstance(update, Update) and update.callback_query:
        user = update.effective_user
        if user:
            context.user_data["nav_stack"] = []
            context.user_data["nav_current"] = None
            _save_nav(user.id, context)
        try:
            await _show_main_menu(update, edit=True, context=context)
        except Exception:
            pass


# ─────────────────────────────────────────────
# APPLICATION SETUP
# ─────────────────────────────────────────────

def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN not set. Add it to your .env file.")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("lang", cmd_lang))
    app.add_handler(CommandHandler("search", cmd_search))
    app.add_handler(CommandHandler("roll", cmd_roll))

    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_error_handler(error_handler)

    logger.info("Mothership bot starting…")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass  # Clean Ctrl+C shutdown — Windows asyncio lets this escape run_until_complete
