(function () {
  "use strict";
  const root = document.getElementById("fe-parity-demo");
  if (!root) return;
  const $ = (q) => root.querySelector(q);
  const data = $("#fe-parity-data"), preset = $("#fe-parity-preset"), mode = $("#fe-parity-mode");
  const guessBit = $("#fe-parity-guess-bit"), guessDetect = $("#fe-parity-guess-detect");
  const sendButton = $("#fe-parity-send"), checkButton = $("#fe-parity-check");
  const noError = $("#fe-parity-none"), single = $("#fe-parity-one"), double = $("#fe-parity-two");
  const reset = $("#fe-parity-reset"), sentBits = $("#fe-parity-sent"), recvBits = $("#fe-parity-received");
  const sentText = $("#fe-parity-sent-text"), recvText = $("#fe-parity-received-text");
  const info = $("#fe-parity-info"), feedback = $("#fe-parity-feedback"), verdict = $("#fe-parity-verdict");
  const error = $("#fe-parity-error");
  const valid = (s) => /^[01]{7}$/.test(s);
  const countOnes = (s) => s.split("").filter((c) => c === "1").length;
  const parityBit = (s, kind) => String((countOnes(s) + (kind === "odd" ? 1 : 0)) % 2);
  const makeBits = (target, value, flipped) => {
    target.replaceChildren(...value.split("").map((v, i) => {
      const span = document.createElement("span");
      span.className = "fe-parity-demo__bit";
      span.textContent = v;
      span.setAttribute("data-parity", String(i === 0));
      span.setAttribute("data-flipped", String(flipped.includes(i)));
      return span;
    }));
  };
  let stage = 0, sent = "", received = "", flipped = [];
  function refresh(message) {
    const raw = data.value.trim(), ok = valid(raw);
    data.setAttribute("aria-invalid", String(!ok));
    error.hidden = ok;
    error.textContent = ok ? "" : "0と1で7桁入力してください（例：1011010）。";
    sendButton.disabled = !ok || stage !== 0;
    [noError, single, double].forEach((b) => { b.disabled = stage === 0; });
    checkButton.disabled = stage === 0;
    guessBit.disabled = stage !== 0 || !ok;
    guessDetect.disabled = stage === 0;
    sentText.textContent = stage === 0 ? "送信前（予想して送信ボタンを押してください）" : sent;
    recvText.textContent = stage === 0 ? "受信前" : received;
    makeBits(sentBits, stage === 0 ? "--------" : sent, []);
    makeBits(recvBits, stage === 0 ? "--------" : received, flipped);
    info.textContent = stage === 0
      ? (ok ? "元データの1の個数：" + countOnes(raw) + "個。追加するパリティビットを予想しましょう。" : "7ビットの値を修正してください。")
      : stage === 1 ? "先頭の1ビットがパリティビットです。誤りを入れてから受信側で確認しましょう。"
      : "受信側で1の総数を調べました。送信時の規則を満たすか確認しましょう。";
    if (stage === 2) {
      const ones = countOnes(received);
      const detectable = (ones % 2) !== (mode.value === "odd" ? 1 : 0);
      verdict.textContent = "受信側の1：" + ones + "個。結果：" +
        (detectable ? "誤りを検出しました。" : "パリティ検査では誤りを検出しませんでした。") +
        (flipped.length === 2 ? " 2ビット反転したため、誤りがあっても偶奇は変わりません。" : "") +
        (flipped.length === 0 ? " この例では誤りを加えていません。" : "") +
        (flipped.length === 1 ? " 1ビット反転すると偶奇が変わります。" : "") +
        " ※パリティが一致しても無誤りの保証にはなりません。";
    } else verdict.textContent = stage === 1 ? "受信側の判定はまだ表示していません。" : "送信前です。";
    feedback.textContent = message || (stage === 0 ? "パリティビットを予想しましょう。" : "誤りを入れ、検出できるか予想しましょう。");
  }
  function restart(message) {
    stage = 0; sent = ""; received = ""; flipped = [];
    guessBit.value = ""; guessDetect.value = "";
    refresh(message || "最初から始めます。");
  }
  data.addEventListener("input", () => { preset.value = ""; restart("入力を変更しました。"); });
  preset.addEventListener("change", () => { data.value = preset.value; restart("データの例を選びました。"); });
  mode.addEventListener("change", () => restart("パリティ方式を変更しました。"));
  sendButton.addEventListener("click", () => {
    const raw = data.value.trim();
    if (!valid(raw) || stage !== 0) return;
    const bit = parityBit(raw, mode.value), predicted = guessBit.value;
    sent = bit + raw; received = sent; stage = 1; flipped = [];
    const prefix = predicted === "" ? "予想を省略しました。" :
      predicted === bit ? "予想正解！" : "予想とは異なりました。";
    refresh(prefix + " パリティビットは" + bit + "、送信する8ビットは" + sent + "です。");
  });
  function inject(indices) {
    if (stage === 0) return;
    received = sent.split("").map((c, i) => indices.includes(i) ? (c === "0" ? "1" : "0") : c).join("");
    flipped = indices.slice(); stage = 1; guessDetect.value = "";
    refresh(indices.length ? indices.length + "ビット反転しました。受信側で検出できるか予想してください。" :
      "誤りを入れない状態に戻しました。");
  }
  noError.addEventListener("click", () => inject([]));
  single.addEventListener("click", () => inject([3]));
  double.addEventListener("click", () => inject([3, 6]));
  checkButton.addEventListener("click", () => {
    if (stage === 0) return;
    const detectable = (countOnes(received) % 2) !== (mode.value === "odd" ? 1 : 0);
    const guess = guessDetect.value;
    stage = 2;
    const result = guess === "" ? "予想を省略しました。" :
      (guess === (detectable ? "yes" : "no") ? "予想正解！" : "予想とは異なりました。");
    refresh(result + " 受信側のパリティを確認しました。");
  });
  reset.addEventListener("click", () => restart());
  refresh();
})();
