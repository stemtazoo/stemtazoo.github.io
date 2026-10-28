---
layout: page
title: for文の終了後、変数iはnかn+1か？擬似言語の仕様と科目Bの注意点【基本情報技術者試験】
description: FE科目Bのfor文について、繰返し中の値と終了後の制御変数を区別。IPA公式の記述範囲、Pythonとの違い、配列の二重添字を体験例で整理します。
permalink: /fe/for-loop-final-variable/
tags: [fe, fe-technology, algorithm, programming, pseudocode]
fe_section: 科目B対策
fe_subsection: アルゴリズム
fe_order: 243
date: 2026-10-28
last_modified_at: 2026-10-28
---

## まず結論

**for文の本体を実行するときの制御変数の値**と、**for文が終了した後の制御変数の値**は分けて考えます。

例えば「iを1から4まで1ずつ増やす」なら、本体を実行するのは i = 1, 2, 3, 4 の4回です。ただし、**終了後のiが4なのか5なのかは、ループの仕様を確認する必要があります**。

IPAの「擬似言語の記述形式」Ver.5.1（別紙2）は、for文を制御記述に基づく繰返し処理として説明していますが、終了後の制御変数の値までは明記していません。

> **本体の最後のiと、ループ終了後のiを混同しない。仕様にない値を決めつけない。**

## 直感的な説明

~~~text
i = 1 → 本体を実行
i = 2 → 本体を実行
i = 3 → 本体を実行
i = 4 → 本体を実行
       → ループ終了
~~~

ここまでなら、どちらの方式でも同じです。

- **終了判定前に5へ増やす方式**：終了後のiは5
- **最後に使った4を保持する方式**：終了後のiは4

どちらになるかは、実際の言語や問題文の定義によります。

### 数値を変えて確認する

<div id="fe-for-final-demo" class="fe-for-final-demo">
  <label for="fe-for-final-n">終了値 n：<strong id="fe-for-final-n-label">4</strong></label>
  <input id="fe-for-final-n" type="range" min="1" max="9" value="4" style="width:100%;margin:.8rem 0">
  <div id="fe-for-final-output" aria-live="polite"></div>
  <button id="fe-for-final-reset" type="button">n = 4 に戻す</button>
</div>
<style>
.fe-for-final-demo{padding:1.2rem;border:1px solid #cbd5e1;border-radius:12px;background:#f8fafc;color:#263747;margin:1rem 0}
.fe-for-final-demo .fe-for-final-line{background:#fff;border:1px solid #e2e8f0;border-radius:8px;padding:.75rem;margin:.6rem 0}
.fe-for-final-demo button{border:1px solid #94a3b8;background:#fff;color:#263747;border-radius:6px;padding:.5rem .8rem;cursor:pointer}
</style>
<script>
(function(){
  function init(){
    var root=document.getElementById('fe-for-final-demo');
    if(!root||root.dataset.ready)return;
    root.dataset.ready='1';
    var input=document.getElementById('fe-for-final-n');
    var label=document.getElementById('fe-for-final-n-label');
    var output=document.getElementById('fe-for-final-output');
    function render(){
      var n=Number(input.value);
      var values=Array.from({length:n},function(_,i){return i+1;});
      label.textContent=String(n);
      output.innerHTML='<div class="fe-for-final-line">本体を実行する i：<strong>'+values.join(' → ')+'</strong></div>'+
      '<div class="fe-for-final-line">終了後の i（増分後に判定する方式）：<strong>'+(n+1)+'</strong></div>'+
      '<div class="fe-for-final-line">終了後の i（最後の値を保持する方式）：<strong>'+n+'</strong></div>'+
      '<p>※これは2種類の動作モデルの比較です。IPAがどちらかを指定しているという意味ではありません。</p>';
    }
    input.addEventListener('input',render);
    document.getElementById('fe-for-final-reset').addEventListener('click',function(){input.value='4';render();});
    render();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);
  else init();
})();
</script>

## 定義・仕組み

### IPAの公式仕様で確認できる範囲

IPA「試験で使用する情報技術に関する用語・プログラム言語など」Ver.5.1の別紙2（基本情報技術者試験・応用情報技術者試験用）では、for文は制御記述に基づいて処理を繰り返す形式です。

**繰返し終了後の制御変数の値については、同資料のfor文の説明に明示的な規定がありません。** したがって「IPAの擬似言語では常にn+1」と断言するのは避けます。

公式資料：[IPA：試験で使用する情報技術に関する用語・プログラム言語など Ver.5.1](https://www.ipa.go.jp/shiken/syllabus/doe3um0000002djj-att/shiken_yougo_ver5_1.pdf)

### Pythonと混同しない

Pythonの次のコードでは、繰返し終了後のiは4です。

~~~python
for i in range(1, 5):
    print(i)
print(i)  # 4
~~~

Pythonの `range(1, 5)` は1から4までの値を生成し、最後に代入されたiが残ります。これはPythonの動作であり、擬似言語の一般ルールを決める根拠にはなりません。

## 科目Bでどう使う？

例えば次のような問題を考えます。配列の添字は1から始まります。

~~~text
data = {5, 3, 1, 2, 4}
n = 4
ret ← 0
for (iを1からnまで1ずつ増やす)
    ret ← ret + data[data[i]]
endfor
return ret + i
~~~

二重の添字は内側から計算します。

| i | data[i] | data[data[i]] | ret |
|---:|---:|---:|---:|
| 1 | 5 | 4 | 4 |
| 2 | 3 | 1 | 5 |
| 3 | 1 | 5 | 10 |
| 4 | 2 | 3 | 13 |

ループ本体の処理後、**ret = 13** は確定します。しかし、最後の `return ret + i` は終了後のiの仕様に依存します。

| 終了後のiの扱い | 戻り値 |
|---|---:|
| 5になる方式 | 18 |
| 4を保持する方式 | 17 |

この例で18が模範解答なら、教材が「終了後は5になる」動作を前提にしている可能性があります。ただし、解答だけからIPA公式仕様の一般則だと断定しません。

## どんな場面で使う？

for文の外側で制御変数を参照するコードを読むときに重要です。反対に、繰返し回数やループ本体内の計算だけを問う問題なら、終了後のiを決める必要はありません。

実務のプログラムでも、ループ終了後の変数値に依存する処理は言語仕様を確認することが大切です。

## よくある誤解・混同

### 誤解1：iを1からnまで動かすなら、終了後も必ずn

**本体で最後に使った値**と**終了後に残る値**は別です。

### 誤解2：終了判定のため、必ずn+1になる

増分後に判定する方式ならそうなりますが、すべての言語・擬似言語に共通するとは限りません。

### 誤解3：Pythonのfor文と同じに考えてよい

Pythonは反復可能オブジェクトから順に値を取り出す仕組みです。擬似言語のfor文と無条件に同一視しません。

### 誤解4：data[data[i]] は data[i] と同じ

まずdata[i]を読み、その値を次の添字としてdata[値]を読みます。[配列の基本](/fe/array/)も確認しましょう。

## まとめ（試験直前用）

- **繰返し本体**：iが1からnなら、通常は1〜nの値で実行する
- **終了後のi**：問題文・教材・言語の仕様を確認する
- **二重添字**：内側から評価し、表でretを追跡する

関連：[前判定・後判定の繰返しとは？](/fe/control-structures-loop-selection/)

{% include fe_article_footer.html %}
