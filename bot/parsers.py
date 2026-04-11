"""
parsers.py — structured parsers for subinfo_fixed string values.

Converts raw stored strings into dicts that formatters use for rich
display and future dice-rolling.  Falls back gracefully on unknown input.
"""

import re
from typing import Any

# ─── Cost ─────────────────────────────────────────────────────────────────────
# Patterns (PSG weapons + armour):
#   "50cr"  "1,400cr"  "10kcr"  "4.5kcr"  "400cr ea."  "Free"

_COST_RE = re.compile(
    r'^(?P<free>Free)$'
    r'|^(?P<num>[\d,]+(?:\.\d+)?)(?P<k>k?)cr(?:\s+(?P<note>.+))?$',
    re.IGNORECASE,
)


def parse_cost(raw: str) -> dict[str, Any]:
    """
    Parse a cost string into a structured dict.

    Return shapes:
        {"type": "free"}
        {"type": "credits", "amount": 1400}
        {"type": "credits", "amount": 400, "note": "ea."}
        {"type": "raw",     "display": <original>}
    """
    m = _COST_RE.match(raw.strip())
    if not m:
        return {"type": "raw", "display": raw}
    if m.group("free"):
        return {"type": "free"}

    num_str = m.group("num").replace(",", "")
    amount = float(num_str) * (1000 if m.group("k") else 1)
    result: dict[str, Any] = {"type": "credits", "amount": int(amount)}
    if m.group("note"):
        result["note"] = m.group("note").strip()
    return result


# ─── Damage ───────────────────────────────────────────────────────────────────
# Patterns (PSG weapons):
#   "—"                            → none
#   "Str/10 DMG"                   → formula
#   "1 DMG"                        → flat
#   "2d10 DMG"                     → dice
#   "1d10+1 DMG"                   → dice + modifier
#   "4d10 DMG (AA)"                → dice + flag
#   "1d10 DMG + 2d10 when removed" → compound

_NONE_RE = re.compile(r'^[—\-]+$')

_FORMULA_RE = re.compile(r'^(?P<formula>\S+/\d+)\s+DMG$', re.IGNORECASE)

# Must be tested BEFORE _STANDARD_RE (both start with dice notation)
_COMPOUND_RE = re.compile(
    r'^(?P<pdice>\d+d\d+)(?P<pmod>[+-]\d+)?\s+DMG'
    r'\s+\+\s+(?P<sdice>\d+d\d+)(?P<smod>[+-]\d+)?(?:\s+(?P<cond>.+))?$',
    re.IGNORECASE,
)

_STANDARD_RE = re.compile(
    r'^(?:(?P<dice>\d+d\d+)|(?P<flat>\d+))'
    r'(?P<mod>[+-]\d+)?\s+DMG'
    r'(?:\s+\((?P<flags>[^)]+)\))?$',
    re.IGNORECASE,
)


def parse_damage(raw: str) -> dict[str, Any]:
    """
    Parse a damage string into a structured dict.

    Return shapes:
        {"type": "none"}
        {"type": "formula",  "formula": "Str/10"}
        {"type": "flat",     "value": 1}
        {"type": "dice",     "dice": "2d10"}
        {"type": "dice",     "dice": "1d10",  "modifier": "+1"}
        {"type": "dice",     "dice": "4d10",  "flags": ["AA"]}
        {"type": "compound", "primary":   {"dice": "1d10"},
                             "secondary": {"dice": "2d10", "condition": "when removed"}}
        {"type": "raw",      "display": <original>}
    """
    s = raw.strip()

    if _NONE_RE.match(s):
        return {"type": "none"}

    m = _FORMULA_RE.match(s)
    if m:
        return {"type": "formula", "formula": m.group("formula")}

    m = _COMPOUND_RE.match(s)
    if m:
        primary: dict[str, Any] = {"dice": m.group("pdice")}
        if m.group("pmod"):
            primary["modifier"] = m.group("pmod")
        secondary: dict[str, Any] = {"dice": m.group("sdice")}
        if m.group("smod"):
            secondary["modifier"] = m.group("smod")
        if m.group("cond"):
            secondary["condition"] = m.group("cond").strip()
        return {"type": "compound", "primary": primary, "secondary": secondary}

    m = _STANDARD_RE.match(s)
    if m:
        if m.group("flat"):
            result: dict[str, Any] = {"type": "flat", "value": int(m.group("flat"))}
        else:
            result = {"type": "dice", "dice": m.group("dice")}
        if m.group("mod"):
            result["modifier"] = m.group("mod")
        if m.group("flags"):
            result["flags"] = [f.strip() for f in m.group("flags").split(",")]
        return result

    return {"type": "raw", "display": raw}
