"""
scripts/add_missed_links_battle_dress.py
Add missing content_links for C44 Standard Battle Dress and C45 Advanced Battle Dress.
  - C44: built-in short-range comms
  - C45: built-in short-range comms, body cam, HUD, radiation shielding, 1hr O2 supply
Run: python scripts/add_missed_links_battle_dress.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

LINKS = [
    # C44 Standard Battle Dress
    (44, 96,  "related"),   # -> Short-range Comms (built-in)
    # C45 Advanced Battle Dress
    (45, 96,  "related"),   # -> Short-range Comms (built-in)
    (45, 62,  "related"),   # -> Body Cam (built-in)
    (45, 73,  "related"),   # -> HUD (built-in)
    (45, 155, "related"),   # -> Radiation (radiation shielding built-in)
    (45, 154, "related"),   # -> Oxygen (1hr O2 supply)
    (45, 150, "related"),   # -> Atmospheres (O2 supply enables hostile atmo use)
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        added = _seed(conn)
        conn.commit()
        print(f"Done — {added} content_links added.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> int:
    added = 0
    for from_id, to_id, label in LINKS:
        cur = conn.execute(
            """
            INSERT INTO content_links (from_content_id, to_content_id, label_key)
            VALUES (?, ?, ?)
            ON CONFLICT(from_content_id, to_content_id) DO NOTHING
            """,
            (from_id, to_id, label),
        )
        added += cur.rowcount
    return added


if __name__ == "__main__":
    run()
