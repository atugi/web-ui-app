"""messe_mitaka_UI package bootstrap.

- Kick-starts logging when the package is imported
- Re-exports public symbols from loader.py
"""

# --- ロギング設定を最初に適用する ------------------------------------------
from .logging_config import configure_logging  # noqa: F401

configure_logging()  # <- これで dictConfig が1回だけ実行される

# --- パッケージ公開 API ------------------------------------------------------
from .loader import SCHEMA_PATH, load_csv_with_schema  # noqa: E402

__all__: list[str] = [
    "SCHEMA_PATH",
    "load_csv_with_schema",
]
