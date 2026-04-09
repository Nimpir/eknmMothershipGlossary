import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# ── 1. CATEGORIES ──────────────────────────────────────────────────────
with open('C:/Git/mothership/seeds/categories.json', encoding='utf-8') as f:
    cats = json.load(f)

cats.append({
    "id": 57, "name": "Campaign", "slug": "campaign",
    "parent_id": 22, "sort_order": 3, "icon": "🗺️",
    "name_ua": "", "name_ru": "", "icon_ua": "", "icon_ru": ""
})
with open('C:/Git/mothership/seeds/categories.json', 'w', encoding='utf-8') as f:
    json.dump(cats, f, ensure_ascii=False, indent=2)
print("cat:57 Campaign added")

# ── 2. TERMS ───────────────────────────────────────────────────────────
with open('C:/Git/mothership/seeds/terms.json', encoding='utf-8') as f:
    terms = json.load(f)

new_terms = [
    {"id": 49, "name": "Campaign Frames", "source_book_id": 2, "page_number": "42-43",
     "body": "A campaign frame tells players who they are, what kind of work they do, and the kinds of things they will encounter. Roll d10 or choose from the Campaign Frames table.",
     "aliases": "[]", "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
    {"id": 50, "name": "Contract Work", "source_book_id": 2, "page_number": "48",
     "body": "Types of jobs available to the crew. Roll d10 to determine the department and description of available work.",
     "aliases": "[]", "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
    {"id": 51, "name": "Pay Scale", "source_book_id": 2, "page_number": "49",
     "body": "How much a job pays and what lifestyle it affords the crew. Roll d100 to determine pay and lifestyle tier.",
     "aliases": "[]", "name_ua": "", "name_ru": "", "body_ua": "", "body_ru": ""},
]
terms.extend(new_terms)
with open('C:/Git/mothership/seeds/terms.json', 'w', encoding='utf-8') as f:
    json.dump(terms, f, ensure_ascii=False, indent=2)
print("terms 49-51 added")

# ── 3. ROLL TABLES ─────────────────────────────────────────────────────
with open('C:/Git/mothership/seeds/roll_tables.json', encoding='utf-8') as f:
    tables = json.load(f)

new_tables = [
    {"id": 27, "name": "Campaign Frames", "description": "Who the players are and what they do.",
     "dice_notation": "d10", "category_id": 57, "source_book_id": 2, "page_number": "42-43",
     "sort_order": 1, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "🗺️"},
    {"id": 28, "name": "Contract Work", "description": "Types of jobs available to the crew.",
     "dice_notation": "d10", "category_id": 57, "source_book_id": 2, "page_number": "48",
     "sort_order": 2, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "💼"},
    {"id": 29, "name": "Pay Scale", "description": "How much a job pays and what lifestyle it affords.",
     "dice_notation": "d100", "category_id": 57, "source_book_id": 2, "page_number": "49",
     "sort_order": 3, "name_ua": "", "name_ru": "", "description_ua": "", "description_ru": "", "icon": "💰"},
]
tables.extend(new_tables)
with open('C:/Git/mothership/seeds/roll_tables.json', 'w', encoding='utf-8') as f:
    json.dump(tables, f, ensure_ascii=False, indent=2)
print("tables 27-29 added")

# ── 4. ROLL TABLE ENTRIES ──────────────────────────────────────────────
with open('C:/Git/mothership/seeds/roll_table_entries.json', encoding='utf-8') as f:
    entries = json.load(f)

eid = 557

def entry(table_id, rmin, rmax, label, result_text):
    global eid
    e = {"id": eid, "table_id": table_id, "roll_min": rmin, "roll_max": rmax,
         "label": label, "result_text": result_text, "result_text_ua": "", "result_text_ru": "",
         "extra_data": None, "linked_term_id": None}
    eid += 1
    return e

# Table 27: Campaign Frames (d10)
frames = [
    (0,0,"Space Truckers","Blockade running, smuggling, or working as a certified owner-operator. Never a dull shift hauling cargo across the Rim. Watch out for stowaways and customs patrols, and always pay your union dues."),
    (1,1,"Private Mercenaries","Jump and drop. Sweep and clear. Seek and destroy. You go where the Company sends you. They said if you had a vaccsuit and were willing to travel, you would always be flush with credits. They were not wrong."),
    (2,2,"Explorers","You wanted to go where no one had gone before. Turns out there is a reason why. What you found out there was not something anyone back home would understand. So you had to keep going."),
    (3,3,"Dogs of War","Humanity was in trouble and you answered the call. You have looked into the yawning maw of destruction. Your response? Come and take it."),
    (4,4,"Corporate Inspectors","Production has shut down on mining station Ypsilon-14. The Alexis research vessel has disappeared. There is a strike brewing on Prospero's Dream. The C-Levels have questions. Find out, fix it, and sign the NDA."),
    (5,5,"Offworld Colonists","You volunteered. Planting terraformers in inhospitable environments, researching planetary phenomena, defending against local flora and fauna. On the Rim, life is what you make of it."),
    (6,6,"Crashlanders","You scraped together a Jumpliner ticket to a new life. But the sirens are blaring and you are waking from cryosleep to screams. Abandon ship! Whether you fix it or ride it to the ground, your life will never be the same."),
    (7,7,"Hyperspace Raiders","It has always been illegal to steal, but only recently illegal to own. Stealing from the rich, giving to whomever you please. Jump before the Marshalls close in, and always watch for bounty hunters."),
    (8,8,"Mining & Salvage","Asteroid mining, skimming gas giants, salvaging derelicts. The pay is steady and they do not make you wear a suit and tie. What more could you ask for?"),
    (9,9,"Bounty Hunters","There is no law on the Rim, just Corporate Policy. Those who break it paint a target on their back. Check the bounty boards, bring in your charge, stay alive. The rules are easy. Getting it done is hard."),
]
for rmin, rmax, label, result in frames:
    entries.append(entry(27, rmin, rmax, label, result))

# Table 28: Contract Work (d10)
contracts = [
    (0,1,"Production & Manufacture","Asteroid mining, derelict salvage and scrap, strikebreaking, terraformer installation, and android troubleshooting."),
    (2,3,"Shipping & Handling","Cargo freight, VIP escort, scrap hauling, prisoner transport, sensitive materials handling, passenger transport, and contraband smuggling."),
    (4,5,"Research & Development","Sample and specimen collection, planetary survey, field testing, sabotage, containment breach, archaeological dig, and corporate espionage."),
    (6,7,"Risk Management","Sweep and clear, liquidation, asset protection, quarantine enforcement, bounty hunting, distress signal response, and system patrol."),
    (8,8,"Human Resources","Missing persons, suspicious death, communication breakdown, troubleshooting, AI negotiation, and settlement evacuation."),
    (9,9,"Mergers & Acquisitions","Asset recovery, salvage retention, personnel recruitment, first contact protocol, repossession, and piracy."),
]
for rmin, rmax, label, result in contracts:
    entries.append(entry(28, rmin, rmax, label, result))

# Table 29: Pay Scale (d100)
payscale = [
    (0,0,"Powerful Favor","The client cannot pay, but they are powerful and well connected. They owe the crew a big favor, called in at the crew's discretion."),
    (1,9,"Desperate","Pays 1d10x100cr up front. This is all the client has. Doing this job would make them a longtime ally."),
    (10,34,"Barter Agreement","The client can only offer trade: astronavigation data, ship repairs, weapons, equipment, or other accommodations."),
    (35,93,"Grunt Work","Pays the crew's salaries, but expenses are the crew's to handle. Jump and Hazard Pay are out of the question."),
    (94,98,"Payday","Pays 1d10x10,000cr on completion and up to 10% up front. All travel expenses paid. Up to 1d10 Contractors to assist."),
    (99,99,"Jackpot","Pays 1d10x1,000,000cr on completion and up to 1d10x10,000cr up front. All expenses paid. Private contractors available on request."),
]
for rmin, rmax, label, result in payscale:
    entries.append(entry(29, rmin, rmax, label, result))

with open('C:/Git/mothership/seeds/roll_table_entries.json', 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)
print(f"Entries added. Total now: {len(entries)}")
