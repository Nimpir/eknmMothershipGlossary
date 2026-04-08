# Mothership RPG Reference Bot

A Telegram inline-keyboard bot that serves as a table-side handbook for the **Mothership 1e** tabletop RPG. Players and Wardens can browse rules, look up glossary terms, view equipment, ships, and NPCs, and roll on random tables — all without leaving the Telegram chat.

---

## Features

- **Rules browser** — Combat, Stress & Panic, Survival & Hazards, Medical Care, and more
- **Glossary** — 47 indexed terms with paginated navigation
- **Equipment** — Weapons, Armor, Gear & Tools with stats and costs
- **Skills** — Full 42-skill tree (Trained / Expert / Master) with prerequisites
- **Roll tables** — 22 tables (Panic, Wounds, Loadouts, Trinkets, Patches, and module-specific tables)
- **Ships** — Ship catalogue with stat blocks
- **Modules** — Locations and NPCs for ABH, Dead Planet, Gradient Descent, and A Pound of Flesh
- **Dice roller** — `/roll d10`, `/roll 2d10`, `/roll d100`
- **Full-text search** — `/search <term>` across all content types
- **Persistent navigation** — Back button with full history; state survives bot restarts

---

## Source Books

| Code | Title |
|------|-------|
| PSG | Player's Survival Guide |
| WOM | Warden's Operations Manual |
| ABH | Another Bug Hunt |
| GD | Gradient Descent |
| ST | Shipbreaker's Toolkit |
| APF | A Pound of Flesh |
| DP | Dead Planet |

---

## Setup

### 1. Create a Telegram Bot and get a token

1. Open Telegram and start a chat with [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the prompts (choose a name and username)
3. BotFather will reply with your **bot token** — copy it, you'll need it in `.env`

### 2. Register bot commands (optional but recommended)

Still in the BotFather chat, send `/setcommands`, select your bot, then paste:

```
start - Open the main menu
search - Search all content, e.g. /search wound
roll - Roll dice, e.g. /roll d10 or /roll 2d10
lang - Change language EN / UA / RU
```

This makes the commands appear in the Telegram command menu (the `/` button).

### 3. Environment Variables

Copy `.env.example` to `.env` and fill in:

```
BOT_TOKEN=your_telegram_bot_token
DB_PATH=mothership.db
DEV_MODE=false
```

Set `DEV_MODE=true` during development to show the live navigation stack on every message.

---

## Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Seed the database
python seed.py

# Start the bot
python -m bot.bot
```

---

## Docker (Production)

### First Deploy

```bash
git clone <repo-url>
cd mothership
cp .env.example .env
# Edit .env — set BOT_TOKEN, leave DEV_MODE=false
sudo docker-compose up -d --build
```

### Update After Code Changes

```bash
bash update.sh
```

This pulls the latest git changes, rebuilds the image (including reseeding the DB), and restarts the container.

---

## Project Structure

```
mothership/
├── bot/
│   ├── bot.py              # Entry point — handlers, nav stack, callback router
│   ├── db.py               # All SQLite query functions
│   ├── formatters.py       # Message text builders (HTML parse mode)
│   ├── keyboards.py        # InlineKeyboardMarkup builders
│   └── logging_setup.py    # Rotating file + console logging
├── seeds/                  # JSON seed data (one file per table)
├── schema.sql              # Full DB schema
├── seed.py                 # Drops and recreates the DB from seed files
├── Dockerfile
├── docker-compose.yml
├── update.sh               # Pull + rebuild + restart helper
├── requirements.txt
└── .env.example
```

---

## Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Open the main menu |
| `/search <term>` | Full-text search across all content |
| `/roll <notation>` | Roll dice (e.g. `d10`, `2d10`, `d100`) |
| `/lang` | Change language (🇬🇧 EN / 🇺🇦 UA / 🇷🇺 RU) |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| Telegram library | python-telegram-bot 21.6 (async) |
| Database | SQLite (stdlib `sqlite3`) |
| Config | `python-dotenv` |
| Deployment | Docker + docker-compose |

---

## License

See [LICENSE](LICENSE).
