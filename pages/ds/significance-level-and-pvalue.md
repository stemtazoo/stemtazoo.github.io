---
layout: page
title: 有意水準とp値の違いとは？【DS検定リテラシー】
description: 有意水準は分析前に決める判断基準、p値は帰無仮説の下で観測結果以上に極端な結果が出る確率です。広告効果やA/Bテストの結果を読む場面で、棄却できないことと効果がないこと、有意差と効果の大きさを区別。分析結果を報告するときに避けたい解釈を確認します。
permalink: /ds/significance-level-and-pvalue/
categories: [data-science]
tags: [ds, statistics]
ds_area: datascience
ds_section: statistics
prev: /ds/sampling-methods-comparison/
next: /ds/spearman-rank-correlation/
last_modified_at: 2026-10-04
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

- **有意水準は、帰無仮説を棄却する基準として事前に決める値**
- **p値は、帰無仮説が正しいと仮定したときに、観測結果以上に極端な結果が出る確率**

DS検定では、  
**「p値と有意水準を比較して、帰無仮説を棄却できるかを判断できるか」**  
が問われます。

👉 判断ルールはシンプルです。  
**このページでは、p値が有意水準以下のとき、帰無仮説を棄却する、とします。**

ここを迷わないことが最重要です。


## 直感的な説明

たとえば、新しい広告を出したとします。

- 「効果はない（たまたま売上が増えただけ）」という立場が**帰無仮説**
- 「効果がある」という立場が**対立仮説**

ここで考えるのは、

> 「今回の売上増加は、偶然で説明できるレベルか？」

です。

### 有意水準（例：5%）

帰無仮説が正しいのに誤って棄却するリスクを、どこまで許容するか事前に決める基準です。

### p値（例：3%）

帰無仮説が正しいと仮定したときに、**今回観測した結果以上に極端な結果が出る確率が3%**という意味です。

そのため、

- p値が有意水準より小さい
- 帰無仮説のもとでは今回のような結果は起こりにくい

と判断して、帰無仮説を棄却します。


## 定義・仕組み

### ■ 有意水準（significance level）

- あらかじめ決める基準値
- 一般的には **5%（0.05）や1%（0.01）**
- 帰無仮説が正しいのに棄却する第1種の過誤を、どこまで許容するかを決める基準

DS検定では  
**“事前に決める基準” であること**が重要です。


### ■ p値（p-value）

- 帰無仮説が正しいと仮定したとき
- 今回のデータ以上に極端な結果が出る確率

ポイントはここです：

> p値は「帰無仮説が正しい確率」ではない

ここを間違える受験者が非常に多いです。


### ■ 判断ルール（最重要）

| 比較 | 判断 |
|------|------|
| p値 ≤ 有意水準 | 帰無仮説を棄却 |
| p値 > 有意水準 | 棄却できない |

資料によっては「p値 < 有意水準」を棄却の条件とします。このページは等号を含む基準で説明しますが、p値が有意水準と等しい場合の扱いが設問で明示されていれば、その定義に従います。


## どんな場面で使う？

### ✔ 使う場面

- A/Bテスト
- 広告効果検証
- 新商品の売上改善検証
- 医療や品質管理の統計的判断

ビジネスでは、

> 「偶然か、意味のある差か」

を判断するために使います。


### ⚠ 使うと誤解しやすい場面

- p値が小さい＝効果が大きい、ではない
- p値が大きい＝効果がない、とは限らない

p値は「効果の大きさ」ではなく、  
**帰無仮説のもとで観測結果がどれくらい極端か**を見る指標です。


## よくある誤解・混同

### ❌ p値が低い＝帰無仮説が正しい確率が低い

→ 誤りです。

p値は  
**帰無仮説が正しいと仮定したときに、観測結果以上に極端な結果が出る確率**です。


### ❌ p値が高いときに棄却する

→ 逆です。

DS検定では  
**小さいときに棄却する**  
を確実に押さえましょう。

迷ったらこう覚えます：

> p値が小さい＝帰無仮説のもとでは起こりにくい結果＝棄却を検討


### ❌ 有意水準はデータから決まる

→ 誤りです。

有意水準は**事前に決める基準**です。


### DS検定での典型的ひっかけ

- 「p値が0.03、有意水準5%の場合どうするか」
- 「p値は帰無仮説が正しい確率である」

この2つは頻出です。


## まとめ（試験直前用）

- 有意水準＝事前に決める基準
- p値＝帰無仮説のもとで「観測結果以上に極端な結果」が出る確率
- このページの基準はp値 ≤ 有意水準 → 帰無仮説を棄却。等号の扱いが設問で指定されていれば従う
- p値は「帰無仮説が正しい確率」ではない

迷ったら：

> 小さいときに棄却する

これだけ覚えておけば選択肢は切れます。


## 公式情報・参考リンク

- [Penn State：Hypothesis Testing (P-Value Approach)](https://online.stat.psu.edu/statprogram/book/export/html/529)
  - p値が有意水準以下なら棄却する判断手順と、棄却できない場合の結論を確認できます。
- [NIST/SEMATECH e-Handbook｜Critical values and p values](https://www.itl.nist.gov/div898/handbook/prc/section1/prc131.htm)
  - 有意水準αとp値の関係を説明するNISTの統計リファレンスです。p値を「帰無仮説が正しい確率」と解釈しないための確認に使えます。
- [NIST/SEMATECH e-Handbook｜What are statistical tests?](https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm)
  - 帰無仮説と有意水準、仮説検定の基本的な考え方を確認できます。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：基礎技術
- **スキルカテゴリ**：科学的解析の基礎
- **サブカテゴリ**：推定・検定
- **必須スキル**：—
- ★ 検定における判断の誤り（第1種の過誤、第2種の過誤）と、p値、有意水準の意味、およびこれら相互の関係性を説明できる
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
