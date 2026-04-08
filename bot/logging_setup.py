"""
logging_setup.py — Centralised logging configuration for the Mothership bot.

Outputs:
  - Console  : INFO and above
  - logs/bot.log    : INFO and above, rotating (5 MB × 3 backups)
  - logs/errors.log : ERROR and above, rotating (2 MB × 5 backups)
"""

import logging
import logging.handlers
from pathlib import Path

LOGS_DIR = Path(__file__).parent.parent / "logs"

_FMT = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
_DATE_FMT = "%Y-%m-%d %H:%M:%S"


def setup_logging(level: int = logging.INFO) -> None:
    LOGS_DIR.mkdir(exist_ok=True)

    formatter = logging.Formatter(_FMT, datefmt=_DATE_FMT)

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)

    all_file = logging.handlers.RotatingFileHandler(
        LOGS_DIR / "bot.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    all_file.setLevel(level)
    all_file.setFormatter(formatter)

    error_file = logging.handlers.RotatingFileHandler(
        LOGS_DIR / "errors.log",
        maxBytes=2 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    error_file.setLevel(logging.ERROR)
    error_file.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)
    root.addHandler(console)
    root.addHandler(all_file)
    root.addHandler(error_file)
