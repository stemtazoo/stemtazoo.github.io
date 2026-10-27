---
layout: page
title: エンディアンとは？ビッグとリトルのバイト格納順序【基本情報技術者試験】
description: エンディアンは複数バイトのデータをメモリに置く順序。16進数をバイト単位に分け、ビッグエンディアンとリトルエンディアンを正しく見分ける方法を解説します。
permalink: /fe/endian/
tags: [fe, fe-technology, basic-theory, computer-architecture]
fe_section: テクノロジ系
fe_subsection: 基礎理論
fe_order: 255
date: 2026-10-27
last_modified_at: 2026-10-27
---

## まず結論

エンディアンとは、**複数バイトのデータをメモリにどの順番で格納するか**を決める方式です。

- **ビッグエンディアン**：上位バイトを小さいアドレスに置く
- **リトルエンディアン**：下位バイトを小さいアドレスに置く

基本情報技術者試験では、**16進数を2桁（1バイト）ずつ区切ってから並べる**ことが判断のポイントです。

## 直感的な説明

16進数の `0x12345678` を例にします。16進数2桁は8ビット、つまり1バイトです。

```text
元の値：  12 | 34 | 56 | 78
         上位             下位
```

メモリのアドレスが左から右へ大きくなるとします。

```text
アドレス    +0   +1   +2   +3
ビッグ      12   34   56   78
リトル      78   56   34   12
```

**リトルではバイトの順番を逆にします。16進数の各桁は逆にしません。**

### 自分でバイト配置を切り替える

次の教材では、4バイトの16進数を入力し、方式を切り替えると格納順序が変わります。

<div class="fe-endian-demo" style="border:1px solid #cbd5e1;border-radius:12px;padding:1rem;margin:1rem 0">
  <label for="fe-endian-input"><strong>8桁の16進数（4バイト）</strong></label>
  <input id="fe-endian-input" type="text" value="12345678" maxlength="8" inputmode="text" spellcheck="false" aria-describedby="fe-endian-help" style="display:block;width:100%;max-width:15rem;margin:.5rem 0;padding:.5rem;border:1px solid #94a3b8;border-radius:6px">
  <p id="fe-endian-help" style="font-size:.9rem">例：12345678（0xは不要）</p>
  <div role="group" aria-label="バイトの格納方式" style="display:flex;gap:.5rem;flex-wrap:wrap">
    <button type="button" id="fe-endian-big" aria-pressed="true" style="padding:.5rem;border:1px solid #64748b;border-radius:6px">ビッグ</button>
    <button type="button" id="fe-endian-little" aria-pressed="false" style="padding:.5rem;border:1px solid #64748b;border-radius:6px">リトル</button>
  </div>
  <p id="fe-endian-error" role="status"></p>
  <p><strong>小さいアドレス → 大きいアドレス</strong></p>
  <div id="fe-endian-cells" aria-live="polite" style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.3rem"></div>
  <p id="fe-endian-note"></p>
</div>
<script>
(function () {
  var input = document.getElementById('fe-endian-input');
  var cells = document.getElementById('fe-endian-cells');
  var error = document.getElementById('fe-endian-error');
  var note = document.getElementById('fe-endian-note');
  var big = document.getElementById('fe-endian-big');
  var little = document.getElementById('fe-endian-little');
  if (!input || !cells || !big || !little) return;
  var mode = 'big';
  function render() {
    var value = input.value.trim().toUpperCase();
    var valid = /^[0-9A-F]{8}$/.test(value);
    cells.textContent = '';
    error.textContent = valid ? '' : '16進数8桁（0～9、A～F）を入力してください。';
    note.textContent = '';
    big.setAttribute('aria-pressed', String(mode === 'big'));
    little.setAttribute('aria-pressed', String(mode === 'little'));
    big.style.fontWeight = mode === 'big' ? 'bold' : 'normal';
    little.style.fontWeight = mode === 'little' ? 'bold' : 'normal';
    if (!valid) return;
    var bytes = value.match(/.{2}/g);
    if (mode === 'little') bytes.reverse();
    bytes.forEach(function (byte, i) {
      var cell = document.createElement('div');
      cell.style.cssText = 'text-align:center;padding:.6rem .1rem;border:1px solid #94a3b8;border-radius:6px;min-width:0';
      var addr = document.createElement('div');
      addr.textContent = '+' + i;
      var val = document.createElement('strong');
      val.textContent = byte;
      cell.appendChild(addr);
      cell.appendChild(val);
      cells.appendChild(cell);
    });
    note.textContent = mode === 'big'
      ? '上位バイトを小さいアドレスに配置します。'
      : '下位バイトを小さいアドレスに配置します。';
  }
  input.addEventListener('input', render);
  big.addEventListener('click', function () { mode = 'big'; render(); });
  little.addEventListener('click', function () { mode = 'little'; render(); });
  render();
}());
</script>

**見るポイント：** 切り替えても各バイトの中の2桁は変わらず、4つのバイトの並びだけが変わります。

## 定義・仕組み

### バイトとアドレスの関係

1バイトは8ビットです。16進数1桁は4ビットなので、**16進数2桁で1バイト**です。

4バイトのデータを、1バイトごとにアドレスが付いたメモリに格納すると、4つの連続するアドレスを使います。

### ビッグエンディアン

数値の**上位バイト**を最も小さいアドレスに格納します。

```text
値：        0xA1B2C3D4
アドレス：  +0  +1  +2  +3
内容：      A1  B2  C3  D4
```

### リトルエンディアン

数値の**下位バイト**を最も小さいアドレスに格納します。

```text
値：        0xA1B2C3D4
アドレス：  +0  +1  +2  +3
内容：      D4  C3  B2  A1
```

## 科目Aでどう出る？

例えば、32ビットの値 `0x2468ACE0` を4バイトのメモリに格納する場合を考えます。

1. 16進数を2桁ずつ区切る：`24 | 68 | AC | E0`
2. 最も小さいアドレスがどちらか確認する
3. ビッグなら `24 68 AC E0`、リトルなら `E0 AC 68 24`

**「リトル＝下位バイトが先」**と判断すれば、16進数を1桁ずつ逆にする誤りを防げます。

## どんな場面で使う？

エンディアンは、CPUがメモリ上の複数バイトの値を扱うときや、異なる機器間でバイナリデータをやり取りするときに重要です。

送信側と受信側でバイト順の解釈が違うと、同じ4バイトでも別の数値として読み取られることがあります。通信仕様やファイル形式では、バイト順を明示して扱います。

## よくある誤解・混同

### リトルエンディアンは16進数の各桁を逆にする？

違います。`0x12345678` の場合は、

```text
正しい：78 56 34 12
誤り：  87 65 43 21
```

です。**逆にする単位はバイト**です。

### 1バイトのデータにも違いが出る？

出ません。1バイトしかなければ、バイトの並び替えは起こりません。

### ビット順も逆になる？

なりません。エンディアンは通常、**複数バイトの配置順序**の話です。1バイト内のビット順とは区別します。

### メモリ上の並びと数値の意味は同じ？

メモリ上の並びは異なっても、方式に従って読み取れば元の数値は同じです。方式を取り違えると違う値になります。

## まとめ（試験直前用）

- **ビッグ：上位バイトを小さいアドレスへ**
- **リトル：下位バイトを小さいアドレスへ**
- 16進数は**2桁で1バイト**に区切る
- 逆にするのは**バイト順**であり、各桁やビット順ではない

{% include fe_article_footer.html %}
