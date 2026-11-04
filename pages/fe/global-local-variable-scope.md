---
layout: page
title: 大域変数と局所変数とは？同じ名前の宣言・代入を読み分ける【基本情報技術者試験】
description: 科目Bの疑似言語で、同名の大域変数と局所変数を混同しない読み方を整理。宣言と代入、手続ごとの値、問題固有のスコープ前提をオリジナル例と段階操作で確かめます。
permalink: /fe/global-local-variable-scope/
tags: [fe, fe-technology, pseudocode, trace, programming]
fe_section: 科目B対策
fe_subsection: 疑似言語
fe_order: 15
date: 2026-11-04
last_modified_at: 2026-11-04
related_articles:
  - /fe/pseudocode-reading-guide/
  - /fe/call-by-value/
---

## まず結論

**大域変数（global variable）は手続の外側に置かれ、局所変数（local variable）は手続の中で宣言される変数**です。同じ名前でも別の変数として扱う場合があり、科目Bでは**変数名だけでなく「どこで宣言されたか」**を確認します。

IPAの疑似言語には「`型名: 変数名`＝宣言」「`変数名 ← 式`＝代入」という書き分けがあります。ただし、**同名の局所変数を手続の途中で宣言した場合の参照先切替え**は、この記述形式だけから一般規則として断定できません。問題文の説明や前提を優先して読みます。

## 直感的な説明

「作業場の共通掲示板」と「作業者が持つ個人メモ」に同じ「在庫」という名前を書いても、記録している場所が異なれば別の値です。

- **大域変数**：共通掲示板。手続をまたいで値が残る。
- **局所変数**：手続ごとの個人メモ。別の手続の同名変数とは区別する。
- **宣言**：新しいメモ（変数）を用意する。
- **代入**：既に選ばれたメモの値を書き換える。

変数の名前が一致するだけで「同じ箱」と判断しないことがポイントです。

## 定義・仕組み

### 宣言と代入は別の操作

| 記述 | 意味 | トレース時に確認すること |
|---|---|---|
| `整数型: stock ← 4` | 整数型の変数stockを宣言し、4を設定 | **どの範囲に**新しいstockを作ったか |
| `stock ← 9` | 既存のstockへ9を代入 | **どのstock**に代入したか |
| `stock を出力する` | 現在参照しているstockの値を出力 | どの範囲のstockを読んだか |

IPA「試験で使用する情報技術に関する用語・プログラム言語など」Ver.5.1の別紙2に、変数宣言と代入の記述形式が示されています。出典：[IPA：試験で使用する情報技術に関する用語・プログラム言語など（PDF）](https://www.ipa.go.jp/shiken/syllabus/doe3um0000002djj-att/shiken_yougo_ver5_1.pdf)。

### 同名の変数が存在するとき

次は**当サイト独自の説明用疑似コード**です。元となる試験問題や市販教材のプログラムは使用していません。

この例では明示的に、**手続内で局所変数を宣言するまでは大域変数を参照し、宣言した行からは同名の局所変数を参照する**、というルールを仮定します。この切替規則そのものをIPAの共通仕様と主張する例ではありません。

```text
大域: 整数型: stock ← 4

○inspect()
  stock ← 9
  stock を出力する
  整数型: stock ← 2
  stock を出力する

○report()
  stock を出力する
```

`inspect()`、続けて`report()`を呼び出すと仮定します。

| 順番 | 実行する行 | 大域stock | inspectの局所stock | 出力 |
|---|---|---:|---:|---:|
| 初期 | 大域変数を宣言 | 4 | まだない | — |
| 1 | `stock ← 9` | 9 | まだない | — |
| 2 | `stock を出力する` | 9 | まだない | **9** |
| 3 | `整数型: stock ← 2` | 9 | 2 | — |
| 4 | `stock を出力する` | 9 | 2 | **2** |
| 5 | `report()`で出力 | 9 | 終了 | **9** |

出力は **9 → 2 → 9** です。最後が2ではない理由は、局所変数の宣言では**大域stockは9のまま**だからです。

### 触って覚える：どのstockが変わる？

**予想：** `整数型: stock ← 2` を実行すると、大域stockは2になるでしょうか？　実行前の大域・局所の状態を見て、次へ進めてみましょう。

<div class="fe-learning-demo" data-fe-scope-demo>
  <p class="fe-learning-demo__title">変数の宣言・代入を1行ずつ追跡</p>
  <p class="fe-learning-demo__hint">この教材は直前の「宣言行から局所へ切り替わる」という明示的な仮定を用います。<strong>プログラムの一般仕様ではありません。</strong></p>
  <p><strong>現在の処理：</strong><output data-scope-line>大域stockを4で宣言</output></p>
  <div class="fe-learning-demo__controls">
    <button type="button" class="fe-learning-demo__button" data-scope-back disabled>1つ戻る</button>
    <button type="button" class="fe-learning-demo__button" data-scope-next>次の行へ</button>
    <button type="button" class="fe-learning-demo__button" data-scope-reset>最初から</button>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(125px,1fr));gap:0.6rem;margin:0.8rem 0;">
    <div style="padding:0.65rem;border:1px solid #888;border-radius:0.4rem;"><strong>大域stock</strong><p><output data-scope-global>4</output></p></div>
    <div style="padding:0.65rem;border:1px solid #888;border-radius:0.4rem;"><strong>inspectの局所stock</strong><p><output data-scope-local>未宣言</output></p></div>
  </div>
  <p><strong>出力の履歴：</strong><output data-scope-output>まだ出力なし</output></p>
  <p role="status" aria-live="polite" aria-atomic="true" data-scope-explain>最初は共通のstockだけが存在します。</p>
  <noscript><p>操作にはJavaScriptが必要です。JavaScriptが使えない場合も、直前のトレース表で初期状態から終了まで確認できます。</p></noscript>
</div>
<script src="{{ '/assets/js/fe-variable-scope.js' | relative_url }}" defer></script>

## 科目Aでどう出る？

選択肢で「局所変数は、ほかの手続で宣言された同名の変数と常に同一である」とあれば誤りです。大域変数と局所変数は**有効範囲（scope）**が異なります。再利用できる名前の範囲と、値が共有される範囲を分けましょう。

## 科目Bでどう使う？

同じ名前の変数が複数登場したら、トレース表を**「大域stock」「inspectのstock」「reportのstock」**のように分けます。表を一列の`stock`だけにすると、どの値が書き換わったのか分からなくなります。

1. 問題文のスコープや引数の指定を読む。
2. `型名:` がある行を**宣言**として印を付ける。
3. 代入と出力のたびに、**どの範囲の変数か**確認する。
4. 呼出し先から戻った後も残る値を区別する。

今回の独自例は途中宣言を分かりやすく示すためのものです。**実際の科目Bでは問題文の指定と、与えられたプログラムの整合性を確認**してください。

## よくある誤解・混同

| 誤解 | 正しくは |
|---|---|
| 名前が同じなら必ず同じ変数 | 宣言位置と有効範囲を区別する |
| `stock ← 9` は新しい変数の宣言 | `←` だけなら代入。宣言の`整数型:`と区別する |
| 局所変数を2にすると大域も2になる | 別々の変数なら大域は変わらない |
| 今回の途中宣言の切替えはIPAが明記した共通規則 | IPA別紙2に明記されているのは宣言・代入の書き方。切替えの詳細は問題の前提を確認する |
| Pythonでも途中で代入した行から局所になる | Pythonでは関数内の代入がある名前は、原則として関数全体で局所扱いされるため同一視できない |

## まとめ（試験直前用）

- **変数名だけでなく宣言位置と有効範囲を確認**する。
- `型名:` の宣言と、`←` の代入を区別する。
- トレース表には大域と手続ごとの局所変数を**別列**に書く。
- 途中宣言の参照先切替えは**問題固有の前提**で扱い、IPA共通規則と決めつけない。

疑似言語の記号全般は[IPA擬似言語の読み方](/fe/pseudocode-reading-guide/)、引数のコピーと元の変数の違いは[値呼出し](/fe/call-by-value/)で確認できます。

{% include fe_article_footer.html %}
