# FE記事の重複監査ログ

ファイル名の一覧取得と本文監査の完了は別です。

## 対象と進捗

- GitHub mainの再帰ツリーを2026-10-17に取得
- FE Markdown: 778ファイル（転送用ページを含む）
- 過去の本文確認履歴に対応する現存ファイル: 254ファイル（重複排除）
- ファイル単位の確認履歴カバー率: 32.6%。これは全件本文比較の完了率ではありません。
- 削除済みファイルは分母・分子から除外。変更前は転送17件・実記事761件でした。本PR適用後は転送20件・実記事758件となる見込みです。

- 実記事の個別確認履歴（本PR適用後）: **240/758件（31.7%）**。転送の20件は別管理。
- 変更前の761実記事すべての**機械的な類似候補抽出は実施済み**。候補の目視確認は抽出された43組を終了。未抽出の組合せが重複なしと確定したわけではありません。

## 修正PRの記録

- #426 派遣・出向・請負の統合
- #427 契約・スタック/キュー・メモリ管理の役割整理
- #428 プロジェクトライフサイクルの統合
- #429 TLO・プログラム記憶方式の統合、USBの役割整理
- #430 入力チェックの統合、結合テストの役割整理
- #431 CIAの統合
- #432 内部統制の統合
- #433 バックアップ方式の役割整理
- #434 PKI・認証局と暗号化の役割整理
- #438 761実記事の自動候補抽出・転送判定を導入（マージ済み）
- #439 追加53記事の役割監査と3記事の学習導線整理（マージ済み）
- #440 ASP・コード体系・LRUの重複統合、関連記事の照合（当PR）

## 本文確認履歴に含まれる現存ファイル

以下は確認履歴のインデックスです。記載されているだけで全本文の逐語比較や公開状態を確認済みとは判断しません。

- pages/fe/account-aggregation.md
- pages/fe/affinity-diagram.md
- pages/fe/agile-iteration.md
- pages/fe/ai-vs-rule-based-control.md
- pages/fe/arrow-diagram.md
- pages/fe/as-is-to-be-ea.md
- pages/fe/asp.md
- pages/fe/asp-service.md
- pages/fe/audit-evidence.md
- pages/fe/audit-working-papers.md
- pages/fe/authentication-devices.md
- pages/fe/automaton-state-transition.md
- pages/fe/backup-methods.md
- pages/fe/backup-redundancy.md
- pages/fe/balance-sheet.md
- pages/fe/bathtub-curve.md
- pages/fe/benchmark-test.md
- pages/fe/benchmarking.md
- pages/fe/binary-representation.md
- pages/fe/binary-search.md
- pages/fe/binary-search-tree.md
- pages/fe/binary-tree-traversal.md
- pages/fe/biometric-authentication.md
- pages/fe/black-box-testing.md
- pages/fe/block-search-average-comparisons.md
- pages/fe/bottom-up-testing.md
- pages/fe/bpo-saas-hosting-comparison.md
- pages/fe/brute-force-attack.md
- pages/fe/business-continuity-management.md
- pages/fe/business-continuity-plan.md
- pages/fe/business-domain.md
- pages/fe/business-impact-analysis.md
- pages/fe/cache-hit-rate-average-access-time.md
- pages/fe/cache-memory.md
- pages/fe/capacity-management-analysis-methods.md
- pages/fe/capacity-management-analysis-models.md
- pages/fe/certificate-authority.md
- pages/fe/challenge-response-authentication.md
- pages/fe/character-code-table.md
- pages/fe/character-encoding.md
- pages/fe/checksum.md
- pages/fe/cia-triad.md
- pages/fe/cidr-network-broadcast-address.md
- pages/fe/class-instance.md
- pages/fe/client-server-system.md
- pages/fe/cloud-deployment-models.md
- pages/fe/code-system-types.md
- pages/fe/code-types-and-identification.md
- pages/fe/cold-warm-start.md
- pages/fe/command-and-control.md
- pages/fe/commit-rollback.md
- pages/fe/common-frame.md
- pages/fe/common-frame-support-processes.md
- pages/fe/compiler-analysis-flow.md
- pages/fe/compiler-linker-loader-debugger.md
- pages/fe/complete-binary-tree.md
- pages/fe/condition-branch-order.md
- pages/fe/conditional-branch-average-comparisons.md
- pages/fe/configuration-management.md
- pages/fe/contract-types-outsourcing.md
- pages/fe/control-structures-loop-selection.md
- pages/fe/core-competence.md
- pages/fe/cpi-clock-cycle-cpu-time.md
- pages/fe/cpu-clock-frequency.md
- pages/fe/cpu-instruction-cycle.md
- pages/fe/cpu-scheduling.md
- pages/fe/cpu-scheduling-idle-time.md
- pages/fe/crashing-vs-fast-tracking.md
- pages/fe/crc.md
- pages/fe/critical-chain.md
- pages/fe/critical-path-vs-critical-chain.md
- pages/fe/crowdfunding.md
- pages/fe/crowdsourcing.md
- pages/fe/cryptographic-algorithm-types.md
- pages/fe/csirt-material-1.md
- pages/fe/csirt-soc-psirt-jcrat.md
- pages/fe/csv-format.md
- pages/fe/csv-spreadsheet-cell-reference.md
- pages/fe/data-mining.md
- pages/fe/data-warehouse.md
- pages/fe/database-backup-recovery.md
- pages/fe/database-log-recovery.md
- pages/fe/database-recovery-rollforward-rollback.md
- pages/fe/development-environment-maintenance.md
- pages/fe/dhcp.md
- pages/fe/disk-scheduling.md
- pages/fe/disk-scheduling-scan.md
- pages/fe/dispatch-secondment-contract.md
- pages/fe/dns.md
- pages/fe/dram.md
- pages/fe/drive-by-download.md
- pages/fe/drive-by-download-attack.md
- pages/fe/economic-order-quantity.md
- pages/fe/effort-productivity-duration.md
- pages/fe/enterprise-architecture.md
- pages/fe/envelope-encryption.md
- pages/fe/fast-tracking.md
- pages/fe/fault-tolerant-system.md
- pages/fe/fe-requirements-definition-process.md
- pages/fe/feedback-feedforward-control.md
- pages/fe/fifo-page-replacement.md
- pages/fe/fixed-partition-memory-allocation.md
- pages/fe/floating-point-errors.md
- pages/fe/floating-point-format.md
- pages/fe/floating-point-normalization.md
- pages/fe/floating-point-representation.md
- pages/fe/full-differential-incremental-backup.md
- pages/fe/function-point-effort.md
- pages/fe/function-point-method.md
- pages/fe/functional-nonfunctional-requirements.md
- pages/fe/gantt-chart.md
- pages/fe/gompertz-curve.md
- pages/fe/gpl-license.md
- pages/fe/gpl-mit-bsd-license-comparison.md
- pages/fe/green-procurement.md
- pages/fe/green-purchasing.md
- pages/fe/hadoop-spark.md
- pages/fe/hamming-code.md
- pages/fe/hash-function-1.md
- pages/fe/hash-method-uniform-distribution.md
- pages/fe/hash-table.md
- pages/fe/hash-table-collision.md
- pages/fe/hex-binary-conversion.md
- pages/fe/hexadecimal-fraction.md
- pages/fe/hexadecimal-fraction-bit-shift.md
- pages/fe/hexadecimal-fraction-conversion.md
- pages/fe/hot-warm-cold-site.md
- pages/fe/hybrid-cloud.md
- pages/fe/hybrid-encryption.md
- pages/fe/ide-development-environment.md
- pages/fe/ide-eclipse.md
- pages/fe/incident-management-vs-problem-management.md
- pages/fe/incident-service-request-management.md
- pages/fe/inheritance.md
- pages/fe/input-data-check.md
- pages/fe/input-data-checks.md
- pages/fe/interface-usb-sata-ieee1394-1000base-t.md
- pages/fe/internal-control-components.md
- pages/fe/internal-control-six-elements.md
- pages/fe/is-a-part-of-instance-class.md
- pages/fe/it-investment-evaluation.md
- pages/fe/it-investment-management.md
- pages/fe/java-language-features.md
- pages/fe/java-programming-language.md
- pages/fe/logistic-curve.md
- pages/fe/lru.md
- pages/fe/lru-cache-replacement.md
- pages/fe/lru-page-replacement.md
- pages/fe/mac-address.md
- pages/fe/magnetic-disk-access-time.md
- pages/fe/magnetic-disk-average-wait-time.md
- pages/fe/memory-hierarchy.md
- pages/fe/memory-management-methods.md
- pages/fe/memory-types.md
- pages/fe/message-authentication-code.md
- pages/fe/mtbf.md
- pages/fe/mtbf-mttr.md
- pages/fe/nat.md
- pages/fe/nat-napt.md
- pages/fe/network-configuration-management.md
- pages/fe/network-device-functions-comparison.md
- pages/fe/network-devices-router-repeater-bridge-switch.md
- pages/fe/non-functional-requirements.md
- pages/fe/ntp.md
- pages/fe/on-demand-service.md
- pages/fe/operational-testing.md
- pages/fe/order-quantity-and-inventory-cost.md
- pages/fe/packet-filtering.md
- pages/fe/paging.md
- pages/fe/password-hash-authentication.md
- pages/fe/pdm-dependency-types.md
- pages/fe/physical-security-measures-comparison.md
- pages/fe/pki-certificate-authority.md
- pages/fe/planning-process.md
- pages/fe/polymorphism.md
- pages/fe/pppoe.md
- pages/fe/problem-management.md
- pages/fe/process-innovation.md
- pages/fe/progress-productivity-effort.md
- pages/fe/project-life-cycle.md
- pages/fe/project-lifecycle-characteristics.md
- pages/fe/project-management-process-groups.md
- pages/fe/project-management-subject-groups.md
- pages/fe/project-scope.md
- pages/fe/prototyping-model.md
- pages/fe/public-key-cryptography.md
- pages/fe/public-key-encryption-digital-signature.md
- pages/fe/rasis.md
- pages/fe/regression-testing.md
- pages/fe/relations-diagram.md
- pages/fe/rest-api.md
- pages/fe/reverse-brute-force.md
- pages/fe/risk-assessment-process.md
- pages/fe/risk-level.md
- pages/fe/router-bridge-repeater-gateway.md
- pages/fe/saas-paas-iaas.md
- pages/fe/scrum-events.md
- pages/fe/scrum-roles.md
- pages/fe/security-by-design.md
- pages/fe/security-cia.md
- pages/fe/security-guidelines-comparison.md
- pages/fe/security-threat-countermeasures.md
- pages/fe/series-parallel-system-availability.md
- pages/fe/server-client-port.md
- pages/fe/server-room-physical-security.md
- pages/fe/service-availability.md
- pages/fe/siem.md
- pages/fe/soc.md
- pages/fe/software-architecture-design.md
- pages/fe/software-design-phases.md
- pages/fe/software-license-contract-types.md
- pages/fe/software-license-minimum-cost.md
- pages/fe/spiral-model.md
- pages/fe/spooling.md
- pages/fe/sql-aggregate-functions.md
- pages/fe/sql-group-by-aggregate-functions.md
- pages/fe/sram.md
- pages/fe/stack-vs-queue.md
- pages/fe/standby-system.md
- pages/fe/state-transition-diagram.md
- pages/fe/state-transition-table.md
- pages/fe/stored-program-architecture.md
- pages/fe/stored-program-concept.md
- pages/fe/stub-driver.md
- pages/fe/subnet-host-address.md
- pages/fe/system-audit.md
- pages/fe/system-audit-regulations.md
- pages/fe/system-audit-techniques.md
- pages/fe/system-auditor-independence.md
- pages/fe/system-development-quality-management.md
- pages/fe/system-failure-monitoring.md
- pages/fe/system-test-audit.md
- pages/fe/three-tier-client-server.md
- pages/fe/throughput.md
- pages/fe/throughput-spooling.md
- pages/fe/tlo.md
- pages/fe/tlo-technology-licensing-organization.md
- pages/fe/top-down-bottom-up-test.md
- pages/fe/top-down-testing.md
- pages/fe/transaction-1.md
- pages/fe/transaction-state-transition.md
- pages/fe/twos-complement.md
- pages/fe/twos-complement-remainder.md
- pages/fe/usb.md
- pages/fe/usb-ieee1394.md
- pages/fe/usb-interface.md
- pages/fe/variable-partition-memory-allocation.md
- pages/fe/waterfall-model.md
- pages/fe/wbs.md
- pages/fe/web-api.md
- pages/fe/web-client-server.md
- pages/fe/white-box-testing.md
- pages/fe/work-made-for-hire.md
- pages/fe/work-made-for-hire-copyright.md

## 追加本文監査：数値表現・IT投資など（2026-10-17）

今回新たに16ファイルの本文を確認。既存ログとの重複は除外して追記しました。

- IT投資評価とIT投資マネジメント：評価時点と投資管理の視点が異なるため維持
- 16進小数の3記事：位取り・4ビット変換・ビットシフトの役割が異なるため維持
- 浮動小数点の4記事：基本構造・ビット形式・正規化・計算誤差の役割が異なるため維持
- 平均比較回数の2記事：ブロック探索と条件分岐の別問題なので維持
- 事業ドメイン・As-Is/To-Be・BIA：別概念のため維持
- このバッチで統合対象となる真の重複は見つかりませんでした。

- pages/fe/it-investment-evaluation.md
- pages/fe/it-investment-management.md
- pages/fe/binary-representation.md
- pages/fe/hex-binary-conversion.md
- pages/fe/hexadecimal-fraction.md
- pages/fe/hexadecimal-fraction-conversion.md
- pages/fe/hexadecimal-fraction-bit-shift.md
- pages/fe/floating-point-representation.md
- pages/fe/floating-point-format.md
- pages/fe/floating-point-normalization.md
- pages/fe/floating-point-errors.md
- pages/fe/block-search-average-comparisons.md
- pages/fe/conditional-branch-average-comparisons.md
- pages/fe/business-domain.md
- pages/fe/as-is-to-be-ea.md
## 自動抽出候補16組の本文・役割確認（2026-10-17）

全761実記事を走査し、しきい値を超えた16組（重複しない28記事）を本文・見出し・試験での判断基準で確認しました。いずれも**役割が異なるため維持**と判断し、新たな統合は行っていません。なお、しきい値未満の重複が存在しないと保証するものではありません。

| 候補の組合せ | 判断 | 理由 |
|---|---|---|
| `bottom-up-testing` / `top-down-testing` | 維持 | 下位→上位と上位→下位。ドライバとスタブの判断を分ける |
| `dram` / `sram` | 維持 | リフレッシュが必要な主記憶と、不要で高速なキャッシュ用途 |
| `enterprise-architecture` / `process-innovation` | 維持 | 組織・システム全体の設計と、業務工程の革新 |
| `bathtub-curve` / `logistic-curve` | 維持 | 時間による故障率と、普及・成長のS字変化 |
| `critical-chain` / `critical-path-vs-critical-chain` | 維持 | 資源制約・バッファの詳説と、パスとの比較 |
| `compiler-analysis-flow` / `compiler-linker-loader-debugger` | 維持 | コンパイラ内部の処理順と、翻訳・結合・読込みツールの役割 |
| `dns` / `nat` | 維持 | 名前解決とIPアドレス変換 |
| `fifo-page-replacement` / `lru-page-replacement` | 維持 | 主記憶に入った順と最後に参照した時刻 |
| `prototyping-model` / `spiral-model` | 維持 | 試作品で要求を確認する方式と、工程を繰り返す方式 |
| `checksum` / `crc` | 維持 | 総和・補数による誤り検出と、生成多項式による検出 |
| `checksum` / `hamming-code` | 維持 | 合計値での誤り検出と、誤り位置の特定・訂正 |
| `gompertz-curve` / `logistic-curve` | 維持 | テストの累積バグ推移と、一般的な普及・成長 |
| `commit-rollback` / `transaction-1` | 維持 | 確定・取消し操作の詳説と、トランザクションの総論 |
| `crc` / `hamming-code` | 維持 | CRCの誤り検出と、ハミング符号の訂正 |
| `rest-api` / `web-api` | 維持 | Web APIの一般概念と、RESTのリソース操作という設計スタイル |
| `packet-filtering` / `pppoe` | 維持 | 通信の許可・拒否と、Ethernet上のPPP接続方式 |

## 追加スキャン：判定しきい値15%（2026-10-17）

通常条件（本文重複率22%以上）の16組に対し、しきい値を15%に下げると**43組**が抽出されました。増分27組の本文・試験での判断基準を確認し、すべて**維持**と判断しました。うち「貸借対照表／HadoopとSpark」「C&Cサーバ／コンパイラ」などは、語句や表現が共通しただけの**誤検知**です。

| 追加候補 | 判断理由 |
|---|---|
| `cloud-deployment-models` / `hybrid-cloud` | クラウド形態の総合比較と、ハイブリッド構成の詳説 |
| `bathtub-curve` / `gompertz-curve` | 故障率の時間変化と、テスト時の累積バグ推移 |
| `network-device-functions-comparison` / `pppoe` | 機能横断比較と接続方式の個別解説 |
| `prototyping-model` / `waterfall-model` | 要求を試作品で確認する方式と工程順行の方式 |
| `affinity-diagram` / `relations-diagram` | 情報を分類する図法と因果関係をつなぐ図法 |
| `dhcp` / `pppoe` | IP設定の配布と接続方式 |
| `network-device-functions-comparison` / `packet-filtering` | ネットワーク機能の比較と許可・拒否の詳説 |
| `account-aggregation` / `crowdfunding` | 複数口座の情報集約と資金調達 |
| `command-and-control` / `compiler-linker-loader-debugger` | 感染端末の指令役と開発ツール。定型文由来のノイズ |
| `dhcp` / `nat` | IPアドレスの割当てと変換 |
| `black-box-testing` / `white-box-testing` | 外部仕様によるテストと内部構造によるテスト |
| `business-domain` / `core-competence` | どの事業領域で戦うかと企業固有の強み |
| `spiral-model` / `waterfall-model` | 工程を繰り返す方式と順行する方式 |
| `balance-sheet` / `hadoop-spark` | 財務諸表と分散処理。定型文由来のノイズ |
| `business-continuity-management` / `business-continuity-plan` | 継続的な運用改善の管理と計画そのもの |
| `dhcp` / `packet-filtering` | アドレス配布と通信許可・拒否 |
| `command-and-control` / `compiler-analysis-flow` | マルウェア指令とコンパイラ内部工程。定型文由来のノイズ |
| `mac-address` / `nat` | 機器識別のMACアドレスとIPアドレス変換 |
| `nat-napt` / `nat` | NAT/NAPTの比較とNAT単独の基本 |
| `dns` / `mac-address` | 名前解決と機器識別 |
| `crowdfunding` / `crowdsourcing` | 資金集めと仕事の募集 |
| `dhcp` / `network-device-functions-comparison` | DHCPの基本とネットワーク機能横断比較 |
| `inheritance` / `polymorphism` | 機能の継承と同一操作の振る舞いの変化 |
| `cidr-network-broadcast-address` / `subnet-host-address` | CIDRの計算工程と割り当て不可アドレスの判断 |
| `data-mining` / `data-warehouse` | 蓄積データの分析とデータ統合・保存基盤 |
| `nat` / `ntp` | IPアドレス変換と時刻同期 |
| `memory-management-methods` / `paging` | 記憶管理全体の総論とページング方式の詳説 |

自動抽出は**全761実記事へ2通りの条件で実施済み**ですが、全記事についての目視レビュー完了とは異なります。


## 追加監査：未確認53記事の学習目的比較（2026-10-17）

全件自動抽出で拾えない可能性がある重複を補うため、**ファイル名・概念上の関連が強い未確認53記事**の本文冒頭・見出し・試験での切り分け視点を確認しました。新たな統合対象はなく、いずれも**維持**の判定です。ここでの確認は各記事の逐語的な全文校正ではありません。

| 系統 | 記事名（ファイル名） | 役割の違い |
|---|---|---|
| オブジェクト指向 | class-instance / is-a-part-of-instance-class | クラスと実体の基本 ／ is-a・part-of・instance-ofの関係比較 |
| クライアントサーバ | client-server-system / server-client-port / three-tier-client-server / web-client-server | 要求と提供の役割 ／ ポート番号 ／ 三層の役割 ／ ブラウザ方式の導入・保守 |
| 共通フレーム | common-frame / common-frame-support-processes | 開発プロセスの全体像 ／ 検証・妥当性確認など支援プロセス |
| CPUスケジューリング | cpu-scheduling / cpu-scheduling-idle-time | 方式を見分ける ／ タスク状態とI/O待ちから遊休時間を追う |
| プロジェクト短縮 | crashing-vs-fast-tracking / fast-tracking | クラッシングとの比較 ／ ファストトラッキング単独の仕組み |
| ディスクスケジューリング | disk-scheduling / disk-scheduling-scan | FCFS・SSTF・SCAN比較 ／ SCANの移動順と距離計算 |
| ファンクションポイント | function-point-method / function-point-effort | 機能の重み付き合計からFP値算出 ／ FPと生産性から工数算出 |
| 状態遷移 | state-transition-diagram / state-transition-table / automaton-state-transition / transaction-state-transition | 図の基本 ／ 表の追跡 ／ オートマトンの入力出力 ／ DB取引の状態変化 |
| 二分木と探索 | binary-search-tree / binary-search / binary-tree-traversal / complete-binary-tree | 探索木の大小関係 ／ 整列済み配列の探索 ／ 走査順 ／ 木の節点数 |
| ハッシュ表 | hash-table / hash-table-collision | ハッシュ表の全体像 ／ modで最初の衝突を見つける |
| OSSライセンス | gpl-license / gpl-mit-bsd-license-comparison | GPL単独の配布条件 ／ GPL・MIT・BSD比較 |
| 2の補数 | twos-complement / twos-complement-remainder | 負数表現 ／ 下位ビット・剰余・負数の商の丸め |
| 主記憶の区画 | fixed-partition-memory-allocation / variable-partition-memory-allocation | 固定区画の内部断片化 ／ 可変区画の割当て・解放トレース |
| ネットワーク装置 | network-devices-router-repeater-bridge-switch / router-bridge-repeater-gateway | スイッチを含むOSI層比較 ／ ゲートウェイの方式変換を含む比較 |
| インタフェース | interface-usb-sata-ieee1394-1000base-t / usb-ieee1394 | 複数規格の特徴語比較 ／ USBとIEEE1394の共通点・ホットプラグ |
| 総当たり攻撃 | brute-force-attack / reverse-brute-force | パスワード等の総当たり ／ パスワード固定・IDを変える攻撃 |
| コールド／ウォーム | cold-warm-start / hot-warm-cold-site | 再起動の考え方 ／ 災害対策拠点の準備レベル |
| CPUのクロックと命令 | cpi-clock-cycle-cpu-time / cpu-clock-frequency / cpu-instruction-cycle | CPIと処理時間 ／ 内部・外部クロック ／ 命令実行工程 |
| 開発環境 | development-environment-maintenance / ide-development-environment | 開発環境の継続維持 ／ IDEというソフトウェアの役割 |
| 発注量 | economic-order-quantity / order-quantity-and-inventory-cost | 費用のバランス点EOQ ／ 割引等を含む年間総費用比較 |
| 工数 | effort-productivity-duration / progress-productivity-effort | 人月と要員数から期間 ／ 出来高率と投入工数から超過工数 |
| ソフトウェア契約 | software-license-contract-types / software-license-minimum-cost | 契約類型の見分け方 ／ 数量制約の下で最安の組合せを求める |
| 物理セキュリティ | physical-security-measures-comparison / server-room-physical-security | 紙・画面・端末の対策比較 ／ サーバ室の入退室・災害対策 |

**編集**：`disk-scheduling.md` と `disk-scheduling-scan.md` に総論とSCANの計算問題の行き先を追加。`order-quantity-and-inventory-cost.md` からEOQ記事へのリンクを追加。3記事とも元の公開日と本文構成を保持し、更新日のみ変更しました。

## 追加監査：未確認53記事と真の重複3組（2026-10-17）

過去の監査ログに載っていなかった53件を、本文冒頭・見出し・内容の使い分けで確認しました。さらに既存確認済みのIDE・LRUページ置換の2件も関連照合に使用しました。**類似語だけで統合せず、検索意図と教材の独自内容を比較**しています。

| 系統 | 判定 | 判断と対応 |
|---|---|---|
| ASP（`asp` / `asp-service`） | **統合** | 同じ定義と「場所・サーバ・アプリ・業務」の切り分け。図2種を`asp`に移し、旧URLを転送 |
| コード体系（`code-system-types` / `code-types-and-identification`） | **統合** | 4種類の定義・例・判断基準が重複。桁別コードも扱う前者に、Python例・確認問題を移し、旧URLを転送 |
| LRU（`lru` / `lru-cache-replacement`） | **統合** | LRUとFIFO/LFU/NRUの比較が重複。参照列とキャッシュの実例を持つ`lru`へ統合。ページ置換の詳細記事は維持 |
| グリーン調達・グリーン購入 | 維持 | 供給者の環境対応を含む調達判断／環境負荷が小さい製品の選択で重点が異なる |
| IDE2記事 | 維持 | Eclipseと言語（Perl/PHP/Ruby）の違い／EclipseとGCC・Tomcat・Linuxの違い |
| 文字コード・CSV | 維持 | 規格比較／ビット表の読解、CSV仕様／表計算でのセル参照は別の判断 |
| CSIRT・SOC・SIEM | 維持 | CSIRT資料／セキュリティ対応組織の比較／ログ相関分析に加え、SoCは半導体の別概念 |
| MTBF・RASIS・可用性・冗長化 | 維持 | 単体MTBF計算／MTBF・MTTR比較／RASIS／サービスの提供条件／直列並列／待機系は別の学習目的 |
| スループット・スプーリング | 維持 | 性能指標／改善効果／スプーリング機構の役割が異なる |
| メモリ階層・キャッシュ・ヒット率 | 維持 | 速度順／書込み方式／平均アクセス時間／メモリ種類を分担 |
| プロジェクト図法・スクラム・制御 | 維持 | PDM・アロー図・ガント・WBS、スクラムのイベント・役割、制御の判定を各別に説明 |
| テスト・品質管理・ベンチマーク | 維持 | 運用テスト／回帰テスト／品質管理／性能測定と、業務改善のベンチマーキングを区別 |

統合先の`date`・`permalink`・FE記事の既存構成を保持し、追加教材も残しました。旧ページは**HTTP 301ではなくHTML meta refreshの転送**で、`sitemap: false`・`noindex,follow`・canonicalを指定します。公開する前にGitHub Actions・Jekyllビルドを確認してください。

## 転送専用ページの確認（2026-10-17）

初回は1100バイト未満から17件を抽出しました。その後、**全778件の本文**を自動走査し、`layout: null` とHTMLのmeta refreshの両方を満たす17件を検出しました。

- 確認済み転送専用ページ: 20件（本PR適用後。うち3件は新規転送）
- 本PR適用後の実記事数: 758件（778 - 20）。HTML meta refresh以外の転送方式は判定対象外
- これらの転送はHTTP 301ではなく、HTML meta refreshです。

- pages/fe/activity-diagram.md
- pages/fe/black-box-vs-white-box-test.md
- pages/fe/capacity-management-analysis-models.md
- pages/fe/communication-encryption-eavesdropping.md
- pages/fe/drive-by-download-attack.md
- pages/fe/dual-vs-duplex-system.md
- pages/fe/fault-tolerance.md
- pages/fe/functional-nonfunctional-requirements.md
- pages/fe/input-data-check.md
- pages/fe/internal-control-components.md
- pages/fe/project-life-cycle.md
- pages/fe/security-cia.md
- pages/fe/software-architecture-design.md
- pages/fe/stored-program-architecture.md
- pages/fe/tlo.md
- pages/fe/uml-diagrams.md
- pages/fe/work-made-for-hire.md
- pages/fe/asp-service.md
- pages/fe/code-types-and-identification.md
- pages/fe/lru-cache-replacement.md

## 全件自動スキャンの実行方法（PR #438）

重複候補の抽出と転送ページ判定を、以下の標準ライブラリのみのスクリプトで再現できます。公開記事を自動変更・自動統合する機能はありません。

```bash
python -m unittest discover -s tests -p 'test_fe_duplicate_content.py' -v
python scripts/audit_fe_duplicate_content.py --output docs/audits/fe-duplicate-candidates.md
```

GitHub Actions の **FE duplicate content candidate audit** は、手動起動、またはFE記事・スクリプト関連のPR時に実行され、結果レポートを `fe-duplicate-candidates` というアーティファクトに保存します。**自動でmainへコミットしません。**

判定基準：転送は `layout: null` とHTML meta refreshの両方を確認。実記事の本文は前付け・見出し・コードなどを除いた文字列の9文字片で比較し、重なりの多い候補だけ抽出します。類似候補は**未審査**です。本文を読んで学習目的・選択肢の判断基準を比較するまで「重複確定」にしません。

## 次の手順

1. 今後の追加記事で転送ページ判定・実記事数が変わらないかを監視する。
2. 15%未満の重なりや未確認記事の個別監査を進める。
3. 統合・役割分担・維持・要再確認の判定理由を記録する。
4. 修正PRのビルドと旧URL転送を確認する。
