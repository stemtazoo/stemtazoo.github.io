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
- For new DS articles, include `last_modified_at` in `YYYY-MM-DD` format if the current convention in nearby DS articles supports it.
- Do not blindly add `last_modified_at` to every existing DS article in unrelated tasks.
- When substantially editing the body of an existing DS article that already uses `last_modified_at`, update it when appropriate.
- Do not write visible "last updated" text inside the body.
- Do not guess `prev` / `next`.

## Title

`title` should clearly identify the term and the DS検定 or practical data-analysis context.

Good patterns:

```yaml
title: ピアソンの相関係数とは？意味と使いどころをわかりやすく解説【DS検定】
title: LEFT JOINでWHERE句を使うときの注意点【SQL・DS検定】
```

## Description

- Make the description unique to the page.
- Explain what the reader will understand after reading.
- Mention similar-term differences, practical use, or exam judgment when natural.
- Avoid repeating one long boilerplate sentence across many pages.
- Do not contradict the page scope.
- Do not duplicate the same sentence as visible body text unless intentionally rewritten.

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
