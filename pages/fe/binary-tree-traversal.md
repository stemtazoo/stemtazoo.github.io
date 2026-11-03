---
layout: page
title: 二分木の走査とは？先行順・中間順・後行順の違い【基本情報技術者試験】
description: 二分木の走査を、根を記録するタイミングで整理します。同じ木から先行順・中間順・後行順を求め、左部分木全体を処理する意味を確認。幅優先のレベル順との違いや、二分探索木を中間順でたどると昇順になる理由、子が片方だけの場合の扱いを押さえ、科目Aの順序問題に備えます。
permalink: /fe/binary-tree-traversal/
tags: [fe, fe-technology, algorithm, data-structure]
fe_section: テクノロジ系
fe_subsection: アルゴリズムとプログラミング
fe_order: 50
date: 2026-10-04
last_modified_at: 2026-11-03
---

## まず結論

**二分木の走査は、木の各節点を決められた順序で処理することです。** 代表的な先行順・中間順・後行順は、左部分木と右部分木を調べる間の、どの時点で根を処理するかが異なります。

このページでは「処理する」を、**節点の名前を一度記録すること**として説明します。

> **先行順＝根・左・右、中間順＝左・根・右、後行順＝左・右・根。**

「左」「右」は直接の子だけではなく、それぞれの**部分木全体**です。科目Aでは、各部分木にも同じ規則を繰り返し適用します。

## 直感的な説明

ある節点を基準にすると、記録するタイミングは次の三つに分けられます。

- 子を調べる前に自分を記録する → 先行順
- 左側を調べ終え、右側を調べる前に自分を記録する → 中間順
- 左右を両方調べ終えてから自分を記録する → 後行順

どの方法でも同じ木をたどります。違うのは、**どこへ移動するかだけでなく、いつ記録するか**です。

## 定義・仕組み

### 節点・根・部分木

木を構成する点を**節点（ノード）**、最上位の節点を**根**といいます。二分木では、各節点が左の子と右の子を最大一つずつ持ちます。子がない節点を**葉**といいます。

左の子を根とする木全体が左部分木、右の子を根とする木全体が右部分木です。部分木の中にも、その部分木の根と左右の部分木があります。

次の木を例にします。

```text
        A
       / \
      B   C
     / \   \
    D   E   F
   /
  G
```

Aの左部分木はB・D・E・G、右部分木はC・Fです。Dは左の子Gだけを持ち、Cは右の子Fだけを持ちます。これ以外の子はありません。

### 三つの走査順序

| 方法 | 各部分木での処理順 | この木の記録順序 |
|---|---|---|
| 先行順（preorder） | 根 → 左部分木 → 右部分木 | A → B → D → G → E → C → F |
| 中間順（inorder） | 左部分木 → 根 → 右部分木 | G → D → B → E → A → C → F |
| 後行順（postorder） | 左部分木 → 右部分木 → 根 | G → D → E → B → F → C → A |

先行順は前順・行きがけ順、中間順は通りがけ順、後行順は後順・帰りがけ順とも呼ばれます。名称に迷ったら、問題文の処理順を確認します。

### 触って覚える：同じ二分木を3つの順序で走査する

**次に記録する節点はどれでしょうか？**

1. 先行順・中間順・後行順から方式を選びます。
2. 次に記録する節点を予想してから「次へ」を押します。
3. 木の強調表示と記録順を確認し、方式を切り替えて比較します。

**見るポイント：** 木の節点を通過していても、その時点で節点名を記録するとは限りません。中間順なら左部分木の記録が終わってから、後行順なら左右の部分木が終わってから根を記録します。

<link rel="stylesheet" href="{{ '/assets/css/fe-tree-traversal.css' | relative_url }}">

<div class="fe-tree-demo" id="fe-tree-traversal-demo" aria-label="二分木の走査を1ステップずつ確認する">
  <p class="fe-tree-demo__step">① 走査方法を選ぶ</p>
  <div class="fe-tree-demo__controls">
    <label for="fe-tree-mode">比較する走査方法
      <select id="fe-tree-mode">
        <option value="pre">先行順：根 → 左 → 右</option>
        <option value="inside">中間順：左 → 根 → 右</option>
        <option value="post">後行順：左 → 右 → 根</option>
      </select>
    </label>
  </div>
  <div class="fe-tree-demo__visual">
    <svg viewBox="0 0 420 270" role="img" aria-label="根A。Aの左がB、右がC。Bの左がD、右がE。Cの右がF。Dの左がG。">
      <g aria-hidden="true">
        <line class="fe-tree-demo__edge" data-tree-edge="A-B" x1="210" y1="31" x2="112" y2="93"/>
        <line class="fe-tree-demo__edge" data-tree-edge="A-C" x1="210" y1="31" x2="308" y2="93"/>
        <line class="fe-tree-demo__edge" data-tree-edge="B-D" x1="112" y1="93" x2="59" y2="159"/>
        <line class="fe-tree-demo__edge" data-tree-edge="B-E" x1="112" y1="93" x2="165" y2="159"/>
        <line class="fe-tree-demo__edge" data-tree-edge="C-F" x1="308" y1="93" x2="355" y2="159"/>
        <line class="fe-tree-demo__edge" data-tree-edge="D-G" x1="59" y1="159" x2="28" y2="230"/>
      </g>
      <g class="fe-tree-demo__node" data-tree-node="A" data-state="idle"><circle cx="210" cy="31" r="22"/><text x="210" y="32">A</text></g>
      <g class="fe-tree-demo__node" data-tree-node="B" data-state="idle"><circle cx="112" cy="93" r="22"/><text x="112" y="94">B</text></g>
      <g class="fe-tree-demo__node" data-tree-node="C" data-state="idle"><circle cx="308" cy="93" r="22"/><text x="308" y="94">C</text></g>
      <g class="fe-tree-demo__node" data-tree-node="D" data-state="idle"><circle cx="59" cy="159" r="22"/><text x="59" y="160">D</text></g>
      <g class="fe-tree-demo__node" data-tree-node="E" data-state="idle"><circle cx="165" cy="159" r="22"/><text x="165" y="160">E</text></g>
      <g class="fe-tree-demo__node" data-tree-node="F" data-state="idle"><circle cx="355" cy="159" r="22"/><text x="355" y="160">F</text></g>
      <g class="fe-tree-demo__node" data-tree-node="G" data-state="idle"><circle cx="28" cy="230" r="22"/><text x="28" y="231">G</text></g>
    </svg>
    <div class="fe-tree-demo__key" aria-label="色の意味">
      <span><span class="fe-tree-demo__swatch fe-tree-demo__swatch--current"></span>今回記録した節点</span>
      <span><span class="fe-tree-demo__swatch fe-tree-demo__swatch--done"></span>記録済み</span>
      <span><span class="fe-tree-demo__swatch fe-tree-demo__swatch--ancestor"></span>通過中の上位節点</span>
    </div>
  </div>
  <p class="fe-tree-demo__step">② 次の節点を予想する</p>
  <div class="fe-tree-demo__controls">
    <label for="fe-tree-guess">次に記録されるのは？
      <select id="fe-tree-guess">
        <option value="">予想しないで進むこともできます</option>
        <option value="A">A</option><option value="B">B</option><option value="C">C</option>
        <option value="D">D</option><option value="E">E</option><option value="F">F</option><option value="G">G</option>
      </select>
    </label>
  </div>
  <p class="fe-tree-demo__step">③ 1節点ずつ記録して確認する</p>
  <div class="fe-tree-demo__actions">
    <button type="button" class="fe-tree-demo__primary" id="fe-tree-next">次へ（1節点記録）</button>
    <button type="button" id="fe-tree-back">1節点戻る</button>
    <button type="button" id="fe-tree-reset">最初から</button>
  </div>
  <div class="fe-tree-demo__result">
    <p id="fe-tree-progress">先行順： 0 / 7 節点を記録</p>
    <p id="fe-tree-feedback" class="fe-tree-demo__feedback" role="status" aria-live="polite">次に記録する節点を予想してから「次へ」を押しましょう。</p>
    <p><strong>記録した順番：</strong> <output id="fe-tree-output" class="fe-tree-demo__output">まだ記録していません。</output></p>
    <p id="fe-tree-reason">線をたどる順番と、節点名を記録するタイミングは同じとは限りません。</p>
  </div>
</div>
<noscript>
  <p>JavaScriptが無効の場合は、直前の「三つの走査順序」の表を確認してください。先行順は A→B→D→G→E→C→F、中間順は G→D→B→E→A→C→F、後行順は G→D→E→B→F→C→A です。</p>
</noscript>
<script src="{{ '/assets/js/fe-tree-traversal.js' | relative_url }}" defer></script>

### 中間順を部分木に分けて求める

中間順なら、Aの左部分木をすべて記録してからAを書き、その後に右部分木を記録します。

| 対象 | 中間順での考え方 | 得られる並び |
|---|---|---|
| Dを根とする部分木 | 左のG → D → 右は空 | G・D |
| Bを根とする部分木 | 左のD部分木 → B → 右のE | G・D・B・E |
| Cを根とする部分木 | 左は空 → C → 右のF | C・F |
| 木全体 | 左のB部分木 → A → 右のC部分木 | G・D・B・E・A・C・F |

**見るポイント：「左を処理する」は、Bだけを書いて終わることではありません。Bの下にあるD・G・Eも同じ規則で処理します。**

子がない側は何も記録せずに飛ばします。左右どちらにも子がない葉は、どの方法でもその節点を一度だけ記録します。

### 根を置く位置を変えて考える

全体を三つのまとまりに分けると、順序を確認しやすくなります。

| 方法 | 左部分木の記録 | 根 | 右部分木の記録 | 全体の組立て |
|---|---|---|---|---|
| 先行順 | B・D・G・E | A | C・F | A ＋ B・D・G・E ＋ C・F |
| 中間順 | G・D・B・E | A | C・F | G・D・B・E ＋ A ＋ C・F |
| 後行順 | G・D・E・B | A | F・C | G・D・E・B ＋ F・C ＋ A |

この表の「＋」は、並びを順につなぐ意味です。**各部分木の中の記録順も、その走査方法に合わせて変わる**ことに注意します。先行順の並びのAだけを末尾へ移しても、後行順にはなりません。

## 科目Aでどう出る？

### 順序問題を解く手順

1. 先行順・中間順・後行順のどれかを確認する。
2. 木を、左部分木・根・右部分木に分ける。
3. 各部分木にも同じ規則を適用し、並びを組み立てる。
4. 全節点が一度ずつ現れ、抜けや重複がないかを確認する。

先行順なら木全体の根は最初、後行順なら最後です。中間順なら左部分木の全節点が根より前、右部分木の全節点が根より後に現れます。

ただし、**根の位置だけで正答を決めない**ようにします。各部分木の内部も、指定された規則になっている必要があります。

### 幅優先のレベル順との違い

木を浅い層から順に記録する方法を、**レベル順**といいます。上の木では、同じ層を左から処理するとA・B・C・D・E・F・Gです。

先行順・中間順・後行順は深さ優先のたどり方に対応し、レベル順は幅優先に対応します。[深さ優先探索と幅優先探索の違い](/fe/dfs-vs-bfs/)では、進み方とスタック・キューの関係を比較しています。

## どんな場面で使う？

先行順は、親の情報を先に扱ってから子へ進む処理に使えます。後行順は、子の結果をそろえてから親の値を計算する処理に適しています。例えば、演算子を親、計算対象を子とした式の木を、下から計算するときの考え方です。

中間順には、**二分探索木をたどると値が昇順に並ぶ**という用途があります。重複しない値を持ち、左部分木の値が根より小さく、右部分木の値が根より大きい二分探索木なら、左・根・右の順で小さい値から記録できます。

この大小関係と探索・挿入の手順は、[2分探索木とは？](/fe/binary-search-tree/)で確認できます。

## よくある誤解・混同

### 中間順なら、どんな二分木でも値が昇順になる？

昇順になるのは、二分探索木の大小関係を満たす場合です。一般の二分木では、左側の値が小さいとは限りません。

### 中間順は、図を左から右へ見て名前を並べればよい？

図の描き方や節点の位置に頼ると誤ります。左部分木全体を処理してから根を記録する、という構造上の規則で判断します。

### 後行順は、先行順を単純に逆にしたもの？

違います。左から先に処理する規則は共通で、根の記録が最後になります。上の例の先行順を逆にするとF・C・E・G・D・B・Aとなり、後行順のG・D・E・B・F・C・Aとは一致しません。

### 「訪れる」と「記録する」は同じ？

設問の定義を確認する必要があります。中間順や後行順では、根を経由して子へ進んでも、その時点では根を記録しません。移動順序と、出力・記録のタイミングを区別します。

## 確認問題（科目A・オリジナル）

次の二分木を、左部分木・右部分木・根の順に処理する後行順で走査する。節点を記録する順序として適切なものはどれか。Bは右の子Dだけを持ち、Cは左の子Eだけを持つ。

```text
        A
       / \
      /   \
     B     C
      \   /
       D E
```

- ア：A・B・D・C・E
- イ：B・D・A・E・C
- ウ：D・B・E・C・A
- エ：A・B・C・D・E

**正解：ウ**

- ア：根を先に記録する先行順です。
- イ：左部分木・根・右部分木の中間順です。
- ウ：B側はD・B、C側はE・Cと記録し、最後に全体の根Aを記録します。
- エ：浅い層から記録するレベル順です。

## 公式情報・参考リンク

- [IPA：基本情報技術者試験シラバス Ver.9.2](https://www.ipa.go.jp/shiken/syllabus/omgdg50000005kpe-att/syllabus_fe_ver9_2.pdf)
  - アルゴリズムとプログラミングの、木構造や探索に関する学習範囲を確認できます。
- [NIST：preorder traversal](https://xlinux.nist.gov/dads/HTML/preorderTraversal.html)
  - 根を先に処理してから部分木を処理する先行順の定義です。
- [NIST：in-order traversal](https://xlinux.nist.gov/dads/HTML/inorderTraversal.html)
  - 左部分木、根、右部分木の順で処理する中間順の定義です。
- [NIST：postorder traversal](https://xlinux.nist.gov/dads/HTML/postorderTraversal.html)
  - 部分木を処理し終えてから根を処理する後行順の定義です。

## まとめ（試験直前用）

- **先行順＝根・左・右、中間順＝左・根・右、後行順＝左・右・根。**
- 左右は直接の子だけではなく、部分木全体を指す。
- 各部分木にも同じ規則を適用し、空の子は飛ばす。
- 浅い層から記録するレベル順は、幅優先の順序。
- 中間順で昇順になるのは、二分探索木の大小関係を満たす場合。

{% include fe_article_footer.html %}
