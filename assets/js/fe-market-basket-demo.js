(() => {
  "use strict";
  const root = document.getElementById("fe-market-basket-demo");
  if (!root || root.dataset.ready) return;
  root.dataset.ready = "1";
  const transactions = [
    ["bread", "milk", "egg"],
    ["bread", "milk"],
    ["bread", "coffee"],
    ["bread", "milk", "egg"],
    ["milk", "egg"]
  ];
  const names = {bread:"パン",milk:"牛乳",egg:"卵",coffee:"コーヒー"};
  const first = root.querySelector("#fe-basket-first");
  const second = root.querySelector("#fe-basket-second");
  const guesses = [...root.querySelectorAll("[data-fe-basket-guess]")];
  const reveal = root.querySelector("#fe-basket-reveal");
  const reset = root.querySelector("#fe-basket-reset");
  const feedback = root.querySelector("#fe-basket-feedback");
  const results = root.querySelector("#fe-basket-results");
  const countOutput = root.querySelector("#fe-basket-count");
  const rateOutput = root.querySelector("#fe-basket-rate");
  const rows = root.querySelector("#fe-basket-rows");
  let guess = null;
  const countMatches = (a,b) => transactions.filter(t => t.includes(a) && t.includes(b)).length;
  function clear() {
    guess = null;
    guesses.forEach(b => b.setAttribute("aria-pressed","false"));
    results.hidden = true;
    feedback.textContent = "商品を選んで結果を確認しましょう。";
  }
  function show() {
    const a = first.value, b = second.value;
    const n = countMatches(a,b);
    countOutput.textContent = n + "件";
    rateOutput.textContent = (n * 100 / transactions.length).toFixed(0) + "%";
    rows.replaceChildren();
    transactions.forEach((t,i) => {
      const matched = t.includes(a) && t.includes(b);
      const tr = document.createElement("tr");
      tr.dataset.match = String(matched);
      [String.fromCharCode(65+i),t.map(k=>names[k]).join("、"),matched?"両方あり":"両方はない"].forEach(value => {
        const td=document.createElement("td");
        td.textContent=value;
        tr.appendChild(td);
      });
      rows.appendChild(tr);
    });
    results.hidden = false;
    feedback.textContent = guess === null ? "5件の取引から同時購入数を数えました。" :
      guess === n ? "予想どおりです！「両方あり」の行を確認しましょう。" :
      "予想は" + guess + "件、実際は" + n + "件でした。「両方あり」の行を数えてみましょう。";
  }
  guesses.forEach(button => button.addEventListener("click", () => {
    guess = Number(button.dataset.feBasketGuess);
    guesses.forEach(b => b.setAttribute("aria-pressed", String(b===button)));
    results.hidden = true;
    feedback.textContent = guess + "件と予想しました。「結果を見る」を押してください。";
  }));
  [first,second].forEach(s => s.addEventListener("change", clear));
  reveal.addEventListener("click",show);
  reset.addEventListener("click", () => {first.value="bread";second.value="milk";clear();});
  clear();
})();
