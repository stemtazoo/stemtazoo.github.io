# DS Front Matter Rules

This file is written in English for Codex readability. However, DS article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules for articles under `pages/ds`.

## Common Format

Many DS articles use this front matter shape:

```yaml
---
layout: page
title: （日本語タイトル）
description: （そのページ固有のmeta description）
permalink: /ds/（英語スラッグ）/
categories: [category-name]
tags: [ds, 分類タグ1]
prev: /ds/previous-article/
next: /ds/next-article/
last_modified_at: YYYY-MM-DD
---
```

Existing DS files vary, so preserve existing valid conventions unless the requested change requires a metadata fix.

## Required Rules

- The first line of the file must be `---`.
- Front matter must end with `---` on its own line.
- Do not compress front matter into a single line.
- Do not allow `layout`, `title`, `description`, `permalink`, `categories`, `tags`, `prev`, `next`, or `last_modified_at` to appear as accidental plain text in the body.
- Use `layout: page` unless a nearby DS file for the same article type clearly uses a different layout.
- Use the format `/ds/english-slug/` for `permalink`.
- Preserve existing `categories` and `tags` conventions after checking nearby DS articles.
- Always include `ds` in `tags` for DS pages.
- Normal individual DS articles should use `last_modified_at`.
- For new normal DS articles, always include `last_modified_at` in `YYYY-MM-DD` format.
- When meaningfully editing the body, title, description, or reader-facing metadata of an existing normal DS article, update `last_modified_at`.
- If an edited normal DS article does not yet have `last_modified_at`, add it.
- Use the current date at the time of editing.
- Do not write visible "last updated" text inside the body.
- Do not add `last_modified_at` to DS index pages, category pages, generated exports, or non-article files unless the page is clearly a normal reader-facing article.
- Do not mass-add `last_modified_at` to unrelated DS files in a content-editing task.
- Do not change `categories`, `tags`, `prev`, or `next` just because `last_modified_at` is being added.
- Do not guess `prev` / `next`.

## Title

`title` should clearly identify the term and the DS検定 or practical data-analysis context.

Good patterns:

```yaml
title: ピアソンの相関係数とは？意味と使いどころをわかりやすく解説【DS検定】
title: LEFT JOINでWHERE句を使うときの注意点【SQL・DS検定】
```

## Description

When creating or revising the `description` field in front matter:

- Do not use boilerplate descriptions that could fit any article.
- Avoid generic phrases such as `初心者向けにわかりやすく解説します`, `基本から整理します`, `試験対策として重要なポイントを解説します`, or `この記事では〜について説明します`.
- The description must summarize the article-specific learning value.
- Include at least one concrete element from the article, such as the main judgment criterion, a common misunderstanding, a distinction from a similar term, a typical exam trap, a practical use case, or the type of question where the concept appears.
- Prefer roughly 100-160 Japanese characters when natural, especially for pages that were previously flagged for short descriptions. Do not simply lengthen the description by adding filler.
- Do not repeat the title with minor wording changes.
- Make each description unique enough that it could not be reused for another article without editing.
- For DS articles, prioritize descriptions that show what data literacy judgment the reader will be able to make, what practical misunderstanding the article prevents, and how the concept appears in analysis, statistics, visualization, business use, or data handling.
- Start with a clear definition or role of the concept when possible.
- Include exam context such as `DS検定` only when it fits naturally.
- Avoid keyword stuffing.
- Do not make the description look like a bullet list.
- Do not contradict the page title or page scope.
- Do not duplicate the same sentence as visible body text unless intentionally rewritten.

Bad / good examples:

```yaml
# Bad
description: 相関係数について初心者向けにわかりやすく解説します。
# Good
description: 相関係数を「2つの量が一緒に増減する強さ」として整理し、因果関係との混同や外れ値に左右される分析上の注意点を解説します。

# Bad
description: SQLのJOINの基本を整理します。
# Good
description: JOINを「複数テーブルをキーで結合する操作」として整理し、INNER JOINとLEFT JOINで残る行が変わる実務上の判断ポイントを解説します。
```
## Categories

- Check nearby DS articles before choosing `categories`.
- Preserve existing category naming style.
- Use categories to support DS learning areas, not every subtopic.
- Do not introduce a new category without checking index/category behavior.

## `prev` / `next`

- Preserve valid existing `prev` / `next` fields.
- Do not add new `prev` / `next` unless the learning sequence is clear and confirmed.
- Use absolute site paths matching actual `permalink` values.
- Never duplicate `prev` / `next` as visible body text.
