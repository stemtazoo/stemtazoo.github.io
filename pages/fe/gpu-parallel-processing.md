---
layout: page
title: GPUとは？CPUとの違いと多数の演算器による並列処理【基本情報技術者試験】
description: GPUが3D画像処理や大量の同種演算を高速化できる理由をCPUとの比較図で説明。GPGPUの用途、FPGA・TPM・量子プロセッサとの違いと科目Aの判断基準を整理します。
permalink: /fe/gpu-parallel-processing/
tags: [fe, fe-technology, computer-architecture, hardware]
fe_section: テクノロジ系
fe_subsection: コンピュータ構成要素
fe_order: 185
date: 2026-11-07
last_modified_at: 2026-11-07
related_articles:
  - /fe/multicore-processor/
  - /fe/multiprocessor-system-types/
---

## まず結論

**GPU（Graphics Processing Unit）は、同じ種類の演算を大量のデータに対して並列に処理することが得意なプロセッサ**です。もともと画像・3D描画を高速化するために発展しましたが、現在はAIや科学技術計算にも利用されています。

基本情報技術者試験（FE）では、**「多数の演算器」「並列演算」「画像・3D処理」**がGPUの判断キーワードです。

一方、CPUは複雑な制御や幅広い処理を柔軟に実行するのが得意です。「GPUならあらゆる計算がCPUより速い」という意味ではありません。

## 直感的な説明

例えば、3Dモデルの多くの頂点に、位置を変換する同じ計算を行う場面を考えます。

- **CPU**：さまざまな種類の仕事を、少数の高性能なコアで柔軟に進めるのが得意。
- **GPU**：大量のデータに似た計算を、数多くの演算器で同時並行に進めるのが得意。

### 図で比較：CPUとGPUの仕事の分担

<div class="fe-gpu-diagram" aria-label="CPUとGPUの並列処理の概念比較">
  <div class="fe-gpu-diagram__panel">
    <h4>CPU：複雑な処理や制御が得意</h4>
    <div class="fe-gpu-diagram__cores fe-gpu-diagram__cores--cpu">
      <span>処理A</span><span>処理B</span><span>処理C</span><span>処理D</span>
    </div>
    <p>少数の高性能なコアで、多様な命令や分岐を柔軟に処理。</p>
  </div>
  <div class="fe-gpu-diagram__panel">
    <h4>GPU：多数の同種演算を並列に実行</h4>
    <div class="fe-gpu-diagram__cores fe-gpu-diagram__cores--gpu" aria-label="同じ種類の計算を多数並列に処理する模式図">
      <span>計算</span><span>計算</span><span>計算</span><span>計算</span>
      <span>計算</span><span>計算</span><span>計算</span><span>計算</span>
      <span>計算</span><span>計算</span><span>計算</span><span>計算</span>
      <span>計算</span><span>計算</span><span>計算</span><span>計算</span>
    </div>
    <p>たくさんのデータに似た計算を行う処理と相性がよい。</p>
  </div>
</div>

<style>
.fe-gpu-diagram{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:12px;margin:1.2rem 0}
.fe-gpu-diagram__panel{border:1px solid #a5b6c3;border-radius:12px;padding:14px;background:#f7fafc;color:#26343e;min-width:0}
.fe-gpu-diagram__panel h4{font-size:1rem;margin:0 0 12px;color:#26343e}
.fe-gpu-diagram__cores{display:grid;gap:5px;margin-bottom:12px}
.fe-gpu-diagram__cores--cpu{grid-template-columns:repeat(2,minmax(0,1fr))}
.fe-gpu-diagram__cores--gpu{grid-template-columns:repeat(4,minmax(0,1fr))}
.fe-gpu-diagram__cores span{border-radius:6px;padding:11px 2px;text-align:center;font-size:.78rem;min-width:0}
.fe-gpu-diagram__cores--cpu span{background:#dbe9f5;color:#173a5e;border:1px solid #8eafcf}
.fe-gpu-diagram__cores--gpu span{background:#d9efe4;color:#174c36;border:1px solid #8dbca1}
.fe-gpu-diagram__panel p{margin:0;font-size:.91rem;line-height:1.65}
</style>

※上の図は違いを学ぶための**模式図**です。実際のCPU・GPUのコア数、演算器数や内部構造の比率ではありません。CPUも複数コア・SIMD命令などで並列処理できます。

## 定義・仕組み

### GPUが画像や3D描画を得意とする理由

3D描画では、頂点の座標変換や画素の色などについて、多数の演算を繰り返します。

例えば、異なる1万個のデータそれぞれに同じ数式を適用する場合、独立して計算できる部分を並列処理することで、全体の処理時間を短縮しやすくなります。

```text
多数の頂点・画素データ
    ↓
似た計算を多数のデータに適用
    ↓
GPUの演算器で並列に処理
    ↓
画像描画などの結果
```

このため、GPUは多数の浮動小数点演算などを並列に実行する構造に向いています。なお、現在のGPUは整数演算や行列演算なども扱い、浮動小数点演算だけに限定されません。

### GPGPUとは？

**GPGPU（General-Purpose computing on Graphics Processing Units）**は、GPUを画像描画以外の汎用的な計算に使う考え方です。

| 用語 | 意味 |
|---|---|
| GPU | 並列演算に強みを持つハードウェア |
| GPGPU | GPUを画像処理以外にも使う方法・利用形態 |

GPGPUの例は、機械学習の行列演算、科学技術シミュレーション、大規模な数値計算です。

GPUは、大量の行列計算や同じ処理を複数データに繰り返す場面で効果を発揮しやすいため、AIの学習・推論にも使われます。ただし、GPGPUとGPUは同じ意味ではありません。

### GPUとCPUの役割比較

| 観点 | CPU | GPU |
|---|---|---|
| 主な強み | 汎用処理・複雑な制御 | 大量の同種演算の並列処理 |
| 得意な場面 | OSの処理、複雑な分岐、順次実行 | 画像描画、行列演算、大量データ処理 |
| 苦手になりやすい場面 | 極めて大量の同種演算を単独で処理 | 分岐の多い処理、データ転送負荷が大きい処理 |
| 注意点 | CPUにも並列実行機能がある | GPUが常に速いわけではない |

CPUの複数コアによる処理は[マルチコアプロセッサ](/fe/multicore-processor/)で詳しく説明しています。

### GPU・FPGA・TPM・量子プロセッサは役割が違う

| 技術 | 何が特徴？ | 判断キーワード |
|---|---|---|
| **GPU** | 多数の演算器で同種演算を並列処理 | **3D描画・並列計算** |
| FPGA | 用途に応じて論理回路の構成を変更できる集積回路 | 回路の再構成 |
| TPM | 暗号鍵の保護や端末の信頼性確認を支援するセキュリティモジュール | 鍵の保護・セキュリティ |
| 量子プロセッサ | 量子ビットの性質を利用して計算する | 量子ビット・量子ゲート |

FPGAも並列処理に利用できますが、**GPUはプログラム可能な演算器群を使う**のに対し、**FPGAは論理回路の構成を変更できる**ことが特徴です。

TPMの中心は暗号鍵の安全な取り扱いです。量子プロセッサは量子ビットを利用するもので、単に「非常に速いGPU」を指すものではありません。

## 科目Aでどう出る？

科目Aでは「どの装置の特徴か」を文章から判断します。

```text
同じ種類の計算を多数同時に行う・3D描画
→ GPU

ハードウェアの論理回路を後から構成し直す
→ FPGA

端末内で暗号鍵を安全に管理
→ TPM

量子ビットの状態を利用して計算
→ 量子プロセッサ
```

**選び方のコツ：** 「速い」「並列」だけで判断せず、**何を並列に計算するか、回路を再構成するか、鍵を保護するか**を見ます。

### 独自の確認問題

工場の画像検査システムで、大量の画像に対して似た数値演算を並列に実行し、処理時間を短くしたい。用途に最も合う計算装置はどれか。

- ア：端末の暗号鍵を安全に管理するためのセキュリティモジュール
- イ：多数の演算器で画像データを並列処理するプロセッサ
- ウ：量子ビットを用いる量子計算装置
- エ：回路構成を変更して専用の信号処理を行える集積回路

<details markdown="1">
<summary>正解と解説を見る（タップして開く）</summary>

**正解：イ**

- ア：TPMの特徴です。暗号鍵の保護が主目的です。
- **イ：GPUの特徴です。** 似た数値演算を大量のデータに対して並列実行する場面と相性がよいです。
- ウ：量子プロセッサの特徴です。
- エ：FPGAの特徴です。画像処理をFPGAで実装する場合もありますが、設問で強調している多数の演算器による汎用的な並列演算という特徴はGPUに対応します。

</details>

## どんな場面で使う？

GPUはゲームや3D CG、画像・動画処理のほか、大量の数値計算でも使われます。

- 3Dモデルの頂点・画素の計算
- 深層学習の学習・推論
- シミュレーションや行列演算
- 大量の画像を対象とする検査・分析

例えばPythonの機械学習でも、対応するライブラリや環境を使えばGPU上で行列演算を実行できます。ただし、GPUにデータを転送する時間などがあるため、少量のデータではCPUの方が速い場合があります。

## よくある誤解・混同

### GPUにはCPUのようなプログラムを実行する機能がない？

GPUもプログラムによる命令に従って演算します。ただし、GPUは大量の同種計算を並列実行する設計を重視しています。

### GPUは必ずCPUより速い？

違います。処理が並列化しにくい場合、複雑な分岐が多い場合、CPUとGPU間でデータ転送を繰り返す場合などは、CPUの方が適することがあります。

### 「複数コア」と書いてあればGPU？

違います。CPUにもマルチコアがあります。**多数のデータに似た演算を並列に適用すること**がGPUを見分けるポイントです。

### GPUとFPGAはどちらも並列処理できるから同じ？

違います。GPUは多数の演算器を用いるプロセッサであり、FPGAは論理回路の構成を変更できる集積回路です。

### GPUをAIに使うのは画像処理の延長？

GPUによる行列演算などの汎用計算（GPGPU）が活用されています。画像を描く用途に限りません。

## まとめ（試験直前用）

- **GPU：同種の演算を大量のデータに並列実行することが得意**
- **CPU：複雑な制御や幅広い処理を柔軟に実行することが得意**
- **GPGPU：GPUを画像描画以外の汎用計算に活用**
- **FPGA：内部の論理回路を再構成できる**
- **TPM：暗号鍵などを保護する**
- **量子プロセッサ：量子ビットを利用する**
- GPUは常にCPUより高速というわけではない

## 公式資料・参考リンク

- [IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)
- [NVIDIA：CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/)
- [Intel：What Is a GPU?](https://www.intel.com/content/www/us/en/products/docs/processors/what-is-a-gpu.html)
- [AMD：FPGAについて](https://www.amd.com/ja/products/adaptive-socs-and-fpgas/fpga.html)
- [Trusted Computing Group：Trusted Platform Module](https://trustedcomputinggroup.org/work-groups/trusted-platform-module/)

{% include fe_article_footer.html %}
