"""
scripts/update_remove_cyclic_links.py
Remove 5 reciprocal content_links that create navigation cycles.

Each pair A→B / B→A causes the nav_stack to grow unboundedly as the user
clicks back and forth between the two items.  We keep the semantically
forward direction and delete the reverse.

Run: python scripts/update_remove_cyclic_links.py
"""
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# (from_content_id, to_content_id) rows to DELETE
# Comments show which direction is being KEPT
REVERSE_LINKS = [
    (91,  66),   # remove Radio Jammer→Emergency Beacon   (keep C66→C91)
    (96,  91),   # remove Short-range Comms→Radio Jammer  (keep C91→C96)
    (156, 98),   # remove Stimpak Overdose→Stimpak        (keep C98→C156)
    (105, 104),  # remove Conditions→Panic Checks          (keep C104→C105)
    (168, 167),  # remove Shore Leave→Port Classes         (keep C167→C168)
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        removed = _remove(conn)
        conn.commit()
        print(f"Done — {removed} cyclic content_link(s) removed.")
    finally:
        conn.close()


def _remove(conn: sqlite3.Connection) -> int:
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
