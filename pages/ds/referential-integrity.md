---
layout: page
title: 参照整合性とは？外部キーとデータ整合性を理解【DS検定】
description: "参照整合性を外部キーでテーブル間の矛盾を防ぐ仕組みとして整理します。主キーとの関係、削除・更新時の注意点、DS検定での判断ポイントを確認できます。本文では、用語の定義、具体例、似た概念との違い、試験で迷いやすい選択肢の見分け方まで短時間で復習できます。"
permalink: /ds/referential-integrity/
categories: [data-engineering]
tags: [ds, database]
ds_area: dataengineering
ds_section: database
prev: /ds/rdb-vs-nosql/
next: /ds/star-schema/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**参照整合性（Referential Integrity）とは、外部キーが参照する値が参照先テーブルに正しく存在することを保つルール**です。

DS検定では、**「存在しないデータへの参照を防ぐ仕組み」**と理解すると判断しやすくなります。

## 直感的な説明

### 顧客テーブル

| 顧客ID | 名前 |
|---:|---|
| 1 | 田中 |
| 2 | 鈴木 |

### 注文テーブル

| 注文ID | 顧客ID |
|---:|---:|
| 100 | 1 |
| 101 | 99 |

`顧客ID = 99` は顧客テーブルに存在しません。これは**存在しない顧客の注文**になってしまいます。

このような矛盾を防ぐのが参照整合性です。

## 定義・仕組み

参照整合性は、外部キーと参照先のキーの関係が正しく保たれている状態です。

### 正常な例

| 注文ID | 顧客ID |
|---:|---:|
| 100 | 1 |
| 101 | 2 |

顧客ID `1` と `2` は参照先に存在するため問題ありません。

### 参照整合性違反の例

| 注文ID | 顧客ID |
|---:|---:|
| 102 | 99 |

参照先に `99` が存在しないため、外部キー制約があれば登録を防げます。

### 更新・削除時

参照先のデータを削除すると、参照している側が行き場を失うことがあります。

そのためDBでは、

- 削除を拒否する
- 関連行も削除する（CASCADE）
- NULLへ変更する

などのルールを設定することがあります。

## どんな場面で使う？

参照整合性は、テーブル同士に関係があるデータで使います。

- 顧客 → 注文
- 学生 → 履修
- 社員 → 部署

リレーショナルデータベースの基本的な品質管理ルールです。

## よくある誤解・混同

### ❌ 外部キー = 参照整合性

| 用語 | 役割 |
|---|---|
| 外部キー | 他テーブルを参照する列 |
| 参照整合性 | 参照関係が正しいことを保つルール |

**外部キー = 構造、参照整合性 = ルール**と整理できます。

### ❌ 主キー・外部キー・参照整合性は同じ

| 概念 | 役割 |
|---|---|
| 主キー | レコードを識別 |
| 外部キー | 他テーブルとの関係を表す |
| 参照整合性 | 参照関係の正しさを保つ |

### ❌ 参照整合性は重複を防ぐ

重複を防ぐ中心的な仕組みは主キーや一意制約です。

参照整合性は、**存在しない値への参照を防ぐこと**が中心です。

## まとめ（試験直前用）

- **参照整合性 = 外部キーの参照を正しく保つルール**
- 存在しないデータへの参照を防ぐ
- 更新・削除時の矛盾も防ぐ
- **主キー = 識別**
- **外部キー = 関係**
- **参照整合性 = ルール**

## 対応スキル項目（データエンジニアリング力シート）

- データ管理
- データベース
- ★ データベースの基本概念（テーブル、主キー、外部キーなど）を理解している
- ★ データの整合性や品質を保つ仕組みを理解している

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
