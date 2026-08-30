# FE全記事監査 Batch 6 修正指示

## 目的

`docs/audits/fe-full-audit-2026-08-29.md` の P1 Structural findings のうち、Batch 6 として人手確認済みの12記事だけを修正する。

今回は **P1の構造・front matter・標準見出しの修正に限定**する。P2/P3の候補を同時に広げない。

## 必ず先に読むルール

- `docs/agent/fe-content-rules.md`
- `docs/agent/fe-article-template.md`
- `docs/agent/fe-frontmatter-rules.md`
- `docs/agent/fe-tag-rules.md`

これらと本指示が矛盾する場合は、上記ルールを優先する。

## 対象12記事

1. `pages/fe/java-beans.md`
2. `pages/fe/jdbc.md`
3. `pages/fe/least-privilege-database-access.md`
4. `pages/fe/legacy-interface-standards.md`
5. `pages/fe/live-migration-virtual-server.md`
6. `pages/fe/mips-processing-time.md`
7. `pages/fe/morphing.md`
8. `pages/fe/mrp.md`
9. `pages/fe/nand-gate.md`
10. `pages/fe/nas.md`
11. `pages/fe/newton-method.md`
12. `pages/fe/osi-reference-model.md`

**この12記事以外は変更しないこと。**

---

## 共通ルール

### 1. `date` は推測禁止

不足している `date` は、対象ファイルが実際に最初に追加されたGit履歴から求める。

まず次を使う。

```bash
git log --follow --diff-filter=A --format='%H %ad' --date=short -- pages/fe/<file>.md
```

候補SHAを得たら必ず次で確認する。

```bash
git show --name-status <candidate-sha> -- pages/fe/<file>.md
```

対象パスの status が **`A`** であることを確認してから、そのコミット日を `date` に使う。

- 既存の `last_modified_at` をそのまま `date` にコピーしない。
- 現在日や一律の日付を入れない。
- 複数記事に同じSHAが出た場合でも、**記事ごとにそのパスが `A` か確認する**。
- `--follow` で追跡できない場合は、履歴を個別に調査し、推測しない。

PR本文には、`date` を追加した全ファイルについて次の形式を必ず記載する。

```text
file -> date -> initial-add commit SHA
```

### 2. `fe_order` の補完

不足している場合、同じ `fe_section` / `fe_subsection` の既存記事を確認し、表示順として自然な未使用値を選ぶ。

- 既存値を無意味に変更しない。
- 重複を避ける。
- 必ず同じ subsection の周辺記事を確認する。

### 3. 科目Bを無理に追加しない

今回、**新しい `## 科目Bでどう使う？` は追加しない**。

アルゴリズムやセキュリティに近い記事でも、P1修正のためだけに科目Bへ広げない。

### 4. 本文の再利用を優先

`## 科目Aでどう出る？` が不足している記事では、すでに本文にある判断基準・比較表・ひっかけを移動または短く再構成する。

新しい教科書的説明を大量に追加しない。

### 5. 更新日

実際に変更した通常記事は

```yaml
last_modified_at: 2026-08-30
```

へ更新する。

---

# 記事ごとの修正方針

## 1. `pages/fe/java-beans.md`

現状確認:

- `layout`, title, description, permalink, tags, section/subsection は妥当。
- `## 科目Aでどう出る？` はすでにあり、JavaBeans / JavaScript / Javaアプリケーション / アプレット / サーブレットの切り分けも十分。
- 不足は `fe_order`, `date`。

修正:

- `fe_order` を同じ `テクノロジ系 / ソフトウェア` の周辺記事から未使用値で補完。
- `date` をGit初回追加履歴から補完。
- 本文は変更しない。

## 2. `pages/fe/jdbc.md`

現状確認:

- primary tag が `technology` で規則外。
- `fe_order`, `date` が不足。
- `## 科目Aでどう出る？` が不足。
- 本文には JDBC / SQL / JavaVM / HTML の十分な判断材料がある。

修正:

- `tags: [fe, technology, database, java]` の `technology` を `fe-technology` に修正。
- `fe_order` を同じ `テクノロジ系 / データベース` の周辺記事から未使用値で補完。
- `date` をGit初回追加履歴から補完。
- `## 定義・仕組み` の後、`## どんな場面で使う？` の前に、短い `## 科目Aでどう出る？` を追加。
- 中心メッセージは以下程度にする。

```text
JavaからDBへ接続しSQLを実行
→ JDBC

DBへ命令する言語
→ SQL

Javaを実行する仮想マシン
→ JavaVM

Webページの構造
→ HTML
```

既存本文の判断軸を再利用し、重複説明を増やさない。

## 3. `pages/fe/least-privilege-database-access.md`

現状確認:

- `## 科目Aでどう出る？` はすでにあり、検索/表示→参照権限、更新→更新権限、管理→管理者権限という判断軸も十分。
- tags も主要カテゴリを含み妥当。
- 不足は `fe_order`, `date`。

修正:

- `fe_order` を同じ `テクノロジ系 / セキュリティ` の周辺記事から未使用値で補完。
- `date` をGit初回追加履歴から補完。
- 本文は変更しない。

## 4. `pages/fe/legacy-interface-standards.md`

現状確認:

- `## 科目Aでどう出る？` はすでにあり、IrDA / Bluetooth / IEEE 1394 / RS-232C / PIAFS の切り分けも十分。
- 不足は `fe_order`, `date`。

修正:

- `fe_order` を同じ `テクノロジ系 / ネットワーク` の周辺記事から未使用値で補完。
- `date` をGit初回追加履歴から補完。
- 本文は変更しない。

## 5. `pages/fe/live-migration-virtual-server.md`

現状確認:

- `fe_order: 80` は既にある。
- `## 科目Aでどう出る？` も十分。
- 不足は `date` のみ。

修正:

- `date` をGit初回追加履歴から補完。
- 本文・既存 `fe_order` は変更しない。

## 6. `pages/fe/mips-processing-time.md`

現状確認:

- title が `【FE試験】` で標準表記外。
- `fe_order: 15` は既にある。
- `date` が不足。
- `## 科目Aでどう出る？` が不足。
- 本文には MIPS→命令/秒、CPU処理時間、I/O時間、単位変換の判断材料が十分ある。

修正:

- title末尾を `【基本情報技術者試験】` に統一。それ以外のタイトル文言は原則維持。
- `date` をGit初回追加履歴から補完。
- `## 定義・仕組み` の後、`## どんな場面で使う？` の前に、短い `## 科目Aでどう出る？` を追加。
- 既存内容を再利用して、次の解法順を判断基準として明示する。

```text
1. MIPSを1秒あたり命令数へ直す
2. 命令数 ÷ 命令/秒でCPU時間
3. I/O回数 × 1回時間を求める
4. 単位をそろえて加算
```

- 科目B節は追加しない。

## 7. `pages/fe/morphing.md`

現状確認:

- `fe_order: 20` あり。
- `## 科目Aでどう出る？` も十分。
- 不足は `date` のみ。

修正:

- `date` をGit初回追加履歴から補完。
- 本文・既存 `fe_order` は変更しない。

## 8. `pages/fe/mrp.md`

現状確認:

- `fe_order: 30` あり。
- `## 科目Aでどう出る？` も十分。
- primary tag `fe-strategy` は妥当。
- 不足は `date` のみ。

修正:

- `date` をGit初回追加履歴から補完。
- 本文・既存 `fe_order` は変更しない。

## 9. `pages/fe/nand-gate.md`

現状確認:

- primary tag が `technology` で規則外。
- `fe_order`, `date` が不足。
- `## 科目Aでどう出る？` が不足。
- 本文には真理値表、`11` のときだけ0、万能ゲート、NOT/AND/OR構成の判断材料が十分ある。

修正:

- `tags: [fe, technology, hardware, logic-circuit]` の `technology` を `fe-technology` に修正。
- `fe_order` を同じ `テクノロジ系 / コンピュータ構成要素` の周辺記事から未使用値で補完。
- `date` をGit初回追加履歴から補完。
- `## 定義・仕組み` の後、`## どんな場面で使う？` の前に、短い `## 科目Aでどう出る？` を追加。
- 判断基準は以下程度。

```text
11のときだけ0
→ NAND

ANDの出力を反転
→ NAND

NANDだけでNOT・AND・ORを構成できる
→ 万能ゲート
```

既存本文を再利用して簡潔にする。

## 10. `pages/fe/nas.md`

現状確認:

- front matter の必須項目は既に揃っている。
- `## 科目Aでどう出る？` が不足。
- 本文には NAS / SAN / DAS / RAID の比較が十分ある。

修正:

- `## 定義・仕組み` の後、`## どんな場面で使う？` の前に、短い `## 科目Aでどう出る？` を追加。
- 判断基準は本文から再利用する。

```text
ネットワーク経由・ファイル単位・SMB/NFS
→ NAS

ブロック単位・iSCSI/Fibre Channel
→ SAN

機器へ直接接続
→ DAS

複数ディスクの構成
→ RAID
```

- 既存 `date: 2026-08-19` と `fe_order: 50` は変更しない。

## 11. `pages/fe/newton-method.md`

現状確認:

- title が `【FE試験】` で標準表記外。
- `fe_order: 130` は既にある。
- `date` が不足。
- `## 科目Aでどう出る？` が不足。
- 本文には接線・微分・初期値1つ・必ず収束しない、という十分な判断材料がある。

修正:

- title末尾を `【基本情報技術者試験】` に統一。それ以外のタイトル文言は原則維持。
- `date` をGit初回追加履歴から補完。
- `## 定義・仕組み` の後、`## どんな場面で使う？` の前に、短い `## 科目Aでどう出る？` を追加。
- 既存判断軸を再利用し、次を明示する。

```text
接線・微分を使う
→ ニュートン法

初期値は基本1つ
→ ニュートン法

どんな初期値でも必ず収束
→ 誤り
```

- 科目B節は追加しない。

## 12. `pages/fe/osi-reference-model.md`

現状確認:

- `## 科目Aでどう出る？` はすでにあり、各層の判断ワードも十分。
- tags も妥当。
- 不足は `fe_order`, `date`。

修正:

- `fe_order` を同じ `テクノロジ系 / ネットワーク` の周辺記事から未使用値で補完。
- `date` をGit初回追加履歴から補完。
- 本文は変更しない。

---

# 変更後の必須検証

## 対象ファイル

最終diffに含まれる記事ファイルは、上記12記事だけであることを確認する。

```bash
git diff --name-only <base>...HEAD
```

今回の指示ファイル自身は既にbase側にあるため、修正PRでは `pages/fe/` の上記12記事だけが変わる想定。

## YAML/front matter

各変更記事について以下を確認する。

- `layout: page`
- title
- description
- permalink
- tags
- `fe_section`
- `fe_subsection`
- `fe_order`
- `date`
- `last_modified_at: 2026-08-30`

primary tag は `fe-technology` / `fe-management` / `fe-strategy` のいずれか1つだけ。

## 見出し

- `jdbc.md`
- `mips-processing-time.md`
- `nand-gate.md`
- `nas.md`
- `newton-method.md`

には、修正後ちょうど1つの `## 科目Aでどう出る？` があること。

今回、新しい `## 科目Bでどう使う？` は0件であること。

## フッター

変更した全通常記事が末尾で次を使っていること。

```liquid
{% include fe_article_footer.html %}
```

## 日付のPR記録

`date` を追加した全記事について、PR本文に必ず

```text
file -> date -> initial-add SHA
```

を列挙し、候補SHAでその対象ファイルが `A` だったことを確認した旨を書く。

## 最終確認

```bash
git diff --check
```

可能ならJekyll buildも実行する。ローカル環境の依存関係で実行できない場合は、その理由をPR本文へ明記し、GitHub Actionsで確認する。

---

# PRで報告する内容

1. 変更した12記事
2. 各記事で直したP1項目
3. `date` を追加した記事の `file -> date -> initial-add SHA`
4. `fe_order` を追加した記事と採用値
5. `technology -> fe-technology` を直した記事
6. `## 科目Aでどう出る？` を追加した記事
7. 新しい科目B節は追加していないこと
8. 検証結果

本文を不用意に広げず、**P1修正だけの小さなPR**にすること。