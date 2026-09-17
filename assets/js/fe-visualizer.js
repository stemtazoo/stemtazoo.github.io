document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-branch-demo]").forEach((demo) => {
    const rates = {
      A: Number(demo.dataset.rateA || 0),
      B: Number(demo.dataset.rateB || 0),
      C: Number(demo.dataset.rateC || 0),
    };

    const buttons = Array.from(demo.querySelectorAll("[data-order]"));
    const steps = Array.from(demo.querySelectorAll("[data-step]"));
    const average = demo.querySelector("[data-average]");
    const total = demo.querySelector("[data-total-comparisons]");
    const breakdown = demo.querySelector("[data-breakdown]");

    function render(order) {
      const first = order[0];
      const firstRate = rates[first];
      const remainingRate = 100 - firstRate;
      const averageComparisons = (firstRate + remainingRate * 2) / 100;
      const totalComparisons = firstRate + remainingRate * 2;

      buttons.forEach((button) => {
        const selected = button.dataset.order.split(",")[0] === first;
        button.setAttribute("aria-pressed", String(selected));
      });

      steps.forEach((step, index) => {
        const category = order[index];
        step.classList.toggle("is-first", index === 0);
        step.innerHTML = index === 0
          ? `<strong>${category}区分 ${rates[category]}%</strong><br>1回で判定`
          : `<strong>${category}区分 ${rates[category]}%</strong><br>2回で判定`;
      });

      if (average) {
        average.textContent = `${averageComparisons.toFixed(1)}回`;
      }

      if (total) {
        total.textContent = `${totalComparisons}回`;
      }

      if (breakdown) {
        breakdown.innerHTML = `
          <li>${first}区分 ${firstRate}件 × 1回 = ${firstRate}回</li>
          <li>残り ${remainingRate}件 × 2回 = ${remainingRate * 2}回</li>
        `;
      }
    }

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        render(button.dataset.order.split(","));
      });
    });

    if (buttons.length > 0) {
      render(buttons[0].dataset.order.split(","));
    }
  });

  document.querySelectorAll("[data-fe-binary-demo]").forEach((demo) => {
    const values = (demo.dataset.values || "").split(",").map(Number);
    const target = Number(demo.dataset.target);
    const cells = Array.from(demo.querySelectorAll("[data-binary-cell]"));
    const nextButton = demo.querySelector("[data-binary-next]");
    const resetButton = demo.querySelector("[data-binary-reset]");
    const status = demo.querySelector("[data-binary-status]");
    const leftLabel = demo.querySelector("[data-binary-left]");
    const midLabel = demo.querySelector("[data-binary-mid]");
    const rightLabel = demo.querySelector("[data-binary-right]");
    const countLabel = demo.querySelector("[data-binary-count]");

    let left;
    let right;
    let comparisons;
    let finished;

    function paint(mid = null, found = false) {
      cells.forEach((cell, index) => {
        const active = index >= left && index <= right;
        cell.classList.toggle("is-discarded", !active);
        cell.classList.toggle("is-mid", index === mid);
        cell.classList.toggle("is-found", found && index === mid);
      });

      if (leftLabel) leftLabel.textContent = String(left);
      if (rightLabel) rightLabel.textContent = String(right);
      if (midLabel) midLabel.textContent = mid === null ? "-" : String(mid);
      if (countLabel) countLabel.textContent = `${comparisons}回`;
    }

    function reset() {
      left = 0;
      right = values.length - 1;
      comparisons = 0;
      finished = false;
      paint();
      if (status) status.textContent = `探す値は ${target}。まず探索範囲の中央を確認します。`;
      if (nextButton) {
        nextButton.disabled = false;
        nextButton.textContent = "次の比較";
      }
    }

    function step() {
      if (finished || left > right) return;

      const mid = Math.floor((left + right) / 2);
      const value = values[mid];
      comparisons += 1;

      if (value === target) {
        finished = true;
        paint(mid, true);
        if (status) status.innerHTML = `<strong>${comparisons}回目：</strong> a[${mid}] = ${value}。探している ${target} と一致したので発見です。`;
        if (nextButton) {
          nextButton.disabled = true;
          nextButton.textContent = "見つかりました";
        }
        return;
      }

      if (target > value) {
        if (status) status.innerHTML = `<strong>${comparisons}回目：</strong> a[${mid}] = ${value}。${target} は ${value} より大きいので、左側を捨てます。`;
        left = mid + 1;
      } else {
        if (status) status.innerHTML = `<strong>${comparisons}回目：</strong> a[${mid}] = ${value}。${target} は ${value} より小さいので、右側を捨てます。`;
        right = mid - 1;
      }

      paint(mid);
      window.setTimeout(() => paint(), 180);
    }

    if (nextButton) nextButton.addEventListener("click", step);
    if (resetButton) resetButton.addEventListener("click", reset);
    reset();
  });

  document.querySelectorAll("[data-fe-adj-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-adj-edge]"));
    const lines = Array.from(demo.querySelectorAll("[data-graph-edge]"));
    const status = demo.querySelector("[data-adj-status]");
    const initial = new Set(["12", "13", "24", "34"]);
    const active = new Set(initial);

    function render() {
      buttons.forEach((button) => {
        const edge = button.dataset.adjEdge;
        const on = active.has(edge);
        button.textContent = on ? "1" : "0";
        button.setAttribute("aria-pressed", String(on));
      });

      lines.forEach((line) => {
        line.classList.toggle("is-off", !active.has(line.dataset.graphEdge));
      });

      if (status) {
        const edges = Array.from(active).sort().map((edge) => `V${edge[0]}―V${edge[1]}`);
        status.innerHTML = edges.length
          ? `<strong>現在の辺：</strong> ${edges.join("、")}`
          : "現在、辺はありません。";
      }
    }

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        const edge = button.dataset.adjEdge;
        if (active.has(edge)) active.delete(edge);
        else active.add(edge);
        render();
      });
    });

    const reset = demo.querySelector("[data-adj-reset]");
    if (reset) {
      reset.addEventListener("click", () => {
        active.clear();
        initial.forEach((edge) => active.add(edge));
        render();
      });
    }

    render();
  });
});
