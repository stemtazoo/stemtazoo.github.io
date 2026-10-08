---
layout: page
title: IPA擬似言語の読み方とは？科目Bで迷わない記号とトレースの基本【基本情報技術者試験】
description: IPA公式の擬似言語Ver.5.1別紙2をもとに、代入・比較・ループ・配列・演算子の読み方と、科目Bで変数を追跡するトレース表の作り方を整理します。
permalink: /fe/pseudocode-reading-guide/
tags: [fe, fe-technology, pseudocode, trace, programming]
fe_section: 科目B対策
fe_subsection: 疑似言語
fe_order: 10
date: 2026-10-09
last_modified_at: 2026-10-09
related_articles:
  - /fe/array/
  - /fe/control-structures-loop-selection/
  - /fe/condition-branch-order/
---

## まず結論

**IPAの擬似言語は、Pythonなどの特定言語を覚えるためのものではなく、処理の流れを共通の書き方で表すためのもの**です。基本情報技術者試験（FE）の科目Bでは、記号を見分けたら、**初期値→条件判定→代入→次の判定**の順に値を追うことが大切です。

根拠は[IPA「試験で使用する情報技術に関する用語・プログラム言語など」Ver.5.1の別紙2（PDFの6〜7ページ）](https://www.ipa.go.jp/shiken/syllabus/doe3um0000002djj-att/shiken_yougo_ver5_1.pdf)です。**個別の問題文に注記がある場合は、その指定を優先**します。

## 直感的な説明

擬似言語を読む作業は、機械の動作手順を順番に確認することに似ています。

- **変数**：現在の値を記録する箱
- **代入**：箱の中身を書き換える
- **条件**：次にどの処理へ進むかの判断
- **繰返し**：条件に応じて同じ工程へ戻る

式を一度に暗算するのではなく、「**今、どの行にいて、どの箱が変わったか**」を確かめます。

## 定義・仕組み

### IPAの基本記号

| 記述 | 読み方 | 注意点 |
|---|---|---|
| `整数型: count` | 変数countを宣言 | 型と名前を区別する |
| `count ← 3` | countに3を代入 | 以前の値は上書きされる |
| `count = 3` | countと3が等しいか比較 | `←`と混同しない |
| `count ≠ 3` | 3と等しくないか比較 | `not`とは別の記法 |
| `a mod b` | aをbで割った余り | 周期・偶奇判定にも使う |
| `and` / `or` / `not` | 論理積／論理和／否定 | 演算の優先順位を確認 |
| `data[i]` | 配列dataの要素番号i | 番号の開始位置は問題文で確認 |
| `data[i, j]` | 二次元配列の行i・列j | Pythonの添字表現と同一視しない |
| `object.member` | メンバ変数・メソッドへのアクセス | 点は小数点とは限らない |
| 未定義 | 値が格納されていない状態 | 数値0とは違う |

「←」は代入、「＝」は比較です。**式の左側の変数が更新される**ことをまず確認しましょう。

### 選択・繰返しの見方

| 記述 | 動作 |
|---|---|
| `if ... elseif ... else ... endif` | 上から順に条件を判定し、最初に真となる枝を実行 |
| `while ... endwhile` | 処理前に条件を判定。0回で終わる場合もある |
| `do ... while` | 処理後に条件を判定。少なくとも1回実行 |
| `for ... endfor` | 制御記述に従って繰り返す。範囲や刻みは記述を確認 |
| `関数名(引数, ...)` | 関数・手続を呼び出す | 引数に何を渡すか確認 |

より詳しい制御構造の比較は[前判定・後判定の繰返し](/fe/control-structures-loop-selection/)で確認できます。

### 演算の優先順位

IPAの別紙2では、主な演算の優先順位は **括弧やメンバアクセス → 単項演算子 → 乗除・mod → 加減 → 比較 → and → or** の順です。

たとえば `true or false and false` は、先に `false and false` を評価するため `true` です。判断が難しければ括弧を補ってください。

## 科目Aでどう出る？

科目Aの基礎知識としては、代入と等価比較、前判定と後判定、配列と添字、論理演算の区別が役立ちます。

特に `x ← x + 1` は数学の等式ではありません。**現在のxに1を足し、その結果をxへ代入**する命令です。これが読めないと科目Bのトレースでも値がずれます。

## 科目Bでどう使う？

### 変数を表で追う（トレース）

次のプログラムは説明用のオリジナル例です。配列 `data` の要素番号は**1から始まる**とし、`data = {4, 7, 2}` です。

```text
○main()
  整数型: i, total
  整数型の配列: data ← {4, 7, 2}
  i ← 1
  total ← 0
  while (i ≦ 3)
    if (data[i] mod 2 = 0)
      total ← total + data[i]
    endif
    i ← i + 1
  endwhile
```

まず `i=1`、`total=0` から開始します。偶数の要素だけを加算するため、各回の変数の変化は次の通りです。

| 判定時のi | data[i] | 偶数？ | 処理後のtotal | 次のi |
|---:|---:|---|---:|---:|
| 1 | 4 | はい | 4 | 2 |
| 2 | 7 | いいえ | 4 | 3 |
| 3 | 2 | はい | 6 | 4 |

最後は `i=4` で `i ≦ 3` が偽となり終了します。**最終的なtotalは6**です。


### 1行ずつ動かすトレース練習

「次の1行」を押すと、**現在の実行行・変数の値・条件の結果**が変化します。偶数だけを合計する上のプログラムと同じ処理です。

<div class="fe-learning-demo fe-pseudocode-demo" data-fe-pseudocode-demo>
  <p class="fe-learning-demo__title">擬似言語トレース：偶数だけ合計</p>
  <p class="fe-learning-demo__hint">配列の添字は1から開始。見るポイント：条件が偽のときは合計を更新しない。</p>
  <div class="fe-pseudocode-demo__layout">
    <div class="fe-pseudocode-demo__code" aria-label="実行中の擬似言語">
      <div data-trace-line="0">i ← 1</div>
      <div data-trace-line="1">total ← 0</div>
      <div data-trace-line="2">while (i ≦ 3)</div>
      <div data-trace-line="3">　if (data[i] mod 2 = 0)</div>
      <div data-trace-line="4">　　total ← total + data[i]</div>
      <div data-trace-line="5">　i ← i + 1</div>
      <div data-trace-line="6">終了</div>
    </div>
    <div class="fe-pseudocode-demo__state">
      <p><strong>配列：</strong> <span data-trace-array>① 4　② 7　③ 2</span></p>
      <p><strong>現在の i：</strong> <output data-trace-i>未設定</output></p>
      <p><strong>現在の total：</strong> <output data-trace-total>未設定</output></p>
      <p><strong>次に実行する行：</strong> <span data-trace-next>i ← 1</span></p>
    </div>
  </div>
  <div class="fe-learning-demo__controls">
    <button type="button" class="fe-learning-demo__button" data-trace-prev disabled>1行戻る</button>
    <button type="button" class="fe-learning-demo__button" data-trace-next-button>次の1行 →</button>
    <button type="button" class="fe-learning-demo__button" data-trace-reset>最初から</button>
  </div>
  <p class="fe-pseudocode-demo__message" data-trace-message role="status" aria-live="polite">開始前です。「次の1行」を押してください。</p>
  <p class="fe-learning-demo__hint">JavaScriptを使えない場合も、直前のトレース表で同じ結果を確認できます。</p>
</div>

### 試験でのトレース手順

1. **初期値**を書く。配列の添字開始番号も確認する。
2. **条件式**を評価し、実行する枝だけを選ぶ。
3. **代入した変数だけ**値を更新する。
4. ループ末尾で**次の添字**を記録する。
5. 再び条件を確認し、偽になった時点で止める。

表では「条件判定時の値」と「処理後の値」を混在させないことがコツです。

## よくある誤解・混同

| 誤読 | 正しくは |
|---|---|
| `←` と `=` は同じ | 代入と比較で役割が異なる |
| `while` の本体は必ず1回実行 | 初回の条件が偽なら0回 |
| `elseif` の後続条件も全部評価する | 先に真となった枝があれば後続の条件は評価しない |
| 配列の最初は必ず0番 | 問題文に指定された要素番号に従う |
| `mod` は割り算の商 | `mod` は余り |
| 未定義は0 | 未定義と0は異なる |
| Pythonと同じ記法で考えればよい | IPA別紙2と問題文の規則で読む |

条件分岐については[条件分岐の判定順序](/fe/condition-branch-order/)、配列の理解には[配列の基本](/fe/array/)も参考になります。

## まとめ（試験直前用）

- `←` は**代入**、`=` は**比較**。
- 配列の**添字開始番号**は必ず問題の指定を確認する。
- `while` は**条件を先に判定**する。
- 演算の順序は、特に **and が or より先**。
- トレースは**初期値→判定→更新→次の判定**を表にする。
- 別紙2は共通の記述形式。**問題ごとの注記が優先**される。

出典：[IPA：擬似言語の記述形式（Ver.5.1、別紙2）](https://www.ipa.go.jp/shiken/syllabus/doe3um0000002djj-att/shiken_yougo_ver5_1.pdf)

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}">
<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}" defer></script>

{% include fe_article_footer.html %}
