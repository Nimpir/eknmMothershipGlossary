FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python seed.py && \
    python scripts/add_character_page.py && \
    python scripts/add_psw_combat.py && \
    python scripts/add_psw_weapons.py && \
    python scripts/add_psw_character.py && \
    python scripts/add_psw_tables.py && \
    python scripts/add_psw_equipment.py && \
    python scripts/add_psw_rules.py && \
    python scripts/add_psw_skills.py && \
    python scripts/add_psw_survival.py && \
    python scripts/add_psw_medical.py && \
    python scripts/add_psw_downtime.py && \
    python scripts/add_psw_armour.py && \
    python scripts/add_content_links.py && \
    python scripts/update_nav_and_descriptions.py

CMD ["python", "-m", "bot.bot"]
