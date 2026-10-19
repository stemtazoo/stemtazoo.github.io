---
layout: page
title: 特徴量エンジニアリング演習：顧客表の加工とリーク判定【DS検定】
description: "2026年10月1日時点の顧客表から、年齢・購入頻度・カテゴリ表現を作る演習です。加工前後の表を比べ、翌月の情報や顧客IDを入力に使うべきか、予測時点と列の役割から判断します。"
permalink: /ds/feature-engineering2/
categories: [business]
tags: [ds, data-preparation, design]
ds_area: datascience
ds_section: data-preparation
prev: /ds/feature/
next: /ds/ffp/
last_modified_at: 2026-10-19
---

<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**同じ顧客表を、予測時点で使える特徴量だけに加工してみましょう。** このページは具体例の演習です。操作の全体像は[特徴量エンジニアリングの概説](/ds/feature-engineering/)で確認できます。

## 直感的な説明

2026年10月1日に、**10月中に購入するか**を予測するとします。下表の購入回数と利用月数は、9月30日までの履歴です。「10月購入」は10月終了後に確定する正解で、入力には使いません。

| 顧客ID | 生年月日 | 会員種別 | 過去の購入回数 | 利用月数 | 10月購入 |
|---|---|---|---:|---:|---:|
| A | 1990-01-01 | 一般 | 12 | 6 | 1 |
| B | 1985-05-10 | プレミアム | 3 | 3 | 0 |

見るポイントは、**何列増えたかより、予測するときに同じ値を作れるか**です。

## 定義・仕組み

### 1. 予測時点を固定して年齢を作る

年齢は、基準日の年から出生年を引き、まだ誕生日を迎えていなければ1を引きます。この基準日ではAは36歳、Bは41歳です。過去データにも実行当日の年齢を使うと、当時の状態とずれます。

### 2. 同じ観測期間の回数と長さから頻度を作る

購入頻度を「過去の購入回数 ÷ 利用月数」とすると、Aは月2回、Bは月1回です。利用月数が0なら割れないため、新規顧客の扱いを別に決めます。

### 3. カテゴリを表し、列の役割を分ける

この演習では、会員種別を二つの0/1列にします。

| 顧客ID（照合用） | 年齢 | 月当たり購入回数 | 一般 | プレミアム | 正解y（別管理） |
|---|---:|---:|---:|---:|---:|
| A | 36 | 2 | 1 | 0 | 1 |
| B | 41 | 1 | 0 | 1 | 0 |

**入力Xは年齢からプレミアムまでの4列**です。顧客IDはこの演習では単なる識別子として入力から外し、正解yも分離します。IDを連番の数値として入れると、意味のない大小関係を学ぶおそれがあります。ID由来の履歴を使う設計とは区別します。

年齢計算をPythonで確認すると、次のようになります。

```python
from datetime import date

def age_at(birth, reference):
    before_birthday = (reference.month, reference.day) < (birth.month, birth.day)
    return reference.year - birth.year - int(before_birthday)

reference = date(2026, 10, 1)
print(age_at(date(1990, 1, 1), reference))  # 36
print(age_at(date(1985, 5, 10), reference))  # 41
```

## どんな場面で使う？

モデルへ渡す表を作るときや、加工仕様をレビューするときに使います。クリック数や気温など、別の特徴量でも「どの時点で分かるか」を同じように確認します。

回数のスケーリングや欠損補完を学習する場合は、**学習データで求めた設定を評価・本番データへ適用**します。カテゴリの変換規則も学習データで決め、未知カテゴリの扱いを用意します。

## よくある誤解・混同

### 10月の購入金額も使えばよく当たる？

10月1日には分かりません。将来の購入結果を特徴量に使うとリークになります。後から作る学習用の正解yとして使うこととは別です。

### 列を増やせば必ず性能が上がる？

この2行だけでは性能は判断できません。十分なデータを分割して評価します。同じ顧客の履歴や時間の前後が評価に混ざらないよう、目的に合わせた分割も必要です。

### 加工とモデル調整は同じ？

収集した表の入力表現を変えることと、モデルのハイパーパラメータ調整は別です。欠損処理など前処理と重なる操作も、ここでは入力表現を作る目的で行います。

## まとめ（試験直前用）

- 年齢は予測基準日で計算する。
- 頻度は回数と対応する利用期間から作る。
- カテゴリ・ID・正解の役割を分ける。
- 将来情報を入力にせず、加工設定は学習データで決める。

## 公式情報・参考リンク

- [scikit-learn：Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html)
  - 予測時に使えない情報や、評価データで前処理を学習するリークを避ける考え方を確認できます。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：解析技術
- **スキルカテゴリ**：データ準備
- **サブカテゴリ**：特徴量エンジニアリング
- **必須スキル**：—
- ★ 数値データの特徴量化（二値化／離散化、対数変換、スケーリング／正規化、交互作用特徴量の作成など）を行うことができる
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
