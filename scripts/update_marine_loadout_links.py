"""
scripts/update_marine_loadout_links.py
Move Marine Loadout (C51) content_links to per-entry links inside the dice JSON.

Before: 15 content_links rows on C51 covering all gear across all rolls.
After:  Each dice entry carries only the links relevant to that specific roll.
        The 15 content_links rows are deleted.

Run: python scripts/update_marine_loadout_links.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

CONTENT_ID = 51

# Per-roll links: index matches entry order (min=0..9).
# {"id": content_id, "label": display_name_en}
ENTRY_LINKS = [
    # Roll 0 — Tank Top, Combat Knife (as Scalpel DMG [+]), Stimpak ×5
    [
        {"id": 16, "label": "Scalpel"},
        {"id": 98, "label": "Stimpak"},
    ],
    # Roll 1 — Advanced Battle Dress, Flamethrower, Boarding Axe
    [
        {"id": 45, "label": "Advanced Battle Dress"},
        {"id":  5, "label": "Flamethrower"},
        {"id":  2, "label": "Boarding Axe"},
    ],
    # Roll 2 — Standard Battle Dress, Combat Shotgun, Rucksack, Camping Gear
    [
        {"id": 44, "label": "Standard Battle Dress"},
        {"id":  3, "label": "Combat Shotgun"},
    ],
    # Roll 3 — Standard Battle Dress, Pulse Rifle, Infrared Goggles
    [
        {"id": 44, "label": "Standard Battle Dress"},
        {"id": 13, "label": "Pulse Rifle"},
        {"id": 74, "label": "Infrared Goggles"},
    ],
    # Roll 4 — Standard Battle Dress, Smart Rifle, Binoculars, Personal Locator
    [
        {"id": 44, "label": "Standard Battle Dress"},
        {"id": 17, "label": "Smart Rifle"},
    ],
    # Roll 5 — Standard Battle Dress, SMG, MRE ×7
    [
        {"id": 44, "label": "Standard Battle Dress"},
        {"id": 18, "label": "SMG"},
    ],
    # Roll 6 — Fatigues, Combat Shotgun, Dog (pet), Leash, Tennis Ball
    [
        {"id":  3, "label": "Combat Shotgun"},
    ],
    # Roll 7 — Fatigues, Revolver, Frag Grenade
    [
        {"id": 14, "label": "Revolver"},
        {"id":  8, "label": "Frag Grenade"},
    ],
    # Roll 8 — Dress Uniform, Revolver, Challenge Coin
    [
        {"id": 14, "label": "Revolver"},
    ],
    # Roll 9 — Advanced Battle Dress, GPMG, HUD
    [
        {"id": 45, "label": "Advanced Battle Dress"},
        {"id":  9, "label": "General-Purpose Machine Gun"},
        {"id": 73, "label": "Heads-Up Display (HUD)"},
    ],
]

# content_links to remove (all outgoing from C51 that are now per-entry)
LINKS_TO_DELETE = [2, 3, 5, 8, 9, 13, 14, 16, 17, 18, 44, 45, 73, 74, 98]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _migrate(conn)
        conn.commit()
        print("Done — C51 Marine Loadout: per-entry links injected, 15 content_links removed.")
    finally:
        conn.close()


def _migrate(conn: sqlite3.Connection) -> None:
    # 1. Load current dice JSON
    row = conn.execute("SELECT dice FROM contents WHERE id = ?", (CONTENT_ID,)).fetchone()
    if not row or not row[0]:
        raise RuntimeError(f"Content {CONTENT_ID} not found or has no dice JSON")

    dice = json.loads(row[0])
    entries = dice.get("entries", [])

    if len(entries) != len(ENTRY_LINKS):
        raise RuntimeError(
            f"Expected {len(ENTRY_LINKS)} entries, found {len(entries)} in C{CONTENT_ID}"
        )

    # 2. Inject links into each entry
    for entry, links in zip(entries, ENTRY_LINKS):
        entry["links"] = links

    # 3. Write updated dice JSON back
    conn.execute(
        "UPDATE contents SET dice = ? WHERE id = ?",
        (json.dumps(dice), CONTENT_ID)
    )

    # 4. Delete the old content_links rows
    placeholders = ",".join("?" * len(LINKS_TO_DELETE))
    deleted = conn.execute(
        f"DELETE FROM content_links WHERE from_content_id = ? AND to_content_id IN ({placeholders})",
        [CONTENT_ID] + LINKS_TO_DELETE
    ).rowcount

    print(f"  • Updated dice JSON for C{CONTENT_ID}")
    print(f"  • Deleted {deleted} content_links rows")


if __name__ == "__main__":
    run()
