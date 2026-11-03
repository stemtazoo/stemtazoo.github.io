(function () {
  "use strict";
  const root = document.getElementById("fe-twos-demo");
  if (!root) return;
  const $ = (q) => root.querySelector(q);
  const bits = $("#fe-twos-input"), preset = $("#fe-twos-preset"), prediction = $("#fe-twos-prediction");
  const next = $("#fe-twos-next"), back = $("#fe-twos-back"), reset = $("#fe-twos-reset");
  const display = $("#fe-twos-bits"), stageText = $("#fe-twos-stage"), reason = $("#fe-twos-reason");
  const output = $("#fe-twos-output"), result = $("#fe-twos-result"), feedback = $("#fe-twos-feedback");
  const error = $("#fe-twos-error");
  let stage = 0;
  const valid = (s) => /^[01]{8}$/.test(s);
  const binary = (n) => (n & 255).toString(2).padStart(8, "0");
  const signed = (n) => n >= 128 ? n - 256 : n;
  const invert = (s) => s.replace(/[01]/g, (c) => c === "0" ? "1" : "0");
  const transformed = (s) => binary(parseInt(invert(s), 2) + 1);

  function render(message) {
    const source = bits.value.trim();
    const ok = valid(source);
    bits.setAttribute("aria-invalid", String(!ok));
    error.textContent = ok ? "" : "0と1を8桁入力してください（例：00110110）。";
    error.hidden = ok;
    next.disabled = !ok || stage === 2;
    back.disabled = !ok || stage === 0;
    prediction.disabled = !ok || stage === 2;
    next.textContent = stage === 0 ? "次へ：全ビット反転" : stage === 1 ? "次へ：1を加える" : "完了";
    if (!ok) {
      display.replaceChildren();
      stageText.textContent = "入力を確認してください。";
      output.textContent = "—";
      reason.textContent = "8ビットの入力がそろうと、操作できます。";
      result.textContent = "—";
      feedback.textContent = "入力を修正してください。";
      return;
    }
    const first = invert(source);
    const final = transformed(source);
    const shown = stage === 0 ? source : stage === 1 ? first : final;
    display.replaceChildren(...shown.split("").map((b, i) => {
      const span = document.createElement("span");
      span.className = "fe-twos-demo__bit";
      span.textContent = b;
      span.setAttribute("data-sign", String(i === 0));
      span.setAttribute("data-changed", String(stage > 0 && source[i] !== b));
      return span;
    }));
    stageText.textContent = ["① 元の8ビット", "② 全ビットを反転した結果（1の補数）", "③ 1を加えた結果（2の補数）"][stage];
    output.textContent = shown;
    const originalSigned = signed(parseInt(source, 2));
    if (stage === 0) {
      reason.textContent = "まず各ビットの0と1を入れ替えます。結果を確認してから1を加えます。";
      result.textContent = "符号付き整数としての元の値：" + originalSigned;
    } else if (stage === 1) {
      reason.textContent = "ここではまだ1の補数です。2の補数にするには、さらに1を加えます。";
      result.textContent = "最終結果はまだ表示していません。";
    } else {
      const unsigned = parseInt(final, 2);
      const value = signed(unsigned);
      const boundary = source === "10000000"
        ? "注意：-128は8ビットで符号反転しても-128のままです。+128は8ビットの符号付き整数では表せません。"
        : source === "00000000"
          ? "注意：0は反転して1を加えても0です。9ビット目への桁上がりは捨てます。"
          : "8ビットを超える桁上がりは捨て、下位8ビットを結果とします。";
      reason.textContent = "反転したビット列に1を加えました。" + boundary;
      result.textContent = "変換結果の符号付き整数：" + value + "（元は" + originalSigned + "）";
    }
    feedback.textContent = message || (stage === 2 ? "変換完了です。" : "次の結果を予想して進みましょう。");
  }
  function restart() {
    stage = 0;
    prediction.value = "";
    render("最初の状態です。変換後のビット列を予想しましょう。");
  }
  preset.addEventListener("change", () => { bits.value = preset.value; restart(); });
  bits.addEventListener("input", () => { preset.value = ""; restart(); });
  prediction.addEventListener("input", () => { if (stage < 2) render(); });
  next.addEventListener("click", () => {
    if (!valid(bits.value.trim()) || stage === 2) return;
    stage++;
    if (stage === 2) {
      const expected = transformed(bits.value.trim());
      const guessed = prediction.value.trim();
      render(!guessed ? "予想を省略して結果を表示しました。" :
        guessed === expected ? "予想正解！ 2の補数が一致しました。" :
          "予想とは異なりました。ビット反転と＋1を見直しましょう。");
    } else render("全ビットを反転しました。次は1を加えます。");
  });
  back.addEventListener("click", () => {
    if (stage === 0) return;
    stage--;
    render("1ステップ戻しました。");
  });
  reset.addEventListener("click", restart);
  render();
})();
