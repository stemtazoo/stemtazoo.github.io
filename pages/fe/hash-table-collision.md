---
layout: page
title: ハッシュ表の衝突とは？modを使ったハッシュ値の求め方【基本情報技術者試験】
description: ハッシュ表では、異なるデータでも同じハッシュ値になると衝突が起こります。modを使ったハッシュ値の求め方と、FE試験で「最初に衝突するデータ」を見抜く手順を整理します。
permalink: /fe/hash-table-collision/
tags: [fe, fe-technology, algorithm]
fe_section: テクノロジ系
fe_subsection: アルゴリズムとプログラミング
fe_order: 30
date: 2026-08-18
last_modified_at: 2026-11-01
---

## まず結論

**ハッシュ表の衝突（collision）**とは、異なるデータから**同じハッシュ値**が求められ、同じ格納位置を使おうとすることです。

FE試験では、次の流れで判断すると分かりやすいです。

```text
データを順番に見る
↓
ハッシュ値を求める
↓
過去に出たハッシュ値か確認
↓
初めて同じ値が出たところ
→ 最初の衝突
```

> **同じデータだから衝突するのではなく、同じハッシュ値になったら衝突する。**

このページでは、**modを使ってハッシュ値を計算し、最初の衝突を見つける問題**を中心に扱います。ハッシュ表全体の仕組みや衝突後の処理は、[ハッシュ表とは？](/fe/hash-table/) を参照してください。

---

## 直感的な説明

8個の箱が並んでいるとします。

```text
0 1 2 3 4 5 6 7
```

データをどの箱に入れるかを、次の式で決めます。

```text
h(x) = x mod 8
```

たとえば、18なら、

```text
18 mod 8 = 2
```

なので、箱2へ入れます。

次に26を入れると、

```text
26 mod 8 = 2
```

となります。

18と26は別のデータですが、どちらも箱2を使おうとします。

```text
18 → 2
26 → 2

同じハッシュ値
→ 衝突
```

これがハッシュ表の衝突です。

---

## 定義・仕組み

### ハッシュ表とは

ハッシュ表は、データから計算した**ハッシュ値**を使って、格納位置を決めるデータ構造です。

データを一つずつ先頭から探すのではなく、ハッシュ値から格納位置をすばやく決められるのが特徴です。

```text
データ
↓
ハッシュ関数
↓
ハッシュ値
↓
格納位置
```

### ハッシュ関数とは

ハッシュ関数は、データからハッシュ値を計算する関数です。

FE試験では、次のように余りを使う形がよく出ます。

```text
h(x) = x mod n
```

`mod` は、割り算の**余り**を表します。

```text
25 mod 7 = 4
```

これは、25を7で割った余りが4という意味です。

### 衝突とは

ハッシュ関数を使っても、異なるデータから同じハッシュ値が出ることがあります。

```text
11 mod 7 = 4
25 mod 7 = 4
```

11と25は異なるデータですが、ハッシュ値はどちらも4です。

このような状態が衝突です。

---


### 触って覚える：衝突した後はどこに入る？

ハッシュ値が重なったとき、**チェイン法**は同じ番地のリストにつなぎ、**オープンアドレス法（線形探索）**は空いている別の番地へ進みます。どちらも同じキー列を入れて比べてみましょう。なお、ここでのオープンアドレス法は「次の番地を順に探す」一例です。

<div class="fe-learning-demo" id="fe-hash-collision-demo" aria-label="チェイン法とオープンアドレス法の比較教材">
  <p class="fe-learning-demo__title">キーの挿入：h(x) = x mod 7</p>
  <p>追加するキー：<strong>10 → 17 → 24 → 8 → 15</strong>。最初の3つはすべて余り3で衝突します。</p>
  <div style="display:flex;flex-wrap:wrap;gap:.5rem;margin:.7rem 0">
    <button type="button" data-hc-next>次のキーを挿入</button>
    <button type="button" data-hc-prev disabled>1つ戻す</button>
    <button type="button" data-hc-reset>最初から</button>
  </div>
  <p data-hc-status role="status" aria-live="polite">開始前：次は10を挿入します。</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(235px,1fr));gap:1rem">
    <div>
      <p><strong>チェイン法</strong>：同じ箱に複数のキーをつなぐ</p>
      <div data-hc-chain></div>
    </div>
    <div>
      <p><strong>オープンアドレス法（線形探索）</strong>：空き箱を探す</p>
      <div data-hc-open></div>
    </div>
  </div>
  <p data-hc-log aria-live="off"></p>
  <p><small>各箱の番号は0〜6。オープンアドレス法では末尾6の次は0へ戻ります。表が満杯の場合は挿入できません。</small></p>
  <noscript>JavaScriptが無効な場合の例：10、17、24はすべてmod 7で3。チェイン法なら箱3に「10 → 17 → 24」、線形探索なら箱3に10、箱4に17、箱5に24を格納します。</noscript>
</div>
<script>
(function () {
  'use strict';
  const root = document.getElementById('fe-hash-collision-demo');
  if (!root) return;
  const keys = [10, 17, 24, 8, 15];
  const size = 7;
  const next = root.querySelector('[data-hc-next]');
  const prev = root.querySelector('[data-hc-prev]');
  const reset = root.querySelector('[data-hc-reset]');
  const status = root.querySelector('[data-hc-status]');
  const log = root.querySelector('[data-hc-log]');
  const chainView = root.querySelector('[data-hc-chain]');
  const openView = root.querySelector('[data-hc-open]');
  let count = 0;
  function drawBox(view, index, values, active) {
    const row = document.createElement('div');
    row.style.cssText = 'display:flex;gap:.5rem;align-items:center;border:1px solid #94a3b8;border-radius:.35rem;padding:.35rem .5rem;margin:.2rem 0;' + (active ? 'background:#d8e9e2;color:#173f35;' : '');
    const label = document.createElement('strong');
    label.textContent = String(index);
    label.style.cssText = 'min-width:1.5rem';
    const value = document.createElement('span');
    value.textContent = values || '空き';
    row.append(label, value);
    view.appendChild(row);
  }
  function render() {
    const chains = Array.from({length: size}, () => []);
    const slots = Array(size).fill(null);
    const traces = [];
    let lastChain = -1, lastOpen = -1;
    for (const key of keys.slice(0, count)) {
      const home = key % size;
      const collided = chains[home].length > 0;
      chains[home].push(key);
      let target = home;
      const probes = [home];
      while (slots[target] !== null && probes.length < size) {
        target = (target + 1) % size;
        probes.push(target);
      }
      if (slots[target] === null) slots[target] = key;
      lastChain = home;
      lastOpen = target;
      traces.push(key + ' mod 7 = ' + home + (collided ? '（衝突）' : '（衝突なし）') + '／線形探索：' + probes.join(' → ') + ' → ' + (slots[target] === key ? '箱' + target : '満杯'));
    }
    chainView.replaceChildren();
    openView.replaceChildren();
    for (let i = 0; i < size; i++) {
      drawBox(chainView, i, chains[i].join(' → '), count > 0 && i === lastChain);
      drawBox(openView, i, slots[i] === null ? '' : String(slots[i]), count > 0 && i === lastOpen);
    }
    status.textContent = count === 0 ? '開始前：次は10を挿入します。' : count === keys.length ? '全5件の挿入が完了しました。' : count + '件挿入済み：次は' + keys[count] + 'を挿入します。';
    log.textContent = count === 0 ? '挿入すると、各方式の格納先を表示します。' : '直前の挿入：' + traces[traces.length - 1];
    next.disabled = count === keys.length;
    prev.disabled = count === 0;
  }
  next.addEventListener('click', () => { if (count < keys.length) { count++; render(); } });
  prev.addEventListener('click', () => { if (count > 0) { count--; render(); } });
  reset.addEventListener('click', () => { count = 0; render(); });
  render();
})();
</script>

## 科目Aでどう出る？

科目Aでは、複数のデータを順番にハッシュ表へ入れ、**最初に衝突するデータ**を選ばせる問題が出ます。

### 基本の解き方

たとえば、

```text
11, 25, 18, 30, 33
```

をこの順で、

```text
h(x) = x mod 7
```

で格納するとします。

順番に計算します。

| データ | ハッシュ値 |
|---:|---:|
| 11 | 4 |
| 25 | 4 |

25のハッシュ値4は、11ですでに使われています。

したがって、**25で最初の衝突**が起こります。

> 「最初に衝突する」ときは、全データを最後まで計算せず、同じハッシュ値が再登場したところで止めます。

### 16進数とmod 8のショートカット

16進数の値に対して `mod 8` を求める問題では、すべてを10進数へ変換しなくても求められる場合があります。

16進数 `XY` は、

```text
16 × X + Y
```

と表せます。

ここで、16は8で割り切れるので、

```text
(16 × X + Y) mod 8
```

では、上位桁の `16 × X` は余りに影響しません。

そのため、**下1桁だけ見ればよい**ことがあります。

たとえば、

```text
1A
→ A = 10
→ 10 mod 8 = 2

B2
→ 2 mod 8 = 2
```

なので、`1A` と `B2` は同じハッシュ値になります。

---

## どんな場面で使う？

ハッシュ表は、キーから対応する値を高速に検索したい場面で使われます。

たとえば、

- 会員番号から会員情報を探す
- 商品コードから商品データを探す
- 文字列から登録済み情報を探す
- 辞書型や連想配列を実装する

といった場面です。

Pythonの`dict`のような連想配列も、ハッシュを利用する代表例です。

---

## よくある誤解・混同

### 同じデータが入ったら衝突する

衝突のポイントは、データそのものが同じかどうかではありません。

```text
異なるデータ
↓
同じハッシュ値
↓
衝突
```

### ハッシュ値は必ず異なる

違います。

限られた数の格納位置へ多数のデータを対応させるため、異なるデータから同じハッシュ値が出る可能性があります。

### 最初の衝突は、最初のデータを見る

違います。

1件目には、まだ比較対象となる格納済みデータがありません。

2件目以降について、過去に出たハッシュ値と同じかを確認します。

### 衝突したらハッシュ表は使えない

違います。

実際のハッシュ表では、衝突が起きたときの処理方法を用意します。

代表的な方式には、

- チェイン法
- オープンアドレス法

などがあります。

FE試験では、問題文で衝突時の処理方法まで指定されている場合に、そのルールに従います。

---

## 確認問題（FE試験対策）

10進数のデータを次の順番でハッシュ表へ格納する。

```text
11, 25, 18, 30, 33
```

ハッシュ関数を、

```text
h(x) = x mod 7
```

とする。

最初に衝突するデータはどれか。

- ア. 25
- イ. 18
- ウ. 30
- エ. 33

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：ア**

順番にハッシュ値を求めます。

```text
11 mod 7 = 4
25 mod 7 = 4
```

11ですでにハッシュ値4を使用しているため、25を入れようとした時点で最初の衝突が起こります。

👉 判断ポイント  
**過去に出たハッシュ値が初めて再登場したデータを探す**と考えます。

</details>

---

## まとめ（試験直前用）

- ハッシュ表は、ハッシュ値から格納位置を決める
- `mod` は割り算の余り
- 異なるデータでも同じハッシュ値なら衝突する
- 「最初の衝突」は、順番に計算して同じ値が初めて再登場したところ
- `mod 8` と16進数の組合せでは、下1桁だけで判断できる場合がある
- 衝突時にはチェイン法やオープンアドレス法などで対応する

> **データが同じかではなく、ハッシュ値が同じかを見る。**

{% include fe_article_footer.html %}
