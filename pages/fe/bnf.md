---
layout: page
title: BNFとは？構文規則の読み方と再帰的な定義【基本情報技術者試験】
description: BNFの::=と|の意味、再帰的な構文規則の読み方を、変数名を1文字ずつ組み立てる図解とPythonの判定例で説明します。先頭文字の制約から選択肢を切る方法も整理します。
permalink: /fe/bnf/
tags: [fe, fe-technology, programming, pseudocode]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 75
date: 2026-10-11
last_modified_at: 2026-10-11
related_articles:
  - /fe/recursion/
  - /fe/compiler-optimization/
---

## まず結論

**BNF（バッカス・ナウア記法）**は、プログラム言語などの**文法上、どんな並びが許されるか**を表す記法です。

科目Aでは、記号を読んで文字列が規則に合うかを判定します。特に**先頭に使える文字**と**後ろに追加できる文字**を分けて見ると、選択肢を切りやすくなります。

## 直感的な説明

例えば、架空の言語で使う変数名を「最初はA〜Fの英字、その後はA〜F・数字・アンダースコアを追加できる」と決めたとします。

次の図は、規則に合う名前を少しずつ作るイメージです。

<div style="max-width:560px;margin:1rem auto;padding:1rem;border:1px solid #cbd5e1;border-radius:12px;background:#f8fafc;color:#243247;">
  <p style="margin:0 0 .8rem;font-weight:700;">変数名を1文字ずつ作る</p>
  <div style="display:flex;align-items:center;justify-content:center;gap:.5rem;flex-wrap:wrap;text-align:center;">
    <span style="padding:.5rem .8rem;background:#dbeafe;border-radius:8px;font-weight:700;">F</span>
    <span aria-hidden="true">→</span>
    <span style="padding:.5rem .8rem;background:#e2e8f0;border-radius:8px;font-weight:700;">F5</span>
    <span aria-hidden="true">→</span>
    <span style="padding:.5rem .8rem;background:#e2e8f0;border-radius:8px;font-weight:700;">F5_</span>
    <span aria-hidden="true">→</span>
    <span style="padding:.5rem .8rem;background:#dcfce7;border-radius:8px;font-weight:700;">F5_1</span>
  </div>
  <p style="font-size:.9rem;margin:.8rem 0 0;">最初のFは英字。後ろの5・_・1は、いずれも追加可能な文字です。</p>
</div>

反対に、`_B39` や `3E5` は、**最初の文字**が規則に合わないため不適切です。

## 定義・仕組み

BNFでは、次の記号を使います。

| 記号 | 意味 | 読み方 |
|---|---|---|
| `::=` | 定義する | 左辺は右辺の形で表せる |
| `&#124;` | 選択肢（または） | いずれかを選べる |
| `<英字>` など | 非終端記号 | さらに別の規則へ展開できる名前 |

例えば、次の規則を考えます。

~~~text
<数字>   ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<英字>   ::= A | B | C | D | E | F
<英数字> ::= <英字> | <数字> | _
<変数名> ::= <英字> | <変数名><英数字>
~~~

`<変数名>` の定義には、`<変数名>` 自身が登場します。これは**再帰的な定義**です。

- `<変数名> ::= <英字>`：英字1文字で名前を作れる
- `<変数名> ::= <変数名><英数字>`：すでにできた名前の後ろに、英数字を1文字付け足せる

この2つを合わせると、**英字1文字で始まり、後ろに0文字以上の英数字を続けられる**という意味になります。ここでの「英数字」には、定義に従って `_` も含まれます。

### Pythonで同じ規則を判定する

次は、**この例で決めたBNFの規則**をPythonで確かめるコードです。Python言語そのものの変数名の規則とは異なります。

```python
def valid_name(name):
    first = "ABCDEF"
    following = "ABCDEF0123456789_"

    if not name:
        return False

    return name[0] in first and all(
        char in following for char in name[1:]
    )

for name in ["_B39", "246", "3E5", "F5_1"]:
    print(name, valid_name(name))
```

~~~text
_B39 False
246 False
3E5 False
F5_1 True
~~~

**見るポイント：** 先頭の1文字だけ判定条件が異なります。

## 科目Aでどう出る？

構文規則と候補文字列が与えられたら、次の順番で調べます。

1. **開始部分を確認する**：`<変数名>` は何から始まれるか。
2. **追加可能な部分を確認する**：後ろには何を続けられるか。
3. **先頭から順に照合する**：途中で規則に合わなければ、その候補を除外する。

この例では、先頭がA〜Fでない候補はすぐ除外できます。

| 候補 | 判定 | 理由 |
|---|---|---|
| `_B39` | × | 先頭がアンダースコア |
| `246` | × | 先頭が数字 |
| `3E5` | × | 先頭が数字 |
| `F5_1` | ○ | 先頭がF、残りも許可文字 |

**「途中で使える文字」と「先頭に使える文字」は同じとは限らない**、という点が判断の中心です。

## どんな場面で使う？

BNFは、プログラミング言語の構文や、入力文字列の形式を定義するときに使われます。

例えば、言語の仕様書では「式」「命令」「識別子」などが、どのような要素の組合せでできているかを表せます。

なお、**BNFで表すのは文法上の形**です。書かれたプログラムの計算結果が正しいか、変数の型が適切か、といった意味的な正しさをBNFだけで保証するわけではありません。

## よくある誤解・混同

### `|` は文字列にそのまま入る？

いいえ。ここでは「または」を表す記号です。`A | B` は、AまたはBを選べるという意味です。

### `<変数名><英数字>` は、必ず2文字だけ？

いいえ。`<変数名>` 自体を再び展開できるため、3文字、4文字と長くできます。

### アンダースコアが使えるなら、先頭にも置ける？

いいえ。今回の規則ではアンダースコアは**追加する文字**には使えますが、**最初の英字**の代わりにはなりません。

### BNFの再帰と、再帰関数は同じ？

どちらも自分自身を参照する形ですが、役割は異なります。BNFの再帰は**文法を定義する方法**、再帰関数は**関数が自分自身を呼び出して処理する方法**です。後者は[再帰処理の解説](/fe/recursion/)で確認できます。

## まとめ（試験直前用）

- BNFは**許される文字列の構造**を定義する記法
- `::=` は定義、`|` は「または」
- 右辺に自分自身が出てきたら、**再帰的に繰り返せる形**を確認する
- 選択肢は**先頭文字の制約**から調べると速い
- BNFの文法チェックと、プログラムの意味的な正しさは別

{% include fe_article_footer.html %}
