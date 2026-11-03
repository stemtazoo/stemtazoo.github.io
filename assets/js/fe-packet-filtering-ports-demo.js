(function () {
  "use strict";
  const root = document.getElementById("fe-port-demo");
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const service = $("#fe-port-service"), clientPort = $("#fe-port-client");
  const direction = $("#fe-port-direction"), rules = $("#fe-port-rules");
  const guess = $("#fe-port-guess"), check = $("#fe-port-check"), reset = $("#fe-port-reset");
  const from = $("#fe-port-from"), to = $("#fe-port-to"), packet = $("#fe-port-packet");
  const feedback = $("#fe-port-feedback"), verdict = $("#fe-port-verdict"), explanation = $("#fe-port-explanation");
  const rulesText = $("#fe-port-rule-summary");
  const pcIP = "192.0.2.10", serverIP = "198.51.100.20";
  let revealed = false;
  function facts() {
    const srv = Number(service.value), cli = Number(clientPort.value), reply = direction.value === "reply";
    const srcIP = reply ? serverIP : pcIP, dstIP = reply ? pcIP : serverIP;
    const srcPort = reply ? srv : cli, dstPort = reply ? cli : srv;
    const outgoingRule = !reply && srcIP === pcIP && dstIP === serverIP && dstPort === srv;
    const returnRule = reply && srcIP === serverIP && dstIP === pcIP && srcPort === srv && dstPort === cli;
    const allowed = rules.value === "both" ? (outgoingRule || returnRule)
      : rules.value === "outgoing" ? outgoingRule
      : rules.value === "return" ? returnRule : false;
    return {srv,cli,reply,srcIP,dstIP,srcPort,dstPort,allowed,outgoingRule,returnRule};
  }
  function render(message) {
    const f = facts();
    from.replaceChildren();
    const fromTitle = document.createElement("strong");fromTitle.textContent=f.reply ? "Webサーバ" : "PC";
    from.append(fromTitle, document.createTextNode(f.srcIP + ":" + f.srcPort));
    to.replaceChildren();
    const toTitle = document.createElement("strong");toTitle.textContent=f.reply ? "PC" : "Webサーバ";
    to.append(toTitle, document.createTextNode(f.dstIP + ":" + f.dstPort));
    packet.textContent = "TCP／送信元 " + f.srcIP + ":" + f.srcPort + " → 宛先 " + f.dstIP + ":" + f.dstPort;
    const rule1 = "PC→WebサーバのTCP宛先ポート" + f.srv + "を許可";
    const rule2 = "Webサーバ→PCのTCP送信元ポート" + f.srv + "、宛先ポート" + f.cli + "を許可";
    rulesText.textContent = rules.value === "both" ? rule1 + "／" + rule2
      : rules.value === "outgoing" ? rule1 + "のみ"
      : rules.value === "return" ? rule2 + "のみ" : "該当する許可ルールなし（すべて拒否）";
    verdict.textContent = revealed ? (f.allowed ? "判定：許可" : "判定：拒否") : "判定前：まだ結果を表示していません。";
    explanation.textContent = revealed
      ? (f.allowed ? "この向きのパケットは選んだ許可ルールに一致します。" :
        "この向きのパケットに一致する許可ルールがなく、暗黙の拒否で遮断されます。") +
        " 往路は宛先がサービス用ポート、復路は送信元がサービス用ポートです。"
      : "送信元／宛先を確認し、ルールと照合してから判定しましょう。";
    feedback.textContent = message || "通信方向とルールを見て、許可か拒否か予想しましょう。";
  }
  function changed() { revealed=false; guess.value="";render("条件を変更しました。もう一度予想してください。"); }
  [service,clientPort,direction,rules].forEach((field)=>field.addEventListener("change",changed));
  check.addEventListener("click",()=>{
    const f=facts(), prediction=guess.value;
    revealed=true;
    const actual=f.allowed?"allow":"deny";
    const prefix=prediction===""?"予想を省略しました。":prediction===actual?"予想正解！":"予想とは異なりました。";
    render(prefix+" このパケットは"+(f.allowed?"許可":"拒否")+"です。");
  });
  reset.addEventListener("click",()=>{
    service.value="80";clientPort.value="50000";direction.value="request";rules.value="outgoing";
    revealed=false;guess.value="";render("初期状態に戻しました。");
  });
  render();
})();
