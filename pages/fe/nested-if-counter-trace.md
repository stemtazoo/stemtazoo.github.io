---
layout: page
title: 入れ子のif文とは？二つのカウンタをトレースする方法【基本情報技術者試験】
description: 入れ子のif文で外側だけ成立した回数と、内側も成立した回数を区別する方法を、5件の注文データと科目B向け疑似言語で解説。カウンタの変化を一件ずつ確認し、式と変数の対応を読み取ります。
permalink: /fe/nested-if-counter-trace/
tags: [fe, fe-technology, algorithm, pseudocode, trace]
fe_section: 科目B対策
fe_subsection: アルゴリズム
fe_order: 62
date: 2026-10-25
last_modified_at: 2026-10-25
related_articles:
  - /fe/pseudocode-reading-guide/
  - /fe/array/
  - /fe/control-structures-loop-selection/
---

## まず結論

**入れ子のif文（nested if）**とは、あるif文の中に別のif文がある書き方です。

科目Bでは、**外側の条件が真のときだけ、内側の条件を判定する**ことを最初に押さえます。

二つのカウンタを増やす処理なら、どの条件が成立したときに何を数えているかで区別します。

~~~text
外側の条件が真 → Kを1増やす
さらに内側の条件も真 → Mも1増やす
~~~

この場合、**両方が成立するとKもMも増えます**。内側だけが単独で実行されることはありません。

## 直感的な説明

パンと牛乳を一緒に買う注文を調べるとします。

- **K**：牛乳が含まれる注文数
- **M**：牛乳とパンの両方が含まれる注文数

例えば、次の5件の注文データを考えます。1件の注文に同じ商品は重複して登場しないものとします。

| 注文番号 | 買われた商品 |
|---|---|
| 1 | パン、牛乳 |
| 2 | 牛乳 |
| 3 | パン、卵 |
| 4 | パン、牛乳、卵 |
| 5 | ジュース |

牛乳が含まれるのは注文1・2・4なので **K＝3**、パンも一緒なのは注文1・4なので **M＝2**です。

同じ注文がKにもMにも加算される場合があるため、KとMを別々の注文集合として足し合わせてはいけません。

## 定義・仕組み

### 入れ子のif文が数えるもの

次は、5件の注文を順に調べる**説明用の疑似コード**です。添字は1から始まり、注文を表す配列に指定した商品が含まれるかを判定できます。基準の商品は「パン」、比較対象は「牛乳」とします。

~~~text
K ← 0
M ← 0

for (order に5件の注文を順番に代入する)
    if (order に「牛乳」が含まれる)
        if (order に「パン」が含まれる)
            M ← M + 1
        endif
        K ← K + 1
    endif
endfor
~~~

Kの加算は**外側のif文の中、内側のif文の外**にあります。そのため、牛乳だけの注文でもKは増えます。

Mの加算は**二つのif文の両方の内側**にあるので、パンと牛乳が同時にある注文だけで増えます。

| 注文 | 牛乳あり？ | パンもあり？ | 処理後K | 処理後M |
|---:|---|---|---:|---:|
| 1 | はい | はい | 1 | 1 |
| 2 | はい | いいえ | 2 | 1 |
| 3 | いいえ | 判定しない | 2 | 1 |
| 4 | はい | はい | 3 | 2 |
| 5 | いいえ | 判定しない | 3 | 2 |

**外側が偽の場合、内側のif文の判定は実行されません。**

### 配列にすると、添字ごとに別の対象を数える

比較対象の商品が牛乳・卵の2種類なら、KとMを配列で管理できます。

~~~text
otherItems ← {「牛乳」, 「卵」}
arrayK ← {0, 0}
arrayM ← {0, 0}
itemCount ← 0

for (order に注文を順番に代入する)
    if (order に「パン」が含まれる)
        itemCount ← itemCount + 1
    endif

    for (i を1から2まで1ずつ増やす)
        if (order にotherItems[i]が含まれる)
            if (order に「パン」が含まれる)
                arrayM[i] ← arrayM[i] + 1
            endif
            arrayK[i] ← arrayK[i] + 1
        endif
    endfor
endfor
~~~

- itemCount：パンが含まれる注文数（3）
- arrayK[i]：比較対象の商品が含まれる注文数
- arrayM[i]：比較対象とパンの両方が含まれる注文数

この場合の結果は次のとおりです。

| 添字i | otherItems[i] | arrayK[i] | arrayM[i] |
|---:|---|---:|---:|
| 1 | 牛乳 | 3 | 2 |
| 2 | 卵 | 2 | 2 |

**同じiでKとMを比較する**ことが重要です。例えば、arrayM[1]は「パンと牛乳の同時購入」、arrayK[2]は「卵を買った注文数」なので、対応しません。

## 科目Aでどう出る？

科目Aでは、条件分岐と論理演算の意味を確認します。

| 書き方 | 読み方 |
|---|---|
| if A の中に if B | Aが真のときだけBを調べる |
| A and B | AとBが両方真なら成立 |
| if A → elseif B | Aが偽の場合にBを判定する |

入れ子のif文と、同じ段に並んだelseifは動きが違います。

~~~text
if A
    if B
        Mを1増やす
    endif
    Kを1増やす
endif
~~~

この例のMはAとBの両方を満たす場合にだけ増えます。一方、KはAを満たせばBが偽でも増えます。

## 科目Bでどう使う？

### 1件ずつ進めてカウンタの更新を確認する

次の教材では比較対象を牛乳・卵から選び、**次の注文**を押して処理を進めます。注文ごとに、外側と内側の条件がどうなり、K・Mがどう変化するかを確認しましょう。

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}?v=20261025-nested">
<div class="fe-learning-demo fe-nested-counter-demo" data-fe-nested-counter-demo>
  <p class="fe-learning-demo__title">入れ子のif文：5件の注文を順にトレース</p>
  <p class="fe-learning-demo__hint">見るポイント：比較対象だけがある注文はKのみ増え、両方ある注文ではKもMも増える。</p>
  <div class="fe-nested-counter-demo__choices" role="group" aria-label="比較対象の商品">
    <button type="button" data-fe-nested-target="牛乳" aria-pressed="true">牛乳とパン</button>
    <button type="button" data-fe-nested-target="卵" aria-pressed="false">卵とパン</button>
  </div>
  <div class="fe-nested-counter-demo__table-wrap">
    <table class="fe-nested-counter-demo__table">
      <thead><tr><th scope="col">注文</th><th scope="col">購入商品</th><th scope="col">今回の判定</th></tr></thead>
      <tbody>
        <tr data-fe-nested-order="パン,牛乳"><th scope="row">1</th><td>パン、牛乳</td><td data-fe-nested-verdict>—</td></tr>
        <tr data-fe-nested-order="牛乳"><th scope="row">2</th><td>牛乳</td><td data-fe-nested-verdict>—</td></tr>
        <tr data-fe-nested-order="パン,卵"><th scope="row">3</th><td>パン、卵</td><td data-fe-nested-verdict>—</td></tr>
        <tr data-fe-nested-order="パン,牛乳,卵"><th scope="row">4</th><td>パン、牛乳、卵</td><td data-fe-nested-verdict>—</td></tr>
        <tr data-fe-nested-order="ジュース"><th scope="row">5</th><td>ジュース</td><td data-fe-nested-verdict>—</td></tr>
      </tbody>
    </table>
  </div>
  <div class="fe-nested-counter-demo__stats">
    <div><span>K：比較対象あり</span><strong data-fe-nested-k>0</strong></div>
    <div><span>M：パンもあり</span><strong data-fe-nested-m>0</strong></div>
    <div><span>処理した注文</span><strong data-fe-nested-progress>0 / 5</strong></div>
  </div>
  <p class="fe-nested-counter-demo__status" data-fe-nested-status role="status" aria-live="polite">開始前です。比較対象を選び、次の注文へ進んでください。</p>
  <div class="fe-nested-counter-demo__controls" data-fe-nested-controls hidden>
    <button type="button" data-fe-nested-prev disabled>一つ戻る</button>
    <button type="button" data-fe-nested-next>次の注文</button>
    <button type="button" data-fe-nested-reset disabled>最初から</button>
  </div>
  <p class="fe-learning-demo__hint">操作できない場合でも、直前のトレース表と配列の結果表から結論を確認できます。</p>
</div>
<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}?v=20261025-nested" defer></script>

### 数式があるときは変数の意味から逆算する

プログラムの最後に計算式があるなら、まず各変数を**回数・件数・合計**などに置き換えます。

例えば次の値を考えます。

~~~text
共に買った注文数 = arrayM[i]
比較対象が買われた注文数 = arrayK[i]
基準商品が買われた注文数 = itemCount
全注文数 = 注文配列の要素数
~~~

このような数え上げ結果が式に使われていても、**計算を全部済ませる前に、各変数の役割を特定**できることがあります。

数式でMが同時購入数なら、**内側のif文で増やす配列がM**です。Kが片方の商品だけの購入数なら、**外側のif文の中で増やす配列がK**です。

## よくある誤解・混同

| 誤解 | 正しい理解 |
|---|---|
| 外側が偽でも内側のif文は判定される | 外側が偽なら内側に入らない |
| 内側も真ならMだけ増える | KもMも増える |
| KとMは別々の注文数だから足せる | Mに数えた注文はKにも含まれる |
| 変数名のMやKで役割が決まる | **どの条件で値が更新されるか**で決める |
| 配列の添字iは常に注文番号 | この例では**比較対象の商品の番号** |
| 二つのifはelseifと同じ | elseifは先の条件が偽のときだけ評価する |

また、このプログラムでは必ず **0 ≦ M ≦ K** です。MがKを超える結果になったら、どこかで加算条件を読み間違えた可能性があります。

## まとめ（試験直前用）

- **外側のifが偽なら、内側のifは判定しない**
- **外側が真ならK、さらに内側も真ならMを増やす**
- **カウンタの意味は変数名ではなく加算条件で決める**
- 配列ならiが「何の添字か」を初期化とループから確認する
- 先に変数の役割を確定すれば、数式の空欄は計算せずに判断できることもある

関連：[疑似言語の読み方](/fe/pseudocode-reading-guide/)・[配列の基本](/fe/array/)・[制御構造と繰返し](/fe/control-structures-loop-selection/)

参考：[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)

{% include fe_article_footer.html %}
