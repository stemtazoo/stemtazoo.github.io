# FE記事の重複監査ログ

ファイル名の一覧取得と本文監査の完了は別です。

## 対象と進捗

- GitHub mainの再帰ツリーを2026-10-17に取得
- FE Markdown: 778ファイル（転送用ページを含む）
- 過去の本文確認履歴に対応する現存ファイル: 94ファイル（重複排除）
- ファイル単位の確認履歴カバー率: 12.1%。これは全件本文比較の完了率ではありません。
- 削除済みファイルは分母・分子から除外。転送ページのうち17ファイルを本文で確認済み。全件分類は未完了です。

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

## 本文確認履歴に含まれる現存ファイル

以下は確認履歴のインデックスです。記載だけで重複なし・公開確認済みとは判断しません。

- pages/fe/audit-evidence.md
- pages/fe/audit-working-papers.md
- pages/fe/authentication-devices.md
- pages/fe/backup-methods.md
- pages/fe/backup-redundancy.md
- pages/fe/biometric-authentication.md
- pages/fe/business-continuity-management.md
- pages/fe/business-continuity-plan.md
- pages/fe/capacity-management-analysis-methods.md
- pages/fe/capacity-management-analysis-models.md
- pages/fe/certificate-authority.md
- pages/fe/challenge-response-authentication.md
- pages/fe/cia-triad.md
- pages/fe/configuration-management.md
- pages/fe/contract-types-outsourcing.md
- pages/fe/cryptographic-algorithm-types.md
- pages/fe/database-backup-recovery.md
- pages/fe/database-log-recovery.md
- pages/fe/database-recovery-rollforward-rollback.md
- pages/fe/dispatch-secondment-contract.md
- pages/fe/drive-by-download.md
- pages/fe/drive-by-download-attack.md
- pages/fe/envelope-encryption.md
- pages/fe/fe-requirements-definition-process.md
- pages/fe/full-differential-incremental-backup.md
- pages/fe/functional-nonfunctional-requirements.md
- pages/fe/hash-function-1.md
- pages/fe/hash-method-uniform-distribution.md
- pages/fe/hybrid-encryption.md
- pages/fe/incident-management-vs-problem-management.md
- pages/fe/incident-service-request-management.md
- pages/fe/input-data-check.md
- pages/fe/input-data-checks.md
- pages/fe/internal-control-components.md
- pages/fe/internal-control-six-elements.md
- pages/fe/java-language-features.md
- pages/fe/java-programming-language.md
- pages/fe/magnetic-disk-access-time.md
- pages/fe/magnetic-disk-average-wait-time.md
- pages/fe/memory-management-methods.md
- pages/fe/message-authentication-code.md
- pages/fe/network-configuration-management.md
- pages/fe/non-functional-requirements.md
- pages/fe/password-hash-authentication.md
- pages/fe/pki-certificate-authority.md
- pages/fe/problem-management.md
- pages/fe/project-life-cycle.md
- pages/fe/project-lifecycle-characteristics.md
- pages/fe/project-management-process-groups.md
- pages/fe/project-management-subject-groups.md
- pages/fe/public-key-cryptography.md
- pages/fe/public-key-encryption-digital-signature.md
- pages/fe/risk-assessment-process.md
- pages/fe/risk-level.md
- pages/fe/security-by-design.md
- pages/fe/security-cia.md
- pages/fe/security-guidelines-comparison.md
- pages/fe/security-threat-countermeasures.md
- pages/fe/software-architecture-design.md
- pages/fe/software-design-phases.md
- pages/fe/sql-aggregate-functions.md
- pages/fe/sql-group-by-aggregate-functions.md
- pages/fe/stack-vs-queue.md
- pages/fe/stored-program-architecture.md
- pages/fe/stored-program-concept.md
- pages/fe/stub-driver.md
- pages/fe/system-audit.md
- pages/fe/system-audit-regulations.md
- pages/fe/system-audit-techniques.md
- pages/fe/system-auditor-independence.md
- pages/fe/system-test-audit.md
- pages/fe/tlo.md
- pages/fe/tlo-technology-licensing-organization.md
- pages/fe/top-down-bottom-up-test.md
- pages/fe/usb.md
- pages/fe/usb-interface.md
- pages/fe/work-made-for-hire.md
- pages/fe/work-made-for-hire-copyright.md


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
- pages/fe/business-impact-analysis.md

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
## 転送専用ページの確認（2026-10-17）

Markdownが1100バイト未満の17件を抽出し、17件すべての本文にHTMLのmeta refresh転送を確認しました。**この条件に当てはまらない転送ページは未調査**です。

- 確認済み転送専用ページ: 17件
- 転送を除いた実記事数の暫定上限: 761件（778 - 17）
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

## 次の手順

1. HTML転送専用ページを全件識別し、実記事の分母を確定する。
2. 未確認の実記事を優先して本文類似度を比較する。
3. 統合・役割分担・維持・要再確認の判定理由を記録する。
4. 修正PRのビルドと旧URL転送を確認する。
