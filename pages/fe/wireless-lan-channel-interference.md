---
layout: page
title: 2.4GHz無線LANのチャネル干渉とは？1・6・11の使い分け【基本情報技術者試験】
description: 2.4GHz帯の無線LANで起こるチャネル干渉を、近接チャネルの重なり、1・6・11の代表的なチャネル設計、SSIDやローミングとの違いから整理し、FE科目Aで選択肢を切る判断基準を解説します。
permalink: /fe/wireless-lan-channel-interference/
tags: [fe, fe-technology, network, wireless-lan, wifi]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 66
date: 2026-09-20
last_modified_at: 2026-11-24
image:
  path: https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/fe/wireless-lan-channel-interference.png
  width: 1200
  height: 630
  alt: "2.4GHz帯の無線LANで、チャネル1・2・3の周波数帯が重なる例と、1・6・11を離して配置する例を比較した図"
---

## まず結論

2.4GHz帯の無線LANでは、**近いチャネル番号同士は周波数帯が重なりやすく、近接するアクセスポイント同士で干渉しやすい**という特徴があります。

基本情報技術者試験では、次の判断が重要です。

```text
近接するAP
＋
2.4GHz帯
↓
離れたチャネルを割り当てる
```

代表的な組合せが、

```text
1
6
11
```

です。

試験では、**「全部同じチャネル」や「1・2・3のような近接チャネル」ではなく、十分に離したチャネルを使う**と判断します。

## 直感的な説明

無線LANのチャネルは、道路の車線というより、**少し幅のある帯域**と考えると分かりやすいです。

2.4GHz帯では、チャネル番号が1つ違うだけでは、使う周波数帯が大きく重なります。

<figure style="margin:16px 0 20px;">
  <picture>
    <source media="(max-width: 640px)" srcset="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/fe/wireless-lan-channel-interference-mobile.png" width="1086" height="1448">
    <img src="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/fe/wireless-lan-channel-interference.png" width="1200" height="630" alt="2.4GHz帯の無線LANで、チャネル1・2・3の重なりと、1・6・11の非重複配置を比較した図" loading="lazy" decoding="async" style="display:block;width:100%;max-width:100%;height:auto;">
  </picture>
  <figcaption style="font-size:0.88em;line-height:1.5;color:#666;margin-top:8px;">近いチャネルは周波数帯が重なりやすい。1・6・11は代表的な非重複の組合せです。</figcaption>
</figure>

このように近いチャネルを、電波が届く範囲のアクセスポイント同士で使うと、互いに影響しやすくなります。

そこで、代表的には、

```text
AP1 → ch1
AP2 → ch6
AP3 → ch11
```

のように、離れたチャネルを割り当てます。

Ciscoの公式資料でも、2.4GHz帯で隣接APに使う代表的な非重複チャネルとして **1・6・11** が示されています。

### 触って覚える：3台のAPのチャネルを変えてみる

**見るポイント：** チャネル番号を変えると、周波数の帯域の重なりがどう変わるでしょうか。まずは **1・2・3** と **1・6・11** を比較しましょう。

1. 組合せを選ぶか、AP1～AP3のチャネルを変更します。
2. 帯域が重なるか予想してから「重なりを確認」を押します（予想は省略可）。
3. 1・2・3と1・6・11の結果を比べ、**SSIDを変えるだけでは干渉対策にならない**理由を考えます。

<link rel="stylesheet" href="{{ '/assets/css/fe-wireless-channel-demo.css' | relative_url }}">

<div id="fe-channel-demo" class="fe-channel-demo" aria-label="2.4GHz帯の無線LANチャネル重なりを調べる操作教材">
  <div class="fe-channel-demo__controls">
    <label for="fe-channel-preset">① チャネルの組合せ
      <select id="fe-channel-preset" data-preset>
        <option value="near">1・2・3（近接チャネル）</option>
        <option value="separate">1・6・11（代表的な非重複例）</option>
        <option value="custom" disabled>個別に設定中</option>
      </select>
    </label>
  </div>
  <div class="fe-channel-demo__controls">
    <label for="fe-channel-ap1">AP1
      <select id="fe-channel-ap1" data-channel>
        <option value="1">ch1</option><option value="2">ch2</option><option value="3">ch3</option><option value="4">ch4</option><option value="5">ch5</option><option value="6">ch6</option><option value="7">ch7</option><option value="8">ch8</option><option value="9">ch9</option><option value="10">ch10</option><option value="11">ch11</option>
      </select>
    </label>
    <label for="fe-channel-ap2">AP2
      <select id="fe-channel-ap2" data-channel>
        <option value="1">ch1</option><option value="2" selected>ch2</option><option value="3">ch3</option><option value="4">ch4</option><option value="5">ch5</option><option value="6">ch6</option><option value="7">ch7</option><option value="8">ch8</option><option value="9">ch9</option><option value="10">ch10</option><option value="11">ch11</option>
      </select>
    </label>
    <label for="fe-channel-ap3">AP3
      <select id="fe-channel-ap3" data-channel>
        <option value="1">ch1</option><option value="2">ch2</option><option value="3" selected>ch3</option><option value="4">ch4</option><option value="5">ch5</option><option value="6">ch6</option><option value="7">ch7</option><option value="8">ch8</option><option value="9">ch9</option><option value="10">ch10</option><option value="11">ch11</option>
      </select>
    </label>
  </div>
  <div class="fe-channel-demo__spectrum" aria-label="APごとの使用周波数帯の模式図">
    <p><strong>2.4GHz帯のチャネル配置（模式図）</strong></p>
    <div class="fe-channel-demo__row"><strong>AP1</strong><div class="fe-channel-demo__track"><span class="fe-channel-demo__band" data-band>ch1</span></div><span data-center>2412 MHz</span></div>
    <div class="fe-channel-demo__row"><strong>AP2</strong><div class="fe-channel-demo__track"><span class="fe-channel-demo__band" data-band>ch2</span></div><span data-center>2417 MHz</span></div>
    <div class="fe-channel-demo__row"><strong>AP3</strong><div class="fe-channel-demo__track"><span class="fe-channel-demo__band" data-band>ch3</span></div><span data-center>2422 MHz</span></div>
    <div class="fe-channel-demo__axis"><span>2400 MHz付近</span><span>2480 MHz付近</span></div>
  </div>
  <div class="fe-channel-demo__controls">
    <label for="fe-channel-prediction">② 帯域が重なる組合せはある？（任意）
      <select id="fe-channel-prediction" data-prediction>
        <option value="">予想しないで進む</option>
        <option value="yes">ある</option>
        <option value="no">ない</option>
      </select>
    </label>
  </div>
  <div class="fe-channel-demo__controls">
    <button type="button" data-check>③ 重なりを確認</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <div class="fe-channel-demo__result">
    <p><strong data-overlap>判定前</strong></p>
    <p data-explanation>予想を選ぶか、そのまま「重なりを確認」を押してください。</p>
    <p role="status" aria-live="polite" aria-atomic="true" data-feedback>チャネル番号が近いほど、使う周波数帯が重なりやすくなります。</p>
  </div>
</div>
<noscript>
  <p>JavaScriptが無効でも比較できます。2.4GHz帯の代表的な例では、ch1・ch2・ch3は周波数帯が互いに重なります。一方、ch1・ch6・ch11は帯域を分けやすい組合せです。SSIDが同じでも異なっていても、チャネルの重なり方自体は変わりません。</p>
</noscript>
<script src="{{ '/assets/js/fe-wireless-channel-demo.js' | relative_url }}" defer></script>

この教材は、2.4GHz帯の**20MHz級チャネルを幅約22MHzの横棒**として描いた、重なりの仕組みを学ぶ模式図です。重なりの判定は中心周波数の間隔で単純化しています。信号の形状、電波強度、周辺APとの距離、送信出力、規格差などを再現した実測・設計用ツールではありません。実際の干渉の程度や通信速度は、この図だけでは決まりません。

## 定義・仕組み

### チャネルとは

無線LANでは、同じ2.4GHz帯の中でも、少しずつ中心周波数をずらした複数のチャネルを使います。

2.4GHz帯では、チャネル番号が近いほど使用する周波数帯が重なりやすくなります。

そのため、

```text
ch1 と ch2
ch6 と ch7
```

のような組合せは、近接するアクセスポイント同士では干渉しやすいです。

### 1・6・11がよく使われる理由

CiscoのWireless RF Reference Guideでは、2.4GHz帯について、**1・6・11が代表的な非重複チャネル**として示されています。

```text
ch1
      ch6
            ch11
```

このように離すことで、近接AP同士のチャネル重複を避けやすくなります。

ただし、

> どの国・地域でも必ず1・6・11だけを使う

という意味ではありません。

利用できるチャネルは国・地域の電波規制や機器の設定によって異なります。

FE試験では、**2.4GHz帯で干渉を避ける代表例として1・6・11を使う**と理解しておけば十分です。

### 同じチャネルにそろえる必要はない

複数のアクセスポイントで同じSSIDを使っていても、チャネルまで同じにする必要はありません。

```text
SSID：Office-WiFi

AP1 → ch1
AP2 → ch6
AP3 → ch11
```

のように、同じネットワーク名を使いながら、APごとに異なるチャネルを設定できます。

ここは試験でよく混同されるポイントです。

## SSID・BSSID・チャネルの違い

| 項目 | 役割 |
|---|---|
| SSID | 無線LANネットワークの名前 |
| BSSID | 個々のAP側を識別する値 |
| チャネル | 無線通信で使う周波数帯の区分 |

試験中は、

```text
どのWi-Fiか
→ SSID

どのAPか
→ BSSID

どの周波数帯を使うか
→ チャネル
```

と分けて考えます。

SSIDについては、[SSIDとは？BSSID・MACアドレスとの違い](/fe/ssid-bssid/)で整理しています。

## ローミングとの関係

端末が移動して、接続先を別のアクセスポイントへ切り替えることをローミングといいます。

例えば、

```text
AP1
SSID：Office-WiFi
ch1

↓ 移動

AP2
SSID：Office-WiFi
ch6
```

のように、チャネルが異なっていてもローミングできます。

そのため、

```text
ローミングする
→ 全APを同じチャネルにする
```

という考え方は誤りです。

重要なのは、**SSIDとチャネルは別の設定項目**だということです。

## 1次情報・公式資料

2.4GHz帯のチャネル配置や1・6・11の扱いは、Ciscoの公式無線LAN資料で確認できます。

- [Cisco：Wireless RF Reference Guide](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/technical-reference/wireless-rf-reference-guide.html)
- [Cisco：RF Channels on a Cisco Business Wireless Network](https://www.cisco.com/c/en/us/support/docs/smb/wireless/CB-Wireless-Mesh/2069-tz-Changing-RF-Channels.html)
- [Cisco：Wireless LAN Configuration Guide - Configuring Radio Settings](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/wlan/configuration/15-mt/wl-15-mt-book/wl-cfg-radio-set.html)
- [IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)

Ciscoの公式資料では、2.4GHz帯で近隣APに割り当てる非重複チャネルとして、**1・6・11**が説明されています。

## 科目Aでどう出る？

科目Aでは、複数のアクセスポイントを配置するときのチャネル設計として問われます。

### まず「干渉を避けたいか」を見る

```text
複数AP
＋
2.4GHz
＋
通信範囲が重なる
↓
離れたチャネルを使う
```

### 選択肢を切る判断表

| 問題文の表現 | 判断 |
|---|---|
| 全APを同じチャネルにする | 疑う |
| 近接APに1・6・11など離れたチャネルを割り当てる | 適切 |
| SSIDを変えれば電波干渉しない | 誤り |
| 1・2・3のように近いチャネルを順に割り当てる | 疑う |
| 同じSSIDでもAPごとにチャネルを変える | 可能 |

試験では、次の3つを別々に考えるのがポイントです。

```text
SSID
→ ネットワーク名

チャネル
→ 周波数

ローミング
→ 接続APの切替え
```

## どんな場面で使う？

### オフィス

フロア内に複数のアクセスポイントを置く場合、互いの電波範囲が重なることがあります。

その場合は、近接するAP同士で同じ・近いチャネルを避けます。

### 店舗・学校・施設

広い建物を複数APでカバーする場合も同じです。

```text
AP1 → ch1
AP2 → ch6
AP3 → ch11
AP4 → ch1
```

のように、距離が十分離れたAPでは同じチャネルを再利用することもあります。

実際の設計では、周囲の無線LAN、AP間距離、送信出力、壁などの条件も考慮します。

## よくある誤解・混同

### ローミングのために全APを同じチャネルにする？

必要ありません。

```text
同じSSID
＋
異なるチャネル
→ ローミング可能
```

チャネルを同じにすると、近接AP同士で干渉しやすくなります。

### SSIDが違えば干渉しない？

違います。

SSIDはネットワークを識別する名前です。

電波干渉は、**使っている周波数帯やチャネル**によって起こります。

```text
SSIDが違う
≠
電波が干渉しない
```

### 1・2・3なら番号が違うので干渉しない？

違います。

2.4GHz帯では、番号が近いチャネル同士は周波数帯が重なります。

```text
1・2・3
→ 近すぎる
→ 干渉しやすい

1・6・11
→ 十分に離す代表例
```

### 1・6・11は世界共通の絶対ルール？

そうではありません。

利用できるチャネルや最適な設計は、国・地域、規格、チャネル幅、周囲の電波環境によって変わります。

FE対策では、

> **2.4GHz帯で干渉を避ける代表的なチャネル設計が1・6・11**

と理解しておくのが安全です。

### 5GHz帯も1・6・11を使う？

違います。

1・6・11は、2.4GHz帯の代表的なチャネル設計です。

5GHz帯では、利用するチャネル番号やチャネル配置が異なります。

## まとめ（試験直前用）

- 2.4GHz帯では、近いチャネル同士は周波数が重なりやすい
- 近接APでは、**離れたチャネルを使う**
- **1・6・11**は代表的な非重複チャネルの組合せ
- SSIDはネットワーク名、チャネルは周波数の区分
- 同じSSIDでも異なるチャネルを使える
- ローミングのために全APを同じチャネルへそろえる必要はない
- SSIDが違っても、近いチャネルを使えば電波干渉は起こり得る
- 1・2・3のような近接チャネル割当ては避ける

```text
SSID
→ 名前

チャネル
→ 周波数

干渉対策
→ チャネルを離す

2.4GHzの代表例
→ 1・6・11
```

{% include fe_article_footer.html %}
