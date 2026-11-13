(() => {
  "use strict";
  function init() {
    document.querySelectorAll("[data-fe-decision-table-demo]").forEach((root) => {
      const hot = root.querySelector("[data-dt-hot]");
      const vibration = root.querySelector("[data-dt-vibration]");
      const cells = Array.from(root.querySelectorAll("[data-dt-col]"));
      const result = root.querySelector("[data-dt-result]");
      const reset = root.querySelector("[data-dt-reset]");
      if (!hot || !vibration || !cells.length || !result || !reset) return;
      function render() {
        const rule = (hot.checked ? 1 : 0) + (vibration.checked ? 2 : 0);
        const actions = ["通常運転", "警告を出す", "警告を出す", "設備を停止"];
        cells.forEach((cell) => {
          const active = Number(cell.dataset.dtCol) === rule;
          cell.classList.toggle("is-active", active);
          if (cell.tagName === "TH") {
            if (active) cell.setAttribute("aria-current", "true");
            else cell.removeAttribute("aria-current");
          }
        });
        result.textContent = "R" + (rule + 1) + "：温度は" + (hot.checked ? "高い" : "正常") +
          "・振動は" + (vibration.checked ? "大きい" : "正常") + " → " + actions[rule];
      }
      hot.addEventListener("change", render);
      vibration.addEventListener("change", render);
      reset.addEventListener("click", () => {
        hot.checked = false;
        vibration.checked = false;
        render();
      });
      render();
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
