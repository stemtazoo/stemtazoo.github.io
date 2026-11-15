---
layout: page
title: NANDとは？AND・OR・NOTを作れる万能ゲートの仕組み【基本情報技術者試験】
description: NANDの真理値表と万能ゲートの仕組みに加え、3個のNANDで二つのANDをORする論理式を図解。入力を切り替えて途中出力と最終出力を確かめられる教材を収録。
permalink: /fe/nand-gate/
tags: [fe, fe-technology, hardware, logic-circuit]
fe_section: テクノロジ系
fe_subsection: コンピュータ構成要素
fe_order: 89
date: 2026-08-07
last_modified_at: 2026-11-14
---

## まず結論

**NAND（Not AND）**とは、ANDの結果を反転する論理演算です。

科目Aでは、次の判断軸を押さえると選択肢を切れます。

```text
AとBが両方1
→ NANDは0

それ以外
→ NANDは1
```

論理式では、次のように表します。

```text
NAND = ¬(A・B)
```

NANDの重要な特徴は、**NANDだけでNOT・AND・ORなどの基本論理回路を作れる**ことです。

この性質から、NANDは**万能ゲート**と呼ばれます。

## 直感的な説明

NANDは、ANDの答えを最後に反対へひっくり返したものです。

ANDは、AとBの両方が1のときだけ1になります。

```text
AND
00 → 0
01 → 0
10 → 0
11 → 1
```

NANDは、この結果を反転します。

```text
NAND
00 → 1
01 → 1
10 → 1
11 → 0
```

したがって、NANDは次のように覚えられます。

```text
11のときだけ0
→ NAND
```

回路記号では、ANDゲートの出力側に小さな丸が付いた形で表されます。

```text
ANDゲート
＋
出力を反転する丸
→ NANDゲート
```

## 定義・仕組み

### NANDの真理値表

NANDの入力と出力を整理すると、次のようになります。

| A | B | AND | NAND |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

ANDの列を反転すると、NANDの列になります。

```text
AND
0 0 0 1

反転
↓

NAND
1 1 1 0
```

### 論理式

ANDは、論理積の記号を使って次のように表します。

```text
A・B
```

NANDは、その全体を否定します。

```text
¬(A・B)
```

否定の位置が重要です。

```text
¬(A・B)
→ ANDの結果全体を反転
→ NAND
```

### NANDだけでNOTを作る

NANDの2つの入力へ、同じ値Aを入れます。

```text
A NAND A
= ¬(A・A)
= ¬A
```

Aが0なら出力は1、Aが1なら出力は0になります。

| A | A NAND A |
|---:|---:|
| 0 | 1 |
| 1 | 0 |

したがって、次の対応になります。

```text
NANDの両方へ同じ入力
→ NOT
```

### NANDだけでANDを作る

最初のNANDで、ANDの結果を反転します。

```text
X = A NAND B
  = ¬(A・B)
```

次に、Xを同じNANDの両入力へ入れて、もう一度反転します。

```text
X NAND X
= ¬X
= A・B
```

つまり、NANDを2段使うとANDを作れます。

```text
A・B
↓ 反転
¬(A・B)
↓ もう一度反転
A・B
```

### 2入力NANDだけで4入力NANDを作る

4入力NANDは、4つの入力が**すべて1のときだけ0**を返す回路です。2入力NANDを5個組み合わせても構成できます。

```text
入力A、B → NAND → P = ¬(A・B)
入力C、D → NAND → Q = ¬(C・D)

PをNANDの両入力に接続 → R = ¬P = A・B
QをNANDの両入力に接続 → S = ¬Q = C・D

最後にR、SをNANDへ入力
→ Y = ¬(R・S)
    = ¬(A・B・C・D)
```

ポイントは、**NANDの両入力に同じ信号を接続するとNOTになる**ことです。途中でNANDをもう一度反転させるとANDに戻り、最後のNANDで4入力全体の論理積を反転できます。

| 入力ABCD | 4入力NANDの出力 |
|---|---:|
| 1111 | 0 |
| 1010 | 1 |
| 0000 | 1 |

試験で複数の候補回路から選ぶときは、まず `1111` を入力し、出力が0にならない回路を除外します。次に `1010` など0を含む入力を試し、出力が1にならない回路を除外します。

ただし、**一部の入力で結果が一致しても、回路全体が等価とは限りません**。最終確認は論理式の変形か、4入力なら16通りすべての真理値表で行います。

複雑な回路の途中出力を追う手順は、[NAND回路からXORを見抜く方法](/fe/nand-xor-circuit/)でも説明しています。


### NANDを3個組み合わせると「ANDの結果をOR」できる

次は、**4つの独立した入力 P・Q・R・S** を使う学習用の組合せ回路です。左の2つのNANDから出た信号を、右のNANDに入力します。元の問題図がなくても理解できるように、変数名と回路は新しく用意しています。

<figure>
  <svg viewBox="0 0 360 204" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="fe-nand-three-title fe-nand-three-desc" style="display:block;width:100%;max-width:560px;height:auto;margin:auto">
    <title id="fe-nand-three-title">NAND3個を用いた二つのANDの論理和回路</title>
    <desc id="fe-nand-three-desc">上側NANDにPとQ、下側NANDにRとSを入力。その出力UとVを右のNANDに接続し、Xを出力する。各NANDの出力に否定を意味する丸がある。</desc>
    <rect x="0" y="0" width="360" height="204" rx="8" fill="#fff"/>
    <g stroke="#293e50" fill="none" stroke-width="2" stroke-linejoin="round">
      <path d="M58 21 L82 21 A27 27 0 0 1 82 75 L58 75 Z"/>
      <circle cx="115" cy="48" r="5"/>
      <path d="M58 119 L82 119 A27 27 0 0 1 82 173 L58 173 Z"/>
      <circle cx="115" cy="146" r="5"/>
      <path d="M226 66 L249 66 A27 27 0 0 1 249 120 L226 120 Z"/>
      <circle cx="282" cy="93" r="5"/>
      <path d="M22 37 H58 M22 61 H58 M22 135 H58 M22 159 H58"/>
      <path d="M120 48 H176 V82 H226 M120 146 H176 V108 H226 M287 93 H328"/>
    </g>
    <g font-size="14" fill="#293e50">
      <text x="8" y="32">P</text><text x="8" y="58">Q</text>
      <text x="8" y="132">R</text><text x="8" y="155">S</text>
      <text x="336" y="97">X</text>
    </g>
    <g fill="#185d8b" font-size="13" font-weight="600">
      <text x="126" y="37">U</text><text x="126" y="165">V</text>
    </g>
    <g fill="#293e50" font-size="11">
      <text x="64" y="13">① NAND</text><text x="64" y="111">② NAND</text>
      <text x="226" y="58">③ NAND</text>
      <text x="10" y="191">小さな丸は、直前のAND結果の否定（NOT）</text>
    </g>
  </svg>
  <figcaption>説明用の回路図。①の出力をU、②の出力をVとし、③でNAND(U,V)を計算します。</figcaption>
</figure>

出力側の**小さな丸は否定（NOT）**です。左から順番に出力を求めます。

~~~text
① U = NOT(P・Q)
② V = NOT(R・S)
③ X = NOT(U・V)
~~~

③に①と②を代入し、**ド・モルガンの法則**を使うと、

~~~text
X = NOT( NOT(P・Q) ・ NOT(R・S) )
  = NOT(NOT(P・Q)) + NOT(NOT(R・S))
  = P・Q + R・S
~~~

となります。**「PとQが両方1」または「RとSが両方1」のときにXが1**です。4入力すべてのAND `P・Q・R・S` とは違います。

| P | Q | R | S | U = NAND(P,Q) | V = NAND(R,S) | X = NAND(U,V) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 | 1 | **1** |
| 0 | 1 | 0 | 1 | 1 | 1 | **0** |
| 1 | 1 | 1 | 1 | 0 | 0 | **1** |

この表は代表的な3組のみです。**回路と論理式が等価かを完全に確かめるには4入力の16通りを比較**します。

#### 触って覚える：入力を変えて3段階の結果を追う

まず、`P=1、Q=1、R=0、S=0` なら、最後の出力Xは0と1のどちらになるか予想してください。次に入力を変えて、各NANDの途中結果がどう変わるか確認します。

<link rel="stylesheet" href="{{ '/assets/css/fe-nand-three-gate-demo.css' | relative_url }}">

<section class="fe-nand3" data-fe-nand3 aria-label="3個のNANDゲートを操作する教材">
  <p>入力P・Q・R・Sを0または1から選び、「回路を計算」を押すと①U・②V・③Xを順番に表示します。</p>
  <div class="fe-nand3__inputs">
    <label>入力P <select data-nand3-input="p"><option value="0">0</option><option value="1" selected>1</option></select></label>
    <label>入力Q <select data-nand3-input="q"><option value="0">0</option><option value="1" selected>1</option></select></label>
    <label>入力R <select data-nand3-input="r"><option value="0" selected>0</option><option value="1">1</option></select></label>
    <label>入力S <select data-nand3-input="s"><option value="0" selected>0</option><option value="1">1</option></select></label>
  </div>
  <div class="fe-nand3__actions">
    <button type="button" data-nand3-run>回路を計算</button>
    <button type="button" data-nand3-reset>初期状態に戻す</button>
  </div>
  <div class="fe-nand3__result" data-nand3-result role="status" aria-live="polite">
    <p>まだ計算していません。まず結果を予想してから「回路を計算」を押してください。</p>
  </div>
  <noscript><p>JavaScriptが無効でも、上の論理式・回路図と3組の真理値表で各NANDを確認できます。P=1、Q=1、R=0、S=0ならU=0、V=1、X=1です。</p></noscript>
</section>
<script src="{{ '/assets/js/fe-nand-three-gate-demo.js' | relative_url }}" defer></script>

**見るポイント：** 左のNANDで一度反転した結果を、最後のNANDがもう一度反転することで、`P・Q + R・S` と同じ出力になります。すべて1の入力でもXは1です。これは**4入力NAND**（すべて1なら0）との重要な違いです。

### NANDだけでORを作る

ORは、ド・モルガンの法則を使うと次のように表せます。

```text
A+B = ¬(¬A・¬B)
```

まず、AとBをそれぞれNANDで反転します。

```text
A NAND A
→ ¬A

B NAND B
→ ¬B
```

その2つをNANDへ入力します。

```text
¬A NAND ¬B
= ¬(¬A・¬B)
= A+B
```

したがって、NANDだけでORも作れます。

### 万能ゲートと呼ばれる理由

論理回路では、NOT・AND・ORを組み合わせることで、多くの論理式を表せます。

NANDだけで、この3つをすべて作れます。

```text
NANDだけで
NOTを作れる
ANDを作れる
ORを作れる

→ 他の論理回路も構成できる
→ 万能ゲート
```

## 科目Aでどう出る？

真理値表・論理式・回路構成の特徴を次のように結び付けます。

```text
11のときだけ0
→ NAND

ANDの出力を反転
→ NAND

NANDだけでNOT・AND・ORを構成できる
→ 万能ゲート
```

## どんな場面で使う？

### デジタル回路の設計

NANDは、CPU、メモリ、制御回路などを構成する基本的な論理ゲートです。

複数種類のゲートを使わず、NANDを中心に回路を構成できれば、部品の種類をそろえやすくなります。

### 論理式の変換

科目Aでは、真理値表や論理式から、どの論理演算かを判断する問題が出ます。

```text
11だけ0
→ NAND

00だけ1
→ NOR

01と10だけ1
→ XOR
```

出力が1または0になる組合せを確認すると、用語を切り分けられます。

### ド・モルガンの法則の理解

NANDからORを作るには、ド・モルガンの法則を使います。

```text
¬(A・B) = ¬A + ¬B

¬(A+B) = ¬A・¬B
```

NANDとNORを学ぶと、否定を含む論理式の変形も理解しやすくなります。

## よくある誤解・混同

### NANDとANDを逆にしない

| A | B | AND | NAND |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

覚え方は次のとおりです。

```text
AND
→ 11だけ1

NAND
→ 11だけ0
```

NANDのNは、NOTのNと考えると分かりやすいです。

### NANDとNORの違い

NORは、ORの結果を反転する論理演算です。

| A | B | NAND | NOR |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

```text
NAND
→ 11だけ0

NOR
→ 00だけ1
```

### NANDとXORの違い

NANDとXORは、`01` と `10` のときはどちらも1です。

違いは `00` のときに現れます。

| A | B | NAND | XOR |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

```text
00のとき
NAND → 1
XOR  → 0
```

XORは「片方だけ1」、NANDは「両方1ではない」と考えると切り分けやすくなります。

### 否定する範囲に注意する

NANDは、ANDの結果全体を否定します。

```text
¬(A・B)
→ NAND
```

一方、次の式は意味が異なります。

```text
¬A・B
→ Aだけを反転してからAND
```

否定記号がどこまで掛かっているかを確認します。

### 科目Aでの切り分け

まず、出力が0になる組合せを探します。

```text
11だけ0
→ NAND

01と10だけ0ではない
→ XORではない

00だけ1ではない
→ NORではない
```

次に、論理式を確認します。

```text
¬(A・B)
→ NAND

¬(A+B)
→ NOR
```

真理値表と論理式の両方から確認できれば、選択肢を安全に切れます。

## まとめ（試験直前用）

- NANDは、ANDの結果を反転する論理演算
- 論理式は `¬(A・B)`
- `11` のときだけ出力が0になる
- NANDの両入力へ同じ値を入れるとNOTになる
- NANDを2段使うとANDを作れる
- ド・モルガンの法則を使うとORも作れる
- **3個のNANDを2段に組むと、二つのANDの論理和** `P・Q + R・S` **を作れる**
- NANDだけで基本ゲートを構成できるため、万能ゲートと呼ばれる
- NORは `00` のときだけ1、XORは入力が異なるときだけ1

```text
11だけ0
→ NAND

NANDだけで
NOT・AND・ORを作れる
→ 万能ゲート
```

{% include fe_article_footer.html %}
