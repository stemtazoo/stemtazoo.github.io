---
layout: page
title: 正規表現のひっかけ総整理（試験直前チートシート）【DS検定】
description: "正規表現を、文字クラス、量指定子、行頭・行末アンカーなどを使って文字列の形式を確認する道具として整理します。任意の1文字とドットそのもの、1回以上と0回以上、部分一致と完全一致を切り分け、形式に一致しても実在性や意味の妥当性までは保証しない点を押さえます。"
permalink: /ds/regular-expression-summary/
categories: [data-science]
tags: [ds, preprocessing]
prev: /ds/regular-expression-postalcode/
next: /ds/stemming-vs-lemmatization/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**正規表現は文字列の「形式」を確認する道具であり、内容の意味や実在性までは保証しません。**

DS検定では、記号の意味だけでなく、**その正規表現が何を保証していないか**まで判断できることが重要です。

## 直感的な説明

電話番号・郵便番号・日付・メールアドレスには、それぞれ「それらしい形」があります。

正規表現が見ているのは、その**文字の並び方**です。

例えば、`2026-99-99` が日付形式の正規表現に一致しても、実在する日付とは限りません。

つまり、

- 正規表現 → **形を確認**
- 範囲チェックやDB照合 → **意味・実在性を確認**

と切り分けます。

## 定義・仕組み

### よく出る記号

| 記号 | 意味 |
|---|---|
| `^` | 文字列の先頭 |
| `$` | 文字列の末尾 |
| `.` | 任意の1文字 |
| `\.` | ドット `.` そのもの |
| `\d` | 数字1文字 |
| `{n}` | ちょうどn回 |
| `{n,}` | n回以上 |
| `?` | 0回または1回 |
| `+` | 1回以上 |
| `*` | 0回以上 |
| `[]` | 角括弧内のいずれか1文字 |

### `+` と `*` の違い

| 記号 | 最小回数 |
|---|---:|
| `+` | 1回 |
| `*` | 0回 |

**0回を許すかどうか**が判断ポイントです。

### 部分一致と完全一致

完全一致を意図する場合は、一般に先頭の `^` と末尾の `$` を確認します。

```text
^ ... $
```

## どんな場面で使う？

### 使う場面

- 入力値の形式チェック
- ログから特定パターンを抽出
- データ前処理
- 明らかに形式が異なるデータの除外

### 正規表現だけでは不十分な場面

- 実在するメールアドレスか確認する
- 日付がカレンダー上で正しいか確認する
- 郵便番号が実在するか確認する

## よくある誤解・混同

### ❌ `.` はドットそのもの

`.` は任意の1文字です。ドットそのものを表すなら `\.` とします。

### ❌ `+` と `*` は同じ

`+` は1回以上、`*` は0回以上です。

### ❌ 形式に一致すれば内容も正しい

正規表現は形式を確認します。意味の妥当性や実在性は別のチェックが必要です。

### ❌ `^` と `$` がなくても常に完全一致

検索方法にもよりますが、試験では**完全一致を意図しているなら先頭・末尾の指定を確認する**と判断しやすくなります。

## まとめ（試験直前用）

- **正規表現 = 形式チェック**
- `.` = 任意の1文字 / `\.` = ドットそのもの
- `+` = 1回以上 / `*` = 0回以上
- 完全一致では `^` と `$` を確認
- **形式の一致 ≠ 意味や実在性の保証**

DS検定では、「何に一致するか」だけでなく、**何までは保証できないか**を見ると選択肢を切りやすくなります。

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
      {% if p.tags contains tag and tag != "ds" %}{% assign matched = true %}{% endif %}
    {% endfor %}
    {% if matched %}
      <li style="margin-bottom: 6px;"><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% assign count = count | plus: 1 %}
    {% endif %}
    {% if count >= 5 %}{% break %}{% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>
<div style="margin-top: 16px;">🏠 <a href="/ds/">DS検定トップに戻る</a></div>
<div style="display:flex;justify-content:space-between;margin-top:12px;">
  {% if page.previous.url %}<a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>{% endif %}
  {% if page.next.url %}<a href="{{ page.next.url }}">{{ page.next.title }} →</a>{% endif %}
</div>
