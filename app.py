"""Minimal Streamlit prototype.

機能
------
1. ファイルアップロード  
2. “Hello World” ボタン（.env からあいさつ文を読む）  
3. 例外表示デモ（ゼロ除算を try/except で捕捉）

実行方法
---------
$ streamlit run app.py
"""

from __future__ import annotations

import traceback

import streamlit as st

from src import settings

st.title("Demo: Streamlit prototype")

# --- 1. ファイルアップロード -----------------------------
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    content = uploaded_file.read()
    st.write(f"Uploaded file size: {len(content):,} bytes")

# --- 2. “Hello World” ボタン ------------------------------
if st.button("Say hello"):
    st.success(settings.get_env("SAMPLE_GREETING"))

# --- 3. 例外表示デモ ------------------------------------
with st.expander("Show error-handling demo"):
    try:
        1 / 0  # noqa: B018  # わざと ZeroDivisionError
    except Exception as exc:  # noqa: BLE001
        st.error(f"{exc.__class__.__name__}: {exc}")
        st.code(traceback.format_exc(), language="python")
