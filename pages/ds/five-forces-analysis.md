---
layout: page
title: 5フォース分析とは？業界の競争環境を分析するフレームワーク【DS検定】
permalink: /ds/five-forces-analysis/
categories: [business]
tags: [ds, design]
prev: /ds/customer-journey/
next: /ds/kpi-kgi/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**5フォース分析（Five Forces Analysis）**とは、業界の競争環境を5つの要因から分析するフレームワークです。

DS検定では「企業ではなく業界の競争構造を分析する手法」として出題されることが多いです。


特に試験では

顧客分析

マーケティング分析


と混同させる問題が出るため、分析対象が「業界」であることを理解しておくことが重要です。



## 直感的な説明

例えば、ある新しいカフェを開業しようと考えたとします。

そのとき重要なのは

競合のカフェは多いか

新しい店が参入しやすいか

原材料の仕入れ価格は上がりやすいか

お客さんは別の店に簡単に乗り換えるか

コンビニコーヒーのような代替サービスがあるか


といった 業界の競争の強さです。

このような

業界の競争環境を体系的に分析する方法が

5フォース分析です。



## 定義・仕組み

5フォース分析は、経営学者の マイケル・ポーター が提唱した分析フレームワークです。

企業を取り巻く競争環境を次の 5つの要因（フォース） で分析します。

1 既存企業間の競争

同じ業界の企業同士の競争の激しさです。

例

多くの企業が存在する

価格競争が激しい




2 新規参入の脅威

新しい企業が市場に参入しやすいかどうかです。

例

開業コストが低い

規制が少ない




3 代替品の脅威

別の製品やサービスに置き換えられる可能性です。

例

映画館 → 動画配信サービス




4 買い手の交渉力

顧客が価格や条件を交渉できる力です。

例

顧客の選択肢が多い




5 売り手の交渉力

仕入れ先が価格などをコントロールできる力です。

例

特定の仕入れ先しかない




この5つを分析することで

業界の収益性や競争の強さを理解できます。



## どんな場面で使う？

5フォース分析は主に次のような場面で使われます。

新規事業の検討

新しい市場に参入する前に

競争の激しさ

利益が出る可能性


を分析します。



事業戦略の立案

企業の競争戦略を考えるときに使われます。

例

価格戦略

差別化戦略




市場分析

業界全体の構造を理解するために使われます。



## よくある誤解・混同

DS検定では次のような誤解を狙った問題がよく出ます。

顧客分析と混同

誤り例

> 顧客の5つの競争要因を分析する



これは誤りです。

5フォース分析は

顧客ではなく業界の競争構造を分析する手法です。



データ分析手法と混同

分析	内容

5フォース分析	業界の競争環境を分析
クラスタ分析	データのグループ分け
アソシエーション分析	事象の関連性分析


DS検定では

> 業界の競争環境を分析する



と書かれていたら

5フォース分析と判断します。



## まとめ（試験直前用）

5フォース分析は 業界の競争環境を分析するフレームワーク

競争構造を 5つの要因で分析する

新規参入・代替品・競争・買い手・売り手

顧客分析ではない点が試験の重要ポイント


DS検定では

> 「業界の競争環境を分析する」



と書かれていたら

5フォース分析と判断するのがポイントです。



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
