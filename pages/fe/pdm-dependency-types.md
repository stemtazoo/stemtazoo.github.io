---
layout: page
title: PDMとは？FS・SS・FF・SFの依存関係を見分ける方法【基本情報技術者試験】
description: プレシデンスダイアグラム法（PDM）の4つの依存関係であるFS・SS・FF・SFを、「先行作業の開始/終了」と「後続作業の開始/終了」の組合せとして、FE試験で迷わない判断基準とともに解説します。
permalink: /fe/pdm-dependency-types/
tags: [fe, fe-management, project-management]
fe_section: マネジメント系
fe_subsection: プロジェクトマネジメント
fe_order: 25
date: 2026-08-28
last_modified_at: 2026-11-28
image:
  path: https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/fe/pdm-dependency-types.png
  width: 1200
  height: 630
  alt: "PDMのFS・SS・FF・SFの4種類の依存関係を、先行作業と後続作業の開始・終了の対応で比較した図"
---

## まず結論

PDM（Precedence Diagramming Method：プレシデンスダイアグラム法）では、作業同士の依存関係を次の4種類で表します。

| 記号 | 依存関係 |
|:---:|---|
| **FS** | **終了 → 開始**<br><small>Finish to Start</small> |
| **SS** | **開始 → 開始**<br><small>Start to Start</small> |
| **FF** | **終了 → 終了**<br><small>Finish to Finish</small> |
| **SF** | **開始 → 終了**<br><small>Start to Finish</small> |

表の矢印は、**先行作業の開始・終了 → 後続作業の開始・終了**を表します。時間の前倒しを指定しない場合、SSでは先行作業の開始以降に後続作業を開始し、FFでは先行作業の終了以降に後続作業を終了します。

<figure style="margin:16px 0 20px;">
  <picture>
    <source media="(max-width: 640px)" srcset="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/fe/pdm-dependency-types-mobile.png" width="1024" height="1536">
    <img src="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/fe/pdm-dependency-types.png" width="1200" height="630" alt="PDMの4つの依存関係。FSは先行作業の終了から後続作業の開始、SSは開始から開始、FFは終了から終了、SFは開始から終了につながる。" style="display:block;width:100%;max-width:100%;height:auto;" loading="lazy" decoding="async">
  </picture>
  <figcaption style="font-size:0.88em;line-height:1.5;color:#596579;margin-top:8px;">SS・FFは、どの時点を基準にするかを表します。先行作業と後続作業の時点には間隔があっても構いません。</figcaption>
</figure>

基本情報技術者試験では、時間差の数字より先に、**「何が何の条件になっているか」**を見るのがポイントです。

```text
先行作業のどの時点？
開始 / 終了

        ↓

後続作業のどの時点？
開始 / 終了
```

この2点だけを拾えば、FS・SS・FF・SFを切り分けられます。

## 直感的な説明

PDMの2文字は、**先行作業 → 後続作業**の順に読めば分かりやすくなります。

```text
FS
F = 先行作業のFinish（終了）
S = 後続作業のStart（開始）

→ 先行作業が終わったら、後続作業を始める
```

同じように、

```text
SS → 開始 → 開始
FF → 終了 → 終了
SF → 開始 → 終了
```

です。

### 4種類を「2本の時間軸」で見る

文字だけで混乱するときは、**矢印の出発点と到着点が、開始か終了か**だけを見ます。

<style>
.fe-pdm-diagrams {
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: .75rem;
  margin: 1rem 0;
}
.fe-pdm-panel {
  min-width: 0;
  margin: 0;
  padding: .5rem;
  border: 1px solid #d8dee4;
  border-radius: 10px;
  background: #fff;
  color: #263746;
}
.fe-pdm-panel figcaption {
  color: #263746;
  margin: .2rem .3rem;
  font-size: 1rem;
}
.fe-pdm-panel svg {
  display: block;
  width: 100%;
  max-width: 420px;
  height: auto;
  margin: 0 auto;
}
@media(max-width: 760px) {
  .fe-pdm-diagrams { grid-template-columns: minmax(0,1fr); }
}
</style>

<div class="fe-pdm-diagrams">
  <figure class="fe-pdm-panel">
    <figcaption><strong>FS：終了 → 開始</strong></figcaption>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 126" width="300" height="126" role="img" aria-labelledby="pdm-FS-title pdm-FS-desc">
      <title id="pdm-FS-title">FS：終了から開始への依存関係</title>
      <desc id="pdm-FS-desc">先行作業Aの終了端から後続作業Bの開始端へ矢印がつながる。時間差ゼロで条件を満たす配置例。</desc>
      <g fill="#263746" font-size="14">
        <text x="6" y="38">先行A</text><text x="6" y="96">後続B</text>
      </g>
      <rect x="82" y="20" width="112" height="24" rx="3" fill="#739ec9" stroke="#527ba5"/>
      <rect x="194" y="78" width="92" height="24" rx="3" fill="#71ad95" stroke="#4c806d"/>
      <g stroke="#a65308" stroke-width="2" fill="none" stroke-linejoin="round">
        <path d="M194 32 V90 M190 83 L194 90 L198 83"/>
      </g>
      <circle cx="194" cy="32" r="3.5" fill="#a65308"/>
      <g fill="#713e12" font-size="13" text-anchor="end">
        <text x="182" y="59">終了（F）</text>
        <text x="182" y="75">開始（S）</text>
      </g>
      <g stroke="#64748b" stroke-width="1.2" fill="none"><path d="M82 116 H286 M281 113 L286 116 L281 119"/></g>
      <text x="6" y="120" fill="#475569" font-size="12">時間</text>
    </svg>
  </figure>
  <figure class="fe-pdm-panel">
    <figcaption><strong>SS：開始 → 開始</strong></figcaption>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 126" width="300" height="126" role="img" aria-labelledby="pdm-SS-title pdm-SS-desc">
      <title id="pdm-SS-title">SS：開始から開始への依存関係</title>
      <desc id="pdm-SS-desc">先行作業Aの開始端から後続作業Bの開始端へ矢印がつながる。時間差ゼロで条件を満たす配置例。</desc>
      <g fill="#263746" font-size="14">
        <text x="6" y="38">先行A</text><text x="6" y="96">後続B</text>
      </g>
      <rect x="82" y="20" width="124" height="24" rx="3" fill="#739ec9" stroke="#527ba5"/>
      <rect x="82" y="78" width="92" height="24" rx="3" fill="#71ad95" stroke="#4c806d"/>
      <g stroke="#a65308" stroke-width="2" fill="none" stroke-linejoin="round">
        <path d="M82 32 V90 M78 83 L82 90 L86 83"/>
      </g>
      <circle cx="82" cy="32" r="3.5" fill="#a65308"/>
      <g fill="#713e12" font-size="13" text-anchor="start">
        <text x="94" y="59">開始（S）</text>
        <text x="94" y="75">開始（S）</text>
      </g>
      <g stroke="#64748b" stroke-width="1.2" fill="none"><path d="M82 116 H286 M281 113 L286 116 L281 119"/></g>
      <text x="6" y="120" fill="#475569" font-size="12">時間</text>
    </svg>
  </figure>
  <figure class="fe-pdm-panel">
    <figcaption><strong>FF：終了 → 終了</strong></figcaption>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 126" width="300" height="126" role="img" aria-labelledby="pdm-FF-title pdm-FF-desc">
      <title id="pdm-FF-title">FF：終了から終了への依存関係</title>
      <desc id="pdm-FF-desc">先行作業Aの終了端から後続作業Bの終了端へ矢印がつながる。時間差ゼロで条件を満たす配置例。</desc>
      <g fill="#263746" font-size="14">
        <text x="6" y="38">先行A</text><text x="6" y="96">後続B</text>
      </g>
      <rect x="82" y="20" width="124" height="24" rx="3" fill="#739ec9" stroke="#527ba5"/>
      <rect x="124" y="78" width="82" height="24" rx="3" fill="#71ad95" stroke="#4c806d"/>
      <g stroke="#a65308" stroke-width="2" fill="none" stroke-linejoin="round">
        <path d="M206 32 V90 M202 83 L206 90 L210 83"/>
      </g>
      <circle cx="206" cy="32" r="3.5" fill="#a65308"/>
      <g fill="#713e12" font-size="13" text-anchor="end">
        <text x="194" y="59">終了（F）</text>
        <text x="194" y="75">終了（F）</text>
      </g>
      <g stroke="#64748b" stroke-width="1.2" fill="none"><path d="M82 116 H286 M281 113 L286 116 L281 119"/></g>
      <text x="6" y="120" fill="#475569" font-size="12">時間</text>
    </svg>
  </figure>
  <figure class="fe-pdm-panel">
    <figcaption><strong>SF：開始 → 終了</strong></figcaption>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 126" width="300" height="126" role="img" aria-labelledby="pdm-SF-title pdm-SF-desc">
      <title id="pdm-SF-title">SF：開始から終了への依存関係</title>
      <desc id="pdm-SF-desc">先行作業Aの開始端から後続作業Bの終了端へ矢印がつながる。時間差ゼロで条件を満たす配置例。</desc>
      <g fill="#263746" font-size="14">
        <text x="6" y="38">先行A</text><text x="6" y="96">後続B</text>
      </g>
      <rect x="174" y="20" width="112" height="24" rx="3" fill="#739ec9" stroke="#527ba5"/>
      <rect x="82" y="78" width="92" height="24" rx="3" fill="#71ad95" stroke="#4c806d"/>
      <g stroke="#a65308" stroke-width="2" fill="none" stroke-linejoin="round">
        <path d="M174 32 V90 M170 83 L174 90 L178 83"/>
      </g>
      <circle cx="174" cy="32" r="3.5" fill="#a65308"/>
      <g fill="#713e12" font-size="13" text-anchor="start">
        <text x="186" y="59">開始（S）</text>
        <text x="186" y="75">終了（F）</text>
      </g>
      <g stroke="#64748b" stroke-width="1.2" fill="none"><path d="M82 116 H286 M281 113 L286 116 L281 119"/></g>
      <text x="6" y="120" fill="#475569" font-size="12">時間</text>
    </svg>
  </figure>
</div>

青は先行作業A、緑は後続作業B、オレンジの矢印は依存関係です。時間は右に進みます。図は時間差ゼロで条件を満たす配置例であり、依存する時点が必ず同時になるという意味ではありません。

図の横棒の長さではなく、**矢印がどの端からどの端へ結ばれているか**を見るのがポイントです。

```text
左端  = Start（開始）
右端  = Finish（終了）
```

したがって、文章でも図でも、

```text
先行作業の［開始 / 終了］
            ↓
後続作業の［開始 / 終了］
```

の2か所だけを拾えば判断できます。

例えば、資格試験の会場運営を考えます。

```text
受付が終わったら試験開始
→ 終了 → 開始
→ FS
```

一方で、

```text
試験を開始して20分後に受付終了
→ 開始 → 終了
→ SF
```

です。

時間差が20分あっても、依存関係そのものは**開始から終了への関係**なのでSFです。

## 定義・仕組み

PDMは、作業をノードで表し、作業同士を矢印で結んで、順序や依存関係を表す方法です。

アローダイアグラムと似ていますが、表現の仕方が異なります。

- PDM：作業をノードで表す
- アローダイアグラム：作業を矢印で表す

アローダイアグラムの基本を先に整理したい場合は、[アローダイアグラムとは？](/fe/arrow-diagram/) を確認すると、作業の前後関係という共通点から理解しやすくなります。

### 4種類の依存関係

#### FS：終了-開始

```text
Aが終了
↓
Bが開始
```

最もイメージしやすい関係です。

例：

```text
設計が終わったら製造を始める
```

#### SS：開始-開始

```text
Aが開始
↓
Bが開始
```

例：

```text
受付開始から30分後に試験を開始する
```

受付の**開始**が試験の**開始**の基準なのでSSです。

#### FF：終了-終了

```text
Aが終了
↓
Bが終了
```

例：

```text
受付終了から45分後に試験を終了する
```

受付の**終了**が試験の**終了**の基準なのでFFです。

#### SF：開始-終了

```text
Aが開始
↓
Bが終了
```

4種類の中では最も直感的に分かりにくい関係です。

例：

```text
試験開始から20分後に受付を終了する
```

試験の**開始**が受付の**終了**の基準なのでSFです。

このテーマは基本情報技術者試験のプロジェクトマネジメント分野と関係します。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

## 科目Aでどう出る？

科目Aでは、文章で示された2つの作業の関係から、FS・SS・FF・SFのどれに当たるかを判断する問題が出ます。

試験中は、文章全体を一度に理解しようとせず、次の順で読みます。

```text
1. 条件を出している作業を探す
2. その作業の「開始」か「終了」かを見る
3. 条件を受ける作業を探す
4. その作業の「開始」か「終了」かを見る
5. 2文字に変換する
```

### 時間差はいったん無視する

例えば、

```text
受付の終了から10分後に試験を開始する
```

と書いてあれば、まず`10分後`を無視します。

残る関係は、

```text
受付の終了
→
試験の開始
```

なので、

```text
F → S
= FS
```

です。

### 4パターンを一気に切り分ける

| 問題文の形 | 変換 | PDM |
|---|---|---|
| Aの終了後にBを開始 | Finish → Start | FS |
| Aの開始後にBを開始 | Start → Start | SS |
| Aの終了後にBを終了 | Finish → Finish | FF |
| Aの開始後にBを終了 | Start → Finish | SF |

試験では、**先行作業の時点が1文字目、後続作業の時点が2文字目**と覚えると安定します。

例えば、

> システム要件定義が完了すれば、システム方式設計を開始できる。

なら、作業名をいったん消して骨組みだけにします。

```text
「完了すれば」 → 「開始できる」
       ↓                ↓
     Finish           Start
       F        →        S
              FS
```

このように、長い文章を**「終了→開始」の2語まで縮める**と迷いにくくなります。

### 迷ったら4マスで決める

| 先行作業 ＼ 後続作業 | 開始（S） | 終了（F） |
|---|:---:|:---:|
| 開始（S） | SS | SF |
| 終了（F） | FS | FF |

まず先行作業が「開始か終了か」で行を選び、次に後続作業が「開始か終了か」で列を選びます。

## どんな場面で使う？

PDMは、プロジェクトの作業順序を整理するときに使います。

単純な「Aが終わったらBを始める」だけでなく、作業を一部並行して進めたい場合にも関係を表現できます。

例えば、

```text
設計をすべて終える前に、準備作業を始めたい
```

といった場合、開始同士の関係や、時間差を含めた関係を設定できます。

プロジェクト全体の所要日数や遅延の影響まで確認したい場合は、[クリティカルパスとは？](/fe/critical-path/) に進むと、依存関係から日程計算へ理解を広げられます。

## よくある誤解・混同

### 1文字目と2文字目を逆に読む

PDMでは、

```text
1文字目 = 先行作業
2文字目 = 後続作業
```

です。

`SF`を「後続作業のStartから先行作業のFinish」と逆向きに読まないようにします。

### 時間差だけを見て判断する

`10分後`、`20分後`、`3日後`などは、依存関係の種類そのものではありません。

まず、

```text
開始か終了か
↓
開始か終了か
```

を決めます。

時間差はその後に確認します。

### FSしかないと思う

アローダイアグラムでは、ある作業の終了を次の作業の開始条件として読む場面が多いため、FSに慣れやすいです。

しかしPDMでは、SS・FF・SFも表現できます。

### SFを「終了-開始」と間違える

`S`はStart、`F`はFinishです。

```text
SF
= Start → Finish
= 開始 → 終了
```

とそのまま読めば混乱しにくくなります。

## まとめ（試験直前用）

- PDMは作業間の依存関係を表す
- 1文字目は先行作業、2文字目は後続作業
- FS = 終了 → 開始
- SS = 開始 → 開始
- FF = 終了 → 終了
- SF = 開始 → 終了
- 「○分後」などの時間差より先に、開始・終了を拾う

```text
終了 → 開始 = FS
開始 → 開始 = SS
終了 → 終了 = FF
開始 → 終了 = SF
```

{% include fe_article_footer.html %}
