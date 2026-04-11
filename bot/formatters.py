"""
formatters.py — HTML message builders for pages and content cards.
All output uses HTML parse mode.
"""

import html

from .i18n import t, label, value_t
from .parsers import parse_damage


def _esc(text: str | None) -> str:
    return html.escape(str(text)) if text else ""


def _fmt_damage(raw: str, lang: str) -> str:
    """Render a damage string as HTML using the structured parser."""
    parsed = parse_damage(raw)
    kind = parsed["type"]

    if kind == "none":
        return "—"

    if kind == "formula":
        # Translate the full string (e.g. "Str/10 DMG" → "Сил/10 шкоди"),
        # then take only the formula token for the code block.
        translated = value_t(lang, "damage", raw)
        formula = translated.split()[0]
        return f"🎲 <code>{_esc(formula)}</code>"

    dmg = t(lang, "dmg")

    if kind == "flat":
        return f"🎲 <code>{parsed['value']}</code> {dmg}"

    if kind == "dice":
        notation = parsed["dice"] + parsed.get("modifier", "")
        result = f"🎲 <code>{_esc(notation)}</code> {dmg}"
        if "flags" in parsed:
            result += " " + " ".join(f"({_esc(f)})" for f in parsed["flags"])
        return result

    if kind == "compound":
        p = parsed["primary"]
        s = parsed["secondary"]
        pnotation = p["dice"] + p.get("modifier", "")
        snotation = s["dice"] + s.get("modifier", "")
        result = f"🎲 <code>{_esc(pnotation)}</code> {dmg}"
        result += f" + <code>{_esc(snotation)}</code>"
        if "condition" in s:
            cond = value_t(lang, "damage_condition", s["condition"])
            result += f" {_esc(cond)}"
        return result

    # fallback for "raw" type
    return f"🎲 <code>{_esc(value_t(lang, 'damage', raw))}</code>"


# ─────────────────────────────────────────────
# PAGE
# ─────────────────────────────────────────────

def format_page(page: dict, lang: str) -> str:
    """Header text for a page screen."""
    icon = page.get("icon") or ""
    name = _esc(page.get("name") or "")
    desc = page.get("desc") or ""

    title = f"{icon} <b>{name}</b>".strip() if icon else f"<b>{name}</b>"
    return f"{title}\n\n{_esc(desc)}" if desc else title


# ─────────────────────────────────────────────
# CONTENT CARD
# ─────────────────────────────────────────────

def format_content(content: dict, lang: str) -> str:
    """Full HTML text for a content card (no dice table)."""
    parts: list[str] = []

    # Title
    icon = content.get("icon") or ""
    name = _esc(content.get("name") or "")
    title = f"{icon} <b>{name}</b>".strip() if icon else f"<b>{name}</b>"
    parts.append(title)

    # Description
    desc = content.get("desc") or ""
    if desc:
        parts.append(_esc(desc))

    # subinfo_fixed — stats/dice/cost/mass (never translated)
    fixed: list[dict] = content.get("subinfo_fixed") or []
    if fixed:
        lines = []
        for entry in fixed:
            key   = entry.get("label_key", "")
            value = entry.get("value", "")
            kind  = entry.get("type", "stat")
            lbl   = label(lang, key)
            if kind == "roll" and key == "damage":
                lines.append(f"<b>{_esc(lbl)}:</b> {_fmt_damage(value, lang)}")
            elif kind == "roll":
                val = value_t(lang, key, value)
                lines.append(f"<b>{_esc(lbl)}:</b> 🎲 <code>{_esc(val)}</code>")
            elif kind == "cost":
                val = value_t(lang, key, value)
                lines.append(f"<b>{_esc(lbl)}:</b> 💰 {_esc(val)}")
            elif kind == "mass":
                val = value_t(lang, key, value)
                lines.append(f"<b>{_esc(lbl)}:</b> ⚖️ {_esc(val)}")
            else:
                val = value_t(lang, key, value)
                lines.append(f"<b>{_esc(lbl)}:</b> {_esc(val)}")
        parts.append("\n".join(lines))

    # subinfo_text — translated free-text fields
    text_fields: list[dict] = content.get("subinfo_text") or []
    if text_fields:
        lines = []
        for entry in text_fields:
            key   = entry.get("label_key", "")
            value = entry.get("value", "")
            lbl   = label(lang, key)
            lines.append(f"<b>{_esc(lbl)}:</b> {_esc(value)}")
        parts.append("\n".join(lines))

    # Source attribution
    source_slug = content.get("source_slug")
    source_page = content.get("source_page")
    if source_slug:
        ref = f"[{_esc(source_slug.upper())}"
        if source_page:
            ref += f" p.{source_page}"
        ref += "]"
        parts.append(f"<i>{ref}</i>")

    return "\n\n".join(p for p in parts if p)


def format_dice_table(content: dict, lang: str) -> str:
    """Content card with dice table entries appended."""
    base = format_content(content, lang)
    dice = content.get("dice")
    if not dice:
        return base

    die     = dice.get("die", "d?")
    entries = dice.get("entries", [])
    lines   = [f"\n<b>{_esc(die.upper())} {t(lang, 'dice_table')}</b>"]
    for e in entries:
        lo  = e.get("min", "?")
        hi  = e.get("max", lo)
        txt = _esc(e.get("text", ""))
        if lo == hi:
            lines.append(f"  <code>{lo}</code>  {txt}")
        else:
            lines.append(f"  <code>{lo}–{hi}</code>  {txt}")

    return base + "\n" + "\n".join(lines)


# ─────────────────────────────────────────────
# ROLL RESULT
# ─────────────────────────────────────────────

def format_roll_result(content: dict, roll_value: int, entry: dict, lang: str, picked: bool = False) -> str:
    """Single roll result card."""
    name = _esc(content.get("name") or "")
    dice = content.get("dice") or {}
    die  = _esc(dice.get("die", "d?"))
    text = _esc(entry.get("text", ""))

    if picked:
        lo         = entry.get("min", roll_value)
        hi         = entry.get("max", lo)
        range_str  = _esc(str(lo) if lo == hi else f"{lo}–{hi}")
        header     = t(lang, "pick_on", range=range_str, name=name)
    else:
        header = t(lang, "roll_on", value=roll_value, name=name)
    body   = t(lang, "roll_result_entry", result=text)

    links = entry.get("links", [])
    link_line = ""
    if links:
        names     = [_esc(lk.get("label", "")) for lk in links]
        link_line = "\n" + " · ".join(f"<i>{n}</i>" for n in names if n)

    return f"🎲 <b>{die.upper()}</b>  {header}\n\n{body}{link_line}"


# ─────────────────────────────────────────────
# SEARCH
# ─────────────────────────────────────────────

def format_search_results(query: str, results: list[dict], lang: str) -> str:
    if not results:
        return t(lang, "search_no_results", query=_esc(query))
    return t(lang, "search_results", query=_esc(query))
