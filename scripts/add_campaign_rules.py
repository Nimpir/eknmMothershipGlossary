import json, sys
sys.stdout.reconfigure(encoding='utf-8')

rules_to_add = [
    {
        "id": 52, "title": "Building Your Campaign", "category_id": 57,
        "source_book_id": 2, "page_number": "41", "sort_order": 1,
        "body": (
            "A game of Mothership takes place over one or more *sessions* and is called a *campaign.* "
            "Many campaigns are a single session (a One Shot). Most are 5-7 sessions. "
            "Long campaigns can last years or be ongoing indefinitely.\n\n"
            "*WHAT DO I NEED TO PREP?*\n"
            "• A *starter scenario* to run first.\n"
            "• A *campaign style* — how the game is broadly structured and what kind of play to expect.\n"
            "• A *campaign frame* — who the players are and what kind of work they do.\n"
            "• A *starting area* to play in.\n"
            "• A few *tools* to maintain and grow the campaign over time.\n\n"
            "*PITCHING THE GAME*\n"
            "Once you have the style and frame worked out, pitch your concept to your players. "
            "This gets everyone on the same page.\n\n"
            "💡 Being a Warden is a lot of work — and you are a player, too. "
            "Make sure the style and frame line up with your interests and the kind of prep you want to do."
        ),
        "icon": "📋", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 53, "title": "Campaign Style", "category_id": 57,
        "source_book_id": 2, "page_number": "41", "sort_order": 2,
        "body": (
            "Your *campaign style* describes broadly how the campaign is structured and the kind of game your players can expect. "
            "You can switch styles between campaigns, or even mid-campaign.\n\n"
            "*ANTHOLOGY* — Sessions and adventures have little narrative cohesion. Each adventure stands alone.\n"
            "*APOCALYPSE* — Play centers around a massive threat to life in the universe (alien invasion, interstellar war, plague, AI revolt).\n"
            "*ENSEMBLE* — Players routinely control multiple characters and switch between them.\n"
            "*EPISODIC* — Heavy emphasis on downtime and roleplaying, frequent time skips and slice-of-life encounters.\n"
            "*HEROIC* — Players are key figures in a large-scale epic struggle with stakes affecting millions.\n"
            "*NARRATIVE* — Players unravel a cohesive narrative as part of the game foreground or background.\n"
            "*OPEN TABLE* — Features a large pool of potential players who may drop in or out each session.\n"
            "*SANDBOX* — Features a large area with many potential leads the players can tackle in any order.\n"
            "*SERIAL* — Play takes place from moment to moment, day to day, with infrequent time skips."
        ),
        "icon": "🎭", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 54, "title": "Campaign Frames", "category_id": 57,
        "source_book_id": 2, "page_number": "42-43", "sort_order": 3,
        "body": (
            "Your campaign *frame* tells players roughly who they are, what kind of work they do, "
            "and the kinds of things they might encounter. "
            "As the game progresses things might change, but the frame sets the right expectations.\n\n"
            "Roll d10 or choose a frame from the Campaign Frames table. "
            "Use it as a starting point — frames are flexible and can be mixed or evolved over time."
        ),
        "icon": "🎬", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 55, "title": "Starting Area & Jump Cluster", "category_id": 57,
        "source_book_id": 2, "page_number": "44-45", "sort_order": 4,
        "body": (
            "Turn to a new spread in your *Campaign Notebook* and copy the map, leaving out all text. "
            "This becomes the starting area: a small Jump-1 cluster in rimspace.\n\n"
            "*MAP LEGEND*\n"
            "• *Solid Lines* — Jump-1 Routes between systems. Label each J1.\n"
            "• *Dotted Lines* — Jump Route to/from the cluster. Roll 1d5+1 for the route number (higher = more remote).\n"
            "• *Empty Circles* — An orbit showing the relationship between dots.\n"
            "• *Filled Dots* — Each dot is a planet, moon, or space station.\n"
            "• *Jump Points* — A dot connected to a Jump Route is the closest location to that Jump Point.\n\n"
            "*KEYING THE MAP*\n"
            "Number each dot, then key the map. Put the first scenario somewhere on the map. "
            "Fill in the key over time using scenarios you prep and official modules. "
            "Do not fill it all in at once — wait to see what your players care about. "
            "Write a scrap of an idea for each location, enough to say something is there, then move on.\n\n"
            "💡 *Good prep is a terrible substitute for good play.*\n\n"
            "*FINDING NEW JUMP ROUTES*\n"
            "Only the most powerful corporations and governments have resources to explore hyperspace. "
            "Finding new routes can be a mission precursor or reward for a job well done. "
            "Always be adding to the map, growing it into a sprawling atlas."
        ),
        "icon": "🌌", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 56, "title": "Factions", "category_id": 57,
        "source_book_id": 2, "page_number": "46", "sort_order": 5,
        "body": (
            "Players will interact with organizations, corporations, cults, gangs, and other groups — called *factions.* "
            "They operate as allies, enemies, and employers.\n\n"
            "*CREATING A FACTION*\n"
            "Title a new page in your Campaign Notebook with the faction's name, then note:\n"
            "• *VIPs* — Important members with short descriptions and page references.\n"
            "• *Locations* — Notable locations with map or scenario references.\n"
            "• *Goals* — Compelling goals that will affect players if completed.\n\n"
            "Factions become most useful once your players have encountered two or three. "
            "This creates situations where players must choose between competing interests.\n\n"
            "*FACTION GOALS*\n"
            "Assign each goal a number of boxes (1-2 for easy, 5-10 for difficult). "
            "Roll 1d100 at regular intervals that fit your game's pace:\n"
            "• *Odds* — Faction makes progress. Fill in a box.\n"
            "• *Evens* — Faction hits an obstacle. Mark a box with X.\n"
            "• *Even doubles* — Breakthrough! Mark off two boxes (or fill one marked X).\n"
            "• *Odd doubles* — Catastrophe. Erase a filled box.\n"
            "• *All boxes filled* — Faction achieves its goal."
        ),
        "icon": "🏴", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 57, "title": "The Company", "category_id": 57,
        "source_book_id": 2, "page_number": "47", "sort_order": 6,
        "body": (
            "The first faction to design is *the Company* — the interstellar megacorporation dominating the corporate-controlled future of Mothership.\n\n"
            "The Company can serve as:\n"
            "• *Primary employer or client* — Players have to work for someone, and the Company has the resources.\n"
            "• *Principal antagonist* — A persistent, faceless, inexhaustible threat that keeps coming back.\n"
            "• *Framing device* — Tells you what work players will do and what technologies foreground your setting.\n\n"
            "*CORPORATE MIND MAP*\n"
            "On a new page, write The Company in the center and circle it. "
            "Draw connections: important people, subsidiaries, secret projects, planets, ports, and enemies. "
            "Add to it as time goes on.\n\n"
            "*CORPORATE POWER*\n"
            "Assume functionally unlimited resources. Assume it is above the law. "
            "Assume it always has another crew — just as disposable, just as desperate — to clean up if your players cannot. "
            "Assume illegal research, regulatory violations, bribery, negligence, and embezzlement. "
            "Assume invasive biometric tracking, industrial sabotage, proxy wars, human experimentation, rampant pollution. "
            "Assume their products cause cancer. Assume they secretly fund terrorist groups. "
            "Assume they have done all of this before. *Assume they will never stop.*"
        ),
        "icon": "🏢", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 58, "title": "Work & Job Board", "category_id": 57,
        "source_book_id": 2, "page_number": "48", "sort_order": 7,
        "body": (
            "Keeping an updated *Job Board* ensures players always have new work. "
            "Create one with 1d5 jobs:\n\n"
            "1. Title a new Campaign Notebook spread *Job Board.*\n"
            "2. Create a table with headers: *Job, Client, Pay,* and *Location.*\n"
            "3. Roll or choose from the *Contract Work Table.*\n"
            "4. Roll or choose from the *Pay Scale Table* for each job.\n"
            "5. Assign a faction as the client, with a specific contact if relevant.\n"
            "6. Note where players can meet the client to start the job.\n\n"
            "Prune and add entries over time. "
            "Start with one new job and one removed job per in-game year.\n\n"
            "*NEGOTIATING RATES*\n"
            "Adjust pay by 10% per factor:\n"
            "• Crew's reliable/unreliable reputation.\n"
            "• Previous good/bad work for this client.\n"
            "• Client is desperate/has other options.\n"
            "• Work is time-sensitive/dangerous.\n\n"
            "Beyond that, the client walks away looking for other options."
        ),
        "icon": "📋", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 59, "title": "Pay", "category_id": 57,
        "source_book_id": 2, "page_number": "49", "sort_order": 8,
        "body": (
            "*SALARY*\n"
            "Players working for the Company earn a monthly salary based on skills:\n"
            "• *500cr/month* per Trained Skill.\n"
            "• *1,000cr/month* per Expert Skill.\n"
            "• *2,000cr/month* per Master Skill.\n\n"
            "*JUMP PAY*\n"
            "A flat bonus equal to Jump x 1,000cr, regardless of distance or time in hyperspace.\n\n"
            "*HAZARD PAY*\n"
            "During incredibly dangerous work: 1d5 months of salary as a bonus. "
            "This does not constitute an admission of liability on the part of the Company or its agents."
        ),
        "icon": "💰", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 60, "title": "Campaign Economics & Debt", "category_id": 57,
        "source_book_id": 2, "page_number": "50", "sort_order": 9,
        "body": (
            "Money in Mothership limits options — another resource like Health and Stress to manage, on a longer time scale.\n\n"
            "• The shorter the campaign, the less important economics are.\n"
            "• *Favors and information are more interesting rewards than credits.*\n"
            "• *This is a horror game, not a small business simulator.*\n"
            "• *Upper mobility is statistically impossible.* Wealth is concentrated in a few generationally wealthy companies and families.\n\n"
            "*NET WORTH*\n"
            "• *Hundreds* — Food, shelter.\n"
            "• *Thousands* — Weapons, equipment, Shore Leave, rent, space travel.\n"
            "• *Hundreds of thousands* — Cybermods, contractors, skill training, vehicles.\n"
            "• *Millions* — Ship repairs, fuel, maintenance.\n"
            "• *Tens of millions* — Mechs, small spacecraft, businesses.\n"
            "• *Hundreds of millions* — Ships, asteroids, small fleets.\n"
            "• *Billions* — Companies, moons, private armies.\n"
            "• *Trillions* — War, colonization, planets, space stations.\n\n"
            "*DEBT*\n"
            "Debt means owing violent people a non-trivial amount of money. "
            "Increase Minimum Stress by 1 for every significant debtor owed.\n\n"
            "*Securing a Loan:*\n"
            "• Downpayment of 1d5x10% up front, or equivalent collateral.\n"
            "• Interest equal to the amount borrowed — players pay back twice as much.\n"
            "• Term: 2d10 months. Payments of 10% of total owed per month.\n\n"
            "*Consequences for Non-Payment:*\n"
            "Violent debt collectors, targeted malware, threats to allies, blacklisting, repossession, "
            "credstick freezes, kidnap and ransom, forced relocation to debtor colonies, or a bounty on the debtor's life."
        ),
        "icon": "📊", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 61, "title": "Getting Rich", "category_id": 57,
        "source_book_id": 2, "page_number": "51", "sort_order": 10,
        "body": (
            "*SAVING MONEY*\n"
            "On a day-to-day basis, players save whatever salary they do not spend. "
            "With large time skips: players can save *one month's salary per year.* "
            "Saving extra requires raising Minimum Stress by the same amount.\n\n"
            "*WHAT IF THEY GET RICH?*\n\n"
            "1. *Big money attracts big predators.* Windfall gains paint a target on players' backs. "
            "Piracy increases, corrupt customs inspectors appear, enemies form alliances.\n\n"
            "2. *Allies will suddenly need help.* Wealthy players attract desperate allies seeking emergency funding. "
            "Family and friends become kidnap-and-ransom targets.\n\n"
            "3. *Old money hates new money.* High society does not welcome new members. Expect skeptics and scam artists.\n\n"
            "4. *It's okay to retire. For now.* Megarich players may retire in style. "
            "The character operates as an ally or NPC — until called back for one last job.\n\n"
            "*RETIREMENT COSTS*\n"
            "• *1mcr* — Fixed income. Cramped homeworld. Part-time job.\n"
            "• *10mcr* — Second home. Core world. S-Class vacations. Space travel.\n"
            "• *100mcr* — Social elite. Multiple homes. Life of luxury.\n"
            "• *1bcr* — Shareholder. Megayacht. Board seat. Private asteroid.\n"
            "• *10bcr* — C-level ancestral home. Space station. Personal army.\n"
            "• *100bcr* — Noble title. Company owner. Private planet. Personal fleet."
        ),
        "icon": "💎", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
    {
        "id": 62, "title": "House Rules", "category_id": 57,
        "source_book_id": 2, "page_number": "52", "sort_order": 11,
        "body": (
            "Common house rules that adjust difficulty up or down. "
            "Add any that work for your group to the *House Rules* page in your Campaign Notebook.\n\n"
            "*ABLATIVE WOUNDS* — Players gain 1 extra Wound that, when lost, requires no Wound table roll. Regained with 30m rest.\n"
            "*ARMOR DEGRADATION* — AP reduced by 1 whenever excess Damage is dealt. Destroyed at 0 AP.\n"
            "*CRITICAL STRESS RELIEF* — Critical Success reduces Stress by 1.\n"
            "*EXHAUSTABLE SKILLS* — Auto-succeed each Skill once per session.\n"
            "*FRAGILITY* — All players get 1 Wound (androids get 5).\n"
            "*HIGH SCORE BREAKER* — Beating your High Score grants 20 points to divide between Stats and Saves.\n"
            "*IMPENETRABLE WOUNDS* — Damage does not carry over after a Wound is received.\n"
            "*IMPROVED ADVANCEMENT* — Stats and Saves can both improve from Shore Leave.\n"
            "*LETHALITY* — Ignore Health, use only Wounds. All weapons deal 1+ Wounds.\n"
            "*LIGHT AMMO TRACKING* — Track ammo only when narratively relevant; then assume 1d5 shots remaining.\n"
            "*OPT-IN STRESS* — Players volunteer to take Stress and make Panic Checks when appropriate.\n"
            "*PLAYER FACING ROLLS* — Players make all rolls; failure in combat could mean being hit instead.\n"
            "*RAPID SKILL LEARNING* — Trained in 3 sessions, Expert in 5, Master in 10.\n"
            "*RESOLVE* — Each session survived grants 1 Resolve, spendable as a free reroll.\n"
            "*SIMPLE SKILLS* — Ignore Skill bonuses; all Skills grant Advantage instead.\n"
            "*SKILLS AS WISHLIST* — After session 1, note your players' skills. "
            "Treat this as a wishlist of what they want to see. Hit one or two each session."
        ),
        "icon": "⚙️", "title_ua": "", "title_ru": "", "body_ua": "", "body_ru": ""
    },
]

with open('C:/Git/mothership/seeds/rules.json', encoding='utf-8') as f:
    rules = json.load(f)
rules.extend(rules_to_add)
with open('C:/Git/mothership/seeds/rules.json', 'w', encoding='utf-8') as f:
    json.dump(rules, f, ensure_ascii=False, indent=2)
print(f"Added {len(rules_to_add)} rules. Total: {len(rules)}")

# ── 5. CONTENT TERM LINKS ──────────────────────────────────────────────
with open('C:/Git/mothership/seeds/content_term_links.json', encoding='utf-8') as f:
    links = json.load(f)

lid = 119  # next after max 118

def link(content_type, content_id, term_id, sort_order=0):
    global lid
    l = {"id": lid, "content_type": content_type, "content_id": content_id,
         "term_id": term_id, "sort_order": sort_order}
    lid += 1
    return l

new_links = [
    # Campaign Frames (rule:54 → term:49, table:27 → term:49)
    link("rule", 54, 49, 1),
    link("roll_table", 27, 49),

    # Contract Work (rule:58 → term:50, table:28 → term:50)
    link("rule", 58, 50, 1),
    link("roll_table", 28, 50),

    # Pay Scale (rule:59 → term:51, table:29 → term:51)
    link("rule", 59, 51, 1),
    link("roll_table", 29, 51),

    # Pay (rule:59) → existing terms
    link("rule", 59, 14, 2),   # Shore Leave
    link("rule", 59, 48, 3),   # Train a Skill

    # Economics (rule:60) → existing terms
    link("rule", 60, 3, 1),    # Stress
    link("rule", 60, 4, 2),    # Minimum Stress
    link("rule", 60, 14, 3),   # Shore Leave

    # Getting Rich (rule:61) → existing terms
    link("rule", 61, 4, 1),    # Minimum Stress

    # House Rules (rule:62) → existing terms
    link("rule", 62, 7, 1),    # Wound
    link("rule", 62, 13, 2),   # Armor Points
    link("rule", 62, 3, 3),    # Stress
    link("rule", 62, 10, 4),   # Critical Success
    link("rule", 62, 14, 5),   # Shore Leave
    link("rule", 62, 1, 6),    # Advantage
]

links.extend(new_links)
with open('C:/Git/mothership/seeds/content_term_links.json', 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)
print(f"Added {len(new_links)} links. Total: {len(links)}")
