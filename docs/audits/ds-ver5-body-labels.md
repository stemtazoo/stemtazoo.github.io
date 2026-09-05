# DS検定 ver.5 本文表記監査

> `scripts/audit_ds_ver5_body_labels.py` により自動生成。通常記事本文に残る旧ver.5スキルシート名を検出します。

## 集計

- 旧表記が残る通常記事: **246**
- `ビジネス力シート`: **48記事**
- `AI利活用スキルシート`: **59記事**
- `データサイエンス力シート`: **79記事**
- `データエンジニアリング力シート`: **60記事**

## 修正方針

旧見出しだけを機械的に名称変更しない。本文に列挙された旧チェック項目自体がver.6で移動・統合されている可能性があるため、`ds_area` / `ds_section` と公式ver.6の★1データを照合して記事単位で更新する。

優先順は **基盤・価値創造（旧ビジネス/AI利活用からの再編）→ データサイエンス → データエンジニアリング** とする。

## 対象記事

| ファイル | title | ds_area | ds_section | 旧表記 |
|---|---|---|---|---|
| `ab-test.md` | A/Bテストとは？データで施策を比較する方法【DS検定】 | `datascience` | `statistics` | ビジネス力シート |
| `access-control-list.md` | アクセス制御リスト（ACL）とは？ファイル権限の基本を整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `activation-functions-hidden-layer.md` | 中間層で使用される活性化関数とは？（ReLU・シグモイド・ソフトマックスの違い）【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `agile-development.md` | アジャイル開発とは？ウォーターフォール開発との違いを整理【DS検定】 | `value-creation` | `project-management` | ビジネス力シート |
| `aiops-mlops-cheatsheet.md` | AIOpsとMLOpsの違いを一発整理【DS検定チートシート】 | `dataengineering` | `environment-setup` | AI利活用スキルシート |
| `aiops.md` | AIOpsとは？MLOpsとの違いを整理【DS検定リテラシー】 | `dataengineering` | `environment-setup` | AI利活用スキルシート |
| `analysis-approach-design.md` | 分析アプローチ設計とは？（分析プロジェクトを成功させる設計プロセス）【DS検定】 | `foundation` | `problem-definition` | ビジネス力シート |
| `analysis-approach-selection.md` | 必要なデータ・分析手法・可視化を適切に選択する力とは？【DS検定】 | `datascience` | `data-understanding` | データサイエンス力シート |
| `analytics-4types.md` | 記述的・診断的・予測的・処方的分析の違いとは？4分類を整理【DS検定】 | `datascience` | `data-understanding` | AI利活用スキルシート |
| `anchoring-effect.md` | アンカリング効果とは？最初の情報に判断が引きずられる心理【DS検定】 | `foundation` | `logical-thinking` | ビジネス力シート |
| `annotation.md` | アノテーションとは？AI学習データの品質を決める作業【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `anonymized-information.md` | 匿名加工情報とは？個人情報との違いをわかりやすく整理【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `apriori-algorithm.md` | Aprioriアルゴリズムとは？（アソシエーション分析の基本手法）【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `association-analysis.md` | アソシエーション分析とは？購買データの関係性を見つける分析【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `association-metrics.md` | 共起頻度・支持度・信頼度・リフト値の違いとは？【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `authentication-authorization.md` | 認証と認可の違いとは？本人確認と権限付与で整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `authentication-vs-authorization.md` | 認証・認可・アクセス制御の関係を例で理解する【DS検定】 | `foundation` | `security` | AI利活用スキルシート |
| `availability-heuristic.md` | 利用可能性ヒューリスティックとは？代表性ヒューリスティックとの違い【DS検定】 | `foundation` | `logical-thinking` | ビジネス力シート |
| `average-methods-comparison.md` | マクロ平均・マイクロ平均・重み付き平均の違いとは？【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `basket-analysis.md` | バスケット分析とは？（リフト値まで整理）【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `batch-vs-stream.md` | バッチ処理とストリーム処理の違いとは？リアルタイム性で切り分ける【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `bayes-theorem.md` | ベイズの定理とは？（条件付き確率の逆算）【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `bcp.md` | BCP（事業継続計画）とは？災害時でも業務を止めない仕組み【DS検定】 | `value-creation` | `governance-risk` | ビジネス力シート |
| `bernoulli-binomial.md` | ベルヌーイ試行とは？成功・失敗の1回の試行を整理【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `bi-operations-cheatsheet.md` | BIツール操作チートシート｜スライス・ダイス・ドリルダウンの違い【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `bi-tool-functions.md` | BIツールの基本機能とは？OLAP・データマイニングを整理【DS検定】 | `datascience` | `data-understanding` | ビジネス力シート |
| `bias-variance-tradeoff.md` | バイアス・バリアンスのトレードオフとは？過学習との関係【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `binomial-bernoulli.md` | 二項分布とは？ベルヌーイ試行をn回繰り返す成功回数の確率【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `boxplot.md` | 箱ひげ図とは？四分位数と外れ値の読み取り方【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `cap-theorem.md` | CAP定理とは？分断時の一貫性と可用性を整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `categorical-variable.md` | カテゴリ変数とは？数値データとの違いを整理【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `causal-inference.md` | 因果推論とは？相関との違いを整理【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `ccpa.md` | CCPAとは？GDPRとの違いとプライバシー保護の基本【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `chart-types.md` | グラフの種類と使い分け（可視化の基本）【DS検定】 | `datascience` | `visualization` | データエンジニアリング力シート |
| `chi-square-distribution.md` | カイ二乗分布とは？（χ²分布の使いどころを整理）【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `cluster-analysis.md` | クラスタ分析とは？似たデータをグループ分けする分析手法【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `cnn.md` | CNN（畳み込みニューラルネットワーク）とは？画像認識AIの基本【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `coefficient-of-determination-contribution.md` | 決定係数と寄与率とは？回帰モデルの説明力を理解する【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `cognitive-bias.md` | 認知バイアスとは？データ分析で判断を誤らせる思い込み【DS検定】 | `foundation` | `logical-thinking` | ビジネス力シート |
| `compliance-risk.md` | コンプライアンスリスクとは？オペレーショナルリスクとの違い【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `confirmation-bias.md` | 確証バイアスとは？自分に都合のよい情報だけ集めてしまう心理【DS検定】 | `foundation` | `logical-thinking` | ビジネス力シート |
| `constructor.md` | コンストラクタとは？初期化処理の役割を整理【DS検定リテラシー】 | `dataengineering` | `programming` | AI利活用スキルシート |
| `contract-ukeoi-juninin.md` | 請負契約と準委任契約の違いとは？成果責任と業務責任を整理【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `convolution.md` | 畳み込み（Convolution）とは？画像フィルタ処理の基本【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `correlation-and-causation.md` | 相関があっても因果とは限らない理由を例で理解する【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `correlation-vs-causation.md` | 相関と因果の違いとは？交絡と「原因とは限らない」を整理【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `covariance-and-correlation.md` | 共分散を相関係数に直す意味とは？単位の影響を外す考え方【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `covariance-correlation.md` | 共分散と相関係数の違いとは？単位の影響と-1〜1の意味で整理【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `cps-iot-digitaltwin-cheatsheet.md` | CPS・IoT・デジタルツインの違いを一発整理【DS検定チートシート】 | `value-creation` | `technology-social-trends` | AI利活用スキルシート |
| `cps.md` | CPS（サイバーフィジカルシステム）とは？Society5.0の中核技術を理解する【DS検定】 | `value-creation` | `technology-social-trends` | AI利活用スキルシート |
| `critical-path.md` | クリティカルパスとは？プロジェクト遅延を左右する重要な経路【DS検定】 | `value-creation` | `project-management` | ビジネス力シート |
| `curse-of-dimensionality.md` | 次元の呪いとは？（高次元データで起きる問題）【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `customer-journey.md` | カスタマージャーニーとは？顧客体験を理解するフレームワーク【DS検定】 | `value-creation` | `business-design` | ビジネス力シート |
| `data-augmentation.md` | データ拡張（Data Augmentation）とは？画像AIの学習データを増やす方法【DS検定】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `data-cube.md` | データキューブとは？OLAP分析の基本をわかりやすく整理【DS検定】 | `datascience` | `data-understanding` | データエンジニアリング力シート |
| `data-driven-management.md` | データドリブン経営とは？データにもとづいて意思決定する考え方【DS検定】 | `value-creation` | `business-design` | ビジネス力シート |
| `data-extraction-vs-aggregation.md` | データ抽出と集計の違いとは？（SQL・BIで混同しやすい操作）【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `data-governance.md` | データガバナンスとは？データ活用に必要な管理の仕組み【DS検定】 | `value-creation` | `governance-risk` | ビジネス力シート |
| `data-lake.md` | データレイクとは？（DWHとの違いも整理）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `data-literacy.md` | データリテラシーとは？データを読み解く力【DS検定】 | `foundation` | `data-understanding` | ビジネス力シート |
| `data-mart.md` | データマートとは？（DWHとの違いを整理）【DS検定リテラシー】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `data-transformation.md` | データトランスフォーメーションとは？（非構造化データの変換）【DS検定】 | `datascience` | `data-preparation` | データエンジニアリング力シート |
| `data-warehouse-vs-datamart.md` | データウェアハウス（DWH）とは？データマートとの違いを理解する【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `data-warehouse.md` | データウェアハウス（DWH）とは？（データレイクとの違いも整理）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `database-constraints.md` | データベースの制約とは？NOT NULL・一意性・外部キーを整理【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `datalake-vs-nosql.md` | データレイクとNoSQLの違いとは？役割の違いを整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `dendrogram.md` | デンドログラムの見方とは？縦軸とクラスタ数【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `dependency-parsing.md` | 係り受け解析とは？形態素解析との違いを整理【DS検定】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `design-of-experiments.md` | 実験計画法とは？少ない実験で原因を見つける方法【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `design-thinking.md` | デザイン思考とは？ユーザー中心で課題を解決する考え方【DS検定】 | `value-creation` | `business-design` | ビジネス力シート |
| `deviation-score.md` | 偏差値とは？zスコア・標準偏差との違いを整理【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `digital-image-representation.md` | 画像のデジタル表現とは？（標本化と量子化の基本）【DS検定】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `digital-signature.md` | 電子署名とは？本人性・完全性と公開鍵での検証を整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `digital-signature2.md` | 電子署名と暗号化の鍵の使い方の違い【DS検定】 | `foundation` | `security` | AI利活用スキルシート |
| `digital-twin.md` | デジタルツインとは？CPSとの違いを整理【DS検定】 | `value-creation` | `technology-social-trends` | AI利活用スキルシート |
| `discrete-continuous-distribution.md` | 離散型確率分布と連続型確率分布の違いとは？【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `docker.md` | Dockerとは？再現性が出る理由を整理【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `drilldown-drillup.md` | ドリルダウンとドリルアップの違いとは？BIツールの基本操作【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `drillthrough.md` | ドリルスルーとは？ドリルダウンとの違いを整理【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `dunning-kruger-effect.md` | ダニング＝クルーガー効果とは？能力が低いほど自信が高くなる心理【DS検定】 | `foundation` | `logical-thinking` | ビジネス力シート |
| `e-calculus.md` | eの微分・積分を最短で整理【DS検定リテラシー】 | `datascience` | `calculus` | データサイエンス力シート |
| `eda.md` | EDA（探索的データ分析）とは？分析の第一歩を理解する【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `eigenvalue.md` | 行列の固有値とは？意味を直感で整理【DS検定】 | `datascience` | `linear-algebra` | データサイエンス力シート |
| `elsi.md` | ELSIとは？AI時代に重要な倫理・法・社会問題を理解する【DS検定】 | `foundation` | `action-norms` | AI利活用スキルシート |
| `encapsulation.md` | カプセル化とは？情報隠蔽との違いを整理【DS検定リテラシー】 | `dataengineering` | `programming` | AI利活用スキルシート |
| `encoding.md` | エンコーディングとは？カテゴリ変数を数値化する理由【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `entropy.md` | エントロピーとは？不確実さを測る指標【DS検定】 | `datascience` | `statistics` | AI利活用スキルシート |
| `er-diagram.md` | ER図とは？エンティティとリレーションを整理する図【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `estimator-properties.md` | 推定量の性質の違いとは？（不偏性・一貫性・効率性・信頼性）【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `etl.md` | ETLとは？（データ統合の基本プロセス）【DS検定リテラシー】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `euclidean-norm.md` | ユーグリッドノルムとは？（ベクトルの長さの測り方）【DS検定】 | `datascience` | `linear-algebra` | データサイエンス力シート |
| `evaluation-metrics-comparison.md` | 分類モデルの評価指標の比較とは？【DS検定リテラシー】 | `datascience` | `modeling` | データサイエンス力シート |
| `f-test.md` | F検定とは？t検定との違いを整理【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `feature-engineering.md` | 特徴量エンジニアリングとは？モデルに効くデータ加工を整理【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `feature-engineering2.md` | 特徴量エンジニアリングの具体例：年齢化・カテゴリ変換・リーク防止【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `feature-importance.md` | 特徴量重要度とは？不純度ベースとPermutationの違い【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `feature.md` | 特徴量（Feature）とは？機械学習で使う入力データを理解する【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `filter.md` | フィルターとは？BIツールの基本操作をわかりやすく解説【DS検定】 | `datascience` | `data-understanding` | データサイエンス力シート |
| `five-forces-analysis.md` | 5フォース分析とは？業界の競争環境を分析するフレームワーク【DS検定】 | `value-creation` | `business-design` | ビジネス力シート |
| `foreign-key.md` | 外部キー（Foreign Key）とは？テーブルの関係を理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `ftp-ssh.md` | FTP・SSH・SFTP・FTPSの違いとは？用途と暗号化を比較【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `gantt-chart.md` | ガントチャートとは？WBSとの違いとプロジェクト管理の基本【DS検定】 | `value-creation` | `project-management` | ビジネス力シート |
| `gdpr.md` | GDPRとは？個人データ保護の基本を整理【DS検定】 | `foundation` | `action-norms` | AI利活用スキルシート |
| `gini-vs-entropy.md` | ジニ不純度とエントロピーの違いとは？分岐基準を整理【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `governance.md` | ガバナンスとは？企業統治とリスク管理の関係【DS検定】 | `value-creation` | `governance-risk` | ビジネス力シート |
| `hadoop-vs-spark.md` | HadoopとSparkの違いとは？（分散処理基盤の比較）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `hadoop.md` | Hadoopとは？（ビッグデータ分散処理基盤）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `hallucination.md` | ハルシネーションとは？生成AIの限界と正しい向き合い方【DS検定】 | `foundation` | `ai-fundamentals` | AI利活用スキルシート |
| `hash-function.md` | ハッシュ関数とは？（コリジョン・ソルトとの違い）【DS検定】 | `foundation` | `security` | AI利活用スキルシート |
| `hash-vs-encryption.md` | ハッシュと暗号化の違いとは？（復号できるかが分かれ目）【DS検定】 | `foundation` | `security` | AI利活用スキルシート |
| `hdfs.md` | HDFS（Hadoop分散ファイルシステム）とは？【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `hierarchical-clustering.md` | 階層クラスター分析とは？手法の違いまで整理【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `hierarchical-distance-metrics.md` | 階層クラスター分析における距離の測定方法の比較【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `hot-cool-archive.md` | Hot・Cool・Archiveの違いとは？（クラウドストレージ階層の整理）【DS検定】 | `dataengineering` | `data-storage` | ビジネス力シート |
| `human-centered-ai-principles.md` | 人間中心のAI社会原則とは？AIと社会のルールを理解する【DS検定】 | `foundation` | `action-norms` | AI利活用スキルシート |
| `iam-policy.md` | クラウドサービスのIAMポリシーとは？（アクセス制御の基本）【DS検定】 | `foundation` | `security` | AI利活用スキルシート |
| `image-filter-processing.md` | 画像のフィルタ処理とは？（ノイズ除去と特徴強調の基本）【DS検定】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `image-metadata.md` | 画像データにおけるメタデータとは？意味と活用を整理【DS検定リテラシー】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `impurity.md` | 不純度とは？決定木の分岐基準を整理【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `imputation.md` | インプテーションとは？（欠損値補完の基本）【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `incident-management.md` | インシデント管理とは？障害対応と報告の基本【DS検定】 | `value-creation` | `governance-risk` | ビジネス力シート |
| `incremental-vs-differential-backup.md` | 増分バックアップと差分バックアップの違いとは？【DS検定リテラシー】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `industry4-0.md` | インダストリー4.0とは？第4次産業革命の本質とドイツ戦略【DS検定】 | `value-creation` | `technology-social-trends` | AI利活用スキルシート |
| `information-gain.md` | 情報利得とは？決定木で分岐の良さを判断する基準【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `inheritance.md` | 継承とは？クラス設計の基本を整理【DS検定リテラシー】 | `dataengineering` | `programming` | AI利活用スキルシート |
| `internal-control.md` | 内部統制とは？企業の不正やミスを防ぐ仕組み【DS検定】 | `value-creation` | `governance-risk` | ビジネス力シート |
| `interpret-statistics.md` | 数字やグラフの持つメッセージを理解するとは？（統計情報の正しい読み取り）【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `inverse-matrix.md` | 逆行列とは何か？求め方と意味をやさしく整理【DS検定】 | `datascience` | `linear-algebra` | データサイエンス力シート |
| `japan-personal-information-protection-act.md` | 改正個人情報保護法とは？日本のデータ保護ルール【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `japanese-morphological-analysis-tools.md` | 日本語の形態素解析ツールとは？代表例と違いを整理【DS検定】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `jupyter-r-usage.md` | Jupyter NotebookやRの使い所とは？（データ分析環境の役割）【DS検定】 | `dataengineering` | `environment-setup` | AI利活用スキルシート |
| `kernel.md` | カーネル（Kernel）とは？画像フィルタ処理の計算ルール【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `key-stretching.md` | ストレッチングとは？（ハッシュ強化の仕組み）【DS検定】 | `foundation` | `security` | AI利活用スキルシート |
| `kpi-kgi.md` | KPIとKGIの違いとは？目標管理の基本を整理【DS検定】 | `foundation` | `goal-setting` | ビジネス力シート |
| `least-privilege.md` | 最小権限の原則とは？ゼロトラストとの関係を整理【DS検定リテラシー】 | `foundation` | `security` | AI利活用スキルシート |
| `left-join-where.md` | LEFT JOINとWHEREの関係とは？（SQLのひっかけ問題）【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `llm-temperature.md` | LLMのTemperatureとは？出力のランダム性を理解する【DS検定】 | `foundation` | `ai-fundamentals` | AI利活用スキルシート |
| `logistic-regression.md` | ロジスティック回帰とは？（オッズ・対数オッズから理解する）【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `machine-learning-algorithms-cheatsheet.md` | 機械学習アルゴリズム一覧チートシート（教師あり・教師なし・強化学習）【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `machine-learning-methods.md` | 機械学習の解析手法とは？（代表的アルゴリズムを整理）【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `malware.md` | マルウェアとは？代表的な種類と違いを整理【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `managed-service.md` | マネージドサービスとは？クラウド環境構築の基本概念を整理【DS検定】 | `dataengineering` | `environment-setup` | ビジネス力シート |
| `mapping.md` | マッピング処理とは？データを対応づける基本操作【DS検定】 | `dataengineering` | `data-processing` | データサイエンス力シート |
| `mapreduce.md` | MapReduceとは？（分散処理の基本モデル）【DS検定リテラシー】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `market-basket-analysis.md` | マーケットバスケット分析とは？購買パターン分析の基本【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `matrix-multiplication.md` | 行列の掛け算とは？（行列同士の掛け算）【DS検定リテラシー】 | `datascience` | `linear-algebra` | データサイエンス力シート |
| `mfa.md` | 多要素認証（MFA）とは？仕組みと必要性を整理【DS検定リテラシー】 | `foundation` | `security` | AI利活用スキルシート |
| `missing-value-handling.md` | 欠損値の処理方法とは？代表的な手法と使い分け【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `mlops.md` | MLOpsとは？AIOpsとの違いを一発整理【DS検定リテラシー】 | `dataengineering` | `environment-setup` | AI利活用スキルシート |
| `nlp-cleaning.md` | 自然言語処理におけるクリーニングとは？（前処理の基本）【DS検定】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `nltk.md` | NLTKとは？自然言語処理ライブラリの役割を整理【DS検定】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `normal-and-standard-normal.md` | 標準正規分布と正規分布の違いとは？【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `normalization-2nf-3nf.md` | 第2正規化と第3正規化の違いを整理（候補キーから考える）【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `nosql-datastore.md` | NoSQLデータストアとは？RDBとの違いと使いどころを整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `nosql.md` | NoSQLとは？リレーショナルDBとの違いを整理【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `oauth.md` | OAuthとは？仕組みとアクセストークンの流れを整理【DS検定リテラシー】 | `foundation` | `security` | AI利活用スキルシート |
| `olap.md` | OLAPとは？BIツール分析の基本概念をわかりやすく解説【DS検定】 | `datascience` | `data-understanding` | データサイエンス力シート |
| `open-data.md` | オープンデータとは？公共データ活用の基本【DS検定】 | `dataengineering` | `data-collection` | ビジネス力シート |
| `operational-risk.md` | オペレーショナルリスクとは？レピュテーションリスクとの違いを整理【DS検定】 | `value-creation` | `governance-risk` | ビジネス力シート |
| `opt-out.md` | オプトアウトとは？個人情報提供の仕組みを整理【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `outlier-visualization.md` | 外れ値を見出すための適切な可視化手法とは？【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `overfitting-tree-depth.md` | 過学習と分岐の深さの関係とは？決定木の注意点【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `paired-vs-independent-data.md` | 対応があるデータと対応がないデータの違いとは？【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `paper-structure.md` | 一般的な論文構成とは？流れを理解する【DS検定リテラシー】 | `foundation` | `logical-thinking` | ビジネス力シート |
| `pdca-cycle.md` | PDCAサイクルとは？継続的改善の基本フレームワーク【DS検定】 | `value-creation` | `project-management` | ビジネス力シート |
| `pearson-correlation.md` | ピアソンの相関係数とは？関係の強さをどう読むか【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `personal-identifier-code.md` | 個人識別符号とは？個人情報・個人関連情報との違い【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `pest-analysis.md` | PEST分析とは？マクロ環境を分析するフレームワーク【DS検定】 | `value-creation` | `business-design` | ビジネス力シート |
| `pivot.md` | ピボットとは？クロス集計との違いを整理【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `poc-concept-proof.md` | PoC（概念実証）とは？AIプロジェクトで重要な理由【DS検定】 | `value-creation` | `poc` | ビジネス力シート |
| `point-interval-estimation.md` | 点推定と区間推定の違いとは？（信頼区間まで整理）【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `polymorphism.md` | ポリモーフィズムとは？（同じ呼び出しで動作が変わる仕組み）【DS検定】 | `dataengineering` | `programming` | AI利活用スキルシート |
| `population-sample-unbiased-variance.md` | 母分散・標本分散・不偏分散の違いとは？【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `power-law.md` | べき乗則とは？両対数グラフが直線になる理由【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `predictive-analytics.md` | 予測的データ分析とは？将来を読む分析手法を整理【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `preprocessing.md` | データ前処理（Preprocessing）とは？分析前に行う重要ステップ【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `primary-key.md` | 主キー（Primary Key）とは？データベースの基本ルールを理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `project-management.md` | プロジェクトマネジメントとは？プロジェクトを成功させるための管理手法【DS検定】 | `value-creation` | `project-management` | ビジネス力シート |
| `pseudonymized-information.md` | 仮名加工情報とは？匿名加工情報との違いを整理【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `publickey-vs-symmetric.md` | 公開鍵暗号方式と共通鍵暗号方式の違いとは？【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `quartile.md` | 四分位とは？値が複数の取り方になる理由まで整理【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `r-squared-adjusted-r-squared.md` | 自由度調整済み決定係数とは？決定係数との違い【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `rainbow-table-attack.md` | レインボーテーブル攻撃とは？（ソルトとの関係）【DS検定】 | `foundation` | `security` | AI利活用スキルシート |
| `random-forest.md` | ランダムフォレストとは？（特徴量重要度の考え方まで理解する）【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `random-sampling-methods.md` | 無作為抽出法とは？種類と違いを整理【DS検定リテラシー】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `rbac.md` | RBAC（ロールベースアクセス制御）とは？【DS検定リテラシー】 | `foundation` | `security` | データエンジニアリング力シート |
| `rdb-vs-nosql.md` | RDBとNoSQLの違いを一発で整理【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `referential-integrity.md` | 参照整合性とは？外部キーとデータ整合性を理解【DS検定】 | `dataengineering` | `database` | データエンジニアリング力シート |
| `regular-expression-email.md` | メールアドレスの正規表現とは？なぜ難しいのかを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `regular-expression-postalcode.md` | 郵便番号の正規表現とは？電話番号との違いで理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `regular-expression-summary.md` | 正規表現のひっかけ総整理（試験直前チートシート）【DS検定】 | `datascience` | `unstructured-data` | データエンジニアリング力シート |
| `replication-vs-backup.md` | レプリケーションとバックアップの違いとは？【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `rest-api-methods.md` | REST API のメソッドとは？データ操作の役割を整理【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `rest-api.md` | REST APIとは？SOAPとの違いを整理【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `revenue-equation.md` | 収益方程式とは？KPI設計の基本となるビジネスモデル【DS検定】 | `foundation` | `goal-setting` | ビジネス力シート |
| `rfm-analysis.md` | RFM分析とは？顧客価値を評価するマーケティング分析【DS検定】 | `datascience` | `modeling` | データサイエンス力シート |
| `risk-management.md` | リスクマネジメントとは？企業がリスクを管理する基本【DS検定】 | `value-creation` | `governance-risk` | ビジネス力シート |
| `rpo-rto.md` | RPOとRTOの違いとは？（障害復旧の判断基準）【DS検定】 | `dataengineering` | `environment-setup` | データエンジニアリング力シート |
| `sample-variance-unbiased-variance.md` | 標本分散と不偏分散の違いとは？【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `sampling-methods-comparison.md` | 抽出方法の違いを整理（単純無作為・層化・集落・多段・系統）【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `scrum.md` | スクラムとは？アジャイル開発の代表的なフレームワーク【DS検定】 | `value-creation` | `project-management` | ビジネス力シート |
| `self-join.md` | 自己結合とは？同じテーブルを結合する理由を理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sensitive-personal-information.md` | 要配慮個人情報とは？個人情報との違いと具体例【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `sigmoid-function.md` | シグモイド関数とは？（確率に変換する関数）【DS検定】 | `datascience` | `modeling` | AI利活用スキルシート |
| `significance-level-and-pvalue.md` | 有意水準とp値の違いとは？【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `slice-dice.md` | スライスとダイスの違いとは？BIツールの基本操作を整理【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `soap.md` | SOAPとは？RESTとの違いを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `society5.md` | Society5.0とは？超スマート社会の本質を整理【DS検定】 | `value-creation` | `technology-social-trends` | AI利活用スキルシート |
| `sora-ame-kasa.md` | 空・雨・傘とは？仮説思考の基本フレーム【DS検定】 | `foundation` | `logical-thinking` | ビジネス力シート |
| `spark.md` | Sparkとは？ビッグデータを高速処理する分散処理エンジン【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `spearman-rank-correlation.md` | スピアマンの順位相関とは？（Spearmanの順位相関係数）【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `sql-count-diff.md` | COUNT(*)・COUNT(列)・COUNT DISTINCTの違い【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-distinct.md` | DISTINCTとは？重複データを除去する基本操作【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-exists.md` | EXISTSとは？サブクエリの存在判定を理解する【DS検定】 | `dataengineering` | `sql` | データエンジニアリング力シート |
| `sql-filtering.md` | SQLのフィルタリング処理とは？（WHERE句によるデータ抽出）【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-groupby.md` | GROUP BYとは？データ集計の基本を理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-having.md` | HAVINGとは？WHEREとの違いを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-in-exists.md` | INとEXISTSの違いとは？値比較と存在判定を整理【DS検定】 | `dataengineering` | `sql` | データエンジニアリング力シート |
| `sql-join.md` | JOINとは？テーブル結合の基本を理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-union.md` | UNIONとUNION ALLの違いとは？重複の扱いを整理【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `sql-where.md` | WHERE句とは？条件抽出の基本を理解する【DS検定】 | `dataengineering` | `data-processing` | データエンジニアリング力シート |
| `ssl-tls.md` | SSL/TLSとは？公開鍵暗号と共通鍵暗号の役割を整理【DS検定】 | `foundation` | `security` | AI利活用スキルシート |
| `star-schema.md` | スタースキーマとは？ファクトテーブルとディメンションテーブルを理解する【DS検定】 | `dataengineering` | `data-structure` | データエンジニアリング力シート |
| `statistics-overview.md` | 統計の基本まとめ（平均・分散・相関・回帰の関係を整理）【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `statistics-summary.md` | DS検定でよく出る統計まとめ（平均・分散・相関を一気に整理） | `datascience` | `statistics` | データサイエンス力シート |
| `stemming-vs-lemmatization.md` | ステミングとレンマ化の違いとは？（テキスト前処理の基本）【DS検定】 | `datascience` | `unstructured-data` | AI利活用スキルシート |
| `student-t-test.md` | スチューデントの検定（t検定）とは？【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `swot-analysis.md` | SWOT分析とは？企業の強みと外部環境を整理するフレームワーク【DS検定】 | `value-creation` | `business-design` | ビジネス力シート |
| `symmetric-difference.md` | 対称差集合とは？意味と考え方をやさしく整理【DS検定】 | `datascience` | `set-theory` | データサイエンス力シート |
| `third-party-provision.md` | 個人情報の第三者提供とは？同意とオプトアウトのルール【DS検定】 | `foundation` | `action-norms` | ビジネス力シート |
| `type1-type2-error.md` | 第一種の過誤と第二種の過誤の違いとは？【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `variance-and-standard-deviation.md` | 分散と標準偏差の違いとは？ばらつきをどう読むか【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `variance-standard-deviation.md` | 分散と標準偏差とは？ばらつきを理解する基本統計【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `vector-dot-product.md` | ベクトルの内積とは？意味と使いどころを整理【DS検定】 | `datascience` | `linear-algebra` | データサイエンス力シート |
| `visualization-basic-perspectives.md` | データ可視化における基本的な視点とは？（差・相関・分布・変化・構成）【DS検定】 | `datascience` | `visualization` | データサイエンス力シート |
| `vpn-ssh.md` | VPNとSSHの違いとは？（安全な通信の仕組みを整理）【DS検定】 | `foundation` | `security` | データエンジニアリング力シート |
| `wbs.md` | WBSとは？作業分解とワークパッケージを整理【DS検定】 | `value-creation` | `project-management` | ビジネス力シート |
| `weak-strong-ai.md` | 弱いAIと強いAIの違いとは？【DS検定リテラシー】 | `foundation` | `ai-fundamentals` | AI利活用スキルシート |
| `web-api.md` | Web APIとは？HTTPでサービスとデータをやり取りする仕組み【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `web-crawling-scraping.md` | Webクローリングとスクレイピングの違いとは？【DS検定】 | `dataengineering` | `data-collection` | データエンジニアリング力シート |
| `welch-t-test.md` | ウェルチのt検定とは？等分散でない場合の平均比較【DS検定】 | `datascience` | `statistics` | データサイエンス力シート |
| `why-structure.md` | WHYの並び立てとは？ストーリー構築の基本【DS検定】 | `foundation` | `logical-thinking` | ビジネス力シート |
| `yarn.md` | YARNとは？Hadoopクラスタのリソース管理の仕組み【DS検定】 | `dataengineering` | `data-storage` | データエンジニアリング力シート |
| `z-score-method.md` | zスコアとは？標準化・偏差値・外れ値判定を整理【DS検定】 | `datascience` | `data-preparation` | データサイエンス力シート |
| `z-test.md` | z検定とは？t検定との違いまで整理【DS検定リテラシー】 | `datascience` | `statistics` | データサイエンス力シート |
| `zero-trust.md` | ゼロトラストとは？考え方と従来型セキュリティとの違い【DS検定リテラシー】 | `foundation` | `security` | AI利活用スキルシート |
