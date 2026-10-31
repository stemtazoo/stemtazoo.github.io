(function () {
  "use strict";
  const root = document.getElementById("fe-floating-errors-demo");
  if (!root || root.dataset.initialized === "true") return;
  root.dataset.initialized = "true";

  const modes = {
    rounding: { title: "丸め誤差", label: "保持する有効数字", min: 1, max: 8, initial: 3 },
    loss: { title: "情報落ち", label: "保持する有効数字", min: 3, max: 8, initial: 4 },
    cancellation: { title: "桁落ち", label: "入力値の有効数字", min: 3, max: 8, initial: 6 },
    overflow: { title: "桁あふれ", label: "250に加える整数", min: 1, max: 10, initial: 6 }
  };
  let mode = "rounding";
  const buttons = Array.from(root.querySelectorAll("[data-fe-fpe-mode]"));
  const slider = root.querySelector("#fe-fpe-slider");
  const controlLabel = root.querySelector("#fe-fpe-control-label");
  const controlValue = root.querySelector("#fe-fpe-control-value");
  const input = root.querySelector("#fe-fpe-input");
  const result = root.querySelector("#fe-fpe-result");
  const note = root.querySelector("#fe-fpe-note");
  const reset = root.querySelector("#fe-fpe-reset");

  // 10進の有効数字で丸める教育用モデル。IEEE 754の2進演算を模倣するものではない。
  function roundSig(x, n) { return Number(x.toPrecision(n)); }
  function fmt(x) { return Number.isInteger(x) ? String(x) : String(Number(x.toPrecision(12))); }
  function render() {
    const n = Number(slider.value);
    controlValue.textContent = String(n) + (mode === "overflow" ? "" : "桁");
    if (mode === "rounding") {
      const exact = 1 / 3;
      const stored = roundSig(exact, n);
      input.textContent = "1 ÷ 3 = 0.333333…";
      result.textContent = fmt(stored);
      note.textContent = "正確な値との差：約 " + Math.abs(exact - stored).toExponential(2) + "。桁数を増やすと誤差が小さくなります。";
    } else if (mode === "loss") {
      const exact = 1234 + 0.01;
      const stored = roundSig(exact, n);
      input.textContent = "1234 + 0.01 = 1234.01";
      result.textContent = fmt(stored);
      note.textContent = stored === 1234 ? "小さい 0.01 が結果に反映されません。" : stored === exact ? "0.01 まで保持できました。" : "下位桁の一部が丸められています。";
    } else if (mode === "cancellation") {
      const a = roundSig(1.2345678, n);
      const b = roundSig(1.2345666, n);
      const computed = a - b;
      const exact = 0.0000012;
      input.textContent = "入力A: " + fmt(a) + " ／ 入力B: " + fmt(b) + "（元の値は1.2345678と1.2345666）";
      result.textContent = fmt(Number(computed.toPrecision(8)));
      note.textContent = "本来の差は 0.0000012。入力を先に丸めると、近い値の減算で誤差が目立ちます。差が小さいだけで必ず誤差になるわけではありません。";
    } else {
      const sum = 250 + n;
      input.textContent = "8ビット符号なし整数の範囲：0〜255 ／ 250 + " + n + " = " + sum;
      result.textContent = sum > 255 ? "範囲外（" + sum + "）" : String(sum);
      note.textContent = sum > 255 ? "最大値255を超えました。ここでは折り返し値を仮定しません。" : "255以下なので表現できます。";
    }
  }
  function select(next) {
    mode = next;
    const cfg = modes[mode];
    buttons.forEach(b => { b.setAttribute("aria-pressed", String(b.dataset.feFpeMode === mode)); });
    slider.min = String(cfg.min);
    slider.max = String(cfg.max);
    slider.value = String(cfg.initial);
    controlLabel.textContent = cfg.label;
    render();
  }
  buttons.forEach(b => b.addEventListener("click", () => select(b.dataset.feFpeMode)));
  slider.addEventListener("input", render);
  reset.addEventListener("click", () => select(mode));
  select(mode);
})();
