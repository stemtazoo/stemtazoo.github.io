---
layout: page
title: UNIONとUNION ALLの違いとは？重複の扱いを整理【DS検定】
permalink: /ds/sql-union/
categories: [data-engineering]
tags: [ds, sql]
prev: /ds/sql-join/
next: /ds/sql-where/
---

## まず結論

UNION＝重複を除いて結合

UNION ALL＝重複もそのまま結合

DS検定では「重複が消えるかどうか」を判断できるかがポイント




## 直感的な説明

2つのリストをくっつけるイメージです。

A
B

B
C

これを結合すると…

UNION → A, B, C（重複削除）

UNION ALL → A, B, B, C（そのまま）


👉 「Bが1つになるか、そのまま2つか」の違い



## 定義・仕組み

UNION

複数のSELECT結果を結合

重複は自動的に削除される


UNION ALL

複数のSELECT結果を結合

重複も含めてすべて残す


基本形：

SELECT 列 FROM テーブル1
UNION
SELECT 列 FROM テーブル2;

SELECT 列 FROM テーブル1
UNION ALL
SELECT 列 FROM テーブル2;

ポイント：

列の数・型は揃える必要がある




## どんな場面で使う？

UNION

ユニークな一覧を作りたいとき

重複が不要な場合


UNION ALL

全データをそのまま結合したいとき

件数を正しく保ちたいとき




## よくある誤解・混同

❌ UNIONとUNION ALLは同じ

→ ⭕ 重複の扱いが違う

👉 DS検定ではここが典型的なひっかけ



❌ 件数は同じになる

→ ⭕ UNIONは重複があると件数が減る



❌ UNIONは速い

→ ⭕ UNIONは重複削除処理があるため遅くなりやすい

👉 UNION ALLの方が基本的に高速



❌ 行の順番は保証される

→ ⭕ ORDER BYを使わないと順序は保証されない



## まとめ（試験直前用）

UNION＝重複削除して結合

UNION ALL＝そのまま結合

件数が変わるかが重要ポイント

UNION ALLの方が高速

「重複を消すか？」で判断する




【対応スキル項目（データエンジニアリング力シート）】

データ基盤

データ操作

★ SQLを用いた基本的なデータ操作（検索・集計・結合等）ができる

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

[DS?? ???????????]({{ '/ds/' | relative_url }})
