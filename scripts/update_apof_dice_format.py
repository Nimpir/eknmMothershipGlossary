"""
scripts/update_apof_dice_format.py
Fix APoF dice JSON format: replace {"sides": N} with the correct
{"die": "dN", "entries": [{"min": ..., "max": ..., "text": ...}]} structure.

Also reworks C296 (Encounter Frequency) from plain-text desc into a proper
d10 range dice table.

Affected content IDs:
  d10  (0-indexed): C246, C252, C253, C304, C305, C306
  d20  (1-indexed): C297
  d30  (range):     C256
  d100 (range):     C255, C298, C299
  special range:    C296 (Encounter Frequency matrix)

Note: C300 (Denizens) was fixed by this script then deleted by
update_apof_denizens_split.py — do not add it back to this list.

Run after: all add_apof_*.py scripts have been executed.
Run BEFORE: update_apof_denizens_split.py (which deletes C300).
Run: python scripts/update_apof_dice_format.py
"""
import json
import os
import re
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── Range parser ─────────────────────────────────────────────────────────────

def _parse_range(text: str):
    """Extract (min, max) from a leading 'NN-MM:' or 'NN:' prefix.
    Returns (-1, -1) for entries without a numeric prefix (e.g. meta rules).
    """
    m = re.match(r"^(\d+)(?:-(\d+))?:", text)
    if m:
        lo = int(m.group(1))
        hi = int(m.group(2)) if m.group(2) else lo
        return lo, hi
    return -1, -1


# ── Entry builders ────────────────────────────────────────────────────────────

def _d10_entries(texts):
    """d10 — decade die, 10 entries indexed 0-9."""
    return [{"min": i, "max": i, "text": texts[i]} for i in range(len(texts))]


def _d20_entries(texts):
    """d20 — 20 entries indexed 1-20."""
    return [{"min": i + 1, "max": i + 1, "text": texts[i]} for i in range(len(texts))]


def _range_entries(texts):
    """Range die (d30/d100) — parse min/max from text prefix."""
    result = []
    for t in texts:
        lo, hi = _parse_range(t)
        result.append({"min": lo, "max": hi, "text": t})
    return result


# ── Fetchers ──────────────────────────────────────────────────────────────────

def _get_en_dice_entries(conn, cid):
    row = conn.execute(
        "SELECT dice_entries FROM content_i18n WHERE content_id=? AND lang='en'", (cid,)
    ).fetchone()
    if row and row[0]:
        return json.loads(row[0])
    return []


# ── Updaters ──────────────────────────────────────────────────────────────────

def _update_dice(conn, cid, die_str, entries):
    dice_json = json.dumps({"die": die_str, "entries": entries}, ensure_ascii=False)
    conn.execute("UPDATE contents SET dice=? WHERE id=?", (dice_json, cid))


# ── Per-type fix functions ─────────────────────────────────────────────────────

def _fix_d10(conn, cid):
    texts = _get_en_dice_entries(conn, cid)
    assert len(texts) == 10, f"C{cid}: expected 10 d10 entries, got {len(texts)}"
    _update_dice(conn, cid, "d10", _d10_entries(texts))


def _fix_d20(conn, cid):
    texts = _get_en_dice_entries(conn, cid)
    assert len(texts) == 20, f"C{cid}: expected 20 d20 entries, got {len(texts)}"
    _update_dice(conn, cid, "d20", _d20_entries(texts))


def _fix_range(conn, cid, die_str):
    texts = _get_en_dice_entries(conn, cid)
    assert texts, f"C{cid}: no dice_entries found"
    _update_dice(conn, cid, die_str, _range_entries(texts))


# ── C296 Encounter Frequency — special matrix table ───────────────────────────

# Preamble text (replaces the old wall-of-text desc)
_C296_DESC = {
    "en": (
        "Roll 1d10 per map slice traversal. Check by Phase (1 / 2 / 3).\n\n"
        "If violence breaks out: 10% chance Tempest Operators "
        "[H:2 C:35 Pulse Rifle 5d10dmg I:25] arrive in 1d10 rounds. "
        "Otherwise no help is coming.\n\n"
        "If a Deadly Encounter doesn't fit Phase Events completed, "
        "move down the list until you find one that matches."
    ),
    "ru": (
        "Бросайте 1d10 при каждом переходе через участок карты. "
        "Проверяйте по Фазе (1 / 2 / 3).\n\n"
        "При вспышке насилия: 10% шанс прибытия Операторов Tempest "
        "[H:2 C:35 Пульсовая винтовка 5d10 I:25] через 1d10 раундов. "
        "Иначе помощи не будет.\n\n"
        "Если Смертельная встреча не подходит по выполненным Событиям Фазы — "
        "спускайтесь по списку ниже."
    ),
    "ua": (
        "Кидайте 1d10 при кожному переході через ділянку карти. "
        "Перевіряйте за Фазою (1 / 2 / 3).\n\n"
        "При спалаху насильства: 10% шанс прибуття Операторів Tempest "
        "[H:2 C:35 Імпульсна гвинтівка 5d10 I:25] через 1d10 раундів. "
        "Інакше допомоги не буде.\n\n"
        "Якщо Смертельна зустріч не відповідає виконаним Подіям Фази — "
        "спускайтесь по списку нижче."
    ),
}

# 7-entry range table per language
_C296_ENTRIES = {
    "en": [
        {"min": 1,  "max": 2,  "text": "1–2  |  No Enc  |  No Enc  |  No Enc"},
        {"min": 3,  "max": 3,  "text": "3    |  No Enc  |  No Enc  |  Station Enc"},
        {"min": 4,  "max": 4,  "text": "4    |  No Enc  |  Station Enc  |  Station Enc"},
        {"min": 5,  "max": 6,  "text": "5–6  |  Station Enc  |  Station Enc  |  Deadly Enc"},
        {"min": 7,  "max": 7,  "text": "7    |  Station Enc  |  Deadly Enc  |  Deadly Enc"},
        {"min": 8,  "max": 9,  "text": "8–9  |  Station Enc  |  Deadly Enc  |  Deadly Enc"},
        {"min": 10, "max": 10, "text": "10   |  Deadly Enc  |  Deadly Enc  |  Deadly Enc"},
    ],
    "ru": [
        {"min": 1,  "max": 2,  "text": "1–2  |  Нет  |  Нет  |  Нет"},
        {"min": 3,  "max": 3,  "text": "3    |  Нет  |  Нет  |  Станция"},
        {"min": 4,  "max": 4,  "text": "4    |  Нет  |  Станция  |  Станция"},
        {"min": 5,  "max": 6,  "text": "5–6  |  Станция  |  Станция  |  Смертельная"},
        {"min": 7,  "max": 7,  "text": "7    |  Станция  |  Смертельная  |  Смертельная"},
        {"min": 8,  "max": 9,  "text": "8–9  |  Станция  |  Смертельная  |  Смертельная"},
        {"min": 10, "max": 10, "text": "10   |  Смертельная  |  Смертельная  |  Смертельная"},
    ],
    "ua": [
        {"min": 1,  "max": 2,  "text": "1–2  |  Немає  |  Немає  |  Немає"},
        {"min": 3,  "max": 3,  "text": "3    |  Немає  |  Немає  |  Станція"},
        {"min": 4,  "max": 4,  "text": "4    |  Немає  |  Станція  |  Станція"},
        {"min": 5,  "max": 6,  "text": "5–6  |  Станція  |  Станція  |  Смертельна"},
        {"min": 7,  "max": 7,  "text": "7    |  Станція  |  Смертельна  |  Смертельна"},
        {"min": 8,  "max": 9,  "text": "8–9  |  Станція  |  Смертельна  |  Смертельна"},
        {"min": 10, "max": 10, "text": "10   |  Смертельна  |  Смертельна  |  Смертельна"},
    ],
}


def _fix_c296(conn):
    cid = 296
    # Set proper dice on contents
    dice_json = json.dumps(
        {"die": "d10", "entries": _C296_ENTRIES["en"]}, ensure_ascii=False
    )
    conn.execute("UPDATE contents SET dice=? WHERE id=?", (dice_json, cid))

    # Update desc + dice_entries for all langs
    for lang in ("en", "ru", "ua"):
        entries_json = json.dumps(
            [e["text"] for e in _C296_ENTRIES[lang]], ensure_ascii=False
        )
        conn.execute(
            "UPDATE content_i18n SET desc=?, dice_entries=? WHERE content_id=? AND lang=?",
            (_C296_DESC[lang], entries_json, cid, lang),
        )


# ── Main ─────────────────────────────────────────────────────────────────────

def _seed(conn):
    # d10 simple tables (decade die, 0-indexed entries)
    for cid in [246, 252, 253, 304, 305, 306]:
        _fix_d10(conn, cid)

    # d20 table (1-indexed entries)
    _fix_d20(conn, 297)

    # d30 range table
    _fix_range(conn, 256, "d30")

    # d100 range tables (C300 was fixed here then deleted by update_apof_denizens_split.py)
    for cid in [255, 298, 299]:
        _fix_range(conn, cid, "d100")

    # C296 special matrix
    _fix_c296(conn)


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(
            "Done — fixed dice format for C246, C252, C253, C255, C256, "
            "C296, C297, C298, C299, C304, C305, C306 "
            "(12 content items updated)."
        )
    except Exception as e:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    run()
