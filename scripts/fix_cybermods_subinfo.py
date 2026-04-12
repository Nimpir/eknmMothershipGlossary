"""
scripts/fix_cybermods_subinfo.py
Convert subinfo_fixed on C259-C295 (cyberware/slickware) from the legacy
flat-dict format {"cost": "x", "slots": "y"} to the canonical list-of-objects
format [{"label_key": "cost", "value": "x", "type": "cost"}, ...].
Run: python scripts/fix_cybermods_subinfo.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

_TYPE_HINTS: dict[str, str] = {"cost": "cost", "mass": "mass"}


def _convert(raw: str) -> str | None:
    """Return the corrected JSON string, or None if already correct / empty."""
    if not raw:
        return None
    data = json.loads(raw)
    if isinstance(data, list):
        return None  # already correct format
    if isinstance(data, dict):
        entries = [
            {"label_key": k, "value": v, "type": _TYPE_HINTS.get(k, "stat")}
            for k, v in data.items()
        ]
        return json.dumps(entries)
    return None


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    updated = 0
    try:
        rows = conn.execute(
            "SELECT id, subinfo_fixed FROM contents WHERE subinfo_fixed IS NOT NULL"
        ).fetchall()
        for cid, raw in rows:
            fixed = _convert(raw)
            if fixed is not None:
                conn.execute(
                    "UPDATE contents SET subinfo_fixed = ? WHERE id = ?",
                    (fixed, cid),
                )
                updated += 1
        conn.commit()
        print(f"Done — {updated} rows converted to list-of-objects format.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
