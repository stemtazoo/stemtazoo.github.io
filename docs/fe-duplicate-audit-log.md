# FE記事の重複監査ログ

ファイル名の一覧取得と本文監査の完了は別です。

## 対象と進捗

- GitHub mainのFEファイル構成を2026-10-18に再確認
- FE Markdown: 778ファイル（転送用ページを含む）
- 過去の本文確認履歴に対応する現存ファイル: 638ファイル（重複排除）
- ファイル単位の確認履歴カバー率: 82.0%。これは全件本文比較の完了率ではありません。
- 削除済みファイルは分母・分子から除外。mainはPR #451まで反映済みで転送29件・実記事749件。今回は新たな統合を行わないため実記事数は変わりません。

- 実記事の個別確認履歴（今回のmain向け継続PR適用後）: **615/749件（82.1%）**。転送の29件は別管理。
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
- #444 CPU・OSの30記事監査と割込み・リンキングの2組統合（#445でmainへ反映済み）
- #445 画像・記憶媒体24記事監査とRAIDの役割整理、#444のmain反映（マージ済み）
- #446 開発・テスト・品質管理30記事監査、開発・運用連携記事の統合（マージ済み）
- #447 ネットワーク・セキュリティ30記事監査、CPSFの重複統合（マージ済み）
- #448 経営戦略・業務30記事監査、ニッチ戦略の導線整理（マージ済み）
- #449 セキュリティ・関連法務30記事監査、検知・メール対策の導線整理（マージ済み）
- #450 アルゴリズム・数理32記事監査、確率・ビット数の導線整理（マージ済み）
- #451 DB・Web・データ形式32記事監査、複式簿記とSQLの導線整理（マージ済み）

## 本文確認履歴に含まれる現存ファイル

以下は確認履歴のインデックスです。記載されているだけで全本文の逐語比較や公開状態を確認済みとは判断しません。

- pages/fe/3d-printer.md
- pages/fe/3pl.md
- pages/fe/absolute-relative-path.md
- pages/fe/account-aggregation.md
- pages/fe/acid-properties.md
- pages/fe/actuator.md
- pages/fe/ad-conversion.md
- pages/fe/address-bus-data-bus.md
- pages/fe/addressing-modes.md
- pages/fe/adjacency-matrix.md
- pages/fe/adsl.md
- pages/fe/affinity-diagram.md
- pages/fe/agile-iteration.md
- pages/fe/ai-vs-rule-based-control.md
- pages/fe/ajax.md
- pages/fe/ansoff-growth-matrix.md
- pages/fe/anti-aliasing.md
- pages/fe/application-maintenance.md
- pages/fe/archive.md
- pages/fe/arp.md
- pages/fe/arp-rarp-dns-nat.md
- pages/fe/array.md
- pages/fe/arrow-diagram.md
- pages/fe/as-is-to-be-ea.md
- pages/fe/asp.md
- pages/fe/asp-service.md
- pages/fe/assertion-check.md
- pages/fe/atm.md
- pages/fe/audit-evidence.md
- pages/fe/audit-working-papers.md
- pages/fe/augmented-reality.md
- pages/fe/authentication-devices.md
- pages/fe/authenticity-reliability-security.md
- pages/fe/automaton-state-transition.md
- pages/fe/backup-media-offsite-storage.md
- pages/fe/backup-methods.md
- pages/fe/backup-redundancy.md
- pages/fe/balance-sheet.md
- pages/fe/bathtub-curve.md
- pages/fe/bayes-theorem.md
- pages/fe/behavioral-targeting.md
- pages/fe/benchmark-test.md
- pages/fe/benchmarking.md
- pages/fe/bi.md
- pages/fe/big-data-3v.md
- pages/fe/big-data-utilization-stages.md
- pages/fe/binary-decimal-digit-count.md
- pages/fe/binary-representation.md
- pages/fe/binary-search.md
- pages/fe/binary-search-tree.md
- pages/fe/binary-tree-traversal.md
- pages/fe/biometric-authentication.md
- pages/fe/bit-mask.md
- pages/fe/bit-pattern-count.md
- pages/fe/bitmap-outline-font.md
- pages/fe/bitwise-operations-mask.md
- pages/fe/black-box-testing.md
- pages/fe/black-box-vs-white-box-testing.md
- pages/fe/block-search-average-comparisons.md
- pages/fe/blue-ocean-strategy.md
- pages/fe/bluetooth.md
- pages/fe/bottom-up-testing.md
- pages/fe/bpm.md
- pages/fe/bpo-saas-hosting-comparison.md
- pages/fe/bpr.md
- pages/fe/branch-coverage.md
- pages/fe/break-even-point.md
- pages/fe/brute-force-attack.md
- pages/fe/buffer-size-transfer-rate.md
- pages/fe/bug-management-chart.md
- pages/fe/bug-seeding.md
- pages/fe/business-continuity-management.md
- pages/fe/business-continuity-plan.md
- pages/fe/business-domain.md
- pages/fe/business-impact-analysis.md
- pages/fe/business-improvement-process.md
- pages/fe/business-model-four-types.md
- pages/fe/business-model-physical-logical.md
- pages/fe/byod.md
- pages/fe/cache-hit-rate-average-access-time.md
- pages/fe/cache-memory.md
- pages/fe/call-by-value.md
- pages/fe/capacity-management-analysis-methods.md
- pages/fe/capacity-management-analysis-models.md
- pages/fe/captcha.md
- pages/fe/case-tools.md
- pages/fe/cd-r.md
- pages/fe/certificate-authority.md
- pages/fe/cgi.md
- pages/fe/challenge-response-authentication.md
- pages/fe/character-code-table.md
- pages/fe/character-encoding.md
- pages/fe/chattering.md
- pages/fe/check-digit.md
- pages/fe/checksum.md
- pages/fe/cia-triad.md
- pages/fe/cidr-network-broadcast-address.md
- pages/fe/class-instance.md
- pages/fe/client-server-system.md
- pages/fe/clipping.md
- pages/fe/cloud-deployment-models.md
- pages/fe/cmmi.md
- pages/fe/code-system-types.md
- pages/fe/code-types-and-identification.md
- pages/fe/coding-conventions-safe-readable-code.md
- pages/fe/cold-warm-start.md
- pages/fe/command-and-control.md
- pages/fe/commit-rollback.md
- pages/fe/commoditization.md
- pages/fe/common-frame.md
- pages/fe/common-frame-support-processes.md
- pages/fe/communication-paths-combination.md
- pages/fe/competitive-position-strategy.md
- pages/fe/compiler-analysis-flow.md
- pages/fe/compiler-linker-loader-debugger.md
- pages/fe/compiler-optimization.md
- pages/fe/complete-binary-tree.md
- pages/fe/computer-graphics-overview.md
- pages/fe/computer-unauthorized-access-countermeasure-standard.md
- pages/fe/condition-branch-order.md
- pages/fe/conditional-branch-average-comparisons.md
- pages/fe/conditional-probability.md
- pages/fe/configuration-management.md
- pages/fe/contract-types-outsourcing.md
- pages/fe/control-structures-loop-selection.md
- pages/fe/control-total-check.md
- pages/fe/conversion-rate.md
- pages/fe/corba.md
- pages/fe/core-competence.md
- pages/fe/core-technology.md
- pages/fe/correlation-coefficient.md
- pages/fe/counting-constrained-strings.md
- pages/fe/cpi-clock-cycle-cpu-time.md
- pages/fe/cpsf.md
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
- pages/fe/csma-ca.md
- pages/fe/csma-cd.md
- pages/fe/csv-format.md
- pages/fe/csv-spreadsheet-cell-reference.md
- pages/fe/customer-portfolio-analysis.md
- pages/fe/cyber-physical-security-framework.md
- pages/fe/cybercrime-laws.md
- pages/fe/cybersecurity-management-guideline.md
- pages/fe/daisy-chain.md
- pages/fe/data-dictionary.md
- pages/fe/data-error-management.md
- pages/fe/data-flow-diagram.md
- pages/fe/data-mining.md
- pages/fe/data-oriented-design.md
- pages/fe/data-transfer-time.md
- pages/fe/data-warehouse.md
- pages/fe/database-administrator.md
- pages/fe/database-backup-recovery.md
- pages/fe/database-consistency.md
- pages/fe/database-index.md
- pages/fe/database-log-recovery.md
- pages/fe/database-normalization.md
- pages/fe/database-performance-troubleshooting.md
- pages/fe/database-recovery-rollforward-rollback.md
- pages/fe/database-schema.md
- pages/fe/database-view-select-privilege.md
- pages/fe/dc-power-feeding.md
- pages/fe/deadlock.md
- pages/fe/debit-credit-double-entry.md
- pages/fe/decimal-to-binary-div-mod.md
- pages/fe/defect-repair-cost-expected-value.md
- pages/fe/depreciation-methods.md
- pages/fe/depreciation-straight-line.md
- pages/fe/development-environment-maintenance.md
- pages/fe/development-operations-collaboration.md
- pages/fe/device-driver.md
- pages/fe/dfs-vs-bfs.md
- pages/fe/dhcp.md
- pages/fe/digital-watermark.md
- pages/fe/disk-scheduling.md
- pages/fe/disk-scheduling-scan.md
- pages/fe/disk-striping.md
- pages/fe/dispatch-secondment-contract.md
- pages/fe/display-types.md
- pages/fe/disruptive-innovation.md
- pages/fe/dma.md
- pages/fe/dmz-server-placement.md
- pages/fe/dns.md
- pages/fe/dns-cache-poisoning.md
- pages/fe/double-entry-bookkeeping-data-model.md
- pages/fe/dram.md
- pages/fe/draw-software.md
- pages/fe/drive-by-download.md
- pages/fe/drive-by-download-attack.md
- pages/fe/dual-duplex-system.md
- pages/fe/dynamic-address-translation.md
- pages/fe/ecc.md
- pages/fe/ecc-memory.md
- pages/fe/economic-order-quantity.md
- pages/fe/edge-computing.md
- pages/fe/edi.md
- pages/fe/effort-productivity-duration.md
- pages/fe/electric-power-energy-wh.md
- pages/fe/electronic-commerce.md
- pages/fe/electronic-signature-law.md
- pages/fe/elementary-row-operations.md
- pages/fe/email-protocols.md
- pages/fe/email-security-measures.md
- pages/fe/enterprise-architecture.md
- pages/fe/envelope-encryption.md
- pages/fe/equipment-investment-cost-effectiveness.md
- pages/fe/equivalence-partitioning-boundary-value.md
- pages/fe/er-diagram.md
- pages/fe/er-diagram-cardinality.md
- pages/fe/erp.md
- pages/fe/euclidean-algorithm.md
- pages/fe/evm.md
- pages/fe/exclusive-resource-task-timing.md
- pages/fe/external-internal-design.md
- pages/fe/extreme-programming.md
- pages/fe/fail-safe-fail-soft-fault-tolerance-foolproof.md
- pages/fe/fast-tracking.md
- pages/fe/fault-tolerant-system.md
- pages/fe/fe-requirements-definition-process.md
- pages/fe/feedback-feedforward-control.md
- pages/fe/fifo-inventory-valuation.md
- pages/fe/fifo-page-replacement.md
- pages/fe/file-block-allocation.md
- pages/fe/finite-fraction-radix.md
- pages/fe/five-functions-fetch-decode.md
- pages/fe/five-stage-pipeline.md
- pages/fe/fixed-partition-memory-allocation.md
- pages/fe/fixed-point-iteration.md
- pages/fe/flash-memory.md
- pages/fe/flip-flop-sequential-circuit.md
- pages/fe/floating-point-errors.md
- pages/fe/floating-point-format.md
- pages/fe/floating-point-normalization.md
- pages/fe/floating-point-representation.md
- pages/fe/floor-function.md
- pages/fe/full-adder.md
- pages/fe/full-differential-incremental-backup.md
- pages/fe/function-point-effort.md
- pages/fe/function-point-method.md
- pages/fe/functional-nonfunctional-requirements.md
- pages/fe/fuzzing.md
- pages/fe/gantt-chart.md
- pages/fe/gompertz-curve.md
- pages/fe/gpl-license.md
- pages/fe/gpl-mit-bsd-license-comparison.md
- pages/fe/grant-revoke-sql-privileges.md
- pages/fe/green-procurement.md
- pages/fe/green-purchasing.md
- pages/fe/grid-shortest-path-combinations.md
- pages/fe/hadoop.md
- pages/fe/hadoop-spark.md
- pages/fe/half-adder.md
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
- pages/fe/honeypot.md
- pages/fe/hot-warm-cold-site.md
- pages/fe/housing-service.md
- pages/fe/https.md
- pages/fe/huffman-coding.md
- pages/fe/hybrid-cloud.md
- pages/fe/hybrid-encryption.md
- pages/fe/hypothesis-testing.md
- pages/fe/ide-development-environment.md
- pages/fe/ide-eclipse.md
- pages/fe/ids-ips-firewall.md
- pages/fe/image-video-formats.md
- pages/fe/incident-management-vs-problem-management.md
- pages/fe/incident-service-request-management.md
- pages/fe/income-statement-profit-levels.md
- pages/fe/inheritance.md
- pages/fe/initial-running-cost.md
- pages/fe/innovation-adoption-lifecycle.md
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
- pages/fe/ipv4-address-classes.md
- pages/fe/ipv4-address-notation.md
- pages/fe/ipv4-global-private-address.md
- pages/fe/ipv4-ipv6.md
- pages/fe/ipv4-subnet-host-count.md
- pages/fe/is-a-part-of-instance-class.md
- pages/fe/isms-pdca.md
- pages/fe/it-investment-evaluation.md
- pages/fe/it-investment-management.md
- pages/fe/java-beans.md
- pages/fe/java-language-features.md
- pages/fe/java-programming-language.md
- pages/fe/java-servlet.md
- pages/fe/jdbc.md
- pages/fe/job-vs-task.md
- pages/fe/json.md
- pages/fe/kanban-jit.md
- pages/fe/kanban-system.md
- pages/fe/keylogger.md
- pages/fe/lan-analyzer.md
- pages/fe/language-processor-comparison.md
- pages/fe/least-privilege-database-access.md
- pages/fe/line-utilization-rate.md
- pages/fe/linear-programming.md
- pages/fe/linear-search.md
- pages/fe/linked-list.md
- pages/fe/linker.md
- pages/fe/lock-granularity.md
- pages/fe/logistic-curve.md
- pages/fe/long-tail.md
- pages/fe/lru.md
- pages/fe/lru-cache-replacement.md
- pages/fe/lru-page-replacement.md
- pages/fe/lte.md
- pages/fe/mac-address.md
- pages/fe/magnetic-disk-access-time.md
- pages/fe/magnetic-disk-average-wait-time.md
- pages/fe/mail-third-party-relay.md
- pages/fe/malware-criminal-law.md
- pages/fe/malware-detection-analysis.md
- pages/fe/many-to-many-associative-entity.md
- pages/fe/marketing-mix.md
- pages/fe/markov-process.md
- pages/fe/mashup.md
- pages/fe/master-file-maintenance.md
- pages/fe/memory-compaction.md
- pages/fe/memory-fragmentation.md
- pages/fe/memory-hierarchy.md
- pages/fe/memory-management-methods.md
- pages/fe/memory-types.md
- pages/fe/message-authentication-code.md
- pages/fe/microkernel.md
- pages/fe/middleware.md
- pages/fe/migration-test.md
- pages/fe/mime.md
- pages/fe/mips.md
- pages/fe/mips-processing-time.md
- pages/fe/module-cohesion.md
- pages/fe/module-coupling.md
- pages/fe/monte-carlo-method.md
- pages/fe/morphing.md
- pages/fe/mpeg.md
- pages/fe/mrp.md
- pages/fe/mtbf.md
- pages/fe/mtbf-mttr.md
- pages/fe/multicore-processor.md
- pages/fe/multiprocessor-system-types.md
- pages/fe/nand-gate.md
- pages/fe/nand-xor-circuit.md
- pages/fe/nas.md
- pages/fe/nat.md
- pages/fe/nat-napt.md
- pages/fe/necessary-and-sufficient-condition.md
- pages/fe/net-present-value.md
- pages/fe/network-configuration-management.md
- pages/fe/network-device-functions-comparison.md
- pages/fe/network-devices-router-repeater-bridge-switch.md
- pages/fe/network-diagnostic-commands.md
- pages/fe/newton-method.md
- pages/fe/niche-strategy.md
- pages/fe/non-functional-requirements.md
- pages/fe/normal-distribution-table.md
- pages/fe/nosql-data-models.md
- pages/fe/ntp.md
- pages/fe/ntp-time-synchronization.md
- pages/fe/on-demand-service.md
- pages/fe/open-innovation.md
- pages/fe/open-redirect.md
- pages/fe/operational-testing.md
- pages/fe/operations-involvement-system-development.md
- pages/fe/order-quantity-and-inventory-cost.md
- pages/fe/os-api.md
- pages/fe/osi-reference-model.md
- pages/fe/ot-dmz.md
- pages/fe/otoo.md
- pages/fe/overall-optimization-business-model.md
- pages/fe/overlay-paging-swapping.md
- pages/fe/packet-filtering.md
- pages/fe/packet-filtering-port-rules.md
- pages/fe/packet-switching.md
- pages/fe/page-printer.md
- pages/fe/paging.md
- pages/fe/parity-check.md
- pages/fe/parity-circuit.md
- pages/fe/password-hash-authentication.md
- pages/fe/password-list-attack-comparison.md
- pages/fe/pcm-sampling-quantization-encoding.md
- pages/fe/pdm-dependency-types.md
- pages/fe/permutations-combinations.md
- pages/fe/phishing.md
- pages/fe/physical-security-measures-comparison.md
- pages/fe/ping.md
- pages/fe/pipe.md
- pages/fe/pipeline-control.md
- pages/fe/pki-certificate-authority.md
- pages/fe/planning-process.md
- pages/fe/pll-frequency-divider.md
- pages/fe/polymorphism.md
- pages/fe/pop3-smtp-imap.md
- pages/fe/power-gating.md
- pages/fe/ppm.md
- pages/fe/pppoe.md
- pages/fe/preemptive-scheduling.md
- pages/fe/preventive-detective-controls.md
- pages/fe/primary-key.md
- pages/fe/privacy-by-design.md
- pages/fe/problem-management.md
- pages/fe/process-innovation.md
- pages/fe/product-life-cycle.md
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
- pages/fe/proxy-server.md
- pages/fe/pseudocode-reading-guide.md
- pages/fe/public-key-cryptography.md
- pages/fe/public-key-encryption-digital-signature.md
- pages/fe/python-indentation-code-blocks.md
- pages/fe/qr-code.md
- pages/fe/qr-code-barcode.md
- pages/fe/queue.md
- pages/fe/radius.md
- pages/fe/raid-levels.md
- pages/fe/rasis.md
- pages/fe/raster-vector-graphics.md
- pages/fe/real-time-system.md
- pages/fe/recursion.md
- pages/fe/recursion-trace.md
- pages/fe/recursive-factorial.md
- pages/fe/recursive-function.md
- pages/fe/reentrant-program.md
- pages/fe/refactoring.md
- pages/fe/referential-integrity.md
- pages/fe/regression-testing.md
- pages/fe/relational-model.md
- pages/fe/relational-operations.md
- pages/fe/relations-diagram.md
- pages/fe/relocation.md
- pages/fe/required-bits.md
- pages/fe/rest-api.md
- pages/fe/retention-rate.md
- pages/fe/reverse-brute-force.md
- pages/fe/reverse-polish-notation.md
- pages/fe/risc-cisc.md
- pages/fe/risk-assessment-process.md
- pages/fe/risk-level.md
- pages/fe/roi.md
- pages/fe/rollback-rollforward.md
- pages/fe/rom-types.md
- pages/fe/rootkit.md
- pages/fe/round-robin-scheduling.md
- pages/fe/router-bridge-repeater-gateway.md
- pages/fe/rpa.md
- pages/fe/rpc.md
- pages/fe/run-length-encoding.md
- pages/fe/saas-paas-iaas.md
- pages/fe/scale-up-vs-scale-out.md
- pages/fe/scm.md
- pages/fe/scrum-events.md
- pages/fe/scrum-roles.md
- pages/fe/sd-sdhc-sdxc-sduc.md
- pages/fe/secure-boot.md
- pages/fe/security-by-design.md
- pages/fe/security-cia.md
- pages/fe/security-guidelines-comparison.md
- pages/fe/security-threat-countermeasures.md
- pages/fe/seo-poisoning.md
- pages/fe/series-parallel-system-availability.md
- pages/fe/server-client-port.md
- pages/fe/server-room-physical-security.md
- pages/fe/service-availability.md
- pages/fe/session-id-invalidation.md
- pages/fe/sfa.md
- pages/fe/sgml.md
- pages/fe/shared-exclusive-lock.md
- pages/fe/shell.md
- pages/fe/shell-redirection.md
- pages/fe/shift-operation.md
- pages/fe/shift-register-timing.md
- pages/fe/shortest-job-first-scheduling.md
- pages/fe/siem.md
- pages/fe/snmp.md
- pages/fe/soa.md
- pages/fe/soap-wsdl-uddi.md
- pages/fe/soc.md
- pages/fe/software-architecture-design.md
- pages/fe/software-design-phases.md
- pages/fe/software-license-contract-types.md
- pages/fe/software-license-minimum-cost.md
- pages/fe/software-quality-characteristics.md
- pages/fe/software-repository.md
- pages/fe/software-reuse.md
- pages/fe/software-review-inspection.md
- pages/fe/software-testing-types.md
- pages/fe/sorting-algorithms.md
- pages/fe/speculative-execution.md
- pages/fe/spf.md
- pages/fe/spiral-model.md
- pages/fe/spooling.md
- pages/fe/spyware.md
- pages/fe/sql-aggregate-functions.md
- pages/fe/sql-correlated-subquery.md
- pages/fe/sql-cursor.md
- pages/fe/sql-group-by-aggregate-functions.md
- pages/fe/sql-group-by-order-by.md
- pages/fe/sql-injection.md
- pages/fe/sql-logical-operators.md
- pages/fe/sql-optimizer.md
- pages/fe/sram.md
- pages/fe/sram-dram.md
- pages/fe/ssid-bssid.md
- pages/fe/stack.md
- pages/fe/stack-vs-queue.md
- pages/fe/standard-deviation.md
- pages/fe/standby-system.md
- pages/fe/state-transition-diagram.md
- pages/fe/state-transition-table.md
- pages/fe/static-dynamic-linking.md
- pages/fe/storage-media-read-write-methods.md
- pages/fe/stored-procedure.md
- pages/fe/stored-program-architecture.md
- pages/fe/stored-program-concept.md
- pages/fe/streaming-buffering.md
- pages/fe/structured-unstructured-data.md
- pages/fe/stub-driver.md
- pages/fe/subnet-host-address.md
- pages/fe/supply-chain-management.md
- pages/fe/swot-analysis.md
- pages/fe/system-audit.md
- pages/fe/system-audit-regulations.md
- pages/fe/system-audit-techniques.md
- pages/fe/system-auditor-independence.md
- pages/fe/system-development-quality-management.md
- pages/fe/system-failure-monitoring.md
- pages/fe/system-performance-evaluation.md
- pages/fe/system-test-audit.md
- pages/fe/tamper-resistance.md
- pages/fe/targeted-attack-email.md
- pages/fe/task-dispatch_revised.md
- pages/fe/task-scheduling.md
- pages/fe/tcp-connection-identification.md
- pages/fe/tcp-ip-layers.md
- pages/fe/tcp-udp-port-number.md
- pages/fe/technology-s-curve.md
- pages/fe/test-support-tools.md
- pages/fe/tethering.md
- pages/fe/thrashing.md
- pages/fe/three-tier-client-server.md
- pages/fe/throughput.md
- pages/fe/throughput-spooling.md
- pages/fe/timestamp-service.md
- pages/fe/tlo.md
- pages/fe/tlo-technology-licensing-organization.md
- pages/fe/top-down-bottom-up-test.md
- pages/fe/top-down-testing.md
- pages/fe/touch-panel.md
- pages/fe/transaction-1.md
- pages/fe/transaction-atomicity-rollback.md
- pages/fe/transaction-state-transition.md
- pages/fe/transition-probability.md
- pages/fe/turnaround-time.md
- pages/fe/two-phase-commit.md
- pages/fe/twos-complement.md
- pages/fe/twos-complement-remainder.md
- pages/fe/uml-multiplicity.md
- pages/fe/unauthorized-access-law.md
- pages/fe/ups.md
- pages/fe/usb.md
- pages/fe/usb-ieee1394.md
- pages/fe/usb-interface.md
- pages/fe/value-chain.md
- pages/fe/variable-partition-memory-allocation.md
- pages/fe/venn-diagram-set-operations.md
- pages/fe/verification-validation.md
- pages/fe/video-bandwidth-calculation.md
- pages/fe/virtual-memory.md
- pages/fe/virus-detection-methods.md
- pages/fe/voip-gatekeeper.md
- pages/fe/waf.md
- pages/fe/wake-on-lan.md
- pages/fe/walkthrough-review.md
- pages/fe/waterfall-defect-correction-cost.md
- pages/fe/waterfall-model.md
- pages/fe/wbs.md
- pages/fe/web-api.md
- pages/fe/web-application-server.md
- pages/fe/web-beacon.md
- pages/fe/web-client-server.md
- pages/fe/weighted-average-inventory-valuation.md
- pages/fe/white-box-test-coverage.md
- pages/fe/white-box-testing.md
- pages/fe/wireless-lan-channel-interference.md
- pages/fe/wireless-lan-security.md
- pages/fe/work-made-for-hire.md
- pages/fe/work-made-for-hire-copyright.md
- pages/fe/xml-digital-signature.md
- pages/fe/xml-dtd.md
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

## 継続監査：開発・テスト・品質管理の未確認30記事（2026-10-17）

履歴422ファイルに含まれない30ファイルを追加しました。定義・冒頭・見出し・科目A/Bの判断軸を比較し、統合対象2記事は本文全体を照合しています。全記事間の総当たり比較や全文校正の完了率ではありません。

| 記事群 | 判定・理由 |
|---|---|
| `development-operations-collaboration` / `operations-involvement-system-development` | **統合**。要件定義からの運用参加・運用テスト・引継ぎという学習目的が同じ。初回日付が早く設備設計のたとえを持つ後者を維持。前者の運用要件表、クラウド移行の例、DevOpsとの違いを移植。旧URLをHTML転送し、既存別名は正規記事へ直接転送する設定を維持 |
| `black-box-vs-white-box-testing` / `white-box-test-coverage` / `branch-coverage` | 維持。テスト設計根拠の比較とPython例／5種類の網羅基準・最小ケース数／判定式全体の真偽とPython例。既存のブラック・ホワイト個別記事とも区別 |
| `equivalence-partitioning-boundary-value` / `assertion-check` / `fuzzing` / `test-support-tools` | 維持。代表値・境界の選び方／実行時に成立すべき条件／多様な入力による異常探索／静的・動的・環境設定のツール分類。既存のリンクも確認 |
| `software-review-inspection` / `walkthrough-review` | 維持。4つのレビュー技法の比較／作成者を含むレビューの進め方・早期発見。双方の役割説明とリンクが既にある |
| `bug-management-chart` / `bug-seeding` / 既存確認済み`gompertz-curve` | 維持。複数曲線の収束と停滞の判定／既知バグ検出率による残存数の計算／累積バグのS字モデルは異なる |
| `defect-repair-cost-expected-value` / `waterfall-defect-correction-cost` | 維持。不良率・発見率・対象割合・単価で費用を計算／上流誤りが後続成果物に及ぼす手戻りの比較。費用という語だけで統合しない |
| `software-testing-types` / `migration-test` / 既存確認済みの回帰・運用テスト | 維持。工程・目的によるテスト全体の分類／切替手順・時間・切戻しのリハーサル／修正後の悪影響／実運用の確認を分担 |
| `application-maintenance` / `master-file-maintenance` | 維持。修正・テスト・承認・本番反映・記録／データの重複・内容・参照関係の整備。「保守」の対象が異なる |
| `module-cohesion` / `module-coupling` | 維持。モジュール内部のまとまり／モジュール間の依存。種類と望ましい強弱も異なる |
| `external-internal-design` / `verification-validation` / 既存確認済み設計工程・共通フレーム支援記事 | 維持。設計成果物の分類／仕様適合と利用目的適合／工程の全体像／支援プロセス群は別の学習目的 |
| `extreme-programming` / `refactoring` / `software-reuse` | 維持。XPのプラクティス比較／外部動作を保った内部改善／再利用部品を作る工数と使う工数の違い |
| `case-tools` / `software-repository` / `cmmi` / `software-quality-characteristics` | 維持。開発支援工程／成果物一元管理／プロセス成熟度／製品品質の評価軸。既存確認済みの構成管理・品質管理とも区別 |

- SG・DS・GKも関連語で検索し、他テーマとの統合は行わない。出典の鮮度・規格変更・全面的な内容校正は別監査。
- 統合先の`date`・`permalink`・分類・見出し・フッターを維持し更新日を変更。既存別名`/fe/development-to-operations-transition/`を統合先の`redirect_from`へ移し、多段転送を避ける。
- 図解評価：設備設計のたとえ・工程フロー・運用要件表で目的を説明できるため、新たな操作UIは追加しない。
- main（`f7dde4d7`、#445まで）：401/751実記事（53.4%）。今回適用後：778 Markdown・転送28・実記事750、確認履歴452ファイル（転送22・実記事430）。**430/750実記事（57.3%）**、未確認320実記事。

## 継続監査：ネットワーク・セキュリティの未確認30記事（2026-10-17）

履歴452ファイルに含まれない30ファイルを追加確認しました。定義・冒頭・見出し・試験の判断基準を比較し、統合対象2記事は本文全体を照合しています。全段落の校正・全記事間の総当たり比較の完了率ではありません。

| 記事群 | 判定・理由 |
|---|---|
| `cpsf` / `cyber-physical-security-framework` | **統合**。目的、産業社会・サプライチェーン、3層のつながり、個別ガイドラインとの区別が同じ。初回日付が早く、設備停止・安全への影響と各層の実例を持つ正式名称側を維持。略称側の学習内容は統合先に含まれている。旧URLをHTML転送し、正式名称側からガイドライン比較へ誘導 |
| `ipv4-address-notation` / `ipv4-address-classes` / `ipv4-global-private-address` / `ipv4-ipv6` | 維持。8ビット区切りの表記／旧来のクラス境界／私用・特殊用途の範囲／IPv6との長さ・表記・機能比較で判断が異なる |
| `ipv4-subnet-host-count` / 既存確認済みCIDR・ホストアドレス記事 | 維持。プレフィックスから使用可能数を計算／ネットワークとブロードキャストの番地算出／個々の番地の割当可否を分担 |
| `osi-reference-model` / `tcp-ip-layers` | 維持。OSI7層の機能判断／TCP/IP4層・プロトコルとフレーム内情報の対応。既存の相互リンクと役割説明を確認 |
| `csma-ca` / `csma-cd` | 維持。無線LANでの衝突回避・ACK／共有型Ethernetの衝突検出・再送・混雑を分担。既存相互リンクを確認 |
| `ssid-bssid` / `wireless-lan-channel-interference` / `wireless-lan-security` | 維持。ネットワーク・APの識別／2.4GHz帯の干渉とチャネル配置／暗号化・接続制限・端末間分離という目的が異なる |
| `adsl` / `atm` / `packet-switching` | 維持。電話線の周波数分離と非対称通信／53バイトの固定長セル／分割転送と回線共有。ATMとパケット交換は関連するが個別方式の判断が異なる |
| `bluetooth` / `lte` / `tethering` | 維持。近距離の無線規格／携帯電話網の移動通信システム／モバイル回線を別端末へ共有する機能。通信方式と機能を混同しない |
| `dns-cache-poisoning` / `seo-poisoning` / `open-redirect` / `phishing` | 維持。名前解決情報／検索順位／Web転送機能の悪用／利用者をだまして情報入力させる攻撃を分担。誘導という結果だけで統合しない |
| `password-list-attack-comparison` / 既存確認済み総当たり・リバース総当たり記事 | 維持。流出した組合せ・候補語・固定する項目・ハッシュ解析の横断比較／全候補による探索／パスワード固定での試行という役割差 |
| `proxy-server` / `radius` / `https` / `voip-gatekeeper` / `wake-on-lan` | 維持。代理接続と2本のTCP接続／ネットワーク利用者の認証／HTTP通信のTLS保護／H.323の番号とIP対応／LAN経由の起動。既存確認済みDNS・NAT・PKI・WAFとの違いも照合 |

- SG・DS・GKの関連語も検索し、他テーマとの統合は行わない。規格・ガイドラインの最新性と全面的な内容校正は別監査。
- 正規記事の初回`date`・`permalink`・分類・主要見出し・フッター・出典・工場の具体例は保持。略称記事の内容に独自の計算問題や操作図解はなく、重複する工程図は追加しない。
- 図解評価：正規記事のセンサー→分析→制御と各層の具体例で目的を説明できるため、新たな操作UIは不要。
- main（`86cca6a8`、#446まで）：430/750実記事（57.3%）。今回適用後：778 Markdown・転送29・実記事749、確認履歴482ファイル（転送23・実記事459）。**459/749実記事（61.3%）**、未確認290実記事。

## 継続監査：経営戦略・業務・マーケティングの未確認30記事（2026-10-17）

履歴482ファイルに含まれない30実記事の定義・冒頭・見出し・試験の判断基準を比較しました。新たな統合対象はありません。以下は学習目的・判断軸の確認履歴であり、全記事間の総当たり比較や全段落の校正の完了率ではありません。

| 記事群 | 判定・理由 |
|---|---|
| `ansoff-growth-matrix` / `ppm` / `swot-analysis` / `customer-portfolio-analysis` | 維持。製品・市場の既存／新規／市場成長率・相対シェア／内部・外部のプラス・マイナス／顧客購買規模・自社取引額。2軸表という形式が共通でも、対象と判断が異なる |
| `product-life-cycle` / `technology-s-curve` / `innovation-adoption-lifecycle` | 維持。製品の売上段階／技術投入に対する性能進歩／採用者の時期・態度。既存確認済みロジスティック曲線とも同一視しない |
| `disruptive-innovation` / `open-innovation` / `blue-ocean-strategy` | 維持。既存企業が重視しない市場からの置換／社外知識の活用／新しい価値と市場の創出。「新しい事業」だけで統合しない |
| `niche-strategy` / `competitive-position-strategy` | 役割を明示して維持。特定市場への集中の詳説／4つの競争地位の比較。冒頭に読み分けの説明と相互リンクを追加 |
| `commoditization` / `core-technology` / 既存確認済み`core-competence` | 維持。差別化困難になる市場状態／競争優位を生む独自技術／技術に限定しない組織の中核能力。状態・技術・能力が異なる |
| `value-chain` / `overall-optimization-business-model` / 既存確認済み業務モデル・SCM | 維持。企業の主活動・支援活動による価値分析／業務と情報のあるべき姿／現新・論理物理の分類／企業間供給連鎖の最適化を分担 |
| `bpm` / `bi` / `rpa` / 既存確認済みBPR・業務改善手順 | 維持。継続的な業務プロセス管理／データ分析による意思決定支援／定型PC業務の自動化／抜本的な再設計／改善活動の工程順は異なる。BIの既存操作図解を保持 |
| `marketing-mix` / `behavioral-targeting` / `long-tail` | 維持。4P・4Cの施策の組合せ／広告表示の基準となる行動履歴／非売れ筋商品の合計売上。マーケティングという分野が共通するだけ |
| `conversion-rate` / `retention-rate` | 維持。訪問から成果への割合／期首顧客の継続割合。母集団・対象期間・新規会員の除外という計算が異なる |
| `sfa` / `erp` / `mrp` | 維持。営業活動・商談／全社経営資源の統合／生産計画から部品所要量と発注時期の算出。既存のERP・SFA相互リンクも確認 |
| `3pl` / `electronic-commerce` / `otoo` | 維持。物流企画を含む包括受託／売り手・買い手による電子商取引の分類／オンラインから実店舗への誘導。SCMと3PLも全体最適と受託形態の違いがある |

- SG・DS・GKも関連語で検索し、他テーマとの統合はしない。原典・規格の鮮度と全面的な内容校正は別監査。
- 編集はニッチ戦略と競争地位別戦略の2記事のみ。元の初回日付・URL・分類・見出し・フッターを保持し、更新日を変更。
- 既存の軸表・例・図解を保持し、学習導線だけの追加には新たな操作UIを設けない。
- main（`aaf0fa59`、#447まで）：459/749実記事（61.3%）。今回適用後：778 Markdown・転送29・実記事749、確認履歴512ファイル（転送23・実記事489）。**489/749実記事（65.3%）**、未確認260実記事。

## 継続監査：セキュリティ対策・認証・関連法務の未確認30記事（2026-10-17）

履歴512ファイルに含まれない30実記事を、定義・冒頭・見出し・試験判断基準で比較しました。重なりが強い検知・メール対策は仕組みの説明部分も照合しています。今回新たな統合対象はありません。全段落校正・法改正確認・全記事間総当たり比較の完了率ではありません。

| 記事群 | 判定・理由 |
|---|---|
| `malware-detection-analysis` / `virus-detection-methods` | 役割を明示して維持。検知・逆アセンブル・ハッシュによる識別の切り分け／パターン・ビヘイビア・コンペア・チェックサムの検出方式比較。両記事に目的説明と相互リンクを追加 |
| `keylogger` / `spyware` / `rootkit` | 維持。キー入力の記録／秘密裏の情報収集／侵入後の痕跡隠蔽・居座り。結果が情報漏えいでも手口・役割が違う |
| `honeypot` / `captcha` / `byod` | 維持。攻撃観察用のおとり／人間とbotの判別／私物端末の業務利用。認証や監視という語だけで統合しない |
| `secure-boot` / `tamper-resistance` / `session-id-invalidation` | 維持。起動時の署名確認／物理解析への耐性／ログアウト時のサーバ側セッション失効。保護する対象・時点が違う |
| `sql-injection` / `privacy-by-design` / 既存確認済み`security-by-design` | 維持。入力がSQLとして解釈される攻撃と対策／設計段階でのプライバシー保護／設計段階でのセキュリティという個別攻撃・保護対象の差がある |
| `email-security-measures` / `spf` / `mail-third-party-relay` / `mime` | 維持。対策の目的別比較／DNS情報と接続元IPの照合／接続元・送信者・受信者の判定／データ形式・添付を表す仕組み。総論からSPFと第三者中継の詳説へリンクを追加 |
| `targeted-attack-email` / 既存確認済みフィッシング | 維持。特定の相手に合わせた業務文面／偽装による情報入力の誘導。対象選定と目的・手段の切り口が異なる |
| `digital-watermark` / `xml-digital-signature` / `timestamp-service` / `electronic-signature-law` | 維持。コンテンツ内の識別情報／XML部分署名と形式／存在・非改ざんの時点／法律上の電子署名・認証業務制度。既存の公開鍵・PKI記事とも役割が異なる |
| `authenticity-reliability-security` / `preventive-detective-controls` / `isms-pdca` | 維持。情報の特性／問題発生を防ぐか発見するか／管理サイクルの段階。既存CIA・内部統制記事とも分類軸が違う |
| `cybercrime-laws` / `malware-criminal-law` / `unauthorized-access-law` | 維持。行為別の法律横断比較／不正指令電磁的記録の目的・理由の判断／識別符号利用・アクセス制御回避。法律総論と個別行為の詳説を分担 |
| `computer-unauthorized-access-countermeasure-standard` / `cybersecurity-management-guideline` | 維持。ID・最小権限・接続・方針・教育の基準／経営者の体制・資源・サプライチェーン責任。禁止行為を扱う法律とも区別 |

- SG・DS・GKも関連語検索を行い、他テーマとの統合はしない。法律・規格・製品挙動の最新性は今回検証していないため、正確性・鮮度監査の完了とは扱わない。
- 編集は検知・解析の2記事とメール総論の計3記事のみ。既存の本文・例・初回日付・URL・分類・見出し・フッターは保持し、更新日と目的説明・リンクだけ変更。
- 図解評価：今回は既存教材への読み分けを補う変更のため、新たな操作UIは追加しない。
- main（`46e26fca`、#448まで）：489/749実記事（65.3%）。今回適用後：778 Markdown・転送29・実記事749、確認履歴542ファイル（転送23・実記事519）。**519/749実記事（69.3%）**、未確認230実記事。

## 継続監査：アルゴリズム・数値表現・確率統計の未確認32記事（2026-10-18）

mainの#449反映と履歴542ファイルを確認してから、未登録32実記事を追加しました。定義・冒頭・見出し・試験の判断軸を比較し、マルコフ過程と遷移確率は本文全体、数え上げとビット数の記事群は計算の対象も照合しています。今回新たな統合対象はありません。全段落の校正・全記事間の総当たり比較の完了率ではありません。

| 記事群 | 判定・理由 |
|---|---|
| `binary-decimal-digit-count` / `bit-pattern-count` / `required-bits` | 維持。基数を変えた桁数の概算／既知ビット数から個数・倍率／種類数から最小ビット数という順逆の計算。必要ビット数からパターン数へのリンクを追加し、既存の逆方向リンクと対応 |
| `decimal-to-binary-div-mod` / `shift-operation` / `finite-fraction-radix` | 維持。整数変換のmod保存・div更新／ビット移動と倍率・マスク／分母の素因数から有限小数になるかの判断。既存確認済み16進変換・浮動小数点誤差とも区別 |
| `permutations-combinations` / `communication-paths-combination` / `grid-shortest-path-combinations` / `counting-constrained-strings` | 維持。順番の有無・余事象の総論／1対1のペアと増員差分／右上移動の並べ方／各位置の制約と重複許容。公式が共通でも制約の読み方が違う |
| `conditional-probability` / `bayes-theorem` / `transition-probability` / `markov-process` | 維持。条件から分母を選ぶ／観測後の逆向き確率／条件を固定した確率表と合計1／複数ステップの経路確率。遷移確率とマルコフ過程へ相互リンクを追加 |
| `standard-deviation` / `normal-distribution-table` / `correlation-coefficient` / `hypothesis-testing` | 維持。散らばりと定数変換／z標準化・左右の面積／2変数の直線関係／p値と有意水準から棄却判断で対象が異なる |
| `fixed-point-iteration` / `newton-method` / `monte-carlo-method` | 維持。反復で変わらない値の条件／接線を使う方程式の求根／乱数の繰返しによる近似。反復という語だけでは統合しない |
| `elementary-row-operations` / `linear-programming` | 維持。行列の操作判定／線形制約の下で頂点を比較する最適化で目的が違う |
| `adjacency-matrix` / `dfs-vs-bfs` / `linear-search` / `sorting-algorithms` | 維持。グラフの接続表現／探索順とスタック・キュー／先頭から値を探す／比較交換による整列。既存の二分探索・木走査記事とも区別。既存のソート操作図解を保持 |
| `euclidean-algorithm` / `call-by-value` | 維持。最大公約数計算の変数更新・終了判定／引数のコピーと仮引数への代入効果。トレース対象・目的が異なる。既存の値呼出し操作図解を保持 |
| `necessary-and-sufficient-condition` / `venn-diagram-set-operations` | 維持。含意の向きと反例／集合の領域・等式・包含の判定。既存確認済み論理演算記事とも対象が違う |

- SG・DS・GKも関連語で検索し、他テーマとの統合は行わない。全面的な数式校正・実装検証・出典の鮮度は別監査。
- 公開記事の編集はマルコフ過程・遷移確率・必要ビット数の3件のみ。元のdate・URL・分類・見出し・計算例・フッターを保持し、更新日・役割説明・リンクだけ変更。
- 図解評価：今回は既存教材の読み分けの補足で、新しい操作UIは不要。既存の操作図解・例は保持。
- main（`c27cd649`、#449まで）：519/749実記事（69.3%）。今回適用後：778 Markdown・転送29・実記事749、確認履歴574ファイル（転送23・実記事551）。**551/749実記事（73.6%）**、未確認198実記事。

## 継続監査：DB・Web・データ形式の未確認32記事（2026-10-18）

mainの#450反映と履歴574ファイルを確認し、未登録32実記事を追加しました。定義・冒頭・見出し・試験判断軸を比較し、SQL集計・簿記データモデルは仕組みと例の対象も照合しました。新たな統合対象はありません。全段落校正や全記事間の総当たり比較の完了率ではありません。

| 記事群 | 判定・理由 |
|---|---|
| `data-dictionary` / `database-administrator` / 既存確認済みスキーマ | 維持。定義情報を管理する辞書／DBを安定稼働させる役割／データ構造の定義と3層スキーマ。情報・担当者・構造という対象が異なる |
| `database-performance-troubleshooting` / `sql-optimizer` / 既存確認済みインデックス | 維持。遅い原因と調査項目の対応／アクセス経路・実行計画の選択／検索高速化のデータ構造。原因調査とDBMS機能を区別 |
| `database-view-select-privilege` / `grant-revoke-sql-privileges` / `least-privilege-database-access` | 維持。ビューの定義・権限・更新可能性／権限付与と取消のSQL／処理に必要な最小権限の選択 |
| `nosql-data-models` / `json` / `xml-dtd` / `sgml` | 維持。DBのデータモデル／データ交換形式／XML文書構造の定義／文書記述の規格。XML・JSONを扱うという理由だけで統合しない |
| `stored-procedure` / `sql-cursor` / `sql-correlated-subquery` / `sql-logical-operators` | 維持。DBMS側の処理保存と呼出し／結果の1行ずつ処理／外側の行を参照し0件も考える条件／WHEREの論理条件。操作と判定対象が違う |
| `sql-group-by-order-by` / 既存確認済み集計関数・GROUP BY詳説 | 維持。集計単位と表示順の比較／COUNT等とNULL・WHERE／WHERE・HAVINGとグループ集計。比較記事から絞り込みの詳説へリンクを追加 |
| `debit-credit-double-entry` / `double-entry-bookkeeping-data-model` | 維持。勘定科目の増減と借方貸方の基本／取引・勘定・移動の3表を対応付ける応用。冒頭に役割説明と相互リンクを追加 |
| `java-servlet` / `java-beans` / `jdbc` / `web-application-server` | 維持。サーバ側で要求処理するJavaプログラム／再利用部品の仕様／JavaからDBへのAPI／Web・APの役割分離。既存確認済みJava・3層クライアントサーバとも役割が異なる |
| `ajax` / `cgi` / `web-beacon` / `absolute-relative-path` | 維持。非同期で画面の一部を更新／Webサーバと外部プログラムの接続／画像読込みで閲覧を計測／基準位置からファイルをたどる指定。Webに関連しても目的が違う |
| `rpc` / `corba` / `soa` / `soap-wsdl-uddi` / `mashup` | 維持。別コンピュータの手続呼出し／分散オブジェクト連携の仕様／サービスを組み合わせる設計思想／交換・記述・検索の役割／公開API等の組合せによる新サービス。既存Web API・REST記事とも比較 |
| `edi` / 既存確認済み電子商取引 | 維持。企業間取引データと4種類の規約／電子的な商取引と当事者分類。情報交換の約束と商取引自体を区別 |

- SG・DS・GKも関連語で検索し、他テーマとの統合はしない。DBMS・言語・規格の現行仕様検証、全面的なSQL実行確認は別監査。
- 公開記事の編集は借方貸方・会計データモデル・GROUP BYとORDER BYの3件。元のdate・URL・分類・見出し・計算例・フッターを保持し、更新日・目的説明・リンクだけ変更。
- 図解評価：今回は既存教材間の読み分けで、新たな操作UIは不要。既存のSQL・表・例は保持。
- main（`004b9b22`、#450まで）：551/749実記事（73.6%）。今回適用後：778 Markdown・転送29・実記事749、確認履歴606ファイル（転送23・実記事583）。**583/749実記事（77.8%）**、未確認166実記事。

## 継続監査：回路・ハードウェア・システム構成の未確認32記事（2026-10-18）

PR #451がmainへマージ済みであることを確認して継続。未登録32記事の結論・見出し・比較対象となる説明を、既存の仮想記憶・ページング・スループット・耐故障性・USB等の記事と照合しました。全本文の逐語比較や全組合せの比較を完了したという意味ではありません。

| 対象記事 | 判定と理由 |
|---|---|
| actuator / chattering | 維持。制御信号を物理動作へ変える装置と、接点の振動による多重入力という現象で異なる。 |
| address-bus-data-bus / dma / daisy-chain | 維持。場所指定とデータ幅、転送の制御主体、機器の接続形態で判断軸が異なる。USBの記事は規格の共通機能を扱う。 |
| archive / file-block-allocation | 維持。ファイルをまとめる操作と、ファイルごとの割当領域の切上げ計算で異なる。バックアップや主記憶の断片化の説明とも目的が異なる。 |
| augmented-reality | 維持。現実への情報の重畳をVR等と区別する教材。CGの描画工程とは役割が異なる。 |
| buffer-size-transfer-rate / streaming-buffering | 維持・相互リンク。速度差を使う点は共通だが、前者は入力超過によるあふれを防ぐ容量、後者は出力超過による不足を防ぐ再生開始待ち時間を扱う。後者の「50秒分のデータ」を待ち時間50秒・蓄積量300kバイトと明確化。 |
| dc-power-feeding / electric-power-energy-wh / power-gating / ups | 維持。変換損失、電力・電力量の計算、回路への電源遮断、停電直後の一時給電という役割で異なる。 |
| dual-duplex-system / multiprocessor-system-types | 維持・相互リンク。二重化の動作・切替えの詳細と、主記憶・OS共有も含めた構成の横断比較で読み分けを明示。旧dual-vs-duplex-systemは既存の転送を維持。 |
| fail-safe-fail-soft-fault-tolerance-foolproof | 維持。故障・誤操作への対応目的を横断比較する教材。fault-tolerant-systemは必要機能の継続と実現手段・復旧との違いを詳しく扱う。 |
| dynamic-address-translation / thrashing | 維持。実行時のアドレス変換と、ページ交換多発による性能低下。virtual-memoryは全体像、pagingは管理単位と対応付けを扱う。 |
| edge-computing / real-time-system | 維持。処理を行う場所と、期限内に完了するという要件で異なる。エッジであることだけでは期限保証にならない。 |
| flip-flop-sequential-circuit / shift-register-timing | 維持。1ビットの状態保持と、クロック・ストローブに沿ったビット列の変化の追跡で異なる。 |
| full-adder / half-adder | 維持。下位桁からの桁上がりを含む加算と、AND・XORによる2入力の加算を扱う。共通の真理値表という形式だけでは統合しない。 |
| nand-gate / nand-xor-circuit | 維持。単一ゲートの定義・万能性と、途中出力を追って複合回路全体の機能を判定する手順で異なる。 |
| nas | 維持。ネットワーク経由のファイル共有をSAN・DASと比較する教材。RAIDはディスク構成、バックアップは復旧用の保存で異なる。 |
| pll-frequency-divider | 維持。ブロック図上の逓倍・分周の計算。CPU性能・クロックの一般説明とは問題の判断手順が異なる。 |
| scale-up-vs-scale-out / system-performance-evaluation / turnaround-time | 維持。性能向上の構成変更、測定条件の選び方、到着から完了までの時間計算で異なる。スループットやスケジューリングは関連するが同一教材ではない。 |

- 新たな統合はなし。転送29件・実記事749件は維持。
- 確認履歴は583/749件から**615/749件（82.1%）**へ。未確認の実記事は134件。
- 現存ファイルの確認履歴インデックスは638件（実記事615件＋履歴に含まれる転送23件）。
- 元の公開日・URL・分類・既存見出し・フッターを保持。記事変更4件の更新日を更新。
- 検証：監査スクリプトの単体テスト5件成功。通常16候補・拡張43候補を再抽出し、git diff --checkを通過。ローカルのJekyll環境がないため公開表示のビルドは未確認。

## 転送専用ページの確認（2026-10-17）

初回は1100バイト未満から17件を抽出しました。その後、**全778件の本文**を自動走査し、`layout: null` とHTMLのmeta refreshの両方を満たす17件を検出しました。

- 確認済み転送専用ページ: 29件（#447で反映済み。今回の新規転送なし）
- 今回の継続PR適用後の実記事数: 749件（778 - 29）。HTML meta refresh以外の転送方式は判定対象外
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

- pages/fe/development-operations-collaboration.md

- pages/fe/cpsf.md

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
