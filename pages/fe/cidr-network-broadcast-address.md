---
layout: page
title: CIDR表記からネットワークアドレスとブロードキャストアドレスを求める方法【基本情報技術者試験】
description: CIDR表記の「/22」などをネットワーク部とホスト部に分け、ネットワークアドレスとブロードキャストアドレスを求める手順を整理します。/24以外で迷いやすいブロックサイズの見方まで、FE科目Aで使える判断軸として解説します。
permalink: /fe/cidr-network-broadcast-address/
tags: [fe, fe-technology, network, ip-address]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 58
date: 2026-08-15
last_modified_at: 2026-10-08
---

## まず結論

CIDR表記の `/22` のような数字は、**IPアドレス32ビットのうち、先頭から何ビットをネットワーク部として使うか**を表します。

ネットワークアドレスとブロードキャストアドレスは、次のルールで求められます。

```text
ネットワークアドレス
→ ホスト部をすべて0にする

ブロードキャストアドレス
→ ホスト部をすべて1にする
```

基本情報技術者試験では、まずこの2つを区別できることが重要です。

```text
ホスト部を全部0
→ ネットワークアドレス

ホスト部を全部1
→ ブロードキャストアドレス
```

さらに `/22` や `/21` のように、8ビット単位で区切れない場合は、**第3オクテットも変化する**ことに注意します。

## 直感的な説明

<style>
.cidr-visual{border:1px solid #cbd5e1;border-radius:12px;padding:1rem;margin:1.2rem 0;max-width:100%;box-sizing:border-box}
.cidr-visual *{box-sizing:border-box}
.cidr-visual .cidr-choices{display:flex;flex-wrap:wrap;gap:.5rem;margin:.75rem 0 1rem}
.cidr-visual button{border:1px solid #64748b;border-radius:7px;background:transparent;color:inherit;padding:.45rem .85rem;cursor:pointer}
.cidr-visual button[aria-pressed="true"]{background:#335f7b;color:#fff;border-color:#335f7b}
.cidr-visual .cidr-octets{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.3rem}
.cidr-visual .cidr-octet{border-radius:7px;background:#e3eef5;color:#18374b;text-align:center;padding:.65rem .1rem;min-width:0}
.cidr-visual .cidr-octet:last-child{background:linear-gradient(to right,#e3eef5 0%,#e3eef5 var(--cidr-octet-net,0%),#f4e9d8 var(--cidr-octet-net,0%),#f4e9d8 100%);color:#18374b}
.cidr-visual .cidr-octet strong{display:block;font-size:clamp(1.15rem,4vw,1.65rem)}
.cidr-visual .cidr-octet small{font-size:.7rem}
.cidr-visual .cidr-bar{display:flex;height:18px;border-radius:5px;overflow:hidden;margin:.45rem 0}
.cidr-visual .cidr-net{background:#4b829f}.cidr-visual .cidr-host{background:#c99b56}
.cidr-visual .cidr-bits{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:.2rem;margin:.4rem 0}
.cidr-visual .cidr-bit{color:#fff;text-align:center;padding:.3rem 0;border-radius:3px;font-family:monospace;font-weight:700}
.cidr-visual .cidr-bit.cidr-net{background:#335f7b}
.cidr-visual .cidr-bit.cidr-host{color:#30210d}
.cidr-visual .cidr-stats{display:flex;justify-content:space-between;gap:.5rem;flex-wrap:wrap;font-size:.85rem}
.cidr-visual dl{margin:.75rem 0 0;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:.6rem .3rem}
.cidr-visual dt{min-width:0}.cidr-visual dd{margin:0;font-weight:700;text-align:right;overflow-wrap:anywhere}
.cidr-visual .cidr-note{font-size:.85rem;margin:.75rem 0 0}
@media(max-width:380px){.cidr-visual{padding:.7rem}.cidr-visual dl{grid-template-columns:1fr}.cidr-visual dd{text-align:left;margin-bottom:.3rem}}
</style>

<div class="cidr-visual" data-cidr-visual>
  <strong>図解：192.168.0.10 のネットワーク</strong>
  <p class="cidr-note">CIDR表記を切り替えて、ネットワーク部とホスト部の境界を比べてみましょう。</p>
  <div class="cidr-choices" role="group" aria-label="CIDR表記を選択">
    <button type="button" data-prefix="24" aria-pressed="true">/24</button>
    <button type="button" data-prefix="25" aria-pressed="false">/25</button>
    <button type="button" data-prefix="26" aria-pressed="false">/26</button>
  </div>
  <div class="cidr-octets" aria-label="IPアドレス 192.168.0.10">
    <div class="cidr-octet"><strong>192</strong><small>ネット部</small></div>
    <div class="cidr-octet"><strong>168</strong><small>ネット部</small></div>
    <div class="cidr-octet"><strong>0</strong><small>ネット部</small></div>
    <div class="cidr-octet" data-last-octet><strong>10</strong><small data-octet-label>ホスト部</small></div>
  </div>
  <p class="cidr-note">第4オクテット「10」の2進数（8ビット）</p>
  <div class="cidr-bits" data-octet-bits role="img" aria-label="00001010：ネットワーク部0ビット、ホスト部8ビット">
    <span class="cidr-bit cidr-host" data-last-bit aria-hidden="true">0</span>
    <span class="cidr-bit cidr-host" data-last-bit aria-hidden="true">0</span>
    <span class="cidr-bit cidr-host" data-last-bit aria-hidden="true">0</span>
    <span class="cidr-bit cidr-host" data-last-bit aria-hidden="true">0</span>
    <span class="cidr-bit cidr-host" data-last-bit aria-hidden="true">1</span>
    <span class="cidr-bit cidr-host" data-last-bit aria-hidden="true">0</span>
    <span class="cidr-bit cidr-host" data-last-bit aria-hidden="true">1</span>
    <span class="cidr-bit cidr-host" data-last-bit aria-hidden="true">0</span>
  </div>
  <p class="cidr-note" data-octet-caption>第4オクテット：ネット部0ビット／ホスト部8ビット</p>
  <div class="cidr-stats"><span>ネットワーク部 <b data-net-bits>24</b>ビット</span><span>ホスト部 <b data-host-bits>8</b>ビット</span></div>
  <div class="cidr-bar" aria-label="ネットワーク部とホスト部のビット数">
    <div class="cidr-net" data-net-bar style="width:75%"></div>
    <div class="cidr-host" data-host-bar style="width:25%"></div>
  </div>
  <dl aria-live="polite">
    <dt>サブネットマスク</dt><dd data-mask>255.255.255.0</dd>
    <dt>ネットワークアドレス</dt><dd data-network>192.168.0.0</dd>
    <dt>ブロードキャストアドレス</dt><dd data-broadcast>192.168.0.255</dd>
    <dt>末尾のアドレス範囲</dt><dd data-range>0〜255</dd>
  </dl>
  <p class="cidr-note">青：ネットワーク部 ／ 茶：ホスト部。/24 では第4オクテットの8ビット全部がホスト部です。/25 は先頭1ビット、/26 は先頭2ビットがネットワーク部になります。</p>
</div>
<script>
(function(){
  function init(){
    var root=document.querySelector('[data-cidr-visual]');
    if(!root)return;
    var data={
      24:{mask:'255.255.255.0',network:'192.168.0.0',broadcast:'192.168.0.255',range:'0〜255'},
      25:{mask:'255.255.255.128',network:'192.168.0.0',broadcast:'192.168.0.127',range:'0〜127'},
      26:{mask:'255.255.255.192',network:'192.168.0.0',broadcast:'192.168.0.63',range:'0〜63'}
    };
    root.querySelectorAll('[data-prefix]').forEach(function(button){
      button.addEventListener('click',function(){
        var n=Number(button.getAttribute('data-prefix')),d=data[n];
        root.querySelectorAll('[data-prefix]').forEach(function(b){b.setAttribute('aria-pressed',String(b===button));});
        root.querySelector('[data-net-bits]').textContent=n;
        root.querySelector('[data-host-bits]').textContent=32-n;
        root.querySelector('[data-net-bar]').style.width=(n/32*100)+'%';
        root.querySelector('[data-host-bar]').style.width=((32-n)/32*100)+'%';
        var octetNet=n-24,octetHost=32-n;
        root.querySelector('[data-last-octet]').style.setProperty('--cidr-octet-net',(octetNet/8*100)+'%');
        root.querySelector('[data-octet-label]').textContent=octetNet===0?'ホスト部':'ネット＋ホスト';
        root.querySelectorAll('[data-last-bit]').forEach(function(bit,i){
          bit.className='cidr-bit '+(i<octetNet?'cidr-net':'cidr-host');
        });
        root.querySelector('[data-octet-bits]').setAttribute('aria-label','00001010：ネットワーク部'+octetNet+'ビット、ホスト部'+octetHost+'ビット');
        root.querySelector('[data-octet-caption]').textContent='第4オクテット：ネット部'+octetNet+'ビット／ホスト部'+octetHost+'ビット';
        ['mask','network','broadcast','range'].forEach(function(k){root.querySelector('[data-'+k+']').textContent=d[k];});
      });
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>


IPv4アドレスは、全部で32ビットあります。

例えば、次のCIDR表記を考えます。

```text
192.168.18.70/22
```

`/22` は、先頭22ビットがネットワーク部という意味です。

```text
32ビット全体
├─ ネットワーク部 22ビット
└─ ホスト部       10ビット
```

同じネットワークに属する端末は、ネットワーク部が共通です。

一方、ホスト部は、そのネットワークの中で各端末を区別するために使われます。

このホスト部をすべて0にすると、そのネットワーク自体を表す**ネットワークアドレス**になります。

逆に、ホスト部をすべて1にすると、そのネットワーク内の全端末へ送るための**ブロードキャストアドレス**になります。

## 定義・仕組み

### CIDR表記とは

CIDR表記では、IPアドレスの後ろに `/数字` を付けて、ネットワーク部の長さを表します。

```text
192.168.10.25/24
             ↑
      ネットワーク部は24ビット
```

IPv4アドレスは32ビットなので、ホスト部の長さは次のように考えられます。

```text
ホスト部のビット数
= 32 - プレフィックス長
```

例えば `/22` なら、

```text
32 - 22 = 10
```

なので、ホスト部は10ビットです。

### サブネットマスクとの関係

サブネットマスクは、**IPアドレスそのものではなく、IPアドレスのどこまでがネットワーク部で、どこからがホスト部かを示す情報**です。

例えば、1つのネットワークをさらに小さなネットワークへ分割するときは、ホスト部の一部をネットワーク部として使います。

~~~text
IPアドレス
├─ ネットワーク部
└─ ホスト部

ホスト部の一部をネットワーク部として使う
↓
より小さいネットワークに分割
~~~

`/22` を2進数のサブネットマスクで表すと、先頭22ビットが1になります。

```text
11111111.11111111.11111100.00000000
```

10進数では次のようになります。

```text
255.255.252.0
```

ここで注目するのは第3オクテットです。

```text
252 = 11111100
```

第3オクテットの下位2ビットはホスト部なので、ネットワークの区切りは第3オクテットで4ずつになります。

```text
0  ～ 3
4  ～ 7
8  ～ 11
12 ～ 15
16 ～ 19
20 ～ 23
...
```

### 正しいサブネットマスクの形

IPv4のサブネットマスクは、2進数で見ると**1が左から連続し、その後は0だけ**になります。

~~~text
11111111.11111111.11111111.10000000
~~~

途中で0になったあとに、再び1が現れる形にはなりません。

~~~text
正しい
11111111.11111111.11111111.10000000

誤り
11111111.11111111.11111111.01000000
~~~

FE試験でサブネットマスクとして正しい値を選ぶ問題では、末尾オクテットを2進数にして、**1が左から連続しているか**を確認すると判断できます。

代表的な値は次のとおりです。

| 10進数 | 2進数 |
|---:|---|
| 0 | 00000000 |
| 128 | 10000000 |
| 192 | 11000000 |
| 224 | 11100000 |
| 240 | 11110000 |
| 248 | 11111000 |
| 252 | 11111100 |
| 254 | 11111110 |
| 255 | 11111111 |

この並びを覚えておくと、選択肢をかなり速く切れます。

### ブロックサイズで考える

2進数に毎回すべて変換しなくても、サブネットマスクから**ブロックサイズ**を求めると判断しやすくなります。

第3オクテットが `252` なら、

```text
256 - 252 = 4
```

なので、4個ずつが一つのネットワーク範囲になります。

```text
16 ～ 19
20 ～ 23
24 ～ 27
...
```

例えば、

```text
192.168.18.70/22
```

の第3オクテットは `18` なので、`16 ～ 19` の範囲に入ります。

したがって、

```text
ネットワークアドレス
192.168.16.0

ブロードキャストアドレス
192.168.19.255
```

となります。

### /24から考えると分かりやすい

まず `/24` を基準にすると理解しやすくなります。

```text
192.168.10.123/24
```

`/24` では第4オクテットの8ビットがすべてホスト部です。

```text
ネットワークアドレス
192.168.10.0

ブロードキャストアドレス
192.168.10.255
```

一方、`/22` ではホスト部が10ビットあります。

つまり、第4オクテットの8ビットだけでなく、**第3オクテットの下位2ビットもホスト部**です。

そのため、ブロードキャストアドレスを求めるときに第4オクテットだけを255にしてはいけません。

## 科目Aでどう出る？

科目Aでは、IPアドレスとプレフィックス長から、ネットワークアドレスやブロードキャストアドレスを選ぶ問題が出ます。

### 判断手順

次の順番で考えると整理しやすくなります。

```text
1. /数字からネットワーク部の長さを確認
2. 32から引いてホスト部の長さを確認
3. サブネットマスクを求める
4. ブロックサイズを確認
5. 対象IPアドレスが入る範囲を探す
6. 範囲の最初 → ネットワークアドレス
7. 範囲の最後 → ブロードキャストアドレス
```

### /24以外では第3オクテットに注意

特に `/17 ～ /23` では、第3オクテットの途中にネットワーク部とホスト部の境界があります。

例えば次のように整理できます。

| CIDR | サブネットマスク | 第3オクテットのブロックサイズ |
|---|---|---:|
| /24 | 255.255.255.0 | 1 |
| /23 | 255.255.254.0 | 2 |
| /22 | 255.255.252.0 | 4 |
| /21 | 255.255.248.0 | 8 |
| /20 | 255.255.240.0 | 16 |

試験中は、次の対応を覚えておくと判断が速くなります。

```text
/24 → 1ずつ
/23 → 2ずつ
/22 → 4ずつ
/21 → 8ずつ
/20 → 16ずつ
```

### 選択肢を切るポイント

サブネットマスクの定義を問う問題では、まず次の切り分けが使えます。

| 説明 | 実際の用語 |
|---|---|
| IPアドレスのネットワーク部とホスト部の境界を示す | サブネットマスク |
| 1つのグローバルIPアドレスを複数端末で共有する | NAPT |
| 同一ネットワーク内の全端末へ同じ情報を送る宛先 | ブロードキャストアドレス |

~~~text
ネットワーク部とホスト部を分ける
→ サブネットマスク

1つのグローバルIPを複数端末で共有
→ NAPT

同一ネットワーク内の全端末へ送信
→ ブロードキャスト
~~~

NAPTとの違いは、[NATとNAPTの違い](/fe/nat-napt/)で整理しています。

### ユニキャスト・マルチキャスト・ブロードキャストの違い

送信方式を問う問題では、**「誰に送るか」と「1回の送信で届くか」**を見ると切り分けやすくなります。

| 方式 | 送信対象 | 試験での見分け方 |
|---|---|---|
| ユニキャスト | 1台 | 1対1で送る |
| マルチキャスト | 選択した複数台 | 特定グループへ1回で送る |
| ブロードキャスト | 同一ブロードキャストドメイン内の全端末 | 全員へ1回で送る |

~~~text
1台だけ
→ ユニキャスト

選択した複数台
→ マルチキャスト

同一範囲の全端末
→ ブロードキャスト
~~~

特に、ブロードキャストは**各端末へ順番に個別送信する方式ではありません**。1回送信したフレームやパケットが、対象範囲の全端末へ届きます。

古い過去問では「同一セグメント内のすべてのノード」と表現されることがあります。現在の学習では、**同一ブロードキャストドメイン内の全端末**と考えると安全です。

サブネットマスクとして正しい値かどうかだけを問われた場合は、次の順番で確認します。

~~~text
1. 255が続いている部分はそのまま見る
2. 境界となるオクテットだけを2進数にする
3. 1が左から連続しているか確認する
4. 0の後に1が出たら不正
~~~

例えば、

~~~text
255.255.255.128
~~~

の末尾は、

~~~text
128 = 10000000
~~~

なので正しい形です。

一方、

~~~text
255.255.255.64
~~~

の末尾は、

~~~text
64 = 01000000
~~~

で、0の後に1が現れるためサブネットマスクとして不適切です。

例えば `/22` なのに、IPアドレスの第3オクテットをそのまま残して末尾だけ `.255` にした選択肢は要注意です。

```text
/22
→ 第3オクテットにもホスト部がある
→ 第4オクテットだけ見てはいけない
```

また、ネットワークアドレスとブロードキャストアドレスを逆にしないようにします。

```text
ホスト部が全部0
→ ネットワークアドレス

ホスト部が全部1
→ ブロードキャストアドレス
```

## どんな場面で使う？

CIDRやサブネットマスクは、IPネットワークを複数の範囲に分割するときに使います。

例えば、社内ネットワークを部署ごとに分けたり、ルータが宛先IPアドレスから転送先ネットワークを判断したりするときに関係します。

また、ネットワーク設定では、端末のIPアドレスだけでなく、サブネットマスクやデフォルトゲートウェイも合わせて設定します。

基本情報技術者試験では、実際の設定作業よりも、**指定されたIPアドレスがどのネットワーク範囲に属するかを判断できること**が重要です。

公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

## よくある誤解・混同

### /22は22個のIPアドレスを使えるという意味

違います。

`/22` の22は、**ネットワーク部のビット数**です。

```text
/22
→ ネットワーク部22ビット
→ ホスト部10ビット
```

IPアドレスの個数そのものを表しているわけではありません。

### ブロードキャストアドレスは末尾を255にすればよい

常にそうとは限りません。

`/24` なら第4オクテットだけがホスト部なので、結果として末尾が255になります。

しかし `/22` では、第3オクテットの下位2ビットもホスト部です。

```text
/24
→ 第4オクテットだけ変化

/22
→ 第3オクテットの一部も変化
```

### ネットワークアドレスはIPアドレスの末尾を0にすればよい

これも `/24` では成り立ちますが、常に正しいわけではありません。

`/22` などでは、第3オクテットもネットワーク範囲の先頭に合わせる必要があります。

### サブネットマスクなら、どんな0〜255の値でも使える

違います。

サブネットマスクは2進数で、

~~~text
111...1100...00
~~~

のように、**1が連続したあと0が続く形**でなければなりません。

そのため、例えば 1、32、64 などは、境界となるオクテットの値としては使えません。

~~~text
1   = 00000001
32  = 00100000
64  = 01000000
~~~

いずれも0の後に1が現れます。

### サブネットマスクとNAPTは同じもの

異なります。

~~~text
サブネットマスク
→ ネットワーク部とホスト部の境界を示す

NAPT
→ 複数端末が1つのグローバルIPアドレスを共有して通信する
~~~

「複数端末で1つのIPアドレスを共有」という説明が出たら、サブネットマスクではなくNAPTを疑います。

### サブネットマスクとブロードキャストアドレスは同じもの

異なります。

サブネットマスクは、ネットワーク部とホスト部の境界を示すために使います。

ブロードキャストアドレスは、そのネットワーク内の全端末を宛先とするための特別なアドレスです。

### ブロードキャストは全端末へ順番に送る

違います。

ブロードキャストは、送信元が各端末へ順番に個別送信する方式ではありません。

~~~text
送信元
↓ 1回送信
対象範囲の全端末へ届く
~~~

一方、送信先が1台ならユニキャスト、選択した複数台ならマルチキャストです。

## まとめ（試験直前用）

- `/数字` は、**ネットワーク部のビット数**を表す
- ネットワークアドレスは、**ホスト部を全部0**にする
- ブロードキャストアドレスは、**ホスト部を全部1**にする
- `/22` では第3オクテットにもホスト部があるので、第4オクテットだけを見ない
- `/23 → 2、/22 → 4、/21 → 8` のブロックサイズを使うと速く判断できる
- サブネットマスクは、**ネットワーク部とホスト部の境界を示す**
- **1つのグローバルIPを複数端末で共有 → NAPT**
- **同一ネットワーク内の全端末へ送る宛先 → ブロードキャストアドレス**
- **ユニキャスト＝1台、マルチキャスト＝選択した複数台、ブロードキャスト＝同一範囲の全端末**
- ブロードキャストは**各端末へ順番に送るのではなく、1回の送信で全端末へ届ける**
- サブネットマスクは**1が左から連続し、その後は0だけ**
- 境界オクテットの代表値は **0, 128, 192, 224, 240, 248, 252, 254, 255**

{% include fe_article_footer.html %}
