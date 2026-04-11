"""
scripts/add_psw_tables.py
Seed Loadout tables (d10 per class), Trinkets (d100), and Patches (d100) from PSG.
Creates P9 (Loadouts & Tables) linked under P7.
Run after add_psw_character.py: python scripts/add_psw_tables.py
"""

import json
import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "mothership.db")


# ── P9: Loadouts & Tables ─────────────────────────────────────────────────────

PAGE = (9, "🎲", 7, "Loadouts & Tables", "Снаряжение и Таблицы", "Спорядження та Таблиці")


# ── Loadout dice tables ───────────────────────────────────────────────────────

LOADOUTS = [
    {
        "id": 51, "icon": "🪖", "source_page": 7,
        "name": ("Marine Loadout", "Снаряжение Морпеха", "Спорядження Морського Піхотинця"),
        "desc": (
            "Roll 1d10 to determine your starting gear.",
            "Бросьте 1d10 для определения начального снаряжения.",
            "Киньте 1d10 для визначення початкового спорядження.",
        ),
        "dice": {"die": "d10", "entries": [
            {"min": 0, "max": 0, "text": "Tank Top and Camo Pants (AP 1), Combat Knife (as Scalpel DMG [+]), Stimpak (x5)"},
            {"min": 1, "max": 1, "text": "Advanced Battle Dress (AP 10), Flamethrower (4 shots), Boarding Axe"},
            {"min": 2, "max": 2, "text": "Standard Battle Dress (AP 7), Combat Shotgun (4 rounds), Rucksack, Camping Gear"},
            {"min": 3, "max": 3, "text": "Standard Battle Dress (AP 7), Pulse Rifle (3 mags), Infrared Goggles"},
            {"min": 4, "max": 4, "text": "Standard Battle Dress (AP 7), Smart Rifle (3 mags), Binoculars, Personal Locator"},
            {"min": 5, "max": 5, "text": "Standard Battle Dress (AP 7), SMG (3 mags), MRE (x7)"},
            {"min": 6, "max": 6, "text": "Fatigues (AP 2), Combat Shotgun (2 rounds), Dog (pet), Leash, Tennis Ball"},
            {"min": 7, "max": 7, "text": "Fatigues (AP 2), Revolver (12 rounds), Frag Grenade"},
            {"min": 8, "max": 8, "text": "Dress Uniform (AP 1), Revolver (1 round), Challenge Coin"},
            {"min": 9, "max": 9, "text": "Advanced Battle Dress (AP 10), General-Purpose Machine Gun (1 can of ammo), HUD"},
        ]},
    },
    {
        "id": 52, "icon": "🤖", "source_page": 7,
        "name": ("Android Loadout", "Снаряжение Андроида", "Спорядження Андроїда"),
        "desc": (
            "Roll 1d10 to determine your starting gear.",
            "Бросьте 1d10 для определения начального снаряжения.",
            "Киньте 1d10 для визначення початкового спорядження.",
        ),
        "dice": {"die": "d10", "entries": [
            {"min": 0, "max": 0, "text": "Vaccsuit (AP 3), Smart Rifle (2 mags), Infrared Goggles, Mylar Blanket"},
            {"min": 1, "max": 1, "text": "Vaccsuit (AP 3), Revolver (12 rounds), Long-range Comms, Satchel"},
            {"min": 2, "max": 2, "text": "Hazard Suit (AP 5), Revolver (6 rounds), Defibrillator, First Aid Kit, Flashlight"},
            {"min": 3, "max": 3, "text": "Hazard Suit (AP 5), Foam Gun (2 charges), Sample Collection Kit, Screwdriver (as Assorted Tools)"},
            {"min": 4, "max": 4, "text": "Standard Battle Dress (AP 7), Tranq Pistol (3 shots), Paracord (100m)"},
            {"min": 5, "max": 5, "text": "Standard Crew Attire (AP 1), Stun Baton, Small Pet (organic)"},
            {"min": 6, "max": 6, "text": "Standard Crew Attire (AP 1), Scalpel, Bioscanner"},
            {"min": 7, "max": 7, "text": "Standard Crew Attire (AP 1), Frag Grenade, Pen Knife"},
            {"min": 8, "max": 8, "text": "Manufacturer Supplied Attire (AP 1), Jump-9 Ticket (destination blank)"},
            {"min": 9, "max": 9, "text": "Corporate Attire (AP 1), VIP Corporate Key Card"},
        ]},
    },
    {
        "id": 53, "icon": "🔬", "source_page": 7,
        "name": ("Scientist Loadout", "Снаряжение Учёного", "Спорядження Вченого"),
        "desc": (
            "Roll 1d10 to determine your starting gear.",
            "Бросьте 1d10 для определения начального снаряжения.",
            "Киньте 1d10 для визначення початкового спорядження.",
        ),
        "dice": {"die": "d10", "entries": [
            {"min": 0, "max": 0, "text": "Hazard Suit (AP 5), Tranq Pistol (3 shots), Bioscanner, Sample Collection Kit"},
            {"min": 1, "max": 1, "text": "Hazard Suit (AP 5), Flamethrower (1 charge), Stimpak, Electronic Tool Set"},
            {"min": 2, "max": 2, "text": "Vaccsuit (AP 3), Rigging Gun, Sample Collection Kit, Flashlight, Lab Rat (pet)"},
            {"min": 3, "max": 3, "text": "Vaccsuit (AP 3), Foam Gun (2 charges), Foldable Stretcher, First Aid Kit, Radiation Pills (x5)"},
            {"min": 4, "max": 4, "text": "Lab Coat (AP 1), Screwdriver (as Assorted Tools), Medscanner, Vaccine (1 dose)"},
            {"min": 5, "max": 5, "text": "Lab Coat (AP 1), Cybernetic Diagnostic Scanner, Portable Computer Terminal"},
            {"min": 6, "max": 6, "text": "Scrubs (AP 1), Scalpel, Automed (x5), Oxygen Tank with Filter Mask"},
            {"min": 7, "max": 7, "text": "Scrubs (AP 1), Vial of Acid, Mylar Blanket, First Aid Kit"},
            {"min": 8, "max": 8, "text": "Standard Crew Attire (AP 1), Utility Knife (as Scalpel), Cybernetic Diagnostic Scanner, Duct Tape"},
            {"min": 9, "max": 9, "text": "Civilian Clothes (AP 1), Briefcase, Prescription Pad, Fountain Pen (Poison Injector)"},
        ]},
    },
    {
        "id": 54, "icon": "🔧", "source_page": 7,
        "name": ("Teamster Loadout", "Снаряжение Рабочего", "Спорядження Робітника"),
        "desc": (
            "Roll 1d10 to determine your starting gear.",
            "Бросьте 1d10 для определения начального снаряжения.",
            "Киньте 1d10 для визначення початкового спорядження.",
        ),
        "dice": {"die": "d10", "entries": [
            {"min": 0, "max": 0, "text": "Vaccsuit (AP 3), Laser Cutter (1 extra battery), Patch Kit (x3), Toolbelt with Assorted Tools"},
            {"min": 1, "max": 1, "text": "Vaccsuit (AP 3), Revolver (6 rounds), Crowbar, Flashlight"},
            {"min": 2, "max": 2, "text": "Vaccsuit (AP 3), Rigging Gun (1 shot), Shovel, Salvage Drone"},
            {"min": 3, "max": 3, "text": "Hazard Suit (AP 5), Vibechete, Spanner, Camping Gear, Water Filtration Device"},
            {"min": 4, "max": 4, "text": "Heavy Duty Work Clothes (AP 2), Explosives & Detonator, Cigarettes"},
            {"min": 5, "max": 5, "text": "Heavy Duty Work Clothes (AP 2), Drill (as Assorted Tools), Paracord (100m), Salvage Drone"},
            {"min": 6, "max": 6, "text": "Standard Crew Attire (AP 1), Combat Shotgun (4 rounds), Extension Cord (20m), Cat (pet)"},
            {"min": 7, "max": 7, "text": "Standard Crew Attire (AP 1), Nail Gun (32 rounds), Head Lamp, Toolbelt with Assorted Tools, Lunch Box"},
            {"min": 8, "max": 8, "text": "Standard Crew Attire (AP 1), Flare Gun (2 rounds), Water Filtration Device, Personal Locator, Subsurface Scanner"},
            {"min": 9, "max": 9, "text": "Lounge Wear (AP 1), Crowbar, Stimpak, Six Pack of Beer"},
        ]},
    },
]


# ── Trinkets d100 ─────────────────────────────────────────────────────────────

TRINKETS_ENTRIES = [
    {"min": 0,  "max": 0,  "text": "Manual: PANIC: Harbinger of Catastrophe"},
    {"min": 1,  "max": 1,  "text": "Antique Company Scrip (Asteroid Mine)"},
    {"min": 2,  "max": 2,  "text": "Manual: SURVIVAL: Eat Soup With a Knife"},
    {"min": 3,  "max": 3,  "text": "Desiccated Husk Doll"},
    {"min": 4,  "max": 4,  "text": "Pressed Alien Flower (common)"},
    {"min": 5,  "max": 5,  "text": "Necklace of Shell Casings"},
    {"min": 6,  "max": 6,  "text": "Corroded Android Logic Core"},
    {"min": 7,  "max": 7,  "text": "Pamphlet: Signs of Parasitical Infection"},
    {"min": 8,  "max": 8,  "text": "Manual: Treat Your Rifle Like A Lady"},
    {"min": 9,  "max": 9,  "text": "Bone Knife"},
    {"min": 10, "max": 10, "text": "Calendar: Alien Pin-Up Art"},
    {"min": 11, "max": 11, "text": "Rejected Application (Colony Ship)"},
    {"min": 12, "max": 12, "text": "Holographic Serpentine Dancer"},
    {"min": 13, "max": 13, "text": "Snake Whiskey"},
    {"min": 14, "max": 14, "text": "Medical Container, Purple Powder"},
    {"min": 15, "max": 15, "text": "Pills: Male Enhancement, Shoddy"},
    {"min": 16, "max": 16, "text": "Casino Playing Cards"},
    {"min": 17, "max": 17, "text": "Lagomorph Foot"},
    {"min": 18, "max": 18, "text": "Moonstone Ring"},
    {"min": 19, "max": 19, "text": "Manual: Mining Safety and You"},
    {"min": 20, "max": 20, "text": "Pamphlet: Against Human Simulacra"},
    {"min": 21, "max": 21, "text": "Animal Skull, 3 Eyes, Curled Horns"},
    {"min": 22, "max": 22, "text": "Bartender's Certification (Expired)"},
    {"min": 23, "max": 23, "text": "Bunraku Puppet"},
    {"min": 24, "max": 24, "text": "Prospecting Mug, Dented"},
    {"min": 25, "max": 25, "text": "Eerie Mask"},
    {"min": 26, "max": 26, "text": "Ultrablack Marble"},
    {"min": 27, "max": 27, "text": "Ivory Dice"},
    {"min": 28, "max": 28, "text": "Tarot Cards, Worn, Pyrite Gilded Edges"},
    {"min": 29, "max": 29, "text": "Bag of Assorted Teeth"},
    {"min": 30, "max": 30, "text": "Ashes (A Relative)"},
    {"min": 31, "max": 31, "text": "DNR Beacon Necklace"},
    {"min": 32, "max": 32, "text": "Cigarettes (Grinning Skull)"},
    {"min": 33, "max": 33, "text": "Pills: Areca Nut"},
    {"min": 34, "max": 34, "text": "Pendant: Shell Fragments Suspended in Plastic"},
    {"min": 35, "max": 35, "text": "Pamphlet: Zen and the Art of Cargo Arrangement"},
    {"min": 36, "max": 36, "text": "Pair of Shot Glasses (Spent Shotgun Shells)"},
    {"min": 37, "max": 37, "text": "Key (Childhood Home)"},
    {"min": 38, "max": 38, "text": "Dog Tags (Heirloom)"},
    {"min": 39, "max": 39, "text": "Token: \"Is Your Morale Improving?\""},
    {"min": 40, "max": 40, "text": "Pamphlet: The Relic of Flesh"},
    {"min": 41, "max": 41, "text": "Pamphlet: The Indifferent Stars"},
    {"min": 42, "max": 42, "text": "Calendar: Military Battles"},
    {"min": 43, "max": 43, "text": "Manual: Rich Captain, Poor Captain"},
    {"min": 44, "max": 44, "text": "Campaign Poster (Home Planet)"},
    {"min": 45, "max": 45, "text": "Preserved Insectile Aberration"},
    {"min": 46, "max": 46, "text": "Titanium Toothpick"},
    {"min": 47, "max": 47, "text": "Gloves, Leather (Xenomorph Hide)"},
    {"min": 48, "max": 48, "text": "Smut (Seditious): The Captain, Ordered"},
    {"min": 49, "max": 49, "text": "Towel, Slightly Frayed"},
    {"min": 50, "max": 50, "text": "Brass Knuckles"},
    {"min": 51, "max": 51, "text": "Fuzzy Handcuffs"},
    {"min": 52, "max": 52, "text": "Journal of Grudges"},
    {"min": 53, "max": 53, "text": "Stylized Cigarette Case"},
    {"min": 54, "max": 54, "text": "Ball of Assorted Gauge Wire"},
    {"min": 55, "max": 55, "text": "Spanner"},
    {"min": 56, "max": 56, "text": "Switchblade, Ornamental"},
    {"min": 57, "max": 57, "text": "Powdered Xenomorph Horn"},
    {"min": 58, "max": 58, "text": "Bonsai Tree, Potted"},
    {"min": 59, "max": 59, "text": "Golf Club (Putter)"},
    {"min": 60, "max": 60, "text": "Trilobite Fossil"},
    {"min": 61, "max": 61, "text": "Pamphlet: A Lover In Every Port"},
    {"min": 62, "max": 62, "text": "Patched Overalls, Personalized"},
    {"min": 63, "max": 63, "text": "Fleshy Thing Sealed in a Murky Jar"},
    {"min": 64, "max": 64, "text": "Spiked Bracelet"},
    {"min": 65, "max": 65, "text": "Harmonica"},
    {"min": 66, "max": 66, "text": "Pictorial Pornography, Dog-eared, Well-thumbed"},
    {"min": 67, "max": 67, "text": "Coffee Cup, Chipped, reads: HAPPINESS IS MANDATORY"},
    {"min": 68, "max": 68, "text": "Manual: Moonshining With Gun Oil & Fuel"},
    {"min": 69, "max": 69, "text": "Miniature Chess Set, Bone, Pieces Missing"},
    {"min": 70, "max": 70, "text": "Gyroscope, Bent, Tin"},
    {"min": 71, "max": 71, "text": "Faded Green Poker Chip"},
    {"min": 72, "max": 72, "text": "Ukulele"},
    {"min": 73, "max": 73, "text": "Spray Paint"},
    {"min": 74, "max": 74, "text": "Wanted Poster, Weathered"},
    {"min": 75, "max": 75, "text": "Locket, Hair Braid"},
    {"min": 76, "max": 76, "text": "Sculpture of a Rat (Gold)"},
    {"min": 77, "max": 77, "text": "Blanket, Fire Retardant"},
    {"min": 78, "max": 78, "text": "Hooded Parka, Fleece-Lined"},
    {"min": 79, "max": 79, "text": "BB Gun"},
    {"min": 80, "max": 80, "text": "Flint Hatchet"},
    {"min": 81, "max": 81, "text": "Pendant: Two Astronauts form a Skull"},
    {"min": 82, "max": 82, "text": "Rubik's Cube"},
    {"min": 83, "max": 83, "text": "Stress Ball, reads: Zero Stress in Zero G"},
    {"min": 84, "max": 84, "text": "Sputnik Pin"},
    {"min": 85, "max": 85, "text": "Ushanka"},
    {"min": 86, "max": 86, "text": "Trucker Cap, Mesh, Grey Alien Logo"},
    {"min": 87, "max": 87, "text": "Menthol Balm"},
    {"min": 88, "max": 88, "text": "Pith Helmet"},
    {"min": 89, "max": 89, "text": "10m x 10m Tarp"},
    {"min": 90, "max": 90, "text": "I Ching, Missing Sticks"},
    {"min": 91, "max": 91, "text": "Kukri"},
    {"min": 92, "max": 92, "text": "Trench Shovel"},
    {"min": 93, "max": 93, "text": "Shiv, Sharpened Butter Knife"},
    {"min": 94, "max": 94, "text": "Taxidermied Cat"},
    {"min": 95, "max": 95, "text": "Pamphlet: Interpreting Sheep Dreams"},
    {"min": 96, "max": 96, "text": "Faded Photograph, A Windswept Heath"},
    {"min": 97, "max": 97, "text": "Opera Glasses"},
    {"min": 98, "max": 98, "text": "Pamphlet: Android Overlords"},
    {"min": 99, "max": 99, "text": "Interstellar Compass, Always Points to Homeworld"},
]

TRINKET = {
    "id": 55, "icon": "💎", "source_page": 8,
    "name": ("Trinkets", "Безделушки", "Дрібнички"),
    "desc": (
        "Roll 1d100 during character creation. May it bring you good luck out there in the void.",
        "Бросьте 1d100 при создании персонажа. Пусть принесёт вам удачу в пустоте.",
        "Киньте 1d100 при створенні персонажа. Хай принесе вам удачу у порожнечі.",
    ),
    "dice": {"die": "d100", "entries": TRINKETS_ENTRIES},
}


# ── Patches d100 ──────────────────────────────────────────────────────────────

PATCHES_ENTRIES = [
    {"min": 0,  "max": 0,  "text": "\"I'm Not A Rocket Scientist / But You're An Idiot\""},
    {"min": 1,  "max": 1,  "text": "Medic Patch (Skull and Crossbones over Cross)"},
    {"min": 2,  "max": 2,  "text": "\"Don't Run You'll Only Die Tired\" Backpatch"},
    {"min": 3,  "max": 3,  "text": "Red Shirt Logo"},
    {"min": 4,  "max": 4,  "text": "Blood Type (Reference Patch)"},
    {"min": 5,  "max": 5,  "text": "\"Do I LOOK Like An Expert?\""},
    {"min": 6,  "max": 6,  "text": "Biohazard Symbol"},
    {"min": 7,  "max": 7,  "text": "Mr. Yuck"},
    {"min": 8,  "max": 8,  "text": "Nuclear Symbol"},
    {"min": 9,  "max": 9,  "text": "\"Eat The Rich\""},
    {"min": 10, "max": 10, "text": "\"Be Sure: Doubletap\""},
    {"min": 11, "max": 11, "text": "Flame Emoji"},
    {"min": 12, "max": 12, "text": "Smiley Face (Glow in the Dark)"},
    {"min": 13, "max": 13, "text": "\"Smile: Big Brother is Watching\""},
    {"min": 14, "max": 14, "text": "Jolly Roger"},
    {"min": 15, "max": 15, "text": "Viking Skull"},
    {"min": 16, "max": 16, "text": "\"APEX PREDATOR\" (Sabertooth Skull)"},
    {"min": 17, "max": 17, "text": "Pin-Up Model (Ace of Spades)"},
    {"min": 18, "max": 18, "text": "Queen of Hearts"},
    {"min": 19, "max": 19, "text": "Security Guard"},
    {"min": 20, "max": 20, "text": "\"LONER\""},
    {"min": 21, "max": 21, "text": "\"Front Towards Enemy\" (Claymore Mine)"},
    {"min": 22, "max": 22, "text": "Pin-Up Model (Riding Missile)"},
    {"min": 23, "max": 23, "text": "FUBAR"},
    {"min": 24, "max": 24, "text": "\"I'm A (Love) Machine\""},
    {"min": 25, "max": 25, "text": "Pin-Up Model (Mechanic)"},
    {"min": 26, "max": 26, "text": "\"HELLO MY NAME IS:\""},
    {"min": 27, "max": 27, "text": "\"Powered By Coffee\""},
    {"min": 28, "max": 28, "text": "\"Take Me To Your Leader\" (UFO)"},
    {"min": 29, "max": 29, "text": "\"DO YOUR JOB\""},
    {"min": 30, "max": 30, "text": "\"Take My Life (Please)\""},
    {"min": 31, "max": 31, "text": "\"Upstanding Citizen\""},
    {"min": 32, "max": 32, "text": "\"Allergic To Bullshit\" (Medical Style Patch)"},
    {"min": 33, "max": 33, "text": "\"Fix Me First\" (Caduceus)"},
    {"min": 34, "max": 34, "text": "\"I Like My Tools Clean / And My Lovers Dirty\""},
    {"min": 35, "max": 35, "text": "\"The Louder You Scream the Faster I Come\" (Nurse Pin-Up)"},
    {"min": 36, "max": 36, "text": "HMFIC (Head Mother Fucker In Charge)"},
    {"min": 37, "max": 37, "text": "Dove in Crosshairs"},
    {"min": 38, "max": 38, "text": "Chibi Cthulhu"},
    {"min": 39, "max": 39, "text": "\"Welcome to the DANGER ZONE\""},
    {"min": 40, "max": 40, "text": "Skull and Crossed Wrenches"},
    {"min": 41, "max": 41, "text": "Pin-Up Model (Succubus)"},
    {"min": 42, "max": 42, "text": "\"DILLIGAF?\""},
    {"min": 43, "max": 43, "text": "\"DRINK / FIGHT / FUCK\""},
    {"min": 44, "max": 44, "text": "\"Work Hard / Party Harder\""},
    {"min": 45, "max": 45, "text": "Mudflap Girl"},
    {"min": 46, "max": 46, "text": "Fun Meter (reads: Bad Time)"},
    {"min": 47, "max": 47, "text": "\"GAME OVER\" (Bride & Groom)"},
    {"min": 48, "max": 48, "text": "Heart"},
    {"min": 49, "max": 49, "text": "\"IMPROVE / ADAPT / OVERCOME\""},
    {"min": 50, "max": 50, "text": "\"SUCK IT UP\""},
    {"min": 51, "max": 51, "text": "\"Cowboy Up\" (Crossed Revolvers)"},
    {"min": 52, "max": 52, "text": "\"Troubleshooter\""},
    {"min": 53, "max": 53, "text": "NASA Logo"},
    {"min": 54, "max": 54, "text": "Crossed Hammers with Wings"},
    {"min": 55, "max": 55, "text": "\"Keep Well Lubricated\""},
    {"min": 56, "max": 56, "text": "Soviet Hammer & Sickle"},
    {"min": 57, "max": 57, "text": "\"Plays Well With Others\""},
    {"min": 58, "max": 58, "text": "\"Live Free and Die\""},
    {"min": 59, "max": 59, "text": "\"IF I'M RUNNING KEEP UP\" Backpatch"},
    {"min": 60, "max": 60, "text": "\"Meat Bag\""},
    {"min": 61, "max": 61, "text": "\"I Am Not A Robot\""},
    {"min": 62, "max": 62, "text": "Red Gear"},
    {"min": 63, "max": 63, "text": "\"I Can't Fix Stupid\""},
    {"min": 64, "max": 64, "text": "\"Space IS My Home\" (Sad Astronaut)"},
    {"min": 65, "max": 65, "text": "All Seeing Eye"},
    {"min": 66, "max": 66, "text": "\"Solve Et Coagula\" (Baphomet)"},
    {"min": 67, "max": 67, "text": "\"All Out of Fucks To Give\" (Astronaut with Turned Out Pockets)"},
    {"min": 68, "max": 68, "text": "\"Travel To Distant Places / Meet Unusual Things / Get Eaten\""},
    {"min": 69, "max": 69, "text": "BOHICA (Bend Over Here It Comes Again)"},
    {"min": 70, "max": 70, "text": "\"I Am My Brother's Keeper\""},
    {"min": 71, "max": 71, "text": "\"Mama Tried\""},
    {"min": 72, "max": 72, "text": "Black Widow Spider"},
    {"min": 73, "max": 73, "text": "\"My Other Ride Married You\""},
    {"min": 74, "max": 74, "text": "\"One Size Fits All\" (Grenade)"},
    {"min": 75, "max": 75, "text": "Grim Reaper Backpatch"},
    {"min": 76, "max": 76, "text": "отъебись (\"Fuck Off,\" Russian)"},
    {"min": 77, "max": 77, "text": "\"Smooth Operator\""},
    {"min": 78, "max": 78, "text": "Atom Symbol"},
    {"min": 79, "max": 79, "text": "\"For Science!\""},
    {"min": 80, "max": 80, "text": "\"Actually, I AM A Rocket Scientist\""},
    {"min": 81, "max": 81, "text": "\"Help Wanted\""},
    {"min": 82, "max": 82, "text": "Princess"},
    {"min": 83, "max": 83, "text": "\"NOMAD\""},
    {"min": 84, "max": 84, "text": "\"GOOD BOY\""},
    {"min": 85, "max": 85, "text": "Dice (Snake Eyes)"},
    {"min": 86, "max": 86, "text": "\"#1 Worker\""},
    {"min": 87, "max": 87, "text": "\"Good\" (Brain)"},
    {"min": 88, "max": 88, "text": "\"Bad Bitch\""},
    {"min": 89, "max": 89, "text": "\"Too Pretty To Die\""},
    {"min": 90, "max": 90, "text": "\"Fuck Forever\" (Roses)"},
    {"min": 91, "max": 91, "text": "Icarus"},
    {"min": 92, "max": 92, "text": "\"Girl's Best Friend\" (Diamond)"},
    {"min": 93, "max": 93, "text": "Risk of Electrocution Symbol"},
    {"min": 94, "max": 94, "text": "Inverted Cross"},
    {"min": 95, "max": 95, "text": "\"Do You Sign My Paychecks?\" Backpatch"},
    {"min": 96, "max": 96, "text": "\"I ♥ Myself\""},
    {"min": 97, "max": 97, "text": "Double Cherry"},
    {"min": 98, "max": 98, "text": "\"Volunteer\""},
    {"min": 99, "max": 99, "text": "Poker Hand: Dead Man's Hand (Aces Full of Eights)"},
]

PATCH = {
    "id": 56, "icon": "🏷️", "source_page": 9,
    "name": ("Patches", "Нашивки", "Нашивки"),
    "desc": (
        "Roll 1d100 during character creation. Sewn on your clothing or gear.",
        "Бросьте 1d100 при создании персонажа. Нашивка на одежде или снаряжении.",
        "Киньте 1d100 при створенні персонажа. Нашивка на одязі або спорядженні.",
    ),
    "dice": {"die": "d100", "entries": PATCHES_ENTRIES},
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _add_linked_page(conn: sqlite3.Connection, parent_id: int, child_id: int) -> None:
    row = conn.execute("SELECT linked_pages FROM pages WHERE id=?", (parent_id,)).fetchone()
    current: list[int] = json.loads(row[0]) if row else []
    if child_id not in current:
        current.append(child_id)
        conn.execute("UPDATE pages SET linked_pages=? WHERE id=?",
                     (json.dumps(current), parent_id))


def _seed_content(conn: sqlite3.Connection, item: dict, page_id: int) -> None:
    cid = item["id"]
    conn.execute("DELETE FROM contents WHERE id = ?", (cid,))
    conn.execute("""
        INSERT INTO contents (id, icon, source_slug, source_page, dice, sort_order)
        VALUES (?, ?, 'psg', ?, ?, ?)
    """, (cid, item["icon"], item["source_page"],
          json.dumps(item["dice"]), cid))
    for lang, name, desc in zip(("en", "ru", "ua"), item["name"], item["desc"]):
        conn.execute("""
            INSERT INTO content_i18n (content_id, lang, name, desc, subinfo_text)
            VALUES (?, ?, ?, ?, NULL)
        """, (cid, lang, name, desc))
    conn.execute("""
        INSERT OR IGNORE INTO page_contents (page_id, content_id, sort_order)
        VALUES (?, ?, ?)
    """, (page_id, cid, cid))


# ── Seed ──────────────────────────────────────────────────────────────────────

def _seed(conn: sqlite3.Connection) -> None:
    conn.execute("""
        INSERT OR IGNORE INTO sources (id, slug, title, type)
        VALUES (1, 'psg', 'Player''s Survival Guide', 'core')
    """)

    # Create P9
    pid, icon, src_page, name_en, name_ru, name_ua = PAGE
    conn.execute("""
        INSERT OR IGNORE INTO pages (id, icon, source_slug, source_page, linked_pages)
        VALUES (?, ?, 'psg', ?, '[]')
    """, (pid, icon, src_page))
    for lang, name in [("en", name_en), ("ru", name_ru), ("ua", name_ua)]:
        conn.execute("""
            INSERT OR IGNORE INTO page_i18n (page_id, lang, name)
            VALUES (?, ?, ?)
        """, (pid, lang, name))

    # Link P9 under P7
    _add_linked_page(conn, parent_id=7, child_id=9)

    # Seed loadouts
    for item in LOADOUTS:
        _seed_content(conn, item, page_id=9)

    # Seed trinkets and patches
    _seed_content(conn, TRINKET, page_id=9)
    _seed_content(conn, PATCH,   page_id=9)


def run() -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        _seed(conn)
        conn.commit()
        total = len(LOADOUTS) + 2
        print(f"Done — Loadouts & Tables (P9) + C51–C56 ({total} items) seeded into '{DB_PATH}'.")
    finally:
        conn.close()


if __name__ == "__main__":
    run()
