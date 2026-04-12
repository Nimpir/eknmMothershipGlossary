"""
scripts/verify_rebuild.py
Build a fresh DB from all migration scripts and compare its SHA-256 table
hashes against the current (live) DB.  The live DB is the source of truth.

Algorithm per table:
  1. SELECT * ORDER BY all columns → deterministic row order
  2. str(rows) → SHA-256  →  single hex digest per table
  3. Compare digest: live vs rebuilt

Usage:
    python scripts/verify_rebuild.py

The script never touches the live DB — it writes to a temp file and
deletes it on exit.
"""
import hashlib
import os
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT     = Path(__file__).resolve().parent.parent
LIVE_DB  = os.getenv("DB_PATH", str(ROOT / "mothership.db"))
SCHEMA   = ROOT / "schema.sql"

TABLES = [
    "sources",
    "pages",
    "page_i18n",
    "contents",
    "content_i18n",
    "page_contents",
    "content_links",
]

# ── Migration script execution order ─────────────────────────────────────────
# Superseded scripts (update_p38_move_c307_delete_p50,
# update_p50_move_desc_to_c307, update_p50_merge_denizen_tables) are excluded
# because update_apof_denizens_split now handles their work inline.
# update_marine_loadout_links.py: runs before update_loadout_links_missed.py to delete
# the 15 C51 content_links; missed.py then overwrites the dice JSON with the full version.
SCRIPTS = [
    # Bootstrap: creates P1 (root nav page) — assumed to exist by all other scripts
    "../seed.py",
    # PSW content
    "add_character_page.py",
    "add_psw_character.py",
    "add_psw_rules.py",            # creates P11/P12 — must run before add_psw_skills.py
    "add_psw_skills.py",           # adds P13 to P11; needs P11 to already exist
    "add_psw_tables.py",
    "add_psw_equipment.py",
    "add_psw_survival.py",
    "add_psw_medical.py",
    "add_psw_downtime.py",
    "add_psw_combat.py",
    "add_psw_weapons.py",          # needs combat (C28)
    "add_psw_armour.py",           # needs combat (C28 for links)
    "add_psw_dice_i18n.py",        # ru/ua dice_entries for PSW tables (historical catchup)
    # PSW links & updates
    "add_content_links.py",
    "update_nav_and_descriptions.py",
    "update_remove_cyclic_links.py",
    "add_missed_links_armour_loadout.py",
    "add_missed_links_battle_dress.py",
    "update_marine_loadout_links.py",   # removes 15 C51 content_links; runs before missed so missed overwrites dice
    "update_loadout_links_c52_c54.py",
    "update_loadout_links_missed.py",
    # WOM content
    "add_wom_part1_pages.py",
    "add_wom_part2_horror.py",
    "add_wom_part3_running.py",
    "add_wom_part4_campaign.py",
    "add_wom_part5_generators.py",
    "add_wom_part6_links.py",
    "update_wom_split_tables.py",
    "add_p29_planet_p30_settlement.py",
    "update_random_horrors_split.py",
    # APOF content
    "add_apof_source_pages.py",    # must be first in APOF group
    "add_apof_cybermods.py",
    "add_apof_npcs.py",
    "add_apof_dream_storylines.py",
    "add_apof_tables.py",
    "add_apof_locations.py",
    "add_apof_deep.py",
    "add_modules_page.py",
    "update_apof_dice_format.py",  # must run before denizens split
    "add_apof_links.py",
    "add_apof_missed_tables.py",
    "update_apof_denizens_split.py",
    "fix_cybermods_subinfo.py",
    # Generator pages
    "add_corespace_generator_page.py",
    "add_rimspace_generator_page.py",
    # Space station layout
    "update_noteworthy_locations.py",      # creates/updates C328/C334-C340 on P38
    "add_noteworthy_locations_intro.py",   # removes C328-C340 from P38, creates C341 gateway
    "add_space_stations_page.py",
    "add_space_station_layout.py",         # links from C341 → C342
    "update_space_station_structure_images.py",
    # Station restructuring
    "update_station_structure.py",
    # update_p35_flatten_station.py excluded: designed for old P42-49 migration;
    # add_apof_locations.py already builds the flat P35 structure from scratch.
    "update_pages_add_image_url.py",
    "update_p35_add_deep_locations.py",
    "update_c229_remove_ships_docked_inline.py",
    "update_dry_dock_sublinking.py",
    "update_station_sublinking.py",
    "update_choke_sublinking.py",
    "update_p35_loc_images.py",
    "update_remove_station_cyclic_links.py",
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def table_hash(conn: sqlite3.Connection, table: str) -> str:
    """SHA-256 of all rows, sorted deterministically.

    page_i18n and content_i18n have a surrogate 'id' INTEGER PRIMARY KEY that is
    autoincrement and will differ between a live DB (explicit IDs from data.sql) and
    a rebuilt DB (autoincrement).  Exclude it so hashes compare semantic content only.
    """
    # Tables whose 'id' column is a surrogate key (auto-assigned, not semantically meaningful)
    EXCLUDE_ID = {"page_i18n", "content_i18n"}
    cols = [col[1] for col in conn.execute(f"PRAGMA table_info(\"{table}\")")]
    if table in EXCLUDE_ID:
        cols = [c for c in cols if c != "id"]
    col_str = ", ".join(f'"{c}"' for c in cols)
    order_str = ", ".join(f'"{c}"' for c in cols)
    rows = conn.execute(
        f"SELECT {col_str} FROM \"{table}\" ORDER BY {order_str}"
    ).fetchall()
    digest = hashlib.sha256(str(rows).encode()).hexdigest()
    return digest


def row_count(conn: sqlite3.Connection, table: str) -> int:
    return conn.execute(f"SELECT COUNT(*) FROM \"{table}\"").fetchone()[0]


def init_schema(db_path: str) -> None:
    schema = SCHEMA.read_text(encoding="utf-8")
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()


def run_script(script_name: str, db_path: str) -> tuple[bool, str]:
    """Run a migration script with DB_PATH overridden.  Returns (ok, output)."""
    env = os.environ.copy()
    env["DB_PATH"] = db_path
    script_path = (ROOT / "scripts" / script_name).resolve()
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        env=env,
    )
    ok = result.returncode == 0
    out = (result.stdout + result.stderr).strip()
    return ok, out


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    test_db = tmp.name

    try:
        print(f"Fresh DB: {test_db}")
        print(f"Live DB:  {LIVE_DB}\n")

        # 1. Schema
        print("-- Applying schema.sql ...")
        init_schema(test_db)

        # 2. Run scripts
        print(f"-- Running {len(SCRIPTS)} migration scripts ...\n")
        failed = []
        for i, script in enumerate(SCRIPTS, 1):
            ok, out = run_script(script, test_db)
            status = "OK" if ok else "FAIL"
            print(f"  [{status}] [{i:02d}/{len(SCRIPTS)}] {script}")
            if out:
                for line in out.splitlines():
                    print(f"       {line}")
            if not ok:
                failed.append(script)

        if failed:
            print(f"\nWARN: {len(failed)} script(s) failed -- comparison may be incomplete.")

        # 3. Compare hashes
        print("\n-- Comparing table hashes ...\n")
        live_conn = sqlite3.connect(LIVE_DB)
        test_conn = sqlite3.connect(test_db)

        all_match = True
        header = f"  {'Table':<18}  {'Live rows':>10}  {'Test rows':>10}  Result"
        print(header)
        print("  " + "-" * (len(header) - 2))

        for table in TABLES:
            live_h = table_hash(live_conn, table)
            test_h = table_hash(test_conn, table)
            live_n = row_count(live_conn, table)
            test_n = row_count(test_conn, table)
            match  = live_h == test_h
            if not match:
                all_match = False
            icon = "OK" if match else "MISMATCH"
            print(f"  {table:<18}  {live_n:>10}  {test_n:>10}  {icon}")

        # 4. Row-level diff for mismatched tables
        def diff_table(name: str, key_cols: list[str], val_cols: list[str]) -> None:
            cols = key_cols + val_cols
            col_str = ", ".join(f'"{c}"' for c in cols)
            live_rows = {tuple(r[:len(key_cols)]): tuple(r[len(key_cols):])
                        for r in live_conn.execute(f'SELECT {col_str} FROM "{name}"').fetchall()}
            test_rows = {tuple(r[:len(key_cols)]): tuple(r[len(key_cols):])
                        for r in test_conn.execute(f'SELECT {col_str} FROM "{name}"').fetchall()}
            diffs = [(k, live_rows[k], test_rows[k]) for k in live_rows
                    if k in test_rows and live_rows[k] != test_rows[k]]
            only_live = set(live_rows) - set(test_rows)
            only_test = set(test_rows) - set(live_rows)
            if only_live:
                print(f"  {name} only in LIVE: {sorted(only_live)}")
            if only_test:
                print(f"  {name} only in TEST: {sorted(only_test)}")
            if diffs:
                print(f"  {name} data diff ({len(diffs)} rows):")
                for k, lv, tv in diffs[:10]:
                    print(f"    key={k}  live={ascii(lv)}  test={ascii(tv)}")

        # 5. Detailed diff for mismatches
        print()
        for table in TABLES:
            live_ids = set(
                row[0] for row in live_conn.execute(f'SELECT id FROM "{table}"').fetchall()
            ) if table not in ("page_contents", "content_links") else None

            if table == "contents":
                test_ids = set(
                    row[0] for row in test_conn.execute('SELECT id FROM "contents"').fetchall()
                )
                only_live = live_ids - test_ids
                only_test = test_ids - live_ids
                if only_live:
                    names = {
                        row[0]: row[1]
                        for row in live_conn.execute(
                            "SELECT c.id, ci.name FROM contents c "
                            "JOIN content_i18n ci ON ci.content_id=c.id AND ci.lang='en' "
                            f"WHERE c.id IN ({','.join(str(i) for i in sorted(only_live))})"
                        ).fetchall()
                    }
                    print(f"  contents only in LIVE ({len(only_live)}):")
                    for cid in sorted(only_live):
                        print(f"    C{cid} {names.get(cid, '?')}")
                if only_test:
                    print(f"  contents only in TEST ({len(only_test)}): {sorted(only_test)}")

            if table == "content_links":
                live_links = set(live_conn.execute(
                    'SELECT from_content_id, to_content_id FROM content_links'
                ).fetchall())
                test_links = set(test_conn.execute(
                    'SELECT from_content_id, to_content_id FROM content_links'
                ).fetchall())
                only_live = live_links - test_links
                only_test = test_links - live_links
                if only_live:
                    print(f"  content_links only in LIVE ({len(only_live)}):")
                    for fl in sorted(only_live):
                        print(f"    C{fl[0]} -> C{fl[1]}")
                if only_test:
                    print(f"  content_links only in TEST ({len(only_test)}):")
                    for fl in sorted(only_test):
                        print(f"    C{fl[0]} -> C{fl[1]}")

        try:
            diff_table("pages",        ["id"],                    ["icon","source_slug","source_page","linked_pages","workflow_steps","image_url"])
            diff_table("page_i18n",    ["page_id","lang"],        ["name","desc"])
            diff_table("contents",     ["id"],                    ["icon","image_url","tg_file_id","subinfo_fixed","dice","source_slug","source_page","sort_order"])
            diff_table("content_i18n", ["content_id","lang"],     ["name","desc","subinfo_text","dice_entries"])
            diff_table("page_contents",["page_id","content_id"],  ["sort_order"])
        finally:
            live_conn.close()
            test_conn.close()

        print()
        if all_match:
            print("PASS: All tables match -- scripts correctly recreate the current DB.")
        else:
            print("FAIL: Mismatch(es) found -- scripts and live DB diverge.")
            sys.exit(1)

    finally:
        os.unlink(test_db)


if __name__ == "__main__":
    main()
