"""
scripts/add_missed_links_armour_loadout.py
Add missing content_links for:
  - Vaccsuit/Hazard Suit <-> Oxygen, Radiation, Atmospheres, Short-range Comms, Rebreather
  - Radiation -> Radiation Pills (reverse of existing C90->C155)
  - Oxygen -> Vaccsuit/Hazard Suit (reverse of existing C83->C154)
  - All four class loadouts -> armour items that appear in their dice tables
  - All four class loadouts -> weapons & equipment that appear in their dice tables
Run: python scripts/add_missed_links_armour_loadout.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# (from_content_id, to_content_id, label_key)
LINKS = [
    # ── Group A: Armour/Suits <-> Survival Rules ──────────────────────────────
    # C42 Vaccsuit
    (42, 154, "related"),   # Vaccsuit -> Oxygen
    (42, 150, "related"),   # Vaccsuit -> Atmospheres
    (42, 96,  "related"),   # Vaccsuit -> Short-range Comms (built-in)
    # C43 Hazard Suit
    (43, 154, "related"),   # Hazard Suit -> Oxygen
    (43, 155, "related"),   # Hazard Suit -> Radiation (reverse of C155->C43 already exists)
    (43, 150, "related"),   # Hazard Suit -> Atmospheres
    (43, 96,  "related"),   # Hazard Suit -> Short-range Comms (built-in)
    (43, 92,  "related"),   # Hazard Suit -> Rebreather

    # ── Group B: Survival Rules -> Gear ───────────────────────────────────────
    (154, 42,  "related"),  # Oxygen -> Vaccsuit
    (154, 43,  "related"),  # Oxygen -> Hazard Suit
    (155, 90,  "related"),  # Radiation -> Radiation Pills (reverse of C90->C155)

    # ── Group C: Loadout -> Armour ────────────────────────────────────────────
    (51, 44, "related"),    # Marine Loadout -> Standard Battle Dress
    (51, 45, "related"),    # Marine Loadout -> Advanced Battle Dress
    (52, 41, "related"),    # Android Loadout -> Standard Crew Attire
    (52, 42, "related"),    # Android Loadout -> Vaccsuit
    (52, 43, "related"),    # Android Loadout -> Hazard Suit
    (52, 44, "related"),    # Android Loadout -> Standard Battle Dress
    (53, 41, "related"),    # Scientist Loadout -> Standard Crew Attire
    (53, 42, "related"),    # Scientist Loadout -> Vaccsuit
    (53, 43, "related"),    # Scientist Loadout -> Hazard Suit
    (54, 41, "related"),    # Teamster Loadout -> Standard Crew Attire
    (54, 42, "related"),    # Teamster Loadout -> Vaccsuit
    (54, 43, "related"),    # Teamster Loadout -> Hazard Suit

    # ── Group D: Marine Loadout -> Weapons & Equipment ────────────────────────
    (51, 2,  "related"),    # Marine -> Boarding Axe
    (51, 3,  "related"),    # Marine -> Combat Shotgun
    (51, 5,  "related"),    # Marine -> Flamethrower
    (51, 8,  "related"),    # Marine -> Frag Grenade
    (51, 9,  "related"),    # Marine -> General-Purpose Machine Gun
    (51, 13, "related"),    # Marine -> Pulse Rifle
    (51, 14, "related"),    # Marine -> Revolver
    (51, 16, "related"),    # Marine -> Scalpel (as combat knife)
    (51, 17, "related"),    # Marine -> Smart Rifle
    (51, 18, "related"),    # Marine -> SMG
    (51, 73, "related"),    # Marine -> HUD
    (51, 74, "related"),    # Marine -> Infrared Goggles
    (51, 98, "related"),    # Marine -> Stimpak

    # ── Group E: Android Loadout -> Weapons & Equipment ───────────────────────
    (52, 7,  "related"),    # Android -> Foam Gun
    (52, 8,  "related"),    # Android -> Frag Grenade
    (52, 14, "related"),    # Android -> Revolver
    (52, 16, "related"),    # Android -> Scalpel
    (52, 17, "related"),    # Android -> Smart Rifle
    (52, 19, "related"),    # Android -> Stun Baton
    (52, 20, "related"),    # Android -> Tranq Pistol
    (52, 61, "related"),    # Android -> Bioscanner
    (52, 69, "related"),    # Android -> First Aid Kit
    (52, 77, "related"),    # Android -> Long-range Comms

    # ── Group F: Scientist Loadout -> Weapons & Equipment ─────────────────────
    (53, 5,  "related"),    # Scientist -> Flamethrower
    (53, 7,  "related"),    # Scientist -> Foam Gun
    (53, 15, "related"),    # Scientist -> Rigging Gun
    (53, 16, "related"),    # Scientist -> Scalpel
    (53, 20, "related"),    # Scientist -> Tranq Pistol
    (53, 58, "related"),    # Scientist -> Automed
    (53, 61, "related"),    # Scientist -> Bioscanner
    (53, 64, "related"),    # Scientist -> Cybernetic Diagnostic Scanner
    (53, 83, "related"),    # Scientist -> Oxygen Tank
    (53, 90, "related"),    # Scientist -> Radiation Pills

    # ── Group G: Teamster Loadout -> Weapons & Equipment ──────────────────────
    (54, 3,  "related"),    # Teamster -> Combat Shotgun
    (54, 4,  "related"),    # Teamster -> Crowbar
    (54, 6,  "related"),    # Teamster -> Flare Gun
    (54, 11, "related"),    # Teamster -> Laser Cutter
    (54, 12, "related"),    # Teamster -> Nail Gun
    (54, 14, "related"),    # Teamster -> Revolver
    (54, 15, "related"),    # Teamster -> Rigging Gun
    (54, 22, "related"),    # Teamster -> Vibechete
    (54, 57, "related"),    # Teamster -> Assorted Tools
    (54, 68, "related"),    # Teamster -> Explosives & Detonator
    (54, 85, "related"),    # Teamster -> Patch Kit
    (54, 94, "related"),    # Teamster -> Salvage Drone
    (54, 99, "related"),    # Teamster -> Water Filtration Device
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
