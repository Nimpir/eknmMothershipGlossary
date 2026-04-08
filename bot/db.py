"""
db.py — All database query functions for the Mothership bot.
"""

import json
import os
import sqlite3
from typing import Any

DB_PATH = os.getenv("DB_PATH", "mothership.db")


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _row(row: sqlite3.Row | None) -> dict | None:
    return dict(row) if row else None


def _rows(rows: list[sqlite3.Row]) -> list[dict]:
    return [dict(r) for r in rows]


# ─────────────────────────────────────────────
# CATEGORIES
# ─────────────────────────────────────────────

def get_top_level_categories() -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            "SELECT * FROM categories WHERE parent_id IS NULL ORDER BY sort_order, name"
        ).fetchall())


def get_subcategories(parent_id: int) -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            "SELECT * FROM categories WHERE parent_id = ? ORDER BY sort_order, name",
            (parent_id,)
        ).fetchall())


def get_category(cat_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            "SELECT * FROM categories WHERE id = ?", (cat_id,)
        ).fetchone())


def get_category_breadcrumb(cat_id: int) -> list[dict]:
    """Returns list from root → given category."""
    breadcrumb = []
    with _conn() as conn:
        current = cat_id
        while current:
            row = conn.execute(
                "SELECT * FROM categories WHERE id = ?", (current,)
            ).fetchone()
            if not row:
                break
            breadcrumb.insert(0, dict(row))
            current = row["parent_id"]
    return breadcrumb


def category_has_children(cat_id: int) -> bool:
    with _conn() as conn:
        row = conn.execute(
            "SELECT COUNT(*) FROM categories WHERE parent_id = ?", (cat_id,)
        ).fetchone()
        return row[0] > 0


# ─────────────────────────────────────────────
# RULES
# ─────────────────────────────────────────────

def get_rules_by_category(cat_id: int) -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            """SELECT r.*, s.short_code AS book_code
               FROM rules r
               LEFT JOIN source_books s ON s.id = r.source_book_id
               WHERE r.category_id = ?
               ORDER BY r.sort_order, r.title""",
            (cat_id,)
        ).fetchall())


def get_rule(rule_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            """SELECT r.*, s.short_code AS book_code
               FROM rules r
               LEFT JOIN source_books s ON s.id = r.source_book_id
               WHERE r.id = ?""",
            (rule_id,)
        ).fetchone())


# ─────────────────────────────────────────────
# TERMS (GLOSSARY)
# ─────────────────────────────────────────────

def get_all_terms() -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            """SELECT t.*, s.short_code AS book_code
               FROM terms t
               LEFT JOIN source_books s ON s.id = t.source_book_id
               ORDER BY t.name""",
        ).fetchall())


def get_term(term_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            """SELECT t.*, s.short_code AS book_code
               FROM terms t
               LEFT JOIN source_books s ON s.id = t.source_book_id
               WHERE t.id = ?""",
            (term_id,)
        ).fetchone())


def get_linked_terms(content_type: str, content_id: int) -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            """SELECT t.id, t.name
               FROM content_term_links ctl
               JOIN terms t ON t.id = ctl.term_id
               WHERE ctl.content_type = ? AND ctl.content_id = ?
               ORDER BY t.name""",
            (content_type, content_id)
        ).fetchall())


# ─────────────────────────────────────────────
# ROLL TABLES
# ─────────────────────────────────────────────

def get_roll_tables_by_category(cat_id: int) -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            """SELECT rt.*, s.short_code AS book_code
               FROM roll_tables rt
               LEFT JOIN source_books s ON s.id = rt.source_book_id
               WHERE rt.category_id = ?
               ORDER BY rt.name""",
            (cat_id,)
        ).fetchall())


def get_all_roll_tables() -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            """SELECT rt.*, s.short_code AS book_code, c.name AS category_name
               FROM roll_tables rt
               LEFT JOIN source_books s ON s.id = rt.source_book_id
               LEFT JOIN categories c ON c.id = rt.category_id
               ORDER BY rt.name"""
        ).fetchall())


def get_roll_table(table_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            """SELECT rt.*, s.short_code AS book_code
               FROM roll_tables rt
               LEFT JOIN source_books s ON s.id = rt.source_book_id
               WHERE rt.id = ?""",
            (table_id,)
        ).fetchone())


def get_table_entries(table_id: int) -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            "SELECT * FROM roll_table_entries WHERE table_id = ? ORDER BY roll_min",
            (table_id,)
        ).fetchall())


def get_entry_for_roll(table_id: int, roll: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            """SELECT * FROM roll_table_entries
               WHERE table_id = ? AND roll_min <= ? AND roll_max >= ?""",
            (table_id, roll, roll)
        ).fetchone())


# ─────────────────────────────────────────────
# ITEMS (EQUIPMENT)
# ─────────────────────────────────────────────

def get_items_by_type(item_type: str) -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            """SELECT i.*, s.short_code AS book_code
               FROM items i
               LEFT JOIN source_books s ON s.id = i.source_book_id
               WHERE i.item_type = ?
               ORDER BY i.name""",
            (item_type,)
        ).fetchall())


def get_item(item_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            """SELECT i.*, s.short_code AS book_code
               FROM items i
               LEFT JOIN source_books s ON s.id = i.source_book_id
               WHERE i.id = ?""",
            (item_id,)
        ).fetchone())


# ─────────────────────────────────────────────
# SKILLS
# ─────────────────────────────────────────────

def get_all_skills() -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            "SELECT * FROM skills ORDER BY tier, name"
        ).fetchall())


def get_skill(skill_id: int) -> dict | None:
    with _conn() as conn:
        row = conn.execute(
            """SELECT s.*, p.name AS prerequisite_name
               FROM skills s
               LEFT JOIN skills p ON p.id = s.prerequisite_id
               WHERE s.id = ?""",
            (skill_id,)
        ).fetchone()
        return _row(row)


def get_skill_tree() -> list[dict]:
    """Returns all skills with their full tree structure."""
    with _conn() as conn:
        rows = _rows(conn.execute(
            """SELECT s.*, p.name AS prerequisite_name
               FROM skills s
               LEFT JOIN skills p ON p.id = s.prerequisite_id
               ORDER BY (s.prerequisite_id IS NOT NULL), s.tier, s.name"""
        ).fetchall())
    return rows


# ─────────────────────────────────────────────
# CLASSES
# ─────────────────────────────────────────────

def get_all_classes() -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            "SELECT * FROM classes ORDER BY name"
        ).fetchall())


def get_class(class_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            "SELECT * FROM classes WHERE id = ?", (class_id,)
        ).fetchone())


# ─────────────────────────────────────────────
# SHIPS
# ─────────────────────────────────────────────

def get_all_ships() -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            """SELECT sh.*, s.short_code AS book_code
               FROM ships sh
               LEFT JOIN source_books s ON s.id = sh.source_book_id
               ORDER BY sh.class, sh.name"""
        ).fetchall())


def get_ship(ship_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            """SELECT sh.*, s.short_code AS book_code
               FROM ships sh
               LEFT JOIN source_books s ON s.id = sh.source_book_id
               WHERE sh.id = ?""",
            (ship_id,)
        ).fetchone())


# ─────────────────────────────────────────────
# LOCATIONS
# ─────────────────────────────────────────────

def get_locations_by_book(source_book_id: int, parent_id: int | None = None) -> list[dict]:
    with _conn() as conn:
        if parent_id is None:
            rows = conn.execute(
                """SELECT * FROM locations
                   WHERE source_book_id = ? AND parent_id IS NULL
                   ORDER BY name""",
                (source_book_id,)
            ).fetchall()
        else:
            rows = conn.execute(
                """SELECT * FROM locations
                   WHERE source_book_id = ? AND parent_id = ?
                   ORDER BY name""",
                (source_book_id, parent_id)
            ).fetchall()
        return _rows(rows)


def get_child_locations(parent_id: int) -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            "SELECT * FROM locations WHERE parent_id = ? ORDER BY name",
            (parent_id,)
        ).fetchall())


def get_location(loc_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            """SELECT l.*, s.short_code AS book_code, p.name AS parent_name
               FROM locations l
               LEFT JOIN source_books s ON s.id = l.source_book_id
               LEFT JOIN locations p ON p.id = l.parent_id
               WHERE l.id = ?""",
            (loc_id,)
        ).fetchone())


# ─────────────────────────────────────────────
# NPCs
# ─────────────────────────────────────────────

def get_npcs_by_book(source_book_id: int) -> list[dict]:
    with _conn() as conn:
        return _rows(conn.execute(
            """SELECT n.*, s.short_code AS book_code, l.name AS location_name
               FROM npcs n
               LEFT JOIN source_books s ON s.id = n.source_book_id
               LEFT JOIN locations l ON l.id = n.location_id
               WHERE n.source_book_id = ?
               ORDER BY n.name""",
            (source_book_id,)
        ).fetchall())


def get_npc(npc_id: int) -> dict | None:
    with _conn() as conn:
        return _row(conn.execute(
            """SELECT n.*, s.short_code AS book_code, l.name AS location_name
               FROM npcs n
               LEFT JOIN source_books s ON s.id = n.source_book_id
               LEFT JOIN locations l ON l.id = n.location_id
               WHERE n.id = ?""",
            (npc_id,)
        ).fetchone())


# ─────────────────────────────────────────────
# SEARCH
# ─────────────────────────────────────────────

def search_all(query: str) -> dict[str, list[dict]]:
    """Full-text search across all content types. Returns dict of results."""
    q = f"%{query.lower()}%"
    results: dict[str, list[dict]] = {}

    with _conn() as conn:
        rules = _rows(conn.execute(
            "SELECT id, title, 'rule' AS type FROM rules WHERE LOWER(title) LIKE ? OR LOWER(body) LIKE ?",
            (q, q)
        ).fetchall())
        if rules:
            results["Rules"] = rules

        terms = _rows(conn.execute(
            "SELECT id, name AS title, 'term' AS type FROM terms WHERE LOWER(name) LIKE ? OR LOWER(body) LIKE ? OR LOWER(aliases) LIKE ?",
            (q, q, q)
        ).fetchall())
        if terms:
            results["Glossary"] = terms

        items = _rows(conn.execute(
            "SELECT id, name AS title, item_type AS type FROM items WHERE LOWER(name) LIKE ? OR LOWER(description) LIKE ?",
            (q, q)
        ).fetchall())
        if items:
            results["Equipment"] = items

        npcs = _rows(conn.execute(
            "SELECT id, name AS title, 'npc' AS type FROM npcs WHERE LOWER(name) LIKE ? OR LOWER(description) LIKE ?",
            (q, q)
        ).fetchall())
        if npcs:
            results["NPCs"] = npcs

        locations = _rows(conn.execute(
            "SELECT id, name AS title, 'location' AS type FROM locations WHERE LOWER(name) LIKE ? OR LOWER(description) LIKE ?",
            (q, q)
        ).fetchall())
        if locations:
            results["Locations"] = locations

        tables = _rows(conn.execute(
            "SELECT id, name AS title, 'table' AS type FROM roll_tables WHERE LOWER(name) LIKE ? OR LOWER(description) LIKE ?",
            (q, q)
        ).fetchall())
        if tables:
            results["Roll Tables"] = tables

    return results

