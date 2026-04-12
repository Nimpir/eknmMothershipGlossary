"""
scripts/update_p38_move_c307_delete_p50.py
Move C307 (Denizens of The Dream) from P50 directly onto P38 (Tables),
then delete P50 entirely.
NOTE: Superseded by update_apof_denizens_split.py which now handles this inline.
      Keep for historical reference — already applied to production DB.
Run: python scripts/update_p38_move_c307_delete_p50.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — C307 moved to P38; P50 deleted.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    # ── 1. Add C307 to P38 page_contents at sort_order 6 ──────────────────
    conn.execute(
        "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (38, 307, 6)",
    )

    # ── 2. Remove C307 from P50 page_contents ─────────────────────────────
    conn.execute("DELETE FROM page_contents WHERE page_id=50 AND content_id=307")

    # ── 3. Remove P50 from P38 linked_pages ───────────────────────────────
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=38").fetchone()
    lp = json.loads(row[0]) if row[0] else []
    lp = [p for p in lp if p != 50]
    conn.execute(
        "UPDATE pages SET linked_pages=? WHERE id=38",
        (json.dumps(lp),),
    )

    # ── 4. Delete P50 page_i18n ────────────────────────────────────────────
    conn.execute("DELETE FROM page_i18n WHERE page_id=50")

    # ── 5. Delete P50 from pages ───────────────────────────────────────────
    conn.execute("DELETE FROM pages WHERE id=50")


if __name__ == "__main__":
    run()
