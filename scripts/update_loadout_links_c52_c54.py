"""
scripts/update_loadout_links_c52_c54.py
Move Android (C52), Scientist (C53), and Teamster (C54) loadout content_links
to per-entry links inside each dice entry's JSON.

Before: flat content_links on the table item covering all gear across all rolls.
After:  each dice entry carries only the links relevant to that specific roll;
        the flat content_links rows are deleted.

Run: python scripts/update_loadout_links_c52_c54.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── Android Loadout (C52) ─────────────────────────────────────────────────────

ANDROID_ENTRY_LINKS = [
    # 0 — Vaccsuit, Smart Rifle, Infrared Goggles, Mylar Blanket
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 17, "label": "Smart Rifle"}],
    # 1 — Vaccsuit, Revolver, Long-range Comms, Satchel
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 14, "label": "Revolver"},
     {"id": 77, "label": "Long-range Comms"}],
    # 2 — Hazard Suit, Revolver, Defibrillator, First Aid Kit, Flashlight
    [{"id": 43, "label": "Hazard Suit"},
     {"id": 14, "label": "Revolver"},
     {"id": 69, "label": "First Aid Kit"}],
    # 3 — Hazard Suit, Foam Gun, Sample Collection Kit, Screwdriver
    [{"id": 43, "label": "Hazard Suit"},
     {"id":  7, "label": "Foam Gun"}],
    # 4 — Standard Battle Dress, Tranq Pistol, Paracord
    [{"id": 44, "label": "Standard Battle Dress"},
     {"id": 20, "label": "Tranq Pistol"}],
    # 5 — Standard Crew Attire, Stun Baton, Small Pet (organic)
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id": 19, "label": "Stun Baton"}],
    # 6 — Standard Crew Attire, Scalpel, Bioscanner
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id": 16, "label": "Scalpel"},
     {"id": 61, "label": "Bioscanner"}],
    # 7 — Standard Crew Attire, Frag Grenade, Pen Knife
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id":  8, "label": "Frag Grenade"}],
    # 8 — Manufacturer Supplied Attire, Jump-9 Ticket
    [],
    # 9 — Corporate Attire, VIP Corporate Key Card
    [],
]

ANDROID_LINKS_TO_DELETE = [7, 8, 14, 16, 17, 19, 20, 41, 42, 43, 44, 61, 69, 77]


# ── Scientist Loadout (C53) ───────────────────────────────────────────────────

SCIENTIST_ENTRY_LINKS = [
    # 0 — Hazard Suit, Tranq Pistol, Bioscanner, Sample Collection Kit
    [{"id": 43, "label": "Hazard Suit"},
     {"id": 20, "label": "Tranq Pistol"},
     {"id": 61, "label": "Bioscanner"}],
    # 1 — Hazard Suit, Flamethrower, Stimpak, Electronic Tool Set
    [{"id": 43, "label": "Hazard Suit"},
     {"id":  5, "label": "Flamethrower"}],
    # 2 — Vaccsuit, Rigging Gun, Sample Collection Kit, Flashlight, Lab Rat
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 15, "label": "Rigging Gun"}],
    # 3 — Vaccsuit, Foam Gun, Foldable Stretcher, First Aid Kit, Radiation Pills
    [{"id": 42, "label": "Vaccsuit"},
     {"id":  7, "label": "Foam Gun"},
     {"id": 90, "label": "Radiation Pills (x5)"}],
    # 4 — Lab Coat, Screwdriver, Medscanner, Vaccine
    [],
    # 5 — Lab Coat, Cybernetic Diagnostic Scanner, Portable Computer Terminal
    [{"id": 64, "label": "Cybernetic Diagnostic Scanner"}],
    # 6 — Scrubs, Scalpel, Automed ×5, Oxygen Tank
    [{"id": 16, "label": "Scalpel"},
     {"id": 58, "label": "Automed (x5)"},
     {"id": 83, "label": "Oxygen Tank"}],
    # 7 — Scrubs, Vial of Acid, Mylar Blanket, First Aid Kit
    [],
    # 8 — Standard Crew Attire, Utility Knife (as Scalpel), CDS, Duct Tape
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id": 16, "label": "Scalpel"},
     {"id": 64, "label": "Cybernetic Diagnostic Scanner"}],
    # 9 — Civilian Clothes, Briefcase, Prescription Pad, Poison Injector
    [],
]

SCIENTIST_LINKS_TO_DELETE = [5, 7, 15, 16, 20, 41, 42, 43, 58, 61, 64, 83, 90]


# ── Teamster Loadout (C54) ────────────────────────────────────────────────────

TEAMSTER_ENTRY_LINKS = [
    # 0 — Vaccsuit, Laser Cutter, Patch Kit ×3, Toolbelt w/ Assorted Tools
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 11, "label": "Laser Cutter"},
     {"id": 85, "label": "Patch Kit (x3)"},
     {"id": 57, "label": "Assorted Tools"}],
    # 1 — Vaccsuit, Revolver, Crowbar, Flashlight
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 14, "label": "Revolver"},
     {"id":  4, "label": "Crowbar"}],
    # 2 — Vaccsuit, Rigging Gun, Shovel, Salvage Drone
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 15, "label": "Rigging Gun"},
     {"id": 94, "label": "Salvage Drone"}],
    # 3 — Hazard Suit, Vibechete, Spanner, Camping Gear, Water Filtration Device
    [{"id": 43, "label": "Hazard Suit"},
     {"id": 22, "label": "Vibechete"},
     {"id": 99, "label": "Water Filtration Device"}],
    # 4 — Heavy Duty Work Clothes, Explosives & Detonator, Cigarettes
    [{"id": 68, "label": "Explosives & Detonator"}],
    # 5 — Heavy Duty Work Clothes, Drill (as Assorted Tools), Paracord, Salvage Drone
    [{"id": 57, "label": "Assorted Tools"},
     {"id": 94, "label": "Salvage Drone"}],
    # 6 — Standard Crew Attire, Combat Shotgun, Extension Cord, Cat (pet)
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id":  3, "label": "Combat Shotgun"}],
    # 7 — Standard Crew Attire, Nail Gun, Head Lamp, Toolbelt w/ Assorted Tools
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id": 12, "label": "Nail Gun"},
     {"id": 57, "label": "Assorted Tools"}],
    # 8 — Standard Crew Attire, Flare Gun, Water Filtration Device, Personal Locator
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id":  6, "label": "Flare Gun"},
     {"id": 99, "label": "Water Filtration Device"}],
    # 9 — Lounge Wear, Crowbar, Stimpak, Six Pack of Beer
    [{"id":  4, "label": "Crowbar"}],
]

TEAMSTER_LINKS_TO_DELETE = [3, 4, 6, 11, 12, 14, 15, 22, 41, 42, 43, 57, 68, 85, 94, 99]


# ── Helpers ───────────────────────────────────────────────────────────────────

TABLES = [
    (52, ANDROID_ENTRY_LINKS,   ANDROID_LINKS_TO_DELETE,   "Android"),
    (53, SCIENTIST_ENTRY_LINKS, SCIENTIST_LINKS_TO_DELETE, "Scientist"),
    (54, TEAMSTER_ENTRY_LINKS,  TEAMSTER_LINKS_TO_DELETE,  "Teamster"),
]


def _migrate_one(
    conn: sqlite3.Connection,
    content_id: int,
    entry_links: list,
    links_to_delete: list,
    label: str,
) -> None:
    row = conn.execute("SELECT dice FROM contents WHERE id = ?", (content_id,)).fetchone()
    if not row or not row[0]:
        raise RuntimeError(f"Content {content_id} not found or has no dice JSON")

    dice = json.loads(row[0])
    entries = dice.get("entries", [])

    if len(entries) != len(entry_links):
        raise RuntimeError(
            f"C{content_id} {label}: expected {len(entry_links)} entries, found {len(entries)}"
        )

    for entry, links in zip(entries, entry_links):
        if links:
            entry["links"] = links
        # Leave entries with no links untouched (no empty key)

    conn.execute(
        "UPDATE contents SET dice = ? WHERE id = ?",
        (json.dumps(dice), content_id)
    )

    placeholders = ",".join("?" * len(links_to_delete))
    deleted = conn.execute(
        f"DELETE FROM content_links "
        f"WHERE from_content_id = ? AND to_content_id IN ({placeholders})",
        [content_id] + links_to_delete,
    ).rowcount

    print(f"  C{content_id} {label}: per-entry links injected, {deleted} content_links removed")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        for content_id, entry_links, links_to_delete, label in TABLES:
            _migrate_one(conn, content_id, entry_links, links_to_delete, label)
        conn.commit()
        print("Done — Android / Scientist / Teamster loadout links migrated.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
