---
layout: page
title: キャッシュメモリのヒット率とは？平均アクセス時間の計算をわかりやすく解説【基本情報技術者試験】
description: キャッシュメモリのヒット率を「キャッシュに目的のデータが存在する割合」として整理し、平均アクセス時間、ミス率、2種類のCPUを比較する計算問題の考え方をFE試験向けに解説します。
permalink: /fe/cache-hit-rate-average-access-time/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 85
date: 2026-07-02
last_modified_at: 2026-11-03
---

## まず結論

キャッシュメモリのヒット率とは、**CPUが必要なデータを取りに行ったときに、キャッシュメモリに目的のデータがある割合**です。

基本情報技術者試験では、平均アクセス時間は次の形で考えます。

```text
平均アクセス時間
= キャッシュメモリのアクセス時間 × ヒット率
+ 主記憶のアクセス時間 × ミス率
```

ヒット率を `P` と置くと、ミス率は `1 - P` です。

```text
平均アクセス時間
= キャッシュ時間 × P
+ 主記憶時間 × (1 - P)
```

この形を作れれば、キャッシュの計算問題はかなり解きやすくなります。

キャッシュメモリ自体の役割や、ヒット・ミス時のデータの流れを先に確認したい場合は、[キャッシュメモリとは？ライトスルー・ライトバックの違い]({{ '/fe/cache-memory/' | relative_url }})を確認してください。

## 直感的な説明

キャッシュメモリは、CPUの近くにある **よく使うデータの一時置き場** です。

CPUがデータを必要としたとき、まずキャッシュメモリを見ます。

```text
キャッシュにある
→ 速く取り出せる

キャッシュにない
→ 主記憶まで取りに行くので遅い
```

つまり、平均アクセス時間は、速い場合と遅い場合の平均です。

ただし、単純に2つの時間を足して2で割るわけではありません。

キャッシュに当たることが多いなら、平均はキャッシュ時間に近づきます。  
キャッシュに外れることが多いなら、平均は主記憶時間に近づきます。

英語では、このような平均を `weighted average` といいます。  
日本語では **重み付き平均** と考えると分かりやすいです。

### 触って覚える：ヒット率を変えてCPU A・Bを比較する

**ヒット率が上がると、どちらのCPUが速くなるでしょうか？**

1. ヒット率とCPU A・Bのキャッシュ時間・主記憶時間を設定します。
2. **平均アクセス時間が短いCPU**を予想します。
3. 「判定する」を押し、両方の重み付き平均の式と結果を確認します。
4. ヒット率0%・75%・100%を比べたり、「同じになるヒット率」を使って交点を探したりします。

**この教材の前提：** 本文と同じ単純化モデルを使います。キャッシュヒットの所要時間はキャッシュ時間、ミスの所要時間は主記憶時間として、`平均 = キャッシュ時間 × P + 主記憶時間 × (1-P)` と計算します。実際のCPUではキャッシュ検索の追加時間などが条件によって異なります。2つのCPUには**同じヒット率P**を適用します。

<link rel="stylesheet" href="{{ '/assets/css/fe-cache-average-demo.css' | relative_url }}">

<div class="fe-cache-demo" id="fe-cache-demo" aria-label="CPU AとCPU Bのキャッシュヒット率と平均アクセス時間の比較">
  <p class="fe-cache-demo__step">① ヒット率とCPUのアクセス時間を設定する</p>
  <div class="fe-cache-demo__controls">
    <label for="fe-cache-hit">ヒット率P（0〜100%）
      <input id="fe-cache-hit" type="range" min="0" max="100" step="1" value="0">
    </label>
    <label for="fe-cache-hit-number">ヒット率（%・数値入力）
      <input id="fe-cache-hit-number" type="number" min="0" max="100" step="0.01" value="0">
    </label>
  </div>
  <p class="fe-cache-demo__hint">両CPUとも同じヒット率を使います。ミス率は100%−ヒット率です。</p>
  <div class="fe-cache-demo__controls">
    <label for="fe-cache-a-cache">CPU A：キャッシュ時間（ns）
      <input id="fe-cache-a-cache" type="number" min="0" max="10000" step="1" value="60">
    </label>
    <label for="fe-cache-a-memory">CPU A：主記憶時間（ns）
      <input id="fe-cache-a-memory" type="number" min="0" max="10000" step="1" value="300">
    </label>
    <label for="fe-cache-b-cache">CPU B：キャッシュ時間（ns）
      <input id="fe-cache-b-cache" type="number" min="0" max="10000" step="1" value="20">
    </label>
    <label for="fe-cache-b-memory">CPU B：主記憶時間（ns）
      <input id="fe-cache-b-memory" type="number" min="0" max="10000" step="1" value="420">
    </label>
  </div>
  <p id="fe-cache-error" class="fe-cache-demo__error" role="alert" hidden></p>
  <p class="fe-cache-demo__step">② どちらが速いか予想する</p>
  <div class="fe-cache-demo__controls">
    <label for="fe-cache-guess">平均アクセス時間が短いのは？
      <select id="fe-cache-guess">
        <option value="">予想しなくても進められます</option>
        <option value="a">CPU A</option>
        <option value="b">CPU B</option>
        <option value="equal">同じ</option>
      </select>
    </label>
  </div>
  <div class="fe-cache-demo__actions">
    <button type="button" class="fe-cache-demo__primary" id="fe-cache-check">判定する</button>
    <button type="button" id="fe-cache-equal">同じになるヒット率を探す</button>
    <button type="button" id="fe-cache-reset">最初から</button>
  </div>
  <p class="fe-cache-demo__step">③ 計算式と結果を確認する</p>
  <div class="fe-cache-demo__model">
    <div class="fe-cache-demo__cpu">
      <strong>CPU A</strong>
      <p id="fe-cache-a-value" class="fe-cache-demo__number">？</p>
      <div class="fe-cache-demo__bar"><div class="fe-cache-demo__fill" id="fe-cache-a-fill"></div></div>
      <p id="fe-cache-a-formula">判定後に計算式と結果を表示します。</p>
    </div>
    <div class="fe-cache-demo__cpu">
      <strong>CPU B</strong>
      <p id="fe-cache-b-value" class="fe-cache-demo__number">？</p>
      <div class="fe-cache-demo__bar"><div class="fe-cache-demo__fill" id="fe-cache-b-fill"></div></div>
      <p id="fe-cache-b-formula">判定後に計算式と結果を表示します。</p>
    </div>
  </div>
  <div class="fe-cache-demo__result">
    <p id="fe-cache-feedback" class="fe-cache-demo__feedback" role="status" aria-live="polite">CPU AとCPU Bのどちらが速いか予想しましょう。</p>
    <p id="fe-cache-answer">どちらが短いか予想してから判定しましょう。</p>
  </div>
  <p class="fe-cache-demo__hint">棒の長さは平均アクセス時間の比較用です。<strong>短い方が速い</strong>ことを示します。交点の計算結果は、ヒット率の小数第2位までを入力に反映します。</p>
</div>
<noscript>
  <p>JavaScriptが無効でも、本文の計算例で確認できます。CPU Aは<code>60P+300(1-P)</code>、CPU Bは<code>20P+420(1-P)</code>です。両者の平均アクセス時間が等しくなるヒット率は<code>P=0.75</code>です。</p>
</noscript>
<script src="{{ '/assets/js/fe-cache-average-demo.js' | relative_url }}" defer></script>

## 定義・仕組み

キャッシュメモリは、CPUと主記憶の間にある高速な記憶装置です。

CPUから見ると、キャッシュメモリに目的のデータがあるかどうかで、アクセス時間が変わります。

| 用語 | 意味 |
|---|---|
| キャッシュヒット | 目的のデータがキャッシュにある |
| キャッシュミス | 目的のデータがキャッシュになく、主記憶へ行く |
| ヒット率 | キャッシュヒットする割合 |
| ミス率 | キャッシュミスする割合 |
| 平均アクセス時間 | ヒット時とミス時を考えた平均のアクセス時間 |

ヒット率を `P` とすると、ミス率は `1 - P` になります。

例えば、ヒット率が `0.8` なら、ミス率は `0.2` です。

```text
ヒット率：0.8
ミス率：1 - 0.8 = 0.2
```

平均アクセス時間は、次のように求めます。

```text
平均アクセス時間
= キャッシュ時間 × ヒット率
+ 主記憶時間 × ミス率
```

このテーマは、基本情報技術者試験の「コンピュータシステム」や「コンピュータ構成要素」と関係する内容です。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

## 科目Aでどう出る？

科目Aでは、キャッシュメモリのヒット率や平均アクセス時間を求める計算問題として出題されやすいです。

判断するときは、まず次の3つを整理します。

| 確認する値 | 例 |
|---|---|
| キャッシュのアクセス時間 | 20ナノ秒、40ナノ秒など |
| 主記憶のアクセス時間 | 300ナノ秒、500ナノ秒など |
| ヒット率 | `P`、`0.8`、`90%` など |

問題文にヒット率が与えられている場合は、そのまま平均アクセス時間を計算します。

```text
平均アクセス時間
= キャッシュ時間 × ヒット率
+ 主記憶時間 × (1 - ヒット率)
```

一方で、「2つのCPUの処理時間が等しい」と書かれている場合は、次のように式を作ります。

```text
CPU A の平均アクセス時間 = CPU B の平均アクセス時間
```

この形にすると、未知のヒット率を求められます。

## どんな場面で使う？

問題文では、キャッシュメモリの計算そのものよりも、問題文の条件を式に変換する力が大切です。

次のような例で考えます。

|  | CPU A | CPU B |
|---|---:|---:|
| キャッシュメモリのアクセス時間 | 60ナノ秒 | 20ナノ秒 |
| 主記憶のアクセス時間 | 300ナノ秒 | 420ナノ秒 |

CPU A と CPU B で同じプログラムを実行したところ、処理時間が同じだったとします。

このとき、キャッシュメモリのヒット率を `P` と置きます。

CPU A の平均アクセス時間は、次のようになります。

```text
60P + 300(1 - P)
```

CPU B の平均アクセス時間は、次のようになります。

```text
20P + 420(1 - P)
```

処理時間が同じなので、2つの式を等しくします。

```text
60P + 300(1 - P) = 20P + 420(1 - P)
```

展開します。

```text
60P + 300 - 300P = 20P + 420 - 420P
300 - 240P = 420 - 400P
160P = 120
P = 0.75
```

したがって、この例ではヒット率は `0.75` です。

ポイントは、キャッシュに当たる割合を `P`、外れる割合を `1 - P` と置くことです。

## よくある誤解・混同

キャッシュメモリのヒット率計算でよくある誤解は、**キャッシュ時間と主記憶時間を単純に足してしまうこと**です。

| 誤解 | 正しい理解 |
|---|---|
| キャッシュ時間と主記憶時間を足す | ヒット率とミス率で重み付けする |
| ヒット率が `P` ならミス率も `P` | ミス率は `1 - P` |
| 主記憶には必ずアクセスする | ヒットした場合は、主記憶まで行かない前提で計算することが多い |
| キャッシュが速いCPUが必ず全体でも速い | ミスしたときの主記憶アクセス時間も効く |
| `90%` を `90` として計算する | 計算では `0.90` として扱う |

特に、2つのCPUを比較する問題では、次のような見方が大切です。

```text
キャッシュは速いが、主記憶が遅いCPU
→ ヒット率が高いほど有利

キャッシュは少し遅いが、主記憶が速いCPU
→ ミスしても不利になりにくい
```

そのため、キャッシュ時間だけを見て判断せず、**ヒット時とミス時の両方**を式に入れます。

## 公式問題で確認する

IPAが公開している**令和6年度 基本情報技術者試験 科目A 公開問題の問3**では、2種類のCPUについて、キャッシュメモリと主記憶のアクセス時間が与えられ、両者の処理時間が等しくなるヒット率を求める問題が出題されています。

- [IPA：令和6年度 基本情報技術者試験 科目A 公開問題（PDF）](https://www.ipa.go.jp/shiken/mondai-kaiotu/sg_fe/koukai/eid2eo0000007g1d-att/2024r06_fe_kamoku_a_qs.pdf)

このタイプも考え方は同じです。

```text
CPU X の平均アクセス時間
= CPU Y の平均アクセス時間
```

と置き、ヒット率を `P`、ミス率を `1 - P` として式を作ります。

試験では数値を暗記するのではなく、**「処理時間が等しい」→ 2つの平均アクセス時間を等号で結ぶ**と判断できることが重要です。

## まとめ（試験直前用）

- ヒット率は、目的のデータがキャッシュにある割合
- ミス率は `1 - ヒット率`
- 平均アクセス時間は、キャッシュ時間と主記憶時間の重み付き平均
- 基本式は `キャッシュ時間 × P + 主記憶時間 × (1 - P)`
- 2つのCPUの処理時間が同じなら、平均アクセス時間の式を等号で結ぶ
- `90%` は計算では `0.90` として扱う

{% include fe_article_footer.html %}