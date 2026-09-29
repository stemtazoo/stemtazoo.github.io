---
layout: page
title: 標準偏差の読み方とは？±1σ・±2σ・±3σと正規分布【DS検定】
description: "標準偏差を正規分布と組み合わせて読む方法を整理します。±1σ・±2σ・±3σに入る確率、平均から片側までの確率、片側の外側確率を図解し、2σと片側2σの混同を防ぎます。"
permalink: /ds/variance-standard-deviation/
categories: [data-science]
tags: [ds, statistics]
ds_area: datascience
ds_section: statistics
prev: /ds/variance-and-standard-deviation/
next: /ds/welch-t-test/
last_modified_at: 2026-09-30
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

標準偏差は、**データが平均からどのくらい散らばっているか**を表す指標です。

さらにデータがおおむね正規分布に従うときは、標準偏差を使って「平均のまわりにどのくらいの割合が入るか」を読むことができます。

| 範囲 | 中央の確率 | 平均〜片側まで | 片側の外側 |
|---|---:|---:|---:|
| ±1σ | 約68.27% | 約34.135% | 約15.865% |
| ±2σ | **約95.45%** | **約47.725%** | **約2.275%** |
| ±3σ | 約99.73% | 約49.865% | 約0.135% |

特に注意したいのが **「2σ」** です。

- 「±2σの範囲」 → 約95.45%
- 「平均から+2σまで」 → 約47.725%
- 「+2σより外側」 → 約2.275%

つまり、**2σという距離だけでは確率は1つに決まりません。どの範囲の面積を聞いているかを見ることが重要**です。

分散と標準偏差そのものの定義や単位の違いは、[分散と標準偏差の違いとは？ばらつきをどう読むか](/ds/variance-and-standard-deviation/)で整理しています。

---

## 直感的な説明

正規分布を山の形として考えると、標準偏差 σ は「山の中心からどれだけ離れた位置か」を測る物差しです。

中央の平均を 0 とすると、

- ±1σ：中心のかなり広い部分
- ±2σ：ほとんどの部分
- ±3σ：ほぼ全体

が含まれます。

ただし「+2σ」という位置を示されても、問題が聞いているのが **中央なのか、平均から右半分なのか、そのさらに外側なのか**で答えは変わります。

### 図で確認：どの面積を見ている？

<div id="sigma-viz" class="sigma-viz">
  <div class="sigma-viz__controls" role="group" aria-label="シグマ範囲を選択">
    <span class="sigma-viz__label">距離</span>
    <button type="button" class="sigma-viz__btn" data-sigma="1">1σ</button>
    <button type="button" class="sigma-viz__btn is-active" data-sigma="2">2σ</button>
    <button type="button" class="sigma-viz__btn" data-sigma="3">3σ</button>
  </div>

  <div class="sigma-viz__controls" role="group" aria-label="確率の範囲を選択">
    <span class="sigma-viz__label">見る範囲</span>
    <button type="button" class="sigma-viz__btn is-active" data-mode="center">中央 ±kσ</button>
    <button type="button" class="sigma-viz__btn" data-mode="half">平均 → +kσ</button>
    <button type="button" class="sigma-viz__btn" data-mode="tail">+kσ より外側</button>
  </div>

  <div class="sigma-viz__result" aria-live="polite">
    <strong id="sigma-viz-title">±2σ に入る確率</strong>
    <span id="sigma-viz-value">約95.45%</span>
    <small id="sigma-viz-note">平均を中心に左右2σまでの範囲です。</small>
  </div>

  <svg id="sigma-viz-svg" viewBox="0 0 720 300" role="img" aria-label="正規分布と標準偏差の範囲">
    <line x1="40" y1="245" x2="680" y2="245" class="sigma-viz__axis"></line>
    <polygon id="sigma-viz-fill" class="sigma-viz__fill" points=""></polygon>
    <polyline id="sigma-viz-curve" class="sigma-viz__curve" points=""></polyline>
    <g id="sigma-viz-guides"></g>
  </svg>

  <div class="sigma-viz__hint">ボタンを押して、同じ「2σ」でも面積が変わることを確認できます。</div>
</div>

<style>
.sigma-viz{
  margin:20px 0 26px;
  padding:18px;
  border:1px solid #dbe4ee;
  border-radius:14px;
  background:#f8fafc;
}
.sigma-viz__controls{
  display:flex;
  flex-wrap:wrap;
  align-items:center;
  gap:8px;
  margin-bottom:10px;
}
.sigma-viz__label{
  min-width:64px;
  font-weight:700;
}
.sigma-viz__btn{
  border:1px solid #94a3b8;
  border-radius:999px;
  padding:7px 12px;
  background:#fff;
  color:#334155;
  font-size:.92rem;
  cursor:pointer;
}
.sigma-viz__btn:hover,
.sigma-viz__btn:focus-visible{
  border-color:#2563eb;
  outline:2px solid transparent;
}
.sigma-viz__btn.is-active{
  background:#2563eb;
  border-color:#2563eb;
  color:#fff;
  font-weight:700;
}
.sigma-viz__result{
  display:grid;
  grid-template-columns:1fr auto;
  gap:4px 14px;
  align-items:center;
  margin:14px 0 4px;
  padding:14px 16px;
  background:#fff;
  border-radius:12px;
  border-left:5px solid #2563eb;
}
.sigma-viz__result strong{
  font-size:1rem;
}
.sigma-viz__result span{
  font-size:1.35rem;
  font-weight:800;
  color:#1d4ed8;
}
.sigma-viz__result small{
  grid-column:1 / -1;
  color:#475569;
}
.sigma-viz__axis{
  stroke:#64748b;
  stroke-width:1.5;
}
.sigma-viz__curve{
  fill:none;
  stroke:#0f172a;
  stroke-width:3;
  stroke-linejoin:round;
  stroke-linecap:round;
}
.sigma-viz__fill{
  fill:#93c5fd;
  opacity:.72;
}
.sigma-viz__guide{
  stroke:#64748b;
  stroke-width:1;
  stroke-dasharray:5 5;
}
.sigma-viz__guide--active{
  stroke:#2563eb;
  stroke-width:2;
}
.sigma-viz__text{
  fill:#334155;
  font-size:13px;
  text-anchor:middle;
}
.sigma-viz__text--active{
  fill:#1d4ed8;
  font-weight:700;
}
.sigma-viz__hint{
  margin-top:-4px;
  font-size:.9rem;
  color:#64748b;
}
@media (max-width: 640px){
  .sigma-viz{padding:14px 10px;}
  .sigma-viz__label{width:100%;min-width:0;}
  .sigma-viz__btn{padding:7px 10px;font-size:.86rem;}
  .sigma-viz__result{grid-template-columns:1fr;}
  .sigma-viz__result span{font-size:1.25rem;}
  #sigma-viz-svg{width:100%;height:auto;}
}
</style>

<script>
(function(){
  const root = document.getElementById('sigma-viz');
  if (!root) return;

  const svg = document.getElementById('sigma-viz-svg');
  const curve = document.getElementById('sigma-viz-curve');
  const fill = document.getElementById('sigma-viz-fill');
  const guides = document.getElementById('sigma-viz-guides');
  const title = document.getElementById('sigma-viz-title');
  const value = document.getElementById('sigma-viz-value');
  const note = document.getElementById('sigma-viz-note');

  let sigma = 2;
  let mode = 'center';

  const values = {
    1: {center:'68.27', half:'34.135', tail:'15.865'},
    2: {center:'95.45', half:'47.725', tail:'2.275'},
    3: {center:'99.73', half:'49.865', tail:'0.135'}
  };

  const xMin = -4;
  const xMax = 4;
  const left = 40;
  const right = 680;
  const baseY = 245;
  const peakHeight = 185;

  function sx(x){
    return left + (x - xMin) / (xMax - xMin) * (right - left);
  }

  function sy(x){
    const y = Math.exp(-0.5 * x * x);
    return baseY - y * peakHeight;
  }

  function range(){
    if (mode === 'center') return [-sigma, sigma];
    if (mode === 'half') return [0, sigma];
    return [sigma, xMax];
  }

  function makeCurve(){
    const pts = [];
    for(let x = xMin; x <= xMax + 0.001; x += 0.04){
      pts.push(sx(x).toFixed(1) + ',' + sy(x).toFixed(1));
    }
    curve.setAttribute('points', pts.join(' '));
  }

  function makeFill(){
    const r = range();
    const pts = [sx(r[0]).toFixed(1) + ',' + baseY];
    for(let x = r[0]; x <= r[1] + 0.001; x += 0.03){
      pts.push(sx(x).toFixed(1) + ',' + sy(x).toFixed(1));
    }
    pts.push(sx(r[1]).toFixed(1) + ',' + baseY);
    fill.setAttribute('points', pts.join(' '));
  }

  function makeGuides(){
    guides.innerHTML = '';
    [-3,-2,-1,0,1,2,3].forEach(function(k){
      const x = sx(k);
      const line = document.createElementNS('http://www.w3.org/2000/svg','line');
      line.setAttribute('x1',x);
      line.setAttribute('x2',x);
      line.setAttribute('y1',k === 0 ? 52 : 92);
      line.setAttribute('y2',baseY);
      line.setAttribute('class','sigma-viz__guide' + (Math.abs(k) === sigma || (mode !== 'center' && k === 0) ? ' sigma-viz__guide--active' : ''));
      guides.appendChild(line);

      const text = document.createElementNS('http://www.w3.org/2000/svg','text');
      text.setAttribute('x',x);
      text.setAttribute('y',268);
      text.setAttribute('class','sigma-viz__text' + (Math.abs(k) === sigma || k === 0 ? ' sigma-viz__text--active' : ''));
      text.textContent = k === 0 ? '平均' : (k > 0 ? '+' + k + 'σ' : k + 'σ');
      guides.appendChild(text);
    });
  }

  function updateText(){
    if(mode === 'center'){
      title.textContent = '±' + sigma + 'σ に入る確率';
      value.textContent = '約' + values[sigma].center + '%';
      note.textContent = '平均を中心に左右' + sigma + 'σまでの範囲です。';
    } else if(mode === 'half'){
      title.textContent = '平均から +' + sigma + 'σ まで';
      value.textContent = '約' + values[sigma].half + '%';
      note.textContent = '左右対称なので、±' + sigma + 'σの中央確率のちょうど半分です。';
    } else {
      title.textContent = '+' + sigma + 'σ より外側';
      value.textContent = '約' + values[sigma].tail + '%';
      note.textContent = '右側だけの上側確率です。左側も同じ確率になります。';
    }
  }

  function updateButtons(){
    root.querySelectorAll('[data-sigma]').forEach(function(btn){
      btn.classList.toggle('is-active', Number(btn.dataset.sigma) === sigma);
    });
    root.querySelectorAll('[data-mode]').forEach(function(btn){
      btn.classList.toggle('is-active', btn.dataset.mode === mode);
    });
  }

  function render(){
    makeFill();
    makeGuides();
    updateText();
    updateButtons();
  }

  root.addEventListener('click', function(e){
    const btn = e.target.closest('button');
    if(!btn) return;
    if(btn.dataset.sigma) sigma = Number(btn.dataset.sigma);
    if(btn.dataset.mode) mode = btn.dataset.mode;
    render();
  });

  makeCurve();
  render();
})();
</script>

<noscript>
JavaScriptを無効にしている場合は、上の表で確率を確認してください。
</noscript>

---

## 定義・仕組み

### 標準偏差そのものは「確率」ではない

標準偏差は、データのばらつきの大きさを表す量です。

標準偏差が 2 だから「確率が95%」という意味ではありません。

**正規分布という分布の形を仮定したときに、平均から標準偏差何個分までの面積を確率として読める**ようになります。

この区別は重要です。

### ±1σ・±2σ・±3σ

正規分布では、平均を中心とした範囲におおよそ次の割合が入ります。

- ±1σ：約68.27%
- ±2σ：約95.45%
- ±3σ：約99.73%

これは「68-95-99.7ルール」と呼ばれることがあります。

### 片側だけを読むとき

正規分布は平均を中心に左右対称です。

そのため、たとえば ±2σ の中央確率が約95.45%なら、

- 平均から +2σ まで：約95.45% ÷ 2 = 約47.725%
- ±2σ の外側全体：約4.55%
- +2σ より外側だけ：約4.55% ÷ 2 = 約2.275%

となります。

「両側を半分にする」のか、「中央以外を求めてから半分にする」のかを整理すると、片側問題でも迷いにくくなります。

### zスコアとの関係

zスコアは、観測値が平均から標準偏差何個分離れているかを表します。

たとえば z = 2 は「平均より +2σ の位置」です。

ただし **z = 2 は位置を表す値**であり、95.45%や2.275%という確率そのものではありません。

詳しくは [zスコアとは？標準化・偏差値・外れ値判定を整理](/ds/z-score-method/) も参考になります。

---

## どんな場面で使う？

標準偏差と正規分布の関係は、次のような場面で使われます。

- センサー値が通常範囲からどれくらい外れているかを見る
- 製品寸法のばらつきを確認する
- 得点や測定値の相対的な位置を考える
- zスコアを使った外れ値候補の確認
- 信頼区間や仮説検定を学ぶ前の基礎として確率の位置関係を理解する

たとえば製品寸法が正規分布に近く、平均100 mm、標準偏差2 mmなら、

- ±1σ：98〜102 mm
- ±2σ：96〜104 mm
- ±3σ：94〜106 mm

という範囲になります。

ただし、**この範囲に68%・95%・99.7%程度が入るという解釈は、分布が正規分布に近いことが前提**です。

---

## よくある誤解・混同

### ① 「2σ = 95.45%」とだけ覚える

これは不十分です。

正しくは、**正規分布で平均を中心とした ±2σ の範囲が約95.45%**です。

+2σより外側だけを聞かれた場合は約2.275%です。

### ② 0〜+2σ も95.45%だと思う

平均から+2σまでは、中央の±2σの半分なので約47.725%です。

正規分布は左右対称なので、中央確率を半分にできます。

### ③ ±2σの外側片側を4.55%だと思う

4.55%は、±2σの**左右両方の外側を合計した確率**です。

片側だけならその半分の約2.275%です。

### ④ どんな分布でも68-95-99.7が使えると思う

使えません。

68-95-99.7という割合は、正規分布に対する性質です。

分布が大きく歪んでいる場合や外れ値が多い場合は、標準偏差だけで範囲を判断しないようにします。

### ⑤ 標準偏差とzスコアを同じものだと思う

標準偏差は「ばらつきの大きさ」、zスコアは「平均から標準偏差何個分離れているか」です。

- 標準偏差 σ：物差しの1目盛り
- zスコア：その物差しで測った位置

と考えると整理しやすくなります。

---

## まとめ（試験直前用）

- 標準偏差はデータのばらつきを表す
- 正規分布なら ±1σ ≈ 68.27%、±2σ ≈ 95.45%、±3σ ≈ 99.73%
- 平均〜+2σは約47.725%
- +2σより外側は約2.275%
- 「2σ」と見たら、**どの範囲の面積を聞いているか**を確認する
- 68-95-99.7ルールは正規分布を前提とする
- zスコアは確率ではなく、平均から標準偏差何個分離れた位置かを表す

迷ったら、**「位置を聞いているのか、面積＝確率を聞いているのか」**で切り分けます。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：基礎技術
- **スキルカテゴリ**：科学的解析の基礎
- **サブカテゴリ**：統計数理基礎
- **必須スキル**：◯
- ★ 分散、標準偏差、四分位、パーセンタイルを理解し、目的に応じて適切に使い分けることができる
- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)
