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
last_modified_at: 2026-10-27
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

### 式を組み立てる規則では、括弧も規則どおり

変数名だけでなく、複数の式を組み合わせるBNFもあります。次は説明用に作った独立した例です。

~~~text
<式> ::= <変数> | (<式>-<式>) | <式>/<式>
<変数> ::= P | Q | R | S
~~~

この規則では、引き算は `(<式>-<式>)` の形で**全体を括弧で囲み**、割り算は `<式>/<式>` の形で組み合わせます。

例えば、`(P-Q)/(R-S)` は次の順番で生成できます。

<div style="max-width:560px;margin:1rem auto;padding:1rem;border:1px solid #cbd5e1;border-radius:12px;background:#f8fafc;color:#243247;">
  <p style="margin:0 0 .7rem;font-weight:700;">式を1段ずつ生成する</p>
  <div style="padding:.55rem .75rem;border-radius:8px;background:#e2e8f0;text-align:center;">
    <code style="color:#243247;">&lt;式&gt;</code>
  </div>
  <p style="margin:.3rem 0;text-align:center;font-size:.85rem;">↓ 割り算の規則を選ぶ</p>
  <div style="padding:.55rem .75rem;border-radius:8px;background:#e2e8f0;text-align:center;">
    <code style="color:#243247;">&lt;式&gt;/&lt;式&gt;</code>
  </div>
  <p style="margin:.3rem 0;text-align:center;font-size:.85rem;">↓ 左右とも引き算の規則を選ぶ</p>
  <div style="padding:.55rem .75rem;border-radius:8px;background:#dbeafe;text-align:center;overflow-x:auto;">
    <code style="color:#243247;white-space:nowrap;">(&lt;式&gt;-&lt;式&gt;)/(&lt;式&gt;-&lt;式&gt;)</code>
  </div>
  <p style="margin:.3rem 0;text-align:center;font-size:.85rem;">↓ 変数をP・Q・R・Sに展開</p>
  <div style="padding:.55rem .75rem;border-radius:8px;background:#dcfce7;text-align:center;">
    <code style="color:#243247;">(P-Q)/(R-S)</code>
  </div>
</div>

**見るポイント：** 規則を選ぶたびに、`<式>` がどの形へ展開されたかを確認します。括弧は引き算の規則に含まれているので、この位置に現れます。

| 候補 | 生成できる？ | 判断 |
|---|---|---|
| `(P-Q)/(R-S)` | ○ | 括弧付きの引き算を2つ作り、割り算で結ぶ |
| `P/Q` | ○ | 割り算の規則をそのまま使う |
| `P-(Q-R)` | × | 引き算全体を囲む括弧がない |
| `(P/Q)` | × | 割り算全体だけを括弧で囲む規則がない |

数式として計算できる形でも、**BNFにない括弧を自由に追加したり、省略したりはできません**。

### 実際に触ってみる：再帰規則を展開する

次は、平成20年春期の科目A相当の過去問で扱われた、別のBNF規則です。

```text
<S> ::= 01 | 0<S>1
```

`01` を選ぶと展開終了、`0<S>1` を選ぶと左右に0と1を一つずつ増やせます。**スライダーを動かして**、途中の `<S>` がどう変わるか確認しましょう。

<div class="fe-learning-demo" data-fe-bnf-expand style="max-width:620px;margin:1rem auto;padding:1rem;border:1px solid #cbd5e1;border-radius:12px;">
  <p class="fe-learning-demo__title" style="font-weight:700;">展開回数を変えて確認</p>
  <label for="fe-bnf-expand-count">再帰規則の使用回数：<strong data-bnf-count>2</strong>回</label>
  <input id="fe-bnf-expand-count" data-bnf-range type="range" min="0" max="5" step="1" value="2" style="display:block;width:100%;margin:1rem 0;" aria-label="再帰規則の使用回数">
  <div style="padding:1rem;border-radius:10px;background:#e2e8f0;color:#1e293b;text-align:center;">
    <p style="margin:0;">生成される文字列</p>
    <strong data-bnf-result style="font-size:1.7rem;letter-spacing:.08em;overflow-wrap:anywhere;">000111</strong>
    <p data-bnf-summary style="margin:.3rem 0 0;">0が3個 ＋ 1が3個</p>
  </div>
  <p style="font-weight:700;margin-top:1rem;">展開の流れ</p>
  <div data-bnf-steps aria-live="polite"><p><code>&lt;S&gt; → 0&lt;S&gt;1 → 00&lt;S&gt;11 → 000111</code></p></div>
  <p style="font-size:.9rem;">青い <code>&lt;S&gt;</code> が、まだ置き換えられる部分です。最後に <code>01</code> を選んで終了します。</p>
  <noscript><p>操作にはJavaScriptが必要です。上の展開例でも規則を確認できます。</p></noscript>
</div>

<script>
(function () {
  var root = document.querySelector('[data-fe-bnf-expand]');
  if (!root) return;
  var range = root.querySelector('[data-bnf-range]');
  function render() {
    var n = Number(range.value);
    var steps = ['&lt;S&gt;'];
    for (var i = 1; i <= n; i++) {
      steps.push('0'.repeat(i) + '&lt;S&gt;' + '1'.repeat(i));
    }
    var result = '0'.repeat(n + 1) + '1'.repeat(n + 1);
    root.querySelector('[data-bnf-count]').textContent = n;
    root.querySelector('[data-bnf-result]').textContent = result;
    root.querySelector('[data-bnf-summary]').textContent = '0が' + (n + 1) + '個 ＋ 1が' + (n + 1) + '個';
    var html = steps.map(function (s, i) {
      return '<p style="margin:.4rem 0"><small>' + (i === 0 ? '開始' : i + '回目') +
        '</small>　<code style="overflow-wrap:anywhere">' +
        s.replace(/&lt;S&gt;/g, '<span style="color:#2563eb;font-weight:700">&lt;S&gt;</span>') +
        '</code></p>';
    }).join('');
    root.querySelector('[data-bnf-steps]').innerHTML = html +
      '<p style="margin:.4rem 0"><small>終了（01に置換）</small>　<strong>' + result + '</strong></p>';
  }
  range.addEventListener('input', render);
  render();
})();
</script>

**選択肢を切る基準：** この規則では、0と1が同数であるだけでは不十分です。**0が先に連続し、その後に同じ個数の1が連続する**必要があります。例えば `0101` は0と1が2個ずつですが、生成できません。

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

### 式に括弧を自由に付けてもよい？

いいえ。**そのBNFが許す位置にしか括弧を付けられません**。上の式の例では、`P/Q` は生成できますが、`(P/Q)` は生成できません。一方、引き算は `(P-Q)` の形が必要です。

### BNFの再帰と、再帰関数は同じ？

どちらも自分自身を参照する形ですが、役割は異なります。BNFの再帰は**文法を定義する方法**、再帰関数は**関数が自分自身を呼び出して処理する方法**です。後者は[再帰処理の解説](/fe/recursion/)で確認できます。

## まとめ（試験直前用）

- BNFは**許される文字列の構造**を定義する記法
- `::=` は定義、`|` は「または」
- 右辺に自分自身が出てきたら、**再帰的に繰り返せる形**を確認する
- 選択肢は**先頭文字の制約**から調べると速い
- 式の規則では**括弧の有無や位置も照合する**。普段の数式の書き方で補わない
- BNFの文法チェックと、プログラムの意味的な正しさは別

{% include fe_article_footer.html %}
