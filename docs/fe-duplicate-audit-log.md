# FE記事の重複監査ログ

ファイル名の一覧取得と本文監査の完了は別です。

## 対象と進捗

- GitHub mainの再帰ツリーを2026-10-17に取得
- FE Markdown: 778ファイル（転送用ページを含む）
- 過去の本文確認履歴に対応する現存ファイル: 422ファイル（重複排除）
- ファイル単位の確認履歴カバー率: 54.2%。これは全件本文比較の完了率ではありません。
- 削除済みファイルは分母・分子から除外。PR #441までの状態は転送21件・実記事757件。mainはPR #442まで反映済みで転送25件・実記事753件。PR #444の未反映分を含む今回のPR適用後は転送27件・実記事751件です。

- 実記事の個別確認履歴（今回のmain向け継続PR適用後）: **401/751件（53.4%）**。転送の27件は別管理。
- 変更前の761実記事に対して**機械的な類似候補抽出を実施済み**。PR #442の新しい構成ではCIで再走査します。未抽出の組合せが重複なしと確定したわけではありません。

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
- #440 ASP・コード体系・LRUの重複統合、関連記事の照合（マージ済み）
- #441 業務モデル2記事の統合と関連教材への学習導線改善（マージ済み）
- #442 損益計算書・メール・SCM・かんばん方式の重複4組の統合（mainにマージ済み）
- #444 CPU・OSの30記事監査と割込み・リンキングの2組統合（#442の作業ブランチにマージ済みだがmain未反映。今回のPRで反映）

## 本文確認履歴に含まれる現存ファイル

以下は確認履歴のインデックスです。記載されているだけで全本文の逐語比較や公開状態を確認済みとは判断しません。

- pages/fe/3d-printer.md
- pages/fe/account-aggregation.md
- pages/fe/acid-properties.md
- pages/fe/ad-conversion.md
- pages/fe/addressing-modes.md
- pages/fe/affinity-diagram.md
- pages/fe/agile-iteration.md
- pages/fe/ai-vs-rule-based-control.md
- pages/fe/anti-aliasing.md
- pages/fe/arp.md
- pages/fe/arp-rarp-dns-nat.md
- pages/fe/array.md
- pages/fe/arrow-diagram.md
- pages/fe/as-is-to-be-ea.md
- pages/fe/asp.md
- pages/fe/asp-service.md
- pages/fe/audit-evidence.md
- pages/fe/audit-working-papers.md
- pages/fe/authentication-devices.md
- pages/fe/automaton-state-transition.md
- pages/fe/backup-media-offsite-storage.md
- pages/fe/backup-methods.md
- pages/fe/backup-redundancy.md
- pages/fe/balance-sheet.md
- pages/fe/bathtub-curve.md
- pages/fe/benchmark-test.md
- pages/fe/benchmarking.md
- pages/fe/big-data-3v.md
- pages/fe/big-data-utilization-stages.md
- pages/fe/binary-representation.md
- pages/fe/binary-search.md
- pages/fe/binary-search-tree.md
- pages/fe/binary-tree-traversal.md
- pages/fe/biometric-authentication.md
- pages/fe/bit-mask.md
- pages/fe/bitmap-outline-font.md
- pages/fe/bitwise-operations-mask.md
- pages/fe/black-box-testing.md
- pages/fe/block-search-average-comparisons.md
- pages/fe/bottom-up-testing.md
- pages/fe/bpo-saas-hosting-comparison.md
- pages/fe/bpr.md
- pages/fe/break-even-point.md
- pages/fe/brute-force-attack.md
- pages/fe/business-continuity-management.md
- pages/fe/business-continuity-plan.md
- pages/fe/business-domain.md
- pages/fe/business-impact-analysis.md
- pages/fe/business-improvement-process.md
- pages/fe/business-model-four-types.md
- pages/fe/business-model-physical-logical.md
- pages/fe/cache-hit-rate-average-access-time.md
- pages/fe/cache-memory.md
- pages/fe/capacity-management-analysis-methods.md
- pages/fe/capacity-management-analysis-models.md
- pages/fe/cd-r.md
- pages/fe/certificate-authority.md
- pages/fe/challenge-response-authentication.md
- pages/fe/character-code-table.md
- pages/fe/character-encoding.md
- pages/fe/check-digit.md
- pages/fe/checksum.md
- pages/fe/cia-triad.md
- pages/fe/cidr-network-broadcast-address.md
- pages/fe/class-instance.md
- pages/fe/client-server-system.md
- pages/fe/clipping.md
- pages/fe/cloud-deployment-models.md
- pages/fe/code-system-types.md
- pages/fe/code-types-and-identification.md
- pages/fe/coding-conventions-safe-readable-code.md
- pages/fe/cold-warm-start.md
- pages/fe/command-and-control.md
- pages/fe/commit-rollback.md
- pages/fe/common-frame.md
- pages/fe/common-frame-support-processes.md
- pages/fe/compiler-analysis-flow.md
- pages/fe/compiler-linker-loader-debugger.md
- pages/fe/compiler-optimization.md
- pages/fe/complete-binary-tree.md
- pages/fe/computer-graphics-overview.md
- pages/fe/condition-branch-order.md
- pages/fe/conditional-branch-average-comparisons.md
- pages/fe/configuration-management.md
- pages/fe/contract-types-outsourcing.md
- pages/fe/control-structures-loop-selection.md
- pages/fe/control-total-check.md
- pages/fe/core-competence.md
- pages/fe/cpi-clock-cycle-cpu-time.md
- pages/fe/cpu-clock-frequency.md
- pages/fe/cpu-execution-overview.md
- pages/fe/cpu-instruction-cycle.md
- pages/fe/cpu-registers.md
- pages/fe/cpu-scheduling.md
- pages/fe/cpu-scheduling-idle-time.md
- pages/fe/crashing-vs-fast-tracking.md
- pages/fe/crc.md
- pages/fe/critical-chain.md
- pages/fe/critical-path-vs-critical-chain.md
- pages/fe/cross-compiler.md
- pages/fe/crowdfunding.md
- pages/fe/crowdsourcing.md
- pages/fe/cryptographic-algorithm-types.md
- pages/fe/csirt-material-1.md
- pages/fe/csirt-soc-psirt-jcrat.md
- pages/fe/csv-format.md
- pages/fe/csv-spreadsheet-cell-reference.md
- pages/fe/data-error-management.md
- pages/fe/data-flow-diagram.md
- pages/fe/data-mining.md
- pages/fe/data-oriented-design.md
- pages/fe/data-transfer-time.md
- pages/fe/data-warehouse.md
- pages/fe/database-backup-recovery.md
- pages/fe/database-consistency.md
- pages/fe/database-index.md
- pages/fe/database-log-recovery.md
- pages/fe/database-normalization.md
- pages/fe/database-recovery-rollforward-rollback.md
- pages/fe/database-schema.md
- pages/fe/deadlock.md
- pages/fe/depreciation-methods.md
- pages/fe/depreciation-straight-line.md
- pages/fe/development-environment-maintenance.md
- pages/fe/device-driver.md
- pages/fe/dhcp.md
- pages/fe/disk-scheduling.md
- pages/fe/disk-scheduling-scan.md
- pages/fe/disk-striping.md
- pages/fe/dispatch-secondment-contract.md
- pages/fe/display-types.md
- pages/fe/dmz-server-placement.md
- pages/fe/dns.md
- pages/fe/dram.md
- pages/fe/draw-software.md
- pages/fe/drive-by-download.md
- pages/fe/drive-by-download-attack.md
- pages/fe/ecc.md
- pages/fe/ecc-memory.md
- pages/fe/economic-order-quantity.md
- pages/fe/effort-productivity-duration.md
- pages/fe/email-protocols.md
- pages/fe/enterprise-architecture.md
- pages/fe/envelope-encryption.md
- pages/fe/equipment-investment-cost-effectiveness.md
- pages/fe/er-diagram.md
- pages/fe/er-diagram-cardinality.md
- pages/fe/evm.md
- pages/fe/exclusive-resource-task-timing.md
- pages/fe/fast-tracking.md
- pages/fe/fault-tolerant-system.md
- pages/fe/fe-requirements-definition-process.md
- pages/fe/feedback-feedforward-control.md
- pages/fe/fifo-inventory-valuation.md
- pages/fe/fifo-page-replacement.md
- pages/fe/five-functions-fetch-decode.md
- pages/fe/five-stage-pipeline.md
- pages/fe/fixed-partition-memory-allocation.md
- pages/fe/flash-memory.md
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
- pages/fe/hadoop.md
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
- pages/fe/hidden-line-and-surface-removal.md
- pages/fe/hot-warm-cold-site.md
- pages/fe/housing-service.md
- pages/fe/huffman-coding.md
- pages/fe/hybrid-cloud.md
- pages/fe/hybrid-encryption.md
- pages/fe/ide-development-environment.md
- pages/fe/ide-eclipse.md
- pages/fe/ids-ips-firewall.md
- pages/fe/image-video-formats.md
- pages/fe/incident-management-vs-problem-management.md
- pages/fe/incident-service-request-management.md
- pages/fe/income-statement-profit-levels.md
- pages/fe/inheritance.md
- pages/fe/initial-running-cost.md
- pages/fe/input-data-check.md
- pages/fe/input-data-checks.md
- pages/fe/input-data-completeness-control.md
- pages/fe/input-devices.md
- pages/fe/instruction-cache.md
- pages/fe/instruction-format.md
- pages/fe/instruction-register-program-counter.md
- pages/fe/interface-usb-sata-ieee1394-1000base-t.md
- pages/fe/internal-control-components.md
- pages/fe/internal-control-six-elements.md
- pages/fe/internal-external-interrupts.md
- pages/fe/internet-vpn.md
- pages/fe/interpreter-compiler-processing-time.md
- pages/fe/interrupt.md
- pages/fe/inventory-collection.md
- pages/fe/inventory-ordering-methods.md
- pages/fe/ip-mac-address-routing.md
- pages/fe/ipsec.md
- pages/fe/ipsec-l2tp-tls.md
- pages/fe/is-a-part-of-instance-class.md
- pages/fe/it-investment-evaluation.md
- pages/fe/it-investment-management.md
- pages/fe/java-language-features.md
- pages/fe/java-programming-language.md
- pages/fe/job-vs-task.md
- pages/fe/kanban-jit.md
- pages/fe/kanban-system.md
- pages/fe/lan-analyzer.md
- pages/fe/language-processor-comparison.md
- pages/fe/line-utilization-rate.md
- pages/fe/linked-list.md
- pages/fe/linker.md
- pages/fe/lock-granularity.md
- pages/fe/logistic-curve.md
- pages/fe/lru.md
- pages/fe/lru-cache-replacement.md
- pages/fe/lru-page-replacement.md
- pages/fe/mac-address.md
- pages/fe/magnetic-disk-access-time.md
- pages/fe/magnetic-disk-average-wait-time.md
- pages/fe/many-to-many-associative-entity.md
- pages/fe/memory-compaction.md
- pages/fe/memory-fragmentation.md
- pages/fe/memory-hierarchy.md
- pages/fe/memory-management-methods.md
- pages/fe/memory-types.md
- pages/fe/message-authentication-code.md
- pages/fe/microkernel.md
- pages/fe/middleware.md
- pages/fe/mips.md
- pages/fe/mips-processing-time.md
- pages/fe/morphing.md
- pages/fe/mpeg.md
- pages/fe/mtbf.md
- pages/fe/mtbf-mttr.md
- pages/fe/multicore-processor.md
- pages/fe/nat.md
- pages/fe/nat-napt.md
- pages/fe/net-present-value.md
- pages/fe/network-configuration-management.md
- pages/fe/network-device-functions-comparison.md
- pages/fe/network-devices-router-repeater-bridge-switch.md
- pages/fe/network-diagnostic-commands.md
- pages/fe/non-functional-requirements.md
- pages/fe/ntp.md
- pages/fe/ntp-time-synchronization.md
- pages/fe/on-demand-service.md
- pages/fe/operational-testing.md
- pages/fe/order-quantity-and-inventory-cost.md
- pages/fe/os-api.md
- pages/fe/ot-dmz.md
- pages/fe/overlay-paging-swapping.md
- pages/fe/packet-filtering.md
- pages/fe/packet-filtering-port-rules.md
- pages/fe/page-printer.md
- pages/fe/paging.md
- pages/fe/parity-check.md
- pages/fe/parity-circuit.md
- pages/fe/password-hash-authentication.md
- pages/fe/pcm-sampling-quantization-encoding.md
- pages/fe/pdm-dependency-types.md
- pages/fe/physical-security-measures-comparison.md
- pages/fe/ping.md
- pages/fe/pipe.md
- pages/fe/pipeline-control.md
- pages/fe/pki-certificate-authority.md
- pages/fe/planning-process.md
- pages/fe/polymorphism.md
- pages/fe/pop3-smtp-imap.md
- pages/fe/pppoe.md
- pages/fe/preemptive-scheduling.md
- pages/fe/primary-key.md
- pages/fe/problem-management.md
- pages/fe/process-innovation.md
- pages/fe/profit-calculation.md
- pages/fe/program-counter-interrupt.md
- pages/fe/progress-productivity-effort.md
- pages/fe/project-life-cycle.md
- pages/fe/project-lifecycle-characteristics.md
- pages/fe/project-management-process-groups.md
- pages/fe/project-management-subject-groups.md
- pages/fe/project-progress-weighted-effort.md
- pages/fe/project-scope.md
- pages/fe/prototyping-model.md
- pages/fe/pseudocode-reading-guide.md
- pages/fe/public-key-cryptography.md
- pages/fe/public-key-encryption-digital-signature.md
- pages/fe/python-indentation-code-blocks.md
- pages/fe/qr-code.md
- pages/fe/qr-code-barcode.md
- pages/fe/queue.md
- pages/fe/raid-levels.md
- pages/fe/rasis.md
- pages/fe/raster-vector-graphics.md
- pages/fe/recursion.md
- pages/fe/recursion-trace.md
- pages/fe/recursive-factorial.md
- pages/fe/recursive-function.md
- pages/fe/reentrant-program.md
- pages/fe/referential-integrity.md
- pages/fe/regression-testing.md
- pages/fe/relational-model.md
- pages/fe/relational-operations.md
- pages/fe/relations-diagram.md
- pages/fe/relocation.md
- pages/fe/rest-api.md
- pages/fe/reverse-brute-force.md
- pages/fe/reverse-polish-notation.md
- pages/fe/risc-cisc.md
- pages/fe/risk-assessment-process.md
- pages/fe/risk-level.md
- pages/fe/roi.md
- pages/fe/rollback-rollforward.md
- pages/fe/rom-types.md
- pages/fe/round-robin-scheduling.md
- pages/fe/router-bridge-repeater-gateway.md
- pages/fe/run-length-encoding.md
- pages/fe/saas-paas-iaas.md
- pages/fe/scm.md
- pages/fe/scrum-events.md
- pages/fe/scrum-roles.md
- pages/fe/sd-sdhc-sdxc-sduc.md
- pages/fe/security-by-design.md
- pages/fe/security-cia.md
- pages/fe/security-guidelines-comparison.md
- pages/fe/security-threat-countermeasures.md
- pages/fe/series-parallel-system-availability.md
- pages/fe/server-client-port.md
- pages/fe/server-room-physical-security.md
- pages/fe/service-availability.md
- pages/fe/shared-exclusive-lock.md
- pages/fe/shell.md
- pages/fe/shell-redirection.md
- pages/fe/shortest-job-first-scheduling.md
- pages/fe/siem.md
- pages/fe/snmp.md
- pages/fe/soc.md
- pages/fe/software-architecture-design.md
- pages/fe/software-design-phases.md
- pages/fe/software-license-contract-types.md
- pages/fe/software-license-minimum-cost.md
- pages/fe/speculative-execution.md
- pages/fe/spiral-model.md
- pages/fe/spooling.md
- pages/fe/sql-aggregate-functions.md
- pages/fe/sql-group-by-aggregate-functions.md
- pages/fe/sram.md
- pages/fe/sram-dram.md
- pages/fe/stack.md
- pages/fe/stack-vs-queue.md
- pages/fe/standby-system.md
- pages/fe/state-transition-diagram.md
- pages/fe/state-transition-table.md
- pages/fe/static-dynamic-linking.md
- pages/fe/storage-media-read-write-methods.md
- pages/fe/stored-program-architecture.md
- pages/fe/stored-program-concept.md
- pages/fe/structured-unstructured-data.md
- pages/fe/stub-driver.md
- pages/fe/subnet-host-address.md
- pages/fe/supply-chain-management.md
- pages/fe/system-audit.md
- pages/fe/system-audit-regulations.md
- pages/fe/system-audit-techniques.md
- pages/fe/system-auditor-independence.md
- pages/fe/system-development-quality-management.md
- pages/fe/system-failure-monitoring.md
- pages/fe/system-test-audit.md
- pages/fe/task-dispatch_revised.md
- pages/fe/task-scheduling.md
- pages/fe/tcp-connection-identification.md
- pages/fe/tcp-udp-port-number.md
- pages/fe/three-tier-client-server.md
- pages/fe/throughput.md
- pages/fe/throughput-spooling.md
- pages/fe/tlo.md
- pages/fe/tlo-technology-licensing-organization.md
- pages/fe/top-down-bottom-up-test.md
- pages/fe/top-down-testing.md
- pages/fe/touch-panel.md
- pages/fe/transaction-1.md
- pages/fe/transaction-atomicity-rollback.md
- pages/fe/transaction-state-transition.md
- pages/fe/two-phase-commit.md
- pages/fe/twos-complement.md
- pages/fe/twos-complement-remainder.md
- pages/fe/uml-multiplicity.md
- pages/fe/usb.md
- pages/fe/usb-ieee1394.md
- pages/fe/usb-interface.md
- pages/fe/variable-partition-memory-allocation.md
- pages/fe/video-bandwidth-calculation.md
- pages/fe/virtual-memory.md
- pages/fe/waf.md
- pages/fe/waterfall-model.md
- pages/fe/wbs.md
- pages/fe/web-api.md
- pages/fe/web-client-server.md
- pages/fe/weighted-average-inventory-valuation.md
- pages/fe/white-box-testing.md
- pages/fe/work-made-for-hire.md
- pages/fe/work-made-for-hire-copyright.md
- pages/fe/xor-bit-flip.md

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

## 追加監査：未確認64記事と業務モデルの統合（2026-10-17）

タイトルだけでは見つけにくい重複を補うため、70記事の**定義・本文冒頭・見出し・試験での判断基準**を照合しました。過去の監査ログと重なる6記事を除き、**新たに64ファイル**を確認履歴へ追加しています。この確認は全段落の逐語校正ではありません。

| 関連する記事群 | 判断と対応 |
|---|---|
| 業務モデルの4種類（`business-model-four-types`／`business-model-physical-logical`） | **実質的な重複のため統合**。詳細な4モデルの説明を前者に集約し、確認問題・「データクラス」の注意書きを維持。後者の旧URLはHTML転送 |
| ビットマスク／AND・OR・XOR・NAND／XORによる反転 | マスクの位置・演算の仕組み・XORの具体例を分担するため**維持**。相互リンクを追加 |
| 再帰処理／再帰関数／階乗／再帰トレース | 呼出しの行き戻り・終了条件・階乗・トレース実演を分担するため**維持**。基本記事から計算・可視化への導線を追加 |
| パリティチェック／パリティ回路／ハミング／CRC／チェックサム | 検査ビット付加・XOR回路・誤り訂正・生成多項式・総和チェックは別機能のため**維持**。パリティ2記事へ相互リンク追加 |
| A/D変換／PCM | 分解能・ノイズ対策／標本化→量子化→符号化の切り分けで**維持**。相互リンク追加 |
| 仮想記憶・断片化・コンパクション・オーバーレイ | 現象・対策・移動時間・管理手法比較は別の学習目的のため**維持** |
| HadoopとSpark／QRコードとバーコード／バックアップ媒体の外部保管 | 個別定義／比較／運用安全管理の役割が異なるため**維持** |
| IPsec・VPN・L2TP・DMZ・WAF・パケットフィルタ・TCPポート | 保護する層・通信の対象・実際のフィルタ条件・接続識別が異なるため**維持** |
| 減価償却／ROI・NPV・投資の費用対効果／EVM・工程工数 | 償却の基本・当期費用計算・投資評価・進捗管理で判断の対象が異なるため**維持** |
| BPR・業務改善／入力チェックとコントロールトータル | 抜本的な改革と改善手順／個々の入力値チェックと合計照合を区別し**維持** |
| ジョブとタスク／CPUスケジューリング／ラウンドロビン／処理時間順 | 管理対象・中断可否・割当計算・実行順の計算を分担するため**維持** |

**注意**：本文スキャンは定型句に影響されるので、自動スコアが低くても「内容の目的が同じ」なら手動照合します。今回の統合もその経緯です。

## 追加監査：未登録34ファイル・実質重複4組（2026-10-17）

タイトルや本文で扱う判断基準から36ファイルを照合しました。過去の確認履歴に載っていた2ファイルを除き、**新たに34ファイル**を確認履歴へ記録しています。今回の判定は定義・本文・見出し・試験での切り分けに関する照合であり、全段落を逐語校正したものではありません。

| 記事群 | 判定 | 対応・理由 |
|---|---|---|
| `profit-calculation` / `income-statement-profit-levels` | **統合** | 5種類の利益と加減算の基準が同一。正規記事`income-statement-profit-levels`へ段階図と数値計算例を移し、旧URLを転送 |
| `pop3-smtp-imap` / `email-protocols` | **統合** | SMTP／POP3／IMAPの送受信の役割が重複。正規記事`email-protocols`へ確認問題・PAP/CHAPとの混同防止・RFC参照を移し、旧URLを転送 |
| `supply-chain-management` / `scm` | **統合** | SCMの定義と全体最適・CRMとの切り分けが重複。`scm`にERPとの違い・企業間連携・出典を加え、旧URLを転送 |
| `kanban-jit` / `kanban-system` | **統合** | 後工程引取り・JITとの関係・中間在庫減が重複。`kanban-system`へ実務の補充例と「在庫は必ずゼロではない」という注意を追加し、旧URLを転送 |
| `mips` / `mips-processing-time` | 維持 | CPI・クロックからMIPSを求める／既知のMIPSからCPU時間とI/O待ちを求める。計算対象が異なるため相互リンク |
| `data-flow-diagram` / `data-oriented-design` | 維持 | DFDの記号・データの流れの読解／共有データを中心にした設計思想 |
| `housing-service` / `asp` | 維持 | サーバ設置場所を借りる／アプリケーション機能を提供する。提供対象が異なる |
| `inventory-ordering-methods` / `inventory-collection` | 維持 | 商品や部品の発注方式／PC資産のハード・ソフト収集。inventoryという語が共通するだけ |
| `fifo-inventory-valuation` / `weighted-average-inventory-valuation` | 維持 | 先入先出法の残存在庫計算／総平均・移動平均法の単価計算 |
| `sram-dram` / キャッシュ・メモリ種類 | 維持 | SRAM/DRAMの比較／キャッシュ・主記憶の用途という異なる切り口 |
| `big-data-3v` / `big-data-utilization-stages` / `structured-unstructured-data` | 維持 | データの性質3V／活用の4段階／構造の3分類 |
| `database-index` / `database-normalization` / `database-schema` / `database-consistency` | 維持 | 性能／重複排除／構造定義／整合性の保持で別概念 |
| `primary-key` / `referential-integrity` / `relational-model` / `relational-operations` | 維持 | 主キー制約／外部キー制約／関係の基本／選択・射影・結合 |
| `er-diagram` / `er-diagram-cardinality` / `many-to-many-associative-entity` / `uml-multiplicity` | 維持 | ER図の基本／多重度を読む／連関エンティティへ変換／UMLクラス図で読む。ER多重度から連関エンティティへ相互リンク |
| `instruction-register-program-counter` / `cpu-registers` | 維持 | 命令フェッチのPC・IRの違い／CPUの各種レジスタの総論 |

統合記事は、旧URLに`layout: null`とHTML meta refresh・canonical・`noindex,follow`を設定しました。**HTTP 301による転送ではありません。** 正規記事は初回公開日・URL・見出し構成・フッターを保持しています。実公開の転送挙動とJekyllビルドはマージ後に確認してください。

## 継続監査：ネットワーク・DB・排他制御の未確認16記事（2026-10-17）

PR #442の既存履歴352ファイルと照合し、未登録16実記事を追加しました。定義・本文冒頭・見出し・科目Aの判断基準・独自の計算例を関連ページと比較した範囲の監査です。全段落の逐語校正や全記事間の総当たり比較ではありません。今回、新たな統合・公開記事の編集は行いません。

| 記事群 | 判定と根拠 |
|---|---|
| `arp` / `arp-rarp-dns-nat` / `ip-mac-address-routing` | 維持。ARP要求・応答・キャッシュ／4用語の変換元と変換先の比較／ルータ通過前後の宛先IP・MACを分担。比較から個別解説への既存リンクもある |
| `network-diagnostic-commands` / `ping` / `snmp` / `lan-analyzer` | 維持。コマンドの目的別選択／ICMP Echoと応答しない場合の注意／マネージャ・エージェントによる状態監視／パケットの取得・解析は異なる。ARP記事とも照合 |
| `ntp-time-synchronization` / 既存確認済み`ntp` | 維持。4時刻・往復遅延・サーバ処理時間から時計差を求める計算／時刻同期プロトコルとNNTP・SMTP・SNMPの識別を分担 |
| `rollback-rollforward` / 既存確認済みのDB復旧・ログ記事 | 維持。更新前・更新後情報の使い分け／リストアからの復旧順序・コミット済み判定／ログによる回復の仕組みを分担。既存の役割説明・相互リンクを確認 |
| `transaction-atomicity-rollback` / `acid-properties` / 既存確認済み`transaction-1`・`commit-rollback` | 維持。SQL実行後に異常終了した表の状態・原子性とデッドロック／ACID4特性の比較／処理単位の総論／確定と取消操作の識別で役割が異なる。原子性記事のDELETE・NULLの比較など独自説明を維持 |
| `two-phase-commit` / `shared-exclusive-lock` / `lock-granularity` / `deadlock` | 維持。分散サイトの準備・確定／ロックの両立性／ロック範囲と並列性・管理負荷／取得順序と循環待ちを分担。2相コミットと2相ロッキングを同一視しない |
| `exclusive-resource-task-timing` / 既存確認済みのタスク・CPU遊休時間記事 | 維持。複数CPUでも共通資源が1つなら待つという終了時刻の計算／CPUを選ぶ方式／I/O待ちからCPU遊休時間を求める計算は別の判断 |

SG・DS・GKの関連語も検索し、テーマをまたぐ記事はFE内の統合候補件数へ含めていません。構成・分類の別監査や出典の最新性監査は今回の範囲外です。

### 進捗の再集計

- 最新main（`bdfba2a9`、PR #443まで）：778ファイル、転送21件、実記事757件。mainログの確認履歴303実記事（40.0%）。
- PR #442の既存変更：転送4件追加、確認履歴333/753実記事（44.2%）。
- 今回16実記事追加後：**349/753実記事（46.3%）**。未確認404実記事。
- ファイル単位の確認履歴は368/778件（47.3%）。うち19件は転送ページ。全転送25件のうち6件は冒頭の履歴インデックスとは別の転送確認一覧だけにあるため、368−25で実記事数を計算しない。
- PR #442は未マージ。main反映済みの進捗と、PR適用後の進捗を区別する。

## 継続監査：CPU・OS・言語処理の未確認30記事（2026-10-17）

前回の確認履歴368ファイルと照合し、未登録30ファイルを追加しました。定義・冒頭・見出し・科目Aの判断基準を比較し、統合対象の4記事は本文全体を照合しました。全記事間の総当たり比較や全段落の校正を終えた割合ではありません。

| 記事群 | 判定・対応 |
|---|---|
| `interrupt` / `internal-external-interrupts` | **統合**。分類基準・タイマー・ゼロ除算・ページフォールト等の学習目的が同じ。同期／非同期、ポーリング、ウォッチドッグ、システムコール、出典を持つ後者を正規記事に維持。前者の内容は後者に含まれるため、割込みの基本定義を冒頭に補い旧URLを転送 |
| `linker` / `static-dynamic-linking` | **統合**。結合の時点とインタプリタ／オーバレイとの混同防止が重複。相互参照解決、ロードモジュール、ローダとの比較も持つ前者を維持。後者の「何をしているか→いつ行うか」の判断順を明示し旧URLを転送 |
| `cpu-execution-overview` / `five-functions-fetch-decode` / `instruction-format` / `addressing-modes` | 維持。CPU用語をつなぐ地図／五大機能の担当／命令コードとオペランド／有効アドレス算出で役割が異なる。既存確認済みの命令サイクル・レジスタ記事とも照合 |
| `five-stage-pipeline` / `pipeline-control` / `speculative-execution` / `risc-cisc` / `multicore-processor` | 維持。5段の順序とサイクル数／段の細分化と命令同時実行の比較／予測に基づく先行実行／命令セットの設計思想／複数コアの並列性と共有資源を分担 |
| `instruction-cache` / 既存確認済みキャッシュ記事 | 維持。命令配置と局所性／キャッシュの基本・書込み方式／ヒット率の計算は別の判断 |
| `program-counter-interrupt` / `preemptive-scheduling` / `task-dispatch_revised` | 維持。復帰位置の保存／優先度に応じた中断後の状態／CPU使用権の割当て。既存のスケジューリング・レジスタ記事とも区別。割込みの正規記事からPCの解説へリンク |
| `compiler-optimization` / `cross-compiler` / `language-processor-comparison` / `interpreter-compiler-processing-time` | 維持。生成コードの効率改善／別環境向けの生成／入力と出力による処理系比較／繰返し実行時の総時間計算。既存確認済みの解析工程・ツール比較記事とも区別 |
| `relocation` / `reentrant-program` | 維持。ロード位置に応じたアドレス補正／再入・再帰・再使用・再配置の性質比較。リンキングの結合処理とも区別 |
| `middleware` / `device-driver` / `os-api` / `microkernel` | 維持。共通機能を提供する層／機器固有制御／OS機能の呼出し口／カーネルに置く機能の設計を分担 |
| `shell` / `shell-redirection` / `pipe` | 維持。コマンドの解釈／入出力の接続先変更／コマンド間の出力→入力接続。記号の判定・実行例という独自内容がある |

- 本バッチの図解評価：統合元の説明図と判断表は統合先でも説明済み。既存の流れ図・表を保持し、重複する図や新たな操作UIは追加しない。
- 正規記事の初回`date`・`permalink`・分類・6見出し・FEフッターを保持し、`last_modified_at`だけ更新。既存の別名`/fe/internal-external-interrupt/`も維持。
- SG・DS・GKの関連語検索も行い、テーマをまたぐ記事の統合はしない。出典の更新やシラバスの鮮度監査は今回の範囲外。
- PR #442を前提に、778 Markdown・転送27・実記事751。確認履歴398ファイル（転送21・実記事377）、**377/751実記事（50.2%）**、未確認374実記事。
- main反映済みは303/757実記事（40.0%）。上記50.2%は前提PRと継続PRがともに適用された場合の値。

## 継続監査：画像・CG・記憶媒体・圧縮の未確認24記事（2026-10-17）

前回の履歴398ファイルに含まれない24実記事を追加確認しました。定義・本文冒頭・見出し・科目Aの判断基準と、重なりの大きい説明部分を照合しています。全段落の逐語校正や全記事間比較の完了率ではありません。新たな統合対象はありません。

| 記事群 | 判定・対応 |
|---|---|
| `computer-graphics-overview` / `anti-aliasing` / `clipping` / `hidden-line-and-surface-removal` / `morphing` | 維持。CG工程の地図／輪郭のギザギザ／表示範囲外の除外／視点と遮蔽物による可視性・Zバッファ／中間画像での変形を分担 |
| `raster-vector-graphics` / `draw-software` / `bitmap-outline-font` | 維持。画像データの表現とSVG／図形・画素単位の編集ソフト／文字の保存方式と等幅・プロポーショナルの別軸を扱う。既存の関連リンクも確認 |
| `image-video-formats` / `mpeg` | 維持。静止画・音声・動画と可逆性の横断比較／MPEG-1・2・4とH.264の用途・配信制御との違い。横断比較からMPEGの詳説へのリンクがある |
| `huffman-coding` / `run-length-encoding` | 維持。出現頻度・プレフィックス・平均符号長／同じ値の連続回数と並び方という異なる圧縮原理 |
| `rom-types` / `flash-memory` / `sd-sdhc-sdxc-sduc` | 維持。ROM系の消去・再書込みの比較／フラッシュの書換え耐久性・消去の仕組み／カードの容量・ファイルシステム規格。ROMとフラッシュの相互リンクを確認 |
| `storage-media-read-write-methods` / `cd-r` | 維持。磁気・光磁気・光の記録／読取りの比較／有機色素と追記・CD-RWとの違い。CD-Rから媒体比較へのリンクがある |
| `disk-striping` / `raid-levels` | **役割整理して維持**。前者のb0〜b15の分散配置図と図問題の読解を残し、重複するRAID0・1・5の詳細比較は短い説明と後者へのリンクに整理。後者からも配置図へ誘導 |
| `input-devices` / `touch-panel` / `display-types` | 維持。文字・マーク・画像・座標の入力対象／タッチの検出原理／表示の発光方式で判断軸が違う |
| `page-printer` / `3d-printer` | 維持。ページ単位の画像展開・ドライバとフォント処理／3Dデータからの実物造形。フォント記事とも役割が違う |

SG・DS・GKも関連語で検索し、テーマ外の記事は本監査の件数に含めません。出典の最新性や記事内容の全面校正は別監査です。ストライピングは既存配置図で学べるため、新しい操作UIは追加しません。

### mainへの反映と進捗

- main（`f692505b`、PR #442まで）：実記事753、確認履歴349（46.3%）。
- #444は#442の作業ブランチにマージされており、mainにはCPU・OS監査と2組統合が未反映。今回のmain向けPRへ同じ変更を取り込み、最新mainの逆ポーランド図解などは保持。
- 今回24記事追加後：778 Markdown・転送27・実記事751、確認履歴422ファイル（転送21・実記事401）。**401/751実記事（53.4%）**、未確認350実記事。
- PRのマージ済み表示だけで公開反映済みと判断せず、mainの本文と履歴を照合した。

## 転送専用ページの確認（2026-10-17）

初回は1100バイト未満から17件を抽出しました。その後、**全778件の本文**を自動走査し、`layout: null` とHTMLのmeta refreshの両方を満たす17件を検出しました。

- 確認済み転送専用ページ: 27件（PR #442と継続PR適用後。今回2件追加）
- PR #442と継続PR適用後の実記事数: 751件（778 - 27）。HTML meta refresh以外の転送方式は判定対象外
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
- pages/fe/business-model-physical-logical.md


- pages/fe/profit-calculation.md
- pages/fe/pop3-smtp-imap.md
- pages/fe/supply-chain-management.md
- pages/fe/kanban-jit.md

- pages/fe/interrupt.md
- pages/fe/static-dynamic-linking.md

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
