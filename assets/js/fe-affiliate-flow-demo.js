(() => {
  "use strict";
  const messages = [
    "ステップ1 / 5：媒体運営者が広告リンクを掲載します。",
    "ステップ2 / 5：閲覧者が広告リンクをクリックします。",
    "ステップ3 / 5：閲覧者が広告主の通販サイトで商品を購入します。",
    "ステップ4 / 5：広告主などが所定の成果条件を確認・承認します。",
    "ステップ5 / 5：広告主から媒体運営者へ成果報酬が支払われます（ASP経由の場合もあります）。"
  ];
  function init() {
    document.querySelectorAll("[data-fe-affiliate-demo]").forEach((root) => {
      const rows = Array.from(root.querySelectorAll("[data-affiliate-step]"));
      const result = root.querySelector("[data-affiliate-result]");
      const next = root.querySelector("[data-affiliate-next]");
      const reset = root.querySelector("[data-affiliate-reset]");
      if (rows.length !== messages.length || !result || !next || !reset) return;
      let index = 0;
      function render() {
        rows.forEach((row, i) => {
          row.classList.toggle("is-active", i === index);
          row.classList.toggle("is-done", i < index);
          if (i === index) row.setAttribute("aria-current", "step");
          else row.removeAttribute("aria-current");
        });
        result.textContent = messages[index];
        next.disabled = index === messages.length - 1;
        reset.disabled = index === 0;
      }
      next.addEventListener("click", () => {
        if (index < messages.length - 1) index += 1;
        render();
      });
      reset.addEventListener("click", () => { index = 0; render(); });
      render();
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
