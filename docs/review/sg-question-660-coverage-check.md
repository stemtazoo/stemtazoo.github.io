# SG第660問（Smurf攻撃）対応チェック

- 例題論点:
  - Smurf攻撃はDoS系攻撃の一種で、ICMP echo request/replyの仕組みを悪用する。
  - 選択肢切り分けは「ICMP応答大量送信（Smurf）」「SYN大量送信（SYN Flood）」「大きいUDP大量送信（UDP Flood）」「大量メール送信（メールボム）」。
- 既存記事状況:
  - `pages/sg/flood-attack.md` にICMP Flood / SYN Floodの切り分けがあり、問660の誤答排除（イ・ウ）に対応可能。
  - `pages/sg/ddos-attack-summary.md` にDoS/DDoSの分類整理があり、可用性低下攻撃としての位置付けを補強可能。
  - ただし、`Smurf` という固有語と「送信元偽装＋ブロードキャスト＋多数端末のecho reply集中」の説明は独立見出しで未整理。
- 判定:
  - 既存記事に追記推奨。
- 推奨対応:
  - `pages/sg/flood-attack.md` に「Smurf攻撃（ICMP反射型）」の小見出しを追加し、
    - 送信元IP偽装
    - ブロードキャスト宛echo request
    - 多数端末から被害者へecho reply集中
    の3点を明記する。
