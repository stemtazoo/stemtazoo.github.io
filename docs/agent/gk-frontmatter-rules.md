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
- Normal individual GK articles should use `last_modified_at`.
- For new normal GK articles, always include `last_modified_at` in `YYYY-MM-DD` format.
- When meaningfully editing the body, title, description, or reader-facing metadata of an existing normal GK article, update `last_modified_at`.
- If an edited normal GK article does not yet have `last_modified_at`, add it.
- Use the current date at the time of editing.
- Do not write visible "last updated" text inside the body.
- Do not add `last_modified_at` to GK index pages, category pages, generated exports, or non-article files unless the page is clearly a normal reader-facing article.
- Do not mass-add `last_modified_at` to unrelated GK files in a content-editing task.
- Do not change `gk_section` or `gk_order` just because `last_modified_at` is being added.
- Do not guess `prev` / `next`.

## Title

`title` should clearly identify the term and the G検定 context.

Good patterns:

```yaml
title: Transformerとは？Attentionを使う深層学習モデル【G検定対策】
title: ランダムフォレストとは？決定木との違いを整理【G検定】
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
- For GK articles, prioritize descriptions that show how to distinguish the term from similar AI/ML concepts, what exam trap or selection criterion the article helps with, and what role the concept has in machine learning, deep learning, evaluation, optimization, or AI systems.
- Start with a clear definition or role of the concept when possible.
- Include exam context such as `G検定` only when it fits naturally.
- Avoid keyword stuffing.
- Do not make the description look like a bullet list.
- Do not contradict the page title or page scope.

Bad / good examples:

```yaml
# Bad
description: 過学習について初心者向けにわかりやすく解説します。
# Good
description: 過学習を「訓練データに合わせすぎて未知データで精度が落ちる状態」として整理し、汎化・正則化・検証データとの関係をG検定向けに解説します。

# Bad
description: 勾配降下法の基本を整理します。
# Good
description: 勾配降下法を「損失が小さくなる向きへ重みを更新する最適化手法」として整理し、学習率や局所最適に関する選択肢の判断軸を解説します。
```
## `gk_section` And `gk_order`

`gk_section` and `gk_order` support GK learning paths and indexes.

- Check existing nearby articles before choosing or changing them.
- Keep section names consistent, including Japanese wording and slashes.
- `gk_order` should reflect learning order within the section, not filename order.
- Do not reorder many articles in a rule-writing or single-article task unless explicitly requested.
