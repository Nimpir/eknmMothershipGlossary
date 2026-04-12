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
    db.save_user_state(
        user_id,
        lang=_lang(context),
        nav_stack=_stack(context),
        msg_ids=context.user_data.get("msg_ids", []),
    )


def _track_msg(context: ContextTypes.DEFAULT_TYPE, msg_id: int) -> None:
    ids = context.user_data.setdefault("msg_ids", [])
    if msg_id not in ids:
        ids.append(msg_id)
    if len(ids) > 100:
        context.user_data["msg_ids"] = ids[-100:]


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
        context.user_data.setdefault("msg_ids", state.get("msg_ids") or [])
        logger.debug("state loaded  user_id=%s depth=%d lang=%s",
                     user_id, len(context.user_data["nav_stack"]), context.user_data["lang"])
    else:
        context.user_data.setdefault("lang", DEFAULT_LANG)
        context.user_data.setdefault("nav_stack", [{"t": "p", "id": HOME_PAGE_ID}])
        context.user_data.setdefault("msg_ids", [])
    context.user_data["_loaded"] = True


# ─────────────────────────────────────────────
# DICE
# ─────────────────────────────────────────────

def _roll(notation: str) -> int:
    notation = notation.lower().strip()
    m = re.match(r"^(\d*)d(\d+)$", notation)
    if not m:
        return 1
    count = min(int(m.group(1)) if m.group(1) else 1, 100)
    sides = int(m.group(2))
    if sides < 2:
        return 1
    return sum(random.randint(1, sides) for _ in range(count))


# ─────────────────────────────────────────────
# SEND / EDIT HELPERS
# ─────────────────────────────────────────────

_TG_MAX = 4096
_CAP_MAX = 1024          # Telegram photo caption limit
_TRUNCATION_MARKER = "\n\n<i>…</i>"


def _truncate(text: str, limit: int = _TG_MAX) -> str:
    """Trim text to the given char limit, cutting at a line boundary."""
    if len(text) <= limit:
        return text
    cutoff = limit - len(_TRUNCATION_MARKER)
    trimmed = text[:cutoff]
    last_nl = trimmed.rfind("\n")
    if last_nl > 0:
        trimmed = trimmed[:last_nl]
    return trimmed + _TRUNCATION_MARKER


async def _edit(update: Update, text: str, keyboard, context=None) -> None:
    if DEV_MODE and context is not None:
        s     = context.user_data.get("nav_stack", [])
        lines = "\n".join(f"  {i+1}. {e}" for i, e in enumerate(reversed(s))) or "  (empty)"
        text += f"\n\n<code>🛠 DEV\n{lines}</code>"

    msg = update.callback_query.message

    # If the current message is a photo card, we can't edit_message_text on it.
    # Delete it and send a fresh text message instead.
    if msg.photo:
        await msg.delete()
        sent = await context.bot.send_message(
            chat_id=msg.chat_id,
            text=_truncate(text),
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
        )
        if context is not None:
            _track_msg(context, sent.message_id)
        return

    try:
        await update.callback_query.edit_message_text(
            text=_truncate(text),
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
        )
    except BadRequest as e:
        if "Message is not modified" not in str(e):
            raise


async def _send(update: Update, text: str, keyboard, context=None) -> None:
    msg = await update.message.reply_text(
        text=text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )
    if context is not None:
        _track_msg(context, msg.message_id)


async def _send_image(update: Update, text: str, keyboard, image_path: str, context=None) -> None:
    """Send a new photo card (used on initial render, not a callback edit)."""
    if DEV_MODE and context is not None:
        s     = context.user_data.get("nav_stack", [])
        lines = "\n".join(f"  {i+1}. {e}" for i, e in enumerate(reversed(s))) or "  (empty)"
        text += f"\n\n<code>🛠 DEV\n{lines}</code>"
    try:
        with open(image_path, "rb") as f:
            sent = await update.message.reply_photo(
                photo=f,
                caption=_truncate(text, _CAP_MAX),
                reply_markup=keyboard,
                parse_mode=ParseMode.HTML,
            )
    except Exception:
        logger.warning("Failed to send image card: %s", image_path)
        sent = await update.message.reply_text(
            text=_truncate(text),
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
        )
    if context is not None:
        _track_msg(context, sent.message_id)


async def _show_image_result(
    update: Update, text: str, keyboard, image_path: str, context
) -> None:
    """Replace the current message with a photo card (caption + keyboard)."""
    if DEV_MODE:
        s     = context.user_data.get("nav_stack", [])
        lines = "\n".join(f"  {i+1}. {e}" for i, e in enumerate(reversed(s))) or "  (empty)"
        text += f"\n\n<code>🛠 DEV\n{lines}</code>"
    msg = update.callback_query.message
    await msg.delete()
    try:
        with open(image_path, "rb") as f:
            sent = await context.bot.send_photo(
                chat_id=msg.chat_id,
                photo=f,
                caption=_truncate(text, _CAP_MAX),
                reply_markup=keyboard,
                parse_mode=ParseMode.HTML,
            )
    except Exception:
        logger.warning("Failed to send image card: %s", image_path)
        sent = await context.bot.send_message(
            chat_id=msg.chat_id,
            text=_truncate(text),
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
        )
    _track_msg(context, sent.message_id)


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

    child_pages  = db.get_pages_by_ids(page["linked_pages"], lang)
    contents     = db.get_page_contents(page_id, lang)
    text         = fmt.format_page(page, lang)
    has_workflow = bool(page.get("workflow_steps"))
    keyboard     = kb.page_keyboard(child_pages, contents, lang, depth,
                                    page_id=page_id, has_workflow=has_workflow)

    image_path = page.get("image_url")
    if image_path and os.path.isfile(image_path):
        if edit:
            await _show_image_result(update, text, keyboard, image_path, context)
        else:
            await _send_image(update, text, keyboard, image_path, context)
    elif edit:
        await _edit(update, text, keyboard, context=context)
    else:
        await _send(update, text, keyboard, context=context)


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

    image_path = content.get("image_url")
    if image_path and os.path.isfile(image_path):
        await _show_image_result(update, text, keyboard, image_path, context)
    else:
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

    # Delete all previous bot messages for a clean session start
    chat_id = update.effective_chat.id
    for msg_id in context.user_data.pop("msg_ids", []):
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
        except Exception:
            pass

    _reset(context)
    _save(user.id, context)
    await _render_page(update, HOME_PAGE_ID, context, edit=False)


async def cmd_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info("/lang  user_id=%s", user.id)
    lang = _lang(context)
    await _send(update, f"{t(lang, 'lang_title')}\n\n{t(lang, 'lang_select')}", kb.lang_keyboard(), context=context)


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
    await _send(update, text, keyboard, context=context)


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
        try:
            content_id = int(data[11:])
        except ValueError:
            return
        await _render_content(update, content_id, context)
        return

    # ── Navigate to page ────────────────────────────
    if data.startswith("p:"):
        try:
            page_id = int(data[2:])
        except ValueError:
            return
        _push(context, {"t": "p", "id": page_id})
        _save(uid, context)
        await _render_page(update, page_id, context)
        return

    # ── Navigate to content ─────────────────────────
    if data.startswith("c:"):
        try:
            content_id = int(data[2:])
        except ValueError:
            return
        _push(context, {"t": "c", "id": content_id})
        _save(uid, context)
        await _render_content(update, content_id, context)
        return

    # ── Roll on dice table ──────────────────────────
    if data.startswith("roll:"):
        try:
            content_id = int(data[5:])
        except ValueError:
            return
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
            (e for e in entries if e.get("min", 1) <= roll_value <= e.get("max", e.get("min", 1))),
            entries[-1],
        )

        depth      = len(_stack(context))
        text       = fmt.format_roll_result(content, roll_value, entry, lang)
        keyboard   = kb.roll_result_keyboard(content_id, entry.get("links", []), lang, depth)
        image_path = entry.get("image")
        if image_path and os.path.isfile(image_path):
            await _show_image_result(update, text, keyboard, image_path, context)
        else:
            await _edit(update, text, keyboard, context=context)
        return

    # ── Paginate dice table entries ─────────────────
    if data.startswith("pick_page:"):
        parts = data.split(":", 2)
        if len(parts) != 3:
            return
        try:
            content_id = int(parts[1])
            page       = int(parts[2])
        except ValueError:
            return
        await _render_content(update, content_id, context, page=page)
        return

    # ── Pick entry from dice table ──────────────────
    if data.startswith("pick:"):
        parts = data.split(":", 2)
        if len(parts) != 3:
            return
        try:
            content_id = int(parts[1])
            idx        = int(parts[2])
        except ValueError:
            return
        content    = db.get_content(content_id, lang)
        if not content or not content.get("dice"):
            await update.callback_query.answer(t(lang, "err_not_found"))
            return
        entries = content["dice"].get("entries", [])
        if not (0 <= idx < len(entries)):
            await update.callback_query.answer(t(lang, "err_not_found"))
            return
        entry      = entries[idx]
        depth      = len(_stack(context))
        text       = fmt.format_roll_result(content, 0, entry, lang, picked=True)
        keyboard   = kb.roll_result_keyboard(content_id, entry.get("links", []), lang, depth)
        image_path = entry.get("image")
        if image_path and os.path.isfile(image_path):
            await _show_image_result(update, text, keyboard, image_path, context)
        else:
            await _edit(update, text, keyboard, context=context)
        return

    # ── Roll all workflow steps ─────────────────────
    if data.startswith("rollall:"):
        try:
            page_id = int(data[8:])
        except ValueError:
            return
        contents = db.get_workflow_contents(page_id, lang)
        if not contents:
            await update.callback_query.answer(t(lang, "err_not_found"))
            return

        rolls = []
        for content in contents:
            dice = content.get("dice")
            if not dice:
                continue
            entries = dice.get("entries", [])
            if not entries:
                continue
            die_name   = dice.get("die", f"d{max(e.get('max', 1) for e in entries)}")
            roll_value = _roll(die_name)
            entry      = next(
                (e for e in entries if e.get("min", 1) <= roll_value <= e.get("max", e.get("min", 1))),
                entries[-1],
            )
            rolls.append({"content": content, "roll_value": roll_value, "entry": entry})

        if not rolls:
            await update.callback_query.answer(t(lang, "err_not_found"))
            return

        page     = db.get_page(page_id, lang)
        depth    = len(_stack(context))
        text     = fmt.format_rollall_result(page, rolls, lang)
        keyboard = kb.rollall_keyboard(page_id, lang, depth)
        await _edit(update, text, keyboard, context=context)
        return

    # ── Back to page (from roll-all result) ────────
    if data.startswith("back_page:"):
        try:
            page_id = int(data[10:])
        except ValueError:
            return
        await _render_page(update, page_id, context)
        return

    # ── noop ────────────────────────────────────────
    if data == "noop":
        return

    logger.warning("Unhandled callback  data=%r", data)
    await update.callback_query.answer(t(lang, "err_not_impl"))


# ─────────────────────────────────────────────
# ERROR HANDLER
# ─────────────────────────────────────────────

async def _cleanup_job(context: ContextTypes.DEFAULT_TYPE) -> None:
    deleted = db.cleanup_user_state(days=90)
    if deleted:
        logger.info("cleanup_user_state removed %d stale rows", deleted)


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

    app.job_queue.run_repeating(_cleanup_job, interval=86400, first=300)

    logger.info("Mothership bot starting…")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
