---
layout: page
title: インプテーションとは？同じデータで補完前後を比べる【DS検定】
description: "欠損値補完を、20・30・40・欠損という同じデータの平均・分散の変化で確認します。代表値・推定値で埋める意味、学習データだけで補完値を求める理由、欠損処理の総論との違いを整理します。"
permalink: /ds/imputation/
categories: [data-science]
tags: [ds, data-preparation, preprocessing]
ds_area: datascience
ds_section: data-preparation
prev: /ds/image-metadata/
next: /ds/missing-value-handling/
last_modified_at: 2026-10-19
---

<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**インプテーションは、欠損を代表値や推定値で補う処理**です。このページでは、同じ小データの補完前後を比べ、「行を残せても、元の分布を復元したとは限らない」ことを確かめます。

そもそも削除・補完のどれを選ぶかは、[欠損値の処理方針](/ds/missing-value-handling/)で確認できます。

## 直感的な説明

アンケートの年齢が、20歳、30歳、40歳、未回答だったとします。**観測済み3人の平均は計算でき、30歳**です。全員の本当の平均は、未回答の年齢が分からないので確定できません。

欠損を受け付けないモデルなどへ入力するために、未回答を仮の30歳で埋めるのが、平均値による補完の例です。30歳がその人の真の年齢だと判明したわけではありません。

## 定義・仕組み

### 同じ4行を補完する

| 行 | 補完前 | 平均値で補完した後 |
|---|---:|---:|
| A | 20 | 20 |
| B | 30 | 30 |
| C | 40 | 40 |
| D | 欠損 | 30（推定値） |

補完前は観測済み3個、補完後は4個で、**ここでは記述用の分散（分母n）**を計算します。

| 指標 | 観測済み3個 | 補完後4個 |
|---|---:|---:|
| 平均 | 30 | 30 |
| 平均からの偏差平方和 | 200 | 200 |
| 分母n | 3 | 4 |
| 分散 | 200/3 ≒ 66.67 | 200/4 = 50 |

平均は同じでも、平均値を追加するとばらつきは小さくなりました。これは**真の分布を復元した証拠ではありません。** 欠損者に偏りがあれば、平均そのものも適切でない可能性があります。

### 補完値をどう作るか

数値なら平均・中央値、カテゴリなら最頻値、ほかの項目を使うなら回帰やk近傍などによる推定が候補です。この年齢例では平均と中央値がどちらも30ですが、一般には一致しません。推定が複雑でも正確とは限りません。

機械学習では、補完値や推定規則を**学習データだけで求め、評価・本番データには同じ規則を適用**します。scikit-learnなら、学習側で`fit`し、評価側は`transform`で変換するという区別です。

## どんな場面で使う？

行を残したいときや、モデルが欠損を受け付けないときに検討します。売上・アンケート・センサーなどでも使いますが、欠損の理由と補完による偏りを確認します。

未回答が特定の層に偏る場合や、補完値が判断を大きく変える場合は、手法を変えた比較や再収集も検討します。真に測定された値と区別するため、欠損フラグや処理記録を残す方法もあります。

## よくある誤解・混同

### 補完した4人は、測定済み4人と同じ？

違います。補完値には不確かさがあります。同じ値を入れたことで、分布や相関が変わる可能性もあります。

### 平均を全データから計算した方がよい？

予測評価では評価側の情報が学習へ混ざるリークになります。交差検証でも、各学習分割の中だけで補完規則を求めます。

### ほかの前処理と同じ？

スケールをそろえる正規化、カテゴリを数値で表すエンコーディング、少数クラスを増やすオーバーサンプリングとは目的が違います。欠損の扱いをカテゴリ表現に組み込むことはありますが、補完と同義ではありません。

## まとめ（試験直前用）

- 補完は欠損を仮の値で埋める処理。
- 行を残せても分布や不確かさは変わる。
- 例では平均30のまま、記述用の分散は約66.67から50へ変化。
- 補完規則は学習データで求める。

## 公式情報・参考リンク

- [scikit-learn：Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html)
  - 代表値や推定による補完方法を確認できます。
- [scikit-learn：Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html)
  - 補完などの前処理を学習データだけで学習する理由を確認できます。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：解析技術
- **スキルカテゴリ**：データ準備
- **サブカテゴリ**：データクレンジング
- **必須スキル**：◯
- ★ 外れ値・異常値・欠損値とは何かを理解し、指示のもと適切に検出と除去・変換などの対応ができる
- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)
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
