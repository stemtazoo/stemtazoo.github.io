---
layout: page
title: データ前処理（Preprocessing）とは？分析前に行う重要ステップ【DS検定】
permalink: /ds/preprocessing/
categories: [data-science]
tags: [ds, data-preparation, preprocessing]
prev: /ds/nlp-cleaning/
next: /ds/regular-expression-basic/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

データ前処理とは、分析や機械学習を行う前にデータを整える作業です。

DS検定では、モデルを作る前にデータ品質を整えることが重要という理解が問われます。




## 直感的な説明

例えば、売上データを分析しようとしたとします。

しかしデータを確認すると

空白のデータ（欠損値）がある

商品名がバラバラに書かれている

文字データが混ざっている


このままでは分析や機械学習がうまくできません。

そこで次のような処理を行います。

欠損値を補完する

データ形式を統一する

カテゴリを数値化する


このように

データを分析できる状態に整える作業を

**データ前処理（Preprocessing）**と呼びます。



## 定義・仕組み

データ前処理とは、データ分析や機械学習の前にデータを整形・加工する工程です。

実際のデータは

欠損

ノイズ

表記ゆれ


などが含まれていることが多く、

そのままでは分析に適していません。

そのため、次のような処理を行います。

代表的な前処理

処理	内容

欠損値処理	空白データを補完・削除
エンコーディング	カテゴリ変数を数値化
正規化・標準化	データのスケール調整
マッピング	値を別の値へ変換
特徴量エンジニアリング	新しい特徴量を作成


DS検定では

データ前処理は機械学習の重要工程

という理解が重要です。



## どんな場面で使う？

① 機械学習モデル作成

モデルを作る前に

欠損値

データ形式

スケール


を整える必要があります。

もし前処理を行わないと

モデル精度が低下

学習が失敗


することがあります。



② データ分析

BIツールや統計分析でも

データ形式

カテゴリ整理


などの前処理が必要になります。

つまり

前処理はすべてのデータ分析の基礎作業です。



## よくある誤解・混同

① データ収集との混同

❌
前処理 = データを集める作業

⭕
前処理 = 既存データを整理する作業



② モデル学習との混同

❌
前処理 = モデルを学習させる工程

⭕
前処理 = モデル学習の前に行う工程

DS検定では

前処理 → モデル学習 → 評価

という流れを理解しているかが問われます。



③ 特徴量エンジニアリングとの関係

特徴量エンジニアリングは

前処理の中でも特にモデル精度に影響する部分です。



## まとめ（試験直前用）

データ前処理 = 分析前にデータを整える作業

代表例

欠損値処理

エンコーディング

正規化

マッピング

特徴量エンジニアリング


前処理を行わないとモデル精度が下がる


DS検定では

「データを分析可能な形に整える工程」

と書かれていたら

データ前処理を思い出すと判断しやすくなります。



## 対応スキル項目（データサイエンス力シート）

データ理解・前処理

データ加工


★ データの前処理（欠損値処理、正規化、カテゴリ変数の処理など）を理解している

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
