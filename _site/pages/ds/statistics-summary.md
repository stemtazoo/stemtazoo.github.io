---
layout: page
title: DS検定でよく出る統計まとめ（平均・分散・相関を一気に整理）
description: DS検定でよく出る統計まとめ（平均・分散・相関を一気に整理）は頻出論点を整理して得点力につなげる学習テーマです。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/statistics-summary/
categories: [data-science]
tags: [ds, statistics]
prev: /ds/statistics-overview/
next: /ds/student-t-test/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

DS検定の統計問題は、次の流れで理解すると整理できます。

1. データの中心  
2. データのばらつき  
3. データ同士の関係  
4. モデルの説明力  
5. 分布の読み取り  

つまり

平均  
↓  
分散・標準偏差  
↓  
共分散・相関係数  
↓  
決定係数  
↓  
箱ひげ図・外れ値  

という構造です。

DS検定では  
**公式よりも「何を表す指標か」を理解しているか**が問われます。


# ① データの中心

まず最初に理解するのが  
**データの代表値**です。

代表的なものは3つです。

- 平均（mean）
- 中央値（median）
- 最頻値（mode）

平均はよく使われますが、

**外れ値の影響を受けやすい**

という特徴があります。

そのためDS検定では

平均  
中央値  

の違いを理解しているかが問われます。


# ② データのばらつき

平均だけではデータの特徴は分かりません。

例えば

平均70点のクラスでも

- 全員70点付近  
- 40点〜100点  

では全く違います。

そこで使うのが

- 分散
- 標準偏差

です。

- 分散 → 平均からどれくらい離れているか  
- 標準偏差 → 分散を元の単位に戻したもの  

詳しくはこちら

→ **[分散と標準偏差とは](/ds/variance-standard-deviation/)**


# ③ データ同士の関係

次に重要なのが

**2つのデータの関係**

です。

例えば

- 気温とアイス売上
- 勉強時間とテスト点数

この関係を表すのが

- 共分散
- 相関係数

です。

相関係数の特徴

- -1〜1の範囲
- 0に近い → 関係が弱い

詳しくはこちら

→ **[共分散と相関係数とは](/ds/covariance-correlation/)**


# ④ モデルの説明力

相関が分かると  
次は **予測モデル**です。

回帰分析では

**決定係数（R²）**

が重要になります。

決定係数は

**モデルがどれくらいデータを説明できるか**

を表します。

例

R² = 0.8

なら、

データのばらつきの8割をモデルで説明できる

と解釈します。

詳しくはこちら

→ **[決定係数とは](/ds/coefficient-of-determination-contribution/)**


# ⑤ 分布の読み取り

最後に重要なのが、

データがどのように分布しているか

を読み取る力です。

DS検定では、

箱ひげ図

外れ値

正規分布


などがよく問われます。

特に箱ひげ図では、

中央値

四分位範囲

外れ値


を読み取れることが重要です。

詳しくはこちら

→ **[箱ひげ図とは](/ds/boxplot/)**


# 試験直前まとめ

DS検定の統計は、

平均 → ばらつき → 関係 → 説明力 → 分布

の順に理解すると整理しやすいです。

それぞれの代表概念は次の通りです。

- 中心：平均・中央値・最頻値
- ばらつき：分散・標準偏差
- 関係：共分散・相関係数
- 説明力：決定係数
- 分布：箱ひげ図・外れ値

公式の暗記だけでなく、

その指標が何を表しているか

を言えるようにしておくと、DS検定で強くなります。

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
