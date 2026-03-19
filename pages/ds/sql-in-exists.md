---
layout: page
title: INとEXISTSの違いとは？値比較と存在判定を整理【DS検定】
permalink: /ds/sql-in-exists/
categories: [data-engineering]
tags: [ds, sql]
---

## まず結論

IN＝値がリストに含まれるかを判定

EXISTS＝条件に合うデータが存在するかを判定

DS検定では「値を見るのか・存在を見るのか」を見抜くことが重要




## 直感的な説明

例えば「注文したことがある顧客」を探す場合

IN

👉 顧客IDが注文リストに含まれているか

EXISTS

👉 注文データが存在するか

👉 結果は同じでも「考え方」が違う



## 定義・仕組み

IN

SELECT *
FROM 顧客
WHERE 顧客ID IN (
    SELECT 顧客ID FROM 注文
);

サブクエリの「値の集合」と比較




EXISTS

SELECT *
FROM 顧客 A
WHERE EXISTS (
    SELECT 1
    FROM 注文 B
    WHERE A.顧客ID = B.顧客ID
);

条件を満たす行が存在するかを判定




## どんな場面で使う？

IN

値のリストと比較したいとき

小さいデータや単純な条件


EXISTS

関連データの有無を確認したいとき

大きなデータ（効率が良い）




## よくある誤解・混同

❌ INとEXISTSは同じ

→ ⭕ 結果は同じでも意味が違う

👉 DS検定ではここがひっかけ



❌ INは常に速い

→ ⭕ データ量が多いとEXISTSの方が有利



❌ EXISTSは値を比較している

→ ⭕ 存在だけを見ている



❌ INはNULLでも問題ない

→ ⭕ NULLが含まれると挙動に注意

👉 DS検定では「NULLを含むIN」がよく出る



## まとめ（試験直前用）

IN＝値の一致を見る

EXISTS＝存在を見る

結果が同じでも考え方が違う

EXISTSは1件見つかればOK

「値か存在か」で判断する




【対応スキル項目（データエンジニアリング力シート）】

データ基盤

データ操作

★ SQLを用いた基本的
