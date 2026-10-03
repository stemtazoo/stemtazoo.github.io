---
layout: page
title: シェルのリダイレクトとは？標準入力・標準出力と「<」「>」「>>」の違い【基本情報技術者試験】
description: シェルのリダイレクトを、標準入力・標準出力の向きから整理します。「<」「>」「>>」の違いと、上書き・追記の判断基準をFE試験向けに解説します。
permalink: /fe/shell-redirection/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
date: 2026-10-03
last_modified_at: 2026-10-03
---

## まず結論

**リダイレクト**とは、シェルでプログラムの**標準入力や標準出力の接続先を切り替える機能**です。

基本情報技術者試験では、まず次の3つを切り分けます。

| 記号 | 何をする？ | 覚え方 |
|---|---|---|
| `<` | ファイルを標準入力にする | ファイル → プログラム |
| `>` | 標準出力をファイルにする | プログラム → ファイル（上書き） |
| `>>` | 標準出力をファイルに追加する | プログラム → ファイル（追記） |

**「入力か出力か」→「出力なら上書きか追記か」**の順で見ると、選択肢を切りやすくなります。

<div class="redirect-flow" aria-label="リダイレクトの基本">
  <div class="redirect-box">入力元<br><strong>キーボード / ファイル</strong></div>
  <div class="redirect-arrow">→</div>
  <div class="redirect-box redirect-program">プログラム</div>
  <div class="redirect-arrow">→</div>
  <div class="redirect-box">出力先<br><strong>画面 / ファイル</strong></div>
</div>

## 直感的な説明

普段、コマンドはキーボードから入力を受け取り、結果を画面へ出すと考えられます。

```text
キーボード → プログラム → 画面
              入力       出力
```

リダイレクトを使うと、この入口や出口をファイルへ付け替えられます。

```text
入力を変更： ファイル → プログラム
出力を変更： プログラム → ファイル
```

つまり、**「データの流れる向きを変える」**と考えると分かりやすいです。

## 定義・仕組み

### 標準入力と標準出力

シェルから起動したプログラムには、一般に標準入力・標準出力などの入出力があります。

- **標準入力（stdin）**：プログラムがデータを受け取る入口
- **標準出力（stdout）**：通常の結果を出す出口

リダイレクトは、その接続先を変更します。

### 「<」は入力

```sh
command < input.txt
```

`input.txt` の内容を、コマンドの標準入力として使います。

```text
input.txt → command
```

### 「>」は出力

```sh
command > result.txt
```

コマンドの標準出力を `result.txt` に送ります。

```text
command → result.txt
```

既存ファイルがある場合、通常は内容を**上書き**します。

### 「>>」は追記

```sh
command >> result.txt
```

こちらも出力先はファイルですが、既存内容を残して末尾へ**追記**します。

```text
既存の内容
────────
今回の出力 ← 追加
```

## 科目Aでどう出る？

科目Aでは、「シェルのリダイレクトで何ができるか」を文章で問われることがあります。

次の3つは、すべて可能です。

```text
標準入力をファイルに切り替える  → <
標準出力をファイルに切り替える  → >
標準出力をファイルに追加する    → >>
```

したがって、選択肢に

> 「標準出力をファイルに追加することはできない」

とあれば、`>>` があるので切れます。

同様に、

> 「標準入力をファイルに切り替えることはできない」

も、`<` があるので誤りです。

<div class="redirect-demo">
  <p><strong>向きを確認</strong></p>
  <div class="redirect-buttons">
    <button type="button" data-redir="in">&lt; 入力</button>
    <button type="button" data-redir="out">&gt; 出力</button>
    <button type="button" data-redir="append">&gt;&gt; 追記</button>
  </div>
  <div id="redirect-demo-result" class="redirect-result">ファイル → プログラム<br><small>&lt; は入力元をファイルへ切り替える</small></div>
</div>

## どんな場面で使う？

例えば、コマンドの結果を後で確認したい場合は、画面ではなくファイルへ出力できます。

```sh
command > result.txt
```

すでにあるログを残しながら結果を追加したい場合は、`>>` を使います。

```sh
command >> result.txt
```

FE試験では、実際のコマンドを細かく暗記するより、**標準入力・標準出力のどちらを、どこへつなぎ替えているか**を見ることを優先します。

## よくある誤解・混同

| 誤解 | 正しい見方 |
|---|---|
| `<` と `>` は似ているので同じ | `<` は入力、`>` は出力 |
| `>` は既存ファイルに追記する | `>` は基本的に上書き |
| `>>` は入力を表す | `>>` は標準出力の追記 |
| リダイレクトは出力だけを変更できる | 標準入力もファイルへ切り替えられる |
| `>` と `>>` は同じ | 出力先は同じでも、上書きと追記が違う |

試験中は記号の形だけで迷わず、次の順で考えます。

```text
1. 入力？ 出力？
2. 出力なら、上書き？ 追記？
```

## 公式技術資料で確認する

シェルのリダイレクトは、POSIXのShell Command Languageで定義されています。

- [The Open Group：Shell Command Language - Redirection](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html#tag_19_07)

FE試験ではPOSIXの細かな仕様まで覚える必要はありません。**`<`＝入力、`>`＝出力、`>>`＝追記**を優先して整理します。

<style>
.redirect-flow{display:flex;align-items:center;justify-content:center;gap:.7rem;margin:1.5rem 0}
.redirect-box{border:1px solid #bbb;border-radius:8px;padding:.8rem;text-align:center;min-width:140px}
.redirect-program{font-weight:700}
.redirect-arrow{font-size:1.5rem}
.redirect-demo{border:1px solid #ddd;border-radius:10px;padding:1rem;margin:1.5rem 0}
.redirect-buttons{display:flex;gap:.5rem;flex-wrap:wrap}
.redirect-buttons button{border:1px solid #aaa;border-radius:7px;background:#fff;padding:.55rem .8rem;cursor:pointer}
.redirect-result{margin-top:1rem;padding:1rem;border-radius:8px;background:#f5f5f5;text-align:center;font-size:1.1rem}
@media(max-width:560px){.redirect-flow{flex-direction:column}.redirect-arrow{transform:rotate(90deg)}}
</style>

<script>
document.addEventListener('DOMContentLoaded', function () {
  const result = document.getElementById('redirect-demo-result');
  document.querySelectorAll('[data-redir]').forEach(function (button) {
    button.addEventListener('click', function () {
      const type = button.dataset.redir;
      if (type === 'in') result.innerHTML = 'ファイル → プログラム<br><small>&lt; は入力元をファイルへ切り替える</small>';
      if (type === 'out') result.innerHTML = 'プログラム → ファイル<br><small>&gt; は標準出力をファイルへ切り替える（上書き）</small>';
      if (type === 'append') result.innerHTML = 'プログラム → ファイル ＋ 追記<br><small>&gt;&gt; は既存内容の末尾へ追加する</small>';
    });
  });
});
</script>

## まとめ（試験直前用）

- **`<`：標準入力をファイルから受け取る**
- **`>`：標準出力をファイルへ出す（上書き）**
- **`>>`：標準出力をファイルへ追加する（追記）**
- 迷ったら「入力か出力か」→「上書きか追記か」で切り分ける

{% include fe_article_footer.html %}
