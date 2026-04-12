"""
keyboards.py — Inline keyboard builders for the Mothership bot.

Callback data format:
    p:<id>          navigate to page
    c:<id>          navigate to content
    roll:<id>       roll on content's dice table
    pick:<id>:<i>      select entry i from content's dice table
    pick_page:<id>:<p> switch to page p of entry buttons
    back_table:<id>    return to dice table from a roll/pick result
    back               pop nav stack
    home               reset to main page
    setlang:<xx>    set language
    noop            do nothing
"""

import math

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .i18n import t, label


def _btn(text: str, data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text, callback_data=data)


_MAX_PICK_LABEL = 28  # max chars of entry text shown in pick buttons

def _pick_label(entry: dict) -> str:
    lo  = entry.get("min", "?")
    hi  = entry.get("max", lo)
    txt = entry.get("text", "")
    num = str(lo) if lo == hi else f"{lo}–{hi}"
    if txt:
        short = txt[:_MAX_PICK_LABEL] + ("…" if len(txt) > _MAX_PICK_LABEL else "")
        return f"{num} — {short}"
    return num


def _nav_row(lang: str, depth: int) -> list[InlineKeyboardButton]:
    """Back + Home buttons based on stack depth."""
    row = []
    if depth > 1:
        row.append(_btn(t(lang, "btn_back"), "back"))
    if depth > 2:
        row.append(_btn(t(lang, "btn_home"), "home"))
    return row


# ─────────────────────────────────────────────
# PAGE KEYBOARD
# ─────────────────────────────────────────────

def page_keyboard(
    child_pages: list[dict],
    contents: list[dict],
    lang: str,
    depth: int,
) -> InlineKeyboardMarkup:
    """Page screen: child pages + contents + nav."""
    rows: list[list[InlineKeyboardButton]] = []

    for p in child_pages:
        icon = p.get("icon") or ""
        name = p.get("name") or str(p["id"])
        text = f"{icon} {name}".strip() if icon else name
        rows.append([_btn(text, f"p:{p['id']}")])

    for c in contents:
        icon = c.get("icon") or ""
        name = c.get("name") or str(c["id"])
        text = f"{icon} {name}".strip() if icon else name
        rows.append([_btn(text, f"c:{c['id']}")])

    nav = _nav_row(lang, depth)
    if nav:
        rows.append(nav)

    return InlineKeyboardMarkup(rows)


# ─────────────────────────────────────────────
# CONTENT KEYBOARD
# ─────────────────────────────────────────────

_ENTRIES_PER_PAGE = 10


def content_keyboard(
    links: list[dict],
    lang: str,
    depth: int,
    content_id: int | None = None,
    has_dice: bool = False,
    entries: list[dict] | None = None,
    page: int = 0,
) -> InlineKeyboardMarkup:
    """Content card: roll button + pick-entry buttons (paged) + content links + nav."""
    rows: list[list[InlineKeyboardButton]] = []

    if has_dice and content_id is not None:
        rows.append([_btn(t(lang, "btn_roll"), f"roll:{content_id}")])

        all_entries = entries or []
        total       = len(all_entries)
        start       = page * _ENTRIES_PER_PAGE
        end         = min(start + _ENTRIES_PER_PAGE, total)

        for i, entry in enumerate(all_entries[start:end]):
            rows.append([_btn(_pick_label(entry), f"pick:{content_id}:{start + i}")])

        # Pagination row (only shown when table has more than one page)
        if total > _ENTRIES_PER_PAGE:
            total_pages = math.ceil(total / _ENTRIES_PER_PAGE)
            pag: list[InlineKeyboardButton] = []
            if page > 0:
                pag.append(_btn(f"◀ {page}/{total_pages}", f"pick_page:{content_id}:{page - 1}"))
            if end < total:
                pag.append(_btn(f"{page + 2}/{total_pages} ▶", f"pick_page:{content_id}:{page + 1}"))
            if pag:
                rows.append(pag)

    for lk in links:
        icon     = lk.get("icon") or ""
        name     = lk.get("name") or str(lk["id"])
        lbl      = label(lang, lk.get("label_key", "see_also"))
        btn_text = f"{lbl}: {icon} {name}".strip(": ").strip()
        rows.append([_btn(btn_text, f"c:{lk['id']}")])

    nav = _nav_row(lang, depth)
    if nav:
        rows.append(nav)

    return InlineKeyboardMarkup(rows)


# ─────────────────────────────────────────────
# ROLL RESULT KEYBOARD
# ─────────────────────────────────────────────

def roll_result_keyboard(
    content_id: int,
    entry_links: list[dict],
    lang: str,
    depth: int,
) -> InlineKeyboardMarkup:
    """After a dice roll/pick: entry links + back-to-table + home."""
    rows: list[list[InlineKeyboardButton]] = []

    for lk in entry_links:
        link_id = lk.get("id")
        if link_id is None:
            continue
        name = lk.get("label") or str(link_id)
        rows.append([_btn(name, f"c:{link_id}")])

    # Back goes to the table, not the parent page
    nav = [_btn(t(lang, "btn_back"), f"back_table:{content_id}")]
    if depth > 2:
        nav.append(_btn(t(lang, "btn_home"), "home"))
    rows.append(nav)

    return InlineKeyboardMarkup(rows)


# ─────────────────────────────────────────────
# UTILITY KEYBOARDS
# ─────────────────────────────────────────────

def lang_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [_btn("English",    "setlang:en")],
        [_btn("Українська", "setlang:ua")],
        [_btn("Русский",    "setlang:ru")],
    ])


def search_results_keyboard(results: list[dict], lang: str) -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []
    for r in results:
        name = r.get("name") or "?"
        cb   = f"p:{r['entity_id']}" if r["entity_type"] == "page" else f"c:{r['entity_id']}"
        rows.append([_btn(name, cb)])
    if rows:
        rows.append([_btn(t(lang, "btn_home"), "home")])
    return InlineKeyboardMarkup(rows)


def back_only(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[_btn(t(lang, "btn_back"), "back")]])


def home_only(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[_btn(t(lang, "btn_home"), "home")]])
