# SG例題対応チェック（CWE/CVSS/CPE/CCE）

## 例題の要点
- 問題テーマ: CWE（Common Weakness Enumeration）の定義。
- 正解判定軸: 「ソフトウェアの脆弱性の種類の一覧」がCWE。
- 誤答の切り分け:
  - CVSS: 脆弱性の深刻度を評価する指標。
  - CPE: 製品・プラットフォームを識別するための名称体系。
  - CCE: セキュリティ設定項目を識別するための識別子。
- ひっかけ: “Common”が付く類似略語（CVE/CVSS/CWE/CPE/CCE）の役割入替。

## 既存記事確認（/pages/sg）
- `vulnerability-information-jvn-cve-cvss.md`: JVN/CVE/CVSSの役割は整理されている。
- `cvss.md`: CVSSの定義と混同回避は十分。
- `vulnerability-management-summary.md`: 脆弱性管理全体の導線はある。
- CWE/CPE/CCEを同一設問文脈で比較する記事は未整備。

## 判定
- 判定: **既存記事に追記推奨**

## 理由
- 現状は「JVN・CVE・CVSS」の説明が強く、今回設問の決め手である「CWE vs CVSS vs CPE vs CCE」の4択切り分けが1ページで完結しない。
- SG試験では略語の定義入替問題が頻出のため、「誤答選択肢を切る表」があると直前復習に有効。

## 具体対応案
### 追記先候補
1. `pages/sg/vulnerability-information-jvn-cve-cvss.md`
   - 新見出し案: `## 関連略語の切り分け（CWE / CVSS / CPE / CCE）`
2. `pages/sg/vulnerability-cheatsheet.md`
   - 新見出し案: `## 似た略語の一問一答（CWE/CVE/CVSS/CPE/CCE）`

### 追記内容（要約）
- CWE=脆弱性の種類一覧
- CVSS=深刻度評価
- CPE=製品識別
- CCE=設定項目識別
- CVE=個別脆弱性識別

### 追記本文案（短縮）
- 「脆弱性の“種類”を体系化したもの」→ **CWE**
- 「脆弱性の“深刻度”を数値化するもの」→ **CVSS**
- 「製品・OS・ミドルウェアなど“対象製品名”の識別」→ **CPE**
- 「セキュリティ設定項目の識別」→ **CCE**
- 「個別脆弱性インシデントの識別番号」→ **CVE**

