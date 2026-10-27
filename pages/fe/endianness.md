---
layout: page
title: エンディアンとは？ビッグとリトルのバイト配置【基本情報技術者試験】
description: "エンディアンの違いを16進数のバイト分割とメモリアドレスで理解します。ビッグとリトルの切り替え図で、科目Aの判断基準と桁反転の誤解を整理します。"
permalink: /fe/endianness/
tags: [fe, fe-technology, basic-theory, computer-system]
fe_section: テクノロジ系
fe_subsection: 基礎理論
fe_order: 16
date: 2026-10-27
last_modified_at: 2026-10-27
---

## まず結論

**エンディアン**は、複数バイトの数値をメモリに格納するときの**バイトの並び順**です。

- **ビッグエンディアン**：上位バイトを小さいアドレスに置く。
- **リトルエンディアン**：下位バイトを小さいアドレスに置く。

科目Aでは、**16進数を2桁ずつ区切り、小さいアドレスから順に並べる**と判断できます。

## 直感的な説明

16進数の `0x12345678` は4バイトです。16進数2桁が1バイトなので、`12 | 34 | 56 | 78` と分けます。

| メモリアドレス | 0 | +1 | +2 | +3 |
|---|---|---|---|---|
| ビッグエンディアン | 12 | 34 | 56 | 78 |
| リトルエンディアン | 78 | 56 | 34 | 12 |

左側が小さいアドレスです。リトルエンディアンでは、**バイトの順番だけが逆**になります。各バイト内の `78` を `87` に変えたりはしません。

## 定義・仕組み

### 上位バイトと下位バイト

`0x12345678` の左端の `12` が最上位バイト、右端の `78` が最下位バイトです。エンディアンは数値の大小ではなく、**どのバイトをどのアドレスに置くか**を指定します。

### バイト配置を切り替えて確認する

<div id="endian-demo" class="endian-demo">
<p><strong>数値：</strong><code>0x12345678</code></p>
<p><button type="button" data-order="big" aria-pressed="true">ビッグエンディアン</button> <button type="button" data-order="little" aria-pressed="false">リトルエンディアン</button></p>
<div class="endian-cells">
<div><small>0</small><strong>12</strong></div>
<div><small>+1</small><strong>34</strong></div>
<div><small>+2</small><strong>56</strong></div>
<div><small>+3</small><strong>78</strong></div>
</div>
<p class="endian-note" aria-live="polite">上位バイト12が最小アドレスに入ります。</p>
</div>
<style>
.endian-demo{border:1px solid #bdcad1;border-radius:10px;padding:1rem;margin:1rem 0}
.endian-demo button{padding:.5rem;border:1px solid #72869b;border-radius:6px;background:transparent;color:inherit;cursor:pointer;margin-bottom:.4rem}
.endian-demo button[aria-pressed="true"]{background:#d9e9e6;color:#173b38;font-weight:bold}
.endian-cells{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.35rem;max-width:440px}
.endian-cells>div{background:#e9eff3;color:#263c4a;text-align:center;padding:.65rem .2rem;border-radius:5px}
.endian-cells small,.endian-cells strong{display:block}
.endian-cells strong{font:700 1.3rem monospace}
</style>
<script>
(function(){
function init(){
var root=document.getElementById('endian-demo');
if(!root||root.dataset.ready)return;
root.dataset.ready='1';
var buttons=root.querySelectorAll('button[data-order]');
var cells=root.querySelectorAll('.endian-cells strong');
var note=root.querySelector('.endian-note');
buttons.forEach(function(button){
button.addEventListener('click',function(){
var little=button.dataset.order==='little';
var bytes=little?['78','56','34','12']:['12','34','56','78'];
cells.forEach(function(cell,i){cell.textContent=bytes[i]});
buttons.forEach(function(b){b.setAttribute('aria-pressed',String(b===button))});
note.textContent=little?'下位バイト78が最小アドレスに入ります。':'上位バイト12が最小アドレスに入ります。';
});
});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>

## 科目Aでどう出る？

例えば、16進数 `0xA1B2C3D4` を4バイトのメモリに格納する場合は次の順序で考えます。

1. `A1 | B2 | C3 | D4` と2桁ずつ区切る。
2. 小さいアドレスから順に並べる。
3. ビッグなら `A1 B2 C3 D4`、リトルなら `D4 C3 B2 A1`。

**「下位バイトが先」ならリトル、「上位バイトが先」ならビッグ**と切り分けます。

## どんな場面で使う？

CPUが複数バイトの整数をメモリに格納するときや、異なるシステム間でバイナリデータを受け渡すときに関係します。送受信側でバイト順の解釈が異なると、同じバイト列でも別の数値として読んでしまうことがあります。

## よくある誤解・混同

### 16進数の1桁ずつを逆にする？

違います。**1バイト（16進数2桁）を単位**として順番を変えます。例えば `12 34` のリトルエンディアン配置は `34 12` であり、`43 21` ではありません。

### ビットの順序も逆になる？

エンディアンは通常、複数バイトの**バイト順**を指します。1バイト内のビット順とは区別します。

### アドレスは右から左へ増える？

図の左右では決まりません。必ずアドレス表示を見て、**小さいアドレスに何が入るか**で判断します。

## まとめ（試験直前用）

- 16進数は**2桁＝1バイト**で区切る。
- ビッグは**上位バイトから**小さいアドレスへ。
- リトルは**下位バイトから**小さいアドレスへ。
- バイトの中の16進数の桁は逆にしない。

数値のビット表現は[2進数の表現とは？](/fe/binary-representation/)で確認できます。

{% include fe_article_footer.html %}
