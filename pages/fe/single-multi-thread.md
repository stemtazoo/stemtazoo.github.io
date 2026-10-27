---
layout: page
title: シングルスレッドとマルチスレッドの違い｜並行・並列処理を操作して理解【基本情報技術者試験】
description: スレッドの意味とDBMSでマルチスレッドを利用する理由を、並行処理・並列処理との違い、操作できるタイムライン、選択肢を切る判断基準から学びます。
permalink: /fe/single-multi-thread/
tags: [fe, fe-technology, operating-system]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 182
date: 2026-10-27
last_modified_at: 2026-10-27
---

## まず結論

**マルチスレッドは、1つのプロセスの中に複数の実行の流れを設ける仕組み**です。DBMSやWebサーバでは、複数の利用者からの要求を並行して扱うために利用されます。

試験では、次の3点を押さえます。

- **スレッド**はプロセス内の実行単位。通常、同じプロセスのメモリ空間を共有する。
- **並行**は複数の処理を進行させること、**並列**は同じ時点で複数の処理を実行すること。
- **シングルスレッドでも並行処理は可能**。非同期I/Oなどの方法があるため、「絶対にできない」という断定に注意する。

## 直感的な説明

DBMSに3人から同時に検索要求が届く場面を考えます。

~~~text
利用者A ─┐
利用者B ─┼─→ DBMS
利用者C ─┘
~~~

要求ごとにスレッドを割り当てれば、ある要求が入出力を待つ間に、別の要求を進められます。ただし、スレッドの生成や切替えにもコストがあり、必ず高速化するわけではありません。

## 定義・仕組み

| 用語 | 意味 |
|---|---|
| プロセス | 実行中のプログラムを管理する単位 |
| スレッド | プロセス内で命令を実行する流れ |
| シングルスレッド | 1つのプロセスに実行の流れが1本 |
| マルチスレッド | 1つのプロセスに複数の実行の流れがある |
| 並行処理 | 複数の処理を切り替えたり待ち時間を利用したりして進める |
| 並列処理 | 複数の処理を同じ時点で実際に実行する |

スレッドは同じプロセスのアドレス空間を共有するため、情報を受け渡しやすい一方、共有データの更新には排他制御や同期が必要になる場合があります。

**シングルスレッド＝必ず逐次処理**ではありません。1本のスレッドでも、非同期I/Oとイベントループを使って複数の要求を並行して進められます。一方、複数コアでCPU処理を同時実行するには、複数の実行単位が必要です。

## 実際に触ってみる

3つの独立したCPU処理が、それぞれ3秒かかると仮定したモデルです。実行方法を選ぶとタイムラインが切り替わります。

<div id="fe-thread-demo" style="border:1px solid #cbd5e1;border-radius:12px;padding:1rem;max-width:680px;margin:1rem auto">
  <label for="fe-thread-mode"><strong>実行方法を切り替える</strong></label>
  <select id="fe-thread-mode" style="display:block;width:100%;margin:.7rem 0 1rem;padding:.6rem;border:1px solid #94a3b8;border-radius:8px;background:var(--color-canvas-default,#fff);color:inherit">
    <option value="sequential">逐次実行（1つずつ）</option>
    <option value="concurrent">並行実行（1コアで切替）</option>
    <option value="parallel">並列実行（3コアで同時）</option>
  </select>
  <div id="fe-thread-chart" role="img" aria-label="処理A、B、Cの実行時間を示す図"></div>
  <p><strong>完了時間：<span id="fe-thread-total">9秒</span></strong></p>
  <p id="fe-thread-note">3つの処理を順番に実行します。</p>
  <noscript>JavaScriptが無効な場合は下の比較表で確認してください。</noscript>
</div>

<script>
(function () {
  var root = document.getElementById('fe-thread-demo');
  if (!root) return;
  var select = root.querySelector('#fe-thread-mode');
  var chart = root.querySelector('#fe-thread-chart');
  var total = root.querySelector('#fe-thread-total');
  var note = root.querySelector('#fe-thread-note');
  var colors = ['#547fa6','#478d7d','#9175aa'];
  function render() {
    var mode = select.value, parts = [];
    for (var j=0;j<3;j++) parts.push([]);
    if (mode==='sequential') {
      for (var i=0;i<3;i++) parts[i].push([i*3,(i+1)*3]);
    } else if (mode==='concurrent') {
      for (var t=0;t<9;t++) parts[t%3].push([t,t+1]);
    } else {
      for (var k=0;k<3;k++) parts[k].push([0,3]);
    }
    var rows = parts.map(function (segments,idx) {
      var bars=segments.map(function (s) {
        return '<rect x="'+(48+s[0]*29)+'" y="'+(12+idx*34)+'" width="'+((s[1]-s[0])*29-2)+'" height="22" rx="3" fill="'+colors[idx]+'"/>';
      }).join('');
      return '<text x="2" y="'+(28+idx*34)+'" fill="currentColor" font-size="12">処理'+('ABC'[idx])+'</text>'+bars;
    }).join('');
    var ticks=[0,3,6,9].map(function(t){return '<text x="'+(48+t*29)+'" y="133" text-anchor="middle" fill="currentColor" font-size="11">'+t+'秒</text>';}).join('');
    chart.innerHTML='<svg viewBox="0 0 320 145" width="100%" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'+rows+ticks+'</svg>';
    total.textContent=mode==='parallel'?'3秒':'9秒';
    note.textContent=mode==='parallel'?'3コアで同時に実行する理想例です。':mode==='concurrent'?'1コアで処理を切り替えます。CPU処理だけなら仕事の総量は変わりません。':'3つの処理を順番に実行します。';
  }
  select.addEventListener('change',render); render();
})();
</script>

| 実行方法 | この例の完了時間 | ポイント |
|---|---:|---|
| 逐次 | 9秒 | 順番に実行 |
| 1コアで並行 | 9秒 | 切替えながら実行 |
| 3コアで並列 | 3秒 | 独立した処理を同時実行 |

※CPU処理だけを仮定し、切替え・同期のオーバーヘッドを無視した理想化モデルです。実際のDBMSはI/O待ちもあるため、並行処理によって待ち時間を有効利用できる場合があります。

## 科目Aでどう出る？

平成18年春期 問62では、スレッド単位で処理できるDBMSについて適切な説明を選びます。

| 選択肢の要旨 | 判定 | 理由 |
|---|---|---|
| ア：シングルスレッドでは並行処理できない | × | 非同期I/Oなどを使えば可能 |
| イ：複数クライアントの要求を効率よく処理するためマルチスレッドを使う | ○ | 待ち時間を利用して別の要求を進められる |
| ウ：マルチスレッドは同期負荷が大きく並列処理に不向き | × | 同期は必要な場合があるが、並列処理にも利用できる |
| エ：マルチプロセッサではシングルスレッドの方が効率的 | × | 複数スレッドで複数コアを利用できる場合がある |

**正解はイ**です。「並行処理はできない」「必ず効率が良い」のような強い断定に注意します。

## どんな場面で使う？

- DBMS：複数利用者の要求を処理する
- Webサーバ：通信や入出力の待ち時間を有効利用する
- Python：I/O待ちの多い処理では `threading`、CPU負荷の高い処理では実行環境に応じて `multiprocessing` などを検討する

## よくある誤解・混同

**「シングルスレッドなら並行処理できない」**は誤りです。非同期I/Oなどで複数の仕事を進められます。

**「マルチスレッドなら必ず高速」**も誤りです。同期・競合・切替えのコストがあるため、処理内容によっては遅くなります。

**「並行と並列は同じ」**も誤りです。並行は複数の処理が進行すること、並列は同じ時点で複数の処理を実行することです。

## まとめ（試験直前用）

- **複数の要求を効率よく処理** → マルチスレッドが候補
- **1コアで切替え** → 並行処理はできるが、同時実行とは限らない
- **共有メモリ・複数スレッド** → 同期や排他制御に注意

関連：[マルチコアプロセッサ](/fe/multicore-processor/) ／ [マルチプロセッサシステム](/fe/multiprocessor-system-types/)

{% include fe_article_footer.html %}
