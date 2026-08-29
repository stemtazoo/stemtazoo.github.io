# FE Audit Batch 1 Repair Instructions

Use these instructions to repair the first reviewed batch from `docs/audits/fe-full-audit-2026-08-29.md`.

## Important

- Read `AGENTS.md` and all current FE rule files before editing.
- Edit only the 12 files listed below.
- Do not make unrelated rewrites.
- Preserve useful existing explanations and examples.
- Prefer moving or renaming existing content over duplicating it.
- Keep article text in Japanese.
- Use the shared footer `{% include fe_article_footer.html %}`.
- Update `last_modified_at` to `2026-08-29` on files that are changed.
- After editing, run the available FE/Jekyll validation and report the result.
- Make the repairs in one batch/commit if practical.

## Reviewer decisions

### 1. `pages/fe/addressing-modes.md`

Finding confirmed: missing `date`.

- Add `date: 2026-07-06`.
- This date is based on the first repository commit that added the article.
- Do not change the article body.

### 2. `pages/fe/adjacency-matrix.md`

Finding confirmed: primary category tag is wrong.

- Change `tags: [fe, technology, basic-theory, graph]`
  to `tags: [fe, fe-technology, basic-theory, graph]`.
- Do not otherwise rewrite the article.

### 3. `pages/fe/ansoff-growth-matrix.md`

Finding confirmed: `fe_order` is missing.

Semantic review also found that `fe_subsection: 経営戦略マネジメント` is inconsistent with nearby FE strategy articles such as benchmarking, BPM, and business-domain, which use `経営戦略`.

- Change `fe_subsection` to `経営戦略`.
- Add an unused numeric `fe_order` that places this article near the other `経営戦略` articles.
- Inspect current articles in that exact section/subsection before choosing the number; do not guess blindly.
- Do not change the article body.

### 4. `pages/fe/audit-working-papers.md`

Finding confirmed, but the content already exists.

- The current `### 科目Aでの典型的な聞かれ方` is effectively the missing Subject A section.
- Promote/rename it to the standard H2 heading `## 科目Aでどう出る？`.
- Preserve its table and explanation.
- Do not duplicate the same content elsewhere.

### 5. `pages/fe/benchmarking.md`

Finding confirmed: there is no standard `## 科目Aでどう出る？` H2.

- Add `## 科目Aでどう出る？` after `## 定義・仕組み` and before `## どんな場面で使う？`.
- Reuse the article's existing exam judgment material: `先進企業・比較・ベストプラクティス・ギャップ → ベンチマーキング`, `抜本的 → BPR`, `全社的品質管理 → TQC`, `独自の中核能力 → コアコンピタンス`.
- Prefer moving/condensing the existing FE comparison table from the later confusion section rather than duplicating it.
- Keep the section concise and focused on eliminating answer choices.

### 6. `pages/fe/binary-representation.md`

Findings confirmed: missing `date`, nonstandard title suffix, and missing Subject A heading.

- Add `date: 2026-07-06`, based on the first repository commit that added the article.
- Change the title suffix from `【FE試験】` to `【基本情報技術者試験】`.
- Add `## 科目Aでどう出る？` after `## 定義・仕組み`.
- The section should distinguish the two typical judgments already explained in the article: 2's-complement negative-number interpretation and binary-fraction place values/conversion.
- Keep `## どんな場面で使う？`.
- Do not add `## 科目Bでどう使う？`; the current article is primarily a Subject A representation/calculation article and does not yet provide a concrete pseudocode-reading skill.

### 7. `pages/fe/block-search-average-comparisons.md`

Finding confirmed: neither optional standard fifth heading exists.

- Do **not** force a Subject B section. This article currently teaches an average-comparison calculation rather than a concrete pseudocode trace/read/debug skill.
- Add a concise `## どんな場面で使う？` section after `## 科目Aでどう出る？`.
- Explain that block search applies to ordered data divided into blocks, first narrowing to a block and then searching within it.
- Keep the article centered on reconstructing the average comparison count; do not broaden into a textbook survey.

### 8. `pages/fe/bpm.md`

Finding confirmed: missing `## 科目Aでどう出る？`.

- Add the standard Subject A section after `## 定義・仕組み`.
- Reuse the article's existing judgment rules: `継続的な業務プロセス改善 → BPM`, `抜本的再設計 → BPR`, `経営資源の統合 → ERP`, `顧客情報 → CRM`, `分析・可視化 → BI`.
- Avoid simply repeating the opening table word for word; keep this section short and question-oriented.

### 9. `pages/fe/brute-force-attack.md`

The mechanical report was triggered partly by a nonstandard practical heading, but semantic review shows a useful Subject B security-control connection already exists.

- Rename `## どんな場面で使われる？` to the standard `## どんな場面で使う？`.
- Convert the existing `## オンライン攻撃とオフライン攻撃` section into `## 科目Bでどう使う？` because it already provides concrete control-selection judgment:
  - online brute-force attempts → rate limiting / account lock / CAPTCHA / MFA;
  - offline hash cracking → long passwords / salt / appropriate password hashing; online lockout alone does not help.
- Add only a short introductory sentence connecting scenario conditions to selecting an effective control. Preserve the existing table and bullets.
- Do not overstate that every brute-force question is Subject B.

### 10. `pages/fe/business-continuity-management.md`

Finding confirmed: missing `## 科目Aでどう出る？`.

- Add the standard Subject A section after `## 定義・仕組み`.
- Reuse the existing distinction: `影響分析 → BIA`, `計画 → BCP`, `教育・訓練・テスト・見直し → BCM`.
- Move or condense the FE-specific judgment wording currently under `## どんな場面で使う？` so it is not duplicated.

### 11. `pages/fe/business-continuity-plan.md`

Finding confirmed: missing `## 科目Aでどう出る？`.

- Add the standard Subject A section after `## 定義・仕組み`.
- Focus on `計画 → BCP`, `影響分析 → BIA`, `継続的運用・訓練・見直し → BCM`, `IT復旧中心 → DR`, and the RTO/MTD distinction when useful.
- Move or condense existing exam-specific wording rather than duplicating it.

### 12. `pages/fe/business-domain.md`

Finding confirmed: missing `## 科目Aでどう出る？`.

- Add the standard Subject A section after `## 定義・仕組み`.
- Move the current FE-specific keyword list from `## どんな場面で使う？` into this new section where appropriate.
- Judgment focus: `事業を行う領域 → 事業ドメイン`, `企業独自の中核能力 → コアコンピタンス`, `ヒト・モノ・カネ・情報 → 経営資源`, `市場を顧客属性やニーズで区切る → 市場セグメント`.
- Keep `## どんな場面で使う？` for actual business-use context.

## Validation after repair

After the 12 edits, verify at least the following:

1. Each normal article has valid YAML front matter.
2. Each edited article has the standard footer include.
3. Each edited article has the required standard headings, with Subject B only where approved above.
4. Tags contain exactly one FE primary category tag (`fe-technology`, `fe-management`, or `fe-strategy`).
5. `fe_section`, `fe_subsection`, and `fe_order` are present.
6. The Jekyll/GitHub Pages build succeeds.
7. No unrelated file is modified.

Report the changed files, key changes, chosen `fe_order` for Ansoff, and validation/build result.