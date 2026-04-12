"""
scripts/update_noteworthy_locations.py
Replace C328 (combined Noteworthy Locations) with 8 individual d100 tables,
one per station type column from A Pound of Flesh pp.50-51:
  C328 Refuel/Repair (repurposed, icon updated)
  C334 Port/Market
  C335 Colony/Habitat
  C336 Military
  C337 Mining/Factory
  C338 Corporate/Research
  C339 Prison
  C340 Religious
All placed on P38 (Tables). Old C328 content links removed.

Run: python scripts/update_noteworthy_locations.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── helpers ───────────────────────────────────────────────────────────────────

def _e(groups: list[str], singles: list[str]) -> list[dict]:
    """Build d100 entries: 18 groups of 5 (00-04..85-89) + 10 singles (90-99)."""
    entries = []
    for i, text in enumerate(groups):
        lo = i * 5
        entries.append({"min": lo, "max": lo + 4, "text": text})
    for i, text in enumerate(singles):
        entries.append({"min": 90 + i, "max": 90 + i, "text": text})
    return entries


# ── table data ─────────────────────────────────────────────────────────────────
# Each table: (id, icon, name_en, name_ru, name_ua, groups_en, singles_en)
# RU/UA: English used as placeholder (no translation available).

TABLES = [
    (
        328, "🔧",
        "Noteworthy Locations — Refuel/Repair",
        "Примечательные места — Дозаправка/Ремонт",
        "Примітні місця — Дозаправка/Ремонт",
        [
            "Dry Dock",
            "Vehicle Repair",
            "Chop Shop",
            "Bars",
            "Showers",
            "Capsule Motel",
            "Navigation Library",
            "Warp Core Storage",
            "Teamster Union Hall",
            "Military Lounge",
            "Commercial Travel",
            "Private Hangar",
            "Showers",
            "Metal Foundry",
            "Ore Trade / Refinery",
            "Food Court",
            "Fuel Bays / Warp Cores",
            "Slickscreens",
        ],
        [
            "Red Light District",
            "Black Market",
            "Tiny Chapel",
            "Weapons Fabrication",
            "Advanced R&D",
            "Experimental FTL Lab",
            "Astronavigator Terminals",
            "Station Overseer",
            "Holding Cells",
            "Power Station",
        ],
    ),
    (
        334, "🏬",
        "Noteworthy Locations — Port/Market",
        "Примечательные места — Порт/Рынок",
        "Примітні місця — Порт/Ринок",
        [
            "Food Stand",
            "Dry Dock",
            "Fence for Stolen Goods",
            "Black Market",
            "Re-Sleeving Facility",
            "Cybermod Shop",
            "Imports Warehouse",
            "Designer Drugs",
            "Gene Therapy",
            "Holotat Shop",
            "Glass Blower",
            "Technobladesmith",
            "Slaughter Yard",
            "Fabric Loom",
            "Sweatshop",
            "Gambling House",
            "Dance Club",
            "Teamster Bar",
        ],
        [
            "Cassette Library",
            "Specimens & Oddities",
            "Red Light District",
            "Military Black Site",
            "Navigator Guildhouse",
            "Decorative Rugs",
            "Tea Shop",
            "Old Earth Antique Shop",
            "Custom Androids",
            "Ship Designer",
        ],
    ),
    (
        335, "🏘️",
        "Noteworthy Locations — Colony/Habitat",
        "Примечательные места — Колония/Жильё",
        "Примітні місця — Колонія/Житло",
        [
            "Farming Unit",
            "Food Court",
            "Slickscreen",
            "Bar/Club",
            "Slaughterhouse",
            "Seed/Gene Storage",
            "Sleeping Units",
            "Meeting Square",
            "Aquaponics Tanks",
            "Markets",
            "School/Training Facilities",
            "Library/Research Lab",
            "Upscale Housing",
            "Security Outpost",
            "Clinic",
            "Factory",
            "Greenhouse",
            "Turret Emplacement",
        ],
        [
            "Red Light District",
            "Brig",
            "Power Station",
            "Pharmalab",
            "Governor's Mansion",
            "Armory",
            "Temple",
            "Courthouse/Records",
            "Landing Strip",
            "Communication Array",
        ],
    ),
    (
        336, "⚔️",
        "Noteworthy Locations — Military",
        "Примечательные места — Военная база",
        "Примітні місця — Військова база",
        [
            "Admin Offices",
            "Drop Station",
            "Training Rooms",
            "Shooting Range",
            "Command Center",
            "Defensive Weaponry",
            "Vehicle Repair Center",
            "Brig",
            "Troopship Carrier",
            "Barracks",
            "Interrogation Rooms",
            "Medbay",
            "R&D Department",
            "Drop-tank Hangar",
            "Mess Hall",
            "Officer's Lounge",
            '"Off-base" Housing',
            "Master Computer",
        ],
        [
            "Diplomatic Embassy",
            "Officer's Quarters",
            "Weapon Testing",
            "Fighter Squadron",
            "Ammunition Storage",
            "Re-Sleeving Facility",
            "Cryochambers",
            "Intelligence Facility",
            "Exomech Hangar",
            "Massive Weapon",
        ],
    ),
    (
        337, "⛏️",
        "Noteworthy Locations — Mining/Factory",
        "Примечательные места — Шахта/Завод",
        "Примітні місця — Шахта/Завод",
        [
            "Material Processing",
            "Shipping Warehouse",
            "Storage Warehouse",
            "Dry Dock",
            "Assembly Line",
            "Metal Refinery",
            "Air Scrubber",
            "Water Reclamation",
            "Sleeping Pods",
            "Cafeteria",
            "Showers/Soakers",
            "Corp. Conference Room",
            "Garage/Hangar",
            "Geology Lab",
            "Records/Maps/Blueprints",
            "Slickscreen",
            "Fighting Ring",
            "Android Maintenance",
        ],
        [
            "Conjugal Trailers",
            "Xenobio Lab",
            "Extraction Point",
            "Infraction Cells",
            "Cloning Facility",
            "Communications",
            "Exosuit Hangar/Repair",
            "Life Support",
            "Laser Drilling Array",
            "Company Store",
        ],
    ),
    (
        338, "🔬",
        "Noteworthy Locations — Corporate/Research",
        "Примечательные места — Корпоративная станция",
        "Примітні місця — Корпоративна станція",
        [
            "Offices",
            "Open Floor Plan Office",
            "Cubicles",
            "Testing Lab",
            "AI Computer Banks",
            "Laboratory",
            "Quarantine Room",
            "Data Analysis Office",
            "Android Storage",
            "Warehouse",
            "Shipping & Receiving",
            "Mail Rooms",
            "Meeting Rooms",
            "Clean Room",
            "Employee Housing",
            "Hazardous Materials",
            "Cryostorage",
            "Containment Lab",
        ],
        [
            "Private Offices",
            "Luxurious Boardroom",
            "High Security Vault",
            "Illegal DNA Splicing Lab",
            "Embryonic Storage",
            "Morgue",
            "Animal Testing Pens",
            "Killteam Barracks",
            "Experiment #237",
            "Mega-AI Brain",
        ],
    ),
    (
        339, "🔒",
        "Noteworthy Locations — Prison",
        "Примечательные места — Тюрьма",
        "Примітні місця — Тюрма",
        [
            "Ruined Cellblock",
            "Administration Offices",
            "Morgue",
            "Riot Armory",
            "Guard Quarters",
            "High Security Area",
            "Isolation Chambers",
            "Cryostorage",
            "VR Exercise Yard",
            "Prison Cells",
            "Group Dormitory",
            "Quarantine Unit",
            "Solitary Confinement",
            "Canteen",
            "Gruel Kitchen",
            "Labor Camp",
            "Execution Chambers",
            "Scrap Metal Workshop",
        ],
        [
            "Slickscreen Classrooms",
            "Illegal Human Testing",
            "Mind Wipe Lab",
            "Mass Grave",
            "Reprogramming Facility",
            "Military Black Site",
            "AI Prison Server",
            "Android Scrapyard",
            "Commissary",
            "Crematorium",
        ],
    ),
    (
        340, "⛪",
        "Noteworthy Locations — Religious",
        "Примечательные места — Религиозная станция",
        "Примітні місця — Релігійна станція",
        [
            "Prayer Gardens",
            "Observatory",
            "Cellarium",
            "Chapter House",
            "Dorter",
            "Refectory",
            "Infirmary",
            "Kitchens",
            "Lavatorium",
            "Misericord",
            "Scriptorium",
            "Calefactory",
            "Musalla",
            "Minaret",
            "Prayer Hall",
            "Ablution Fountains",
            "Chinjusha",
            "Three Gate",
        ],
        [
            "Bell Tower",
            "Shrine",
            "Lecture Hall",
            "Grand Reliquary",
            "Massive Statue",
            "Secret Chambers",
            "Palatial Gardens",
            "Scourging Room",
            "Bishop's Manor",
            "Unmarked Prison Cell",
        ],
    ),
]


def _upsert_table(conn: sqlite3.Connection, cid: int, icon: str,
                  name_en: str, name_ru: str, name_ua: str,
                  groups: list[str], singles: list[str],
                  page_id: int, sort_order: int) -> None:
    entries_en = _e(groups, singles)
    dice_json = json.dumps({"die": "d100", "entries": entries_en}, ensure_ascii=False)

    conn.execute(
        "INSERT OR IGNORE INTO contents (id, icon, dice, source_slug) VALUES (?, ?, ?, 'apof')",
        (cid, icon, dice_json),
    )
    conn.execute(
        "UPDATE contents SET icon=?, dice=? WHERE id=?",
        (icon, dice_json, cid),
    )

    for lang, name in [("en", name_en), ("ru", name_ru), ("ua", name_ua)]:
        de_json = json.dumps(entries_en, ensure_ascii=False)  # EN entries as placeholder for all langs
        conn.execute(
            """INSERT INTO content_i18n (content_id, lang, name, dice_entries)
               VALUES (?, ?, ?, ?)
               ON CONFLICT (content_id, lang) DO UPDATE
               SET name=excluded.name, dice_entries=excluded.dice_entries""",
            (cid, lang, name, de_json),
        )

    conn.execute(
        "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (?, ?, ?)",
        (page_id, cid, sort_order),
    )
    conn.execute(
        "UPDATE page_contents SET sort_order=? WHERE page_id=? AND content_id=?",
        (sort_order, page_id, cid),
    )


def _seed(conn: sqlite3.Connection) -> None:
    # Remove old content_links for C328 (combined table)
    conn.execute("DELETE FROM content_links WHERE from_content_id=328")

    # Upsert all 8 tables
    for i, (cid, icon, name_en, name_ru, name_ua, groups, singles) in enumerate(TABLES):
        _upsert_table(conn, cid, icon, name_en, name_ru, name_ua,
                      groups, singles, page_id=38, sort_order=14 + i)

    # Content links: all 8 tables → Space Station Structure and Issues
    for cid, *_ in TABLES:
        conn.execute(
            """INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key, sort_order)
               VALUES (?, 305, 'related', 0)""",
            (cid,),
        )
        conn.execute(
            """INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key, sort_order)
               VALUES (?, 306, 'related', 1)""",
            (cid,),
        )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(
            "Done — C328 repurposed as Refuel/Repair; "
            "C334–C340 (Port/Market, Colony/Habitat, Military, "
            "Mining/Factory, Corporate/Research, Prison, Religious) created. "
            "16 content links added."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
