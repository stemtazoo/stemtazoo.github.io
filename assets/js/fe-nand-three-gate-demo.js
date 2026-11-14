(() => {
  "use strict";
  const nand = (a, b) => Number(!(a && b));
  function initialize() {
    document.querySelectorAll("[data-fe-nand3]").forEach((root) => {
      const inputs = ["p", "q", "r", "s"].map((name) => root.querySelector('[data-nand3-input="' + name + '"]'));
      const run = root.querySelector("[data-nand3-run]");
      const reset = root.querySelector("[data-nand3-reset]");
      const result = root.querySelector("[data-nand3-result]");
      if (inputs.some((input) => !input) || !run || !reset || !result) return;
      const show = (lines) => {
        result.replaceChildren();
        lines.forEach((line) => {
          const p = document.createElement("p");
          p.textContent = line;
          result.appendChild(p);
        });
      };
      const clear = () => show(["入力が変わりました。最終出力を予想してから「回路を計算」を押してください。"]);
      inputs.forEach((input) => input.addEventListener("change", clear));
      run.addEventListener("click", () => {
        const [p, q, r, s] = inputs.map((input) => Number(input.value));
        const u = nand(p, q);
        const v = nand(r, s);
        const x = nand(u, v);
        const simplified = Number(Boolean(p && q) || Boolean(r && s));
        show([
          "① U = NAND(P,Q) = NAND(" + p + "," + q + ") = " + u,
          "② V = NAND(R,S) = NAND(" + r + "," + s + ") = " + v,
          "③ X = NAND(U,V) = NAND(" + u + "," + v + ") = " + x,
          "論理式 P・Q + R・S = " + simplified + "。Xと一致します。",
          x === 1 ? "P・QとR・Sの少なくとも一方が1なので、X=1です。" : "P・QとR・Sの両方が0なので、X=0です。"
        ]);
      });
      reset.addEventListener("click", () => {
        [1, 1, 0, 0].forEach((value, i) => { inputs[i].value = String(value); });
        show(["初期状態（P=1、Q=1、R=0、S=0）に戻しました。結果を予想して実行してください。"]);
      });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initialize);
  else initialize();
})();
