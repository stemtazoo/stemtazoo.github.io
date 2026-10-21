---
layout: page
title: 2分探索木とは？左右の大小関係と探索・挿入手順【基本情報技術者試験】
description: 2分探索木の左右の部分木全体の大小関係を整理。探索・挿入に加え、削除時に候補9・10・13・14を試して違反箇所を図解し、1個だけ移動できる条件と木の再構成を科目Aの判断につなげます。
permalink: /fe/binary-search-tree/
tags: [fe, fe-technology, data-structure, algorithm]
fe_section: 科目B対策
fe_subsection: データ構造
fe_order: 40
date: 2026-07-13
last_modified_at: 2026-10-21
---

## まず結論

**2分探索木**は、各節点について、**左部分木のすべての値がその節点より小さく、右部分木のすべての値が大きい**という関係を保つ木構造です。

探索や挿入では、根から始めて、現在の節点より小さければ左、大きければ右へ進みます。**直接の子だけでなく、部分木全体で大小関係を満たすこと**が重要です。

英語では binary search tree（BST）と呼びます。このページでは重複しない値を扱い、挿入後の回転などによる自動的な平衡化は行わないものとします。

## 直感的な説明

50を根に置いた木に、35を入れるとします。根の50より小さいので左へ進みますが、そこで終わりではありません。

左の子が30なら、35は30より大きいので右へ進みます。さらに右の子が40なら、35は40より小さいので左へ進みます。その位置が空いていれば35を追加します。

**「根と比較 → 移動先と比較 → 空いている位置に追加」**を繰り返すイメージです。

次の例では、空の木へ **50、70、30、20、60、40、35** の順に挿入します。「次の比較・追加」で一つずつ操作を追えます。

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}">

<div class="fe-learning-demo fe-bst-demo" data-fe-bst-demo data-bst-values="50,70,30,20,60,40,35">
  <p class="fe-learning-demo__title">触って確認：比較する節点を追って挿入する</p>
  <p>挿入順：50 → 70 → 30 → 20 → 60 → 40 → 35</p>
  <svg class="fe-bst-demo__tree" viewBox="0 0 420 300" role="img" aria-label="完成した木。根50、左の子30、右の子70。30の左は20、右は40。70の左は60。40の左は35。">
    <g class="fe-bst-demo__edge" data-bst-child="30"><line x1="210" y1="35" x2="105" y2="105"></line></g>
    <g class="fe-bst-demo__edge" data-bst-child="70"><line x1="210" y1="35" x2="315" y2="105"></line></g>
    <g class="fe-bst-demo__edge" data-bst-child="20"><line x1="105" y1="105" x2="45" y2="175"></line></g>
    <g class="fe-bst-demo__edge" data-bst-child="40"><line x1="105" y1="105" x2="165" y2="175"></line></g>
    <g class="fe-bst-demo__edge" data-bst-child="60"><line x1="315" y1="105" x2="255" y2="175"></line></g>
    <g class="fe-bst-demo__edge" data-bst-child="35"><line x1="165" y1="175" x2="125" y2="245"></line></g>
    <g class="fe-bst-demo__node" data-bst-value="50"><circle cx="210" cy="35" r="23"></circle><text x="210" y="41">50</text></g>
    <g class="fe-bst-demo__node" data-bst-value="70"><circle cx="315" cy="105" r="23"></circle><text x="315" y="111">70</text></g>
    <g class="fe-bst-demo__node" data-bst-value="30"><circle cx="105" cy="105" r="23"></circle><text x="105" y="111">30</text></g>
    <g class="fe-bst-demo__node" data-bst-value="20"><circle cx="45" cy="175" r="23"></circle><text x="45" y="181">20</text></g>
    <g class="fe-bst-demo__node" data-bst-value="60"><circle cx="255" cy="175" r="23"></circle><text x="255" y="181">60</text></g>
    <g class="fe-bst-demo__node" data-bst-value="40"><circle cx="165" cy="175" r="23"></circle><text x="165" y="181">40</text></g>
    <g class="fe-bst-demo__node" data-bst-value="35"><circle cx="125" cy="245" r="23"></circle><text x="125" y="251">35</text></g>
  </svg>
  <p class="fe-bst-demo__status" data-bst-status role="status" aria-live="polite">図は全7個を挿入した完成形です。操作が有効になると、空の木から挿入過程を確認できます。</p>
  <div class="fe-learning-demo__controls">
    <button type="button" class="fe-learning-demo__button" data-bst-next disabled>次の比較・追加</button>
    <button type="button" class="fe-learning-demo__button" data-bst-reset disabled>最初から</button>
  </div>
  <p class="fe-learning-demo__hint">見るポイント：太い実線の節点は比較中、破線の節点は追加直後です。文章でも比較と挿入位置を確認できます。</p>
</div>

<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}" defer></script>

## 定義・仕組み

### 子と部分木の違い

2分木は、各節点の子が最大2個の木です。一番上の節点を**根**、子を持たない節点を**葉**と呼びます。ある子と、その子から下につながる節点全体が**部分木**です。

2分探索木では、各節点で次の条件を保ちます。

- 左部分木のすべての値は、その節点より小さい。
- 右部分木のすべての値は、その節点より大きい。

例えば50の左部分木に35があれば、35は50より小さくなければなりません。さらに35が30の右部分木に属するなら、30より大きいことも必要です。**祖先の節点との関係も引き継ぐ**点を押さえます。

### 探索する手順

完成した例の木から35を探す場合は、次の順で比較します。

| 比較する節点 | 判断 | 次の動作 |
|---|---|---|
| 50 | 35 < 50 | 左の子30へ |
| 30 | 35 > 30 | 右の子40へ |
| 40 | 35 < 40 | 左の子35へ |
| 35 | 35 = 35 | 発見して終了 |

進む先が空なら、目的の値は存在しません。左右を両方探す必要がないのは、部分木全体の大小関係が保たれているためです。

### 挿入する手順

値を挿入する場合も探索と同じように比較します。進む先が空になった位置に、新しい節点を追加します。木が空なら最初の値を根にします。

| 挿入する値 | 根からの比較 | 挿入位置 |
|---|---|---|
| 50 | 木が空 | 根 |
| 70 | 70 > 50 | 50の右の子 |
| 30 | 30 < 50 | 50の左の子 |
| 20 | 20 < 50、20 < 30 | 30の左の子 |
| 60 | 60 > 50、60 < 70 | 70の左の子 |
| 40 | 40 < 50、40 > 30 | 30の右の子 |
| 35 | 35 < 50、35 > 30、35 < 40 | 40の左の子 |

**新しい値の比較は、毎回根から始めます。** 直前に追加した節点から始めたり、途中で既存の値を並べ替えたりはしません。

性質は[NIST DADS：binary search tree](https://xlinux.nist.gov/dads/HTML/binarySearchTree.html)、探索・挿入と挿入順による形の違いは[Princeton大学：Binary Search Trees](https://algs4.cs.princeton.edu/32bst/)で確認できます。

### 左右に子がある節点を削除するとき

削除する節点に子がない場合は、その節点を外します。子が一つなら、子を削除位置につなぎます。**子が二つある場合**は、ほかの値との大小関係を保てる代わりの節点を選びます。

代表的な候補は、**左部分木の最大値（直前の値）**と**右部分木の最小値（直後の値）**です。これらは、削除した位置に移しても部分木全体の大小関係を保てます。移動元の節点に子がある場合は、その子のつなぎ替えも必要です。

「値を上から順番にずらす」操作ではありません。今回の例は、候補の13が葉（子を持たない節点）なので、元の場所から外して12の位置へ直接移せます。**移す節点の数が1個**という条件と、実装上の参照の付け替え回数は区別しましょう。

## 科目Aでどう出る？

### 「正しい木」と「指定順でできる木」を分ける

科目Aでは、木の条件を満たすかどうかと、与えられた順で挿入してできるかどうかを区別します。

例えば、30、50、70を格納する2分探索木には、50を根にして左右に30と70を置く形も、30を根にして右に50、その右に70を置く形もあります。どちらも条件を満たします。

しかし、空の木に**50、30、70の順**で通常の挿入を行うなら、根は最初の50です。30を根にした木は、この挿入順の結果ではありません。

指定順の問題では、次の順で確認します。

1. 最初の値が根になっているか。
2. 次の値を根から比較し、空いた子の位置まで進めるか。
3. 追加済みの節点を移動せず、その後の値も同じ手順で入れているか。

### 削除後、ほかの要素を移動せずに再構成できる候補は？

次は、12を削除し、その位置に **9・10・13・14のどれか1個だけ**を移す問題です。選択した値を12の位置に仮置きし、違反する値を赤く示します。

<div class="fe-learning-demo fe-bst-delete" data-fe-bst-delete-demo>
  <p class="fe-learning-demo__title">触って比較：12の位置にどの値を移せる？</p>
  <p><strong>条件：</strong>12を削除し、ほかの値を並べ替えずに、候補1個をその位置へ直接移します。違反する節点を探しましょう。</p>
  <div class="fe-bst-delete__choices" role="group" aria-label="12の代わりに移す候補">
    <button type="button" class="fe-learning-demo__button" data-bst-delete-choice="9" aria-pressed="false">9を試す</button>
    <button type="button" class="fe-learning-demo__button" data-bst-delete-choice="10" aria-pressed="false">10を試す</button>
    <button type="button" class="fe-learning-demo__button" data-bst-delete-choice="13" aria-pressed="false">13を試す</button>
    <button type="button" class="fe-learning-demo__button" data-bst-delete-choice="14" aria-pressed="false">14を試す</button>
  </div>
  <svg class="fe-bst-delete__tree" viewBox="0 0 454 335" role="img" aria-label="6の右部分木。8の左は7、右は12。12の左は10で子は9と11、12の右は14で子は13と15。">
    <line class="fe-bst-delete__edge" x1="111" y1="38" x2="50" y2="118"></line>
    <line class="fe-bst-delete__edge" x1="111" y1="38" x2="288" y2="118"></line>
    <line class="fe-bst-delete__edge" x1="288" y1="118" x2="212" y2="205"></line>
    <line class="fe-bst-delete__edge" x1="288" y1="118" x2="372" y2="205"></line>
    <line class="fe-bst-delete__edge" x1="212" y1="205" x2="164" y2="290" data-bst-delete-edge-from="9"></line>
    <line class="fe-bst-delete__edge" x1="212" y1="205" x2="254" y2="290"></line>
    <line class="fe-bst-delete__edge" x1="372" y1="205" x2="326" y2="290" data-bst-delete-edge-from="13"></line>
    <line class="fe-bst-delete__edge" x1="372" y1="205" x2="414" y2="290"></line>
    <g class="fe-bst-delete__node"><circle cx="111" cy="38" r="21"></circle><text x="111" y="44">8</text></g>
    <g class="fe-bst-delete__node"><circle cx="50" cy="118" r="21"></circle><text x="50" y="124">7</text></g>
    <g class="fe-bst-delete__node fe-bst-delete__target" data-bst-delete-target><circle cx="288" cy="118" r="22"></circle><text x="288" y="124" data-bst-delete-target-value>12</text></g>
    <g class="fe-bst-delete__node" data-bst-delete-node="10"><circle cx="212" cy="205" r="21"></circle><text x="212" y="211">10</text></g>
    <g class="fe-bst-delete__node" data-bst-delete-node="14"><circle cx="372" cy="205" r="21"></circle><text x="372" y="211">14</text></g>
    <g class="fe-bst-delete__node" data-bst-delete-node="9"><circle cx="164" cy="290" r="21"></circle><text x="164" y="296">9</text></g>
    <g class="fe-bst-delete__node" data-bst-delete-node="11"><circle cx="254" cy="290" r="21"></circle><text x="254" y="296">11</text></g>
    <g class="fe-bst-delete__node" data-bst-delete-node="13"><circle cx="326" cy="290" r="21"></circle><text x="326" y="296">13</text></g>
    <g class="fe-bst-delete__node" data-bst-delete-node="15"><circle cx="414" cy="290" r="21"></circle><text x="414" y="296">15</text></g>
  </svg>
  <p class="fe-bst-delete__legend">赤い節点：大小関係に違反　／　破線：選んだ節点の元の位置</p>
  <p class="fe-bst-delete__verdict" data-bst-delete-verdict aria-live="polite">候補を選ぶと判定が表示されます。</p>
  <p class="fe-bst-delete__status" data-bst-delete-status>まずは9・10・13・14を試してください。6を根とする木のうち、8の部分木を表示しています。</p>
  <p class="fe-bst-delete__hint">見るポイント：<strong>直接の子だけでなく、部分木全体</strong>を比較します。赤の図は「その候補を置いたら？」という判定用の仮配置で、完成した木ではありません。ほかの節点は自動で動きません。</p>
</div>

| 12の位置へ移す値 | 判定 | なぜ？ |
|---|---|---|
| 9 | × | 左部分木に9より大きい10と11が残る |
| 10 | × | 左部分木に10より大きい11が残る |
| 13 | ○ | 左は9・10・11、右は14・15なので成立 |
| 14 | × | 右部分木に14より小さい13が残る |

**答えは13です。** 左部分木の最大値11も候補ですが、今回は選択肢にありません。10や14を選んでも、ほかの節点をつなぎ直せば二分探索木を作ることはできます。ただし、それは設問の「別の要素をその位置に移動するだけ」とは異なります。

### 似た用語の判断軸

| 用語 | 中心となる条件・処理 |
|---|---|
| 2分木 | 各節点の子が最大2個 |
| 2分探索木 | 左部分木全体が小さく、右部分木全体が大きい |
| ヒープ | 親子間の大小関係を保つ。左右の部分木を小・大に分ける条件ではない |
| 二分探索 | 整列済み配列などの中央と比較して、探索範囲を半分に絞る |

配列の中央を調べる方法は[二分探索の記事]({{ '/fe/binary-search/' | relative_url }})、木の形や節点数・深さを扱うテーマは[完全2分木の記事]({{ '/fe/complete-binary-tree/' | relative_url }})で整理しています。

## 科目Bでどう使う？

科目Bの疑似言語では、**現在の節点を表す変数と、左・右の子への参照**を追います。探索の考え方を表す疑似コードは次のようになります。

```text
現在 ← 根
現在が空でない間、繰り返す
    目的の値 = 現在の値 なら、発見して終了
    目的の値 < 現在の値 なら、現在 ← 現在の左の子
    それ以外なら、現在 ← 現在の右の子
進む先が空になったら、見つからない
```

この疑似コードは考え方を示したものです。実際の問題では、空を表す値や参照の表現を問題文の定義に合わせて読みます。

トレースでは、次の3点を確認します。

- 大小比較の相手は、現在の節点の値か。
- 比較後に「現在」が左の子・右の子のどちらへ更新されるか。
- 一致した場合と、進む先が空の場合で、どう終了するか。

挿入のコードなら、空の子への参照に新しい節点を接続する箇所も確認します。**左右の参照を逆に更新する誤り**を見つけるには、表の35の例のように、途中で進む方向が変わる値を追うと有効です。

## よくある誤解・混同

### 削除するときは、値を1段ずつずらす必要がある？

必要ありません。配列のように隣の値を順番に詰めると考えると、移動できる候補を見落とします。二分探索木では、**右部分木の最小値などを離れた位置から直接移せる**場合があります。ただし、残りの節点が勝手に移動するわけではありません。設問が許す操作の範囲を読み分けます。

### 親子の大小関係だけ合っていればよい？

不十分です。例えば、50の左の子が30で、その30の右の子が60だったとします。30 < 50と60 > 30という直接の親子関係だけを見ると自然ですが、60は50の左部分木にあるため50より小さくなければなりません。この木は2分探索木ではありません。

### 同じ値の集合なら、いつも同じ形になる？

通常の2分探索木では、挿入順によって形が変わります。また、挿入順が違っても同じ形になる場合があります。**値の集合だけでは形が一意に決まらない**と覚えます。

### 必ず半分ずつ絞れる？

二分探索木では、左右の節点数が同じになる保証はありません。例えば10、20、30を順に挿入すると、右の子だけが続く形になります。

探索や挿入の手間は木の高さに依存します。平衡ならおおむねO(log n)、片側に偏った最悪の場合はO(n)です。nは節点数です。名前に「2分」があっても、常に候補が半分になるとは限りません。

### 同じ値を入れる場合も、必ず右へ進む？

重複する値の扱いは仕様によって異なります。同じキーの情報を更新する実装や、重複を扱う別の規則もあります。問題文に重複の扱いが指定されていれば、その規則を優先します。

## まとめ（試験直前用）

- 2分探索木は、**左部分木全体が小さく、右部分木全体が大きい**。
- 探索・挿入は根から始め、現在の節点と比較して左か右へ進む。
- 挿入は空いた子の位置で行い、指定のない並べ替えや平衡化はしない。
- 子が二つある節点の削除では、左部分木の最大値か右部分木の最小値が候補になる。
- 条件を満たす木でも、指定順の挿入結果とは限らない。
- 科目Bでは現在の節点と左右の参照を追い、偏った木では探索が遅くなる点も区別する。

{% include fe_article_footer.html %}
