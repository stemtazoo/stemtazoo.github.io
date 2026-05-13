# SG Front Matter Rules

SG通常記事の front matter は、必ず次の形式にします。

```yaml
---
layout: page
title: （日本語タイトル）
description: （そのページ固有のmeta description）
permalink: /sg/（英語スラッグ）/
tags: [sg, 分類タグ1, 分類タグ2]
last_modified_at: YYYY-MM-DD
---
```

## 必須ルール

- ファイルの1行目は必ず `---` から開始する。
- front matter の前に空行、文字、不可視文字を入れない。
- `layout: page` を使う。
- `description` を必ず入れる。
- `permalink` は `/sg/英語スラッグ/` の形式にする。
- `tags` は必ず YAML の配列形式 `tags: [sg, xxx, yyy]` にする。
- `last_modified_at` を必ず `YYYY-MM-DD` 形式で入れる。
- 新規記事では、作成日を `last_modified_at` に入れる。
- 既存記事の本文を修正した場合は、必要に応じて `last_modified_at` を更新する。
- 本文中には「最終更新日」を書かない。
- `prev` / `next` は原則入れない。
- ユーザーが前後記事を指定した場合のみ `prev` / `next` を追加する。
- 不明な前後記事を推測して入れない。

## Title

`title` は、検索結果やサイト内リンクで意味が伝わるようにします。

```yaml
title: Cookieとは？HTTPヘッダで扱う状態管理の基本【SG試験】
title: リスクアセスメントの手順をやさしく整理【情報セキュリティマネジメント】
```

## Description

- 1ページごとに固有の内容にする。
- 100〜140文字程度を目安にする。
- 書き出しは「〇〇は〜です。」のように、その用語の一言定義から始める。
- 何がわかる記事かが自然に伝わるようにする。
- 「SG試験」「情報セキュリティマネジメント」「ひっかけポイント」「試験対策」などは、不自然にならない範囲で入れる。
- 末尾の定型文を使い回さない。
- 箇条書き風にしない。
- `title` と矛盾させない。
