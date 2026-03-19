---
layout: page
title: データ抽出と集計の違いとは？（SQL・BIで混同しやすい操作）【DS検定】
permalink: /ds/data-extraction-vs-aggregation/
categories: [data-science]
tags: [ds, preprocessing]
prev: /ds/stemming-vs-lemmatization/
next: /ds/jupyter-r-usage/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

データ抽出は「必要なデータを選ぶ操作」、集計は「データをまとめて数値を計算する操作」です。
DS検定では、この2つの役割の違いを理解しているかがよく問われます。



## 直感的な説明

例えば、次の売上データがあるとします。

日付	店舗	売上

4/1	東京	80万円
4/2	東京	120万円
4/3	大阪	90万円
4/4	東京	150万円


データ抽出

「売上100万円以上の日だけ知りたい」

日付	店舗	売上

4/2	東京	120万円
4/4	東京	150万円


これは 条件に合うデータを取り出しているだけです。

これが データ抽出（フィルタリング） です。



集計

「東京店舗の売上合計を知りたい」

店舗	売上合計

東京	350万円
大阪	90万円


このように

複数のデータをまとめて数値を計算する操作

が 集計（Aggregation） です。



## 定義・仕組み

データ抽出

データ抽出とは

条件に合うレコード（行）だけを取り出す処理です。

SQLでは主に WHERE句を使います。

SELECT *
FROM sales
WHERE 売上 >= 1000000;



集計

集計とは

複数のデータをまとめて統計値を計算する処理です。

SQLでは次のような関数を使います。

関数	意味

SUM	合計
AVG	平均
COUNT	件数
MAX	最大
MIN	最小


例

SELECT 店舗, SUM(売上)
FROM sales
GROUP BY 店舗;

これは

店舗ごとの売上合計を計算する処理です。



## どんな場面で使う？

データ分析ではこの2つはよく組み合わせて使われます。

典型的な流れは次の通りです。

① データ抽出
② 集計
③ 可視化

例：

「2024年の売上だけ抽出 → 店舗ごとに売上合計 → グラフ表示」

つまり

抽出はデータを選ぶ作業
集計はデータをまとめて計算する作業

です。



## よくある誤解・混同

① 抽出と集計を同じ操作と思ってしまう

DS検定では次のようなひっかけが出ることがあります。

❌ 「データ抽出とは平均や合計を計算する処理である」

これは誤りです。

抽出 → データを選ぶ

集計 → 数値を計算する


役割が全く違います。



② WHEREとGROUP BYの混同

操作	役割

WHERE	データ抽出
GROUP BY	集計


DS検定では

「条件によるデータの絞り込み」＝WHERE

と理解しておくと選択肢を切りやすくなります。



③ フィルタリング＝集計と思う

ExcelでもBIツールでも

フィルターと集計は 別機能です。

この違いは実務でも非常に重要です。



## まとめ（試験直前用）

データ抽出 → 条件に合うデータを取り出す

集計 → データをまとめて数値を計算

SQLでは


操作	SQL

データ抽出	WHERE
集計	GROUP BY


DS検定では

「条件でデータを取り出す」＝抽出（フィルタリング）

と覚えておくと判断しやすくなります。



## 対応スキル項目（データエンジニアリング力シート）

データ加工

データ抽出・加工

★ 数十万レコードのデータに対して、条件を指定してフィルタリングできる（特定値に合致する・もしくは合致しないデータの抽出、特定範囲のデータの抽出、部分文字列の抽出など）

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
