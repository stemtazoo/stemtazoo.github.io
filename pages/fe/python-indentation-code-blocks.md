---
layout: page
title: Pythonのインデントとコードブロック｜JavaScript・Rubyとの違い【基本情報技術者試験】
description: Pythonではインデントの深さがコードブロックを表す構文上の意味をもちます。JavaScript・Perl・Rubyとの違いを比較し、FE試験で言語を見分ける判断基準を初心者向けに整理します。
permalink: /fe/python-indentation-code-blocks/
tags: [fe, fe-technology, programming, python, software]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 21
date: 2026-09-19
last_modified_at: 2026-09-19
---

## まず結論

**Pythonは、インデント（字下げ）の深さでコードブロックの範囲を表すプログラミング言語**です。

基本情報技術者試験では、次の切り分けができれば判断しやすくなります。

```text
{ } でブロックを表す
→ JavaScript・Perlなど

インデントでブロックを表す
→ Python

end でブロックを閉じる
→ Ruby
```

試験中に「**インデントの深さでクラス・関数・条件文などの範囲を示す**」とあれば、まずPythonを考えます。

---

## 直感的な説明

Pythonでは、見た目の字下げがそのままプログラムの構造を表します。

```python
score = 80

if score >= 60:
    print("合格")
    print("おめでとう")

print("判定終了")
```

この場合、2つの `print` は同じ深さなので、どちらも `if` の処理です。

```text
if score >= 60:
    ├─ print("合格")
    └─ print("おめでとう")

print("判定終了")
↑ if の外
```

Pythonでは、インデントを変えると**処理の所属先そのものが変わる**のがポイントです。

---

## 定義・仕組み

### Pythonではインデントが構文の一部

Python公式ドキュメントでは、行頭の空白からインデントレベルを決定し、その変化を `INDENT`・`DEDENT` として扱う仕様が定められています。

つまり、インデントは単にコードを読みやすくするための飾りではなく、**文をどのブロックに所属させるかを決める構文上の意味**をもちます。

- [Python公式ドキュメント：Lexical analysis - Indentation](https://docs.python.org/3/reference/lexical_analysis.html#indentation)
- [Python公式ドキュメント：Compound statements](https://docs.python.org/3/reference/compound_stmts.html)

### 条件分岐

```python
if 条件:
    処理1
    処理2
else:
    処理3
```

`処理1` と `処理2` は同じ深さなので、同じ `if` ブロックに属します。

### 関数

```python
def hello():
    print("Hello")
    print("Python")
```

関数本体もインデントで表します。

### クラス

```python
class Car:
    def run(self):
        print("run")
```

クラスの中、さらにその中のメソッドというように、インデントが深くなるほど階層も深くなります。

---

## 科目Aでどう出る？

科目Aでは、言語ごとの記述方法を比較して該当する言語を選ばせる問題に注意します。

### Pythonを疑うキーワード

```text
インデント
字下げ
コードブロック
深さで範囲を表す
↓
Python
```

特に、

> **インデントの深さによって、クラスや関数、条件文などのコードブロックの範囲を指定する**

という説明ならPythonを考えます。

### JavaScript・Perlとの違い

JavaScriptやPerlでは、一般に `{` と `}` でコードブロックを囲みます。

```javascript
if (condition) {
    doSomething();
}
```

字下げをすると読みやすくなりますが、Pythonとは違い、**ブロックを決める中心は波括弧**です。

### Rubyとの違い

Rubyでは、`if` や `def` などで始まったブロックを `end` で閉じます。

```ruby
if condition
  puts "OK"
end
```

| 問題文の特徴 | 考える言語 |
|---|---|
| インデントの深さでブロックを指定 | Python |
| `{ }` でブロックを囲む | JavaScript・Perlなど |
| `end` でブロックを閉じる | Ruby |

---

## どんな場面で使う？

Pythonのインデントは、条件分岐、繰返し、関数、クラスなど、処理のまとまりを表す場面で使います。

```python
for i in range(3):
    if i == 1:
        print("1です")
    print(i)

print("終了")
```

この例は、次の構造です。

```text
for
├─ if
│  └─ print("1です")
└─ print(i)

print("終了")
↑ for の外
```

Pythonを読むときは、**文字だけでなく左端の位置も見る**のが重要です。

---

## よくある誤解・混同

### インデントは読みやすくするためだけ？

違います。

Pythonではインデントが**文法上の意味**をもちます。

```text
JavaScriptなど
→ インデントは主に可読性のため
→ ブロックは { } で表す

Python
→ インデントそのものがブロックを表す
```

### Pythonは必ず4スペースでなければ動かない？

「4スペース」は、Pythonのスタイルガイドである **PEP 8の推奨**です。

- [PEP 8：Indentation](https://peps.python.org/pep-0008/#indentation)

一方、

> **インデントで文をグループ化する**

ことはPythonの**言語仕様**です。

```text
インデントでブロックを決める
→ Pythonの言語仕様

1段を4スペースにする
→ PEP 8の推奨スタイル
```

### タブとスペースを混ぜてもよい？

避けるべきです。

Pythonでは、インデントの解釈が一貫しないようなタブとスペースの混在は `TabError` になる場合があります。

初心者のうちは、**スペース4個で統一**すると分かりやすいです。

### Pythonならどんな場所でもインデントが必要？

すべての行を字下げするわけではありません。

`if`、`for`、`while`、`def`、`class` など、**ブロックを作る構文の本体**をインデントします。

---

## まとめ（試験直前用）

- Pythonは**インデントの深さでコードブロックを表す**
- インデントは見た目だけではなく**構文の一部**
- `{ }` でブロックを表すならJavaScript・Perlなどを疑う
- `end` で閉じるならRubyを疑う
- 「4スペース」はPEP 8の推奨であり、「インデントでブロックを表す」という言語仕様とは別

```text
インデント
→ Python

{ }
→ JavaScript・Perlなど

end
→ Ruby
```

> **「インデントの深さで範囲を決める」と出たら、まずPython。**

{% include fe_article_footer.html %}
