
# 開発フルセーフティ・マスターチェックリスト  
*生成日: 2025-07-01*

各タスクの `[ ]` を `[x]` に変えて進捗管理してください。  
途中で工程追加/削除が必要なら、このファイルを直接編集して OK です。

---

## 0. プロジェクト初期化
- [x] **Git 初期化** `git init` → `.gitignore` 生成（Python 用）
- [x] **GitHub リポジトリ作成** → `origin` 登録 → `main` ブランチ push
- [x] **ライセンス & README 雛形** 作成

## 1. 環境セットアップ
- [x] **Python 仮想環境** `python -m venv .venv` & activate
- [x] **依存ファイル** `pyproject.toml` *or* `requirements.txt` 作成
- [x] **pre-commit 導入** (`black`, `ruff`, `mypy`)
  ```bash
  pip install pre-commit black ruff mypy
  pre-commit install
  ```

## 2. データ契約 (スキーマ)
- [x] `schemas/csv_columns.json` に必須11列を書き込む
- [x] `docs/CONTRACT.md` で列説明・禁止変更事項を定義
- [x] データロード関数でスキーマ検証を組み込む

## 3. ゴールデンデータ & テスト基盤
- [x] Notebook で正解出力を CSV 保存 (`tests/data/expected_*.csv`)
- [x] **pytest** 導入 (`pip install pytest`)
  - [x] 成功ケース
  - [x] 失敗/境界ケース
- [x] **mypy strict** 設定
- [x] **ruff** 設定 (`pyproject.toml`)

## 4. CI / CD
- [x] GitHub Actions: `.github/workflows/ci.yml`
  - pytest, mypy, ruff, pre-commit の全ジョブ
- [x] main マージ時に CI 緑必須設定

## 5. ロギング & 例外処理
- [x] `logging` 基本設定 (file & console)
- [x] Streamlit エラー表示 `st.error` + トレースバック

## 6. 設定 & パス管理
- [x] `settings.py` にパス定義
- [x] `.env` にローカル差異を書く (`python-dotenv`)

## 7. UI プロトタイプ
- [x] `pip install streamlit`
- [x] `app.py` で
  - ファイルアップロード
  - “Hello World” 表示ボタン

## 8. Docker / 配布
- [ ] `Dockerfile` 作成（python:3.12-slim など）
- [ ] `docker-compose.yml` （optional）
  - web (Streamlit)
  - db (if future)

## 9. ドキュメント整備
- [x] `README.md` にセットアップ3行・起動1行
- [ ] CHANGELOG.md 初版
- [ ] ISSUE & PR テンプレ GitHub に配置

## 10. 例示的開発サイクル
- [ ] **Issue** 登録例: “累積差枚グラフ表示”
- [ ] **feature ブランチ** `git checkout -b feature-cumsum`
- [ ] コード追加 → pytest 緑確認
- [ ] **PR** 作成 → CI 緑 → レビュー → main マージ

---

### 運用ルール
1. 新タスクは **Issue → ブランチ → PR** を必ず踏む
2. 列追加・変更時は **schemas/csv_columns.json と CONTRACT.md を同時更新**
3. テストが失敗したバグは **テストを修正する前にロジックを直す**
4. main ブランチはいつでも `docker compose up` で起動できる状態に保つ

---

> **メモ**: 不要工程は `~~[ ] ...~~` と打ち消し線を付けて残すと履歴が分かりやすいです。
