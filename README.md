# web-ui-app

ローカル PC で **Streamlit** を使い  
パチスロ差枚データなどを “すぐ可視化” する **完全個人向けツール** です。  
「ポチッ → ブラウザ表示」までをワンコマンド化しています。

---

## 1. 30 秒クイックスタート

## 1-A. Python で動かす (3 行 + 1 行)

```powershell
# ① 仮想環境をつくって有効化
python -m venv .venv && .\.venv\Scripts\activate
# ② 依存をインストール
pip install -r requirements.txt      # ← ここまでセットアップ 3 行
# ③ アプリ起動
streamlit run app.py                 # ← 起動 1 行


■1-B. 依存ゼロで動かす (Docker 2 行)
# ① 初回かバージョン更新時だけビルド
docker build -t messe_ui:0.3 .
# ② 実行 & ブラウザ起動
docker run --rm -p 8501:8501 --name messe_ui messe_ui:0.3 ^
  && start http://localhost:8501/

■2. プロジェクト構成

messe_mitaka_UI/
├─ data/              サンプル CSV 等
├─ src/               読み込み・加工・描画ロジック
├─ tests/             Pytest
├─ app.py             Streamlit エントリポイント
├─ Dockerfile         ビルド定義
├─ requirements.txt   最小依存ライブラリ
└─ README.md          このファイル


■3. 開発メモ（自分用）

git add README.md dev_master_checklist.md
git commit -m "docs: update README & checklist"
git push


