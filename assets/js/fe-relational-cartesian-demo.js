(() => {
  "use strict";
  function init() {
    document.querySelectorAll("[data-fe-cartesian-demo]").forEach((root) => {
      const r = root.querySelector("[data-cartesian-r]");
      const s = root.querySelector("[data-cartesian-s]");
      const rCount = root.querySelector("[data-cartesian-r-count]");
      const sCount = root.querySelector("[data-cartesian-s-count]");
      const result = root.querySelector("[data-cartesian-result]");
      const guide = root.querySelector("[data-cartesian-guide]");
      const grid = root.querySelector("[data-cartesian-grid]");
      const reset = root.querySelector("[data-cartesian-reset]");
      if (!r || !s || !rCount || !sCount || !result || !guide || !grid || !reset) return;
      function render() {
        const a = Number(r.value);
        const b = Number(s.value);
        rCount.textContent = String(a);
        sCount.textContent = String(b);
        result.textContent = "R " + a + "行 × S " + b + "行 = " + (a * b) + "行";
        guide.textContent = a === 0 || b === 0
          ? "どちらかが0行なので、組合せはありません。"
          : "Rの各行にSの" + b + "行が対応します。";
        grid.replaceChildren();
        grid.style.setProperty("--fe-cartesian-cols", String(Math.max(1, b)));
        if (a === 0 || b === 0) {
          const empty = document.createElement("p");
          empty.textContent = "結果は0行です。";
          grid.appendChild(empty);
        } else {
          for (let i = 1; i <= a; i += 1) {
            for (let j = 1; j <= b; j += 1) {
              const cell = document.createElement("span");
              cell.textContent = "R" + i + "・S" + j;
              if (i % 2 === 0) cell.classList.add("fe-cartesian-demo__alt");
              grid.appendChild(cell);
            }
          }
        }
      }
      r.addEventListener("input", render);
      s.addEventListener("input", render);
      reset.addEventListener("click", () => {
        r.value = "3";
        s.value = "2";
        render();
      });
      render();
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
