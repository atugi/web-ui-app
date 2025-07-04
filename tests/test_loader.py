from __future__ import annotations

# ── 標準ライブラリ ─────────────────────────────
import json
from pathlib import Path

# ── サードパーティ ────────────────────────────
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

# ── 自作モジュール ─────────────────────────────
from src.loader import (
    SCHEMA_PATH,
    load_csv_with_schema,
)  # isort: skip  (相対 import を維持)

# ──────────────────────────────────────────────
# ★ ファイルパス定義
DATA_DIR = Path(__file__).parent / "data"
RAW = DATA_DIR / "raw_sample.csv"
EXPECTED = DATA_DIR / "expected_loader_head.csv"
BAD_MISSING_COLS = DATA_DIR / "bad_missing_cols.csv"

# スキーマに列定義を追加したくなったら、loader 側の csv_columns.json だけ直せば
# ここは自動で追従します。
REQUIRED_COLS: list[str] = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))[
    "columns"
]


# ── テスト: 先頭 10 行が正しく読める ───────────────────────────
def test_loader_head() -> None:
    df_expected = pd.read_csv(EXPECTED, encoding="utf-8")
    df_actual = load_csv_with_schema(RAW).head(10).reset_index(drop=True)
    assert_frame_equal(df_actual, df_expected, check_like=False)


# ── テスト: 正常系フルロード ────────────────────────────────
def test_loader_success_columns_and_rows() -> None:
    """列名と 0 行でないことを確認"""
    df = load_csv_with_schema(RAW).reset_index(drop=True)
    # 列が完全一致しているか（順序も含む）
    assert list(df.columns) == REQUIRED_COLS
    # 行数が 0 でない
    assert len(df) > 0


# ── テスト: 異常系（必須列欠落）──────────────────────────────
def test_loader_failure_missing_columns() -> None:
    """必須列が欠けている CSV は ValueError を投げる"""
    with pytest.raises(ValueError, match="Schema mismatch"):
        load_csv_with_schema(BAD_MISSING_COLS)
