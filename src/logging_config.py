"""
Centralised logging configuration.

- INFO 以上をコンソールにカラー表示（colorlog）
- DEBUG 以上を logs/app.log へローテーション保存（1 MB × 5 ファイル）
"""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path

from colorlog import ColoredFormatter

# --------------------------------------------------------------------------- #
# パス準備                                                                     #
# --------------------------------------------------------------------------- #
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# --------------------------------------------------------------------------- #
# dictConfig 定義                                                              #
# --------------------------------------------------------------------------- #
LOGGING_DICT: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "color": {
            "()": ColoredFormatter,
            # ★ 100 文字を超えないよう 2 行に折り返し（PEP 8 / Ruff E501）
            "format": (
                "%(log_color)s[%(asctime)s] %(levelname)-8s "
                "%(name)s:%(lineno)d | %(message)s"
            ),
            "log_colors": {
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bold",
            },
        },
        "simple": {
            "format": "[%(asctime)s] %(levelname)-8s %(name)s:%(lineno)d | %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "color",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": str(LOG_DIR / "app.log"),
            "maxBytes": 1_000_000,  # 1 MB
            "backupCount": 5,
            "encoding": "utf-8",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
}

# --------------------------------------------------------------------------- #
# API                                                                          #
# --------------------------------------------------------------------------- #
def configure_logging() -> None:
    """Apply dictConfig at import-time."""
    logging.config.dictConfig(LOGGING_DICT)
