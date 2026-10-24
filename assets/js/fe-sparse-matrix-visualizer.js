(() => {
  "use strict";

  function initialize() {
    document.querySelectorAll("[data-fe-sparse-demo]").forEach((demo) => {
      const matrixRows = Array.from(demo.querySelectorAll("[data-sparse-row]"));
      const rowOutput = demo.querySelector("[data-sparse-rows]");
      const colOutput = demo.querySelector("[data-sparse-cols]");
      const valOutput = demo.querySelector("[data-sparse-vals]");
      const status = demo.querySelector("[data-sparse-status]");
      const counter = demo.querySelector("[data-sparse-counter]");
      const controls = demo.querySelector("[data-sparse-controls]");
      const next = demo.querySelector("[data-sparse-next]");
      const prev = demo.querySelector("[data-sparse-prev]");
      const reset = demo.querySelector("[data-sparse-reset]");
      if (!matrixRows.length || !rowOutput || !colOutput || !valOutput ||
          !status || !counter || !controls || !next || !prev || !reset) return;

      const entries = [];
      const cells = [];
      matrixRows.forEach((row, i) => {
        row.querySelectorAll("[data-sparse-value]").forEach((cell, j) => {
          const value = Number(cell.textContent.trim());
          cells.push({ cell, value });
          cell.classList.toggle("is-zero", value === 0);
          cell.classList.toggle("is-nonzero", value !== 0);
          if (value !== 0 && Number.isFinite(value)) {
            entries.push({ row: i + 1, col: j + 1, value, cell });
          }
        });
      });
      if (!entries.length || cells.some(({ value }) => !Number.isFinite(value))) return;

      let step = 0;
      function render() {
        const recorded = entries.slice(0, step);
        const current = recorded[recorded.length - 1];
        entries.forEach(({ cell }, index) => {
          cell.classList.toggle("is-completed", index < step - 1);
          cell.classList.toggle("is-current", index === step - 1);
        });
        rowOutput.textContent = recorded.length ? recorded.map((e) => e.row).join(", ") : "まだなし";
        colOutput.textContent = recorded.length ? recorded.map((e) => e.col).join(", ") : "まだなし";
        valOutput.textContent = recorded.length ? recorded.map((e) => e.value).join(", ") : "まだなし";
        status.textContent = current
          ? "行" + current.row + "・列" + current.col + "の値" + current.value +
            "を追加しました。0の場所は記録しません。"
          : "開始前：0以外の値を行の先頭から順に探します。";
        counter.textContent = step + " / " + entries.length + "件";
        prev.disabled = step === 0;
        reset.disabled = step === 0;
        next.disabled = step === entries.length;
      }

      controls.hidden = false;
      next.addEventListener("click", () => {
        step = Math.min(entries.length, step + 1);
        render();
      });
      prev.addEventListener("click", () => {
        step = Math.max(0, step - 1);
        render();
      });
      reset.addEventListener("click", () => {
        step = 0;
        render();
      });
      render();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize);
  } else {
    initialize();
  }
})();
