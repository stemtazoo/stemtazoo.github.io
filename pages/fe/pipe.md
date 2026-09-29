---
layout: page
title: パイプとは？標準出力を次のコマンドの標準入力へつなぐ仕組み【基本情報技術者試験】
description: UNIX系シェルのパイプを「前のコマンドの標準出力を次のコマンドの標準入力へ渡す仕組み」として整理し、リダイレクト・バックグラウンド実行・ブレース展開との違いをFE科目A向けに切り分けます。
permalink: /fe/pipe/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 110
date: 2026-09-30
last_modified_at: 2026-09-30
---

## まず結論

パイプ（pipe）とは、**あるコマンドの標準出力を、別のコマンドの標準入力へ直接つなぐ仕組み**です。

UNIX系のシェルでは、代表的に `|` を使って次のように書きます。

```bash
command1 | command2
```

基本情報技術者試験では、

> **「標準出力を、別のコマンドの標準入力へつなぐ」→ パイプ**

を最優先の判断基準にすると選択肢を切りやすくなります。

## 直感的な説明

パイプは、**前の処理の結果を、そのまま次の処理へ流すベルトコンベア**のようなものです。

<style>
.fe-pipe-flow {
  display: flex;
  align-items: stretch;
  justify-content: center;
  gap: 0.75rem;
  margin: 1.25rem 0;
}
.fe-pipe-node {
  flex: 1 1 0;
  min-width: 0;
  padding: 0.9rem 1rem;
  border: 1px solid #cbd5e1;
  border-radius: 0.7rem;
  background: #f8fafc;
  text-align: center;
}
.fe-pipe-node strong {
  display: block;
  margin-bottom: 0.25rem;
}
.fe-pipe-node small {
  color: #475569;
}
.fe-pipe-connector {
  display: flex;
  flex: 0 0 auto;
  align-items: center;
  justify-content: center;
  min-width: 4.2rem;
  padding: 0.5rem;
  border-radius: 999px;
  background: #eef6ff;
  color: #0b6fae;
  font-weight: 700;
  text-align: center;
}
.fe-pipe-note {
  margin: 0.6rem 0 1.2rem;
  padding: 0.8rem 1rem;
  border-left: 4px solid #0b6fae;
  background: #f7fbff;
}
@media (max-width: 640px) {
  .fe-pipe-flow {
    flex-direction: column;
  }
  .fe-pipe-connector {
    align-self: center;
    min-width: 5rem;
  }
}
</style>

<div class="fe-pipe-flow" role="img" aria-label="コマンドAの標準出力がパイプを通ってコマンドBの標準入力につながる流れ">
  <div class="fe-pipe-node">
    <strong>command A</strong>
    <small>標準出力 stdout</small>
  </div>
  <div class="fe-pipe-connector">→ | →</div>
  <div class="fe-pipe-node">
    <strong>command B</strong>
    <small>標準入力 stdin</small>
  </div>
</div>

<div class="fe-pipe-note">
<strong>見るポイント：</strong>ファイルにいったん保存するのではなく、前のコマンドの出力を次のコマンドへ渡しています。
</div>

例えば、文字列を並べ替える処理なら次のように考えられます。

```bash
printf "banana\napple\n" | sort
```

処理の流れは、

```text
printf が文字列を出力
        ↓
       |
        ↓
sort がその文字列を入力として受け取る
        ↓
apple
banana
```

です。

一つのコマンドに全部の処理をさせるのではなく、**小さな処理をつないで使う**のがポイントです。

## 定義・仕組み

コマンドには、代表的に次の入出力があります。

| 名前 | 意味 |
|---|---|
| 標準入力（stdin） | コマンドが通常の入力として受け取るデータ |
| 標準出力（stdout） | コマンドが通常の結果として出力するデータ |
| 標準エラー出力（stderr） | エラーメッセージなどを出すための出力 |

通常のパイプ `|` では、**前のコマンドの標準出力（stdout）を、次のコマンドの標準入力（stdin）へ接続**します。

```text
command1 の stdout
        ↓
      pipe
        ↓
command2 の stdin
```

Bashの公式マニュアルでも、パイプラインでは各コマンドの出力がパイプを介して次のコマンドの入力へ接続されると説明されています。

- [GNU Bash Reference Manual：Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html)

なお、通常の `|` で自動的につながるのは標準出力です。標準エラー出力まで一緒に扱う方法もありますが、FEではまず **stdout → stdin** の基本を押さえれば十分です。

このテーマはOS・シェルの働きと関係します。公式の出題範囲は[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

## 科目Aでどう出る？

科目Aでは、パイプと似たシェル機能を混ぜた選択肢に注意します。

| キーワード | 判断する機能 | 代表例 |
|---|---|---|
| 前のコマンドの出力を次のコマンドへ渡す | **パイプ** | `command1 \| command2` |
| 入出力先をファイルなどへ切り替える | リダイレクト | `command > file` |
| コマンドの終了を待たずに処理を続ける | バックグラウンド実行 | `command &` |
| 規則に従って複数の文字列を作る | ブレース展開 | `file{1,2}.txt` |

特に重要なのは、**パイプとリダイレクトの違い**です。

```text
command A → command B
→ パイプ

command → file
file → command
→ リダイレクト
```

試験では厳密な内部実装よりも、**何と何をつないでいるか**を見ると判断しやすくなります。

## どんな場面で使う？

パイプは、一つのコマンドの結果を別のコマンドで絞り込んだり、並べ替えたり、集計したりするときに使います。

例えば、

```bash
command1 | command2 | command3
```

のように複数の処理を順番につなぐこともできます。

```text
データを作る
   ↓
絞り込む
   ↓
並べ替える
   ↓
結果を表示
```

というように、**小さな処理を組み合わせて一つの流れを作る**イメージです。

シェルそのものの役割を確認したい場合は、[シェルとは？カーネルとの違いとコマンドを解釈する役割]({{ '/fe/shell/' | relative_url }})も合わせて確認すると整理しやすくなります。

## よくある誤解・混同

### パイプとリダイレクト

最も混同しやすい組合せです。

```bash
command1 | command2
```

は、前のコマンドの出力を**次のコマンドへ渡す**パイプです。

一方、

```bash
command > result.txt
```

は、標準出力の行き先を**ファイルへ変更する**リダイレクトです。

リダイレクトには入力元をファイルへ切り替える `<` などもあります。試験では「次のコマンドへ渡す」のか、「入出力先を切り替える」のかに注目します。

### パイプとバックグラウンド実行

バックグラウンド実行は、コマンド同士のデータをつなぐ機能ではありません。

```bash
command &
```

のように、シェルがそのコマンドの終了を待たずに次の処理へ進めるための実行方法です。

```text
データを次へ渡す
→ パイプ

終了を待たずに実行
→ バックグラウンド実行
```

### パイプとブレース展開

Bashなどのブレース展開は、`{}` の指定から文字列を展開する機能です。

```bash
echo file{1,2,3}.txt
```

なら、次のような文字列が作られます。

```text
file1.txt file2.txt file3.txt
```

パイプのようにコマンド間の入出力を接続する機能ではありません。

## まとめ（試験直前用）

試験直前は、次の3点で切り分けます。

1. **標準出力 → 次のコマンドの標準入力**ならパイプ
2. **ファイルなどへ入出力先を変える**ならリダイレクト
3. `|` は「処理結果を次へ流す」と覚える

```text
command A
   ↓ stdout
   |
   ↓ stdin
command B

→ パイプ
```

> **「コマンド → コマンド」なら、まずパイプを疑う。**

{% include fe_article_footer.html %}
