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

When creating or revising the `description` field in front matter:

- Do not use boilerplate descriptions that could fit any article.
- Avoid generic phrases such as `初心者向けにわかりやすく解説します`, `基本から整理します`, `試験対策として重要なポイントを解説します`, or `この記事では〜について説明します`.
- The description must summarize the article-specific learning value.
- Include at least one concrete element from the article, such as the main judgment criterion, a common misunderstanding, a distinction from a similar term, a typical exam trap, a practical use case, or the type of question where the concept appears.
- Prefer roughly 120-160 Japanese characters when natural, especially for pages that were previously flagged for short descriptions. Do not simply lengthen the description by adding filler.
- Do not repeat the title with minor wording changes.
- Make each description unique enough that it could not be reused for another article without editing.
- For SG articles, prioritize descriptions that show what business/security judgment the reader will be able to make, what confusing term or exam trap the article helps distinguish, and how the concept appears in SG-style questions.
- Start with a clear definition or role of the concept when possible.
- Explain what the reader can distinguish, judge, or understand after reading.
- Include exam context such as `SG試験` or `情報セキュリティマネジメント` only when it fits naturally.
- Avoid keyword stuffing.
- Do not make the description look like a bullet list.
- Do not contradict the page title or page scope.

Bad / good examples:

```yaml
# Bad
description: アクセス制御について初心者向けにわかりやすく解説します。
# Good
description: アクセス権限を「誰に・何を・どこまで許すか」で整理し、認証・認可・最小権限との混同を防ぐ判断基準を解説します。

# Bad
description: SQLインジェクションの基本と対策を整理します。
# Good
description: SQLインジェクションを「入力値がSQL文として実行される攻撃」として整理し、XSSとの違いとSG・FE試験での選択肢の切り方を解説します。
```
