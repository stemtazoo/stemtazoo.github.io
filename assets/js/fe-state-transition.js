(() => {
  "use strict";
  const root = document.getElementById("fe-state-demo");
  if (!root) return;

  const states = ["停止中", "運転中", "異常停止"];
  const transitions = [
    { from: "停止中", event: "起動", to: "運転中" },
    { from: "運転中", event: "異常検知", to: "異常停止" },
    { from: "異常停止", event: "リセット", to: "停止中" }
  ];
  let current = "停止中";
  let records = [];
  const currentEl = root.querySelector("[data-current]");
  const historyEl = root.querySelector("[data-history]");
  const statusEl = root.querySelector("[data-feedback]");
  const guessEl = root.querySelector("[data-guess]");
  const buttons = root.querySelectorAll("[data-event]");

  function render(activeTransition = null) {
    currentEl.textContent = current;
    root.querySelectorAll("[data-state]").forEach((node) => {
      const active = node.dataset.state === current;
      node.classList.toggle("is-current", active);
      node.setAttribute("aria-current", active ? "step" : "false");
    });
    root.querySelectorAll("[data-transition]").forEach((node) => {
      node.classList.toggle("is-traversed", node.dataset.transition === activeTransition);
    });
    historyEl.replaceChildren();
    if (!records.length) {
      const li = document.createElement("li");
      li.textContent = "まだ操作していません。";
      historyEl.append(li);
    } else {
      records.forEach((record, index) => {
        const li = document.createElement("li");
        li.textContent = `${index + 1}. ${record}`;
        historyEl.append(li);
      });
    }
  }

  buttons.forEach((button) => button.addEventListener("click", () => {
    const event = button.dataset.event;
    const transition = transitions.find((item) => item.from === current && item.event === event);
    const prediction = guessEl.value;
    const before = current;
    if (transition) {
      current = transition.to;
      records.push(`${before} ─${event}→ ${current}`);
      statusEl.textContent = (prediction
        ? prediction === current ? "予想どおりです。 " : `予想は「${prediction}」でした。 `
        : "") + `「${before}」から「${event}」の矢印をたどり、「${current}」へ移りました。`;
      render(`${before}:${event}`);
    } else {
      statusEl.textContent = `「${before}」から「${event}」の矢印はこの図にありません。図に指定のない動作は決めつけません。`;
      render();
    }
    guessEl.value = "";
  }));

  root.querySelector("[data-reset]").addEventListener("click", () => {
    current = states[0];
    records = [];
    guessEl.value = "";
    statusEl.textContent = "初期状態は「停止中」です。次の状態を予想してからイベントを押しましょう。";
    render();
  });
  render();
})();