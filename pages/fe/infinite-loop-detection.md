---
layout: page
title: 無限ループの見抜き方とは？終了条件と変数更新を確認する方法【基本情報技術者試験】
description: FE科目Bの疑似言語で無限ループを見抜くため、終了条件と変数更新をセットで確認する手順を解説。二分探索のlow・highが動かない例を図解し、具体例を試す方法から効率的なトレースへつなげます。
permalink: /fe/infinite-loop-detection/
tags: [fe, fe-technology, algorithm, pseudocode, trace]
fe_section: 科目B対策
fe_subsection: アルゴリズム
fe_order: 55
date: 2026-10-20
last_modified_at: 2026-10-20
related_articles:
  - /fe/binary-search/
  - /fe/pseudocode-reading-guide/
  - /fe/control-structures-loop-selection/
---

## まず結論

無限ループを見抜くには、**終了条件を確認したうえで、次の判定に向けて変数や状態が変化するか**を調べます。

特に注意したいのが、**「代入文がある」ことと「値が変わる」ことは別**という点です。科目Bでは、全ての選択肢を長く追う前に、同じ状態へ戻る条件がないか探すと効率的です。

## 直感的な説明

出口へ進みたいのに、毎回同じ位置で足踏みしている状態を想像してください。

```text
位置を更新する
  ↓
「今いる場所」を、再び「今いる場所」にする
  ↓
次の判定でも位置は変わらない
  ↓
同じ処理を繰り返す
```

プログラムにも、次のような更新が出てきます。

```text
low ← middle
```

これだけでは誤りとは言えません。しかし、`low = middle` のときは、代入しても `low` が変わりません。

**ループが終わる方向へ進んでいるか**を見ることがポイントです。

## 定義・仕組み

### まず「終了」と「更新」を分けて考える

```text
while (low ≦ high)
    ... 条件による分岐 ...
    low ← middle  または  high ← middle
endwhile
```

このような処理は、次の順で読みます。

1. **終了条件**：`low > high` なら `while` を抜ける。途中で `return` する場合もある。
2. **更新する変数**：`low` と `high` が探索範囲を決める。
3. **更新後の状態**：`low`、`high` が変わらず、同じ分岐になることはないか。

「終了条件が存在するから、いつか終了する」とは限りません。終了条件に到達できない場合があります。

### 二分探索の短い例

昇順の配列 `data = [3, 8]` から `target = 8` を探します。以下の疑似言語では**要素番号は1から**始まります。

```text
low ← 1
high ← 2
while (low ≦ high)
    middle ← (low + high) ÷ 2 の商
    if (data[middle] < target)
        low ← middle
    elseif (data[middle] > target)
        high ← middle
    else
        return middle
    endif
endwhile
return -1
```

初回は `middle = (1 + 2) ÷ 2 の商 = 1` です。

`data[1] = 3 < 8` なので `low ← middle` を実行しますが、`low` は **1のまま**。`high` も2のままです。次回も同じ位置を調べるため、処理が進みません。

| 回数 | low | high | middle | 結果 |
|---:|---:|---:|---:|---|
| 1回目 | 1 | 2 | 1 | `low ← 1`（変化なし） |
| 2回目 | 1 | 2 | 1 | また同じ更新 |
| 3回目以降 | 1 | 2 | 1 | 同じ状態の繰返し |

一度確認した中央の要素が不一致なら、次回の候補から外します。この例では `low ← middle + 1` と修正すると、次は `low = 2` となり、`data[2] = 8` を見つけて終了します。

## 科目Aでどう出る？

繰返し処理の基本知識として、`while` は**処理の前に条件を判定する**ことを押さえます。初回から条件が偽なら0回で終了します。

一方、条件が真のまま変わらなければ、`while` は繰り返されます。前判定・後判定の違いは[制御構造の記事](/fe/control-structures-loop-selection/)で確認できます。

## 科目Bでどう使う？

### 1. 具体例で発見 → 次は更新条件から絞る

慣れないうちは、実際に値を代入して2～3回追う方法で問題ありません。変数が変化しないと気づいたら、**なぜ変化しないのか**を式に戻って確認します。

```text
low ← middle
      ↑
  low と middle が等しい場合は変化しない
```

この条件を先に見つけられるようになると、すべての選択肢に配列の値を仮定する必要がなくなります。

### 2. 不具合あり／修正後を切り替えて比べる

次の図解は、配列 `[3, 8]`、探す値 `8` に固定しています。**「次の比較」**を押すと、中央の要素と `low`・`high` の値を追えます。

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}">

<div class="fe-learning-demo fe-loop-demo" data-fe-loop-demo>
  <p class="fe-learning-demo__title">触って確認：無限ループになる二分探索</p>
  <p class="fe-learning-demo__lead">「不具合あり」と「修正後」で、探索範囲が変わるかを比較します。</p>
  <div class="fe-loop-demo__modes" role="group" aria-label="更新方法を切り替える">
    <button type="button" class="fe-learning-demo__button" data-loop-mode="bug" aria-pressed="true">不具合あり</button>
    <button type="button" class="fe-learning-demo__button" data-loop-mode="fixed" aria-pressed="false">修正後</button>
  </div>
  <div class="fe-loop-demo__array" aria-label="要素番号が1から始まる配列">
    <div class="fe-loop-demo__cell" data-loop-cell="1"><span>data[1]</span><strong>3</strong><small data-loop-mark="1">初期状態</small></div>
    <div class="fe-loop-demo__cell" data-loop-cell="2"><span>data[2]</span><strong>8</strong><small data-loop-mark="2">target</small></div>
  </div>
  <div class="fe-loop-demo__values">
    <span>low = <strong data-loop-low>1</strong></span>
    <span>high = <strong data-loop-high>2</strong></span>
    <span>middle = <strong data-loop-middle>―</strong></span>
    <span>比較 = <strong data-loop-count>0回</strong></span>
  </div>
  <p class="fe-loop-demo__update" data-loop-update>まず探索範囲の中央を確認します。</p>
  <p class="fe-loop-demo__status" data-loop-status role="status" aria-live="polite">まだ比較していません。</p>
  <div class="fe-learning-demo__controls">
    <button type="button" class="fe-learning-demo__button" data-loop-next>次の比較 →</button>
    <button type="button" class="fe-learning-demo__button" data-loop-reset>最初から</button>
  </div>
  <p class="fe-learning-demo__hint">見るポイント：同じ `low`・`high`・`middle` で同じ比較が繰り返されるか。無限実行はせず、2回の比較で再発を表示します。</p>
</div>

<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}" defer></script>

### 3. 変数が一つ変われば必ず終了する、とは限らない

例えば `x` が `1 → 2 → 1 → 2` と変わる処理も、条件次第では終了しません。

したがって、確認すべきなのは**単独の変数の変化だけでなく、次に同じ処理を決める状態が再び現れるか**です。

同じ入力条件・同じ状態で、以後の動作が決まる処理なら、その状態に戻った時点で同じ動きを繰り返します。

### Pythonで安全に再現する

普段Pythonを使う場合は、検証回数に上限を設けて確かめられます。**Pythonの添字は0から**なので、上の疑似言語とは番号が1ずれる点に注意してください。

```python
def trace(data, target, fixed=False):
    low, high = 0, len(data) - 1
    seen = set()

    for _ in range(4):  # 無限実行を避ける
        if low > high:
            return -1  # 見つからない
        if (low, high) in seen:
            print("同じ探索範囲が再登場")
            return None
        seen.add((low, high))

        middle = (low + high) // 2
        print(f"low={low}, high={high}, middle={middle}")
        if data[middle] == target:
            return middle
        if data[middle] < target:
            low = middle + 1 if fixed else middle
        else:
            high = middle - 1 if fixed else middle

    return None  # 4回で打ち切り


print(trace([3, 8], 8))              # 同じ範囲を検知 → None
print(trace([3, 8], 8, fixed=True))  # 見つかる → 1
```

この例で `None` は「繰返し状態を検知した／上限に達した」という検証用の値です。問題文の「見つからなければ -1」と混同しないでください。

## よくある誤解・混同

| 誤解 | 正しい見方 |
|---|---|
| 代入があるので毎回値は変化する | `low ← middle` でも、両者が等しければ変化しない |
| `while` に終了条件があるから必ず止まる | 条件が偽にならなければ止まらない |
| 値が変わっていれば無限ループではない | 複数の状態を循環する場合もある |
| 二分探索で不一致の中央要素を残してよい | 一般的な両端を含む区間では、`middle ± 1` で除外する |
| 見つからないときだけ無限ループになる | 探す値が存在しても、到達できずに止まる場合がある |

一般的な二分探索の前提と動作は[二分探索の記事](/fe/binary-search/)で、代入や分岐の読み方は[疑似言語の読み方](/fe/pseudocode-reading-guide/)で確認できます。

## まとめ（試験直前用）

- **終了条件**：何が変わればループを抜けるか確認する。
- **更新処理**：代入後に実際の値や探索範囲が変化するか確認する。
- **同じ状態**：同じ判定と更新を繰り返す条件を探す。
- **具体例は2～3回**：気づいた規則を使い、次の選択肢を効率的に切る。

{% include fe_article_footer.html %}
