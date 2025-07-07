"""
Centralised logging configuration.

- INFO 以上をコンソールにカラー表示（colorlog）
- DEBUG 以上を logs/app.log へローテーション保存（1 MB × 5 ファイル）
"""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path
from typing import Any

from colorlog import ColoredFormatter

# ────────────────────────────────────────────────────────────────
#  フォルダ準備
# ────────────────────────────────────────────────────────────────
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# ────────────────────────────────────────────────────────────────
#  dictConfig 用設定
# ────────────────────────────────────────────────────────────────
LOGGING_DICT: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    #
    "formatters": {
        "color": {
            "()": ColoredFormatter,
            "format": (
                "%(log_color)s[%(asctime)s] "
                "%(levelname)-8s %(name)s:%(lineno)d | %(message)s"
            ),
            "log_colors": {
                "DEBUG":    "cyan",
                "INFO":     "green",
                "WARNING":  "yellow",
                "ERROR":    "red",
                "CRITICAL": "bold_red",
            },
        },
        "plain": {
            "format": "[%(asctime)s] %(levelname)-8s %(name)s:%(lineno)d | %(message)s",
        },
    },
    #
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "color",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "plain",
            "level": "DEBUG",
            "filename": str(LOG_DIR / "app.log"),
            "maxBytes": 1_048_576,   # 1 MB
            "backupCount": 5,
            "encoding": "utf-8",
        },
    },
    #
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}

# ────────────────────────────────────────────────────────────────
#  公開 API
# ────────────────────────────────────────────────────────────────
def configure_logging() -> None:
    """Apply `LOGGING_DICT`. 何度呼んでも安全."""
    logging.config.dictConfig(LOGGING_DICT)


__all__ = ["configure_logging", "LOGGING_DICT"]
