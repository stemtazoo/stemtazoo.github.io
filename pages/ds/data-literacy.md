---
layout: page
title: データリテラシーとは？データを読み解く力【DS検定】
permalink: /ds/data-literacy/
categories: [business]
tags: [ds, design]
next: /ds/data-literacy-practice/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**データリテラシー（Data Literacy）**とは、データを理解し、正しく読み取り、意思決定に活用する能力のことです。

DS検定では データ社会で必要な基本的な能力として重要な概念です。


ポイントは

> データを「見る」だけでなく「正しく解釈して判断する」こと



です。



## 直感的な説明

例えば売上データを見たときに

売上が増えている理由は何か

季節要因なのか

新しい施策の効果なのか


を考える力が必要です。

ただ数字を見るだけではなく

データの意味

背景

偏り


を理解して判断する能力が データリテラシー です。



## 定義・仕組み

データリテラシーには次のような能力が含まれます。

データ理解

グラフ

統計

指標


などを読み取る能力。



データ分析

データを使って

傾向

パターン


を見つける能力。



批判的思考

データをそのまま信じるのではなく

バイアス

誤解


がないかを考える能力。



意思決定

データを使って

経営判断

業務改善


を行う能力。



## どんな場面で使う？

ビジネス

企業では

売上データ

顧客データ


をもとに意思決定が行われます。



データ分析

データサイエンスでは

統計

機械学習


を理解するための基礎能力です。



社会

データ社会では

フェイク情報

誤解を招くグラフ


を見抜く力も重要です。



## よくある誤解・混同

ITスキルとの違い

概念	内容

ITスキル	ツールを使う能力
データリテラシー	データを理解し判断する能力


つまり

ツールが使えるだけでは

データリテラシーとは言えません。



データサイエンスとの違い

概念	内容

データリテラシー	データを理解する基礎能力
データサイエンス	高度な分析手法




## まとめ（試験直前用）

データリテラシーは データを理解し判断する能力

データ理解

データ分析

批判的思考

意思決定


などの能力を含む。

DS検定では

> 「データを理解し、意思決定に活用する能力」



と書かれていたら

データリテラシーと判断するのがポイントです。



【対応スキル項目（ビジネス力シート）】

ビジネス理解

データ活用

★ データに基づく意思決定を理解している

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
