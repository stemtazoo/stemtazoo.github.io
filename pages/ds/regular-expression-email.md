---
layout: page
title: メールアドレスの正規表現とは？なぜ難しいのかを整理【DS検定】
description: メールアドレスの正規表現はなぜ難しいのかを整理するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/regular-expression-email/
categories: [data-science]
tags: [ds, data-processing, preprocessing]
prev: /ds/regular-expression-date/
next: /ds/regular-expression-postalcode/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

---

layout: page
title: メールアドレスの正規表現とは？なぜ難しいのかを整理【DS検定】
permalink: /ds/regular-expression-email/
tags: [ds, preprocessing, cheatsheet]
-------------------------------------

## まず結論

メールアドレスの正規表現は「文字列の構造」を確認するためのパターンですが、完全に正しいメールアドレスを保証することはできません。
DS検定では、「正規表現で何が保証できて、何が保証できないか」を判断できるかが問われます。

---

## 直感的な説明

メールアドレスは、

[sample@example.com](mailto:sample@example.com)

のように

ユーザー名 @ ドメイン名

という構造をしています。

電話番号や郵便番号と違い、

* 英字
* 数字
* 記号

が混ざります。

そのため、正規表現も一気に複雑になります。

ここで大切なのは、

正規表現は「それっぽい形」を確認しているだけ

という理解です。

---

## 定義・仕組み

よくある簡易的なメールアドレスの正規表現は次の形です。

^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$

意味を分解すると、

* ^ ：先頭
* [A-Za-z0-9._%+-]+ ：英数字や一部記号が1回以上
* @ ：アットマーク
* [A-Za-z0-9.-]+ ：ドメイン部分
* \. ：ドット（.）そのもの
* [A-Za-z]{2,} ：2文字以上の英字
* $ ：末尾

ポイントは、

* * は「1回以上」
* [] は「いずれか1文字」
* . はそのままだと「任意の1文字」になるため、\. と書く

という点です。

---

## どんな場面で使う？

### 使う場面

* 入力フォームの形式チェック
* 不正データの簡易除外
* データ前処理での基本確認

### 使うと誤解しやすい場面

* 実在するメールアドレスかどうかを判定できると思う
* RFC仕様まで完全対応していると考える

DS検定では、
「この正規表現で正しいメールアドレスのみを保証できる」と書かれていたら誤りです。

---

## よくある誤解・混同

### ① . の意味を誤解する

. は「任意の1文字」です。

ドットを表すには \. と書く必要があります。

選択肢で「. はドットを意味する」と書かれていたら注意です。

---

### ② + と * の違い

* * ：1回以上
* * ：0回以上

- を使うことで「最低1文字必要」であることを表しています。

---

### ③ [] の意味を誤解する

[A-Za-z] は「英字1文字」を意味します。

「文字列全体が英字」とは限りません。

---

## まとめ（試験直前用）

* メール正規表現は構造チェックである
* . は任意の1文字、ドットは \.
* * は1回以上、* は0回以上
* 正規表現では実在性は保証できない

DS検定では、
「その正規表現が何を保証していないか」を考えることが重要です。

---

## 対応スキル項目（データエンジニアリング力シート）

データ収集・加工

データ前処理

★ データの前処理（クレンジング・加工）ができる

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
