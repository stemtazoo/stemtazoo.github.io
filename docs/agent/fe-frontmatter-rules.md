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

- Make the description unique to each page.
- Aim for a concise Japanese meta description that explains the page-specific value.
- Mention 科目A or 科目B naturally when it helps clarify the article role.
- Avoid generic boilerplate endings reused across many FE pages.
- Do not make the description look like a bullet list.
- Do not contradict the page title or page scope.
- Do not duplicate the same sentence as visible body text.

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
