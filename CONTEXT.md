# Mothership Bot — Project Context for AI Assistants

This file provides a stable, high-level overview of the project for AI coding assistants.
It should be updated whenever significant features are added or the architecture changes.

---

## What This Project Is

A **Telegram inline-keyboard bot** for the Mothership 1e tabletop RPG. It acts as a
table-side digital handbook. Players and Wardens browse rules, equipment, skills, roll tables,
NPCs, and locations — all through Telegram's inline button UI, without leaving the chat.

The bot is read-only from the user's perspective. There is no user-generated content.
All data lives in a SQLite database seeded from JSON files in `seeds/`.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| Telegram | python-telegram-bot 21.6 (PTB v21, async) |
| Database | SQLite via stdlib `sqlite3` |
| Config | `python-dotenv` — `.env` with `BOT_TOKEN`, `DB_PATH`, `DEV_MODE` |
| Deployment | Docker + docker-compose |
| Run (local) | `python -m bot.bot` from project root |

---

## File Map

```
bot/bot.py          Entry point: PTB Application, all handlers, callback router, nav stack
bot/db.py           All database access functions (read-only queries + nav state upsert)
bot/formatters.py   Build HTML message strings for each content type
bot/keyboards.py    Build InlineKeyboardMarkup for each content type
bot/i18n.py         UI string translations (en/ua/ru); t(lang, key) helper with EN fallback
bot/logging_setup.py  Rotating log configuration (bot.log + errors.log)
schema.sql          Authoritative DB schema — all CREATE TABLE and indexes
seed.py             Drops and recreates the DB; loads all JSON seed files in order
seeds/              One JSON file per DB table; source of truth for all content
CONTEXT.md          This file — permanent AI project overview
```

---

## Database Tables (summary)

| Table | Purpose |
|-------|---------|
| `source_books` | 7 books (PSG, WOM, ABH, GD, ST, APF, DP) |
| `categories` | Navigation tree — 56 nodes, self-referencing `parent_id` |
| `terms` | Glossary entries (47 terms), optional JSON aliases array |
| `rules` | Rule text blocks, each linked to a category |
| `roll_tables` | Named dice tables with `dice_notation` and `sort_order` |
| `roll_table_entries` | Rows per table (`roll_min`/`roll_max`, optional `linked_term_id`) |
| `items` | Weapons, armor, gear, trinkets (`item_type` CHECK constraint) |
| `skills` | 42 skills in three tiers (trained/expert/master) |
| `skill_prerequisites` | Junction table: (skill_id, prerequisite_id) — any one prereq suffices |
| `classes` | 4 character classes with JSON stat/save bonuses + starting skills |
| `ships` | Ship catalogue entries |
| `locations` | Module locations, self-referencing `parent_id` for rooms/areas |
| `npcs` | Module NPCs with stat block and JSON `attacks` array |
| `content_term_links` | Many-to-many: any content row ↔ terms |
| `user_nav_state` | Persisted nav stack + language per Telegram user_id (crash-safe) |

### Translation columns

All 11 content tables have `_ua` and `_ru` suffix columns for every translatable field
(e.g. `name_ua`, `name_ru`, `body_ua`, `body_ru`). Currently all empty — bot falls back
to English automatically via `_localize()` in `db.py`. Fill these in seed JSONs to translate.

---

## Navigation Architecture

The bot uses a **navigation stack** stored in `context.user_data` per user and persisted to
`user_nav_state` after every nav change.

```python
context.user_data["nav_stack"]    # list of previous callback_data strings
context.user_data["nav_current"]  # what is currently on screen
context.user_data["nav_loaded"]   # flag: DB load attempted this session
context.user_data["language"]     # active language code ("en"/"ua"/"ru")
```

**Key rules:**
- `_push_page` — saves current to stack, updates current.
- `_pop_page` — returns and removes top of stack (Back button).
- Pagination callbacks (`cat:X:page:N`, `entries:X:page:N`, `glossary:page:N`) update
  `nav_current` in-place **without** pushing to history. Back skips all paging.
- `roll:X` is stored as `table:X` in the nav stack.
- Back from empty stack → clears `nav_current`, shows main menu.
- On any unhandled exception → reset stack, navigate user to main menu, log full traceback.

---

## Callback Data Format

All inline buttons use `type:id` or `type:id:page:N`.

| Prefix | Meaning |
|--------|---------|
| `menu` | Main menu |
| `back` | Pop nav stack |
| `noop` | Display-only, no action |
| `setlang:XX` | Set user language (en/ua/ru) |
| `cat:ID[:page:N]` | Category page |
| `glossary:page:N` | Glossary pagination |
| `rule:ID` | Rule detail |
| `term:ID` | Glossary term |
| `item:ID` | Equipment detail |
| `table:ID` | Roll table detail |
| `roll:ID` | Roll on a table |
| `entries:ID[:page:N]` | Selectable entry list |
| `entry:TABLE_ID:ENTRY_ID` | Single entry detail |
| `cls:ID` | Class detail |
| `skill:ID` | Skill detail |
| `ship:ID` | Ship detail |
| `loc:ID` | Location detail |
| `npc:ID` | NPC detail |

---

## Special Category Slugs

Certain category slugs trigger custom data loaders instead of the default child-listing:

| Slug | Action |
|------|--------|
| `weapons` / `armor` / `gear-tools` | `get_items_by_type(...)` |
| `classes` | `get_all_classes()` |
| `ship-catalogue` / `st-catalogue` | `get_all_ships()` |
| `skills` | `get_all_skills()` |
| `glossary` | Paginated glossary |
| `roll-tables` | `get_all_roll_tables()` |
| `abh/dp/gd/apf-npcs` | `get_npcs_by_book(book_id)` |
| `abh/dp/gd/apf-locations` | `get_locations_by_book(book_id)` |

**Single-item auto-navigation:** if a category has no subcategories and exactly one content
item, `_show_category` skips the list and navigates directly to that item.

---

## Language Support (i18n)

- `bot/i18n.py` — `_STRINGS` dict with `en`, `ua`, `ru` keys; `t(lang, key, **kwargs)` helper
- Fallback chain: translated string → English string → key name
- Language stored in `user_nav_state.language` (default `'en'`)
- `/lang` command shows flag keyboard; `setlang:XX` callback saves and re-renders main menu
- Content translations: `_ua`/`_ru` columns in all seed tables; `db._localize()` applies them
- All translations currently empty — fill seed JSONs and reseed to activate

---

## Dev Mode

Set `DEV_MODE=true` in `.env`. Every rendered message gets a `<code>` block appended showing
the current `nav_current` and full `nav_stack` (top→bottom). Useful for debugging navigation.

---

## Seed Data (current row counts)

| File | Rows |
|------|------|
| source_books.json | 7 |
| categories.json | 56 |
| terms.json | 47 |
| rules.json | 50 |
| roll_tables.json | 22 |
| roll_table_entries.json | 456 |
| items.json | 73 |
| skills.json | 42 |
| skill_prerequisites.json | 43 |
| classes.json | 4 |
| ships.json | 4 |
| locations.json | 34 |
| npcs.json | 17 |
| content_term_links.json | 112 |

---

## Deployment

- **Docker image** seeds the DB at build time (`RUN python seed.py` in Dockerfile).
- The `.env` file is injected at runtime via `env_file` in docker-compose.yml.
- `update.sh` — `docker-compose down` + git pull + `docker-compose up --build` + status check.
  The `down` step is required to avoid a docker-compose 1.29.2 bug (`KeyError: 'ContainerConfig'`).
- Reseeding in production destroys all `user_nav_state` rows (nav history + language prefs).

---

## Git Branches

| Branch | Purpose |
|--------|---------|
| `main` | Production — deployed to server via `update.sh` |
| `feature/i18n` | Multi-language support (EN/UA/RU) — pending merge to main |

---

## Known Gaps (as of 2026-04-08)

- `feature/i18n` not yet merged to `main` — server still runs EN-only
- Translation content (`_ua`/`_ru` seed fields) all empty — falls back to English
- Wound table entries (tables 2–6) have placeholder content — need replacing with PSG data
- Trinket table missing entries at rolls 64, 67, 72, 80, 82–84, 91, 99
- No admin commands (reload DB, usage stats, broadcast)
- `roll_table_entries.extra_data` JSON has no structured display in the bot
