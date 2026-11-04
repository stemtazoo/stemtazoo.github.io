---
layout: page
title: サーバ仮想化とは？ホスト型・ハイパーバイザ型・コンテナ型の違い【基本情報技術者試験】
description: サーバ仮想化の3方式をホストOS・ゲストOS・ハイパーバイザ・カーネル共有の有無で比較。構造を切り替える操作教材でFE科目Aの判断ポイントを学びます。
permalink: /fe/server-virtualization/
tags: [fe, fe-technology, computer-system, virtualization]
fe_section: テクノロジ系
fe_subsection: システム構成要素
fe_order: 75
date: 2026-11-04
last_modified_at: 2026-11-04
related_articles:
  - /fe/live-migration-virtual-server/
  - /fe/scale-up-vs-scale-out/
  - /fe/saas-paas-iaas/
---

## まず結論

**サーバ仮想化**とは、物理サーバのCPU・メモリなどをソフトウェアで分け、複数の独立した実行環境を利用できるようにする技術です。

基本情報技術者試験（FE）の科目Aでは、**ホストOSの上に仮想化ソフトがあるか、物理サーバ上にハイパーバイザがあるか、ホストOSのカーネルを共有するか**で3方式を区別します。

| 方式 | 構造上の目印 | 各環境にゲストOSは必要？ |
|---|---|---|
| ホスト型 | 物理サーバ → ホストOS → 仮想化ソフト → 仮想マシン | 必要 |
| ハイパーバイザ型（ベアメタル型） | 物理サーバ → ハイパーバイザ → 仮想マシン | 必要 |
| コンテナ型 | 物理サーバ → ホストOS → コンテナ基盤 → コンテナ | 原則不要（ホストのカーネルを共有） |

## 直感的な説明

1台の物理サーバを**大きな建物**に例えます。

- **ホスト型**は、すでにある建物の管理設備（ホストOS）に、別の部屋を作る仕組み（仮想化ソフト）を追加します。
- **ハイパーバイザ型**は、物理サーバ上で直接、仮想マシンへの資源の割当てを管理します。
- **コンテナ型**は、建物の共通設備（ホストOSのカーネル）を共有しながら、アプリケーションの実行環境を分離します。

**「仮想化＝必ずゲストOSを一つずつ起動する」ではありません。** コンテナ型は、通常はホストOSのカーネルを共有します。

## 定義・仕組み

### ホスト型：ホストOSの上で仮想化

物理サーバにWindowsやLinuxなどの**ホストOS**を動かし、その上に仮想化ソフトを導入します。仮想マシン（VM）にはそれぞれ**ゲストOS**を動かせます。既存PC上で試しやすい一方、ホストOSを介する分の管理や資源が必要です。

```text
アプリ        アプリ
ゲストOS      ゲストOS
└ 仮想マシン ┘
  仮想化ソフト
    ホストOS
    物理サーバ
```

### ハイパーバイザ型：物理サーバ上で直接管理

**ベアメタル型（タイプ1）**のハイパーバイザは、物理サーバ上で仮想マシンを管理します。各仮想マシンはゲストOSとアプリケーションを持ちます。一般的なホスト型のような、独立した汎用ホストOSを仮想化ソフトの下に置く構造ではありません。

```text
アプリ        アプリ
ゲストOS      ゲストOS
└ 仮想マシン ┘
  ハイパーバイザ
    物理サーバ
```

管理用のOSや専用の管理領域を持つ製品もあります。「ハイパーバイザ型ならOSという文字が一切登場しない」という意味ではなく、**ゲストOSを動かす位置関係**を押さえます。

### コンテナ型：ホストOSのカーネルを共有

**コンテナ**はアプリケーションと、その実行に必要なライブラリなどを隔離された環境で動かします。通常、コンテナごとに完全なゲストOSを起動せず、**ホストOSのカーネルを共有**します。

```text
アプリA       アプリB
└ コンテナ   ┘
  コンテナ実行基盤
  ホストOSのカーネル
    物理サーバ
```

このため仮想マシンより軽量に起動・配置できることが多い一方、カーネルの共有という制約があります。なお、Windows上でLinuxコンテナを使うときなど、**内部でLinux仮想マシンを動かす実装**もあります。科目Aではまず基本的な構造を理解しましょう。

### 触って覚える：3方式の積み重なりを比較

次の教材では「方式を選ぶ → ゲストOSが必要か予想する → 構造を見る」を繰り返します。**表示される層の順番と、ゲストOSの有無**を見比べてください。

<link rel="stylesheet" href="{{ '/assets/css/fe-server-virtualization-visualizer.css' | relative_url }}">

<div id="fe-server-virtualization-demo" class="fe-server-virtualization-demo">
  <p class="fe-server-virtualization-demo__step"><strong>① 方式を選ぶ</strong></p>
  <div class="fe-server-virtualization-demo__modes" role="group" aria-label="仮想化方式">
    <button type="button" data-mode="host" aria-pressed="true">ホスト型</button>
    <button type="button" data-mode="hypervisor" aria-pressed="false">ハイパーバイザ型</button>
    <button type="button" data-mode="container" aria-pressed="false">コンテナ型</button>
  </div>
  <p class="fe-server-virtualization-demo__step"><strong>② 予想する</strong>：この方式で、各実行環境にゲストOSが必要でしょうか？</p>
  <fieldset class="fe-server-virtualization-demo__prediction">
    <legend>ゲストOSについての予想</legend>
    <label><input type="radio" name="fe-virtualization-guess" value="yes"> 必要</label>
    <label><input type="radio" name="fe-virtualization-guess" value="no"> 原則不要</label>
  </fieldset>
  <p class="fe-server-virtualization-demo__step"><strong>③ 構造を表示する</strong></p>
  <div class="fe-server-virtualization-demo__actions">
    <button type="button" data-reveal>構造と理由を見る</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <div class="fe-server-virtualization-demo__result" data-result hidden>
    <p class="fe-server-virtualization-demo__feedback" data-feedback role="status" aria-live="polite"></p>
    <div class="fe-server-virtualization-demo__layers" data-layers aria-label="仮想化方式の積層構造"></div>
    <p data-explanation></p>
  </div>
  <p class="fe-server-virtualization-demo__note">上から「アプリケーション側」→「物理サーバ側」の順に表示します。これは基本構造を学ぶ概念図で、製品ごとの管理用OS・実装差は省略しています。予想しなくても表示できます。</p>
</div>
<noscript><p>JavaScriptを使わない場合も、直前の3つの構造図で比較できます。ホスト型はホストOSの上に仮想化ソフト、ハイパーバイザ型は物理サーバ上にハイパーバイザ、コンテナ型はホストOSのカーネルを共有する点が違います。</p></noscript>
<script src="{{ '/assets/js/fe-server-virtualization-visualizer.js' | relative_url }}" defer></script>

## 科目Aでどう出る？

| 選択肢に出る表現 | 判断 |
|---|---|
| ホストOS上に仮想化ソフトを導入する | ホスト型 |
| 物理サーバ上で直接ハイパーバイザが仮想マシンを管理する | ハイパーバイザ型 |
| ホストOSのカーネルを複数の実行環境で共有する | コンテナ型 |
| 稼働中の仮想マシンを別の物理サーバへ移動する | ライブマイグレーション |
| CPUやメモリを増強して1台を高性能化する | スケールアップ |
| サーバ台数を増やして処理能力を拡張する | スケールアウト |

### 確認問題

次のうち、一般的な**コンテナ型**の特徴として最も適切なのはどれでしょうか。

- ア：実行環境ごとに独立したゲストOSのカーネルを必ず起動する。
- イ：ホストOSのカーネルを共有してアプリケーションの実行環境を分離する。
- ウ：稼働中の仮想マシンを物理サーバ間で無停止に近い形で移す。

<details markdown="1">
<summary>正解と解説を見る（タップして開く）</summary>

**正解：イ。** 一般的なコンテナ型はホストOSのカーネルを共有し、アプリケーションを分離して動かします。

- ア：ゲストOSのカーネルをそれぞれ起動するのは仮想マシン型のイメージです。
- イ：コンテナ型の基本的な特徴です。
- ウ：ライブマイグレーションの説明であり、仮想化方式の分類とは別です。

</details>

## どんな場面で使う？

ホスト型は学習環境や開発用PCで仮想マシンを試す場面、ハイパーバイザ型は物理サーバに複数の仮想サーバを集約する場面、コンテナ型はアプリケーションを軽量に配布・起動する場面などで使われます。

サーバを仮想化すれば必ずクラウドになるわけではありません。自社設備でも仮想化は利用できます。また、仮想化したサーバを別ホストに移す運用技術は[ライブマイグレーション](/fe/live-migration-virtual-server/)で、処理能力の拡張方法は[スケールアップとスケールアウト](/fe/scale-up-vs-scale-out/)で詳しく扱います。

## よくある誤解・混同

### 「コンテナはOSなしで動く」？

違います。**ゲストOSを丸ごと起動しない**のであって、ホストOSのカーネルなどの機能は必要です。コンテナと仮想マシンは同じものではありません。

### 「ハイパーバイザ型にはゲストOSがない」？

違います。ハイパーバイザ型でも**仮想マシンごとにゲストOS**を動かします。一般的なホスト型との違いは、**仮想化基盤が物理サーバにどう配置されているか**です。

### 「仮想化したら自動的に処理能力が上がる」？

仮想化は主に資源の分割・集約・柔軟な運用に役立ちます。物理サーバのCPUやメモリが無制限に増えるわけではありません。性能向上には、負荷や構成に応じた資源設計が必要です。

## まとめ（試験直前用）

- サーバ仮想化は、物理資源を使って複数の独立した実行環境を作る技術。
- **ホスト型**：ホストOSの上に仮想化ソフト、その上にゲストOS。
- **ハイパーバイザ型**：物理サーバ上で直接VMを管理、VMにはゲストOS。
- **コンテナ型**：ホストOSのカーネルを共有し、原則としてコンテナごとのゲストOSは不要。
- **移動＝ライブマイグレーション、性能拡張＝スケールアップ／アウト**と区別する。

> **ホストOSを介すか、ハイパーバイザが直接管理するか、カーネルを共有するか。**

{% include fe_article_footer.html %}
