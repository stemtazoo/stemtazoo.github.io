# DS検定 ver.5 本文表記監査

> `scripts/audit_ds_ver5_body_labels.py` により自動生成。通常記事本文に残る旧ver.5スキルシート名を検出します。

## 集計

- 旧表記が残る通常記事: **76**
- `ビジネス力シート`: **0記事**
- `AI利活用スキルシート`: **0記事**
- `データサイエンス力シート`: **27記事**
- `データエンジニアリング力シート`: **49記事**

## 修正方針

旧見出しだけを機械的に名称変更しない。本文に列挙された旧チェック項目自体がver.6で移動・統合されている可能性があるため、`ds_area` / `ds_section` と公式ver.6の★1データを照合して記事単位で更新する。

まず、★1文言が公式ver.6と完全一致し、かつ `ds_area` も一致する1項目記事は `scripts/migrate_ds_ver6_exact_skill_items.py` で自動移行する。残りは類似一致と記事内容を確認して個別に更新する。

優先順は **基盤・価値創造（旧ビジネス/AI利活用からの再編）→ データサイエンス → データエンジニアリング** とする。

## 対象記事

| ファイル | title | ds_area | ds_section | 旧表記 |
|---|---|---|---|---|
| `access-control-list.md` | アクセス制御リスト（ACL）とは？ファイル権限の基本を整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `authentication-authorization.md` | 認証と認可の違いとは？本人確認と権限付与で整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `average-methods-comparison.md` | マクロ平均・マイクロ平均・重み付き平均の違いとは？【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `batch-vs-stream.md` | バッチ処理とストリーム処理の違いとは？リアルタイム性で切り分ける【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `bi-operations-cheatsheet.md` | BIツール操作チートシート｜スライス・ダイス・ドリルダウンの違い【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `cap-theorem.md` | CAP定理とは？分断時の一貫性と可用性を整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `categorical-variable.md` | カテゴリ変数とは？数値データとの違いを整理【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `data-cube.md` | データキューブとは？OLAP分析の基本をわかりやすく整理【DS検定】 | `datascience` | `data-understanding` | データエンジニアリング力シート |
| `data-extraction-vs-aggregation.md` | データ抽出と集計の違いとは？（SQL・BIで混同しやすい操作）【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `data-lake.md` | データレイクとは？（DWHとの違いも整理）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `data-transformation.md` | データトランスフォーメーションとは？（非構造化データの変換）【DS検定】 | `datascience` | `data-preparation` | データエンジニアリング力シート |
| `data-warehouse.md` | データウェアハウス（DWH）とは？（データレイクとの違いも整理）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `database-constraints.md` | データベースの制約とは？NOT NULL・一意性・外部キーを整理【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `datalake-vs-nosql.md` | データレイクとNoSQLの違いとは？役割の違いを整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `deviation-score.md` | 偏差値とは？zスコア・標準偏差との違いを整理【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `digital-signature.md` | 電子署名とは？本人性・完全性と公開鍵での検証を整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `docker.md` | Dockerとは？再現性が出る理由を整理【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `drilldown-drillup.md` | ドリルダウンとドリルアップの違いとは？BIツールの基本操作【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `drillthrough.md` | ドリルスルーとは？ドリルダウンとの違いを整理【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `eda.md` | EDA（探索的データ分析）とは？分析の第一歩を理解する【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `encoding.md` | エンコーディングとは？カテゴリ変数を数値化する理由【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `er-diagram.md` | ER図とは？エンティティとリレーションを整理する図【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `estimator-properties.md` | 推定量の性質の違いとは？（不偏性・一貫性・効率性・信頼性）【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `etl.md` | ETLとは？（データ統合の基本プロセス）【DS検定リテラシー】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `euclidean-norm.md` | ユーグリッドノルムとは？（ベクトルの長さの測り方）【DS検定】 | `datascience` | `linear-algebra` | データサイエンス力シート |
| `feature-engineering.md` | 特徴量エンジニアリングとは？モデルに効くデータ加工を整理【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `feature-engineering2.md` | 特徴量エンジニアリングの具体例：年齢化・カテゴリ変換・リーク防止【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `feature.md` | 特徴量（Feature）とは？機械学習で使う入力データを理解する【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `filter.md` | フィルターとは？BIツールの基本操作をわかりやすく解説【DS検定】 | `datascience` | `data-understanding` | データサイエンス力シート |
| `foreign-key.md` | 外部キー（Foreign Key）とは？テーブルの関係を理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `ftp-ssh.md` | FTP・SSH・SFTP・FTPSの違いとは？用途と暗号化を比較【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `hadoop-vs-spark.md` | HadoopとSparkの違いとは？（分散処理基盤の比較）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `hadoop.md` | Hadoopとは？（ビッグデータ分散処理基盤）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `hdfs.md` | HDFS（Hadoop分散ファイルシステム）とは？【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `imputation.md` | インプテーションとは？（欠損値補完の基本）【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `incremental-vs-differential-backup.md` | 増分バックアップと差分バックアップの違いとは？【DS検定リテラシー】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `left-join-where.md` | LEFT JOINとWHEREの関係とは？（SQLのひっかけ問題）【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `mapping.md` | マッピング処理とは？データを対応づける基本操作【DS検定】 | `dataengineering` | `data-processing` | データサイエンス力シート |
| `mapreduce.md` | MapReduceとは？（分散処理の基本モデル）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `missing-value-handling.md` | 欠損値の処理方法とは？代表的な手法と使い分け【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `normalization-2nf-3nf.md` | 第2正規化と第3正規化の違いを整理（候補キーから考える）【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `nosql-datastore.md` | NoSQLデータストアとは？RDBとの違いと使いどころを整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `olap.md` | OLAPとは？BIツール分析の基本概念をわかりやすく解説【DS検定】 | `datascience` | `data-understanding` | データサイエンス力シート |
| `pivot.md` | ピボットとは？クロス集計との違いを整理【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `preprocessing.md` | データ前処理（Preprocessing）とは？分析前に行う重要ステップ【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `primary-key.md` | 主キー（Primary Key）とは？データベースの基本ルールを理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `publickey-vs-symmetric.md` | 公開鍵暗号方式と共通鍵暗号方式の違いとは？【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `random-sampling-methods.md` | 無作為抽出法とは？種類と違いを整理【DS検定リテラシー】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `rbac.md` | RBAC（ロールベースアクセス制御）とは？【DS検定リテラシー】 | `foundation` | `security` | データエンジニアリング力シート |
| `referential-integrity.md` | 参照整合性とは？外部キーとデータ整合性を理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `regular-expression-email.md` | メールアドレスの正規表現とは？なぜ難しいのかを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `regular-expression-postalcode.md` | 郵便番号の正規表現とは？電話番号との違いで理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `regular-expression-summary.md` | 正規表現のひっかけ総整理（試験直前チートシート）【DS検定】 | `datascience` | `unstructured-data` | データエンジニアリング力シート |
| `replication-vs-backup.md` | レプリケーションとバックアップの違いとは？【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `rest-api-methods.md` | REST API のメソッドとは？データ操作の役割を整理【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `rest-api.md` | REST APIとは？SOAPとの違いを整理【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `rfm-analysis.md` | RFM分析とは？顧客価値を評価するマーケティング分析【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `rpo-rto.md` | RPOとRTOの違いとは？（障害復旧の判断基準）【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `sampling-methods-comparison.md` | 抽出方法の違いを整理（単純無作為・層化・集落・多段・系統）【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `self-join.md` | 自己結合とは？同じテーブルを結合する理由を理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `slice-dice.md` | スライスとダイスの違いとは？BIツールの基本操作を整理【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `soap.md` | SOAPとは？RESTとの違いを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-count-diff.md` | COUNT(*)・COUNT(列)・COUNT DISTINCTの違い【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-distinct.md` | DISTINCTとは？重複データを除去する基本操作【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-exists.md` | EXISTSとは？サブクエリの存在判定を理解する【DS検定】 | `dataengineering` | `sql` | データエンジニアリング力シート |
| `sql-filtering.md` | SQLのフィルタリング処理とは？（WHERE句によるデータ抽出）【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-in-exists.md` | INとEXISTSの違いとは？値比較と存在判定を整理【DS検定】 | `dataengineering` | `sql` | データエンジニアリング力シート |
| `sql-union.md` | UNIONとUNION ALLの違いとは？重複の扱いを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-where.md` | WHERE句とは？条件抽出の基本を理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `star-schema.md` | スタースキーマとは？ファクトテーブルとディメンションテーブルを理解する【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `statistics-overview.md` | 統計の基本まとめ（平均・分散・相関・回帰の関係を整理）【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `statistics-summary.md` | DS検定でよく出る統計まとめ（平均・分散・相関を一気に整理） | `datascience` | `statistics` | データサイエンス力シート |
| `vpn-ssh.md` | VPNとSSHの違いとは？（安全な通信の仕組みを整理）【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `web-api.md` | Web APIとは？HTTPでサービスとデータをやり取りする仕組み【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `web-crawling-scraping.md` | Webクローリングとスクレイピングの違いとは？【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `z-score-method.md` | zスコアとは？標準化・偏差値・外れ値判定を整理【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
