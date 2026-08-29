# FE監査 Batch 5 修正指示

`docs/audits/fe-full-audit-2026-08-29.md` の P1 Batch 5 を、人手レビュー済みの判断に従って修正してください。

## 前提

- `docs/agent/fe-content-rules.md`
- `docs/agent/fe-article-template.md`
- `docs/agent/fe-frontmatter-rules.md`
- `docs/agent/fe-tag-rules.md`

を優先してください。

今回は **P1 の構造修正だけ**を対象とします。P2/P3 の候補を理由に本文を広げないでください。

## 対象12ファイル

1. `pages/fe/flip-flop-sequential-circuit.md`
2. `pages/fe/functional-nonfunctional-requirements.md`
3. `pages/fe/half-adder.md`
4. `pages/fe/https.md`
5. `pages/fe/hybrid-encryption.md`
6. `pages/fe/ids-ips-firewall.md`
7. `pages/fe/incident-service-request-management.md`
8. `pages/fe/income-statement-profit-levels.md`
9. `pages/fe/ip-mac-address-routing.md`
10. `pages/fe/ipsec.md`
11. `pages/fe/it-governance.md`
12. `pages/fe/it-investment-evaluation.md`

## 重要：特殊ページを通常記事化しない

`pages/fe/functional-nonfunctional-requirements.md` は通常記事ではなく、`/fe/non-functional-requirements/` へ統合するための **意図的なリダイレクト補助ページ**です。

現在の特徴：

- `layout: null`
- `sitemap: false`
- `meta refresh`
- `noindex,follow`
- canonical が `/fe/non-functional-requirements/`

したがって、監査の通常記事向け P1 指摘は **false positive** と判断します。

**このファイルは変更しないでください。**

Batch 5 は12ファイルをレビュー対象としますが、実際に変更するのは最大11ファイルです。

## ファイル別の修正方針

### 1. `flip-flop-sequential-circuit.md`

P1:
- `date` 不足
- `## 科目Aでどう出る？` 不足

対応：
- Git履歴から実際の初回追加日を調べて `date` を追加する。
- 既存本文には「フリップフロップ＝1ビット保持する順序回路」「組合せ回路との違い」「NAND・加算器・コンデンサとの切り分け」が十分あるので、その内容を再利用して短い `## 科目Aでどう出る？` を追加する。
- 科目B節は追加しない。

### 2. `functional-nonfunctional-requirements.md`

**変更禁止。** リダイレクト補助ページとして現状維持する。

### 3. `half-adder.md`

P1:
- `fe_order`, `date` 不足
- primary tag 不正 (`technology`)
- `## 科目Aでどう出る？` 不足

対応：
- `technology` を `fe-technology` に変更する。
- 同じ `fe_subsection: コンピュータ構成要素` の周辺記事を確認して自然な未使用 `fe_order` を追加する。
- Git履歴から実際の初回追加日を確認して `date` を追加する。
- 既存の「C=AND / S=XOR」「全加算器との違い」を使い、短い `## 科目Aでどう出る？` を追加する。
- 科目B節は追加しない。

### 4. `https.md`

P1:
- `date` 不足
- `## 科目Aでどう出る？` 不足

対応：
- Git履歴から実際の初回追加日を確認して `date` を追加する。
- 既存の HTTPS / WAF / ファイアウォールの切り分けを再利用し、短い `## 科目Aでどう出る？` を追加する。
- P2 では科目B候補だが、今回はP1修正だけなので `## 科目Bでどう使う？` は追加しない。既存の `## どんな場面で使う？` を維持する。

### 5. `hybrid-encryption.md`

P1:
- `fe_order`, `date` 不足
- primary tag 不正 (`technology`)
- `## 科目Aでどう出る？` 不足

対応：
- `technology` を `fe-technology` に変更する。
- 同じセキュリティ系の周辺記事を確認して自然な未使用 `fe_order` を追加する。
- Git履歴から実際の初回追加日を確認して `date` を追加する。
- 既存の「データ本体＝共通鍵、鍵の保護＝公開鍵」を中心に、短い `## 科目Aでどう出る？` を追加する。
- 今回は科目B節を追加しない。

### 6. `ids-ips-firewall.md`

P1:
- `fe_order`, `date` 不足

対応：
- 同じセキュリティ系の周辺記事を確認して自然な未使用 `fe_order` を追加する。
- Git履歴から実際の初回追加日を確認して `date` を追加する。
- 既に `## 科目Aでどう出る？` があり内容も十分なので、本文を書き換えない。
- `intrusion-detection` は今回のP1修正対象ではないため、タグ品質の追加整理はしない。
- 科目B節も今回は追加しない。

### 7. `incident-service-request-management.md`

P1:
- `date` 不足
- `## 科目Aでどう出る？` 不足

対応：
- Git履歴から実際の初回追加日を確認して `date` を追加する。
- 既存の「受付後はまず記録」「分類・優先度・段階的取扱い」の判断軸を再利用して短い `## 科目Aでどう出る？` を追加する。
- マネジメント系なので科目B節は追加しない。

### 8. `income-statement-profit-levels.md`

P1:
- `fe_order`, `date` 不足

対応：
- `fe_subsection: 企業活動` の周辺記事を確認して自然な未使用 `fe_order` を追加する。
- Git履歴から実際の初回追加日を確認して `date` を追加する。
- 既に `## 科目Aでどう出る？` があり、利益段階の切り分けも十分なので本文は変更しない。

### 9. `ip-mac-address-routing.md`

P1:
- タグ数が7個で規則外

現在：
`[fe, fe-technology, network, ip, mac, arp, routing]`

対応：
- 3〜5タグへ整理する。
- 推奨：`[fe, fe-technology, network, routing, arp]`
- `ip` と `mac` は記事タイトル・本文で十分明確なので削除してよい。
- front matter の他項目・本文・科目B節は変更しない。

### 10. `ipsec.md`

P1:
- `date` 不足
- `## 科目Aでどう出る？` 不足

対応：
- Git履歴から実際の初回追加日を確認して `date` を追加する。
- 既存の「ネットワーク層/IP→IPsec、リモートログイン→SSH、Web→TLS、PPP→データリンク層」の切り分けを使い、短い `## 科目Aでどう出る？` を追加する。
- P2では科目B候補だが、今回はP1修正に限定し、科目B節は追加しない。

### 11. `it-governance.md`

P1:
- `## 科目Aでどう出る？` 不足

対応：
- 既存の ITガバナンス / コーポレートガバナンス / コンプライアンス / ITマネジメント の比較を再利用し、短い `## 科目Aでどう出る？` を追加する。
- front matter は変更不要。
- 科目B節は追加しない。

### 12. `it-investment-evaluation.md`

P1:
- `fe_order`, `date` 不足

対応：
- `fe_subsection: システム戦略` の周辺記事を確認して自然な未使用 `fe_order` を追加する。
- Git履歴から実際の初回追加日を確認して `date` を追加する。
- 既に `## 科目Aでどう出る？` があり内容も十分なので本文は変更しない。

## `date` の決め方（厳守）

今回も `last_modified_at` や監査実施日を `date` として流用しないでください。

各ファイルについて、パス指定のGit履歴から **そのパスを初めて追加した最古のコミット**を特定し、そのコミットで対象ファイルが本当に追加 (`A`) されていることを確認してください。

例：

```bash
git log --follow --format='%H %aI %s' -- pages/fe/<file>.md
git show --name-status <candidate-sha> -- pages/fe/<file>.md
```

`git show --name-status` の対象行が `A` であることを確認してから、そのコミット日を日本時間（JST）の `YYYY-MM-DD` として `date` に使用してください。

注意：
- 複数ファイルが同じSHAになる場合でも、ファイルごとに `A` を確認する。
- 「それらしい古いコミット」「一括metadata修正コミット」「現在の `last_modified_at`」を初回追加日とみなさない。
- 初回追加コミットが確認できなければ推測せず、そのファイルは未修正として報告する。

PR本文には、今回 `date` を追加した全ファイルについて次の形式で記載してください。

```text
file -> date -> initial-add commit SHA
```

## `fe_order` の決め方

- 同じ `fe_section` + `fe_subsection` の既存記事を確認する。
- 読者に自然な並びになる未使用値を選ぶ。
- 既存の `fe_order` を不用意に変更しない。
- 重複を機械的にエラー扱いしないが、今回は新規追加値では可能な限り未使用値を使う。

## `last_modified_at`

実際に変更した通常記事だけ：

```yaml
last_modified_at: 2026-08-29
```

へ更新してください。

`functional-nonfunctional-requirements.md` は変更しないため、追加しないでください。

## 本文編集の制限

- `## 科目Aでどう出る？` を追加する場合は、既存本文にある判断軸を移動・再利用して簡潔にする。
- 同じ説明を重複して増やさない。
- 例題依存の文章を追加しない。
- 今回はP2候補を理由に `## 科目Bでどう使う？` を新規追加しない。
- 大幅な本文書き換えは禁止。

## 期待する変更ファイル数

レビュー対象は12ファイルですが、リダイレクト補助ページ1件は変更禁止なので、**変更ファイルは11件**になる想定です。

もし11件にならない場合は、理由をPR本文に明示してください。

## 検証

修正後に最低限、次を確認してください。

1. 変更対象が意図した11通常記事だけであること。
2. `functional-nonfunctional-requirements.md` に差分がないこと。
3. 各変更記事のYAML front matterがパースできること。
4. 通常記事に必須 front matter が揃っていること。
5. primary tag がちょうど1つであること。
6. `ip-mac-address-routing.md` のタグ数が3〜5であること。
7. 指定した `## 科目Aでどう出る？` が1つだけ存在すること。
8. 通常記事末尾が `{% include fe_article_footer.html %}` であること。
9. `git diff --check` が成功すること。
10. 可能なら `bundle exec jekyll build` を実行する。環境上できなければ、その理由をPR本文へ記載する。

## PRで特に報告すること

- 11通常記事を変更し、リダイレクト1件を意図的に除外したこと。
- `date` を追加した各ファイルの `file -> date -> initial-add commit SHA`。
- `fe_order` を追加したファイルと値。
- `ip-mac-address-routing.md` のタグ整理内容。
- 新しい科目B節は追加していないこと。
