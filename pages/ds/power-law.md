---
layout: page
title: べき乗則とは？両対数グラフが直線になる理由【DS検定リテラシー】
description: "べき乗則とは、ある量が別の量のべき乗に比例する関係です。両対数グラフで直線になる理由を押さえ、指数成長との違いを整理します。DS検定では『両対数か片対数か』『xのべき乗か一定割合の増加か』で選択肢を切り分けます。"
permalink: /ds/power-law/
image:
  path: https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/ds/power-law.png
  width: 1200
  height: 630
  alt: "べき乗則の例として、通常のグラフでは曲線、両対数グラフでは直線になる関係を比較した図"
categories: [business]
tags: [ds, design]
ds_area: datascience
ds_section: statistics
prev: /ds/polymorphism/
next: /ds/primary-data/
last_modified_at: 2026-11-21
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

<figure style="margin:16px 0 20px;">
  <picture>
    <source media="(max-width: 640px)" srcset="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/ds/power-law-mobile.png" width="1122" height="1402">
    <img src="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/ds/power-law.png" width="1200" height="630" alt="べき乗則の例。通常のグラフでは右上がりの曲線、両対数グラフでは直線になることを比較" loading="lazy" decoding="async" style="display:block;width:100%;max-width:100%;height:auto;">
  </picture>
  <figcaption style="font-size:0.88em;line-height:1.5;color:#606b75;margin-top:8px;">べき乗則の例：同じ関係を異なる目盛りで表したグラフ。</figcaption>
</figure>

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

## 確認問題：片対数と両対数を見分ける

次の関係をグラフにするとき、**直線になりやすい目盛り**を考えてみましょう。

- **問題A**：\(y=3x^2\) は、片対数グラフと両対数グラフのどちらで直線になりますか？
- **問題B**：\(y=3\times 2^x\) は、片対数グラフと両対数グラフのどちらで直線になりますか？

答えを見る前に、**「指数がついているのは x か、それとも定数 2 か」**を確かめると区別できます。

<details markdown="1">
<summary>▶ 答えと解説を確認する</summary>

**問題A：両対数グラフ**です。\(y=3x^2\) は \(y=ax^b\) のべき乗則で、横軸と縦軸をともに対数にすると直線になります。

**問題B：片対数グラフ**です。\(y=3\times 2^x\) は指数関数の形で、縦軸を対数、横軸を通常目盛りにすると直線になります。

迷ったら次のように確認します。

- \(x^2\) のように **x 自体をべき乗**する → **両対数**
- \(2^x\) のように **x が指数**に入る → **片対数**

</details>

## まとめ（試験直前用）

- べき乗則＝**$y=ax^b$ の形**
- 両対数グラフで直線になる
- 指数関数的な関係は片対数で直線になりやすい
- 「一定割合で増える」なら指数側を疑う
- 「xのべき乗に比例」ならべき乗則

DS検定では、**「両対数か？片対数か？」**でまず切り分けると整理しやすくなります。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：基礎技術
- **スキルカテゴリ**：科学的解析の基礎
- **サブカテゴリ**：統計数理基礎
- **必須スキル**：◯
- ★ 指数関数とlog関数の関係を理解し、片対数グラフ、両対数グラフ、対数化されていないグラフを適切に使いわけることができる
- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)
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
