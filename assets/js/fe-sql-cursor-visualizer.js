(() => {
  "use strict";

  // FETCH updates host variables; positioned UPDATE changes the current row.
  const employees = [
    { name: "田中", salary: 300000 },
    { name: "佐藤", salary: 350000 },
    { name: "鈴木", salary: 400000 }
  ];
  const steps = [
    { command: "開始前", row: -1, fetched: -1, updated: [], message: "OPEN前です。まだどの行も取り出していません。" },
    { command: "OPEN X", row: -1, fetched: -1, updated: [], message: "カーソルを開きます。まだFETCHしていないので現在行はありません。" },
    { command: "FETCH X INTO :NAME, :SALARY", row: 0, fetched: 0, updated: [], message: "田中さんの行を取得しました。現在行が1行目になります。" },
    { command: "UPDATE ... WHERE CURRENT OF X", row: 0, fetched: 0, updated: [0], message: "現在行の田中さんだけ給与を10%増やします。次の行へは移動しません。" },
    { command: "FETCH X INTO :NAME, :SALARY", row: 1, fetched: 1, updated: [0], message: "佐藤さんの行を取得しました。現在行が2行目に移動します。" },
    { command: "UPDATE ... WHERE CURRENT OF X", row: 1, fetched: 1, updated: [0, 1], message: "現在行の佐藤さんだけ給与を10%増やします。" },
    { command: "FETCH X INTO :NAME, :SALARY", row: 2, fetched: 2, updated: [0, 1], message: "鈴木さんの行を取得しました。現在行が3行目に移動します。" },
    { command: "UPDATE ... WHERE CURRENT OF X", row: 2, fetched: 2, updated: [0, 1, 2], message: "現在行の鈴木さんだけ給与を10%増やします。" },
    { command: "CLOSE X", row: -1, fetched: 2, updated: [0, 1, 2], message: "カーソルを閉じました。取得済みのホスト変数は最後のFETCH時の値を保持します。" }
  ];

  function initialize() {
    document.querySelectorAll("[data-fe-sql-cursor-demo]").forEach((demo) => {
      const rows = Array.from(demo.querySelectorAll("[data-cursor-row]"));
      const command = demo.querySelector("[data-cursor-command]");
      const message = demo.querySelector("[data-cursor-message]");
      const variables = demo.querySelector("[data-cursor-variables]");
      const counter = demo.querySelector("[data-cursor-step]");
      const next = demo.querySelector("[data-cursor-next]");
      const reset = demo.querySelector("[data-cursor-reset]");
      if (rows.length !== employees.length || !command || !message || !variables || !counter || !next || !reset) return;

      let stepIndex = 0;
      function render() {
        const step = steps[stepIndex];
        rows.forEach((row, index) => {
          const updated = step.updated.includes(index);
          const isCurrent = step.row === index;
          row.classList.toggle("is-current", isCurrent);
          row.classList.toggle("is-updated", updated);
          row.querySelector("[data-cursor-salary]").textContent =
            (employees[index].salary * (updated ? 1.1 : 1)).toLocaleString("ja-JP") + "円";
          row.querySelector("[data-cursor-row-state]").textContent =
            (isCurrent ? "▶ 現在行" : "—") + (updated ? "・更新済" : "");
        });
        command.textContent = step.command;
        message.textContent = step.message;
        if (step.fetched >= 0) {
          const fetched = employees[step.fetched];
          variables.textContent = ":NAME = " + fetched.name + "、:SALARY = " + fetched.salary.toLocaleString("ja-JP") + "円";
        } else {
          variables.textContent = "まだFETCHしていません";
        }
        counter.textContent = stepIndex + " / " + (steps.length - 1);
        next.disabled = stepIndex === steps.length - 1;
        reset.disabled = stepIndex === 0;
      }

      next.addEventListener("click", () => {
        if (stepIndex < steps.length - 1) stepIndex += 1;
        render();
      });
      reset.addEventListener("click", () => {
        stepIndex = 0;
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
