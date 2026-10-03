---
layout: page
title: 前判定・後判定の繰返しとは？双岐選択・多岐選択との違い【基本情報技術者試験】
description: プログラムの制御構造を、前判定繰返し・後判定繰返し・双岐選択・多岐選択に分けて整理します。「0回あり」「最低1回」などFE試験で選択肢を切る判断基準を図解します。
permalink: /fe/control-structures-loop-selection/
tags: [fe, fe-technology, algorithm, programming, pseudocode]
fe_section: 科目B対策
fe_subsection: アルゴリズム
fe_order: 61
date: 2026-10-03
last_modified_at: 2026-10-03
---

## まず結論

制御構造の問題では、名前を丸暗記するより、**条件をいつ判定するか／何個の処理から選ぶか**で切り分けます。

| 制御構造 | 判断基準 |
|---|---|
| 前判定繰返し | **処理の前**に判定 → 0回の可能性あり |
| 後判定繰返し | **処理の後**に判定 → 最低1回は実行 |
| 双岐選択 | 条件によって**2つ**の処理から選ぶ |
| 多岐選択 | 条件によって**複数**の処理から選ぶ |

特に重要なのは、**前判定繰返しは処理を1回も実行しないことがある**という点です。

## 直感的な説明

前判定と後判定の違いは、「入口でチェックするか、処理した後でチェックするか」です。

<div class="control-compare">
  <div class="control-card">
    <strong>前判定</strong>
    <span class="control-node">条件判定</span>
    <span>↓ 続ける</span>
    <span class="control-node">処理</span>
    <small>最初の判定が偽なら<br><b>0回</b>で終了</small>
  </div>
  <div class="control-card">
    <strong>後判定</strong>
    <span class="control-node">処理</span>
    <span>↓</span>
    <span class="control-node">条件判定</span>
    <small>判定より先に処理するので<br><b>最低1回</b></small>
  </div>
</div>

試験中は、

```text
前判定 → 0回あり
後判定 → 最低1回
```

まで圧縮して思い出せれば十分です。

## 定義・仕組み

### 前判定繰返し

繰返し処理の**先頭で条件を判定**します。

Pythonの `while` もこの考え方です。

```python
while 条件:
    処理
```

最初から条件が成立しなければ、処理は一度も実行されません。

```text
条件判定
├─ 真 → 処理 → 条件判定へ戻る
└─ 偽 → 終了
```

### 後判定繰返し

先に処理を実行して、その**後で条件を判定**します。

```text
処理
 ↓
条件判定
├─ 続ける → 処理へ戻る
└─ 終了
```

最初の条件判定より前に処理を通るため、**少なくとも1回は処理されます**。

### 双岐選択

条件によって、**2つの処理のどちらか**を選びます。

```text
       条件
      ／  ＼
    真      偽
    ↓       ↓
  処理A   処理B
```

「前の処理へ戻る」という意味ではありません。

### 多岐選択

条件によって、**3つ以上を含む複数の候補から処理を選ぶ**構造です。

```text
          条件
      ／   │   ＼
    A      B      C
    ↓      ↓      ↓
  処理1  処理2  処理3
```

「複数の処理を並列に実行する」という意味ではありません。

## 科目Aでどう出る？

文章だけで正誤を判断させる問題では、次の特徴語を探します。

```text
「先頭で条件判定」 → 前判定
「最後で条件判定」 → 後判定

「2つから選択」    → 双岐選択
「複数から選択」   → 多岐選択
```

例えば、

> 前判定繰返しでは、繰返し処理の本体を1回も実行しないことがある。

これは正しい説明です。

最初の条件判定で終了すれば、処理本体には入りません。

一方、

> 多岐選択では、二つ以上の処理を並列に行う。

は誤りです。**選択と並列実行は別の概念**です。

## 科目Bでどう使う？

科目Bでループをトレースするときも、最初に**条件判定の位置**を確認します。

```text
条件が先
↓
0回の可能性を考える

処理が先
↓
最初の1回は必ず実行
```

特に初期値の時点で条件が偽になっている問題では、この違いだけで実行回数が1回ずれることがあります。

条件分岐については、[条件分岐の判定順序](/fe/condition-branch-order/)も合わせて確認すると、選択構造の読み方を整理できます。

## よくある誤解・混同

| 誤解 | 正しい見方 |
|---|---|
| 後判定は最初に条件を見る | **処理の後**に条件を見る |
| 前判定でも必ず1回は処理する | 最初の判定が偽なら**0回** |
| 双岐選択は前へ戻るか次へ進むかを選ぶ | **2つの処理**から選ぶ |
| 多岐選択は複数処理を同時実行する | 複数候補から**処理を選ぶ** |

「繰返し」と「選択」を混ぜないことも重要です。

```text
繰返し → 同じ処理へ戻る
選択   → どの処理へ進むか決める
```

## まとめ（試験直前用）

- **前判定**：判定 → 処理。0回の可能性あり
- **後判定**：処理 → 判定。最低1回
- **双岐・多岐**：「同時実行」ではなく、条件によって処理を選ぶ

<style>
.control-compare{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.5rem 0}
.control-card{border:1px solid #ccc;border-radius:10px;padding:1rem;text-align:center;display:flex;flex-direction:column;gap:.55rem}
.control-card>strong{font-size:1.1rem}
.control-node{border:1px solid #aaa;border-radius:6px;padding:.55rem;background:#f5f5f5}
.control-card small{margin-top:.4rem}
@media(max-width:560px){.control-compare{grid-template-columns:1fr}}
</style>

{% include fe_article_footer.html %}
