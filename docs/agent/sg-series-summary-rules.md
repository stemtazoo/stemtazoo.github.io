# SG Series Summary Rules

This file is written in English for Codex readability. However, SG article content must be written in Japanese unless the user explicitly requests otherwise.

Use these standard rules when creating study-friendly series summary pages from existing articles under `pages/sg`.

Follow this workflow when the user asks to create an SG article series page, create a `まとめ`, or propose series candidates.

## Basic Policy

- Do not make summary pages into simple link collections.
- Reorganize existing standalone articles into a learning path that beginners can read in order.
- Focus on the judgment criteria used to eliminate choices in the SG exam.
- Organize differences, roles, procedures, and scope for similar terms.
- After creating a summary page, always add a link to the related category summary page under `pages/sg/category/*.md`.

## Pre-Work Checks

Before editing, always check:

- Target articles under `pages/sg`.
- Each article's front matter `title` / `description` / `permalink` / `tags`.
- Body headings and the concept handled by each article.
- Related `pages/sg/category/*.md` files.

Important:

- Do not guess `permalink`; always confirm and use the actual front matter.
- Do not create internal links to non-existent articles.
- Do not link planned articles in the body. Mention them only as possible future additions.
- Match existing article title text and link targets accurately.

## When Proposing Series Candidates

If the user has not chosen the target series yet, do not create files.

First check existing articles, then propose around 5-10 themes that naturally group together. Do not be overly guided by example theme names; prioritize the actual article set and relationships.

```md
### シリーズ候補1：〇〇まとめ

- 想定タイトル：
- 想定 permalink：
- 対象になりそうな既存記事：
  - 記事タイトル
  - permalink
- このシリーズで学べること：
- SG試験での判断ポイント：
- 追加で作るとよさそうな記事：
```

Proposal cautions:

- Under `対象になりそうな既存記事`, list only articles that actually exist.
- List useful future articles separately from existing articles.
- Summary page candidates should group multiple articles; they should not be single-term articles.
- If a candidate may overlap with an existing summary page, state whether consolidation, reinforcement, or a separate theme is better.

## When Creating The Selected Series

When the user specifies the target series, create a new Markdown file under `pages/sg`.

- Match the filename to the English slug used in `permalink`.
- Example: `/sg/project-management-summary/` uses `pages/sg/project-management-summary.md`.

front matter:

```md
---
layout: page
title: 〇〇まとめ｜主要用語を整理【SG試験】
description: 〇〇は〜です。SG試験で問われやすい用語の違い、判断基準、学習順序を整理します。
permalink: /sg/xxxxx-summary/
tags: [sg, 分類タグ1, 分類タグ2]
last_modified_at: YYYY-MM-DD
---
```

Front matter cautions:

- Do not put blank lines or characters before front matter.
- Use `layout: page`.
- Make `description` unique to the series and aim for roughly 100-140 Japanese characters.
- Write `tags` as a YAML array.
- Include `last_modified_at`.
- Do not add `prev` / `next`.
- Choose category tags such as `sg-security-measures`, `sg-security-management`, or `sg-management` according to the existing category structure.

## Standard Summary Page Structure

As a rule, use the following heading order.

```md
## まず結論

## 全体像

## 主要用語の整理

## SG試験でのひっかけポイント

## おすすめの学習順序

## 記事一覧

## まとめ（試験直前用）

{% include sg_article_footer.html %}
```

Role of each section:

- `## まず結論`: Explain what the reader will learn in this series and what they need to judge in the SG exam.
- `## 全体像`: Give beginners a high-level map of the theme.
- `## 主要用語の整理`: Use a table to organize terms and judgment criteria, with links to existing articles.
- `## SG試験でのひっかけポイント`: Use a table to organize differences between similar terms.
- `## おすすめの学習順序`: Show the recommended reading order as a numbered list.
- `## 記事一覧`: List the articles in the series by category.
- `## まとめ（試験直前用）`: Summarize judgment criteria in about 3-5 lines.

## Body Link Rules

- Put only existing internal links in the summary page body.
- Confirm `permalink` from actual front matter.
- Base link text on the existing article `title`.
- Linking the same article multiple times is acceptable only when it has learning value.
- Keep external links to the minimum necessary; usually prioritize internal links to existing articles.

## Adding Links To Category Summary Pages

After creating a series summary page, always add a link to the related category file under `pages/sg/category/*.md`.

How to choose the destination:

- Authentication, access control, network countermeasures, malware, physical controls, vulnerability countermeasures: `pages/sg/category/security-measures.md`
- Information security policy, ISMS, risk management, vendor management, incident response, audit, log management: `pages/sg/category/security-management.md`
- Laws, personal information, copyright, electronic signatures, unauthorized access: `pages/sg/category/law.md`
- Network, database, system configuration, cryptography, and other technology elements: `pages/sg/category/technology.md`
- PMBOK, project management, service management, system audit: `pages/sg/category/management.md`
- Business strategy, business improvement, organization management, procurement and contract topics: `pages/sg/category/strategy.md`
- Entry points and cross-cutting themes for information security as a whole: `pages/sg/category/security-overview.md`

How to add the link:

- If the category page has `## まず読むまとめ記事` or `## 関連するまとめページ`, add the link there.
- If that section does not exist, add the link after the category explanation and before the related article list.
- Add a one-line description under the link, or follow the existing category page style.
- If the category page has `summary_page_urls`, add the new summary page `permalink` so it does not duplicate in the normal article list.
- If the category page has `curated_slugs`, add the new summary page slug when needed so it does not duplicate in `その他の関連記事`.
- Even when the summary strongly relates to multiple categories, choose one primary category first. Add secondary category links only when useful, and avoid excessive duplication.

## Post-Creation Checks

- Confirm that the new summary page front matter is correct.
- Confirm that every internal link points to an existing `permalink`.
- Confirm that the related category summary page links to the new summary page.
- Confirm that pages needing `summary_page_urls` or `curated_slugs` updates are not missed.
- Run `bundle exec jekyll build` if possible.
- If editing Liquid, prioritize GitHub Pages compatibility and avoid complex conditions.
