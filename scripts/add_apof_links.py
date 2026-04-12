"""
scripts/add_apof_links.py
A Pound of Flesh — content_links between new APoF items and cross-links to
existing PSG items. Run after all other add_apof_*.py scripts.
Run: python scripts/add_apof_links.py
"""
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# (from_id, to_id, label_key)
LINKS = [
    # ── Cross-module links to existing PSG content ────────────────────────────
    # Cybermods → PSG Skills (Surgery, Jury Rigging, Engineering, Hacking)
    (254, 106, "related"),   # Install Rules → First Aid (C106 Trained Skills area)
    (257, 148, "related"),   # Overclocking → Skill Training
    (258, 148, "related"),   # Reaping → Skill Training

    # APoF weapons map to P2 weapons
    (263, 41, "related"),    # Cloakskin → Armour (P6 C41)
    (285, 57, "related"),    # Terminal Jack → Equipment (P10)

    # ── Internal APoF links ───────────────────────────────────────────────────
    # P32 Dream overview → P33 NPCs
    (212, 218, "see_also"),  # Station Overview → Angus
    (212, 219, "see_also"),  # Station Overview → Reidmar
    (212, 220, "see_also"),  # Station Overview → Yandee
    (212, 221, "see_also"),  # Station Overview → Brunhildh
    (212, 222, "see_also"),  # Station Overview → Cutter
    (212, 223, "see_also"),  # Station Overview → Ukko/Ukka

    # Storylines → relevant NPCs
    (225, 218, "related"),   # Teamster Strike → Angus
    (225, 219, "related"),   # Teamster Strike → Reidmar
    (226, 218, "related"),   # Unrest in The Choke → Angus
    (227, 218, "related"),   # ACMD Outbreak → Angus
    (227, 222, "related"),   # ACMD Outbreak → Cutter

    # Storylines → locations
    (226, 245, "related"),   # Unrest → Doptown
    (227, 249, "related"),   # ACMD Outbreak → Life Support 01

    # Locations → relevant NPCs
    (232, 221, "related"),   # Chop Shop → Brunhildh (she runs trials)
    (240, 221, "related"),   # The Court → Brunhildh
    (242, 222, "related"),   # Tempest HQ → Cutter
    (237, 218, "related"),   # CANYONHEAVY → Angus

    # Locations → each other
    (245, 247, "see_also"),  # Doptown → The Choke
    (248, 247, "see_also"),  # The Sink → The Choke
    (249, 247, "see_also"),  # Life Support 01 → The Choke
    (250, 248, "related"),   # The Burrows → The Sink
    (251, 250, "related"),   # Caliban's Heart → The Burrows
    (251, 249, "related"),   # Caliban's Heart → Life Support 01

    # Chokespawn and encounters link to locations
    (252, 247, "related"),   # Chokespawn → The Choke
    (253, 247, "related"),   # Choke Encounters → The Choke
    (253, 248, "related"),   # Choke Encounters → The Sink
    (246, 245, "related"),   # Doptown Encounters → Doptown

    # Cybermods inter-links (requires chains)
    (260, 279, "related"),   # Black Box → Slicksocket
    (261, 279, "related"),   # Cloakskin → (no hard req but Slicksocket flavour)
    (265, 271, "related"),   # Holoprojector → OGRE
    (267, 271, "related"),   # Huntershot → OGRE
    (275, 260, "related"),   # Remote Uplink → Black Box
    (276, 274, "related"),   # Nanoblade → Prosthetic
    (277, 260, "related"),   # Revenant Protocol → Black Box
    (281, 282, "related"),   # Spider Mount → Spinal Rig
    (284, 279, "related"),   # Tattletale → Slicksocket

    # Slickware inter-links
    (287, 285, "related"),   # God Mode → Terminal Jack
    (287, 279, "related"),   # God Mode → Slicksocket
    (289, 265, "related"),   # Holopet → Holoprojector
    (290, 269, "related"),   # Looky-loo → Loudmouth
    (291, 260, "related"),   # Machine Code → Black Box
    (291, 285, "related"),   # Machine Code → Terminal Jack
    (293, 271, "related"),   # Skillslick → OGRE
    (295, 269, "related"),   # Vox Box → Loudmouth

    # Cybermod rules → cyberware/slickware pages
    (254, 255, "see_also"),  # Install Rules → Malfunctions
    (254, 256, "see_also"),  # Install Rules → Panic Table
    (254, 257, "see_also"),  # Install Rules → Overclocking
    (254, 258, "see_also"),  # Install Rules → Reaping

    # Tables → relevant game content
    (297, 252, "related"),   # Deadly Encounters → Chokespawn
    (298, 297, "see_also"),  # Station Encounters → Deadly Encounters
    (296, 297, "see_also"),  # Encounter Freq → Deadly Encounters
    (296, 298, "see_also"),  # Encounter Freq → Station Encounters
    (302, 304, "see_also"),  # Corespace Gen → Crisis Table
    (303, 304, "see_also"),  # Rimspace Gen → Crisis Table
    (302, 305, "see_also"),  # Corespace Gen → Structure Table
    (303, 305, "see_also"),  # Rimspace Gen → Structure Table
]


def _seed(conn: sqlite3.Connection) -> None:
    for from_id, to_id, label in LINKS:
        conn.execute("""
            INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key)
            VALUES (?, ?, ?)
        """, (from_id, to_id, label))


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(LINKS)} content links added.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
