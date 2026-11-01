---
layout: page
title: LRUページ置換とは？最後に参照した時刻で置換ページを決める【基本情報技術者試験】
description: LRUのうち仮想記憶のページ置換に焦点を当て、「最後に参照された時刻が最も古いページを置換する」考え方、ページ参照列の追い方、FIFO・LFUとの違いをFE試験向けに解説します。
permalink: /fe/lru-page-replacement/
tags: [fe, fe-technology, computer-system, algorithm]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 290
date: 2026-07-02
last_modified_at: 2026-11-01
related_articles:
  - /fe/paging/
  - /fe/fifo-page-replacement/
  - /fe/lru/
---

## まず結論

LRU（Least Recently Used）は、**最後に参照された時刻が最も古いページを置換対象にする方式**です。

このページでは、LRUの中でも **仮想記憶のページ置換** に絞って説明します。

```text
最後に参照されてから最も長い
→ LRU

ページ枠がいっぱい
→ 最後の参照が最も古いページを追い出す
```

LRUそのものの概要や、キャッシュ置換も含めたFIFO・LFU・NRUとの比較は、[LRU方式とは？FIFO・LFU・NRUとの違い](/fe/lru/)で整理しています。

> **このページは「LRUをページ参照列でどう追うか」に重点を置く記事です。**

LRUの定義やFIFO・LFU・NRUとの横断比較は、[LRU方式とは？](/fe/lru/) を参照してください。

## 直感的な説明

LRUは、机の上の資料整理に似ています。

机の上には、資料を4冊しか置けないとします。

新しい資料を置きたいのに机がいっぱいなら、どれか1冊を片付ける必要があります。

このとき、LRUでは、**一番長い間使っていない資料** を片付けます。

```text
最近使った資料
→ また使うかもしれないので残す

長く使っていない資料
→ 使う可能性が低そうなので追い出す
```

ページ置換でも同じです。

最近参照されたページは、近いうちにまた参照される可能性があると考え、長く参照されていないページを置換対象にします。

判断に使うのは、回数ではなく **最後に参照した時刻** です。

このページでは、**最後に参照した時刻を使うLRU方式**を中心に扱います。読み込まれた順番だけを見るFIFO方式は、[FIFO方式とは？](/fe/fifo-page-replacement/) で整理しています。

## 定義・仕組み

ページ置換とは、主記憶に必要なページがないときに、どのページを主記憶から追い出すかを決める処理です。

仮想記憶では、プログラムが使うページの一部だけを主記憶に置きます。

主記憶のページ枠がいっぱいの状態で、新しいページを読み込む必要があると、どれかのページを追い出さなければなりません。

このとき、どのページを追い出すかを決める方法が、ページ置換アルゴリズムです。

| 用語 | 意味 |
|---|---|
| ページ | 仮想記憶で扱う固定サイズの単位 |
| ページ枠 | 主記憶上でページを入れる場所 |
| ページフォールト | 必要なページが主記憶にない状態 |
| ページ置換 | 主記憶のページを入れ替えること |
| LRU | 最後の参照時刻が最も古いページを置き換える方式 |

LRUでは、ページが参照されるたびに、そのページを「最近使った」として扱います。

ページ枠がいっぱいで新しいページを入れるときは、枠内にあるページのうち、**最後に参照された時刻が最も古いページ** を置き換えます。

例えば、次のような状態を考えます。

| ページ | 最後に参照された時刻 | LRUでの見方 |
|---|---|---|
| A | 10:01 | 比較的新しい |
| B | 09:50 | 最も古いので置換候補 |
| C | 10:05 | 新しい |

この例では、最後に参照された時刻が最も古いBが置換候補になります。

このテーマは、基本情報技術者試験の「コンピュータシステム」や「オペレーティングシステム」と関係する内容です。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

## LFU・FIFOとの違い

LRUは、LFUやFIFOと混同しやすいです。

| 方式 | 見るもの | 判断の合図 |
|---|---|---|
| LRU | 最後に参照した時刻 | 最近いつ使ったか、最後に参照 |
| LFU | 参照頻度 | 単位時間当たりの参照頻度、Least Frequently Used |
| FIFO | 読み込まれた順番 | 最初に入ったページを先に出す |
| 参照回数方式 | 累積の参照回数 | これまで何回使われたか |

LRUとLFUは名前が似ています。

```text
LRU
→ Recently
→ 最近
→ 最後に参照した時刻

LFU
→ Frequently
→ 頻繁
→ 参照頻度
```

FE試験では、**時刻ならLRU、頻度ならLFU** と切ると分かりやすいです。

また、LRUとFIFOも間違えやすいです。

```text
FIFO
→ 先に入ったものを先に出す

LRU
→ 最近使われていないものを出す
```

古くからページ枠にあるページでも、直前に参照されていれば、LRUでは置換対象になりにくいです。

FIFOのページ参照列の追い方は、[FIFO方式とは？先に入ったページを先に置き換える方法]({{ '/fe/fifo-page-replacement/' | relative_url }})で確認できます。

## 科目Aでどう出る？

科目Aでは、LRU方式の説明や、ページ置換アルゴリズムの判断基準として出題されやすいです。

判断するときは、次の表で切ります。

| 問題文の表現 | 選びたい方式 |
|---|---|
| 最後に参照した時刻が最も古いページを置き換える | LRU |
| 最近使われていないページを置き換える | LRU |
| 単位時間当たりの参照頻度が低いページを置き換える | LFU |
| 最初に読み込まれたページを置き換える | FIFO |
| これから最も長く使われないページを置き換える | OPT |
| 累積の参照回数が少ないページを置き換える | 参照回数系の方式 |

似た選択肢は、次のように切ります。

| 選択肢の方向性 | 判断 |
|---|---|
| 最後に参照した時刻 | LRU |
| 最初に参照した時刻 | LRUではない。FIFO系と混同しやすい |
| 単位時間当たりの参照頻度 | LFU |
| 累積の参照回数 | LRUではない。回数を見る方式 |

決め手は、**Recently = 最近** です。

```text
LRU
→ 最近いつ参照したかを見る
→ 最後に参照した時刻
```

## どんな場面で使う？

問題文では、ページ参照列を順に追って、ページ枠の中身を更新する問題でLRUの考え方が役立ちます。

基本手順は次のとおりです。

1. ページ参照列を左から順に見る
2. 参照ページがページ枠にあれば、置換はしない
3. ただし、そのページは「最近使った」として更新する
4. 参照ページがページ枠になければ、ページフォールトになる
5. 空き枠があれば、そのまま入れる
6. 空き枠がなければ、最後の参照が最も古いページを置き換える

例えば、ページ枠が3つで、次の順に参照するとします。

```text
1, 2, 3, 2, 4
```

途中の状態を簡単に追うと、次のようになります。

| 参照 | ページ枠 | 考え方 |
|---|---|---|
| 1 | 1 | 空き枠に入れる |
| 2 | 1, 2 | 空き枠に入れる |
| 3 | 1, 2, 3 | 空き枠に入れる |
| 2 | 1, 2, 3 | 2を最近使った扱いにする |
| 4 | 4, 2, 3 | 最後の参照が最も古い1を置き換える |

ここで、ページ2を参照した後に、ページ2を古いままと考えると間違えます。

LRUでは、**ヒットしたページも参照時刻を更新する** のがポイントです。


### FIFOとLRUを1ステップずつ比較する

ページ枠が3つで、参照順が \`1, 3, 2, 1, 4, 5, 2, 3, 4, 5\` の場合を追います。**空き枠への初回読み込みはページフォールトですが、ページの置換え回数には含めません。**

<div id="fe-page-replacement-demo" class="fe-pr-demo">
  <p class="fe-pr-hint">「次へ」で参照を進めると、2方式の違いを同時に確認できます。</p>
  <div class="fe-pr-sequence" aria-label="ページ参照順"></div>
  <div class="fe-pr-comparison">
    <section class="fe-pr-panel" data-method="fifo">
      <h3>FIFO <small>読み込んだ順</small></h3>
      <div class="fe-pr-frames"></div>
      <p class="fe-pr-count"></p>
      <p class="fe-pr-detail" aria-live="polite"></p>
    </section>
    <section class="fe-pr-panel" data-method="lru">
      <h3>LRU <small>最後に参照した順</small></h3>
      <div class="fe-pr-frames"></div>
      <p class="fe-pr-count"></p>
      <p class="fe-pr-detail" aria-live="polite"></p>
    </section>
  </div>
  <p class="fe-pr-status" role="status" aria-live="polite">開始前：3つのページ枠は空です。</p>
  <div class="fe-pr-controls">
    <button type="button" data-action="prev" disabled>戻る</button>
    <button type="button" data-action="next">次へ</button>
    <button type="button" data-action="reset">最初から</button>
  </div>
  <p class="fe-pr-hint">確認ポイント：4番目の「1」は置換えなし。FIFOは読み込み順を変えず、LRUは「1」を最近使った扱いに更新します。</p>
</div>

<style>
.fe-pr-demo{border:1px solid #b9c8d2;border-radius:12px;padding:1rem;margin:1.2rem 0;color:#253541;background:#f9fbfc}
.fe-pr-hint{font-size:.88rem;line-height:1.65;color:#536574}
.fe-pr-sequence{display:flex;gap:3px;margin:1rem 0;flex-wrap:wrap}
.fe-pr-sequence span{min-width:2rem;text-align:center;padding:.35rem .25rem;background:#e9eff2;border-radius:5px;font-variant-numeric:tabular-nums}
.fe-pr-sequence span.done{background:#dce9e8}
.fe-pr-sequence span.current{background:#335e78;color:white;font-weight:700}
.fe-pr-comparison{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.7rem}
.fe-pr-panel{border:1px solid #ccd7dd;border-radius:8px;background:white;padding:.7rem;min-width:0}
.fe-pr-panel h3{font-size:1rem;margin:0 0 .7rem;color:#253541}
.fe-pr-panel h3 small{color:#536574}
.fe-pr-panel h3 small{display:block;font-size:.72rem;font-weight:400;color:#60727d;margin-top:.2rem}
.fe-pr-frames{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px}
.fe-pr-frame{background:#eaf0f3;border:1px solid #d3dfe4;border-radius:5px;text-align:center;padding:.6rem .1rem;font-weight:700;font-size:1.15rem}
.fe-pr-frame.empty{color:#84929a}
.fe-pr-count{font-size:.9rem;font-weight:700;margin:.7rem 0 .35rem}
.fe-pr-detail{font-size:.82rem;line-height:1.6;min-height:3em;margin:0}
.fe-pr-status{padding:.7rem;background:#e9f0f2;border-radius:6px;font-size:.9rem;margin:.8rem 0}
.fe-pr-controls{display:flex;gap:.5rem;flex-wrap:wrap}
.fe-pr-controls button{border:1px solid #335e78;border-radius:6px;padding:.5rem .9rem;background:#335e78;color:white;cursor:pointer}
.fe-pr-controls button[data-action="reset"]{background:white;color:#335e78}
.fe-pr-controls button:disabled{opacity:.45;cursor:default}
@media(max-width:380px){.fe-pr-demo{padding:.65rem}.fe-pr-panel{padding:.45rem}.fe-pr-sequence span{min-width:1.55rem;font-size:.85rem}}
@media(prefers-color-scheme:dark){.fe-pr-demo{background:#19262e;color:#e9f0f3;border-color:#536775}.fe-pr-panel{background:#24333c;border-color:#526571}.fe-pr-frame{background:#334650;border-color:#60717a}.fe-pr-sequence span{background:#334650}.fe-pr-sequence span.done{background:#375650}.fe-pr-sequence span.current{background:#487e9c}.fe-pr-status{background:#304650} .fe-pr-hint,.fe-pr-panel h3 small{color:#bdcbd2}.fe-pr-panel h3{color:#f0f5f8}}
</style>
<script>
(function(){
  function init(){
    const root=document.getElementById('fe-page-replacement-demo');
    if(!root || root.dataset.ready) return;
    root.dataset.ready='1';
    const sequence=[1,3,2,1,4,5,2,3,4,5];
    let step=0;
    function simulate(){
      const fifo=[null,null,null],lru=[null,null,null],queue=[],last={};
      let fifoCount=0,lruCount=0;
      const history=[];
      sequence.forEach((page,i)=>{
        const notes={fifo:'',lru:''};
        if(fifo.includes(page)){
          notes.fifo='ヒット：読み込み順は更新しません';
        }else{
          let slot=fifo.indexOf(null);
          if(slot!==-1){
            fifo[slot]=page;queue.push(page);
            notes.fifo='空き枠へ読み込み（置換えなし）';
          }else{
            const victim=queue.shift();
            slot=fifo.indexOf(victim);
            fifo[slot]=page;queue.push(page);fifoCount++;
            notes.fifo=victim+'を追い出し、'+page+'を読み込み';
          }
        }
        if(lru.includes(page)){
          notes.lru='ヒット：'+page+'の最終参照時刻を更新';
        }else{
          let slot=lru.indexOf(null);
          if(slot!==-1){
            lru[slot]=page;
            notes.lru='空き枠へ読み込み（置換えなし）';
          }else{
            let victim=lru[0];
            lru.forEach(p=>{if(last[p]<last[victim])victim=p;});
            slot=lru.indexOf(victim);
            lru[slot]=page;lruCount++;
            notes.lru=victim+'を追い出し、'+page+'を読み込み';
          }
        }
        last[page]=i;
        history.push({page,fifo:fifo.slice(),lru:lru.slice(),fifoCount,lruCount,notes});
      });
      return history;
    }
    const history=simulate();
    function render(){
      root.querySelector('.fe-pr-sequence').innerHTML=sequence.map((p,i)=>'<span class="'+(i===step-1?'current':i<step?'done':'')+'">'+p+'</span>').join('');
      ['fifo','lru'].forEach(method=>{
        const panel=root.querySelector('[data-method="'+method+'"]');
        const current=step?history[step-1]:null;
        const frames=current?current[method]:[null,null,null];
        panel.querySelector('.fe-pr-frames').innerHTML=frames.map(p=>'<div class="fe-pr-frame'+(p===null?' empty':'')+'">'+(p===null?'—':p)+'</div>').join('');
        panel.querySelector('.fe-pr-count').textContent='置換え：'+(current?current[method+'Count']:0)+'回';
        panel.querySelector('.fe-pr-detail').textContent=current?current.notes[method]:'まだ参照していません';
      });
      root.querySelector('.fe-pr-status').textContent=step===0?'開始前：3つのページ枠は空です。':step===sequence.length?'完了：この参照列の置換え回数はFIFOが3回、LRUが6回です。':'ステップ '+step+' / '+sequence.length+'：ページ'+history[step-1].page+'を参照';
      root.querySelector('[data-action="prev"]').disabled=step===0;
      root.querySelector('[data-action="next"]').disabled=step===sequence.length;
    }
    root.querySelector('[data-action="prev"]').addEventListener('click',()=>{step=Math.max(0,step-1);render();});
    root.querySelector('[data-action="next"]').addEventListener('click',()=>{step=Math.min(sequence.length,step+1);render();});
    root.querySelector('[data-action="reset"]').addEventListener('click',()=>{step=0;render();});
    render();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);
  else init();
})();
</script>

## よくある誤解・混同

LRUでは、次の混同がよく起こります。

| 混同 | 正しい切り分け |
|---|---|
| LRUは参照回数を見る | LRUは最後に参照した時刻を見る |
| LRUは最初に参照した時刻を見る | LRUは最後に参照した時刻を見る |
| LFUとLRUを同じだと思う | LFUは頻度、LRUは最近使った時刻 |
| 累積の参照回数が少ないものを必ず置換する | LRUでは回数ではなく、最後に使った時刻を見る |
| 最近よく使ったページを捨てる | LRUは最近使われていないページを捨てる |
| ページ枠にあるページを見たら何もしない | 置換はしないが、参照時刻は更新する |
| 数字が小さいページを追い出す | ページ番号の大小は関係ない |

## さらに注意したいひっかけ

LRUでは、次のひっかけにも注意します。

| ひっかけ表現 | なぜ注意する？ |
|---|---|
| 最初に参照した時刻 | LRUではなく、古い順やFIFO系の考え方に近い |
| 単位時間当たりの参照頻度 | LFUの判断基準 |
| 累積の参照回数 | 回数を見る方式で、LRUとは違う |
| 使用頻度の低いページを置き換える | LFUの説明になりやすい |
| ページサイズが小さいものを置き換える | LRUの判断基準ではない |

LRUは、**最近使われたかどうか** を見ます。

古くから存在しているページでも、直前に参照されていれば置換対象にはなりにくいです。

## まとめ（試験直前用）

まず、アルゴリズム名を見たら次の質問に置き換えると判断しやすくなります。

```text
LRU  → 最後にいつ使った？
LFU  → どれくらい頻繁に使った？
FIFO → いつ主記憶に入った？
```

- LRUは、Least Recently Used の略
- LRUは、最後に参照された時刻が最も古いページを置換する
- 判断の合図は「最後に参照した時刻」「最近使われていない」
- LFUは、単位時間当たりの参照頻度を見る
- FIFOは、最初に読み込まれた順番を見る
- **「古くからいるページ」と「長く使っていないページ」は同じとは限らない**
- LRUは参照回数ではなく、最後に使ったタイミングを見る
- ページ枠にヒットした場合も、参照時刻は更新する
- ページ参照列では、ヒットのたびに「最近使った順」を更新する

## 関連記事

役割を分けて読むと整理しやすくなります。

- [LRUとは？FIFO・LFU・NRUとの違い]({{ '/fe/lru/' | relative_url }}) — LRUの全体像とキャッシュ置換を含む比較
- [FIFO方式とは？先に入ったページを先に置き換える方法]({{ '/fe/fifo-page-replacement/' | relative_url }}) — FIFOのページ置換と参照列の追い方
- [ページング方式とは？ページとフレームで主記憶を管理する考え方]({{ '/fe/paging/' | relative_url }})
- [主記憶管理方式の違いとは？固定区画・可変区画・ページングを比較]({{ '/fe/memory-management-methods/' | relative_url }})

{% include fe_article_footer.html %}
