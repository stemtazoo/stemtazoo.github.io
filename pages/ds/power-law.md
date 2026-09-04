---
layout: page
title: べき乗則とは？両対数グラフが直線になる理由【DS検定リテラシー】
description: "べき乗則とは、ある量が別の量のべき乗に比例する関係です。両対数グラフで直線になる理由を押さえ、指数成長との違いを整理します。DS検定では『両対数か片対数か』『xのべき乗か一定割合の増加か』で選択肢を切り分けます。"
permalink: /ds/power-law/
categories: [business]
tags: [ds, design]
ds_area: datascience
ds_section: statistics
prev: /ds/polymorphism/
next: /ds/primary-data/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**べき乗則とは、ある量が別の量のべき乗に比例する関係**です。

DS検定では、次の切り分けが重要です。

| 関係 | 直線になりやすいグラフ |
|---|---|
| べき乗則 | 両対数グラフ |
| 指数関数的な関係 | 片対数グラフ |

つまり、**「両対数で直線」ならべき乗則を疑う**のが基本です。

## 直感的な説明

べき乗則は、単純な「毎回10%ずつ増える」といった一定割合の増加とは異なります。

例えば、

- 都市規模と一部の都市指標
- ネットワーク上の接続数
- 所得やアクセス数などで大きな偏りが見られるデータ

などでは、ある量が別の量のべき乗に比例する関係が現れることがあります。

普通のグラフでは曲線に見えても、横軸と縦軸の両方を対数にすると直線になることがあります。

## 定義・仕組み

べき乗則は、次の形で表せます。

$$
y = a x^b
$$

両辺の対数を取ると、

$$
\log y = \log a + b \log x
$$

となります。

これは、

- 横軸：$\log x$
- 縦軸：$\log y$

としたとき、**傾き $b$ の直線**になる形です。

### 数値例

例えば $y=x^2$ なら、次のようになります。

| x | y |
|---:|---:|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |

通常のグラフでは曲線ですが、両対数グラフでは直線関係になります。

## どんな場面で使う？

べき乗則は、**一部の値が非常に大きく、分布に強い偏りがある現象**を理解するときに登場します。

例として、

- ネットワークの次数分布
- 都市規模に関する一部の指標
- 所得・資産などの裾の分布
- Webアクセスや人気度の分布

などがあります。

ただし、データが偏っているだけで必ずべき乗則とは限りません。実際にはグラフやモデル適合を確認する必要があります。

## よくある誤解・混同

### ❌ べき乗則と指数成長は同じ

異なります。

| 観点 | べき乗則 | 指数関数的な関係 |
|---|---|---|
| 基本形 | $y=ax^b$ | $y=ab^x$ など |
| 直線化 | 両対数 | 片対数 |
| 判断語 | xのべき乗、スケール則 | 一定割合、倍々、複利的増加 |

### ❌ 大きいものほど大きくなる現象はすべてべき乗則

そうとは限りません。

「偏りが大きい」「一部だけ極端に大きい」という見た目だけでは、べき乗則とは断定できません。

### ❌ 両対数グラフでほぼ直線なら、それだけでべき乗則が証明できる

両対数グラフは重要な手掛かりですが、実データでは別の分布でも似た形になることがあります。DS検定では基本的な見分け方として使い、実務では追加の検証が必要です。

## まとめ（試験直前用）

- べき乗則＝**$y=ax^b$ の形**
- 両対数グラフで直線になる
- 指数関数的な関係は片対数で直線になりやすい
- 「一定割合で増える」なら指数側を疑う
- 「xのべき乗に比例」ならべき乗則

DS検定では、**「両対数か？片対数か？」**でまず切り分けると整理しやすくなります。

## 対応スキル項目（データサイエンス力シート）
- データの理解
- データの可視化
- ★ データの特徴を適切なグラフで表現できる
- ★ データの分布や関係性を読み取ることができる

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
