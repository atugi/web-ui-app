"""Project-wide settings & path helpers."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

# --------------------------------------------------
# 1) ルート / サブディレクトリのパスを集中管理
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent           # …/messe_mitaka_UI
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# 必要なら自動生成
for _d in (DATA_DIR, LOG_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 2) .env を読み込む   （python-dotenv）
# --------------------------------------------------
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE, override=False)   # .env が無くてもエラーにしない

# --------------------------------------------------
# 3) キャッシュ付きで環境変数を取得
# --------------------------------------------------
@lru_cache(maxsize=None)
def get_env(key: str, default: str | None = None) -> str | None:
    """環境変数 `key` を取得（無ければ default）。"""
    return os.getenv(key, default)
