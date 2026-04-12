"""
scripts/add_wom_part6_links.py
Add content_links for all WOM contents (C172-C206) — both new→existing and new→new.
Run: python scripts/add_wom_part6_links.py
"""
import os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# (from_id, to_id, label_key)
LINKS = [
    # ── P24 Session Prep ─────────────────────────────────────────────────────
    # C172 Starting Scenarios → C173 Setting Table (see_also: when you roll a scenario, also roll setting)
    (172, 173, "see_also"),
    # C172 Starting Scenarios → C174 Something to Survive (see_also: parts of a session)
    (172, 174, "see_also"),
    # C172 Starting Scenarios → C175 Something to Solve (see_also)
    (172, 175, "see_also"),
    # C172 Starting Scenarios → C176 Someone to Save (see_also)
    (172, 176, "see_also"),
    # C174 Something to Survive → C36 Death Table (related: survive means avoiding death)
    (174, 36, "related"),
    # C175 Something to Solve → C189 Running Investigations (related)
    (175, 189, "related"),
    # C177 Tactical Considerations → C188 Violent Encounters (related)
    (177, 188, "related"),
    # C178 Map It Out → C199 Planets (related: map uses planet generation)
    (178, 199, "related"),
    # C178 Map It Out → C200 Settlement Locale (related)
    (178, 200, "related"),

    # ── P25 The Horror ────────────────────────────────────────────────────────
    # C179 Random Horrors → C103 Stress (related: encountering horrors causes stress)
    (179, 103, "related"),
    # C179 Random Horrors → C104 Panic Checks (related)
    (179, 104, "related"),
    # C180 Horror Themes → C179 Random Horrors (related)
    (180, 179, "related"),
    # C181 The TOMBS Cycle → C179 Random Horrors (related: TOMBS is the framework for horrors)
    (181, 179, "related"),
    # C182 Puzzle Components → C181 The TOMBS Cycle (related: puzzles are part of TOMBS)
    (182, 181, "related"),

    # ── P26 Running the Game ──────────────────────────────────────────────────
    # C183 How the Game Works → C100 Stat Checks (related)
    (183, 100, "related"),
    # C183 How the Game Works → C101 Saves (related)
    (183, 101, "related"),
    # C184 Setting the Stakes → C183 How the Game Works (related)
    (184, 183, "related"),
    # C185 Interpreting Failure → C183 How the Game Works (related)
    (185, 183, "related"),
    # C185 Interpreting Failure → C103 Stress (related: failure causes stress)
    (185, 103, "related"),
    # C186 Difficulty Settings → C100 Stat Checks (related)
    (186, 100, "related"),
    # C186 Difficulty Settings → C102 Advantage & Disadvantage (related)
    (186, 102, "related"),
    # C187 Social Encounters → C184 Setting the Stakes (related)
    (187, 184, "related"),
    # C188 Violent Encounters → C23 Turn Order (related)
    (188, 23, "related"),
    # C188 Violent Encounters → C184 Setting the Stakes (related)
    (188, 184, "related"),
    # C188 Violent Encounters → C30 What Are Wounds? (related)
    (188, 30, "related"),
    # C189 Running Investigations → C185 Interpreting Failure (related)
    (189, 185, "related"),
    # C190 Ship-to-Ship Combat → C188 Violent Encounters (related)
    (190, 188, "related"),
    # C190 Ship-to-Ship Combat → C23 Turn Order (related)
    (190, 23, "related"),

    # ── P27 Campaign Building ─────────────────────────────────────────────────
    # C191 Campaign Style → C192 Campaign Frames (related: style + frame together define campaign)
    (191, 192, "related"),
    # C193 The Company → C194 How to Create Factions (related: Company is a faction)
    (193, 194, "related"),
    # C194 How to Create Factions → C203 Factions Table (see_also: roll to find factions)
    (194, 203, "see_also"),
    # C195 Contract Work → C196 Pay Scale (related: roll contract then check pay)
    (195, 196, "related"),
    # C195 Contract Work → C168 Shore Leave (related: jobs lead to shore leave)
    (195, 168, "related"),
    # C196 Pay Scale → C168 Shore Leave (related: payday enables shore leave)
    (196, 168, "related"),
    # C196 Pay Scale → C169 Contractor Stats (related: payday allows hiring contractors)
    (196, 169, "related"),
    # C197 Campaign Economics → C196 Pay Scale (related)
    (197, 196, "related"),
    # C197 Campaign Economics → C167 Port Classes (related: port class affects costs)
    (197, 167, "related"),
    # C198 Ending Your Campaign → C168 Shore Leave (related: final sessions include shore leave)
    (198, 168, "related"),
    # C198 Ending Your Campaign → C103 Stress (related: ending involves stress management)
    (198, 103, "related"),

    # ── P28 Random Generators ─────────────────────────────────────────────────
    # C199 Planets → C200 Settlement Locale (see_also: combined for world-building)
    (199, 200, "see_also"),
    # C199 Planets → C150 Atmospheres (related: atmosphere type affects survival)
    (199, 150, "related"),
    # C200 Settlement Locale → C201 Control Faction (see_also)
    (200, 201, "see_also"),
    # C200 Settlement Locale → C202 Population (see_also)
    (200, 202, "see_also"),
    # C200 Settlement Locale → C205 Settlements (see_also)
    (200, 205, "see_also"),
    # C201 Control Faction → C203 Factions Table (related: control faction → roll specific faction)
    (201, 203, "related"),
    # C202 Population → C205 Settlements (related)
    (202, 205, "related"),
    # C203 Factions Table → C194 How to Create Factions (related)
    (203, 194, "related"),
    # C204 Port Class → C167 Port Classes (related: same subject, player-facing vs warden-facing)
    (204, 167, "related"),
    # C204 Port Class → C168 Shore Leave (related)
    (204, 168, "related"),
    # C205 Settlements → C199 Planets (related: settlement is on a planet)
    (205, 199, "related"),
    # C205 Settlements → C204 Port Class (related)
    (205, 204, "related"),
    # C206 Random Lore → C179 Random Horrors (related: lore inspires horror scenarios)
    (206, 179, "related"),
    # C206 Random Lore → C180 Horror Themes (related)
    (206, 180, "related"),
]


def _seed(conn: sqlite3.Connection) -> None:
    inserted = 0
    for from_id, to_id, label in LINKS:
        conn.execute("""
            INSERT OR IGNORE INTO content_links (from_content_id, to_content_id, label_key)
            VALUES (?, ?, ?)
        """, (from_id, to_id, label))
        inserted += conn.execute(
            "SELECT changes()"
        ).fetchone()[0]
    print(f"  Inserted {inserted} new link(s) (skipped {len(LINKS) - inserted} already existing).")


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(LINKS)} content_links processed for WOM contents.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
