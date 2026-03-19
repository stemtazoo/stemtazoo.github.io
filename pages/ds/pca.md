---
layout: page
title: 主成分分析（PCA）とは？次元削減の基本をわかりやすく整理【DS検定】
permalink: /ds/pca/
categories: [data-science]
tags: [ds, math]
prev: /ds/matrix-multiplication/
next: /ds/vector-dot-product/
---

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

しかしデ

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

---

[DS検定 学習まとめトップに戻る]({{ '/ds/' | relative_url }})
