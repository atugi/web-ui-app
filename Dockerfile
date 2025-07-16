# ───────── ベースイメージ ─────────
FROM python:3.12-slim

# ───────── 作業ディレクトリ ─────────
WORKDIR /app

# ───────── 依存関係 ─────────
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ───────── アプリ本体 ─────────
COPY src/ ./src/
COPY app.py ./

# ───────── 環境変数ファイル ─────────
# .env.example は空でも OK。機密は絶対に入れない！
#   将来実際の環境変数を使う場合は
#   ・ここはこのまま
#   ・CI/CD や docker run 時の -e オプションで値を上書き
COPY .env.example ./.env

# ───────── ポートを開ける (Streamlit のデフォルト 8501) ─────────
EXPOSE 8501

# ───────── エントリーポイント ─────────
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
