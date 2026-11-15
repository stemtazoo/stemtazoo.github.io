(() => {
  "use strict";
  const root = document.getElementById("fe-return-condition-demo");
  if (!root) return;
  const xInput = root.querySelector("#fe-return-x");
  const operationInput = root.querySelector("#fe-return-operation");
  const button = root.querySelector("#fe-return-check");
  const result = root.querySelector("#fe-return-result");
  const before = root.querySelector("#fe-return-before");
  const after = root.querySelector("#fe-return-after");
  const sum = root.querySelector("#fe-return-sum");
  const judgment = root.querySelector("#fe-return-judgment");
  const bits = (n) => n.toString(2).padStart(8, "0");
  const reset = () => {
    result.hidden = true;
    before.textContent = "";
    after.textContent = "";
    sum.textContent = "";
    judgment.textContent = "";
  };
  xInput.addEventListener("change", reset);
  operationInput.addEventListener("change", reset);
  button.addEventListener("click", () => {
    const x = Number(xInput.value);
    const initial = operationInput.value === "or" ? (x | 255) : (x ^ 255);
    const y = (initial + 1) & 255;
    const total = (x + y) & 255;
    const ok = total === 0;
    before.textContent = bits(initial) + "（" + initial + "）";
    after.textContent = bits(y) + "（" + y + "）";
    sum.textContent = bits(total) + "（" + total + "）";
    judgment.textContent = ok
      ? "条件を満たします。戻り値自体が0でなくても、xに足した結果が0なら正しいです。"
      : "条件を満たしません。計算自体は正しくても、xに足すと0になりません。";
    result.hidden = false;
  });
})();
