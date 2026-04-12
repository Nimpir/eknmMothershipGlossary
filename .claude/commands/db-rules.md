# Mothership Bot — DB Content Rules

These rules apply whenever you add, modify, or delete database content in this project.

---

## Rule 0 — Show mapping before inserting

Before inserting any data sourced from a book or external content, present a mapping table that shows how each piece of source material maps to a database column. Include one sample row so the user can verify the interpretation is correct before any SQL runs.

Format:

```
Source field        → Table.column          Sample value
------------------    ----------------------  ---------------------------
Item name           → contents.slug          "combat_knife"
Display name (EN)   → content_i18n.name      "Combat Knife"
Body text           → content_i18n.body      "A short blade for close..."
Dice table entry    → roll_table_entries.*   d10 result 1 → "Slash wound"
Parent category     → page_contents.page_id  P12 (Weapons)
```

**Wait for explicit user approval** of the mapping before writing any INSERT statements.

---

## Rule 1 — Always fill all supported languages

`bot/i18n.py` defines `SUPPORTED_LANGS = ("en", "ru", "ua")`.

Every `page_i18n` and `content_i18n` row you write **must include one entry per language**.
- Write the real translation when you have it.
- When a translation is missing, copy the English text as a placeholder — never omit a language row entirely.
- The same rule applies to `seed.py` / any SQL scripts you write for seeding.

```sql
-- Good: all three languages present
INSERT INTO page_i18n (page_id, lang, name) VALUES (1, 'en', 'Weapons');
INSERT INTO page_i18n (page_id, lang, name) VALUES (1, 'ru', 'Оружие');
INSERT INTO page_i18n (page_id, lang, name) VALUES (1, 'ua', 'Зброя');

-- Bad: only English row added
INSERT INTO page_i18n (page_id, lang, name) VALUES (1, 'en', 'Weapons');
```

---

## Rule 2 — Propose content links before applying them

`content_links` records semantic connections between content items (e.g. "Weapons → Ammo Types").
`data.md` is the living index of every page and content item with their IDs.

Before executing any INSERT/UPDATE that adds new pages or contents:

1. Read `_docs/data.md` to see all existing pages (`P<id>`) and contents (`C<id>`).
2. Identify potential `content_links` rows between the new items and existing ones (e.g. shared topic, "see also" relationships, prerequisites).
3. Present the proposed links to the user in this format:

   ```
   Proposed content links:
   - C<from_id> (<name>) → C<to_id> (<name>)  [label: see_also]
   - C<from_id> (<name>) → C<to_id> (<name>)  [label: related]
   ```

4. **Wait for explicit user approval** before inserting those `content_links` rows.
5. Never silently add links — only apply what the user approves.

---

## Rule 3 — Keep data.md in sync

`_docs/data.md` is the authoritative human-readable index of the database.
Its format is defined in the file header. After **every** DB change:

### After adding a page
Append to the **Pages** section:

```
P<id> <Name> → [P<child1>, P<child2>] | C<content1>, C<content2>
```

- `→ [...]` lists `linked_pages` (child page buttons) in order.
- `| ...` lists `page_contents` entries in `sort_order` order.
- Omit the `→ [...]` part if `linked_pages` is empty.
- Omit the `| ...` part if there are no `page_contents` rows.

### After adding a content item
Append to the **Contents** section:

```
C<id> <Name>  [🎲 if it has a dice table]
```

### After adding a content link
Append to the **Content Links** section:

```
C<from_id> → C<to_id> (<label_key>)
```

### After modifying or deleting
- **Modified:** update the relevant line in-place.
- **Deleted:** mark the line with `(deleted)` — never reuse the ID.
- **Linked pages / page contents changed:** update the `→ [...]` / `| ...` parts of the affected page line.

### Never leave data.md out of sync
If you write SQL or seed code that changes the DB, update `data.md` in the same response.
If data.md currently says `*(empty)*` for a section, replace that line with the first real entry.

---

## Rule 4 — No duplicate icons on the same page

Every page's direct children (both sub-pages in `linked_pages` and content items in `page_contents`) must use distinct icons.

Before assigning an icon to a new page or content item:

1. Check `data.md` for all items already listed on the target parent page.
2. Verify the chosen icon is not already used by a sibling on that page.
3. If a conflict exists, pick a different icon and note the change in your response.

This applies to:
- Sub-pages listed in a parent's `linked_pages` — each must have a unique icon.
- Content items listed in a page's `page_contents` — each must have a unique icon.

> **Note:** Weapons on P2 are exempt — many share 🔫 because the icon represents weapon *type* (firearm, melee, etc.), not a unique identity. Apply the rule to navigational pages and content sections where the icon is the primary visual differentiator.

---

## Rule 5 — Every DB change gets a migration script

Any session that adds, modifies, or deletes rows must produce a standalone Python migration script in `scripts/`.

### Naming

```
scripts/add_<topic>.py        # new pages / contents
scripts/update_<topic>.py     # modifying existing rows
scripts/delete_<topic>.py     # removing rows
```

### Script requirements

- **Idempotent** — use `INSERT OR IGNORE`, `ON CONFLICT DO UPDATE`, or existence checks so re-running causes no harm.
- **Self-contained** — reads `DB_PATH` from env (with `"mothership.db"` as default), loads `.env` via `dotenv`.
- **All three languages** — satisfies Rule 1; never writes a row for fewer than all supported langs.
- **Prints a summary** on success, e.g. `Done — 3 pages, 12 contents added.`

### Minimal template

```python
"""
scripts/add_example.py
One-line description of what this script adds / changes.
Run: python scripts/add_example.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — ...")
    finally:
        conn.close()

def _seed(conn: sqlite3.Connection) -> None:
    pass  # INSERT OR IGNORE / UPDATE statements here

if __name__ == "__main__":
    run()
```

### After writing the script

1. Apply the changes to the live DB by running the script locally.
2. Regenerate `data.sql` so the Docker image stays in sync:

```python
# Run this after any migration script:
python scripts/regenerate_data_sql.py
```

3. Update `data.md` (Rule 3) in the same response.

> `data.sql` is the Docker seed — it must always reflect the current live DB state.
> Never manually edit `data.sql`; always regenerate it via `regenerate_data_sql.py`.
