---
layout: page
title: 分類モデルの評価指標の比較とは？【DS検定リテラシー】
description: "分類モデルの評価指標の比較とは、「何を減らしたいのか」という目的に応じて Accuracy・Precision・Recall・F1・ROC・PR を使い分けることです。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。"
permalink: /ds/evaluation-metrics-comparison/
categories: [data-science]
tags: [ds, modeling, evaluation]
ds_area: datascience
ds_section: modeling
prev: /ds/coefficient-of-determination-contribution/
next: /ds/r-squared-adjusted-r-squared/
last_modified_at: 2026-09-20
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

分類モデルの評価指標の比較とは、「何を減らしたいのか」という目的に応じて Accuracy・Precision・Recall・F1・ROC・PR を使い分けることです。  
DS検定では「どの指標を選ぶべきか」を判断させる問題が多く出題されます。


## 直感的な説明

モデル評価は「テストの点数」ではありません。

- 病気の見逃しを防ぎたい  
- 不良品を確実に検出したい  
- 無駄な精密検査を減らしたい  

目的によって「良いモデル」の定義は変わります。

だからこそ、

> 正解率が高い＝良いモデル

とは限りません。

評価指標は  
**何を優先するかを数値で表したもの**です。


## 定義・仕組み

まず前提となるのが **混同行列（Confusion Matrix）** です。

|  | 実際：陽性 | 実際：陰性 |
|---|---|---|
| 予測：陽性 | TP（真陽性） | FP（偽陽性） |
| 予測：陰性 | FN（偽陰性） | TN（真陰性） |

- TP：正しく陽性と予測
- FP：本当は陰性なのに陽性と予測
- FN：本当は陽性なのに陰性と予測
- TN：正しく陰性と予測


### Accuracy（正解率）

$$
Accuracy = \frac{TP + TN}{全体}
$$

全体のうちどれだけ正解したか。

※ 不均衡データでは注意。


### Precision（適合率）

$$
Precision = \frac{TP}{TP + FP}
$$

陽性と予測した人のうち、本当に陽性だった割合。  
→ 偽陽性を減らしたいとき。


### Recall（再現率・感度・TPR）

$$
Recall = \frac{TP}{TP + FN}
$$

実際に陽性の人をどれだけ拾えたか。  
→ 偽陰性を減らしたいとき。

※ TPR（True Positive Rate）と同じ。


### 操作して確認：しきい値を変えると、どの誤りが増える？

**見るポイント：しきい値を下げて見逃しを減らすと、誤検出はどう変わるでしょうか。** まず0.80、0.50、0.30を比べてください。

架空の製品10件について、不良品を「陽性」、良品を「陰性」とします。正解は検査で確認済みという設定です。モデルが出したスコアは固定し、**スコアがしきい値以上なら陽性**と判定します。しきい値を変えても、正解やモデルのスコアは変わりません。

<link rel="stylesheet" href="{{ '/assets/css/ds-visualizer.css' | relative_url }}">

<div class="ds-learning-demo ds-threshold-demo" data-ds-threshold-demo>
  <p class="ds-learning-demo__title">しきい値と見逃し・誤検出の関係</p>
  <label for="ds-evaluation-threshold">判定しきい値：<strong data-dt-value>0.50</strong></label>
  <input id="ds-evaluation-threshold" class="ds-threshold-demo__slider" data-dt-slider type="range" min="0" max="100" step="5" value="50" aria-valuetext="0.50" disabled>
  <div class="ds-learning-demo__controls" role="group" aria-label="しきい値の比較例">
    <button type="button" class="ds-learning-demo__button" data-dt-preset="80" disabled>0.80にする</button>
    <button type="button" class="ds-learning-demo__button" data-dt-preset="50" disabled>0.50に戻す</button>
    <button type="button" class="ds-learning-demo__button" data-dt-preset="30" disabled>0.30にする</button>
  </div>
  <p>各製品のスコア・正解・判定</p>
  <div class="ds-threshold-demo__samples">
    <div class="ds-threshold-demo__sample" data-dt-score="95" data-dt-actual="positive"><strong>A：0.95</strong><span>正解：陽性</span><span data-dt-prediction>判定：陽性（TP）</span></div>
    <div class="ds-threshold-demo__sample" data-dt-score="85" data-dt-actual="positive"><strong>B：0.85</strong><span>正解：陽性</span><span data-dt-prediction>判定：陽性（TP）</span></div>
    <div class="ds-threshold-demo__sample is-error" data-dt-score="70" data-dt-actual="negative"><strong>C：0.70</strong><span>正解：陰性</span><span data-dt-prediction>判定：陽性（FP）</span></div>
    <div class="ds-threshold-demo__sample" data-dt-score="65" data-dt-actual="positive"><strong>D：0.65</strong><span>正解：陽性</span><span data-dt-prediction>判定：陽性（TP）</span></div>
    <div class="ds-threshold-demo__sample is-error" data-dt-score="55" data-dt-actual="negative"><strong>E：0.55</strong><span>正解：陰性</span><span data-dt-prediction>判定：陽性（FP）</span></div>
    <div class="ds-threshold-demo__sample is-error" data-dt-score="45" data-dt-actual="positive"><strong>F：0.45</strong><span>正解：陽性</span><span data-dt-prediction>判定：陰性（FN）</span></div>
    <div class="ds-threshold-demo__sample" data-dt-score="35" data-dt-actual="negative"><strong>G：0.35</strong><span>正解：陰性</span><span data-dt-prediction>判定：陰性（TN）</span></div>
    <div class="ds-threshold-demo__sample" data-dt-score="25" data-dt-actual="negative"><strong>H：0.25</strong><span>正解：陰性</span><span data-dt-prediction>判定：陰性（TN）</span></div>
    <div class="ds-threshold-demo__sample" data-dt-score="15" data-dt-actual="negative"><strong>I：0.15</strong><span>正解：陰性</span><span data-dt-prediction>判定：陰性（TN）</span></div>
    <div class="ds-threshold-demo__sample" data-dt-score="5" data-dt-actual="negative"><strong>J：0.05</strong><span>正解：陰性</span><span data-dt-prediction>判定：陰性（TN）</span></div>
  </div>
  <p class="ds-learning-demo__hint">FP＝良品を不良と判定（誤検出）、FN＝不良品を良品と判定（見逃し）。誤りのカードは枠でも区別します。</p>
  <table class="ds-threshold-demo__matrix">
    <caption>混同行列（件数）</caption>
    <thead><tr><th scope="col">予測／正解</th><th scope="col">正解：陽性</th><th scope="col">正解：陰性</th></tr></thead>
    <tbody><tr><th scope="row">予測：陽性</th><td>TP：<strong data-dt-tp>3</strong></td><td>FP：<strong data-dt-fp>2</strong></td></tr><tr><th scope="row">予測：陰性</th><td>FN：<strong data-dt-fn>1</strong></td><td>TN：<strong data-dt-tn>4</strong></td></tr></tbody>
  </table>
  <div class="ds-threshold-demo__metrics">
    <p><strong>Precision（適合率）</strong><br><span data-dt-precision>3 / (3 + 2) = 60.0%</span></p>
    <p><strong>Recall（再現率）</strong><br><span data-dt-recall>3 / (3 + 1) = 75.0%</span></p>
  </div>
  <p class="ds-causal-demo__result" data-dt-status role="status" aria-live="polite" aria-atomic="true">しきい値0.50：見逃し（FN）1件、誤検出（FP）2件。適合率60.0%、再現率75.0%。</p>
  <noscript><p>操作にはJavaScriptが必要です。下の表でもしきい値による違いを確認できます。</p></noscript>
</div>

<script src="{{ '/assets/js/ds-visualizer.js' | relative_url }}" defer></script>

| しきい値 | 見逃し（FN） | 誤検出（FP） | Precision | Recall |
|---|---|---|---|---|
| 0.80 | 2件 | 0件 | 100.0% | 50.0% |
| 0.50 | 1件 | 2件 | 60.0% | 75.0% |
| 0.30 | 0件 | 3件 | 57.1% | 100.0% |

**固定したデータでは、しきい値を下げると陽性と判定する範囲が広がり、見逃しは減るか変わらず、誤検出は増えるか変わりません。** 見逃しを避けたいならRecall、陽性判定の確かさを重視するならPrecisionを確認し、許容できる誤りと合わせて判断します。

ただし、**Precisionはしきい値を上げれば必ず上がるわけではありません。** 例えば0.60から0.70に上げると、正しく拾えていたDも陰性になり、Precisionは75.0%から66.7%へ下がります。しきい値1.00では陽性判定が0件のため、Precisionの分母が0となり、この教材では「算出不可」と表示します。
### Specificity（特異度）

$$
Specificity = \frac{TN}{TN + FP}
$$

実際に陰性をどれだけ正しく除外できたか。


### FPR（偽陽性率）

$$
FPR = \frac{FP}{FP + TN}
$$

実際に陰性なのに陽性と誤判定した割合。

※ FPR = 1 − Specificity


### F1スコア

$$
F1 = \frac{2 \times Precision \times Recall}{Precision + Recall}
$$

PrecisionとRecallのバランスを見る指標。


### ROC曲線

- 縦軸：TPR（Recall）
- 横軸：FPR

モデルの**全体的な識別能力**を見る。


### PR曲線

- 縦軸：Precision
- 横軸：Recall

陽性クラスの性能を見る。  
不均衡データで有効。


## どんな場面で使う？

### 見逃しを防ぎたい
→ Recall

### 無駄な陽性を減らしたい
→ Precision

### 両方重要
→ F1

### クラス均衡
→ ROC-AUC

### 不均衡データ（陽性が少ない）
→ PR曲線

DS検定では  
「発生率2％」「陽性が非常に少ない」と書かれていたら  
PR曲線を疑います。


## よくある誤解・混同

### 医療＝必ずRecall？

目的次第です。

- 見逃し防止 → Recall
- 誤検知削減 → Precision


### Accuracyが高い＝良い？

陽性1％の場合、  
全員を陰性と予測してもAccuracy99％。

選択肢では  
「正解率が最も重要」と書かれていたら注意。


### ROCとPRの違いが曖昧

- ROC → 全体性能
- PR → 不均衡データに強い

DS検定ではこの切り分けを問われます。


## まとめ（試験直前用）

- 減らしたい誤りで決める  
- 偽陰性を減らす → Recall  
- 偽陽性を減らす → Precision  
- 不均衡データ → PR曲線  
- Accuracyは万能ではない  

「何を守りたいのか？」を読む。


## 対応スキル項目（ver.6 データサイエンス）

- **分類**：解析技術
- **スキルカテゴリ**：モデル化
- **サブカテゴリ**：統計的評価
- **必須スキル**：—
- ★ 混同行列（正誤分布のクロス表）、Accuracy、Precision、Recall、F値、特異度を理解し、精度を評価できる
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
