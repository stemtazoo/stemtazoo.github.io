# FE 全記事監査 Batch 4 修正指示

対象: `pages/fe/` の通常記事 12件。

このファイルは `docs/audits/fe-full-audit-2026-08-29.md` の P1 Batch 4 を、人手で本文確認したうえで修正方針を具体化したものです。

## 0. 最初に読むもの

作業前に、リポジトリの最新版から次を確認してください。

- `AGENTS.md`
- `docs/agent/fe-content-rules.md`
- `docs/agent/fe-article-template.md`
- `docs/agent/fe-frontmatter-rules.md`
- `docs/agent/fe-tag-rules.md`
- `docs/audits/fe-full-audit-2026-08-29.md`

## 1. 共通ルール

- **この12記事だけを編集する。** 関係ないファイルは変更しない。
- 既存の有用な説明は残し、監査対応のために本文全体を書き直さない。
- 既存内容に判断基準がある場合は、**新しい説明を重複追加せず、移動・見出し変更・短い要約を優先**する。
- 科目Bは `fe-content-rules.md` の基準を満たす記事だけにする。背景知識だけで無理に `## 科目Bでどう使う？` を追加しない。
- 科目Bでない通常記事は `## どんな場面で使う？` を維持する。
- 変更した記事の `last_modified_at` は `2026-08-29` にする。
- 通常記事は末尾を `{% include fe_article_footer.html %}` にする。
- primary tag は `fe-technology` / `fe-management` / `fe-strategy` のどれか **ちょうど1つ**。
- `fe_order` は同じ `fe_section` / `fe_subsection` の既存記事を確認し、表示順として自然で、できれば未使用の値を選ぶ。機械的に適当な数を入れない。

### `date` の取得ルール（最重要）

**推測・現在日・`last_modified_at` の流用は禁止。**

各ファイルについて Git 履歴から、そのパスを実際に追加した最古のコミットを確認する。

推奨手順:

```bash
git log --follow --format='%H %as %s' --reverse -- pages/fe/<file>.md
```

最古候補のコミットについて必ず次も確認する。

```bash
git show --name-status <commit-sha> -- pages/fe/<file>.md
```

そのコミットで対象パスが `A`（追加）であることを確認してから、そのコミット日を `date` に使う。

- 同じ SHA を複数記事に使う場合も、**そのコミットで各対象ファイルが本当に `A` になっていることを記事ごとに確認**する。
- 確認できない場合は `date` を捏造しない。作業結果で blocker として報告する。
- PR本文に `file -> date -> initial-add commit SHA` を記事ごとに列挙する。

## 2. 対象ファイルと修正方針

### 1. `pages/fe/double-entry-bookkeeping-data-model.md`

現状:
- 内容・標準見出しは十分整っている。
- `fe_order` が不足。

対応:
- `企業活動` の近隣記事を確認し、自然な未使用 `fe_order` を追加する。
- 本文は原則変更しない。

### 2. `pages/fe/draw-software.md`

現状:
- `tags` の primary category が `technology` で規則外。
- `fe_order` と `date` が不足。
- `## 科目Aでどう出る？` は既にあり、本文も十分。

対応:
- `technology` を `fe-technology` に変更する。
- `マルチメディア` の近隣記事を見て自然な `fe_order` を追加する。
- 上記の Git 履歴手順で正しい `date` を追加する。
- 本文は原則変更しない。

### 3. `pages/fe/eavesdropping-encryption.md`

現状:
- タイトル末尾が `【FE試験】`。
- `date` が不足。
- `## 科目Aでどう出る？` がないが、冒頭・定義・実用節に、盗聴→暗号化 / 接続制限→IPアドレス制限 / 認証→パスワード、という試験向け判断材料が既にある。

対応:
- タイトル末尾を `【基本情報技術者試験】` に統一する。
- Git 履歴から正しい `date` を追加する。
- `## 定義・仕組み` の後、`## どんな場面で使う？` の前に、短い `## 科目Aでどう出る？` を追加する。
- 内容は既存の判断軸を整理して再利用し、重複説明を増やさない。
- 判断基準の中心:
  - 通信経路上で内容を読ませない → 暗号化
  - 接続元を制限 → IPアドレス制限
  - 利用者を確認 → 認証
  - ポート変更だけでは盗聴対策にならない
- 科目Bは追加しない。

### 4. `pages/fe/electronic-commerce.md`

現状:
- `## 科目Aでどう出る？` がない。
- `## どんな場面で使う？` に EC / SFA / ERP / リテールサポート / EDI の比較が既にある。

対応:
- `## 定義・仕組み` の後に、簡潔な `## 科目Aでどう出る？` を追加する。
- 既存比較を重複させず、必要なら比較表の試験向け部分を移動・要約する。
- 判断基準:
  - 電子的ネットワーク上で商取引そのもの → EC
  - 企業間の注文書・請求書など取引データ交換 → EDI
  - 営業活動支援 → SFA
  - 経営資源の全社統合 → ERP
- `## どんな場面で使う？` は実務用途中心に残す。
- 科目Bは追加しない。

### 5. `pages/fe/elementary-row-operations.md`

現状:
- `date` はある。
- `## 科目Aでどう出る？` もあり、本文は十分。
- 監査で不足している front matter のみを補う対象。

対応:
- 最新の監査 P1 指摘を確認し、不足している `fe_order` を `基礎理論` の近隣記事に合わせて追加する。
- 本文は変更しない。

### 6. `pages/fe/email-protocols.md`

現状:
- `fe_order` と `date` が不足。
- `## 科目Aでどう出る？` はあり、本文も十分。

対応:
- `ネットワーク` の近隣記事を確認して自然な `fe_order` を追加する。
- Git 履歴から正しい `date` を追加する。
- 本文は原則変更しない。

### 7. `pages/fe/encapsulation.md`

現状:
- primary tag が `technology` で規則外。
- `fe_order` と `date` が不足。
- H2 の `## 科目Aでどう出る？` はないが、冒頭と本文に「内部を隠す→カプセル化 / 親の性質→継承 / 同じ命令で異なる動作→多態性」という判断材料がある。

対応:
- `technology` を `fe-technology` に変更する。
- `ソフトウェア` の近隣記事を確認し自然な `fe_order` を追加する。
- Git 履歴から正しい `date` を追加する。
- 監査 P1 が `科目Aでどう出る？` 不足も指摘している場合は、`## 定義・仕組み` の後に短い `## 科目Aでどう出る？` を追加し、既存の判断材料を移動・要約する。重複は増やさない。
- 科目Bは追加しない。

### 8. `pages/fe/equipment-investment-cost-effectiveness.md`

現状:
- `date` が不足。
- `## 科目Aでどう出る？` はないが、本文は「現状総コストと導入後総コストを比較し、導入費も含める」という試験向け計算手順を十分説明している。

対応:
- Git 履歴から正しい `date` を追加する。
- 監査 P1 が `科目Aでどう出る？` 不足も指摘している場合は、`## 定義・仕組み` の後に短い科目A節を追加する。
- 判断基準は「不良率が下がっただけで採用しない。導入費まで含む総コストで比較する」。
- 既存の計算例を重複コピーしない。
- 科目Bは追加しない。

### 9. `pages/fe/euclidean-algorithm.md`

現状:
- `fe_section: 科目B対策`、`## 科目Aでどう出る？`、`## 科目Bでどう使う？` がそろっており、内容もトレース技能に直結している。
- `date` が不足。

対応:
- Git 履歴から正しい `date` を追加する。
- 本文は変更しない。
- 科目B分類は維持する。

### 10. `pages/fe/fail-safe-foolproof-fail-soft.md`

現状:
- tags に `fe` はあるが、正式な primary category (`fe-technology` / `fe-management` / `fe-strategy`) がない。
- `date` が不足。
- `## 科目Aでどう出る？` はないが、本文に故障時/誤操作/継続運転の明確な切り分けがある。

対応:
- 内容・sectionから primary category は `fe-technology` とする。既存の specific tags は3〜5タグルールに収まるよう整理する。
- Git 履歴から正しい `date` を追加する。
- 監査 P1 が `科目Aでどう出る？` 不足も指摘している場合は、短い科目A節を追加し、既存の判断軸を再利用する。
- 判断基準:
  - 故障時、安全側へ → フェールセーフ
  - 人の誤操作を防ぐ → フールプルーフ
  - 障害時、機能低下して継続 → フェールソフト
- 科目Bは追加しない。

### 11. `pages/fe/five-functions-fetch-decode.md`

現状:
- `date` はある。
- 内容は十分で、五大機能と fetch/decode の対応が明確。
- 監査で不足している front matter のみを補う対象。

対応:
- 最新の監査 P1 指摘を確認し、不足している `fe_order` を `コンピュータ構成要素` の近隣記事に合わせて追加する。
- 本文は原則変更しない。

### 12. `pages/fe/fixed-point-iteration.md`

現状:
- タイトル末尾が `【FE試験】`。
- `date` が不足。
- 本文は反復処理を展開し、不動点 `f(p)=p` を導く判断軸が十分ある。

対応:
- タイトル末尾を `【基本情報技術者試験】` に統一する。
- Git 履歴から正しい `date` を追加する。
- 監査 P1 の標準見出し指摘がある場合のみ、既存内容を使って必要な標準 H2 を整える。新規説明の大量追加はしない。
- 反復処理・値の追跡という観点は科目Bにも近いが、**現状の主眼が数値反復と不動点の理解であり、具体的な疑似言語読解技能を主題にしていないなら科目Bを無理に追加しない**。

## 3. 検証

修正後、最低限次を確認する。

1. 変更ファイルが上記12件だけであること。
2. YAML front matter がパースできること。
3. 全12記事に `layout`, `title`, `description`, `permalink`, `tags`, `fe_section`, `fe_subsection`, `fe_order`, `date`, `last_modified_at` があること。
4. primary category tag がちょうど1つであること。
5. タイトル末尾がルールどおり `【基本情報技術者試験】` であること。
6. 必要な標準 H2 があり、同じ内容を重複追加していないこと。
7. 科目Bのある記事は内容が具体的な読解・トレース技能に直結していること。
8. 末尾が `{% include fe_article_footer.html %}` であること。
9. `git diff --check` が通ること。
10. Jekyll / GitHub Pages build を実行できる環境では build を確認すること。できなければ理由を報告すること。

## 4. PR / 作業結果で必ず報告すること

- 変更した12ファイル一覧
- 各ファイルの主要変更点
- 追加した全 `fe_order`
- Git 履歴から追加した全 `date` を次の形式で列挙

```text
pages/fe/example.md -> date: YYYY-MM-DD -> initial-add commit <SHA>
```

- 各 SHA で対象ファイルが `A`（追加）だったことを確認した旨
- title / tag / heading の修正一覧
- YAML / footer / diff check / build の検証結果
- blocker があれば明記

可能なら1つのまとまったコミット・PRにしてください。