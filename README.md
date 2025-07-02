\# web-ui-app



ローカルで \*\*Streamlit\*\* を使い、パチスロ差枚データなどを可視化する個人用ツール。  

Jupyter Notebook で動かしていたミニアプリをモジュール化し、この Web UI に統合していく。



---



\## セットアップ（Windows・初回だけ）



> “忘れたらこの README を ChatGPT に貼って『手順 1 から実行したい』と伝えれば OK”



```bash

\# 1. PowerShell でプロジェクトフォルダへ

cd C:\\messe\_mitaka\_UI



\# 2. 仮想環境

python -m venv .venv

.venv\\Scripts\\activate



\# 3. 依存パッケージ

pip install streamlit pandas



\# 4. 起動

streamlit run app.py



------------------
自分用メモ
-------------------
# 編集後

git add dev\_master\_checklist.md

git commit -m "docs: update checklist"

git push











\#### 使い方メモ

\- \*\*上の 1〜4 行をコピペすれば “動くまで” 辿りつける\*\*、を目標に構成しています。  

\- 手順を忘れたら \*\*この README の「セットアップ」節\*\* を丸ごと ChatGPT に渡して  

&nbsp; “このコマンドを１行ずつ実行したい、次に何を押せばいい？” と聞けば、同じ流れで案内できます。



---



\### 3. 次のアクション



1\. エディタで `README.md` を作成し、上の内容を貼り付ける  

2\. \*\*ライセンスを置かない場合\*\* は README だけコミット  

&nbsp;  ```powershell

&nbsp;  git add README.md

&nbsp;  git commit -m "docs: add minimal README"

&nbsp;  git push














