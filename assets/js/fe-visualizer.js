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
});
