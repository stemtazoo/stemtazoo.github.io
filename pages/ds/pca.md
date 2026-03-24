---
layout: page
title: 主成分分析（PCA）とは？次元削減の基本をわかりやすく整理【DS検定】
permalink: /ds/pca/
categories: [data-science]
tags: [ds, linear-algebra, math]
prev: /ds/matrix-multiplication/
next: /ds/vector-dot-product/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**主成分分析（PCA：Principal Component Analysis）**とは、
多くの特徴量を、情報をできるだけ保ちながら少ない次元にまとめる「次元削減」の手法です。

DS検定では、

次元の呪いの対策として使われる

多くの変数を少数の「主成分」にまとめる


という理解ができているかが問われます。



## 直感的な説明

例えば、次のようなデータを考えます。

身長	体重

170	65
175	70
180	75


このデータを見ると

身長が高い人ほど体重も重い

という関係があります。

つまり

身長

体重


の2つの情報は かなり似た情報 を持っています。

主成分分析は、

> この2つを別々に扱うのではなく
「体格」という1つの軸にまとめよう



と考える方法です。

つまり

2次元データ
→ 1次元にまとめる

これが 次元削減です。



## 定義・仕組み

主成分分析は、

データのばらつき（分散）が大きい方向を見つけて、新しい軸を作る方法です。

少しイメージしてみます。

元のデータ

身長 →
体重 ↑

このように2軸があります。

しかしデータの点が細長く並んでいる場合、

その伸びている方向に新しい軸を取り直すと、

データの特徴を少ない軸で表しやすくなります。

この「もっともばらつきが大きい方向」が第1主成分です。

さらに、

第1主成分と直交しつつ、次にばらつきが大きい方向

を第2主成分と呼びます。

つまりPCAは、

元の変数そのものを見るのではなく、

データの情報をよく表す新しい軸へ変換する方法

です。



## どんな場面で使う？

PCAは次のような場面で使われます。

特徴量が多すぎるとき

可視化したいとき

ノイズを減らしたいとき


例えば

アンケート項目が多いデータ

画像の高次元データ

センサーの多変量データ


などで使われます。

DS検定では、

次元の呪いへの対策

可視化のための次元削減


として理解しておくことが重要です。



## よくある誤解・混同

混同①：PCAは重要な変数を選ぶ方法

PCAは変数を選ぶというより、

複数の変数を組み合わせて新しい軸を作る方法

です。



混同②：主成分は元の変数と同じ意味を持つ

主成分は元の変数の線形結合なので、

「身長」や「体重」のようにそのまま解釈できるとは限りません。



混同③：次元を減らしても情報は完全に同じ

次元削減では、

情報をできるだけ保つ

ことを目指しますが、

一部の情報は失われる可能性があります。



## まとめ（試験直前用）

PCA＝主成分分析＝次元削減の代表手法

分散が大きい方向に新しい軸を作る

第1主成分が最も情報をよく表す

多変量データの可視化や次元の呪い対策で使う



## 対応スキル項目（データサイエンス力）

数理・統計基礎

多変量解析

★ 高次元データを少ない軸で表現する考え方を理解できる

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
