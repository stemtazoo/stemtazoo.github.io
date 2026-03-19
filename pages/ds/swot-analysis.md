---
layout: page
title: SWOT分析とは？企業の強みと外部環境を整理するフレームワーク【DS検定】
permalink: /ds/swot-analysis/
categories: [business]
tags: [ds, design]
prev: /ds/rfm-analysis/
next: /ds/bcp/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**SWOT分析（SWOT Analysis）**とは、企業や事業の状況を「強み・弱み・機会・脅威」の4つの視点で整理するフレームワークです。

DS検定では 企業の戦略を考えるための基本的なビジネスフレームワークとして出題されます。


DS検定では特に

5フォース分析

PEST分析


との 分析対象の違い を判断できるかが重要です。



## 直感的な説明

例えば、新しいサービスを始めるとします。

そのとき次のようなことを考えます。

自社の強みは何か

自社の弱みは何か

市場のチャンスはあるか

競争や規制のリスクはあるか


これらを整理すると

どの戦略を取るべきか

が見えてきます。

このように

企業の内部と外部の状況を整理する方法

が SWOT分析 です。



## 定義・仕組み

SWOT分析は次の4つの要素で構成されます。

Strength（強み）

企業の内部にある 優れている点 です。

例

ブランド力

技術力

コスト競争力




Weakness（弱み）

企業の内部にある 改善すべき点 です。

例

知名度が低い

資金力が弱い




Opportunity（機会）

企業の外部環境にある ビジネスチャンス です。

例

市場の成長

新しい技術の登場




Threat（脅威）

企業の外部環境にある リスク要因 です。

例

競争の激化

法規制の強化




このように

内部要因

外部要因


を整理することで

戦略立案に役立てることができます。



## どんな場面で使う？

SWOT分析は主に次のような場面で使われます。

事業戦略の立案

企業の状況を整理して

強みを活かす戦略

弱みを補う戦略


を考えます。



新規事業の検討

市場機会とリスクを整理して

参入するべきか

どのように参入するか


を判断します。



マーケティング戦略

企業の立ち位置を理解し

ターゲット市場

競争戦略


を決めるときに使われます。



## よくある誤解・混同

DS検定では次の分析との違いがよく問われます。

5フォース分析との違い

分析	内容

SWOT分析	企業の内部と外部環境を整理
5フォース分析	業界の競争構造を分析


5フォース分析は

業界の競争環境を分析する手法です。



PEST分析との違い

分析	内容

SWOT分析	企業視点で内部・外部を整理
PEST分析	マクロ環境を分析


PEST分析は

政治

経済

社会

技術


などの 外部環境分析です。



## まとめ（試験直前用）

SWOT分析は 企業の内部と外部環境を整理するフレームワーク

Strength・Weakness・Opportunity・Threat

内部要因と外部要因を整理する

5フォース分析は 業界の競争環境

PEST分析は マクロ環境分析


DS検定では

> 「企業の強み・弱み・機会・脅威を整理する」



と書かれていたら

SWOT分析と判断するのがポイントです。



【対応スキル項目（ビジネス力シート）】

ビジネス理解

ビジネスフレームワーク

★ ビジネス課題を整理するための基本的なフレームワークを理解している

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
