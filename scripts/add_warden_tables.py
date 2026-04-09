import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# ── RANDOM LORE — replace table:15 entries ─────────────────────────────
lore_data = [
    (0, 0, "The Maru Banking Colonies", "The Maru Banking Colonies"),
    (1, 4, "False Europa", "False Europa"),
    (5, 8, "The Egosystem", "The Egosystem"),
    (9, 12, "The MIDAS-12 Massacre", "The MIDAS-12 Massacre"),
    (13, 16, "The Shadow Algorithm", "The Shadow Algorithm"),
    (17, 20, "Universal Remote", "Universal Remote"),
    (21, 24, "The Conway Machine", "The Conway Machine"),
    (25, 28, "The Book of Sar", "The Book of Sar"),
    (29, 32, "MOGUL: Maximum Prison Planet", "MOGUL: Maximum Prison Planet"),
    (33, 36, "The Orlov Incident", "The Orlov Incident"),
    (37, 40, "Fred, the Disappearing Man", "Fred, the Disappearing Man"),
    (41, 44, "The Creeping Fog", "The Creeping Fog"),
    (45, 48, "Mindpillers", "Mindpillers"),
    (49, 52, "The Precursors", "The Precursors"),
    (53, 56, "Zygotean Mercenaries", "Zygotean Mercenaries"),
    (57, 60, "The Teaman Murders", "The Teaman Murders"),
    (61, 64, "The Whispering Plague", "The Whispering Plague"),
    (65, 68, "Sea of Tranquility Conspiracy", "Sea of Tranquility Conspiracy"),
    (69, 72, "UCSCV Mournbringer Flight 364", "UCSCV Mournbringer Flight 364"),
    (73, 76, "The Bracewell Autonomous Zone", "The Bracewell Autonomous Zone"),
    (77, 80, "Spasi, Otets, Syna", "Spasi, Otets, Syna"),
    (81, 83, "Cosmetic Vampire Hoax", "Cosmetic Vampire Hoax"),
    (84, 84, "IMG 2238", "IMG 2238"),
    (85, 85, "The Magnetic Typhoon", "The Magnetic Typhoon"),
    (86, 86, "The Battle for Columbia Gate", "The Battle for Columbia Gate"),
    (87, 87, "The Spitz-Okoro Theoreum", "The Spitz-Okoro Theoreum"),
    (88, 88, "The Uplifted Possums", "The Uplifted Possums"),
    (89, 89, "The Silent Century", "The Silent Century"),
    (90, 90, "Naktari War Syndrome", "Naktari War Syndrome"),
    (91, 91, "The Autumnal City at Bellona", "The Autumnal City at Bellona"),
    (92, 92, "Origin Point Zero", "Origin Point Zero"),
    (93, 93, "The Mountebank Game", "The Mountebank Game"),
    (94, 94, "The Helium Uprising", "The Helium Uprising"),
    (95, 95, "The Dearborn Corpse", "The Dearborn Corpse"),
    (96, 96, "Wombship", "Wombship"),
    (97, 97, "The Hymn of Saeeda Dawn", "The Hymn of Saeeda Dawn"),
    (98, 98, "Divinity Strain", "Divinity Strain"),
    (99, 99, "Ray Burtnolds is Alive and Well and Living on Casimir",
              "Ray Burtnolds is Alive and Well and Living on Casimir"),
]

with open('C:/Git/mothership/seeds/roll_table_entries.json', encoding='utf-8') as f:
    entries = json.load(f)

entries = [e for e in entries if e['table_id'] != 15]
eid = max(e['id'] for e in entries) + 1

for rmin, rmax, label, result in lore_data:
    entries.append({"id": eid, "table_id": 15, "roll_min": rmin, "roll_max": rmax,
                    "label": label, "result_text": result,
                    "result_text_ua": "", "result_text_ru": "", "extra_data": None, "linked_term_id": None})
    eid += 1

print(f"Random Lore: {len(lore_data)} entries. Next eid={eid}")

# ── CATEGORIES ─────────────────────────────────────────────────────────
with open('C:/Git/mothership/seeds/categories.json', encoding='utf-8') as f:
    cats = json.load(f)

cats += [
    {"id": 58, "name": "Planets & Factions", "slug": "planets-factions", "parent_id": 24,
     "sort_order": 1, "icon": "🌍", "name_ua": "", "name_ru": "", "icon_ua": "", "icon_ru": ""},
    {"id": 59, "name": "Settlements", "slug": "settlements", "parent_id": 24,
     "sort_order": 2, "icon": "🏘️", "name_ua": "", "name_ru": "", "icon_ua": "", "icon_ru": ""},
]
with open('C:/Git/mothership/seeds/categories.json', 'w', encoding='utf-8') as f:
    json.dump(cats, f, ensure_ascii=False, indent=2)
print("cat:58-59 added")

# ── TERMS ──────────────────────────────────────────────────────────────
with open('C:/Git/mothership/seeds/terms.json', encoding='utf-8') as f:
    terms = json.load(f)

terms += [
    {"id": 52, "name": "Planet Surface", "source_book_id": 2, "page_number": "58",
     "body": "The surface type of the planet.", "aliases": "[]",
     "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
    {"id": 53, "name": "Planet Size & Gravity", "source_book_id": 2, "page_number": "58",
     "body": "The size and gravity of the planet.", "aliases": "[]",
     "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
    {"id": 54, "name": "Planet Atmosphere", "source_book_id": 2, "page_number": "58",
     "body": "The type of atmosphere the planet has.", "aliases": "[]",
     "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
    {"id": 55, "name": "Planet Climate", "source_book_id": 2, "page_number": "58",
     "body": "The climate conditions of the planet.", "aliases": "[]",
     "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
    {"id": 56, "name": "Settlement Type", "source_book_id": 2, "page_number": "59",
     "body": "The type of settlement.", "aliases": "[]",
     "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
    {"id": 57, "name": "Settlement Conditions", "source_book_id": 2, "page_number": "59",
     "body": "Current conditions at the settlement.", "aliases": "[]",
     "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
    {"id": 58, "name": "Settlement Weird", "source_book_id": 2, "page_number": "59",
     "body": "Something strange or unusual about the settlement.", "aliases": "[]",
     "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
]
with open('C:/Git/mothership/seeds/terms.json', 'w', encoding='utf-8') as f:
    json.dump(terms, f, ensure_ascii=False, indent=2)
print("terms 52-58 added")

# ── ROLL TABLES ────────────────────────────────────────────────────────
with open('C:/Git/mothership/seeds/roll_tables.json', encoding='utf-8') as f:
    tables = json.load(f)

tables += [
    # Planet tables (cat:58)
    {"id": 30, "name": "Planet Surface", "description": "The surface type of the planet.",
     "dice_notation": "d10", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 1, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "🪨"},
    {"id": 31, "name": "Planet Size & Gravity", "description": "The size and gravity of the planet.",
     "dice_notation": "d10", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 2, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "⚖️"},
    {"id": 32, "name": "Planet Atmosphere", "description": "The type of atmosphere the planet has.",
     "dice_notation": "d10", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 3, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "🌫️"},
    {"id": 33, "name": "Planet Climate", "description": "The climate conditions of the planet.",
     "dice_notation": "d10", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 4, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "🌡️"},
    {"id": 34, "name": "Geological Feature", "description": "A notable geological feature near the settlement.",
     "dice_notation": "d100", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 5, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "⛰️"},
    {"id": 35, "name": "Population", "description": "The number of people at the settlement.",
     "dice_notation": "d10", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 6, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "👥"},
    {"id": 36, "name": "Port Class", "description": "The class of the settlement's port.",
     "dice_notation": "d10", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 7, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "🚀"},
    {"id": 37, "name": "Control Faction", "description": "The faction that controls the settlement.",
     "dice_notation": "d10", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 8, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "🏴"},
    {"id": 38, "name": "Factions", "description": "Named factions operating in the Mothership universe.",
     "dice_notation": "d100", "category_id": 58, "source_book_id": 2, "page_number": "58",
     "sort_order": 9, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "🏛️"},
    # Settlement tables (cat:59)
    {"id": 39, "name": "Settlement Type", "description": "The type of settlement.",
     "dice_notation": "d100", "category_id": 59, "source_book_id": 2, "page_number": "59",
     "sort_order": 1, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "🏠"},
    {"id": 40, "name": "Settlement Conditions", "description": "Current conditions at the settlement.",
     "dice_notation": "d100", "category_id": 59, "source_book_id": 2, "page_number": "59",
     "sort_order": 2, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "⚠️"},
    {"id": 41, "name": "Settlement Weird", "description": "Something strange or unusual about the settlement.",
     "dice_notation": "d100", "category_id": 59, "source_book_id": 2, "page_number": "59",
     "sort_order": 3, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "👁️"},
]
with open('C:/Git/mothership/seeds/roll_tables.json', 'w', encoding='utf-8') as f:
    json.dump(tables, f, ensure_ascii=False, indent=2)
print("tables 30-41 added")

# ── ROLL TABLE ENTRIES ─────────────────────────────────────────────────

def e(table_id, rmin, rmax, label, result):
    global eid
    r = {"id": eid, "table_id": table_id, "roll_min": rmin, "roll_max": rmax,
         "label": label, "result_text": result,
         "result_text_ua": "", "result_text_ru": "", "extra_data": None, "linked_term_id": None}
    eid += 1
    return r

# Planet Surface (table:30, d10)
for rmin, rmax, val in [(0,2,"Liquid"),(3,7,"Terrestrial"),(8,9,"Gas")]:
    # expand to individual rows matching the source table
    pass

# Use exact rows from source table
planet_rows = [
    (0,0,"Liquid","Giant (Crushing Gravity)","Corrosive","Hellish"),
    (1,1,"Liquid","Giant (Crushing Gravity)","Corrosive","Hot"),
    (2,2,"Liquid","Mini-Giant (Heavy Gravity)","Toxic","Hot"),
    (3,3,"Terrestrial","Mini-Giant (Heavy Gravity)","Toxic","Balmy"),
    (4,4,"Terrestrial","Mini-Giant (Heavy Gravity)","Thin","Temperate"),
    (5,5,"Terrestrial","Earth-Sized Planet (Normal Gravity)","Thin","Heavenly"),
    (6,6,"Terrestrial","Earth-Sized Planet (Normal Gravity)","Terraformed","Rainy"),
    (7,7,"Terrestrial","Dwarf Planet (Light Gravity)","Terraformed","Turbulent"),
    (8,8,"Gas","Dwarf Planet (Light Gravity)","Terraformed","Cold"),
    (9,9,"Gas","Dwarf Planet (Light Gravity)","Pristine","Freezing"),
]

for row in planet_rows:
    rmin, rmax, surface, size, atmo, climate = row
    entries.append(e(30, rmin, rmax, surface, surface))
    entries.append(e(31, rmin, rmax, size, size))
    entries.append(e(32, rmin, rmax, atmo, atmo))
    entries.append(e(33, rmin, rmax, climate, climate))

# Geological Feature (table:34, d100)
geo_data = [
    (0,4,"CATENA","CATENA (crater chain)"),
    (5,8,"CHAOS","CHAOS (broken terrain)"),
    (9,12,"COLLIS","COLLIS (small hill)"),
    (13,16,"CRATER","CRATER (impact valley)"),
    (17,20,"DORSUM","DORSUM (ridge)"),
    (21,24,"ERUPTIVE CENTER","ERUPTIVE CENTER (volcano)"),
    (25,28,"FOSSA","FOSSA (trough)"),
    (29,32,"LABES","LABES (landslide)"),
    (33,35,"LABYRINTHUS","LABYRINTHUS (complex of intersecting valleys/ridges)"),
    (36,39,"LACUS","LACUS (small plain)"),
    (40,43,"LANDING SITE","LANDING SITE"),
    (44,47,"MARE","MARE (sea on a moon)"),
    (48,51,"MENSA","MENSA (mesa)"),
    (52,56,"MONS","MONS (mountain)"),
    (57,60,"MONTES","MONTES (mountain range)"),
    (61,65,"PATERA","PATERA (irregular crater)"),
    (66,69,"PLANITIA","PLANITIA (low plain)"),
    (70,73,"PLANUM","PLANUM (high plain/plateau)"),
    (74,77,"RUPES","RUPES (cliff/scarp)"),
    (78,81,"RIMA","RIMA (fissure)"),
    (82,85,"SAXUM","SAXUM (boulder)"),
    (86,89,"TERRA","TERRA (extensive land mass)"),
    (90,94,"THOLUS","THOLUS (small mountain)"),
    (95,99,"UNDAE","UNDAE (field of dunes)"),
]
for rmin, rmax, label, result in geo_data:
    entries.append(e(34, rmin, rmax, label, result))

# Population (table:35, d10)
pop_data = [
    (0,0,"A single person","A single person."),
    (1,2,"A small handful","A small handful of people."),
    (3,4,"A few dozen","A few dozen people."),
    (5,6,"Roughly a hundred","Roughly a hundred people."),
    (7,7,"A few hundred","A few hundred people."),
    (8,8,"Roughly a thousand","Roughly a thousand people."),
    (9,9,"Overpopulated","Overpopulated."),
]
for rmin, rmax, label, result in pop_data:
    entries.append(e(35, rmin, rmax, label, result))

# Port Class (table:36, d10)
port_data = [
    (0,0,"X-Class Port","X-Class Port"),
    (1,5,"C-Class Port","C-Class Port"),
    (6,7,"B-Class Port","B-Class Port"),
    (8,8,"A-Class Port","A-Class Port"),
    (9,9,"S-Class Port","S-Class Port"),
]
for rmin, rmax, label, result in port_data:
    entries.append(e(36, rmin, rmax, label, result))

# Control Faction (table:37, d10)
ctrl_data = [
    (0,0,"Religious Group","Religious Group"),
    (1,5,"Corporation","Corporation"),
    (6,7,"Government","Government"),
    (8,8,"Union","Union"),
    (9,9,"Criminal Organization","Criminal Organization"),
]
for rmin, rmax, label, result in ctrl_data:
    entries.append(e(37, rmin, rmax, label, result))

# Factions (table:38, d100)
factions_data = [
    (0,0,"The Seraphim Institute","The Seraphim Institute"),
    (1,9,"The Outer Rim Colonial Marshalls","The Outer Rim Colonial Marshalls (OCRM)"),
    (10,19,"SEBACO Mining Ltd.","SEBACO Mining Ltd."),
    (20,26,"The Teamster's Union","The Teamster's Union"),
    (27,31,"The Alliance of Hyperspace Jump Couriers","The Alliance of Hyperspace Jump Couriers"),
    (32,35,"The Evangelical Solarion Church","The Evangelical Solarion Church (AKA The Solarians)"),
    (36,40,"Los Ninos Basura","Los Ninos Basura"),
    (41,44,"The Computer Coders Collective","The Computer Coders Collective (AKA T-Triple-C)"),
    (45,48,"PROJECT RICHTER","PROJECT RICHTER"),
    (49,52,"BAS-Lehman Ges.m.b.H","BAS-Lehman Ges.m.b.H"),
    (53,56,"Tannhauser Heavy Industries","Tannhauser Heavy Industries"),
    (57,60,"The Synthetic Liberation Front","The Synthetic Liberation Front"),
    (61,64,"Parker-Vance Holding Company","Parker-Vance Holding Company"),
    (65,68,"The Interstellar Postal Inspection Service","The Interstellar Postal Inspection Service"),
    (69,72,"The Komarov Squad","The Komarov Squad"),
    (73,76,"The Interstellar Asteroid Miners Association","The Interstellar Asteroid Miners Association"),
    (77,80,"The Jump-9 Club","The Jump-9 Club"),
    (81,84,"Second Samuel Church","Second Samuel Church"),
    (85,89,"The Zero-G Laborers Coalition","The Zero-G Laborers Coalition (AKA Zed-GLC)"),
    (90,90,"REDKNIFE Psyops Unit","REDKNIFE Psyops Unit"),
    (91,91,"The Astronavigator's Guild","The Astronavigator's Guild"),
    (92,92,"The Organization","The Organization"),
    (93,93,"Revolutionary Forces of Luna","Revolutionary Forces of Luna"),
    (94,94,"The Interplanetary Sex Workers Union","The Interplanetary Sex Workers Union"),
    (95,95,"The Space Monkey Mafia","The Space Monkey Mafia"),
    (96,96,"House Sivaranjan","House Sivaranjan"),
    (97,97,"Uplifted Dolphin Pod 67","Uplifted Dolphin Pod 67"),
    (98,98,"Aleph Gate","Aleph Gate"),
    (99,99,"FRIEND","FRIEND"),
]
for rmin, rmax, label, result in factions_data:
    entries.append(e(38, rmin, rmax, label, result))

# Settlements — 3 columns split into 3 tables (39, 40, 41)
settlements_data = [
    (0,0,"Forced Relocation Slum","Under quarantine.","Failed utopia."),
    (1,9,"Terraformer Colony","Overworked, tired. Low morale.","Unsolved string of gruesome murders."),
    (10,19,"Mining Colony","Business as usual.","Home to powerful criminal syndicate."),
    (20,26,"Colonial Settlement","Workers on strike.","Local customs are strange, wary of outsiders."),
    (27,32,"Marine Garrison","Hazardous working conditions.","Deserted."),
    (33,35,"Research Facility","Security forces in control.","Secretly a corporate re-education camp."),
    (36,38,"Corporate Operations Center","Gross managerial misconduct.","Settlement has newfound religious significance."),
    (39,41,"Manufacturing Complex","Frequent storms.","Company secretly dosing the water."),
    (42,44,"Deep Sea Research Base","Productivity low.","Live hostage situation."),
    (45,47,"Heavy Industry Complex","Corporate strikebreakers called in.","Local environment is a radioactive wasteland."),
    (48,50,"Shipping & Logistics Center","Hostile wildlife.","Rapidly growing doomsday cult."),
    (51,53,"Ore Refinery","Military blockade.","Controlled by separatist militia."),
    (54,56,"Forward Military Base","Lush overgrown wilderness.","Collapse of local social order."),
    (57,59,"Rural Backworld Installation","In desperate need of aid.","Refugee crisis."),
    (60,62,"Corporate Resupply Depot","Weather frighteningly unstable.","Extinction event."),
    (63,65,"Monitoring Outpost","Food shortage.","Settlement has descended into anarchy."),
    (66,68,"Off-World Training Installation","Colonists talking of joining a Union.","Colonists report being replaced by imposters."),
    (69,71,"Polar Research Station","Awaiting orders from corporate.","Secret military operation recently arrived."),
    (72,74,"Restricted Testing Facility","Local Union elections.","Deadly viral outbreak."),
    (75,77,"Maximum Security Prison Complex","Contract negotiation breakdown.","Environmental collapse imminent."),
    (78,80,"Stakeholder Camp","Low on supplies.","Recent breakthrough discovery."),
    (81,83,"Farming Colony","Massive crop failure.","Settlement houses decadent corporate nobility."),
    (84,86,"Prison, formerly a... (roll again)","Communications cut-off.","Colonists slowly disappearing."),
    (87,89,"Autonomous Factory Zone","Company holiday celebrations.","Strange black monolith unearthed."),
    (90,91,"Independent Frontier Settlement","Under constant threat of terrorist attacks.","Rumors of meddling from powerful AI."),
    (92,92,"Covert Pirate Base","Local government crumbling.","Colonists believe settlement haunted."),
    (93,93,"Classified Corporate Installation","Rumors of layoffs.","Android uprising imminent."),
    (94,94,"Desolate Scrapworld","Overpopulation issue.","Gigantic unidentifiable fossilized remains."),
    (95,95,"Major Colonial Settlement","Settlement being shut down by corporate.","Reports of interference by Celestials."),
    (96,96,"Religious Compound","Petty bickering escalating out of control.","Wreckage of spacecraft of unknown origin."),
    (97,97,"Anti-corporate Rebel Base","Population entirely synthetic.","Ruins of precursor star-faring civilization found."),
    (98,98,"Undisclosed Black Site","Co-opted by military as temporary base.","Ancient gateway recently uncovered."),
    (99,99,"Private C-Suite Game Preserve","Mutiny brewing.","First Contact event."),
]
for rmin, rmax, stype, conditions, weird in settlements_data:
    entries.append(e(39, rmin, rmax, stype, stype))
    entries.append(e(40, rmin, rmax, conditions, conditions))
    entries.append(e(41, rmin, rmax, weird, weird))

with open('C:/Git/mothership/seeds/roll_table_entries.json', 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)
print(f"All entries written. Total: {len(entries)}, next eid={eid}")

# ── RULES ──────────────────────────────────────────────────────────────
with open('C:/Git/mothership/seeds/rules.json', encoding='utf-8') as f:
    rules = json.load(f)

rules += [
    {
        "id": 63, "title": "Planets", "category_id": 58,
        "source_book_id": 2, "page_number": "58", "sort_order": 1,
        "body": (
            "Roll on each of the four tables to generate a random planet, or pick values that fit your scenario.\n\n"
            "*SURFACE* — What the planet surface is made of: Liquid, Terrestrial, or Gas.\n"
            "*SIZE & GRAVITY* — From Dwarf Planet (Light Gravity) to Giant (Crushing Gravity).\n"
            "*ATMOSPHERE* — Pristine, Terraformed, Thin, Toxic, or Corrosive.\n"
            "*CLIMATE* — From Freezing to Hellish.\n\n"
            "Use *Geological Feature* to add a notable landmark near a settlement. "
            "Use *Population, Port Class,* and *Control Faction* to flesh out settlements on the planet."
        ),
        "icon": "🌍", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 64, "title": "Settlements", "category_id": 59,
        "source_book_id": 2, "page_number": "59", "sort_order": 1,
        "body": (
            "Roll on each of the three tables to generate a random settlement, or pick values that fit your scenario.\n\n"
            "*TYPE* — What kind of settlement it is: mining colony, research facility, prison, etc.\n"
            "*CONDITIONS* — What is currently happening there: strikes, blockades, food shortages, etc.\n"
            "*WEIRD* — Something unusual or sinister: a doomsday cult, an android uprising, a monolith.\n\n"
            "Combine all three results to create a vivid, immediately playable location."
        ),
        "icon": "🏘️", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
]
with open('C:/Git/mothership/seeds/rules.json', 'w', encoding='utf-8') as f:
    json.dump(rules, f, ensure_ascii=False, indent=2)
print(f"Rules 63-64 added. Total: {len(rules)}")

# ── CONTENT TERM LINKS ─────────────────────────────────────────────────
with open('C:/Git/mothership/seeds/content_term_links.json', encoding='utf-8') as f:
    links = json.load(f)

lid = max(l['id'] for l in links) + 1

def lnk(content_type, content_id, term_id, sort_order=0):
    global lid
    l = {"id": lid, "content_type": content_type, "content_id": content_id,
         "term_id": term_id, "sort_order": sort_order}
    lid += 1
    return l

new_links = [
    # Planets: rule:63 → terms 52-55 in order
    lnk("rule", 63, 52, 1),  # Surface
    lnk("rule", 63, 53, 2),  # Size & Gravity
    lnk("rule", 63, 54, 3),  # Atmosphere
    lnk("rule", 63, 55, 4),  # Climate
    # Planet tables → terms
    lnk("roll_table", 30, 52),
    lnk("roll_table", 31, 53),
    lnk("roll_table", 32, 54),
    lnk("roll_table", 33, 55),
    # Settlements: rule:64 → terms 56-58 in order
    lnk("rule", 64, 56, 1),  # Type
    lnk("rule", 64, 57, 2),  # Conditions
    lnk("rule", 64, 58, 3),  # Weird
    # Settlement tables → terms
    lnk("roll_table", 39, 56),
    lnk("roll_table", 40, 57),
    lnk("roll_table", 41, 58),
]

links.extend(new_links)
with open('C:/Git/mothership/seeds/content_term_links.json', 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)
print(f"Added {len(new_links)} links. Total: {len(links)}")
