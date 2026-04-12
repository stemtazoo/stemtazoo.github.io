---
layout: page
title: 相関係数と決定係数の違いとは？回帰分析の基本を理解する【DS検定】
description: 相関係数と決定係数の違いは関連概念を切り分けるための考え方です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/correlation-coefficient-determination/
categories: [data-science]
tags: [ds, statistics]
prev: /ds/correlation-and-causation/
next: /ds/correlation-vs-causation/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

相関係数は「2つのデータの関係の強さ」を表し、決定係数は「その関係でどれくらい説明できるか」を表す指標です。

DS検定では

相関係数と決定係数の違い

決定係数の意味


を理解しているかが問われます。

特に

決定係数 = 相関係数²（単回帰の場合）

という関係はよく出題されます。



## 直感的な説明

例えば

勉強時間	テスト点数

1時間	50
2時間	60
3時間	70


のようなデータがあるとします。

この場合

勉強時間が増えるほど点数も上がる

という関係があります。

このとき

どれくらい強く関係しているか


を見るのが

相関係数です。

一方で

この関係を使って

点数を予測するモデル

を作ったとき

どれくらいデータを説明できているか


を見る指標が

決定係数です。



## 定義・仕組み

相関係数

相関係数は

2つのデータの直線的な関係の強さ

を表します。

特徴

値の範囲： -1 〜 1


値	意味

1	完全な正の相関
0	相関なし
-1	完全な負の相関


例えば

気温とアイス売上 → 正の相関

気温と暖房使用量 → 負の相関


になります。



決定係数

決定係数は

回帰モデルがどれくらいデータを説明できているか

を表します。

値の範囲

0 〜 1


意味

値	意味

1	完全に説明できる
0	説明できない


例えば

決定係数 = 0.64

の場合

データのばらつきの64%を説明できている

という意味になります。



相関係数との関係

単回帰では

決定係数 = 相関係数²

という関係があります。

例えば

相関係数 = 0.8

なら

決定係数 = 0.64

になります。

DS検定ではこの関係がよく出題されます。



## どんな場面で使う？

相関係数は

データ同士の関係があるか

を確認するときに使います。

例えば

広告費と売上

勉強時間とテスト点数


などです。

一方で決定係数は

回帰モデルの評価

で使われます。

例えば

売上予測モデル

需要予測


などです。



## よくある誤解・混同

相関が高い＝予測できる

これは誤解です。

相関が高くても

外れ値

説明変数不足


などの理由で

予測が当たらないことがあります。



相関係数0＝関係なし

相関係数は

直線関係

しか測れません。

例えば

y = x²

のような関係では

相関係数が0になることがあります。

DS検定では

相関係数0は「直線関係がない」ことを意味する

という理解が重要です。



## まとめ（試験直前用）

相関係数と決定係数は次のように整理できます。

相関係数 → 関係の強さ

決定係数 → モデルの説明力


覚えるポイント

相関係数の範囲は -1〜1

決定係数の範囲は 0〜1

単回帰では


決定係数 = 相関係数²

DS検定では

相関の意味と決定係数の意味を区別できるか

がよく問われます。



## 対応スキル項目（データサイエンス力シート）

スキルカテゴリ名 データサイエンス基礎

サブカテゴリ名 統計数理基礎

★ 相関や回帰など、複数の変数間の関係性を理解し説明できる

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
