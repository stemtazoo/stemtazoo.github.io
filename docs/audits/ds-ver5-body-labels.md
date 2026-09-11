# DS検定 ver.5 本文表記監査

> `scripts/audit_ds_ver5_body_labels.py` により自動生成。通常記事本文に残る旧ver.5スキルシート名を検出します。

## 集計

- 旧表記が残る通常記事: **47**
- `ビジネス力シート`: **0記事**
- `AI利活用スキルシート`: **0記事**
- `データサイエンス力シート`: **1記事**
- `データエンジニアリング力シート`: **46記事**

## 修正方針

旧見出しだけを機械的に名称変更しない。本文に列挙された旧チェック項目自体がver.6で移動・統合されている可能性があるため、`ds_area` / `ds_section` と公式ver.6の★1データを照合して記事単位で更新する。

まず、★1文言が公式ver.6と完全一致し、かつ `ds_area` も一致する1項目記事は `scripts/migrate_ds_ver6_exact_skill_items.py` で自動移行する。残りは類似一致と記事内容を確認して個別に更新する。

優先順は **基盤・価値創造（旧ビジネス/AI利活用からの再編）→ データサイエンス → データエンジニアリング** とする。

## 対象記事

| ファイル | title | ds_area | ds_section | 旧表記 |
|---|---|---|---|---|
| `access-control-list.md` | アクセス制御リスト（ACL）とは？ファイル権限の基本を整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `authentication-authorization.md` | 認証と認可の違いとは？本人確認と権限付与で整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `batch-vs-stream.md` | バッチ処理とストリーム処理の違いとは？リアルタイム性で切り分ける【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `cap-theorem.md` | CAP定理とは？分断時の一貫性と可用性を整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `data-extraction-vs-aggregation.md` | データ抽出と集計の違いとは？（SQL・BIで混同しやすい操作）【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `data-lake.md` | データレイクとは？（DWHとの違いも整理）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `data-warehouse.md` | データウェアハウス（DWH）とは？（データレイクとの違いも整理）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `database-constraints.md` | データベースの制約とは？NOT NULL・一意性・外部キーを整理【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `datalake-vs-nosql.md` | データレイクとNoSQLの違いとは？役割の違いを整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `digital-signature.md` | 電子署名とは？本人性・完全性と公開鍵での検証を整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `docker.md` | Dockerとは？再現性が出る理由を整理【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `er-diagram.md` | ER図とは？エンティティとリレーションを整理する図【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `etl.md` | ETLとは？（データ統合の基本プロセス）【DS検定リテラシー】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `foreign-key.md` | 外部キー（Foreign Key）とは？テーブルの関係を理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `ftp-ssh.md` | FTP・SSH・SFTP・FTPSの違いとは？用途と暗号化を比較【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `hadoop-vs-spark.md` | HadoopとSparkの違いとは？（分散処理基盤の比較）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `hadoop.md` | Hadoopとは？（ビッグデータ分散処理基盤）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `hdfs.md` | HDFS（Hadoop分散ファイルシステム）とは？【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `incremental-vs-differential-backup.md` | 増分バックアップと差分バックアップの違いとは？【DS検定リテラシー】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `left-join-where.md` | LEFT JOINとWHEREの関係とは？（SQLのひっかけ問題）【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `mapping.md` | マッピング処理とは？データを対応づける基本操作【DS検定】 | `dataengineering` | `data-processing` | データサイエンス力シート |
| `mapreduce.md` | MapReduceとは？（分散処理の基本モデル）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `normalization-2nf-3nf.md` | 第2正規化と第3正規化の違いを整理（候補キーから考える）【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `nosql-datastore.md` | NoSQLデータストアとは？RDBとの違いと使いどころを整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `primary-key.md` | 主キー（Primary Key）とは？データベースの基本ルールを理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `publickey-vs-symmetric.md` | 公開鍵暗号方式と共通鍵暗号方式の違いとは？【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `rbac.md` | RBAC（ロールベースアクセス制御）とは？【DS検定リテラシー】 | `foundation` | `security` | データエンジニアリング力シート |
| `referential-integrity.md` | 参照整合性とは？外部キーとデータ整合性を理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `regular-expression-email.md` | メールアドレスの正規表現とは？なぜ難しいのかを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `regular-expression-postalcode.md` | 郵便番号の正規表現とは？電話番号との違いで理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `replication-vs-backup.md` | レプリケーションとバックアップの違いとは？【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `rest-api-methods.md` | REST API のメソッドとは？データ操作の役割を整理【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `rest-api.md` | REST APIとは？SOAPとの違いを整理【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `rpo-rto.md` | RPOとRTOの違いとは？（障害復旧の判断基準）【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `self-join.md` | 自己結合とは？同じテーブルを結合する理由を理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `soap.md` | SOAPとは？RESTとの違いを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-count-diff.md` | COUNT(*)・COUNT(列)・COUNT DISTINCTの違い【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-distinct.md` | DISTINCTとは？重複データを除去する基本操作【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-exists.md` | EXISTSとは？サブクエリの存在判定を理解する【DS検定】 | `dataengineering` | `sql` | データエンジニアリング力シート |
| `sql-filtering.md` | SQLのフィルタリング処理とは？（WHERE句によるデータ抽出）【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-in-exists.md` | INとEXISTSの違いとは？値比較と存在判定を整理【DS検定】 | `dataengineering` | `sql` | データエンジニアリング力シート |
| `sql-union.md` | UNIONとUNION ALLの違いとは？重複の扱いを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-where.md` | WHERE句とは？条件抽出の基本を理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `star-schema.md` | スタースキーマとは？ファクトテーブルとディメンションテーブルを理解する【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `vpn-ssh.md` | VPNとSSHの違いとは？（安全な通信の仕組みを整理）【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `web-api.md` | Web APIとは？HTTPでサービスとデータをやり取りする仕組み【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `web-crawling-scraping.md` | Webクローリングとスクレイピングの違いとは？【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
