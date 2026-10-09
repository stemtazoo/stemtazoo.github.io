---
layout: page
title: 再帰関数のトレースとは？呼び出しスタックと戻り値を見える化【基本情報技術者試験】
description: 科目Bで再帰関数の実行位置を見失わないために、呼び出し中・待機中・戻り処理を区別し、スタックと戻り値を1ステップずつ追う練習教材です。
permalink: /fe/recursion-trace/
tags: [fe, fe-technology, algorithm, programming, trace]
fe_section: 科目B対策
fe_subsection: トレース
fe_order: 71
date: 2026-10-09
last_modified_at: 2026-10-09
---

## まず結論

再帰関数のトレースでは、**同じ関数名でも呼び出しごとに別の状態を持つ**ことが重要です。呼び出し元は一時停止し、呼び出し先の結果が戻ると、その続きから再開します。

このページは[再帰処理の基本](/fe/recursion/)や[再帰関数の展開](/fe/recursive-function/)を読んだ後、**実行位置を見失わないための練習**に使います。

## 直感的な説明

再帰は、途中まで書いた計算をいったん保留して、別の計算を先に済ませる仕組みです。

```text
f(3) = 3 × f(2)  ← f(2)の結果を待つ
f(2) = 2 × f(1)  ← f(1)の結果を待つ
f(1) = 1         ← ここで止まる
```

戻る順番は逆になります。

```text
f(1) = 1 → f(2) = 2 → f(3) = 6
```

## 定義・仕組み

- **呼び出しスタック**：現在実行中の呼び出しと、結果を待っている呼び出しを保持する仕組み
- **スタックフレーム**：1回の呼び出しに対応する引数・ローカル変数・戻り先などの情報
- **終了条件（基底条件）**：それ以上自分自身を呼び出さず、値を返す条件
- **戻り値**：呼び出し先から呼び出し元へ渡される結果

次の例は説明用のオリジナル擬似言語です。

```text
○整数型: f(整数型: n)
  if (n = 1)
    return 1
  endif
  return n × f(n - 1)
```

**見るポイント：** `return n × f(n - 1)` では、先に `f(n - 1)` の結果を待ち、戻ってきた値に `n` を掛けます。

## 科目Aでどう出る？

再帰・終了条件・スタック（後入れ先出し）の関係を区別します。**終了条件に近づく引数の変化**を確認しましょう。

## 科目Bでどう使う？

### 1ステップずつ動かす再帰トレース

「次へ」で、**コード・スタック・戻り値**が連動して変わります。戻り値は、関数を数値に置き換える計算過程をカードで表示し、最新の結果を青く強調します。最初は `f(3)`、慣れたら `f(4)` に変更してください。

<div class="fe-learning-demo fe-recursion-trace" data-fe-recursion-trace>
  <p class="fe-learning-demo__title">再帰の行きと戻りを確認</p>
  <label for="fe-recursion-n">最初に呼び出す関数</label>
  <select id="fe-recursion-n" data-recursion-input><option value="3">f(3)</option><option value="4">f(4)</option></select>
  <div class="fe-recursion-trace__layout">
    <div>
      <p class="fe-recursion-trace__heading">① 実行中のコード</p>
      <div class="fe-recursion-trace__code" aria-label="擬似言語">
        <div data-recursion-line="0">f(n)</div>
        <div data-recursion-line="1">　if (n = 1)</div>
        <div data-recursion-line="2">　　return 1</div>
        <div data-recursion-line="3">　return n × f(n - 1)</div>
      </div>
    </div>
    <div>
      <p class="fe-recursion-trace__heading">② 呼び出しスタック（下が最新）</p>
      <div data-recursion-stack class="fe-recursion-trace__stack">まだ呼び出していません。</div>
    </div>
  </div>
  <p class="fe-recursion-trace__heading">③ 戻り値の流れ</p>
  <div data-recursion-returns class="fe-recursion-trace__returns" aria-label="確定した戻り値と計算過程">まだ戻り値はありません。</div>
  <div class="fe-learning-demo__controls">
    <button type="button" class="fe-learning-demo__button" data-recursion-prev disabled>1ステップ戻る</button>
    <button type="button" class="fe-learning-demo__button" data-recursion-next>次のステップ →</button>
    <button type="button" class="fe-learning-demo__button" data-recursion-reset>最初から</button>
  </div>
  <p data-recursion-message class="fe-recursion-trace__message" role="status" aria-live="polite">開始前です。次のステップを押してください。</p>
  <p class="fe-learning-demo__hint">青い行＝今のステップで実行した行。青いスタック枠＝現在処理中の呼び出し。灰色＝呼び出し先の結果を待つ呼び出し。戻り値の青いカード＝直近で確定した計算結果。</p>
</div>

JavaScriptを使えない場合は、以下の静的なトレース表でも同じ順番を確認できます。

| 順番 | 動作 | スタックの状態（下が最新） |
|---:|---|---|
| 1 | f(3) 呼び出し | f(3) |
| 2 | f(2) 呼び出し、f(3) は待機 | f(3), f(2) |
| 3 | f(1) 呼び出し、f(2) は待機 | f(3), f(2), f(1) |
| 4 | f(1) が 1 を返す | f(3), f(2) |
| 5 | f(2) が 2 × 1 = 2 を返す | f(3) |
| 6 | f(3) が 3 × 2 = 6 を返す | 空 |

## よくある誤解・混同

| 誤解 | 正しい見方 |
|---|---|
| 同じ関数なので n も一つだけ | 呼び出しごとに n が別々に存在する |
| f(3) が f(2) を呼んだら f(3) は終了 | f(3) は結果を待っている |
| 終了条件に達したら全部終了 | そこから呼び出し元へ順番に戻る |
| 呼び出し順と戻る順は同じ | スタックなので戻る順番は逆 |

## まとめ（試験直前用）

1. **終了条件**を先に確認する。
2. 呼び出すたびに**別のフレーム**を積む。
3. 呼び出し元は**待機中**として残す。
4. 戻り値が確定したら**一段ずつ戻る**。
5. 再開位置は「呼び出しの後」である。

関連：[スタックの仕組み](/fe/stack/)・[IPA公式：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)

<link rel="stylesheet" href="{{ '/assets/css/fe-recursion-trace.css' | relative_url }}?v=20261009-spacing2">
<script src="{{ '/assets/js/fe-recursion-trace.js' | relative_url }}" defer></script>

{% include fe_article_footer.html %}
