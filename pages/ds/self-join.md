---
layout: page
title: 自己結合とは？同じテーブルを結合する理由を理解する【DS検定】
description: "自己結合（Self Join）とは、同じテーブルを2回使って結合するSQL処理です。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。初学者が迷いやすい判断ポイントも確認します。"
permalink: /ds/self-join/
categories: [data-engineering]
tags: [ds, data-processing, sql]
prev: /ds/left-join-where/
next: /ds/batch-vs-stream/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**自己結合（Self Join）とは、同じテーブルに別名を付けて、そのテーブル同士をJOINする方法**です。

DS検定では、**同じテーブル内の別の行を対応づけたいときに使う**と理解できれば十分です。

## 直感的な説明

例えば社員テーブルに「上司ID」はあるものの、「上司の名前」はないとします。

| 社員ID | 名前 | 上司ID |
|---:|---|---:|
| 1 | 田中 | 3 |
| 2 | 鈴木 | 3 |
| 3 | 山本 | NULL |

この表だけでは、`上司ID = 3` が山本さんだと直接表示できません。

そこで同じ社員テーブルを、

- 社員として見るテーブル
- 上司として見るテーブル

の2つに見立てて結合します。

結果は次のようになります。

| 社員 | 上司 |
|---|---|
| 田中 | 山本 |
| 鈴木 | 山本 |
| 山本 | NULL |

## 定義・仕組み

自己結合は、同じテーブルに異なるエイリアスを付けて通常のJOINを行います。

```sql
SELECT
  e1.name AS 社員,
  e2.name AS 上司
FROM employees e1
LEFT JOIN employees e2
  ON e1.manager_id = e2.employee_id;
```

ここでは、

- `e1` → 社員として見る `employees`
- `e2` → 上司として見る `employees`

です。

**同じテーブルを役割別に2回使う**のがポイントです。

## どんな場面で使う？

自己結合は、同一テーブル内の行同士に関係があるときに使います。

- 社員と上司
- 親カテゴリと子カテゴリ
- 組織ツリー
- 前日と当日のデータ比較

## よくある誤解・混同

### ❌ 自己結合は特別なJOIN構文

特別なSQL構文ではありません。**同じテーブルをエイリアスで分けて通常のJOINを行う**だけです。

### ❌ 同じテーブル同士はJOINできない

エイリアスを付ければ別の役割として扱えるため、問題なくJOINできます。

### ❌ 自己結合は親子関係だけに使う

親子関係は代表例ですが、**同一テーブル内の別行を対応づける場面全般**で使えます。

## まとめ（試験直前用）

- **自己結合 = 同じテーブルを2回使ってJOIN**
- エイリアスで役割を分ける
- 社員と上司などの関係でよく使う
- 特別なJOIN構文ではない

DS検定では、**「同じテーブル内の別行を対応づける」なら自己結合**と判断しましょう。

## 対応スキル項目（データエンジニアリング力シート）

- データ操作
- SQL
- ★ 同一テーブルを別名で結合して関係を取り出せる

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
