"""
scripts/update_space_station_structure_images.py
Attach image paths to each dice entry in C305 Space Station Structure.
Images: images/A Pound of Flesh/Space Station Structure/1.png (roll 0) … 10.png (roll 9).
Run: python scripts/update_space_station_structure_images.py
"""
import json, os, sqlite3
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "mothership.db")

CONTENT_ID = 305

# roll value → image filename (1-based filename, 0-based roll)
IMAGE_MAP = {
    0: "images/A Pound of Flesh/Space Station Structure/1.png",   # Asteroid Surface
    1: "images/A Pound of Flesh/Space Station Structure/2.png",   # Asteroid Interior
    2: "images/A Pound of Flesh/Space Station Structure/3.png",   # Spindle
    3: "images/A Pound of Flesh/Space Station Structure/4.png",   # Cylinder
    4: "images/A Pound of Flesh/Space Station Structure/5.png",   # Sphere
    5: "images/A Pound of Flesh/Space Station Structure/6.png",   # Torus/Ring
    6: "images/A Pound of Flesh/Space Station Structure/7.png",   # Tower
    7: "images/A Pound of Flesh/Space Station Structure/8.png",   # Modular
    8: "images/A Pound of Flesh/Space Station Structure/9.png",   # Platform
    9: "images/A Pound of Flesh/Space Station Structure/10.png",  # Amalgamation
}


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        print("Done — C305 Space Station Structure: image paths added to all 10 entries.")
    finally:
        conn.close()


def _seed(conn: sqlite3.Connection) -> None:
    row = conn.execute("SELECT dice FROM contents WHERE id = ?", (CONTENT_ID,)).fetchone()
    if not row or not row[0]:
        raise RuntimeError(f"C{CONTENT_ID} not found or has no dice JSON")

    dice = json.loads(row[0])
    for entry in dice["entries"]:
        roll = entry["min"]
        if roll in IMAGE_MAP:
            entry["image"] = IMAGE_MAP[roll]

    conn.execute(
        "UPDATE contents SET dice = ? WHERE id = ?",
        (json.dumps(dice), CONTENT_ID),
    )


if __name__ == "__main__":
    run()
