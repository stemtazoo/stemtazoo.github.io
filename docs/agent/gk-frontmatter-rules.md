# GK Front Matter Rules

This file is written in English for Codex readability. However, GK article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules for articles under `pages/gk`.

## Common Format

Many normal GK articles use this front matter shape:

```yaml
---
layout: page
title: （日本語タイトル）
description: （そのページ固有のmeta description）
permalink: /gk/（英語スラッグ）/
tags: [gk, 分類タグ1, 分類タグ2]
gk_section: （既存のGKセクション名）
gk_order: 1
last_modified_at: YYYY-MM-DD
---
```

Existing GK files vary, so preserve existing valid conventions unless the requested change requires a metadata fix.

## Required Rules

- The first line of the file must be `---`.
- Front matter must end with `---` on its own line.
- Do not compress front matter into a single line.
- Do not allow `layout`, `title`, `description`, `permalink`, `tags`, `gk_section`, `gk_order`, or `last_modified_at` to appear as accidental plain text in the body.
- Use `layout: page` unless a nearby GK file for the same article type clearly uses a different layout.
- Use the format `/gk/english-slug/` for `permalink`.
- Always include `gk` in `tags` for GK pages.
- Preserve `gk_section` and `gk_order` when they already exist.
- Do not invent `gk_section` or `gk_order` without checking nearby GK articles and index behavior.
- For new GK articles, include `last_modified_at` in `YYYY-MM-DD` format if the current convention in nearby GK articles supports it.
- Do not blindly add `last_modified_at` to every existing GK article in unrelated tasks.
- When substantially editing the body of an existing GK article that already uses `last_modified_at`, update it when appropriate.
- Do not write visible "last updated" text inside the body.
- Do not guess `prev` / `next`.

## Title

`title` should clearly identify the term and the G検定 context.

Good patterns:

```yaml
title: Transformerとは？Attentionを使う深層学習モデル【G検定対策】
title: ランダムフォレストとは？決定木との違いを整理【G検定】
```

## Description

- Make the description unique to each page.
- Aim for roughly 120-160 Japanese characters.
- Start with a clear definition or role of the concept when possible.
- Explain what the reader can distinguish, judge, or understand after reading.
- Include exam context such as `G検定` only when it fits naturally.
- Avoid keyword stuffing.
- Avoid generic boilerplate endings reused across many pages.
- Do not make the description look like a bullet list.
- Do not contradict the page title or page scope.

## `gk_section` And `gk_order`

`gk_section` and `gk_order` support GK learning paths and indexes.

- Check existing nearby articles before choosing or changing them.
- Keep section names consistent, including Japanese wording and slashes.
- `gk_order` should reflect learning order within the section, not filename order.
- Do not reorder many articles in a rule-writing or single-article task unless explicitly requested.
