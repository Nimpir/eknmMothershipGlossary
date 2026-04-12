"""
scripts/update_p35_loc_images.py
Link location images to P35 content items (Prospero's Dream station locations).
Run: python scripts/update_p35_loc_images.py
"""
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

BASE = "images/A Pound of Flesh/ProsperosDreamLocs"

IMAGES = [
    (229, f"{BASE}/1.DryDock.png"),               # 01 Dry Dock
    (230, f"{BASE}/2.TheStellarBurn.png"),         # 02 The Stellar Burn
    (232, f"{BASE}/3.TheChopShop.png"),            # 03 The Chop Shop
    (233, f"{BASE}/4.TheIceBox.png"),              # 04 The Ice Box
    (235, f"{BASE}/5.TheFarm.png"),                # 05 The Farm
    (237, f"{BASE}/6.CanyonHeavyMarket.png"),      # 06 CANYONHEAVY.market
    (240, f"{BASE}/7.TheCourt.png"),               # 07 The Court
    (242, f"{BASE}/8.TempestCompanyHQ.png"),       # 08 Tempest Company HQ
    (245, f"{BASE}/9.DopTown.png"),                # 09 Doptown (merged)
    (248, f"{BASE}/10.TheSink.png"),               # The Sink
    (249, f"{BASE}/TheSinkLocs/LifeSupport.png"),  # Life Support 01
    (250, f"{BASE}/TheSinkLocs/TheBurrows.png"),   # The Burrows
    (251, f"{BASE}/TheSinkLocs/CalibansHeart.png"),# Caliban's Heart
]


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print(f"Done — {len(IMAGES)} content image_url values set.")

    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    for content_id, image_url in IMAGES:
        conn.execute(
            "UPDATE contents SET image_url = ? WHERE id = ?",
            (image_url, content_id),
        )


if __name__ == "__main__":
    run()
