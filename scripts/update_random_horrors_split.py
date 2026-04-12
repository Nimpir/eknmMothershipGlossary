"""
scripts/update_random_horrors_split.py
Split the old C179 "Random Horrors" 5-column d100 table into 5 separate
d100 tables (C310–C314) and a dedicated sub-page P51 "Generate Horror".

Changes applied:
- C179 deleted (was a combined header/table).
- C310 Transgressions ⚡, C311 Omens 🔮, C312 Manifestations 👾,
  C313 Banishments 🛡️, C314 Slumber 💤 inserted as standalone dice tables.
- P51 😱 "Generate Horror" created with workflow_steps=[310..314]
  and page_contents C310–C314.
- P25 linked_pages updated to [51]; P25 workflow_steps cleared.
- P25 sort order: C180=1, C181=2, C182=3.
- C206 (Random Lore) related link redirected from C179 → C181.

Run: python scripts/update_random_horrors_split.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

PAGE_ID     = 25
NEW_PAGE_ID = 51

# (col_idx, new_id, icon, name_en, name_ru, name_ua, desc_en, desc_ru, desc_ua)
COLS = [
    (
        0, 310, "⚡",
        "Transgressions", "Проступки", "Проступки",
        "What awakens the Horror",
        "Что пробуждает Ужас",
        "Що пробуджує Жах",
    ),
    (
        1, 311, "🔮",
        "Omens", "Знамения", "Знамення",
        "Signs of the Horror's arrival",
        "Признаки прихода Ужаса",
        "Ознаки приходу Жаху",
    ),
    (
        2, 312, "👾",
        "Manifestations", "Проявления", "Прояви",
        "The Horror's form",
        "Форма Ужаса",
        "Форма Жаху",
    ),
    (
        3, 313, "🛡️",
        "Banishments", "Изгнание", "Вигнання",
        "How to defeat the Horror",
        "Как победить Ужас",
        "Як перемогти Жах",
    ),
    (
        4, 314, "💤",
        "Slumber", "Дремота", "Сон",
        "What the Horror does if not defeated",
        "Что делает Ужас, если его не победить",
        "Що робить Жах, якщо його не перемогти",
    ),
]


def _parse_col_en(entries, col_idx):
    result = []
    for e in entries:
        parts = e["text"].split(" | ")
        text = parts[col_idx]
        text = text[text.index(": ") + 2:]
        result.append({"min": e["min"], "max": e["max"], "text": text})
    return result


def _parse_col_i18n(entries_list, col_idx):
    result = []
    for entry in entries_list:
        parts = entry.split(" | ")
        text = parts[col_idx]
        text = text[text.index(": ") + 2:]
        result.append(text)
    return result


def _seed(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()

    # ── Read C179 dice data if it still exists (first run only) ─────────────
    cur.execute("SELECT dice FROM contents WHERE id=179")
    row = cur.fetchone()
    raw_dice = row[0] if row else None
    en_entries = json.loads(raw_dice)["entries"] if raw_dice else None

    cur.execute(
        "SELECT lang, dice_entries FROM content_i18n WHERE content_id=179 AND lang IN ('ru','ua')"
    )
    i18n_map = {lang: json.loads(de) for lang, de in cur.fetchall() if de}

    # ── Redirect C206→C179 to C206→C181 before deleting C179 ────────────────
    conn.execute(
        "INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key)"
        " VALUES (206, 181, 'related')"
    )

    # ── Delete C179 (CASCADE removes content_i18n, page_contents, links) ────
    conn.execute("DELETE FROM contents WHERE id=179")

    # ── Insert 5 dice tables ─────────────────────────────────────────────────
    for col_idx, cid, icon, name_en, name_ru, name_ua, desc_en, desc_ru, desc_ua in COLS:
        if en_entries:
            en_col = _parse_col_en(en_entries, col_idx)
            dice_json = json.dumps({"die": "d100", "entries": en_col}, ensure_ascii=False)
        else:
            cur.execute("SELECT dice FROM contents WHERE id=?", (cid,))
            r = cur.fetchone()
            dice_json = r[0] if r else None

        conn.execute(
            "INSERT OR IGNORE INTO contents (id, icon, source_slug, source_page, dice, sort_order)"
            " VALUES (?, ?, 'wom', 2, ?, ?)",
            (cid, icon, dice_json, col_idx + 2),
        )
        conn.execute("UPDATE contents SET dice=?, sort_order=? WHERE id=?", (dice_json, col_idx + 2, cid))

        for lang, name, desc in [
            ("en", name_en, desc_en),
            ("ru", name_ru, desc_ru),
            ("ua", name_ua, desc_ua),
        ]:
            de = None
            if lang != "en" and i18n_map.get(lang):
                de = json.dumps(_parse_col_i18n(i18n_map[lang], col_idx), ensure_ascii=False)
            conn.execute(
                "INSERT OR IGNORE INTO content_i18n (content_id, lang, name, desc, dice_entries)"
                " VALUES (?, ?, ?, ?, ?)",
                (cid, lang, name, desc, de),
            )

    # ── Create P51 "Generate Horror" ─────────────────────────────────────────
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages, workflow_steps)
        VALUES (51, '😱', 'wom', 2, '[]', ?)
    """, (json.dumps([310, 311, 312, 313, 314]),))
    conn.execute(
        "UPDATE pages SET workflow_steps=? WHERE id=51",
        (json.dumps([310, 311, 312, 313, 314]),),
    )
    for lang, name, desc in [
        ("en", "Generate Horror",
         "Roll each column separately or use Roll All for a complete Horror."),
        ("ru", "Сгенерировать Ужас",
         "Бросайте каждый столбец отдельно или используйте «Бросить всё» для полного Ужаса."),
        ("ua", "Згенерувати Жах",
         "Кидайте кожен стовпець окремо або використовуйте «Кинути все» для повного Жаху."),
    ]:
        conn.execute(
            "INSERT OR IGNORE INTO page_i18n (page_id, lang, name, desc) VALUES (51, ?, ?, ?)",
            (lang, name, desc),
        )

    # ── P51 page_contents: C310–C314 ─────────────────────────────────────────
    for cid, sord in [(310, 1), (311, 2), (312, 3), (313, 4), (314, 5)]:
        conn.execute("""
            INSERT INTO page_contents (page_id, content_id, sort_order)
            VALUES (51, ?, ?)
            ON CONFLICT(page_id, content_id) DO UPDATE SET sort_order = excluded.sort_order
        """, (cid, sord))

    # ── P25: link to P51, clear workflow, fix sort order ────────────────────
    conn.execute(
        "UPDATE pages SET linked_pages=?, workflow_steps=NULL WHERE id=?",
        (json.dumps([NEW_PAGE_ID]), PAGE_ID),
    )
    for cid, sord in [(180, 1), (181, 2), (182, 3)]:
        conn.execute(
            "UPDATE page_contents SET sort_order=? WHERE page_id=? AND content_id=?",
            (sord, PAGE_ID, cid),
        )
    # Remove sub-tables from P25 if a previous run added them
    conn.execute(
        "DELETE FROM page_contents WHERE page_id=? AND content_id IN (310,311,312,313,314)",
        (PAGE_ID,),
    )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done -- C179 removed; P51 created; C310-C314 on P51 with Roll All; P25 -> P51.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
