# CSV Manager プロジェクト – マスターチェックリスト

## フェーズ1：Jupyter Notebook 実装（※このチャットで対応）

### A. 環境準備
- [x] **新しい Notebook** を作成（例: `messe_csv_manager.ipynb`）
- [x] 必要ライブラリのインストール確認：  
      `import pandas, pyarrow` がエラーなく実行できる
- [x] **インポートセル**を追加  
  ```python
  from pathlib import Path
  import shutil
  import pandas as pd
  from datetime import datetime
  ```

### B. File‑Mover v0.1（Downloads → 年/月/日 フォルダへ移動）
- [x] **定数を定義**  
  ```python
  DOWNLOADS = Path.home() / "Downloads"
  DST_ROOT  = Path.home() / "Downloads/messe-mitaka-html/csv"
  ```
- [x] **`move_new_csv()` を実装**  
  1. `DOWNLOADS.glob("messe_*.csv")` で対象 CSV を列挙  
  2. ファイル名から `YYYY-MM-DD` を抽出し、日付を取得  
  3. `DST_ROOT / YYYY-MM / YYYY-MM-DD` というフォルダを自動生成（`mkdir(parents=True, exist_ok=True)`)  
  4. 同名ファイルが既に存在する場合は **スキップ**、無ければ `shutil.move()`  
  5. `Moved:` / `Skipped:` を `print()` で表示
- [x] **テスト実行**  
  - Downloads にダミー CSV を置き、`move_new_csv()` を実行  
  - 対象ファイルが正しいフォルダへ移動し、ログが正しいことを確認

### C. Master Updater v0.2（Parquet 更新＋曜日列追加）
- [x] **`update_master()` を実装**  
  1. `slot_master.parquet` を読み込み（存在しなければ空 DataFrame）  
  2. `DST_ROOT.rglob("messe_*.csv")` で CSV を再帰的に取得  
  3. 各 CSV に `日付` 列を追加し、未取込データだけを結合  
  4. `曜日` 列を `pd.to_datetime(...).dt.strftime('%a')` で追加  
  5. Parquet へ保存
- [x] **テスト実行**  
  - `update_master()` を実行し、追加行数・スキップ行数を確認  
  - Parquet を再読み込みし、`曜日` 列が作成されているか確認
- [x] **リグレッションテスト**  
  - もう一度 `move_new_csv()` → `update_master()` を実行し、重複行が増えないことを確認

### フェーズ1完了基準
- [x] Notebook がエラーなく一連の処理を完了する  
- [x] `slot_master.parquet` が最新データを保持し、`曜日` 列が正しい

---

## フェーズ2：追加作業（※別チャットで対応）– GitHub / Docker / UI

### E. GitHub 連携
- [ ] `.gitignore` に `*.parquet`, `.ipynb_checkpoints/` を追加
- [ ] `requirements.txt`（pandas, pyarrow）を作成しコミット
- [ ] Notebook とスクリプトを Push し、GitHub 上でファイルを確認

### F. スクリプト化
- [ ] Notebook の主要関数を `csv_manager.py` に抽出
- [ ] `python csv_manager.py` 単体で動作することを確認

### G. Docker 化
- [ ] `Dockerfile` を作成  
      ベースイメージ `python:3.12-slim`  
      コピー → 依存インストール → `CMD ["python","csv_manager.py"]`
- [ ] データフォルダをボリュームマウントしてコンテナをビルド＆実行

### H. UI ラッパー
- [ ] Streamlit / Flask / FastAPI から 1 つ選択
- [ ] 「CSV 取込 & マスタ更新」ボタンを試作
- [ ] Dockerfile でポート公開し、ブラウザから UI を確認

---

---
### 共通注意事項
- 既存の変数名・関数名・列名は**絶対に変更・削除しない**こと。
- 新しい機能を追加するときは **SCHEMA_VERSION を +1 し、旧バージョンとの互換処理を書いてからマージ**する。
- Notebook 外部環境を変える場合（Docker など）は **`DOWNLOADS` / `DST_ROOT` 定数だけを書き換える**。他セルにパスを直書きしない。
- すべての読み書きは `encoding="utf-8-sig"` 固定。  
- 日付・時間は **Asia/Tokyo** タイムゾーンで統一。  
- `update_master()` 完了後に **重複行が無いことを assert** する。  
- Parquet 保存前に **バックアップファイルを自動生成**し、破損時のリカバリを可能にする。  
- ChatGPT が提示するコードは **セル全文を貼付**し、差分だけの提案は避ける。  
---


#### 例外ルール（変更が必要になった場合）
- 本チェックリストの固定仕様でエラーが解決できない場合は **仕様を変更しても良い**。
- ただし変更時は次の 3 ステップを必ず実施すること：
  1. **変更理由・影響範囲を “更新履歴” セクションに記載**
  2. 旧仕様で動いていたコードが壊れないよう **互換レイヤ** を追加
  3. **テストセル**を更新し、旧データ・新データ両方で PASS することを確認


