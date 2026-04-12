"""
scripts/add_rimspace_generator_page.py
Restructures the Rimspace Station Generator:

- Deletes C303 (plain-text generator card)
- Creates P53 "Rimspace Station Generator" with intro desc and Roll All workflow
- Creates C320 Rim Landmark, C321 Station, C322 Call-Sign,
  C323 Control, C324 Rival, C325 Rival Leader — each a d10 dice table on P53
- Adds P53 to P38 linked_pages
- RU/UA dice entries use EN text as placeholder (no source translations exist)

Run: python scripts/add_rimspace_generator_page.py
"""
import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

# ── P53 page i18n ─────────────────────────────────────────────────────────────
PAGE_53 = {
    "icon": "🌌",
    "source_slug": "apof",
    "workflow_steps": [320, 321, 322, 323, 324, 325],
    "i18n": {
        "en": {
            "name": "Rimspace Station Generator",
            "desc": (
                "Near a(n) [RIM LANDMARK], a(n) [STATION NAME] station "
                "(call-sign [CALL-SIGN]) spins. "
                "Controlled by [CONTROL FACTION], undermined by [RIVAL FACTION] "
                "led by a(n) [RIVAL LEADER]. "
                "20% chance of a [CRISIS]. "
                "Otherwise: fuel as normal, only [GOODS] for sale, "
                "station in dire need of [RESOURCE]."
            ),
        },
        "ru": {
            "name": "Генератор станций Края",
            "desc": (
                "У [ОРИЕНТИРА КРАЯ] вращается станция [НАЗВАНИЕ] "
                "(позывной [ПОЗЫВНОЙ]). "
                "Контролируется [ФРАКЦИЕЙ], подрывается [СОПЕРНИКОМ] "
                "под руководством [ЛИДЕРА СОПЕРНИКА]. "
                "20% шанс [КРИЗИСА]. "
                "Иначе: топливо как обычно, продаётся только [ТОВАР], "
                "острая нужда в [РЕСУРСЕ]."
            ),
        },
        "ua": {
            "name": "Генератор станцій Краю",
            "desc": (
                "Біля [ОРІЄНТИРА КРАЮ] обертається станція [НАЗВА] "
                "(позивний [ПОЗИВНИЙ]). "
                "Контролюється [ФРАКЦІЄЮ], підривається [СУПЕРНИКОМ] "
                "під керівництвом [ЛІДЕРА СУПЕРНИКА]. "
                "20% шанс [КРИЗИ]. "
                "Інакше: пальне як зазвичай, продається лише [ТОВАР], "
                "гостра потреба в [РЕСУРСІ]."
            ),
        },
    },
}

# ── 6 dice tables (id, icon, {lang: name}, entries list) ─────────────────────
# RU/UA dice entries fall back to EN (no source translations available).
_EN_TABLES = {
    "rim_landmark": [
        "Heavily Guarded Corporate DMZ",
        "Battered Asteroid Field",
        "Uninhabitable Desert Planet",
        "Strip-Mined Ice World",
        "First Generation Pioneer Colony",
        "Resource Rich Asteroid Cluster",
        "Disputed Territory Border",
        "Massive Jump-5 Derelict Hulk",
        "Burgeoning Off-World Colony",
        "Ship Graveyard",
    ],
    "station": [
        "Independent Colony",
        "Run Down Factory",
        "Military Base",
        "Lighthouse",
        "Asteroid Mining",
        "Maximum Sec. Prison",
        "Scrap Processing",
        "Rest & Refuel",
        "Black Market",
        "Abandoned Derelict",
    ],
    "call_sign": [
        "Remote Site-[d100]-[Letter]",
        "[d100]-[d10]",
        "Forward Base-[d10]-[Letter]",
        "Rimward-Post [d10]-[d10]",
        "[Letter]-[d100]",
        "Supervisor-[Letter]-[d10]",
        "Control-[d100]",
        "Command-[d10]-[d10]",
        "Outpost [d100]-[Letter]-[d10]",
        "Bridle-[d10]",
    ],
    "control": [
        "Anders-Klimt Mining Corp",
        "Gaff Android Labor Syndicate",
        "601st Colonial Marine Regiment",
        "Salo-Mercury Biomotors Inc.",
        "Apostles Gate Church",
        "Confederated Systems Inc.",
        "'Opera' Fleet of Mercenary Raiders",
        "Sindec Alloyed Metals Corp",
        "SEBACO Mining Ltd.",
        "Limited Colonial Government",
    ],
    "rival": [
        "Synthetic Liberation Front",
        "Altruistic Scientists",
        "Neo-Haram Anarchists",
        "Violent Return-Earthers",
        "Carter Tactical Concerns Ltd.",
        "Armadyne Weapons Inc.",
        "House Sivaranjan",
        "Secret Union Instigators",
        "Black Dawn Mercenaries",
        "Family of Eleven",
    ],
    "rival_leader": [
        "Renegade Android",
        "Powerful Rogue AI",
        "Ruthless Criminal Despot",
        "Charismatic Revivalist",
        "Perverse Corp. Warden",
        "Highly Intelligent Merc. Captain",
        "Cunning Corporate Spy",
        "Merciless Slaver",
        "Stalwart Union Organizer",
        "Relentless Warrant Officer",
    ],
}

DICE_TABLES = [
    (
        320, "🏔️",
        {"en": "Rim Landmark", "ru": "Ориентир Края", "ua": "Орієнтир Краю"},
        _EN_TABLES["rim_landmark"],
    ),
    (
        321, "🏠",
        {"en": "Station", "ru": "Станция", "ua": "Станція"},
        _EN_TABLES["station"],
    ),
    (
        322, "📡",
        {"en": "Call-Sign", "ru": "Позывной", "ua": "Позивний"},
        _EN_TABLES["call_sign"],
    ),
    (
        323, "🎯",
        {"en": "Control Faction", "ru": "Фракция контроля", "ua": "Фракція контролю"},
        _EN_TABLES["control"],
    ),
    (
        324, "⚔️",
        {"en": "Rival Faction", "ru": "Фракция-соперник", "ua": "Фракція-суперник"},
        _EN_TABLES["rival"],
    ),
    (
        325, "👑",
        {"en": "Rival Leader", "ru": "Лидер соперника", "ua": "Лідер суперника"},
        _EN_TABLES["rival_leader"],
    ),
]


def _entries(texts: list[str]) -> list[dict]:
    return [{"min": i + 1, "max": i + 1, "text": t} for i, t in enumerate(texts)]


def _seed(conn: sqlite3.Connection) -> None:
    # 1. Delete C303 (cascades content_i18n and page_contents)
    conn.execute("DELETE FROM contents WHERE id = 303")

    # 2. Create P53
    conn.execute(
        """INSERT OR IGNORE INTO pages (id, icon, source_slug, linked_pages, workflow_steps)
           VALUES (53, ?, ?, '[]', ?)""",
        (
            PAGE_53["icon"],
            PAGE_53["source_slug"],
            json.dumps(PAGE_53["workflow_steps"]),
        ),
    )
    conn.execute(
        "UPDATE pages SET workflow_steps = ? WHERE id = 53",
        (json.dumps(PAGE_53["workflow_steps"]),),
    )
    for lang, strings in PAGE_53["i18n"].items():
        conn.execute(
            """INSERT INTO page_i18n (page_id, lang, name, desc) VALUES (53, ?, ?, ?)
               ON CONFLICT (page_id, lang) DO UPDATE SET name=excluded.name, desc=excluded.desc""",
            (lang, strings["name"], strings["desc"]),
        )

    # 3. Add P53 to P38 linked_pages
    row = conn.execute("SELECT linked_pages FROM pages WHERE id = 38").fetchone()
    lp: list = json.loads(row[0]) if row and row[0] else []
    if 53 not in lp:
        lp.append(53)
        conn.execute(
            "UPDATE pages SET linked_pages = ? WHERE id = 38",
            (json.dumps(lp),),
        )

    # 4. Create C320–C325 and place on P53
    for sort, (cid, icon, names, en_texts) in enumerate(DICE_TABLES, start=1):
        en_entries = _entries(en_texts)
        dice_json = json.dumps({"die": "d10", "entries": en_entries}, ensure_ascii=False)

        conn.execute(
            "INSERT OR IGNORE INTO contents (id, icon, dice, source_slug) VALUES (?, ?, ?, 'apof')",
            (cid, icon, dice_json),
        )
        conn.execute(
            "UPDATE contents SET icon = ?, dice = ? WHERE id = ?",
            (icon, dice_json, cid),
        )

        for lang, name in names.items():
            # RU/UA use EN entries as placeholder
            de_json = json.dumps(en_entries, ensure_ascii=False)
            conn.execute(
                """INSERT INTO content_i18n (content_id, lang, name, dice_entries)
                   VALUES (?, ?, ?, ?)
                   ON CONFLICT (content_id, lang) DO UPDATE
                   SET name=excluded.name, dice_entries=excluded.dice_entries""",
                (cid, lang, name, de_json),
            )

        conn.execute(
            "INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order) VALUES (53, ?, ?)",
            (cid, sort),
        )


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(
            "Done — C303 deleted, P53 created with workflow, "
            "C320–C325 (Rim Landmark, Station, Call-Sign, "
            "Control Faction, Rival Faction, Rival Leader) added."
        )
    finally:
        conn.close()


if __name__ == "__main__":
    run()
