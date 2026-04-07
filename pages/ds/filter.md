---
layout: page
title: フィルターとは？BIツールの基本操作をわかりやすく解説【DS検定】
description: フィルターはBIツールの基本操作をわかりやすく解説を理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/filter/
categories: [business]
tags: [ds, data-processing, visualization, design]
prev: /ds/file-transfer-protocol/
next: /ds/hdfs/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**フィルター（Filter）とは、条件を指定して表示するデータを絞り込む操作**です。

DS検定では、  
**「スライス・ダイス・ドリルダウン」との違いを判断させる問題**がよく出題されます。

ポイントは

**「粒度を変えるのか」  
「条件でデータを絞るのか」**

という違いです。


## 直感的な説明

BIツールでは、大量のデータを扱います。

例えば次のような売上データがあるとします。

| 年 | 地域 | 商品 | 売上 |
|---|---|---|---|
| 2024 | 東京 | A | 100 |
| 2024 | 大阪 | B | 120 |
| 2023 | 東京 | B | 90 |

このとき

**東京のデータだけ表示したい**

場合に使うのが **フィルター**です。

つまり

> 「見たいデータだけを表示する」

操作です。


## 定義・仕組み

フィルターは

**条件に一致するデータだけを表示する操作**

です。

例

- 地域 = 東京  
- 年 = 2024  
- 商品 = A  

などの条件を設定すると  
**条件に合うデータだけ表示されます。**

BIツールでは

- レポートフィルター  
- ビジュアルフィルター  
- ページフィルター

など複数の種類があることもありますが、  
DS検定では

**「条件でデータを絞る操作」**

と理解しておけば十分です。


## どんな場面で使う？

### ① 特定の条件のデータだけ見たいとき

例

- 東京の売上だけ分析  
- 2024年の売上だけ分析  


### ② データ量が多すぎるとき

例えば

全国売上データ  
→ 関東だけ表示  

のように

**分析対象を限定するために使います。**


## よくある誤解・混同

DS検定では、次の用語と混同させる問題がよく出ます。


### フィルター vs スライス

| 操作 | 意味 |
|---|---|
| フィルター | 条件でデータを絞る |
| スライス | 多次元データの断面を切る |

実務では似ていますが、試験では

**「条件で表示を絞る」  
→ フィルター**

と覚えると選択肢を切りやすいです。


### フィルター vs ダイス

| 操作 | 意味 |
|---|---|
| フィルター | 条件で絞る |
| ダイス | 複数条件でデータ範囲を切り出す |

DS検定では

- 範囲  
- 多次元  
- データキューブ  

などの言葉が出てきたら  
**ダイス**の可能性が高くなります。


### フィルター vs ドリルダウン

| 操作 | 意味 |
|---|---|
| フィルター | 条件でデータを絞る |
| ドリルダウン | データをより詳細に見る |

例

- 年 → 月 → 日  
→ **ドリルダウン**


## まとめ（試験直前用）

BIツールの操作は次の4つで整理できます。

- **フィルター**：条件でデータを絞る  
- **スライス**：1つの条件でデータを切る  
- **ダイス**：複数条件でデータ範囲を切る  
- **ドリルダウン**：集計 → 詳細  

DS検定では  

**「粒度を変えているのか」  
「条件で絞っているのか」**

を判断すると、選択肢を正しく切ることができます。


## 対応スキル項目（データサイエンス力シート）

- データ理解・可視化  
- データ可視化

★ データの特徴を理解し、適切な可視化手法を選択できる

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
