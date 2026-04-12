PRAGMA foreign_keys = ON;

-- ─────────────────────────────────────────────
-- SOURCES
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS sources (
    id    INTEGER PRIMARY KEY,
    slug  TEXT    UNIQUE NOT NULL,
    title TEXT    NOT NULL,
    type  TEXT    NOT NULL CHECK (type IN ('core', 'module', 'supplement'))
);

-- ─────────────────────────────────────────────
-- PAGES
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS pages (
    id             INTEGER PRIMARY KEY,
    icon           TEXT,
    source_slug    TEXT    REFERENCES sources(slug) ON DELETE SET NULL,
    source_page    INTEGER,
    linked_pages   JSON    NOT NULL DEFAULT '[]',
    workflow_steps JSON,
    image_url      TEXT
);

CREATE TABLE IF NOT EXISTS page_i18n (
    id      INTEGER PRIMARY KEY,
    page_id INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE,
    lang    TEXT    NOT NULL,
    name    TEXT    NOT NULL,
    desc    TEXT,
    UNIQUE (page_id, lang)
);

-- ─────────────────────────────────────────────
-- CONTENTS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS contents (
    id            INTEGER PRIMARY KEY,
    icon          TEXT,
    image_url     TEXT,
    tg_file_id    TEXT,
    subinfo_fixed JSON,
    dice          JSON,
    source_slug   TEXT    REFERENCES sources(slug) ON DELETE SET NULL,
    source_page   INTEGER,
    sort_order    INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS content_i18n (
    id           INTEGER PRIMARY KEY,
    content_id   INTEGER NOT NULL REFERENCES contents(id) ON DELETE CASCADE,
    lang         TEXT    NOT NULL,
    name         TEXT    NOT NULL,
    desc         TEXT,
    subinfo_text JSON,
    dice_entries JSON,
    UNIQUE (content_id, lang)
);

-- ─────────────────────────────────────────────
-- RELATIONS
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS page_contents (
    page_id    INTEGER NOT NULL REFERENCES pages(id)    ON DELETE CASCADE,
    content_id INTEGER NOT NULL REFERENCES contents(id) ON DELETE CASCADE,
    sort_order INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (page_id, content_id)
);

CREATE TABLE IF NOT EXISTS content_links (
    from_content_id INTEGER NOT NULL REFERENCES contents(id) ON DELETE CASCADE,
    to_content_id   INTEGER NOT NULL REFERENCES contents(id) ON DELETE CASCADE,
    label_key       TEXT    NOT NULL DEFAULT 'see_also',
    sort_order      INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (from_content_id, to_content_id)
);

-- ─────────────────────────────────────────────
-- SEARCH (FTS5)
-- ─────────────────────────────────────────────
CREATE VIRTUAL TABLE IF NOT EXISTS search_fts USING fts5 (
    entity_type UNINDEXED,
    entity_id   UNINDEXED,
    lang        UNINDEXED,
    name,
    body,
    tokenize = 'unicode61'
);

-- FTS triggers — page_i18n
CREATE TRIGGER IF NOT EXISTS trg_fts_page_insert
AFTER INSERT ON page_i18n BEGIN
    INSERT INTO search_fts (entity_type, entity_id, lang, name, body)
    VALUES ('page', NEW.page_id, NEW.lang, NEW.name, COALESCE(NEW.desc, ''));
END;

CREATE TRIGGER IF NOT EXISTS trg_fts_page_update
AFTER UPDATE ON page_i18n BEGIN
    DELETE FROM search_fts
    WHERE entity_type = 'page' AND entity_id = OLD.page_id AND lang = OLD.lang;
    INSERT INTO search_fts (entity_type, entity_id, lang, name, body)
    VALUES ('page', NEW.page_id, NEW.lang, NEW.name, COALESCE(NEW.desc, ''));
END;

CREATE TRIGGER IF NOT EXISTS trg_fts_page_delete
AFTER DELETE ON page_i18n BEGIN
    DELETE FROM search_fts
    WHERE entity_type = 'page' AND entity_id = OLD.page_id AND lang = OLD.lang;
END;

-- FTS triggers — content_i18n
CREATE TRIGGER IF NOT EXISTS trg_fts_content_insert
AFTER INSERT ON content_i18n BEGIN
    INSERT INTO search_fts (entity_type, entity_id, lang, name, body)
    VALUES (
        'content', NEW.content_id, NEW.lang, NEW.name,
        COALESCE(NEW.desc, '') || CASE WHEN NEW.subinfo_text IS NOT NULL THEN
            ' ' || COALESCE(
                (SELECT group_concat(json_extract(e.value, '$.value'), ' ')
                 FROM json_each(NEW.subinfo_text) AS e), '')
        ELSE '' END
    );
END;

CREATE TRIGGER IF NOT EXISTS trg_fts_content_update
AFTER UPDATE ON content_i18n BEGIN
    DELETE FROM search_fts
    WHERE entity_type = 'content' AND entity_id = OLD.content_id AND lang = OLD.lang;
    INSERT INTO search_fts (entity_type, entity_id, lang, name, body)
    VALUES (
        'content', NEW.content_id, NEW.lang, NEW.name,
        COALESCE(NEW.desc, '') || CASE WHEN NEW.subinfo_text IS NOT NULL THEN
            ' ' || COALESCE(
                (SELECT group_concat(json_extract(e.value, '$.value'), ' ')
                 FROM json_each(NEW.subinfo_text) AS e), '')
        ELSE '' END
    );
END;

CREATE TRIGGER IF NOT EXISTS trg_fts_content_delete
AFTER DELETE ON content_i18n BEGIN
    DELETE FROM search_fts
    WHERE entity_type = 'content' AND entity_id = OLD.content_id AND lang = OLD.lang;
END;

-- ─────────────────────────────────────────────
-- INDEXES
-- ─────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_page_i18n_lang     ON page_i18n(page_id, lang);
CREATE INDEX IF NOT EXISTS idx_content_i18n_lang  ON content_i18n(content_id, lang);
CREATE INDEX IF NOT EXISTS idx_page_contents_page ON page_contents(page_id, sort_order);
CREATE INDEX IF NOT EXISTS idx_page_contents_cont ON page_contents(content_id);
CREATE INDEX IF NOT EXISTS idx_content_links_from ON content_links(from_content_id, sort_order);
CREATE INDEX IF NOT EXISTS idx_contents_source    ON contents(source_slug);
CREATE INDEX IF NOT EXISTS idx_pages_source       ON pages(source_slug);

-- ─────────────────────────────────────────────
-- USER STATE
-- ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS user_state (
    user_id     INTEGER PRIMARY KEY,
    lang        TEXT    NOT NULL DEFAULT 'en',
    nav_stack   JSON    NOT NULL DEFAULT '[]',
    last_msg_id INTEGER,
    last_query  TEXT,
    msg_ids     JSON    NOT NULL DEFAULT '[]',
    updated_at  INTEGER NOT NULL DEFAULT (strftime('%s', 'now'))
);
