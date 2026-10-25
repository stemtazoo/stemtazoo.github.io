/* FE delegation: stepwise caller, callee, and return-flow illustration. */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("[data-fe-delegation-demo]").forEach(function (demo) {
    const stages = Array.from(demo.querySelectorAll("[data-delegation-stage]"));
    const order = demo.querySelector("[data-delegation-order]");
    const payment = demo.querySelector("[data-delegation-payment]");
    const status = demo.querySelector("[data-delegation-status]");
    const progress = demo.querySelector("[data-delegation-progress]");
    const prev = demo.querySelector("[data-delegation-prev]");
    const next = demo.querySelector("[data-delegation-next]");
    const reset = demo.querySelector("[data-delegation-reset]");
    if (stages.length !== 4 || !order || !payment || !status || !progress || !prev || !next || !reset) return;

    const messages = [
      "Order.checkout() が呼ばれ、注文処理を始めます。",
      "Order.checkout() から PaymentProcessor.pay() へ決済を委譲します。",
      "PaymentProcessor.pay() が決済処理を実行し、結果を返します。",
      "Order.checkout() が結果を受け取り、呼出元へ返します。"
    ];
    let index = 0;
    demo.classList.add("is-interactive");

    function render() {
      stages.forEach(function (el, i) {
        el.classList.toggle("is-current", i === index);
        if (i === index) el.setAttribute("aria-current", "step");
        else el.removeAttribute("aria-current");
      });
      order.classList.toggle("is-active", index !== 2);
      payment.classList.toggle("is-active", index === 2);
      status.textContent = messages[index];
      progress.textContent = (index + 1) + " / " + stages.length;
      prev.disabled = index === 0;
      next.disabled = index === stages.length - 1;
    }
    prev.addEventListener("click", function () {
      index = Math.max(0, index - 1);
      render();
    });
    next.addEventListener("click", function () {
      index = Math.min(stages.length - 1, index + 1);
      render();
    });
    reset.addEventListener("click", function () {
      index = 0;
      render();
    });
    render();
  });
});
