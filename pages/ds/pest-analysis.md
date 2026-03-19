---
layout: page
title: PEST分析とは？マクロ環境を分析するフレームワーク【DS検定】
permalink: /ds/pest-analysis/
categories: [business]
tags: [ds, design]
prev: /ds/kpi-kgi/
next: /ds/revenue-equation/
---

## まず結論

**PEST分析（PEST Analysis）**とは、企業を取り巻く外部環境を「政治・経済・社会・技術」の4つの視点から分析するフレームワークです。

DS検定では 企業ではなく社会全体の環境（マクロ環境）を分析する手法として問われることが多いです。


試験では特に

SWOT分析

5フォース分析


との 分析対象の違い を判断できるかが重要です。



## 直感的な説明

例えば、電気自動車のビジネスを考えてみます。

成功するかどうかは、企業の努力だけでは決まりません。

例えば次のような社会環境が影響します。

政府が環境規制を強化する

ガソリン価格が高くなる

環境意識が高まる

電池技術が進歩する


このような

企業の外側にある社会環境

を整理して分析するのが PEST分析です。



## 定義・仕組み

PEST分析は次の4つの要因を分析します。

Political（政治）

政治・政策・法律などの影響です。

例

環境規制

税制

政府補助金




Economic（経済）

経済状況が企業活動に与える影響です。

例

景気

為替

金利




Social（社会）

社会や生活者の変化です。

例

人口構造

ライフスタイル

消費者意識




Technological（技術）

技術の進歩による影響です。

例

AI

自動化

新素材




この4つを分析することで

企業に影響を与える社会環境を理解できます。



## どんな場面で使う？

PEST分析は主に次のような場面で使われます。

市場環境の分析

企業が活動する社会環境を整理します。

例

規制

技術革新




新規事業の検討

新しい市場に参入する前に

社会環境

技術トレンド


を確認します。



長期戦略の検討

企業の将来戦略を考えるときに

社会環境の変化を分析します。



## よくある誤解・混同

DS検定では次の分析との違いがよく問われます。

SWOT分析との違い

分析	内容

PEST分析	マクロ環境（社会環境）を分析
SWOT分析	企業の内部と外部を整理


SWOT分析は

企業視点の分析です。



5フォース分析との違い

分析	内容

PEST分析	社会全体の環境を分析
5フォース分析	業界の競争構造を分析


DS検定では

> 政治・経済・社会・技術の環境を分析する



と書かれていたら

PEST分析と判断します。



## まとめ（試験直前用）

PEST分析は マクロ環境を分析するフレームワーク

Political・Economic・Social・Technological

社会環境が企業に与える影響を分析

SWOT分析は 企業視点の分析

5フォース分析は 業界競争の分析


DS検定では

> 「政治・経済・社会・技術」



と書かれていたら

PEST分析と判断するのがポイントです。



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
