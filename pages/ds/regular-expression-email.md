---
layout: page
title: メールアドレスの正規表現とは？なぜ難しいのかを整理【DS検定】
description: "メールアドレスの正規表現を、文字列形式を確認する前処理の例として整理します。完全判定が難しい理由、入力チェックの限界、DS検定での注意点を確認できます。本文では、用語の定義、具体例、似た概念との違い、試験で迷いやすい選択肢の見分け方まで短時間で復習できます。"
permalink: /ds/regular-expression-email/
categories: [data-science]
tags: [ds, data-processing, preprocessing]
ds_area: dataengineering
ds_section: data-processing
prev: /ds/regular-expression-date/
next: /ds/regular-expression-postalcode/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

メールアドレスの正規表現は、**文字列の形式を確認するためのパターン**です。

ただし、正規表現だけで「実在する正しいメールアドレス」まで保証することはできません。

DS検定では、**正規表現で確認できるのは文字列の形であって、実在性ではない**と切り分けることが重要です。

## 直感的な説明

メールアドレスは、例えば次のような形です。

```text
sample@example.com
```

大きく見ると、

```text
ユーザー名 @ ドメイン名
```

という構造になっています。

電話番号や郵便番号より使える文字の種類が多いため、完全な仕様を正規表現だけで表そうとすると複雑になります。

> **判断ポイント：** 正規表現は「それらしい形式か」を確認する道具であり、「そのメールアドレスが実際に使えるか」を確認する道具ではありません。

## 定義・仕組み

簡易的なメールアドレス形式を確認する正規表現の例は次のようになります。

```regex
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```

主な記号の意味を分解すると次の通りです。

| 記号 | 意味 |
|---|---|
| `^` | 文字列の先頭 |
| `[A-Za-z0-9._%+-]` | 指定した文字のいずれか1文字 |
| `+` | 直前のパターンを1回以上繰り返す |
| `@` | `@` そのもの |
| `\.` | ドット `.` そのもの |
| `{2,}` | 直前のパターンを2回以上繰り返す |
| `$` | 文字列の末尾 |

### `.` と `\.` の違い

正規表現では、`.` は**任意の1文字**を表します。

ドットそのものを表したい場合は、`\.` のようにエスケープします。

### `+` と `*` の違い

| 記号 | 繰り返し回数 |
|---|---|
| `+` | 1回以上 |
| `*` | 0回以上 |

ここはMarkdownの装飾記号とも重なるため、記事では必ずコード表記にして読むと安全です。

## どんな場面で使う？

### 使う場面

- 入力フォームの簡易的な形式チェック
- 不正な形式のデータを除外する前処理
- 文字列データの基本的な検証

### 正規表現だけでは判断できないこと

- メールアドレスが実在するか
- 本当にメールを受信できるか
- その人が所有しているアドレスか

実在性を確認したい場合は、確認メールを送るなど別の仕組みが必要です。

## よくある誤解・混同

### ❌ `.` はドットそのものを意味する

正規表現の `.` は任意の1文字です。

ドットそのものは `\.` と書きます。

### ❌ `+` と `*` は同じ

- `+` → 1回以上
- `*` → 0回以上

最低1文字必要かどうかが違います。

### ❌ `[]` は文字列全体を表す

`[A-Za-z]` は、**英字のいずれか1文字**を表します。

### ❌ 正規表現に一致すれば実在するメールアドレス

一致していても、実際に存在するとは限りません。

## まとめ（試験直前用）

- **正規表現 = 文字列パターンの確認**
- `.` = 任意の1文字
- `\.` = ドットそのもの
- `+` = 1回以上
- `*` = 0回以上
- 正規表現だけではメールアドレスの実在性は保証できない

DS検定では、**「形式チェック」と「実在性確認」を分けて考える**と選択肢を切りやすくなります。

## 対応スキル項目（データエンジニアリング力シート）

- データ収集・加工
- データ前処理
- ★ データの前処理（クレンジング・加工）ができる

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>

<div style="margin-top: 16px;">
  🏠 <a href="/ds/">DS検定トップに戻る</a>
</div>

<div style="display:flex;justify-content:space-between;margin-top:12px;">

  {% if page.previous.url %}
    <a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url }}">{{ page.next.title }} →</a>
  {% endif %}

</div>
