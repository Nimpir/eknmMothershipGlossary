"""
scripts/update_loadout_links_missed.py
Fill in per-entry links that were missed in the initial migration for all 4 loadout
tables (C51 Marine, C52 Android, C53 Scientist, C54 Teamster).

Each table entry is defined with its COMPLETE correct links list so this script
is safe to re-run — it fully overwrites the links for every entry.

Run: python scripts/update_loadout_links_missed.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── Complete per-entry link definitions ──────────────────────────────────────
# Each list contains 10 dicts (one per roll 0–9).
# Empty list [] = no DB content items in that entry.

MARINE = [  # C51
    # 0 — Tank Top, Combat Knife (as Scalpel), Stimpak ×5
    [{"id": 16, "label": "Scalpel"},
     {"id": 98, "label": "Stimpak"}],
    # 1 — Advanced Battle Dress, Flamethrower, Boarding Axe
    [{"id": 45, "label": "Advanced Battle Dress"},
     {"id":  5, "label": "Flamethrower"},
     {"id":  2, "label": "Boarding Axe"}],
    # 2 — Standard Battle Dress, Combat Shotgun, Rucksack, Camping Gear
    [{"id": 44, "label": "Standard Battle Dress"},
     {"id":  3, "label": "Combat Shotgun"},
     {"id": 93, "label": "Rucksack"}],
    # 3 — Standard Battle Dress, Pulse Rifle, Infrared Goggles
    [{"id": 44, "label": "Standard Battle Dress"},
     {"id": 13, "label": "Pulse Rifle"},
     {"id": 74, "label": "Infrared Goggles"}],
    # 4 — Standard Battle Dress, Smart Rifle, Binoculars, Personal Locator
    [{"id": 44, "label": "Standard Battle Dress"},
     {"id": 17, "label": "Smart Rifle"},
     {"id": 60, "label": "Binoculars"},
     {"id": 86, "label": "Personal Locator"}],
    # 5 — Standard Battle Dress, SMG, MRE ×7
    [{"id": 44, "label": "Standard Battle Dress"},
     {"id": 18, "label": "SMG"},
     {"id": 81, "label": "MRE (x7)"}],
    # 6 — Fatigues, Combat Shotgun, Dog (pet), Leash, Tennis Ball
    [{"id":  3, "label": "Combat Shotgun"},
     {"id": 87, "label": "Pet (Organic)"}],
    # 7 — Fatigues, Revolver, Frag Grenade
    [{"id": 14, "label": "Revolver"},
     {"id":  8, "label": "Frag Grenade"}],
    # 8 — Dress Uniform, Revolver, Challenge Coin
    [{"id": 14, "label": "Revolver"}],
    # 9 — Advanced Battle Dress, GPMG, HUD
    [{"id": 45, "label": "Advanced Battle Dress"},
     {"id":  9, "label": "General-Purpose Machine Gun"},
     {"id": 73, "label": "Heads-Up Display (HUD)"}],
]

ANDROID = [  # C52
    # 0 — Vaccsuit, Smart Rifle, Infrared Goggles, Mylar Blanket
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 17, "label": "Smart Rifle"},
     {"id": 74, "label": "Infrared Goggles"},
     {"id": 82, "label": "Mylar Blanket"}],
    # 1 — Vaccsuit, Revolver, Long-range Comms, Satchel
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 14, "label": "Revolver"},
     {"id": 77, "label": "Long-range Comms"}],
    # 2 — Hazard Suit, Revolver, Defibrillator, First Aid Kit, Flashlight
    [{"id": 43, "label": "Hazard Suit"},
     {"id": 14, "label": "Revolver"},
     {"id": 69, "label": "First Aid Kit"},
     {"id": 70, "label": "Flashlight"}],
    # 3 — Hazard Suit, Foam Gun, Sample Collection Kit, Screwdriver (as Assorted Tools)
    [{"id": 43, "label": "Hazard Suit"},
     {"id":  7, "label": "Foam Gun"},
     {"id": 95, "label": "Sample Collection Kit"},
     {"id": 57, "label": "Assorted Tools"}],
    # 4 — Standard Battle Dress, Tranq Pistol, Paracord (100m)
    [{"id": 44, "label": "Standard Battle Dress"},
     {"id": 20, "label": "Tranq Pistol"},
     {"id": 84, "label": "Paracord (50m)"}],
    # 5 — Standard Crew Attire, Stun Baton, Small Pet (organic)
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id": 19, "label": "Stun Baton"},
     {"id": 87, "label": "Pet (Organic)"}],
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

SCIENTIST = [  # C53
    # 0 — Hazard Suit, Tranq Pistol, Bioscanner, Sample Collection Kit
    [{"id": 43, "label": "Hazard Suit"},
     {"id": 20, "label": "Tranq Pistol"},
     {"id": 61, "label": "Bioscanner"},
     {"id": 95, "label": "Sample Collection Kit"}],
    # 1 — Hazard Suit, Flamethrower, Stimpak, Electronic Tool Set
    [{"id": 43, "label": "Hazard Suit"},
     {"id":  5, "label": "Flamethrower"},
     {"id": 98, "label": "Stimpak"},
     {"id": 65, "label": "Electronic Tool Set"}],
    # 2 — Vaccsuit, Rigging Gun, Sample Collection Kit, Flashlight, Lab Rat (pet)
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 15, "label": "Rigging Gun"},
     {"id": 95, "label": "Sample Collection Kit"},
     {"id": 70, "label": "Flashlight"},
     {"id": 87, "label": "Pet (Organic)"}],
    # 3 — Vaccsuit, Foam Gun, Foldable Stretcher, First Aid Kit, Radiation Pills ×5
    [{"id": 42, "label": "Vaccsuit"},
     {"id":  7, "label": "Foam Gun"},
     {"id": 71, "label": "Foldable Stretcher"},
     {"id": 69, "label": "First Aid Kit"},
     {"id": 90, "label": "Radiation Pills (x5)"}],
    # 4 — Lab Coat, Screwdriver (as Assorted Tools), Medscanner, Vaccine
    [{"id": 57, "label": "Assorted Tools"},
     {"id": 79, "label": "Medscanner"}],
    # 5 — Lab Coat, Cybernetic Diagnostic Scanner, Portable Computer Terminal
    [{"id": 64, "label": "Cybernetic Diagnostic Scanner"},
     {"id": 89, "label": "Portable Computer Terminal"}],
    # 6 — Scrubs, Scalpel, Automed ×5, Oxygen Tank with Filter Mask
    [{"id": 16, "label": "Scalpel"},
     {"id": 58, "label": "Automed (x5)"},
     {"id": 83, "label": "Oxygen Tank"}],
    # 7 — Scrubs, Vial of Acid, Mylar Blanket, First Aid Kit
    [{"id": 82, "label": "Mylar Blanket"},
     {"id": 69, "label": "First Aid Kit"}],
    # 8 — Standard Crew Attire, Utility Knife (as Scalpel), CDS, Duct Tape
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id": 16, "label": "Scalpel"},
     {"id": 64, "label": "Cybernetic Diagnostic Scanner"}],
    # 9 — Civilian Clothes, Briefcase, Prescription Pad, Fountain Pen (Poison Injector)
    [],
]

TEAMSTER = [  # C54
    # 0 — Vaccsuit, Laser Cutter, Patch Kit ×3, Toolbelt w/ Assorted Tools
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 11, "label": "Laser Cutter"},
     {"id": 85, "label": "Patch Kit (x3)"},
     {"id": 57, "label": "Assorted Tools"}],
    # 1 — Vaccsuit, Revolver, Crowbar, Flashlight
    [{"id": 42, "label": "Vaccsuit"},
     {"id": 14, "label": "Revolver"},
     {"id":  4, "label": "Crowbar"},
     {"id": 70, "label": "Flashlight"}],
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
    # 5 — Heavy Duty Work Clothes, Drill (as Assorted Tools), Paracord (100m), Salvage Drone
    [{"id": 57, "label": "Assorted Tools"},
     {"id": 84, "label": "Paracord (50m)"},
     {"id": 94, "label": "Salvage Drone"}],
    # 6 — Standard Crew Attire, Combat Shotgun, Extension Cord, Cat (pet)
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id":  3, "label": "Combat Shotgun"},
     {"id": 87, "label": "Pet (Organic)"}],
    # 7 — Standard Crew Attire, Nail Gun, Head Lamp, Toolbelt w/ Assorted Tools, Lunch Box
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id": 12, "label": "Nail Gun"},
     {"id": 57, "label": "Assorted Tools"}],
    # 8 — Standard Crew Attire, Flare Gun, Water Filtration Device, Personal Locator
    [{"id": 41, "label": "Standard Crew Attire"},
     {"id":  6, "label": "Flare Gun"},
     {"id": 99, "label": "Water Filtration Device"},
     {"id": 86, "label": "Personal Locator"}],
    # 9 — Lounge Wear, Crowbar, Stimpak, Six Pack of Beer
    [{"id":  4, "label": "Crowbar"},
     {"id": 98, "label": "Stimpak"}],
]

TABLES = [
    (51, MARINE,    "Marine"),
    (52, ANDROID,   "Android"),
    (53, SCIENTIST, "Scientist"),
    (54, TEAMSTER,  "Teamster"),
]


def _apply(conn: sqlite3.Connection, content_id: int, entry_links: list, label: str) -> None:
    row = conn.execute("SELECT dice FROM contents WHERE id = ?", (content_id,)).fetchone()
    if not row or not row[0]:
        raise RuntimeError(f"C{content_id} has no dice JSON")

    dice = json.loads(row[0])
    entries = dice.get("entries", [])

    if len(entries) != len(entry_links):
        raise RuntimeError(
            f"C{content_id} {label}: expected {len(entry_links)} entries, got {len(entries)}"
        )

    for entry, links in zip(entries, entry_links):
        if links:
            entry["links"] = links
        else:
            entry.pop("links", None)  # clean up any stale empty list

    conn.execute("UPDATE contents SET dice = ? WHERE id = ?",
                 (json.dumps(dice), content_id))
    print(f"  C{content_id} {label}: {len(entries)} entries updated")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        for content_id, entry_links, label in TABLES:
            _apply(conn, content_id, entry_links, label)
        conn.commit()
        print("Done — all 4 loadout tables fully corrected.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
