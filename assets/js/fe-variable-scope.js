/* Scope trace for the original FE teaching example; explicit scenario assumption. */
(() => {
  "use strict";
  const states = [
    { line: "大域stockを4で宣言", global: "4", local: "未宣言", output: "まだ出力なし", explain: "最初は共通のstockだけが存在します。" },
    { line: "inspect: stock ← 9", global: "9", local: "未宣言", output: "まだ出力なし", explain: "この教材の前提では、局所宣言前なので大域stockへ9を代入します。" },
    { line: "inspect: stock を出力する", global: "9", local: "未宣言", output: "9", explain: "大域stockの9が出力されました。" },
    { line: "inspect: 整数型: stock ← 2", global: "9", local: "2", output: "9", explain: "新しい局所stockを2で宣言。大域stockは9のままです。" },
    { line: "inspect: stock を出力する", global: "9", local: "2", output: "9 → 2", explain: "この教材の前提では、局所stockの2を出力します。" },
    { line: "report: stock を出力する", global: "9", local: "終了", output: "9 → 2 → 9", explain: "inspectは終了。reportには同名の局所宣言がないため大域stockの9を出力します。" }
  ];
  function setup(root) {
    const find = (name) => root.querySelector('[data-scope-' + name + ']');
    const back = find('back'), next = find('next'), reset = find('reset');
    const names = ["line", "global", "local", "output", "explain"];
    if (!back || !next || !reset || names.some((name) => !find(name))) return;
    let step = 0;
    function render() {
      const current = states[step];
      names.forEach((name) => { find(name).textContent = current[name]; });
      back.disabled = step === 0;
      next.disabled = step === states.length - 1;
    }
    back.addEventListener("click", () => { step = Math.max(0, step - 1); render(); });
    next.addEventListener("click", () => { step = Math.min(states.length - 1, step + 1); render(); });
    reset.addEventListener("click", () => { step = 0; render(); });
    render();
  }
  document.querySelectorAll("[data-fe-scope-demo]").forEach(setup);
})();
