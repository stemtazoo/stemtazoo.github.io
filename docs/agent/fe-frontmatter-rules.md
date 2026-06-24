# FE Front Matter Rules

This file is written in English for Codex readability. However, FE article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules for normal 基本情報技術者試験 articles under `pages/fe`.

## Standard Front Matter Format

Use the following front matter format for normal FE articles:

```yaml
---
layout: page
title: （日本語タイトル）【基本情報技術者試験】
description: （そのページ固有のmeta description）
permalink: /fe/（英語スラッグ）/
tags: [fe, fe-technology, 具体タグ]
fe_section: （科目A対策 / 科目B対策 / テクノロジ系 / マネジメント系 / ストラテジ系 / 情報セキュリティ）
fe_subsection: （アルゴリズム / データ構造 / 疑似言語 / トレース / 基礎理論 / ネットワーク など）
fe_order: 数値
date: YYYY-MM-DD
last_modified_at: YYYY-MM-DD
---
```

## Required Rules

- The first line of the file must be `---`.
- Front matter must end with `---` on its own line.
- Do not compress front matter into a single line.
- Use `layout: page` for normal FE articles.
- Always include `tags`.
- Always include `fe_section`, `fe_subsection`, and `fe_order` for normal FE articles so they appear on `/fe/`.
- Use `permalink: /fe/english-slug/`.
- Do not add `prev` or `next` unless the user explicitly requests it.
- Keep `description` unique to the article.
- Do not duplicate the exact `description` sentence in the visible body.
- Include `date` and `last_modified_at` in `YYYY-MM-DD` format for newly created normal FE articles.
- When meaningfully editing an existing normal FE article, update `last_modified_at`.
- Do not allow `layout`, `title`, `description`, `permalink`, `tags`, `fe_section`, `fe_subsection`, `fe_order`, `date`, or `last_modified_at` to appear as accidental plain text in the body.

## Title

- Use a Japanese title that clearly names the concept.
- Include `【基本情報技術者試験】` for normal FE articles unless nearby FE pages for the same article type intentionally use another convention.
- Keep the title aligned with one term or one concept.

Good patterns:

```yaml
title: スタックとは？後入れ先出しをわかりやすく解説【基本情報技術者試験】
title: 二分探索とは？整列済みデータを半分ずつ調べる考え方【基本情報技術者試験】
```

## Description

When creating or revising the `description` field in front matter:

- Do not use boilerplate descriptions that could fit any article.
- Avoid generic phrases such as `初心者向けにわかりやすく解説します`, `基本から整理します`, `試験対策として重要なポイントを解説します`, or `この記事では〜について説明します`.
- The description must summarize the article-specific learning value.
- Include at least one concrete element from the article, such as the main judgment criterion, a common misunderstanding, a distinction from a similar term, a typical exam trap, a practical use case, or the type of question where the concept appears.
- Prefer roughly 80-140 Japanese characters when natural. Do not simply lengthen the description by adding filler.
- Do not repeat the title with minor wording changes.
- Make each description unique enough that it could not be reused for another article without editing.
- For FE articles, prioritize descriptions that show what technical or exam judgment the reader will be able to make, what similar term, formula, mechanism, or process the article helps distinguish, how the concept appears in FE-style questions, and whether the article helps with calculation, terminology, algorithm, database, network, security, management, or strategy questions.
- Mention 科目A or 科目B naturally when it helps clarify the article role.
- Avoid generic boilerplate endings reused across many FE pages.
- Do not make the description look like a bullet list.
- Do not contradict the page title or page scope.
- Do not duplicate the same sentence as visible body text.

Bad / good examples:

```yaml
# Bad
description: 正規化について基本からわかりやすく解説します。
# Good
description: 正規化を「データの重複と更新時の不整合を減らす考え方」として整理し、第1〜第3正規形の切り分けをFE試験向けに解説します。

# Bad
description: スタックとキューについて説明します。
# Good
description: スタックは後入れ先出し、キューは先入れ先出しとして整理し、データ構造の動作順序を問うFE試験の選択肢を切る視点を解説します。
```
## `fe_section`, `fe_subsection`, And `fe_order`

The FE index page `/fe/` uses `fe_section`, `fe_subsection`, and `fe_order` to list pages.

- Choose `fe_section` from the site’s current FE learning structure, such as `科目A対策`, `科目B対策`, `テクノロジ系`, `マネジメント系`, `ストラテジ系`, or `情報セキュリティ`.
- Choose a clear `fe_subsection`, such as `アルゴリズム`, `データ構造`, `疑似言語`, `トレース`, `基礎理論`, `ネットワーク`, `データベース`, `プロジェクトマネジメント`, `サービスマネジメント`, `システム監査`, `システム戦略`, `経営戦略`, or `法務`.
- Use numeric `fe_order` values with spacing such as `10`, `20`, `30`, etc.
- Keep related topics close together.
- Confirm that new FE articles appear under the intended section on `/fe/` after building when possible.

Suggested ordering examples:

```yaml
# array.md
fe_section: 科目B対策
fe_subsection: データ構造
fe_order: 10

# stack.md
fe_section: 科目B対策
fe_subsection: データ構造
fe_order: 20

# queue.md
fe_section: 科目B対策
fe_subsection: データ構造
fe_order: 30

# linear-search.md
fe_section: 科目B対策
fe_subsection: アルゴリズム
fe_order: 40

# binary-search.md
fe_section: 科目B対策
fe_subsection: アルゴリズム
fe_order: 50
```

## `prev` / `next`

- Do not add `prev` or `next` to FE articles unless the user explicitly requests it.
- Preserve valid existing `prev` / `next` fields only if they are intentionally part of a requested structure.
- Never duplicate `prev` / `next` as visible body text.
