"""
scripts/update_remove_station_cyclic_links.py
Remove 5 stale backward content_links left by the old add_apof_missed_tables.py.
These create navigation cycles now that forward links exist from parent locations
to their sub-items (added by update_dry_dock_sublinking / update_station_sublinking).

Pairs removed (keeping the forward direction):
  C329 → C229  (Dry Dock Rumors → 01 Dry Dock)       keep C229 → C329
  C330 → C229  (Ships Currently Docked → 01 Dry Dock) keep C229 → C330
  C331 → C232  (Jobs for Babushka → 03 The Chop Shop) keep C232 → C331
  C332 → C240  (The Docket → 07 The Court)            keep C240 → C332
  C333 → C240  (Accused & What They Can Pay → Court)  keep C240 → C333

Run: python scripts/update_remove_station_cyclic_links.py
"""
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

REVERSE_LINKS = [
    (329, 229),
    (330, 229),
    (331, 232),
    (332, 240),
    (333, 240),
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        removed = _clean(conn)
        conn.commit()
        print(f"Done — {removed} cyclic content_link(s) removed.")
    finally:
        conn.close()


def _clean(conn: sqlite3.Connection) -> int:
    removed = 0
    for from_id, to_id in REVERSE_LINKS:
        cur = conn.execute(
            "DELETE FROM content_links WHERE from_content_id = ? AND to_content_id = ?",
            (from_id, to_id),
        )
        removed += cur.rowcount
    return removed


if __name__ == "__main__":
    run()
