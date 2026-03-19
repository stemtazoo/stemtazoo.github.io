---
layout: page
title: 郵便番号の正規表現とは？電話番号との違いで理解する【DS検定】
permalink: /ds/regular-expression-postalcode/
categories: [data-science]
tags: [ds, preprocessing]
prev: /ds/regular-expression-email/
next: /ds/regular-expression-summary/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

郵便番号の正規表現は「3桁-4桁」という形式を表現するパターンです。
DS検定では、電話番号との違いを理解しながら「完全一致かどうか」を判断できるかが問われます。



## 直感的な説明

郵便番号は、例として
123-4567
のような形をしています。

実はこの形式は、前回学んだ電話番号（市内番号形式）と同じ構造です。

ここで重要なのは、

「同じ形でも、用途が違う」

という点です。

正規表現は意味ではなく“形”だけを見ています。

DS検定では、
「この正規表現は郵便番号を完全に表しているか？」
といった形で問われることがあります。



## 定義・仕組み

代表的な郵便番号の正規表現は次の形です。

^\d{3}-\d{4}$

意味は次の通りです。

^ ：先頭から始まる

\d{3} ：数字3桁

：ハイフン


\d{4} ：数字4桁

$ ：末尾で終わる


つまり、

「数字3桁-数字4桁で構成された文字列全体」

を表しています。

ここでのポイントは、

正規表現は“数字であること”しか見ていない

実在する郵便番号かどうかまでは判定しない


という点です。



## どんな場面で使う？

使う場面

Webフォームでの入力チェック

データ前処理での形式確認

不正データの除外


使うと誤解しやすい場面

ハイフンなし（1234567）も許可するかどうか

部分一致を許してしまうケース


たとえば、

\d{3}-\d{4}

だけだと、文字列の途中に含まれていても一致します。

DS検定では「完全一致している」と説明されていたら、^ と $ があるかを確認します。



## よくある誤解・混同

① 電話番号との混同

形は同じでも、意味は別です。

正規表現は意味を理解しているわけではありません。

選択肢で
「電話番号専用の正規表現である」
と書かれていたら誤りです。



② ハイフンの有無

次のように書くこともあります。

^\d{3}-?\d{4}$

? は「0回または1回」


これで、

123-4567
1234567

の両方に一致できます。



③ 形式が合えば正しい郵便番号だと思い込む

正規表現で確認できるのは、

あくまで文字列の形

だけです。

存在しない郵便番号でも、形式が合えば一致します。



## まとめ（試験直前用）

郵便番号の基本形は `^\d{3}-\d{4}$`

^ と $ があると完全一致になる

`?` を使うとハイフンあり・なし両方を許可できる

正規表現は「形」を判定するもので、「実在性」は判定しない

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
