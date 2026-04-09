import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Remove rule:54 (Campaign Frames — thin wrapper, table:27 already in cat:57 directly)
with open('C:/Git/mothership/seeds/rules.json', encoding='utf-8') as f:
    rules = json.load(f)
rules = [r for r in rules if r['id'] != 54]
with open('C:/Git/mothership/seeds/rules.json', 'w', encoding='utf-8') as f:
    json.dump(rules, f, ensure_ascii=False, indent=2)
print(f'Removed rule:54. Rules count: {len(rules)}')

# 2. Remove content_term_links for rule:54
with open('C:/Git/mothership/seeds/content_term_links.json', encoding='utf-8') as f:
    links = json.load(f)
links = [l for l in links if not (l['content_type'] == 'rule' and l['content_id'] == 54)]
with open('C:/Git/mothership/seeds/content_term_links.json', 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)
print(f'Removed rule:54 links. Links count: {len(links)}')

# 3. Update table descriptions using term body text
with open('C:/Git/mothership/seeds/terms.json', encoding='utf-8') as f:
    terms = json.load(f)
term_map = {t['id']: t for t in terms}

with open('C:/Git/mothership/seeds/roll_tables.json', encoding='utf-8') as f:
    tables = json.load(f)

updates = {
    27: term_map[49]['body'],  # Campaign Frames description from term:49
    28: term_map[50]['body'],  # Contract Work description from term:50
    29: term_map[51]['body'],  # Pay Scale description from term:51
}
for t in tables:
    if t['id'] in updates:
        t['description'] = updates[t['id']]
        print(f"table:{t['id']} ({t['name']}) description updated")

with open('C:/Git/mothership/seeds/roll_tables.json', 'w', encoding='utf-8') as f:
    json.dump(tables, f, ensure_ascii=False, indent=2)
