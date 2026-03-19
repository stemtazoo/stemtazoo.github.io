---
layout: page
title: 特徴量（Feature）とは？機械学習で使う入力データを理解する【DS検定】
permalink: /ds/feature/
categories: [business]
tags: [ds, design]
prev: /ds/estimator-properties/
next: /ds/feature-engineering2/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

特徴量（Feature）とは？

## まず結論

**特徴量（Feature）**とは、

機械学習モデルが学習や予測に利用する入力データのことです。

DS検定では、

どの情報をモデルに入力するか

特徴量の作り方が予測精度に影響する


という **「データ設計の重要性」**を理解しているかが問われます。



## 直感的な説明

例えば住宅価格を予測するAIを作るとします。

モデルに入力するデータとして

面積

築年数

駅からの距離

部屋数


などを使います。

この モデルに入力する変数が

**特徴量（Feature）**です。

つまり

特徴量 = AIに与える情報

と言えます。

特徴量の選び方によって

予測精度

モデル性能


が大きく変わります。



## 定義・仕組み

特徴量は

機械学習モデルが入力として受け取る変数を指します。

機械学習では一般的に

特徴量 → モデル → 予測結果

という構造になります。

特徴量の例

住宅価格予測

特徴量

面積

築年数

最寄駅距離

部屋数


予測

住宅価格


特徴量エンジニアリング

特徴量はそのまま使うだけでなく

加工することもあります。

例

年齢 → 年齢グループ

日付 → 曜日

気温 → 平均気温


このような加工を

特徴量エンジニアリング

と呼びます。



## どんな場面で使う？

機械学習モデル

機械学習では

回帰

分類

クラスタリング


などすべてのモデルで特徴量が必要です。

データ前処理

特徴量は

正規化

標準化

エンコーディング


などの前処理を行ってからモデルに入力されます。

データ分析

ビジネス分析でも

顧客属性

行動ログ

購買履歴


などが特徴量として扱われます。



## よくある誤解・混同

特徴量 = データ全部？

❌ 必ずしもすべてのデータを使うわけではない

重要なのは

予測に役立つ情報です。

特徴量 = 目的変数？

DS検定ではこの混同がよく出ます。

用語	意味

特徴量	モデルに入力するデータ
目的変数	予測したい値


例

住宅価格予測

特徴量

→ 面積、築年数

目的変数

→ 住宅価格

DS検定のひっかけ

選択肢で

「モデルに入力する変数」

「学習に使う入力データ」


と書かれていた場合

特徴量（Feature）

と判断できることが重要です。



## まとめ（試験直前用）

特徴量（Feature）とは

機械学習モデルに入力するデータです。

ポイント

モデルの入力データ

予測精度に影響する

加工すると特徴量エンジニアリング


DS検定では

「モデルの入力データ」

と書かれていたら

特徴量

と判断するのがポイントです。



## 対応スキル項目（データサイエンス力シート）

機械学習

データ前処理

★ 機械学習モデルにおける特徴量の役割を理解している

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
