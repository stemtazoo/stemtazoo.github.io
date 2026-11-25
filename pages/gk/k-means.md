---
layout: page
title: k-means法とは？教師なし学習とクラスタリングの基本【G検定対策】
description: "k-means法を、ラベルを使わずデータをk個のクラスタへ分ける代表的な非階層型クラスタリングとして整理します。重心の更新、kを事前に決める点、階層型クラスタリングやk-NNとの違いをG検定の判断軸で確認します。"
permalink: /gk/k-means/
tags: [gk, clustering]
gk_section: 機械学習の概要/代表的な手法/教師なし学習/クラスタリング
gk_order: 1
last_modified_at: 2026-11-25
---

## まず結論

**k-means法**は、ラベルを使わずにデータを**k個のクラスタへ分ける、代表的な非階層型クラスタリング**です。

G検定では、次の3点で切り分けます。

- **ラベルを使わない** → 教師なし学習
- **クラスタ数 k を先に決める** → k-means
- **階層構造を作らない** → 非階層型クラスタリング

## 直感的な説明

k-meansは、データを「近いもの同士でk個のグループに分ける」方法です。

1. k個の中心を置く
2. 各データを最も近い中心へ割り当てる
3. 各グループの重心を新しい中心にする
4. 割り当てと中心の更新を繰り返す

正解ラベルを見て分類するのではなく、**データ同士の位置関係からグループを作る**のがポイントです。

## 定義・仕組み

k-meansでは、各データ点と所属クラスタの重心との距離が小さくなるようにクラスタを作ります。

基本的な流れは次の通りです。

1. クラスタ数 k を決める
2. k個の初期重心を設定する
3. 各データを最も近い重心へ割り当てる
4. 各クラスタの重心を再計算する
5. 割り当てがほぼ変わらなくなるまで繰り返す

**kはクラスタ数**です。近傍数を表す[k-NN](/gk/k-means-vs-knn/)のkとは意味が違います。

### 触って覚える：点の割り当てと重心の更新

「近い中心に割り当てる」を押し、どの点がA・Bのどちらに入るか見てください。次に「重心を更新する」を押すと、点の所属を保ったまま各中心がグループ内の点の平均へ動きます。

<link rel="stylesheet" href="{{ '/assets/css/first-step-demos.css' | relative_url }}">
<div class="first-step-demo" data-first-step="kmeans" hidden>
  <div class="first-step-demo__actions">
    <button type="button" data-action="next">近い中心に割り当てる</button>
    <button type="button" data-action="reset">最初から</button>
  </div>
  <svg viewBox="0 0 300 105" role="img" aria-label="数直線上の点と中心A・B" data-board></svg>
  <p role="status" data-result></p>
</div>
<noscript><p>数直線の点1・2・4・6・9・10を、中心A＝1、B＝4に割り当てると、Aは1・2、Bは4・6・9・10です。次の重心はA＝1.5、B＝7.25になり、再割り当てでは点4がAに移ります。</p></noscript>

この例では計算を追いやすいよう、1次元の点を2グループに分けます。

<script defer src="{{ '/assets/js/first-step-demos.js' | relative_url }}"></script>

## いつ使う？（得意・不得意）

### 得意な場面

- 顧客やデータのグループ分け
- ラベルのないデータから大まかな構造を見つけたい
- 比較的まとまりのよいクラスタを分けたい

### 注意点

- クラスタ数 k を事前に決める必要がある
- 初期重心によって結果が変わることがある
- 外れ値の影響を受けやすい
- 球状で大きさが近いクラスタは扱いやすいが、複雑な形のクラスタは苦手

## G検定ひっかけポイント

- ❌「正解ラベルを使って分類する」→ 教師あり学習の分類
- ❌「デンドログラムを作る」→ 階層型クラスタリング
- ❌「kは参照する近傍数」→ k-NN
- ⭕「k個の重心を更新しながら分ける」→ k-means
- ⭕「教師なし＋非階層型」→ k-meansの基本分類

## まとめ（試験直前用）

- k-means＝**教師なしのクラスタリング**
- **非階層型**で、クラスタ数 k を先に決める
- 各クラスタの**重心**を更新して分割する
- k-NNのkは近傍数、k-meansのkはクラスタ数
- **「ラベルなし＋k個＋重心」ならk-means**

## 参考資料（原論文）

- [Some Methods for Classification and Analysis of Multivariate Observations｜UC Berkeley](https://digicoll.lib.berkeley.edu/record/113015)
  - MacQueen（1967）によるk-meansの代表的な原典です。データをk個のクラスタへ分け、クラスタ中心を反復更新する考え方を示しています。

{% include gk_article_footer.html %}
