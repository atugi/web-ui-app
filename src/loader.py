# src/loader.py
import json
from pathlib import Path
import pandas as pd

SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "csv_columns.json"


def load_csv_with_schema(csv_path: str | Path) -> pd.DataFrame:
    """CSV を読み込み、列スキーマを検証して DataFrame を返す"""
    csv_path = Path(csv_path)

    # --- スキーマ読み込み ---
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    required_cols: list[str] = schema["columns"]

    # --- CSV 読み込み ---
    df = pd.read_csv(csv_path)

    # --- 検証 ---
    missing = [c for c in required_cols if c not in df.columns]
    extra = [c for c in df.columns if c not in required_cols]

    if missing or extra:
        raise ValueError(f"Schema mismatch\n  missing: {missing}\n  extra: {extra}")

    return df
