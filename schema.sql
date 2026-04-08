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
    body            TEXT NOT NULL,
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
    body            TEXT NOT NULL,
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
    description     TEXT,
    dice_notation   TEXT NOT NULL,
    category_id     INTEGER REFERENCES categories(id),
    source_book_id  INTEGER REFERENCES source_books(id),
    page_number     INTEGER
);

CREATE TABLE IF NOT EXISTS roll_table_entries (
    id              INTEGER PRIMARY KEY,
    table_id        INTEGER NOT NULL REFERENCES roll_tables(id) ON DELETE CASCADE,
    roll_min        INTEGER NOT NULL,
    roll_max        INTEGER NOT NULL,
    label           TEXT,
    result_text     TEXT NOT NULL,
    extra_data      TEXT,               -- JSON for multi-column tables
    linked_term_id  INTEGER REFERENCES terms(id)
);

-- ─────────────────────────────────────────────
-- EQUIPMENT  (weapons + armor + gear in one table)
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS items (
    id               INTEGER PRIMARY KEY,
    name             TEXT NOT NULL,
    item_type        TEXT NOT NULL CHECK(item_type IN ('weapon','armor','gear','trinket')),
    cost_cr          INTEGER,
    cost_display     TEXT,
    description      TEXT,
    -- weapon columns
    damage_dice      TEXT,
    damage_modifier  TEXT,
    range_band       TEXT,
    shots            INTEGER,
    wound_type       TEXT,
    wound_modifier   TEXT,
    is_auto_attack   INTEGER DEFAULT 0,
    special_rules    TEXT,
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
    tier            TEXT NOT NULL CHECK(tier IN ('trained','expert','master')),
    bonus           INTEGER NOT NULL,
    description     TEXT,
    prerequisite_id INTEGER REFERENCES skills(id),
    source_book_id  INTEGER REFERENCES source_books(id),
    page_number     INTEGER
);

-- ─────────────────────────────────────────────
-- CLASSES
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS classes (
    id                INTEGER PRIMARY KEY,
    name              TEXT NOT NULL UNIQUE,
    description       TEXT,
    stat_bonuses      TEXT NOT NULL,   -- JSON
    save_bonuses      TEXT NOT NULL,   -- JSON
    special_abilities TEXT,
    trauma_response   TEXT NOT NULL,
    starting_skills   TEXT NOT NULL,   -- JSON
    max_wounds_bonus  INTEGER DEFAULT 0,
    health_dice       TEXT DEFAULT '1d10+10',
    source_book_id    INTEGER REFERENCES source_books(id),
    page_number       INTEGER
);

-- ─────────────────────────────────────────────
-- SHIPS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS ships (
    id               INTEGER PRIMARY KEY,
    name             TEXT NOT NULL,
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
    source_book_id   INTEGER REFERENCES source_books(id),
    page_number      INTEGER
);

-- ─────────────────────────────────────────────
-- LOCATIONS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS locations (
    id              INTEGER PRIMARY KEY,
    name            TEXT NOT NULL,
    location_type   TEXT,   -- planet / station / ship / building / area / room
    description     TEXT,
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
    role            TEXT,   -- BBEG / Ally / Hostile / Neutral / Creature
    description     TEXT,
    combat_stat     INTEGER,
    speed_stat      INTEGER,
    instinct_stat   INTEGER,
    wounds          INTEGER,
    health          INTEGER,
    armor_points    INTEGER,
    attacks         TEXT,   -- JSON array
    special_rules   TEXT,
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
    UNIQUE(content_type, content_id, term_id)
);

-- ─────────────────────────────────────────────
-- INDEXES
-- ─────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_categories_parent      ON categories(parent_id);
CREATE INDEX IF NOT EXISTS idx_rules_category         ON rules(category_id);
CREATE INDEX IF NOT EXISTS idx_items_type             ON items(item_type);
CREATE INDEX IF NOT EXISTS idx_rte_table              ON roll_table_entries(table_id);
CREATE INDEX IF NOT EXISTS idx_roll_tables_category   ON roll_tables(category_id);
CREATE INDEX IF NOT EXISTS idx_skills_prereq          ON skills(prerequisite_id);
CREATE INDEX IF NOT EXISTS idx_locations_parent       ON locations(parent_id);
CREATE INDEX IF NOT EXISTS idx_locations_source_book  ON locations(source_book_id);
CREATE INDEX IF NOT EXISTS idx_npcs_location          ON npcs(location_id);
CREATE INDEX IF NOT EXISTS idx_npcs_source_book       ON npcs(source_book_id);
CREATE INDEX IF NOT EXISTS idx_ctl_content            ON content_term_links(content_type, content_id);
CREATE INDEX IF NOT EXISTS idx_ctl_term               ON content_term_links(term_id);
