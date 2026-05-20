# SG Front Matter Rules

This file is written in English for Codex readability. However, SG article content must be written in Japanese unless the user explicitly requests otherwise.

Use the following front matter format for normal SG articles.

```yaml
---
layout: page
title: （日本語タイトル）
description: （そのページ固有のmeta description）
permalink: /sg/（英語スラッグ）/
tags: [sg, 分類タグ1, 分類タグ2]
date: YYYY-MM-DD
last_modified_at: YYYY-MM-DD
---
```

## Required Rules

- The first line of the file must be `---`.

- Front matter must end with `---` on its own line.
- Do not compress front matter into a single line.
- Do not allow `layout`, `title`, `description`, `permalink`, `tags`, `date`, or `last_modified_at` to appear as accidental plain text in the article body.
- `description` is metadata. Do not duplicate the same sentence in visible body text unless intentionally rewritten for the introduction.
- `tags` is metadata. Do not print tags as a plain-text line in the article body.
- Do not put blank lines, characters, or invisible characters before front matter.
- Use `layout: page`.
- Always include `description`.
- Use the format `/sg/英語スラッグ/` for `permalink`.
- Always write `tags` as a YAML array, such as `tags: [sg, xxx, yyy]`.
- Always include `last_modified_at` in `YYYY-MM-DD` format.
- For new articles, use the creation date as `last_modified_at`.
- When editing the body of an existing article, update `last_modified_at` when appropriate.
- Do not write "last updated" text inside the body.
- As a rule, do not add `prev` / `next`.
- Add `prev` / `next` only when the user explicitly specifies the previous and next articles.
- Do not guess unknown previous or next articles.

## Title

`title` should make the page meaning clear in search results and internal links.

```yaml
title: Cookieとは？HTTPヘッダで扱う状態管理の基本【SG試験】
title: リスクアセスメントの手順をやさしく整理【情報セキュリティマネジメント】
```

## Description

- Make the description unique to each page.
- Aim for roughly 100-140 Japanese characters.
- Start with a one-sentence definition of the term, such as `〇〇は〜です。`.
- Make it clear what the reader will learn from the article.
- Include terms such as `SG試験`, `情報セキュリティマネジメント`, `ひっかけポイント`, or `試験対策` only when they fit naturally.
- Do not reuse the same boilerplate ending across pages.
- Do not make it look like a bullet list.
- Do not contradict `title`.
