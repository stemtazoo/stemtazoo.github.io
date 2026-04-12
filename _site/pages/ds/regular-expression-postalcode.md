---
layout: page
title: 郵便番号の正規表現とは？電話番号との違いで理解する【DS検定】
description: 郵便番号の正規表現は電話番号との違いで理解するを理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/regular-expression-postalcode/
categories: [data-science]
tags: [ds, data-processing, preprocessing]
prev: /ds/regular-expression-email/
next: /ds/regular-expression-summary/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>


## まず結論

正規表現は「文字列の形式」を確認する道具であり、「意味の正しさ」までは保証しません。
DS検定では、“何を保証していて、何を保証していないか”を判断できるかが問われます。

---

## 直感的な説明

これまで、

* 電話番号
* 郵便番号
* 日付
* メールアドレス

を通して学んできました。

共通しているのは、

正規表現は「形」を見ているだけ

ということです。

実務でも、正規表現は入力チェックやデータ前処理で使われますが、
「妥当性」や「実在性」までは確認しません。

DS検定では、この“限界”を理解しているかどうかが重要です。

---

## 定義・仕組み

ここで、よく出る記号を整理します。

* ^ ：先頭
* $ ：末尾
* . ：任意の1文字
* \. ：ドットそのもの
* \d ：数字1文字
* {n} ：ちょうどn回
* {n,} ：n回以上
* ? ：0回または1回
* * ：1回以上
* * ：0回以上
* [] ：いずれか1文字

重要なのは、

記号の意味を“日本語で説明できるか”どうかです。

DS検定では「この記号の意味として正しいものはどれか」と問われることがあります。

---

## どんな場面で使う？

### 使う場面

* 入力値の形式チェック
* ログデータ抽出
* データ前処理
* 不正データの除外

### 使うと誤解しやすい場面

* 正しい日付のみを抽出できると思う
* 実在するメールアドレスだけを抽出できると思う
* 完全一致かどうかを確認していない

DS検定では、
「完全一致である」と書かれていたら ^ と $ を探します。

---

## よくある誤解・混同

### ① . を数字だと誤解する

. は「任意の1文字」です。

---

### ② 形式＝妥当性だと誤解する

正規表現は範囲チェックまでは保証しません。

---

### ③ + と * の違いを曖昧にする

* * ：1回以上
* * ：0回以上

0回を許すかどうかは重要な違いです。

---

### ④ ^ と $ を見落とす

これが最も多いひっかけです。

部分一致と完全一致の違いを必ず確認します。

---

## まとめ（試験直前用）

* 正規表現は「形式チェック」
* 形式と妥当性は別
* . は任意の1文字
* * と * の違いを区別する
* 完全一致かどうかは ^ と $ を見る

DS検定では、
「その正規表現は何を保証していないか？」を考えると正解に近づきます。

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
