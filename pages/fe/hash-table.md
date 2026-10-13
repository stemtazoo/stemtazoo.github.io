---
layout: page
title: ハッシュ表とは？ハッシュ関数と基数変換法を整理【基本情報技術者試験】
description: ハッシュ表を、キーから格納先アドレスを求めてデータを管理する構造として整理します。ハッシュ関数、基数変換法、除算法、衝突の意味と、進数変換だけの問題との違いをFE試験向けに解説します。
permalink: /fe/hash-table/
tags: [fe, fe-technology, data-structure, algorithm]
fe_section: 科目B対策
fe_subsection: データ構造
fe_order: 60
date: 2026-07-30
last_modified_at: 2026-10-13
---

## まず結論

ハッシュ表とは、**キーをハッシュ関数に入力し、データを格納するアドレスを求めるデータ構造**です。

基本情報技術者試験では、次の関係を最初に押さえます。

```text
キー
  ↓ ハッシュ関数
格納先のアドレス
```

試験では、キーからアドレスを求める計算だけでなく、同じアドレスが求められる**衝突**も問われます。

衝突が最初に起きるデータを `mod` で計算する問題は、[ハッシュ表の衝突とは？](/fe/hash-table-collision/) で詳しく整理しています。

## 直感的な説明

たくさんの引き出しが並んだ棚を考えます。

普通にデータを探す場合は、先頭から一つずつ確認することがあります。

一方、ハッシュ表では、キーから引き出し番号を計算します。

```text
会員番号 55550
  ↓ 計算
引き出し番号 0260
```

引き出し番号がすぐに分かれば、先頭から順番に探す必要がありません。

ただし、異なるキーから同じ引き出し番号が求められることがあります。これが衝突です。

### 動かして理解する：キーから格納場所を求める

次の図では、キーを切り替えると `キー mod 10` で求めた格納場所が変わります。**123と133はどちらも場所3**となり、同じ格納先を使おうとすることが分かります。

<div class="fe-learning-demo" id="fe-hash-interactive" aria-label="キーを選んでハッシュ値と格納場所を確認する図解">
  <p class="fe-learning-demo__title">ハッシュ関数：キー mod 10</p>
  <div style="display:flex;flex-wrap:wrap;gap:.5rem;margin:.8rem 0">
    <button type="button" data-hash-key="123" aria-pressed="true">123</button>
    <button type="button" data-hash-key="124" aria-pressed="false">124</button>
    <button type="button" data-hash-key="133" aria-pressed="false">133</button>
  </div>
  <p aria-live="polite">キー <strong data-hash-current>123</strong> → 10で割った余り <strong data-hash-result>3</strong></p>
  <div data-hash-slots style="display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:.35rem;margin:.75rem 0">
    <span>0</span><span>1</span><span>2</span><strong style="background:#d8e9e2;padding:.5rem;border-radius:.35rem;text-align:center">3 ←</strong><span>4</span>
    <span>5</span><span>6</span><span>7</span><span>8</span><span>9</span>
  </div>
  <p data-hash-note>123と133は同じ場所3になります。異なるキーが同じ場所を求めることを「衝突」といいます。</p>
</div>
<script>
(function () {
  const root = document.getElementById('fe-hash-interactive');
  if (!root) return;
  const buttons = root.querySelectorAll('[data-hash-key]');
  const slots = root.querySelector('[data-hash-slots]');
  const current = root.querySelector('[data-hash-current]');
  const result = root.querySelector('[data-hash-result]');
  const note = root.querySelector('[data-hash-note]');
  function update(key) {
    const index = key % 10;
    current.textContent = String(key);
    result.textContent = String(index);
    slots.replaceChildren();
    for (let i = 0; i < 10; i++) {
      const cell = document.createElement(i === index ? 'strong' : 'span');
      cell.textContent = String(i) + (i === index ? ' ←' : '');
      cell.style.cssText = 'padding:.5rem .15rem;text-align:center;border:1px solid #94a3b8;border-radius:.35rem;' + (i === index ? 'background:#d8e9e2;color:#173f35;' : '');
      slots.appendChild(cell);
    }
    buttons.forEach(button => button.setAttribute('aria-pressed', String(Number(button.dataset.hashKey) === key)));
    note.textContent = index === 3
      ? '123と133はどちらも場所3です。異なるキーが同じ場所を求めることを「衝突」といいます。'
      : 'キーを変えると格納場所も変わります。123と133を選んで衝突を確認しましょう。';
  }
  buttons.forEach(button => button.addEventListener('click', () => update(Number(button.dataset.hashKey))));
  update(123);
})();
</script>

## 定義・仕組み

ハッシュ表では、キーとデータを対応させて管理します。

| 用語 | 意味 |
|---|---|
| キー | データを識別する値 |
| ハッシュ関数 | キーからアドレスを求める計算規則 |
| ハッシュ値 | ハッシュ関数によって得られた値 |
| ハッシュ表 | 求めたアドレスを使ってデータを格納する表 |
| 衝突 | 異なるキーから同じアドレスが求められること |

### 基数変換法

基数変換法は、キーを別の進数として扱い、10進数へ変換した結果からアドレスを求める方法です。

例えば、キー `55550` を11進数とみなして10進数へ変換する場合は、次のように計算します。

```text
55550₍11₎
= 5×11⁴ + 5×11³ + 5×11² + 5×11¹ + 0×11⁰
= 80520
```

その後、問題文の指示に従って下4桁を取り出し、係数を掛けます。

```text
80520の下4桁 → 0520
0520 × 0.5 → 0260
```

このような問題では、次の順番を崩さないことが大切です。

```text
1. 指定された進数として読む
2. 10進数へ変換する
3. 指定された桁を取り出す
4. 係数を掛ける
5. 必要なら切り捨てる
```

進数変換そのものを復習したい場合は、[16進小数の変換](/fe/hexadecimal-fraction-conversion/)も参考になります。

### 除算法

除算法は、キーを表の大きさなどで割り、その余りをアドレスとして使う方法です。

```text
アドレス = キー mod 表の大きさ
```

例えば、キーが123、表の大きさが10なら、余り3をアドレスとして使います。

### 衝突への対応

異なるキーから同じアドレスが求められると、そのままでは同じ場所へ格納できません。

代表的な対応には、次の方法があります。

| 方法 | 考え方 |
|---|---|
| チェイン法 | 同じアドレスのデータを連結して管理する |
| オープンアドレス法 | 空いている別の場所を探して格納する |

チェイン法は、[連結リスト](/fe/linked-list/)の考え方と関係します。

このテーマは、基本情報技術者試験の「データ構造」と「アルゴリズム」に関係する内容です。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

## 科目Aでどう出る？

科目Aでは、ハッシュ関数の計算手順や、用語の役割を選ばせる問題が中心です。

| 問題文の表現 | 選ぶ用語・考え方 |
|---|---|
| キーから格納先を計算する | ハッシュ関数 |
| キーとデータをアドレスで対応させる | ハッシュ表 |
| 異なるキーが同じアドレスになる | 衝突 |
| キーを別の進数とみなして変換する | 基数変換法 |
| キーを割った余りを使う | 除算法 |

計算問題では、ハッシュ表の大きさやアドレス範囲も確認します。

```text
アドレス範囲が0000〜4999
→ 得られた値が範囲内か確認する
```

また、次の2つを混同しないことが大切です。

```text
進数を変換する
→ 計算の途中手順

キーから格納先を決める
→ ハッシュ関数の目的
```

## 科目Bでどう使う？

科目Bでは、配列をハッシュ表として使う疑似言語や、衝突時の処理を追う問題に関係します。

読むときは、次の点を順番に確認します。

```text
1. キーから最初のアドレスをどう求めるか
2. その場所が空いているか
3. 衝突したときに次の場所をどう探すか
4. 探索をどの条件で終了するか
```

オープンアドレス法では、衝突後にアドレスを一つずつずらす処理などが使われます。

```text
最初のアドレスが使用中
  ↓
次のアドレスを確認
  ↓
空きが見つかるまで繰り返す
```

このとき、配列の添字、繰返し回数、表の末尾に達した後の戻り方を追うことがポイントです。

探索方法との違いも整理しておきましょう。[線形探索](/fe/linear-search/)は先頭から順番に探し、[二分探索](/fe/binary-search/)は整列済みデータを半分ずつ絞り込みます。ハッシュ法は、キーから格納先を直接計算する考え方です。

### 探索方法を選択肢から切り分ける

| 探索方法 | 何を手掛かりに探す？ | 代表的な計算量 |
|---|---|---|
| 線形探索 | 先頭から順番に比較 | O(n) |
| 二分探索 | 整列済みの範囲を半分ずつ絞る | O(log n) |
| ハッシュ法 | キーから格納先を計算 | 平均 O(1) |

ハッシュ法は**2分木を使う方法ではありません**。また、異なるキーが同じ格納先になる衝突が起こり得るため、「衝突しない」という説明も誤りです。

**平均 O(1) は常に一定時間という意味ではありません。** 衝突が集中するなど、実装や条件によっては最悪 O(n) になることがあります。試験では「キーの関数値で格納場所を決める」を最優先の判断基準にします。

## よくある誤解・混同

### 誤解1：ハッシュ関数は暗号化のためだけに使う

ハッシュという言葉は情報セキュリティでも使われますが、ハッシュ表では、**キーから格納先を求めること**が目的です。

```text
ハッシュ表
→ データの格納・探索

暗号学的ハッシュ関数
→ 改ざん検知など
```

同じ「ハッシュ」でも、問題文の目的を確認します。

改ざん検知などに使うセキュリティ側のハッシュ関数は、[ハッシュ関数とは？改ざん検知に使う一方向の要約値](/fe/hash-function/) で整理しています。

### 誤解2：基数変換法は進数変換だけの問題だと思う

10進数へ変換したところで終わりではありません。

```text
10進数へ変換
  ↓
指定された桁を取り出す
  ↓
係数を掛ける
  ↓
アドレスを決める
```

最後に何をアドレスとして使うのかまで確認します。

### 誤解3：異なるキーなら必ず異なるアドレスになる

ハッシュ表のアドレス数には限りがあるため、異なるキーから同じアドレスが求められることがあります。

```text
異なるキー
  ↓
同じアドレス
  → 衝突
```

### 誤解4：ハッシュ法なら必ず1回で見つかる

衝突がなければ高速にアクセスできますが、衝突が多いと追加の探索が必要になります。

そのため、ハッシュ関数の選び方や衝突への対応が重要です。

## まとめ（試験直前用）

- ハッシュ表は、キーから格納先アドレスを求めてデータを管理する
- キーからアドレスを求める計算規則がハッシュ関数
- 基数変換法は、キーを指定された進数として10進数へ変換して使う
- 異なるキーが同じアドレスになることを衝突という
- 進数変換で終わらず、桁の抽出・係数・切捨てまで問題文どおりに行う

{% include fe_article_footer.html %}
