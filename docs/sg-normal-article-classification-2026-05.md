# SG通常記事の「例題依存度」仕分け（2026-05-18）

## 目的

`pages/sg` の通常記事について、
「特定の選択肢付き確認問題に依存して見えるか」を観点に、次の2区分で棚卸しした。

1. ほぼ1問解説に依存（相対的に強い）
2. 用語解説が主で例題は補助

## 判定方針

- 本文全体に占める解説パート（定義・誤解・判断基準）の厚み
- `## 確認問題（SG試験対策）` の位置と比重
- 「SG試験での判断ポイント」「混同回避」の独立セクション有無

> 注: 本判定は「通常記事の中での相対評価」。
> いずれも SG 学習記事として有効であり、問題専用記事と断定するものではない。

## 1) ほぼ1問解説に依存（相対的に強い）

- `pages/sg/ips.md`
- `pages/sg/dmz.md`
- `pages/sg/sandbox.md`
- `pages/sg/botnet.md`
- `pages/sg/vishing.md`
- `pages/sg/clickjacking.md`
- `pages/sg/port-number.md`

### 改善方針（通常解説寄りへ戻す）

- `## どんな場面で使う？` に「現場判断（導入可否・運用の注意）」を2〜3論点追加
- `## よくある誤解・混同` に「似た用語との切り分け軸」を明示（役割・層・対象・タイミング）
- 可能なら `## SG試験での判断ポイント` を独立見出し化し、確認問題はその検算位置に固定

## 2) 用語解説が主で例題は補助

- `pages/sg/security-testing-types.md`
- `pages/sg/static-dynamic-analysis.md`
- `pages/sg/dast.md`
- `pages/sg/sast.md`
- `pages/sg/vulnerability-assessment-penetration-test.md`
- `pages/sg/psk-wireless-auth.md`
- `pages/sg/xml-signature.md`
- `pages/sg/pki.md`
- `pages/sg/authorization.md`
- `pages/sg/access-control-physical.md`
- `pages/sg/security-patch.md`
- `pages/sg/aes.md`
- `pages/sg/hybrid-cryptography.md`
- `pages/sg/public-key-cryptography.md`
- `pages/sg/sg_apt_attack.md`
- `pages/sg/sg-arp-spoofing.md`
- `pages/sg/tamper-detection.md`
- `pages/sg/unauthorized-access.md`
- `pages/sg/unauthorized-access-related-actions.md`
- `pages/sg/identification-code.md`
- `pages/sg/phishing.md`
- `pages/sg/confidentiality-obligation.md`

## 次アクション（小さい順）

1. 上記「依存強め」7本だけを優先し、各記事に追記する解説論点を先に設計する。
2. 1本ずつ最小差分で改稿し、`last_modified_at` を更新する。
3. レイアウトや Liquid は触らず、GitHub Pages 互換性リスクを増やさない。
