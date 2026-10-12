---
layout: page
title: LLMのTemperatureとは？出力のランダム性を理解する【DS検定】
description: LLMのTemperatureが次のトークンの確率分布をどう変えるかを、数値例で説明します。低い値と高い値の違い、サンプリングやtop-k・top-pとの役割の違いを整理し、再現性や正確さを保証しない点と、生成方式・実装に応じた設定の確認方法を学べます。
permalink: /ds/llm-temperature/
categories: [ai-utilization]
tags: [ds, ai-use]
ds_area: foundation
ds_section: ai-fundamentals
prev: /ds/hallucination/
next: /ds/mlops/
last_modified_at: 2026-10-12
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

Temperature（テンペラチャー）は、**次のトークンを確率的に選ぶとき、その確率分布の偏りを調整する設定**です。同じモデル・入力で比べると、低くするほど有力な候補に確率が集中し、高くするほど候補間の差が小さくなります。

低い値は似た出力を得やすくする傾向がありますが、**同じ出力や事実の正しさを保証する設定ではありません**。

## 直感的な説明

次の言葉の候補に「晴れ」「曇り」「雨」があると考えます。有力な候補をより選びやすくするのが低いTemperature、比較的選ばれにくい候補にも選ばれる余地を広げるのが高いTemperatureです。

| 候補 | Temperature＝1 | Temperature＝0.5 |
|---|---:|---:|
| 晴れ | 60.0% | 約78.3% |
| 曇り | 30.0% | 約19.6% |
| 雨 | 10.0% | 約2.2% |

これは仕組みを説明する仮の分布です。低くしても、有力な候補以外が必ず選ばれなくなるわけではありません。実際の文章では、選んだトークンによって、その後の候補も変わります。

## 定義・仕組み

モデルが次のトークン候補に付けたスコア（logit）を、正のTemperatureで割ってから、softmaxで確率へ変換します。

- **Temperature＜1**：候補間のスコア差を強め、確率を有力な候補に集中させる。
- **Temperature＝1**：Temperatureによるスコアの拡大・縮小をしない。
- **Temperature＞1**：候補間のスコア差を弱め、分布を平らにする。

上の表では、Temperature＝1の確率を2乗して合計が1になるように割ると、Temperature＝0.5の確率になります。これはほかの候補制限を加えていない場合の例です。

Temperatureは学習済みモデルの重みを更新するものではありません。また、候補の範囲を絞るtop-k・top-pや、サンプリングの有無は別の設定です。

例えばHugging Face Transformersでは、通常の貪欲法（greedy decoding）は最も有力な候補を選び、サンプリングでは候補を確率的に選びます。Temperatureを調整してサンプリングする場合は、`do_sample=True`など、生成方式の設定も確認します。

## どんな場面で使う？

定型文や形式をそろえたい出力では低めの値を、案の候補を広げたい生成では高めの値を試す、という使い方が考えられます。ただし、高くすると内容が不自然になることもあり、低くしても誤った回答を繰り返す場合があります。

実務では、同じ評価用入力を使い、設定を一つずつ変えて、形式への適合・内容の妥当性・候補の多様性を確認します。事実の正確さが必要な回答は、根拠資料との照合も行います。

## よくある誤解・混同

- **低ければ毎回同じ回答？** 似やすくなる傾向はありますが、乱数、ほかの生成設定、モデルや実行環境の違いなども影響します。
- **Temperature＝0ならどの製品でも使える？** 0を貪欲法に相当する指定として扱うAPIもありますが、正の値を要求する実装もあります。対応する値・モデル・生成方式を確認します。
- **高いほど優れたアイデアになる？** 候補が多様になることと、案が有用であることは別です。用途に合うか評価します。
- **低くするとハルシネーションを防げる？** 正しさは保証されません。出典や元データによる確認が必要です。

## まとめ（試験直前用）

- Temperatureは、サンプリングに用いる次トークンの確率分布を調整する。
- 低い値は有力な候補に集中、高い値は分布を平らにする。
- 学習、候補の絞り込み、事実確認とは別の役割。
- 出力の再現性や正確さは保証しない。利用できる設定は実装ごとに確認する。

## 公式情報・参考リンク

- [Hugging Face Transformers：生成設定](https://huggingface.co/docs/transformers/main_classes/text_generation)：Temperature、サンプリング、top-k・top-pの役割。

## 対応スキル項目（ver.6 基盤）

- **位置づけ**：生成AIの出力制御の補助学習
- **★1直接対応**：なし
- ver.6の★1一覧にはこの用語自体の直接項目はありません。関連する試験テーマの理解を補う学習内容として整理します。
- [ver.6 ★1スキルチェックで確認する](/ds/foundation-skillcheck/)
## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>

<div style="margin-top: 16px;">
  🏠 <a href="/ds/">DS検定トップに戻る</a>
</div>

<div style="display:flex;justify-content:space-between;margin-top:12px;">

  {% if page.previous.url %}
    <a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url }}">{{ page.next.title }} →</a>
  {% endif %}

</div>
