---
layout: page
title: 混同行列とは？TP・TN・FP・FNを見分ける【G検定】
description: "混同行列を、分類結果をTP・TN・FP・FNの4種類に分けて整理する表として解説します。特にFP＝誤検知、FN＝見逃しというG検定の判断軸を中心に、Accuracy・Precision・Recallなど多くの分類指標との関係や、表の向きに惑わされない読み方を確認します。"
permalink: /gk/confusion-matrix/
tags: [gk, 機械学習, 評価指標, 頻出]
gk_section: 機械学習の概要/モデルの選択・評価/分類の評価指標
gk_order: 1
last_modified_at: 2026-10-29
---

## まず結論

混同行列（Confusion Matrix）は、**分類結果を「実際」と「予測」の組合せで4種類に分けて整理する表**です。

G検定では、まず次の2つを即座に切れるようにします。

```text
FP → 誤検知
FN → 見逃し
```

混同行列は、Accuracy・Precision・Recall・F1-scoreなど、**多くの分類評価指標を理解する土台**です。

## 直感的な説明

異常検知を例にして、

```text
陽性 = 異常
陰性 = 正常
```

とします。

すると、分類結果は次の4通りです。

- 異常を異常と判定 → TP
- 正常を正常と判定 → TN
- 正常なのに異常と判定 → FP（誤検知）
- 異常なのに正常と判定 → FN（見逃し）

単に「当たった・外れた」ではなく、**どの種類の間違いだったか**を分けるのがポイントです。

## 定義・仕組み

代表的な表は次のとおりです。

|  | 予測：陽性 | 予測：陰性 |
| --- | --- | --- |
| 実際：陽性 | TP（真陽性） | FN（偽陰性） |
| 実際：陰性 | FP（偽陽性） | TN（真陰性） |

各要素の意味は次のとおりです。

| 記号 | 意味 | 試験での言い換え |
| --- | --- | --- |
| TP | 実際も陽性、予測も陽性 | 正しく陽性を検出 |
| TN | 実際も陰性、予測も陰性 | 正しく陰性を判定 |
| FP | 実際は陰性、予測は陽性 | 誤検知 |
| FN | 実際は陽性、予測は陰性 | 見逃し |

ここから、例えば次の指標を作れます。

```text
Accuracy → 全体の正解割合
Precision → 予測陽性の中で正解した割合
Recall → 実際の陽性を拾えた割合
F1-score → Precision と Recall のバランス
```

ただし、**すべての評価指標が1つの混同行列だけから求まるわけではありません**。例えばROC-AUCは、しきい値を動かしたときの複数の結果を使って評価します。

### 計算結果の4つの指標を先に知っておこう

混同行列の数値を使うと、**何を正しく判定できたか**を異なる角度から確認できます。

| 指標 | 何を表す？ | この表での計算 |
| --- | --- | --- |
| [Accuracy（正解率）]({{ '/gk/accuracy/' | relative_url }}) | 全体のうち正しく判定した割合 | (TP + TN) ÷ 全件数 |
| [Precision（適合率）]({{ '/gk/precision/' | relative_url }}) | 陽性と予測した中で、本当に陽性だった割合 | TP ÷ (TP + FP) |
| [Recall（再現率）]({{ '/gk/recall/' | relative_url }}) | 実際に陽性の中で、見逃さず検出した割合 | TP ÷ (TP + FN) |
| [F1-score]({{ '/gk/f1-score/' | relative_url }}) | PrecisionとRecallをまとめた値（調和平均） | 2TP ÷ (2TP + FP + FN) |

**見るポイント：** FP（誤検知）を増やすとPrecisionはどう変わるでしょうか。FN（見逃し）を増やすとRecallはどう変わるでしょうか。

※以下の操作では、ほかの数値を固定して1つの値を変えます。これは**指標の計算の仕組みを理解するための実験**であり、同じデータに対して分類モデルの予測だけを変えた比較ではありません。

### 操作して確認：誤検知と見逃しで指標はどう変わる？

数値を変えて、**FP（誤検知）とFN（見逃し）**がどの評価指標に影響するか確認しましょう。陽性は「異常」、陰性は「正常」の例です。

**操作例：右上の「FN 見逃し」を2から12に変えてみましょう。** TP=8・FP=2・TN=88はそのままにすると、Recallは80.0%から40.0%になります。

<link rel="stylesheet" href="{{ '/assets/css/gk-interactive-pilot.css' | relative_url }}">
<div class="gk-pilot" data-gk-matrix>
  <table class="gk-matrix-table gk-matrix-guided"><caption>実際と予測の組合せ</caption><thead><tr><th scope="col">実際＼予測</th><th scope="col">陽性</th><th scope="col">陰性</th></tr></thead><tbody><tr><th scope="row">陽性</th><td><label>TP 正しく検出<input data-tp type="number" min="0" max="999" value="8"></label></td><td class="gk-matrix-target"><label>FN 見逃し<input aria-label="FN 見逃し（右上のセル）" data-fn type="number" min="0" max="999" value="2"></label></td></tr><tr><th scope="row">陰性</th><td><label>FP 誤検知<input data-fp type="number" min="0" max="999" value="2"></label></td><td><label>TN 正しく正常<input data-tn type="number" min="0" max="999" value="88"></label></td></tr></tbody></table>
  <p class="gk-pilot-output" data-results aria-live="polite">Precision 80.0% ／ Recall 80.0% ／ Accuracy 96.0% ／ F1 80.0%</p>
  <p class="gk-pilot-note" data-input-feedback role="status" aria-live="polite"></p>
  <p class="gk-pilot-note">TP・FN・FP・TNには0〜999の整数を入力します。空欄や範囲外の値では計算しません。</p>
  <p class="gk-pilot-note">Precision = TP/(TP+FP)、Recall = TP/(TP+FN)。分母が0の場合は「—」と表示します。</p>
</div>
<script defer src="{{ '/assets/js/gk-confusion-demo.js' | relative_url }}"></script>

## いつ使う？（得意・不得意）

### 得意なこと

- 誤検知と見逃しを分けて評価する
- Accuracyだけでは見えない誤りの内訳を確認する
- PrecisionやRecallを計算するときの土台にする

### 注意点

表の行と列は、資料によって「実際」と「予測」の配置が逆になることがあります。

そのため、位置だけを暗記せず、必ずラベルを確認します。

```text
True / False → 予測が正しかったか
Positive / Negative → 予測したクラス
```

という意味で読むと混乱しにくくなります。

## G検定ひっかけポイント

### FPとFNを逆にしない

```text
FP
→ 陰性なのに陽性と予測
→ 誤検知

FN
→ 陽性なのに陰性と予測
→ 見逃し
```

### Falseは「実際が陰性」という意味ではない

Falseは、**予測が外れた**ことを表します。

- FP：陽性と予測したが外れた
- FN：陰性と予測したが外れた

### 混同行列だけでモデルの良し悪しを1つに決めない

どの誤りを重く見るかで、重視すべき指標は変わります。

- 誤検知を抑えたい → [Precision](/gk/precision/)
- 見逃しを抑えたい → [Recall](/gk/recall/)
- 両者のバランス → [F1-score](/gk/f1-score/)

## まとめ（試験直前用）

- 混同行列：分類結果をTP・TN・FP・FNに分ける表
- **FP＝誤検知**
- **FN＝見逃し**
- 行・列の位置ではなく「実際／予測」のラベルを見る
- 多くの分類評価指標を理解する土台になる

{% include gk_article_footer.html %}
