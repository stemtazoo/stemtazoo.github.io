(() => {
  "use strict";
  const root = document.getElementById("ds-sampling-demo");
  if (!root) return;
  const method = root.querySelector("[data-method]");
  const guess = root.querySelector("[data-guess]");
  const grid = root.querySelector("[data-population]");
  const feedback = root.querySelector("[data-feedback]");
  const count = root.querySelector("[data-count]");
  const breakdown = root.querySelector("[data-breakdown]");
  const draw = root.querySelector("[data-draw]");
  const people = Array.from({ length: 60 }, (_, id) => ({
    id, cluster: Math.floor(id / 10), stratum: id % 3
  }));
  const labels = ["A", "B", "C"];
  const descriptions = {
    simple: { unit: "全員から個人を選ぶ", explain: "60人を一つの名簿として扱い、重複なしで12人を無作為に選びました。" },
    systematic: { unit: "最初を無作為に選び、一定間隔で選ぶ", explain: "最初の位置を1～5番目から無作為に選び、そこから5人おきに計12人を選びました。名簿の並びに周期性がある場合は注意が必要です。" },
    stratified: { unit: "各層から一部ずつ選ぶ", explain: "A・B・Cの各層20人から4人ずつ、合計12人を無作為に選びました。各層を必ず含める比例配分の例です。" },
    cluster: { unit: "選んだ集団の全員を選ぶ", explain: "6グループから2つを無作為に選び、選ばれたグループの全員（合計20人）を調べます。" },
    multistage: { unit: "集団を選んでから個人を選ぶ", explain: "まず6グループから2つを選び、次に各グループの10人から6人ずつ選びます。合計12人です。" }
  };

  function shuffle(items) {
    const values = items.slice();
    for (let i = values.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [values[i], values[j]] = [values[j], values[i]];
    }
    return values;
  }

  function sample() {
    const mode = method.value;
    if (mode === "simple") return shuffle(people).slice(0, 12).map(p => p.id);
    if (mode === "systematic") {
      const start = Math.floor(Math.random() * 5);
      return Array.from({length: 12}, (_, n) => start + n * 5);
    }
    if (mode === "stratified") {
      return labels.flatMap((_, stratum) =>
        shuffle(people.filter(p => p.stratum === stratum)).slice(0, 4).map(p => p.id));
    }
    const groups = shuffle([0, 1, 2, 3, 4, 5]).slice(0, 2);
    if (mode === "cluster") return people.filter(p => groups.includes(p.cluster)).map(p => p.id);
    return groups.flatMap(group =>
      shuffle(people.filter(p => p.cluster === group)).slice(0, 6).map(p => p.id));
  }

  function paint(ids) {
    const selected = new Set(ids);
    grid.replaceChildren();
    for (let group = 0; group < 6; group++) {
      const field = document.createElement("div");
      field.className = "ds-sampling-demo__group";
      const heading = document.createElement("strong");
      heading.textContent = `グループ${group + 1}`;
      field.append(heading);
      const dots = document.createElement("div");
      dots.className = "ds-sampling-demo__dots";
      people.filter(p => p.cluster === group).forEach(p => {
        const cell = document.createElement("span");
        cell.className = "ds-sampling-demo__person" + (selected.has(p.id) ? " is-selected" : "");
        cell.textContent = labels[p.stratum];
        cell.title = `番号${p.id + 1}：層${labels[p.stratum]}${selected.has(p.id) ? "（抽出済み）" : ""}`;
        cell.setAttribute("aria-label", cell.title);
        dots.append(cell);
      });
      field.append(dots);
      grid.append(field);
    }
  }

  function resetDisplay() {
    paint([]);
    count.textContent = "未抽出";
    breakdown.textContent = "抽出ボタンを押すと、選ばれた人を表示します。";
    feedback.textContent = "どの単位を選ぶ方式か予想してみましょう。";
    guess.value = "";
  }

  draw.addEventListener("click", () => {
    const choice = guess.value;
    const ids = sample();
    const selected = new Set(ids);
    const byStratum = labels.map((_, index) =>
      people.filter(p => p.stratum === index && selected.has(p.id)).length);
    paint(ids);
    count.textContent = `${ids.length} / 60人を抽出`;
    breakdown.textContent = `標本の内訳：A ${byStratum[0]}人、B ${byStratum[1]}人、C ${byStratum[2]}人`;
    const detail = descriptions[method.value];
    const judgment = choice ? choice === method.value ? "予想が当たりました。 " : "予想と違いました。 " : "";
    feedback.textContent = judgment + detail.explain;
    guess.value = "";
  });
  method.addEventListener("change", resetDisplay);
  root.querySelector("[data-reset]").addEventListener("click", resetDisplay);
  resetDisplay();
})();
