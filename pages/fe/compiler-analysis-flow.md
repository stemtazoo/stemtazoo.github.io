---
layout: page
title: "コンパイラの処理順序｜字句解析・構文解析・意味解析・最適化・コード生成【基本情報技術者試験】"
description: "コンパイラ内部の処理を、字句解析→構文解析→意味解析→最適化→コード生成の順に整理します。FE科目Aで迷いやすい各処理を「何を確認するか」で切り分けます。"
permalink: /fe/compiler-analysis-flow/
tags: [fe, fe-technology, software]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 51
date: 2026-10-06
last_modified_at: 2026-10-06
---

<style>
.compiler-flow{display:flex;align-items:stretch;gap:.4rem;margin:1.2rem 0;flex-wrap:wrap}
.compiler-step{flex:1 1 125px;border:1px solid #d8dee4;border-radius:10px;padding:.75rem;text-align:center;background:#f6f8fa}
.compiler-step strong,.compiler-step span{display:block}
.compiler-step span{margin-top:.35rem;font-size:.9em}
.compiler-arrow{display:flex;align-items:center;font-weight:700}
.analysis-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:.7rem;margin:1rem 0}
.analysis-card{border:1px solid #d8dee4;border-radius:10px;padding:.85rem;background:#f6f8fa}
.analysis-card strong{display:block;margin-bottom:.35rem}
@media(max-width:600px){.compiler-flow{flex-direction:column}.compiler-arrow{justify-content:center;transform:rotate(90deg)}}
</style>

## まず結論

コンパイラの代表的な処理は、次の順で考えると整理しやすくなります。

**字句解析 → 構文解析 → 意味解析 → 最適化 → コード生成**

FE科目Aで「最初に行う処理」を問われたら、まず**字句解析**を考えます。

ただし、順番だけを暗記するより、

> **文字列を単語に分ける → 文法を調べる → 意味を調べる**

という流れを理解しておく方が、選択肢を切りやすくなります。

## 直感的な説明

例えば、次のソースコードを考えます。

```c
total = price + 100;
```

コンパイラはいきなり機械語へ変換するのではなく、段階を踏んで内容を理解していきます。

<div class="compiler-flow" aria-label="コンパイラ内部の代表的な処理順序">
  <div class="compiler-step"><strong>字句解析</strong><span>単語に分ける</span></div>
  <div class="compiler-arrow">→</div>
  <div class="compiler-step"><strong>構文解析</strong><span>文法を調べる</span></div>
  <div class="compiler-arrow">→</div>
  <div class="compiler-step"><strong>意味解析</strong><span>意味を調べる</span></div>
  <div class="compiler-arrow">→</div>
  <div class="compiler-step"><strong>最適化</strong><span>むだを減らす</span></div>
  <div class="compiler-arrow">→</div>
  <div class="compiler-step"><strong>コード生成</strong><span>実行できる形へ</span></div>
</div>

最初の字句解析では、例えば次のような単位に分けます。

```text
total | = | price | + | 100 | ;
```

この意味のある最小単位を**トークン（token）**と呼びます。

## 定義・仕組み

<div class="analysis-cards">
  <div class="analysis-card"><strong>字句解析</strong>文字列をトークンに分ける</div>
  <div class="analysis-card"><strong>構文解析</strong>トークンの並びが文法に合っているか調べる</div>
  <div class="analysis-card"><strong>意味解析</strong>型など、意味上の矛盾がないか調べる</div>
  <div class="analysis-card"><strong>最適化</strong>意味を変えずに実行効率を高める</div>
  <div class="analysis-card"><strong>コード生成</strong>機械語などの目的コードを生成する</div>
</div>

### 字句解析

ソースプログラムを文字の並びとして読み、識別子、演算子、数値などの**トークン**へ分割します。

英語では **lexical analysis** といいます。

### 構文解析

字句解析で得られたトークンを、プログラミング言語の**文法（syntax）**に従って解析します。

構文木などを使って、式や文の構造を表します。

### 意味解析

文法として成立していても、意味上おかしい場合があります。

例えば、変数の宣言や利用の対応、演算に使うデータ型の整合性などを確認します。

### 最適化

プログラムの意味を保ったまま、不要な計算を減らすなどして実行効率を改善します。

例えば、

```text
2 * 5
↓
10
```

のように、あらかじめ計算できるものを変換する処理があります。

### コード生成

解析・最適化した結果から、機械語やアセンブリ言語、中間コードなどの目的コードを生成します。

## 科目Aでどう出る？

試験では、処理名と役割を入れ替えた選択肢に注意します。

| 問題文の表現 | 判断する処理 |
|---|---|
| トークンに分割 | **字句解析** |
| 文法・構文木 | **構文解析** |
| 型・意味の整合性 | **意味解析** |
| 不要な処理を減らす | **最適化** |
| 目的コードを作る | **コード生成** |

特に「最初に行う」という表現があれば、

**文字 → トークン → 文法 → 意味**

の順を思い出します。

## どんな場面で使う？

例えば、

```c
int a = 5 + 3;
```

というコードでも、コンパイラは段階的に処理します。

まず `int`、`a`、`=`、`5`、`+`、`3`、`;` などに分けます。

その後、それらの並びが文法に合っているか、型などに問題がないかを確認し、必要に応じて最適化して目的コードを生成します。

つまり、**後の処理ほど、前の処理で得た情報を利用する**と考えると順番を理解しやすくなります。

## よくある誤解・混同

### 字句解析と構文解析は同じ？

違います。

- 字句解析：**単語に分ける**
- 構文解析：**単語の並びを文法として調べる**

日本語で考えるなら、「単語を切り出す」と「文章の構造を調べる」の違いです。

### 構文解析と意味解析はどう違う？

ここは特に混同しやすいポイントです。

- 構文解析：**文法として正しいか**
- 意味解析：**意味として矛盾していないか**

試験では、**文法 → 構文、型 → 意味**を判断キーワードにすると切り分けやすくなります。

### 最適化はコンパイルを速くする処理？

主眼はそこではありません。

コンパイラ最適化は、生成されるプログラムの意味を保ちながら、主に**実行効率などを改善する**ための処理です。

### コンパイラ・リンカ・ローダとの関係は？

この記事は**コンパイラ内部**の処理を扱っています。

一方、プログラム全体の流れでは、コンパイル後にリンカが目的モジュールなどを結合し、その後ローダが実行時に主記憶へ読み込みます。

詳しくは「[コンパイラ・リンカ・ローダ・デバッガの違い](/fe/compiler-linker-loader-debugger/)」で整理しています。

## 確認問題（基本情報技術者試験対策）

コンパイラがソースプログラムを処理するとき、一般に最も早い段階で行う処理はどれか。

- ア. 意味解析
- イ. 構文解析
- ウ. 最適化
- エ. 字句解析

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：エ（字句解析）**

まずソースプログラムの文字列をトークンへ分割する字句解析を行い、その結果を使って構文解析へ進みます。

順番だけを思い出せないときは、

**文字 → 単語 → 文法 → 意味**

と考えると、字句解析が最初だと判断できます。

</details>

## まとめ（試験直前用）

- **トークンに分ける** → 字句解析
- **文法を確認** → 構文解析
- **型などの意味を確認** → 意味解析
- **意味を保って効率化** → 最適化
- **目的コードを作る** → コード生成
- 順番は **字句 → 構文 → 意味 → 最適化 → コード生成**
- 迷ったら **文字 → 単語 → 文法 → 意味** で考える

{% include fe_article_footer.html %}
