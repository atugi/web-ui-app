"""
Central logging config – import once, then just
    from logging import getLogger
    log = getLogger(__name__)
"""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path

# ── ログファイル保存先 ────────────────────────────────
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

# ── dictConfig 定義 ──────────────────────────────────
LOGGING_DICT = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "fmt": {
            "format": "%(asctime)s | %(levelname)-8s | %(name)s:%(lineno)d — %(message)s"
        },
        "color": {  # human-friendly colorized console
            "format": "%(log_color)s%(levelname)-8s%(reset)s | %(message)s",
            "()": "colorlog.ColoredFormatter",
            "log_colors": {
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "purple",
            },
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "color",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": str(LOG_FILE),
            "maxBytes": 1_000_000,
            "backupCount": 3,
            "encoding": "utf-8",
            "formatter": "fmt",
            "level": "DEBUG",
        },
    },
    "root": {  # 全体のデフォルト
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}

logging.config.dictConfig(LOGGING_DICT)
