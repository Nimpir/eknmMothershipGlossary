"""
scripts/add_content_links.py
Insert cross-reference content_links discovered from body text and dice entries.
Safe to re-run (INSERT OR IGNORE).
"""

import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")

# (from_content_id, to_content_id, label_key)
LINKS = [
    # ── Cover → Armor rule ────────────────────────────────────────────────────
    (29, 28, "related"),   # Cover → Armor

    # ── Wound tables → Death Table (C36) ─────────────────────────────────────
    # dice entries reference "Death Save"
    (27, 36, "related"),   # Damage → Death Table
    (31, 36, "see_also"),  # Wounds—Blunt Force → Death Table
    (32, 36, "see_also"),  # Wounds—Bleeding → Death Table
    (33, 36, "see_also"),  # Wounds—Gunshot → Death Table
    (34, 36, "see_also"),  # Wounds—Fire & Explosives → Death Table
    (35, 36, "see_also"),  # Wounds—Gore & Massive → Death Table

    # ── Wound tables → Bleeding condition (C151) ──────────────────────────────
    # dice entries reference "Bleeding +N"
    (32, 151, "related"),  # Wounds—Bleeding → Bleeding condition
    (33, 151, "related"),  # Wounds—Gunshot → Bleeding condition
    (35, 151, "related"),  # Wounds—Gore & Massive → Bleeding condition

    # ── Survival hazards → Death Table ────────────────────────────────────────
    (154, 36, "related"),  # Oxygen → Death Table
    (156, 36, "related"),  # Stimpak Overdose → Death Table

    # ── Core Rules → Stress (C103) ────────────────────────────────────────────
    # body text: "gain 1 Stress"
    (100, 103, "related"),  # Stat Checks → Stress
    (101, 103, "related"),  # Saves → Stress
    (26,  103, "related"),  # How Do I Attack? → Stress

    # ── Core Rules → Panic Checks (C104) ──────────────────────────────────────
    # body text: "must make a Panic Check" on Critical Failure
    (102, 104, "related"),  # Advantage & Disadvantage → Panic Checks

    # ── Survival / Combat → Saves (C101) ──────────────────────────────────────
    # body text references Body Save / Fear Save
    (24,  101, "related"),  # Surprise → Saves
    (150, 101, "related"),  # Atmospheres → Saves
    (153, 101, "related"),  # Food & Water → Saves
    (154, 101, "related"),  # Oxygen → Saves
    (155, 101, "related"),  # Radiation → Saves
    (157, 101, "related"),  # Temperature → Saves
    (158, 101, "related"),  # Short-Term Recovery → Saves

    # ── Medical Care ──────────────────────────────────────────────────────────
    (159, 105, "related"),  # Long-Term Recovery → Conditions
    (159, 160, "see_also"), # Long-Term Recovery → AWC
    (159, 161, "see_also"), # Long-Term Recovery → Cognitive Defrag
    (159, 162, "see_also"), # Long-Term Recovery → Massage
    (159, 163, "see_also"), # Long-Term Recovery → Slicksim Therapy
    (159, 164, "see_also"), # Long-Term Recovery → Medpod
    (159, 165, "see_also"), # Long-Term Recovery → Pseudoflesh Injection
    (159, 166, "see_also"), # Long-Term Recovery → Psychosurgery
    (161, 105, "related"),  # Cognitive Defrag → Conditions
    (164, 30,  "related"),  # Medpod → What Are Wounds?
    (165, 30,  "related"),  # Pseudoflesh Injection → What Are Wounds?

    # ── Stimpak references ────────────────────────────────────────────────────
    (152, 98, "related"),   # Cryosickness → Stimpak
    (156, 98, "related"),   # Stimpak Overdose → Stimpak

    # ── Radiation ↔ Hazard Suit ───────────────────────────────────────────────
    (155, 43, "related"),   # Radiation → Hazard Suit

    # ── Stress → Shore Leave ──────────────────────────────────────────────────
    (103, 168, "related"),  # Stress → Shore Leave

    # ── Classes → mechanics ───────────────────────────────────────────────────
    (47, 101, "related"),   # Marine → Saves (Fear Save in Trauma Response)
    (47, 104, "related"),   # Marine → Panic Checks
    (47, 119, "related"),   # Marine → Military Training (starting skill)
    (47, 121, "related"),   # Marine → Athletics (starting skill)
    (48, 101, "related"),   # Android → Saves (Fear Saves in Trauma Response)
    (48, 106, "related"),   # Android → Linguistics (starting skill)
    (48, 113, "related"),   # Android → Computers (starting skill)
    (48, 115, "related"),   # Android → Mathematics (starting skill)
    (49, 101, "related"),   # Scientist → Saves (Sanity Save in Trauma Response)
    (49, 103, "related"),   # Scientist → Stress
    (50, 104, "related"),   # Teamster → Panic Checks
    (50, 110, "related"),   # Teamster → Industrial Equipment (starting skill)
    (50, 114, "related"),   # Teamster → Zero-G (starting skill)

    # ── Character Creation → Stress ───────────────────────────────────────────
    (46, 103, "related"),   # Character Creation → Stress (step 5)

    # ── Equipment → mechanics ─────────────────────────────────────────────────
    (58,  101, "related"),  # Automed → Saves (Body Saves)
    (58,  158, "related"),  # Automed → Short-Term Recovery
    (67,  30,  "related"),  # Exoloader → What Are Wounds?
    (68,  101, "related"),  # Explosives → Saves (Body Save)
    (68,  34,  "related"),  # Explosives → Wounds—Fire & Explosives
    (68,  91,  "related"),  # Explosives detonator → Radio Jammer
    (69,  151, "related"),  # First Aid Kit → Bleeding
    (72,  155, "related"),  # Geiger Counter → Radiation
    (82,  157, "related"),  # Mylar Blanket → Temperature
    (83,  42,  "related"),  # Oxygen Tank → Vaccsuit
    (83,  154, "related"),  # Oxygen Tank → Oxygen
    (85,  42,  "related"),  # Patch Kit → Vaccsuit
    (87,  103, "related"),  # Pet (Organic) → Stress
    (87,  104, "related"),  # Pet (Organic) → Panic Checks
    (88,  101, "related"),  # Pet (Synthetic) → Saves
    (88,  103, "related"),  # Pet (Synthetic) → Stress
    (90,  155, "related"),  # Radiation Pills → Radiation
    (92,  150, "related"),  # Rebreather → Atmospheres
    (98,  103, "related"),  # Stimpak → Stress
    (98,  152, "related"),  # Stimpak → Cryosickness (forward)
    (98,  156, "see_also"), # Stimpak → Stimpak Overdose
    (98,  36,  "related"),  # Stimpak → Death Table (overdose Death Save)

    # ── Shore Leave / Contractors ─────────────────────────────────────────────
    (167, 168, "see_also"), # Port Classes ↔ Shore Leave
    (168, 167, "see_also"), # Shore Leave ↔ Port Classes
    (168, 101, "related"),  # Shore Leave → Saves (Sanity Save)
    (168, 103, "related"),  # Shore Leave → Stress
    (168, 104, "related"),  # Shore Leave → Panic Checks
    (169, 30,  "related"),  # Contractor Stats → What Are Wounds?
    (170, 169, "related"),  # Hiring Contractors → Contractor Stats
    (171, 169, "related"),  # Contractors Table → Contractor Stats
    (171, 170, "related"),  # Contractors Table → Hiring Contractors

    # ── Radio Jammer cross-links ──────────────────────────────────────────────
    (66,  91,  "related"),  # Emergency Beacon → Radio Jammer
    (91,  66,  "related"),  # Radio Jammer → Emergency Beacon
    (91,  96,  "related"),  # Radio Jammer → Short-range Comms
    (96,  91,  "related"),  # Short-range Comms → Radio Jammer

    # ── HUD → Smart-link ──────────────────────────────────────────────────────
    (73,  97,  "related"),  # HUD → Smart-link Add-On
]


def run(db_path: str) -> None:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    inserted = 0
    skipped = 0
    try:
        for from_id, to_id, label in LINKS:
            cur = conn.execute(
                "INSERT OR IGNORE INTO content_links"
                " (from_content_id, to_content_id, label_key, sort_order)"
                " VALUES (?, ?, ?, 0)",
                (from_id, to_id, label),
            )
            if cur.rowcount:
                inserted += 1
            else:
                skipped += 1
        conn.commit()
        print(f"Done — {inserted} links inserted, {skipped} already existed.")
    finally:
        conn.close()


if __name__ == "__main__":
    run(DB_PATH)
