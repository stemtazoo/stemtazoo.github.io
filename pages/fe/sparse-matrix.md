---
layout: page
title: 疎行列とは？0以外の値を行・列・値で保存する方法【基本情報技術者試験】
description: 疎行列の0以外の要素を「行番号・列番号・値」の3配列へ変換する仕組みを、二重ループと図解で説明します。FE科目Bでiとjを取り違えずに追う方法、配列へ追加される順番、選択肢の違いから必要な箇所だけを確かめる判断法を整理します。
permalink: /fe/sparse-matrix/
tags: [fe, fe-technology, data-structure, algorithm, pseudocode]
fe_section: 科目B対策
fe_subsection: データ構造
fe_order: 15
date: 2026-10-24
last_modified_at: 2026-10-24
related_articles:
  - /fe/array/
  - /fe/pseudocode-reading-guide/
---

## まず結論

疎行列（そぎょうれつ、sparse matrix）とは、**要素の多くが0である行列**です。

0が多い場合、すべての値をそのまま保存する代わりに、**0以外の要素について「行番号・列番号・値」を記録する**方法があります。これは疎行列の保存方法の一例です。

基本情報技術者試験では、二重ループを読んで、**どの位置の値が、どの順番で追加されるか**を判断できることが大切です。

## 直感的な説明

商品ごとの在庫数を表にするとき、在庫0の欄ばかりなら、商品がある場所だけをメモする方がコンパクトになることがあります。

疎行列も同じように、0以外の要素を次の3点で記録できます。

```text
何行目？ → 行番号
何列目？ → 列番号
値はいくつ？ → 値
```

たとえば4行4列の行列を考えます。以下では行番号と列番号を**1から**数えます。

<link rel="stylesheet" href="{{ '/assets/css/fe-sparse-matrix-visualizer.css' | relative_url }}">

<div class="fe-sparse-demo" data-fe-sparse-demo>
  <p class="fe-sparse-demo__title">触って確認：0以外の要素を3つの配列へ追加</p>
  <p class="fe-sparse-demo__instruction">「次の要素」を押すと、記録した位置が強調され、行番号・列番号・値の配列が増えます。</p>
  <div class="fe-sparse-demo__table-wrap">
    <table class="fe-sparse-demo__matrix" aria-label="4行4列の疎行列。行と列は1から数える">
      <thead><tr><th scope="col">行＼列</th><th scope="col">1</th><th scope="col">2</th><th scope="col">3</th><th scope="col">4</th></tr></thead>
      <tbody>
        <tr data-sparse-row><th scope="row">1</th><td data-sparse-value>4</td><td data-sparse-value>0</td><td data-sparse-value>0</td><td data-sparse-value>0</td></tr>
        <tr data-sparse-row><th scope="row">2</th><td data-sparse-value>0</td><td data-sparse-value>6</td><td data-sparse-value>2</td><td data-sparse-value>0</td></tr>
        <tr data-sparse-row><th scope="row">3</th><td data-sparse-value>0</td><td data-sparse-value>0</td><td data-sparse-value>0</td><td data-sparse-value>5</td></tr>
        <tr data-sparse-row><th scope="row">4</th><td data-sparse-value>0</td><td data-sparse-value>1</td><td data-sparse-value>0</td><td data-sparse-value>0</td></tr>
      </tbody>
    </table>
  </div>

  <div class="fe-sparse-demo__output" aria-label="変換結果の3つの配列">
    <div><span>行番号 a</span><code data-sparse-rows>まだなし</code></div>
    <div><span>列番号 b</span><code data-sparse-cols>まだなし</code></div>
    <div><span>値 c</span><code data-sparse-vals>まだなし</code></div>
  </div>
  <p class="fe-sparse-demo__status" data-sparse-status aria-live="polite">開始前：0以外の値を行の先頭から順に探します。</p>
  <div class="fe-sparse-demo__controls" data-sparse-controls hidden>
    <button type="button" data-sparse-prev>一つ戻る</button>
    <button type="button" data-sparse-next>次の要素</button>
    <button type="button" data-sparse-reset>最初から</button>
    <span data-sparse-counter>0 / 5件</span>
  </div>
  <p class="fe-sparse-demo__hint">見るポイント：<strong>行番号は同じ値が続くことがあり、列番号は次の行へ進むと小さく戻ることもある</strong>点です。</p>
  <noscript><p>JavaScriptが無効でも、行列と変換結果は次の「定義・仕組み」の表から確認できます。</p></noscript>
</div>

<script src="{{ '/assets/js/fe-sparse-matrix-visualizer.js' | relative_url }}" defer></script>

## 定義・仕組み

行列の各要素を確認し、0以外の場合だけ位置と値を保存します。先ほどの4行4列の行列には、0以外の要素が5個あります。

| 行番号 i | 列番号 j | 値 matrix[i, j] |
|---:|---:|---:|
| 1 | 1 | 4 |
| 2 | 2 | 6 |
| 2 | 3 | 2 |
| 3 | 4 | 5 |
| 4 | 2 | 1 |

表の各列をそれぞれ別の配列にすると、次の結果になります。

```text
a（行番号）= [1, 2, 2, 3, 4]
b（列番号）= [1, 2, 3, 4, 2]
c（値）    = [4, 6, 2, 5, 1]
```

3つの配列の**同じ位置**が、1個の要素に対応します。たとえば4番目の組は、3行目・4列目の値5を表します。

### 二重ループで変換する

行数を4、列数を4としたときの処理は次のようになります。ここでも添字を1から始めます。

```text
a ← 空の配列
b ← 空の配列
c ← 空の配列

for (i を 1 から 4 まで増やす)
    for (j を 1 から 4 まで増やす)
        if (matrix[i, j] ≠ 0)
            a の末尾に i を追加
            b の末尾に j を追加
            c の末尾に matrix[i, j] を追加
        endif
    endfor
endfor
```

**外側の i が行、内側の j が列**なので、1行目を左から右まで調べてから2行目へ進みます。値が0なら、3つの配列には何も追加しません。

### 保存容量について

この例の元の行列は16個の値を持ちます。一方、3つの配列に保存する数字は、0以外の5件について3つずつなので15個です。

ただし、行番号・列番号を持つ分、**どんな行列でも必ず省メモリになるわけではありません**。0が非常に多い大きな行列ほど、0を省略する利点が出やすくなります。

基本情報技術者試験の「アルゴリズムとプログラミング」「データ構造」に関係する内容です。試験範囲は[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

## 科目Aでどう出る？

科目Aでは、疎行列や圧縮表現について、保存方法の特徴を判断します。

| 説明 | 判断 |
|---|---|
| 0以外の値の位置と内容を記録する | 疎行列を扱う方法の一つ |
| 行列の全要素をそのまま保存する | 通常の二次元配列の表現 |
| 0が多いほど記録する要素を減らせる場合がある | 疎行列の圧縮に適した特徴 |
| 3配列にすると必ず記憶量が小さくなる | 誤り。0以外の要素数などによる |

疎行列は「0が多い行列」という性質を表す言葉で、**必ず3つの配列で保存するという意味ではありません**。3配列に分けるのは表現方法の一つです。

## 科目Bでどう使う？

科目Bの疑似言語では、ループの実行順と、配列に追加する値を追います。

### まず外側と内側のループを確認する

```text
外側：i（行）
  内側：j（列）
    0以外なら a・b・c に追加
```

最初の3件だけ追うと、次のようになります。

| 追加した回数 | i | j | 値 |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 4 |
| 2 | 2 | 2 | 6 |
| 3 | 2 | 3 | 2 |

この時点で、

```text
a = [1, 2, 2, ...]
b = [1, 2, 3, ...]
c = [4, 6, 2, ...]
```

まで分かります。

### 選択肢があるときは、違う位置だけ追う

すべての値を最後まで追う前に、選択肢を比較します。

1. 行番号の並びが違えば、最初の数件で候補を減らす
2. 候補が残ったら、列番号や値の**異なる位置**を探す
3. その位置のデータが追加されるまでだけ、ループを追う

大切なのは、値が0の場所を配列に追加しないことです。また、iが同じ値のままでも、jが進めば別の要素が追加されます。

二重ループの読み方に不安がある場合は、[配列の基本](/fe/array/)と[疑似言語の読み方](/fe/pseudocode-reading-guide/)も参考になります。

## よくある誤解・混同

| 誤解 | 正しい理解 |
|---|---|
| aには元の行列の値が入る | aは**行番号 i**を記録する |
| bは必ず1, 2, 3, ...と増える | bは**列番号 j**。行が変わると小さく戻ることもある |
| 0の要素も追加する | 条件が「0以外」のため追加しない |
| a、b、cを別々のデータとして読む | **同じ添字の3つ**が1組の要素 |
| 疎行列と隣接行列は同じ | 疎行列は0が多いという性質、[隣接行列](/fe/adjacency-matrix/)はグラフの接続を表す方法 |

特に、sparseMatrix[1]のような式が登場したら、**元の行列の1行目なのか、変換後の3配列の1番目なのか**を、初期化処理から確認します。

## まとめ（試験直前用）

- 疎行列は、0の要素が多い行列
- 3配列で表す方法では、**行番号・列番号・値**を同じ順番で保存する
- 二重ループは、**外側の行 i → 内側の列 j**の順で追う
- 条件が「0以外」なら、0は追加しない
- 選択肢の違いを探し、必要なところだけトレースする

{% include fe_article_footer.html %}
