---
layout: page
title: F検定とは？t検定との違いを整理【DS検定リテラシー】
description: "F検定は、t検定との違いを理解するための基本テーマです。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。初学者が迷いやすい判断ポイントも確認します。分析や業務での判断場面も確認します。"
permalink: /ds/f-test/
categories: [data-science]
tags: [ds, statistics]
ds_area: datascience
ds_section: statistics
prev: /ds/discrete-continuous-distribution/
next: /ds/interpret-statistics/
last_modified_at: 2026-09-26
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

F検定は、**F分布を使う検定の総称**です。  
DS検定では特に、**2群の分散が等しいかを調べるF検定**と、ANOVAで使うF統計量を切り分けて理解すると安全です。


## 直感的な説明

2つのクラスのテスト結果を考えてみます。

- クラスA：点数のばらつきが小さい  
- クラスB：点数のばらつきが大きい  

このとき知りたいのは、

> 「平均が違うか？」  
ではなく  
> 「ばらつき（分散）が違うか？」

2群の分散比較として使うF検定は、**平均ではなく“ばらつき”を見る検定**です。ANOVAでは、群間変動と群内変動の比から作るF統計量で平均差を評価します。

DS検定では  
「何を比べているのか？」を見抜けるかが重要です。


## 定義・仕組み

2群の分散比較として使うF検定では、2つの母集団の**分散が等しいかどうか**を検定します。

考え方はとてもシンプルで、

- 2つの分散の比を計算する  
- その比が「偶然の範囲かどうか」をF分布で判断する  

という仕組みです。

ここで大事なのは、

> 2群分散比較のF検定では「分散の比」を見る

という点です。

平均の差を直接検定するものではありません。


## どんな場面で使う？

### ① 分散が等しいかを確認したいとき

t検定を行う前に、

- 「等分散とみなしてよいか？」

を確認する目的で使われることがあります。

### ② 分散分析（ANOVA）

3群以上の平均差を検定する分散分析では、  
内部的にF統計量を使います。

ただし、ここでも本質は

> 平均差を分散の比で評価している

という構造です。


## よくある誤解・混同

### ① 2群分散比較のF検定＝平均の差の検定？

これは誤りです。

- **2群の平均差** → t検定や、条件に応じてz検定
- **2群の分散比** → F検定
- **3群以上などの平均差をまとめて評価** → ANOVAでF統計量を使う

「Fが出てきたら必ず分散だけ」と覚えるのではなく、**何を比較しているF統計量か**を見ることが重要です。

DS検定では  
「2群の平均差を検定する方法はどれか？」  
と問われて、F検定を選ばせるひっかけがあります。


### ② F検定＝金融のF検定？

これは全く別物です。

統計でいうF検定・F統計量は、**F分布を使って比を評価する仕組み**です。2群の分散比較やANOVAなど、用途によって何の比を見ているかが異なります。

名称だけで判断しないことが重要です。


### ③ サンプルサイズで使い分ける？

t検定とz検定も、**サンプルサイズだけで機械的に区別するものではありません**。母分散が既知か、標準誤差をどう推定するか、どの近似を使えるかなどの前提で判断します。

「大標本だからF検定」という判断は誤りです。


## まとめ（試験直前用）

- 2群分散比較のF検定は「分散の比」を検定する
- ANOVAでもF統計量を使うため、「F＝常に分散だけ」と固定しない
- t検定・z検定との混同に注意
- 「何を比べているか？」で判断する

問題文に  
「分散」「ばらつき」「等分散」  
とあればF検定を疑う。

「2群の平均差」ならF検定を直接選ぶのではなく、t検定などを検討します。一方、ANOVAでは平均差の検定にF統計量を使います。


## 公式情報・参考リンク

- [NIST/SEMATECH e-Handbook｜F-Test for Equality of Two Variances](https://www.itl.nist.gov/div898/handbook/eda/section3/eda359.htm)
  - 2つの母分散が等しいかをF分布で検定する方法を確認できます。正規性からの逸脱に敏感な点にも注意が必要です。
- [NIST/SEMATECH e-Handbook｜The ANOVA table and tests of hypotheses about means](https://www.itl.nist.gov/div898/handbook/prc/section4/prc433.htm)
  - ANOVAで平均平方の比からF統計量を作り、群平均の差を評価する流れを確認できます。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：基礎技術
- **スキルカテゴリ**：科学的解析の基礎
- **サブカテゴリ**：推定・検定
- **必須スキル**：—
- ★ 検定する対象となるデータの対応の有無を考慮した上で適切な検定手法（t検定, z検定など）を選択し、適用できる
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
