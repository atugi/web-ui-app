"""messe_mitaka_UI package bootstrap.

- Kick-starts logging when the package is imported
- Re-exports public symbols from loader.py
"""

# ── ロギング設定を先に読み込む ──────────────────────
# ── パッケージ公開 API ────────────────────────────
from .loader import SCHEMA_PATH, load_csv_with_schema
from .logging_config import *  # noqa: F401,F403  ← ピリオド付き！

__all__: list[str] = [
    "SCHEMA_PATH",
    "load_csv_with_schema",
]
