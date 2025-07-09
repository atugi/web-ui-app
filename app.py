"""Minimal Streamlit prototype.

機能
------
1. ファイルアップロード
2. “Hello World” ボタン（.env からあいさつ文を読む）
3. 例外表示デモ（ゼロ除算を try/except で捕捉）

実行方法
----------
$ streamlit run app.py
"""
from __future__ import annotations

import traceback
from pathlib import Path

import streamlit as st

from src import settings

st.title("Demo: Streamlit prototype")

# --- 1. ファイルアップロード --------------------------------------------
st.subheader("1. ファイルアップロード")
uploaded = st.file_uploader("CSV をアップロード", type=["csv"])
if uploaded:
    save_path = Path("data") / uploaded.name
    save_path.parent.mkdir(exist_ok=True)
    save_path.write_bytes(uploaded.getbuffer())
    st.success(f"保存しました → {save_path}")

# --- 2. “Hello World” ボタン ---------------------------------------------
st.subheader("2. “Hello World” ボタン")
greeting = settings.get_env("SAMPLE_GREETING", default="Hello World!")
if st.button("Say Hello"):
    st.write(greeting)

# --- 3. 例外表示デモ ------------------------------------------------------
st.subheader("3. 例外表示デモ")
try:
    raise ZeroDivisionError("division by zero")  # ← ★ ここを修正
except ZeroDivisionError:
    st.error("ZeroDivisionError: division by zero")
    st.code(traceback.format_exc(), language="python")
