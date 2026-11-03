(function () {
  "use strict";
  const root = document.getElementById("fe-port-demo");
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const service = $("#fe-port-service"), clientPort = $("#fe-port-client");
  const direction = $("#fe-port-direction"), protocol = $("#fe-port-protocol");
  const guess = $("#fe-port-guess"), check = $("#fe-port-check"), reset = $("#fe-port-reset");
  const from = $("#fe-port-from"), to = $("#fe-port-to"), packet = $("#fe-port-packet");
  const feedback = $("#fe-port-feedback"), verdict = $("#fe-port-verdict"), explanation = $("#fe-port-explanation");
  const pcIP = "192.0.2.10", serverIP = "198.51.100.20";
  // These rules are FIXED. User input changes only the packet to be tested.
  // All six header fields must match the same allow rule. Everything else is denied.
  const fixedRules = [
    { id: "R1", proto: "TCP", srcIP: pcIP, srcPort: 50000, dstIP: serverIP, dstPort: 80 },
    { id: "R2", proto: "TCP", srcIP: serverIP, srcPort: 80, dstIP: pcIP, dstPort: 50000 },
    { id: "R3", proto: "TCP", srcIP: pcIP, srcPort: 51000, dstIP: serverIP, dstPort: 443 }
  ];
  const fields = [
    ["proto", "プロトコル"], ["srcIP", "送信元IP"], ["srcPort", "送信元ポート"],
    ["dstIP", "宛先IP"], ["dstPort", "宛先ポート"]
  ];
  let revealed = false;
  function facts() {
    const srv = Number(service.value), cli = Number(clientPort.value);
    const reply = direction.value === "reply";
    return {
      proto: protocol.value,
      srcIP: reply ? serverIP : pcIP,
      srcPort: reply ? srv : cli,
      dstIP: reply ? pcIP : serverIP,
      dstPort: reply ? cli : srv,
      reply
    };
  }
  function decide(f) {
    const matched = fixedRules.find((r) => fields.every(([key]) => r[key] === f[key]));
    return { matched, allowed: Boolean(matched) };
  }
  function explainMismatch(f) {
    const comparisons = fixedRules.map((r) => ({
      rule: r, mismatches: fields.filter(([key]) => r[key] !== f[key]).map(([,label]) => label)
    }));
    // The nearest rule is a concrete diagnostic, not a different allow policy.
    comparisons.sort((a,b) => a.mismatches.length - b.mismatches.length);
    const closest = comparisons[0];
    return "許可ルールに完全一致しません。近い" + closest.rule.id +
      "と異なる条件：" + closest.mismatches.join("・") + "。暗黙の拒否です。";
  }
  function render(message) {
    const f = facts(), outcome = decide(f);
    from.replaceChildren();
    const fromTitle = document.createElement("strong");
    fromTitle.textContent = f.reply ? "Webサーバ" : "PC";
    from.append(fromTitle, document.createTextNode(f.srcIP + ":" + f.srcPort));
    to.replaceChildren();
    const toTitle = document.createElement("strong");
    toTitle.textContent = f.reply ? "PC" : "Webサーバ";
    to.append(toTitle, document.createTextNode(f.dstIP + ":" + f.dstPort));
    packet.textContent = f.proto + "／送信元 " + f.srcIP + ":" + f.srcPort +
      " → 宛先 " + f.dstIP + ":" + f.dstPort;
    verdict.textContent = revealed ? (outcome.allowed ? "判定：許可" : "判定：拒否")
      : "判定前：まだ結果を表示していません。";
    explanation.textContent = revealed
      ? (outcome.allowed ? "固定ルール" + outcome.matched.id + "のプロトコル・送信元・宛先がすべて一致しました。"
        : explainMismatch(f))
      : "上の固定ルール表とパケットの各項目を照合しましょう。ルール表は変更されません。";
    root.querySelectorAll("[data-fe-port-rule]").forEach((row) => {
      row.removeAttribute("data-matched");
      if (revealed && outcome.matched && row.getAttribute("data-fe-port-rule") === outcome.matched.id) {
        row.setAttribute("data-matched", "true");
      }
    });
    feedback.textContent = message || "固定ルール表と比較して許可・拒否を予想しましょう。";
  }
  function changed() { revealed = false; guess.value = ""; render("パケット条件を変更しました。再度ルールと照合してください。"); }
  [service, clientPort, direction, protocol].forEach((field) => field.addEventListener("change", changed));
  check.addEventListener("click", () => {
    const decision = decide(facts()), prediction = guess.value;
    revealed = true;
    const actual = decision.allowed ? "allow" : "deny";
    const prefix = prediction === "" ? "予想を省略しました。"
      : prediction === actual ? "予想正解！" : "予想とは異なりました。";
    render(prefix + " このパケットは" + (decision.allowed ? "許可" : "拒否") + "です。");
  });
  reset.addEventListener("click", () => {
    service.value = "80"; clientPort.value = "50000"; direction.value = "request"; protocol.value = "TCP";
    revealed = false; guess.value = ""; render("初期状態に戻しました。");
  });
  render();
})();
