/* FE: show why adding 0.5 before floor produces half-up rounding for x >= 0. */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("[data-fe-round-floor-demo]").forEach(function (demo) {
    const slider = demo.querySelector("[data-round-slider]");
    const xEl = demo.querySelector("[data-round-x]");
    const plusEl = demo.querySelector("[data-round-plus]");
    const resultEl = demo.querySelector("[data-round-result]");
    const messageEl = demo.querySelector("[data-round-message]");
    if (!slider || !xEl || !plusEl || !resultEl || !messageEl) return;

    function render() {
      // The slider moves in hundredths, so normalize values for a stable display.
      const x = Math.round(Number(slider.value) * 100) / 100;
      const result = Math.floor(x + 0.5);
      xEl.textContent = x.toFixed(2);
      plusEl.textContent = (x + 0.5).toFixed(2);
      resultEl.textContent = String(result);
      messageEl.textContent = x.toFixed(2) + (x < 2.5
        ? "は2.50未満なので、結果は2です。"
        : "は2.50以上なので、結果は3です。");
    }

    slider.addEventListener("input", render);
    demo.querySelectorAll("[data-round-preset]").forEach(function (button) {
      button.addEventListener("click", function () {
        slider.value = button.getAttribute("data-round-preset");
        render();
      });
    });
    render();
  });
});
