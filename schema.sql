PRAGMA foreign_keys = ON;

-- ─────────────────────────────────────────────
-- SOURCE BOOKS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS source_books (
    id          INTEGER PRIMARY KEY,
    short_code  TEXT NOT NULL UNIQUE,
    title       TEXT NOT NULL,
    page_count  INTEGER
);

-- ─────────────────────────────────────────────
-- CATEGORIES  (nav tree)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS categories (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    name_ua     TEXT,
    name_ru     TEXT,
    slug        TEXT NOT NULL UNIQUE,
    parent_id   INTEGER REFERENCES categories(id),
    sort_order  INTEGER DEFAULT 0,
    icon        TEXT
);

-- ─────────────────────────────────────────────
-- GLOSSARY TERMS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS terms (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL UNIQUE,
    name_ua         TEXT,
    name_ru         TEXT,
    body            TEXT NOT NULL,
    body_ua         TEXT,
    body_ru         TEXT,
    source_book_id  INTEGER REFERENCES source_books(id),
    page_number     INTEGER,
    aliases         TEXT    -- JSON array of alternate names / symbols
);

-- ─────────────────────────────────────────────
-- RULES
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS rules (
    id              INTEGER PRIMARY KEY,
    title           TEXT NOT NULL,
    title_ua        TEXT,
    title_ru        TEXT,
    body            TEXT NOT NULL,
    body_ua         TEXT,
    body_ru         TEXT,
    icon            TEXT,
    category_id     INTEGER NOT NULL REFERENCES categories(id),
    source_book_id  INTEGER REFERENCES source_books(id),
    page_number     INTEGER,
    sort_order      INTEGER DEFAULT 0
);

-- ─────────────────────────────────────────────
-- ROLL TABLES
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS roll_tables (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    name_ua         TEXT,
    name_ru         TEXT,
    icon            TEXT,
    description     TEXT,
    description_ua  TEXT,
    description_ru  TEXT,
    dice_notation   TEXT NOT NULL,
    category_id     INTEGER REFERENCES categories(id),
    source_book_id  INTEGER REFERENCES source_books(id),
    page_number     INTEGER,
    sort_order      INTEGER
);

CREATE TABLE IF NOT EXISTS roll_table_entries (
    id              INTEGER PRIMARY KEY,
    table_id        INTEGER NOT NULL REFERENCES roll_tables(id) ON DELETE CASCADE,
    roll_min        INTEGER NOT NULL,
    roll_max        INTEGER NOT NULL,
    label           TEXT,
    result_text     TEXT NOT NULL,
    result_text_ua  TEXT,
    result_text_ru  TEXT,
    extra_data      TEXT,               -- JSON for multi-column tables
    linked_term_id  INTEGER REFERENCES terms(id)
);

-- ─────────────────────────────────────────────
-- EQUIPMENT  (weapons + armor + gear in one table)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS items (
    id               INTEGER PRIMARY KEY,
    name             TEXT NOT NULL,
    name_ua          TEXT,
    name_ru          TEXT,
    item_type        TEXT NOT NULL CHECK(item_type IN ('weapon','armor','gear','trinket')),
    cost_cr          INTEGER,
    cost_display     TEXT,
    description      TEXT,
    description_ua   TEXT,
    description_ru   TEXT,
    -- weapon columns
    damage_dice      TEXT,
    damage_modifier  TEXT,
    range_band       TEXT,
    shots            INTEGER,
    wound_type       TEXT,
    wound_modifier   TEXT,
    is_auto_attack   INTEGER DEFAULT 0,
    special_rules    TEXT,
    special_rules_ua TEXT,
    special_rules_ru TEXT,
    -- armor columns
    armor_points     INTEGER,
    o2_hours         REAL,
    speed_penalty    INTEGER DEFAULT 0,
    damage_reduction INTEGER DEFAULT 0,
    -- source
    source_book_id   INTEGER REFERENCES source_books(id),
    page_number      INTEGER
);

-- ─────────────────────────────────────────────
-- SKILLS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS skills (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL UNIQUE,
    name_ua         TEXT,
    name_ru         TEXT,
    tier            TEXT NOT NULL CHECK(tier IN ('trained','expert','master')),
    bonus           INTEGER NOT NULL,
    description     TEXT,
    description_ua  TEXT,
    description_ru  TEXT,
    source_book_id  INTEGER REFERENCES source_books(id),
    page_number     INTEGER
);

CREATE TABLE IF NOT EXISTS skill_prerequisites (
    skill_id        INTEGER NOT NULL REFERENCES skills(id) ON DELETE CASCADE,
    prerequisite_id INTEGER NOT NULL REFERENCES skills(id) ON DELETE CASCADE,
    PRIMARY KEY (skill_id, prerequisite_id)
);

-- ─────────────────────────────────────────────
-- CLASSES
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS classes (
    id                      INTEGER PRIMARY KEY,
    name                    TEXT NOT NULL UNIQUE,
    name_ua                 TEXT,
    name_ru                 TEXT,
    description             TEXT,
    description_ua          TEXT,
    description_ru          TEXT,
    stat_bonuses            TEXT NOT NULL,   -- JSON
    save_bonuses            TEXT NOT NULL,   -- JSON
    special_abilities       TEXT,
    special_abilities_ua    TEXT,
    special_abilities_ru    TEXT,
    trauma_response         TEXT NOT NULL,
    trauma_response_ua      TEXT,
    trauma_response_ru      TEXT,
    starting_skills         TEXT NOT NULL,   -- JSON
    max_wounds_bonus        INTEGER DEFAULT 0,
    health_dice             TEXT DEFAULT '1d10+10',
    source_book_id          INTEGER REFERENCES source_books(id),
    page_number             INTEGER
);

-- ─────────────────────────────────────────────
-- SHIPS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS ships (
    id               INTEGER PRIMARY KEY,
    name             TEXT NOT NULL,
    name_ua          TEXT,
    name_ru          TEXT,
    class            TEXT,
    ship_type        TEXT,
    manufacturer     TEXT,
    thrusters_stat   INTEGER,
    weapons_stat     INTEGER,
    systems_stat     INTEGER,
    hull_points      INTEGER,
    megadamage_dice  TEXT,
    fuel_capacity    INTEGER,
    crew_capacity    INTEGER,
    cryopod_count    INTEGER,
    escape_pod_count INTEGER,
    hardpoints       INTEGER,
    upgrade_slots    INTEGER,
    description      TEXT,
    description_ua   TEXT,
    description_ru   TEXT,
    source_book_id   INTEGER REFERENCES source_books(id),
    page_number      INTEGER
);

-- ─────────────────────────────────────────────
-- LOCATIONS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS locations (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    name_ua         TEXT,
    name_ru         TEXT,
    location_type   TEXT,   -- planet / station / ship / building / area / room
    description     TEXT,
    description_ua  TEXT,
    description_ru  TEXT,
    parent_id       INTEGER REFERENCES locations(id),
    source_book_id  INTEGER NOT NULL REFERENCES source_books(id),
    page_number     INTEGER
);

-- ─────────────────────────────────────────────
-- NPCs
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS npcs (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    name_ua         TEXT,
    name_ru         TEXT,
    role            TEXT,   -- BBEG / Ally / Hostile / Neutral / Creature
    role_ua         TEXT,
    role_ru         TEXT,
    description     TEXT,
    description_ua  TEXT,
    description_ru  TEXT,
    combat_stat     INTEGER,
    speed_stat      INTEGER,
    instinct_stat   INTEGER,
    wounds          INTEGER,
    health          INTEGER,
    armor_points    INTEGER,
    attacks         TEXT,   -- JSON array
    special_rules   TEXT,
    special_rules_ua TEXT,
    special_rules_ru TEXT,
    location_id     INTEGER REFERENCES locations(id),
    source_book_id  INTEGER NOT NULL REFERENCES source_books(id),
    page_number     INTEGER
);

-- ─────────────────────────────────────────────
-- CROSS-REFERENCE LINKS  (content ↔ terms)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS content_term_links (
    id              INTEGER PRIMARY KEY,
    content_type    TEXT NOT NULL,
    -- rule / item / roll_table / roll_table_entry /
    -- class / skill / ship / npc / location
    content_id      INTEGER NOT NULL,
    term_id         INTEGER NOT NULL REFERENCES terms(id),
    sort_order      INTEGER DEFAULT 0,
    UNIQUE(content_type, content_id, term_id)
);

-- ─────────────────────────────────────────────
-- USER NAV STATE  (persisted nav stack per user)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS user_nav_state (
    user_id     INTEGER PRIMARY KEY,
    nav_current TEXT,
    nav_stack   TEXT NOT NULL DEFAULT '[]',  -- JSON array of callback_data strings
    language    TEXT NOT NULL DEFAULT 'en',  -- user's preferred language
    saved_at    INTEGER NOT NULL DEFAULT 0   -- unix timestamp
);

-- ─────────────────────────────────────────────
-- INDEXES
-- ─────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_categories_parent      ON categories(parent_id);
CREATE INDEX IF NOT EXISTS idx_rules_category         ON rules(category_id);
CREATE INDEX IF NOT EXISTS idx_items_type             ON items(item_type);
CREATE INDEX IF NOT EXISTS idx_rte_table              ON roll_table_entries(table_id);
CREATE INDEX IF NOT EXISTS idx_roll_tables_category   ON roll_tables(category_id);
CREATE INDEX IF NOT EXISTS idx_skill_prereq_skill     ON skill_prerequisites(skill_id);
CREATE INDEX IF NOT EXISTS idx_skill_prereq_prereq    ON skill_prerequisites(prerequisite_id);
CREATE INDEX IF NOT EXISTS idx_locations_parent       ON locations(parent_id);
CREATE INDEX IF NOT EXISTS idx_locations_source_book  ON locations(source_book_id);
CREATE INDEX IF NOT EXISTS idx_npcs_location          ON npcs(location_id);
CREATE INDEX IF NOT EXISTS idx_npcs_source_book       ON npcs(source_book_id);
CREATE INDEX IF NOT EXISTS idx_ctl_content            ON content_term_links(content_type, content_id);
CREATE INDEX IF NOT EXISTS idx_ctl_term               ON content_term_links(term_id);
