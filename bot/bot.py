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
)

from . import db
from . import formatters as fmt
from . import keyboards as kb
from .i18n import t, SUPPORTED_LANGS, DEFAULT_LANG
from .logging_setup import setup_logging

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

DEV_MODE     = os.getenv("DEV_MODE", "").lower() == "true"
HOME_PAGE_ID = 1
NAV_MAX      = 20


# ─────────────────────────────────────────────
# NAV STACK HELPERS
# ─────────────────────────────────────────────
#
# nav_stack is a list of {"t": "p"|"c", "id": int}
# Current position is always stack[-1].
# An empty stack falls back to the home page.

def _lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    return context.user_data.get("lang", DEFAULT_LANG)


def _stack(context: ContextTypes.DEFAULT_TYPE) -> list:
    return context.user_data.setdefault("nav_stack", [{"t": "p", "id": HOME_PAGE_ID}])


def _current(context: ContextTypes.DEFAULT_TYPE) -> dict:
    s = _stack(context)
    return s[-1] if s else {"t": "p", "id": HOME_PAGE_ID}


def _push(context: ContextTypes.DEFAULT_TYPE, entry: dict) -> None:
    s = _stack(context)
    if s and s[-1] == entry:
        return
    # If the destination is already somewhere in the stack, truncate back to
    # it instead of pushing a duplicate — prevents A→B→A→B…cycle growth.
    for i, e in enumerate(s):
        if e == entry:
            del s[i + 1:]
            return
    s.append(entry)
    if len(s) > NAV_MAX:
        s.pop(0)


def _pop(context: ContextTypes.DEFAULT_TYPE) -> None:
    s = _stack(context)
    if len(s) > 1:
        s.pop()


def _reset(context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data["nav_stack"] = [{"t": "p", "id": HOME_PAGE_ID}]


def _save(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    db.save_user_state(user_id, lang=_lang(context), nav_stack=_stack(context))


def _load(user_id: int, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data.get("_loaded"):
        return
    state = db.get_user_state(user_id)
    if state:
        context.user_data.setdefault("lang", state["lang"] or DEFAULT_LANG)
        context.user_data.setdefault(
            "nav_stack",
            state["nav_stack"] or [{"t": "p", "id": HOME_PAGE_ID}]
        )
        logger.debug("state loaded  user_id=%s depth=%d lang=%s",
                     user_id, len(context.user_data["nav_stack"]), context.user_data["lang"])
    else:
        context.user_data.setdefault("lang", DEFAULT_LANG)
        context.user_data.setdefault("nav_stack", [{"t": "p", "id": HOME_PAGE_ID}])
    context.user_data["_loaded"] = True


# ─────────────────────────────────────────────
# DICE
# ─────────────────────────────────────────────

def _roll(notation: str) -> int:
    notation = notation.lower().strip()
    m = re.match(r"^(\d*)d(\d+)$", notation)
    if not m:
        return 1
    count = int(m.group(1)) if m.group(1) else 1
    sides = int(m.group(2))
    return sum(random.randint(1, sides) for _ in range(count))


# ─────────────────────────────────────────────
# SEND / EDIT HELPERS
# ─────────────────────────────────────────────

async def _edit(update: Update, text: str, keyboard, context=None) -> None:
    if DEV_MODE and context is not None:
        s     = context.user_data.get("nav_stack", [])
        lines = "\n".join(f"  {i+1}. {e}" for i, e in enumerate(reversed(s))) or "  (empty)"
        text += f"\n\n<code>🛠 DEV\n{lines}</code>"
    try:
        await update.callback_query.edit_message_text(
            text=text,
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
        )
    except BadRequest as e:
        if "Message is not modified" not in str(e):
            raise


async def _send(update: Update, text: str, keyboard) -> None:
    await update.message.reply_text(
        text=text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# RENDERERS
# ─────────────────────────────────────────────

async def _render_page(update: Update, page_id: int, context, edit: bool = True) -> None:
    lang  = _lang(context)
    depth = len(_stack(context))

    page = db.get_page(page_id, lang)
    if not page:
        if edit:
            await update.callback_query.answer(t(lang, "err_not_found"))
        return

    child_pages = db.get_pages_by_ids(page["linked_pages"], lang)
    contents    = db.get_page_contents(page_id, lang)
    text        = fmt.format_page(page, lang)
    keyboard    = kb.page_keyboard(child_pages, contents, lang, depth)

    if edit:
        await _edit(update, text, keyboard, context=context)
    else:
        await _send(update, text, keyboard)


async def _render_content(update: Update, content_id: int, context, page: int = 0) -> None:
    lang  = _lang(context)
    depth = len(_stack(context))

    content = db.get_content(content_id, lang)
    if not content:
        await update.callback_query.answer(t(lang, "err_not_found"))
        return

    links    = db.get_content_links(content_id, lang)
    has_dice = content.get("dice") is not None
    entries  = content["dice"].get("entries", []) if has_dice else []

    text     = fmt.format_dice_table(content, lang) if has_dice else fmt.format_content(content, lang)
    keyboard = kb.content_keyboard(links, lang, depth, content_id=content_id, has_dice=has_dice, entries=entries, page=page)

    await _edit(update, text, keyboard, context=context)


async def _render_current(update: Update, context, edit: bool = True) -> None:
    cur = _current(context)
    if cur["t"] == "p":
        await _render_page(update, cur["id"], context, edit=edit)
    else:
        await _render_content(update, cur["id"], context)


# ─────────────────────────────────────────────
# COMMAND HANDLERS
# ─────────────────────────────────────────────

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info("/start  user_id=%s username=%s", user.id, user.username)
    _load(user.id, context)
    _reset(context)
    _save(user.id, context)
    await _render_page(update, HOME_PAGE_ID, context, edit=False)


async def cmd_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info("/lang  user_id=%s", user.id)
    lang = _lang(context)
    await _send(update, f"{t(lang, 'lang_title')}\n\n{t(lang, 'lang_select')}", kb.lang_keyboard())


async def cmd_search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user  = update.effective_user
    lang  = _lang(context)
    query = " ".join(context.args) if context.args else ""
    if not query:
        await update.message.reply_text(t(lang, "search_usage"), parse_mode=ParseMode.HTML)
        return
    logger.info("/search  user_id=%s query=%r", user.id, query)
    results  = db.search(query, lang)
    text     = fmt.format_search_results(query, results, lang)
    keyboard = kb.search_results_keyboard(results, lang)
    await _send(update, text, keyboard)


async def cmd_roll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user     = update.effective_user
    notation = context.args[0] if context.args else "d10"
    result   = _roll(notation)
    lang     = _lang(context)
    logger.info("/roll  user_id=%s notation=%s result=%s", user.id, notation, result)
    await update.message.reply_text(
        t(lang, "roll_result", notation=notation.upper(), value=result),
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# CALLBACK HANDLER
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

    _load(user.id, context)

    try:
        await _dispatch(update, data, context)
    except Exception:
        logger.exception("Unhandled error  user_id=%s data=%r", user.id, data)
        _reset(context)
        _save(user.id, context)
        try:
            await _render_page(update, HOME_PAGE_ID, context)
        except Exception:
            pass


async def _dispatch(update: Update, data: str, context) -> None:
    lang = _lang(context)
    uid  = update.effective_user.id

    # ── Language selection ──────────────────────────
    if data.startswith("setlang:"):
        new_lang = data.split(":")[1]
        if new_lang in SUPPORTED_LANGS:
            context.user_data["lang"] = new_lang
            db.set_user_lang(uid, new_lang)
            _reset(context)
            _save(uid, context)
            await _render_page(update, HOME_PAGE_ID, context)
        return

    # ── Home ────────────────────────────────────────
    if data == "home":
        _reset(context)
        _save(uid, context)
        await _render_page(update, HOME_PAGE_ID, context)
        return

    # ── Back ────────────────────────────────────────
    if data == "back":
        _pop(context)
        _save(uid, context)
        await _render_current(update, context)
        return

    # ── Back to dice table (from roll/pick result) ──
    if data.startswith("back_table:"):
        content_id = int(data[11:])
        await _render_content(update, content_id, context)
        return

    # ── Navigate to page ────────────────────────────
    if data.startswith("p:"):
        page_id = int(data[2:])
        _push(context, {"t": "p", "id": page_id})
        _save(uid, context)
        await _render_page(update, page_id, context)
        return

    # ── Navigate to content ─────────────────────────
    if data.startswith("c:"):
        content_id = int(data[2:])
        _push(context, {"t": "c", "id": content_id})
        _save(uid, context)
        await _render_content(update, content_id, context)
        return

    # ── Roll on dice table ──────────────────────────
    if data.startswith("roll:"):
        content_id = int(data[5:])
        content    = db.get_content(content_id, lang)
        if not content or not content.get("dice"):
            await update.callback_query.answer(t(lang, "err_not_found"))
            return

        dice    = content["dice"]
        entries = dice.get("entries", [])
        if not entries:
            await update.callback_query.answer(t(lang, "err_not_found"))
            return

        die_name   = dice.get("die", f"d{max(e.get('max', 1) for e in entries)}")
        roll_value = _roll(die_name)
        entry      = next(
            (e for e in entries if e.get("min", 0) <= roll_value <= e.get("max", 0)),
            entries[-1],
        )

        depth    = len(_stack(context))
        text     = fmt.format_roll_result(content, roll_value, entry, lang)
        keyboard = kb.roll_result_keyboard(content_id, entry.get("links", []), lang, depth)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Paginate dice table entries ─────────────────
    if data.startswith("pick_page:"):
        _, cid_s, pg_s = data.split(":", 2)
        content_id = int(cid_s)
        page       = int(pg_s)
        await _render_content(update, content_id, context, page=page)
        return

    # ── Pick entry from dice table ──────────────────
    if data.startswith("pick:"):
        _, cid_s, idx_s = data.split(":", 2)
        content_id = int(cid_s)
        idx        = int(idx_s)
        content    = db.get_content(content_id, lang)
        if not content or not content.get("dice"):
            await update.callback_query.answer(t(lang, "err_not_found"))
            return
        entries = content["dice"].get("entries", [])
        if not (0 <= idx < len(entries)):
            await update.callback_query.answer(t(lang, "err_not_found"))
            return
        entry    = entries[idx]
        depth    = len(_stack(context))
        text     = fmt.format_roll_result(content, 0, entry, lang, picked=True)
        keyboard = kb.roll_result_keyboard(content_id, entry.get("links", []), lang, depth)
        await _edit(update, text, keyboard, context=context)
        return

    # ── noop ────────────────────────────────────────
    if data == "noop":
        return

    logger.warning("Unhandled callback  data=%r", data)
    await update.callback_query.answer(t(lang, "err_not_impl"))


# ─────────────────────────────────────────────
# ERROR HANDLER
# ─────────────────────────────────────────────

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("PTB error  update=%s", update, exc_info=context.error)
    if isinstance(update, Update) and update.callback_query:
        user = update.effective_user
        if user:
            _reset(context)
            _save(user.id, context)
        try:
            await _render_page(update, HOME_PAGE_ID, context)
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
    app.add_handler(CommandHandler("lang",   cmd_lang))
    app.add_handler(CommandHandler("search", cmd_search))
    app.add_handler(CommandHandler("roll",   cmd_roll))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_error_handler(error_handler)

    logger.info("Mothership bot starting…")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
