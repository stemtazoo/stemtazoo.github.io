---
layout: page
title: データ抽出と集計の違いとは？（SQL・BIで混同しやすい操作）【DS検定】
description: "データ抽出と集計の違いを、行を選ぶ操作と複数行をまとめて指標化する操作として整理します。SQLやBIで混同しやすい処理をDS検定向けに確認できます。本文では、用語の定義、具体例、似た概念との違い、試験で迷いやすい選択肢の見分け方まで短時間で復習できます。"
permalink: /ds/data-extraction-vs-aggregation/
categories: [data-science]
tags: [ds, data-collection, preprocessing]
ds_area: dataengineering
ds_section: data-collection
prev: /ds/stemming-vs-lemmatization/
next: /ds/jupyter-r-usage/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**データ抽出**は「必要なデータを選ぶ操作」、**集計**は「複数のデータをまとめて数値を計算する操作」です。

DS検定では、

- **条件に合う行を残す** → 抽出
- **合計・平均・件数などを計算する** → 集計

と切り分けられることが重要です。

## 直感的な説明

例えば、次の売上データがあるとします。

| 日付 | 店舗 | 売上 |
|---|---|---:|
| 4/1 | 東京 | 80万円 |
| 4/2 | 東京 | 120万円 |
| 4/3 | 大阪 | 90万円 |
| 4/4 | 東京 | 150万円 |

### データ抽出

「売上100万円以上の日だけ知りたい」とします。

| 日付 | 店舗 | 売上 |
|---|---|---:|
| 4/2 | 東京 | 120万円 |
| 4/4 | 東京 | 150万円 |

これは、**条件に合う行だけを取り出している**処理です。

### 集計

「店舗ごとの売上合計を知りたい」とします。

| 店舗 | 売上合計 |
|---|---:|
| 東京 | 350万円 |
| 大阪 | 90万円 |

こちらは、**複数行をまとめて数値を計算している**処理です。

> **判断ポイント：** 行を選ぶのが抽出、行をまとめて計算するのが集計です。

## 定義・仕組み

### データ抽出

データ抽出とは、**条件に合うレコード（行）だけを取り出す処理**です。

SQLでは、主に `WHERE` 句を使います。

```sql
SELECT *
FROM sales
WHERE 売上 >= 1000000;
```

この処理では、元の各行の値を計算し直しているわけではありません。

### 集計

集計とは、**複数のデータをまとめて統計値を計算する処理**です。

代表的な集計関数は次の通りです。

| 関数 | 意味 |
|---|---|
| `SUM` | 合計 |
| `AVG` | 平均 |
| `COUNT` | 件数 |
| `MAX` | 最大 |
| `MIN` | 最小 |

例えば、店舗ごとの売上合計を求める場合は次のようになります。

```sql
SELECT 店舗, SUM(売上)
FROM sales
GROUP BY 店舗;
```

`GROUP BY` でグループを作り、`SUM` などの集計関数で値をまとめます。

## どんな場面で使う？

データ分析では、抽出と集計を組み合わせて使うことがよくあります。

典型的な流れは、

1. **抽出**：必要なデータだけを選ぶ
2. **集計**：合計・平均・件数などを計算する
3. **可視化**：結果をグラフなどで確認する

です。

例えば、

> 2024年の売上だけ抽出 → 店舗ごとに売上合計 → グラフ表示

という流れになります。

## よくある誤解・混同

### ❌ データ抽出 = 平均や合計を計算する処理

これは誤りです。

- **抽出** → 条件に合うデータを選ぶ
- **集計** → 複数データから数値を計算する

### ❌ `WHERE` と `GROUP BY` は同じ役割

| SQL | 主な役割 |
|---|---|
| `WHERE` | 条件で行を絞る（抽出） |
| `GROUP BY` | 行をグループ化して集計しやすくする |

DS検定では、**「条件による絞り込み」= `WHERE`** と判断できると選択肢を切りやすくなります。

### ❌ フィルタリング = 集計

ExcelやBIツールでも、フィルターと集計は別の操作です。

- フィルター → 表示・分析対象を絞る
- 集計 → 合計・平均・件数などを求める

## まとめ（試験直前用）

| 判断したいこと | 操作 | SQLの代表例 |
|---|---|---|
| 条件に合う行を選ぶ | データ抽出 | `WHERE` |
| データをまとめて計算する | 集計 | `GROUP BY` + 集計関数 |

覚えるポイントは次の3つです。

- **抽出 = 選ぶ**
- **集計 = まとめて計算する**
- `WHERE` と `GROUP BY` を混同しない

DS検定では、**「条件でデータを取り出す」なら抽出（フィルタリング）**と判断しましょう。

## 対応スキル項目（データエンジニアリング力シート）

- データ加工
- データ抽出・加工
- ★ 数十万レコードのデータに対して、条件を指定してフィルタリングできる（特定値に合致する・もしくは合致しないデータの抽出、特定範囲のデータの抽出、部分文字列の抽出など）

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
