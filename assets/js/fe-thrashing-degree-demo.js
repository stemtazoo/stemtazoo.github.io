(() => {
  "use strict";
  const throughput = [25, 48, 68, 80, 76, 62, 43, 27, 17, 10];
  const paging = [2, 4, 7, 11, 20, 38, 57, 75, 89, 97];
  function initialize() {
    document.querySelectorAll("[data-fe-thrashing-degree-demo]").forEach((root) => {
      const slider = root.querySelector("[data-degree-input]");
      const degree = root.querySelector("[data-degree-value]");
      const throughputValue = root.querySelector("[data-degree-throughput]");
      const pagingValue = root.querySelector("[data-degree-paging]");
      const throughputDot = root.querySelector("[data-degree-throughput-dot]");
      const pagingDot = root.querySelector("[data-degree-paging-dot]");
      const cursor = root.querySelector("[data-degree-cursor]");
      const comment = root.querySelector("[data-degree-comment]");
      const reset = root.querySelector("[data-degree-reset]");
      if (![slider, degree, throughputValue, pagingValue, throughputDot, pagingDot, cursor, comment, reset].every(Boolean)) return;
      function render() {
        const index = Math.min(9, Math.max(0, Number(slider.value) - 1));
        const t = throughput[index], p = paging[index];
        const x = 40 + index * (286 / 9);
        degree.textContent = String(index + 1);
        throughputValue.textContent = String(t);
        pagingValue.textContent = String(p);
        cursor.setAttribute("x1", String(x));
        cursor.setAttribute("x2", String(x));
        throughputDot.setAttribute("cx", String(x));
        throughputDot.setAttribute("cy", String(157 - 1.44 * t));
        pagingDot.setAttribute("cx", String(x));
        pagingDot.setAttribute("cy", String(157 - 1.44 * p));
        comment.textContent = index <= 3
          ? "このモデルでは多重度を増やすと処理能力が上がっています。さらに増やすとどうなるでしょうか？"
          : index <= 5
            ? "ページ交換負荷が増え、処理能力が下がり始めました。"
            : "ページ交換負荷が大きく、処理能力は低下しています。スラッシングの傾向です。";
      }
      slider.addEventListener("input", render);
      slider.addEventListener("change", render);
      reset.addEventListener("click", () => {
        slider.value = "4";
        render();
      });
      render();
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initialize);
  else initialize();
})();
