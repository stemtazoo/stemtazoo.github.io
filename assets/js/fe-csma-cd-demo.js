(() => {
  "use strict";
  const root = document.getElementById("fe-csma-cd-demo");
  if (!root) return;

  // A teaching trace, not a timing-accurate Ethernet protocol simulator.
  const scenarios = {
    collision: [
      { a: "待機", b: "待機", medium: "空き", title: "初期状態",
        note: "2台は同じ共有通信路で送信を待っています。" },
      { a: "空きを確認", b: "空きを確認", medium: "空き", title: "通信路を確認",
        note: "両端末がほぼ同時に通信路は空いていると判断します。" },
      { a: "送信中", b: "送信中", medium: "衝突", title: "ほぼ同時に送信",
        note: "信号の伝搬に時間差があるため、両端末が送信を開始すると衝突が起こり得ます。" },
      { a: "送信中止", b: "送信中止", medium: "衝突を検出", title: "衝突を検出",
        note: "端末は衝突を検出し、送信を中止します。" },
      { a: "短い待機", b: "長い待機", medium: "空き", title: "待機時間をずらす",
        note: "各端末は再送までの待ち時間をランダムに選びます。ここではAが先に待機を終えた一例です。" },
      { a: "再送して成功", b: "待機中", medium: "Aが使用中", title: "Aが再送",
        note: "Aは通信路が空いたことを確かめて再送します。Bはまだ待機しています。" },
      { a: "送信完了", b: "再送して成功", medium: "Bが使用中", title: "Bが再送",
        note: "Aの送信後、Bも通信路の空きを確かめて再送し、今回は両端末の送信が完了します。" }
    ],
    staggered: [
      { a: "待機", b: "待機", medium: "空き", title: "初期状態",
        note: "2台は同じ共有通信路を使いますが、送信を始める時刻が異なる例です。" },
      { a: "空きを確認", b: "待機", medium: "空き", title: "Aが確認",
        note: "通信路が空いているため、Aは送信を開始できます。" },
      { a: "送信中", b: "空きを確認", medium: "Aが使用中", title: "Bは送信を待つ",
        note: "Aの送信中にBが通信路を確認すると、使用中なのでBは送信しません。" },
      { a: "送信完了", b: "空きを確認", medium: "空き", title: "Aの送信が終了",
        note: "Aの送信が終わり、通信路が空きました。" },
      { a: "送信完了", b: "送信して成功", medium: "Bが使用中", title: "Bが送信",
        note: "Bは空きを確認して送信します。衝突も再送も起きません。" }
    ]
  };

  const scenario = root.querySelector("[data-scenario]");
  const next = root.querySelector("[data-next]");
  const back = root.querySelector("[data-back]");
  const reset = root.querySelector("[data-reset]");
  const prediction = root.querySelector("[data-prediction]");
  const fields = {
    a: root.querySelector("[data-a]"),
    b: root.querySelector("[data-b]"),
    medium: root.querySelector("[data-medium]"),
    step: root.querySelector("[data-step]"),
    title: root.querySelector("[data-title]"),
    note: root.querySelector("[data-note]"),
    feedback: root.querySelector("[data-feedback]"),
    trace: root.querySelector("[data-trace]")
  };
  let index = 0;
  let feedback = "予想は任意です。「次へ」で順番に確認できます。";

  function render() {
    const steps = scenarios[scenario.value];
    const item = steps[index];
    fields.a.textContent = item.a;
    fields.b.textContent = item.b;
    fields.medium.textContent = item.medium;
    fields.step.textContent = `${index + 1} / ${steps.length}`;
    fields.title.textContent = item.title;
    fields.note.textContent = item.note;
    fields.feedback.textContent = feedback;
    fields.medium.dataset.condition = item.medium.includes("衝突") ? "collision" :
      item.medium.includes("使用中") ? "busy" : "idle";
    fields.trace.replaceChildren();
    steps.slice(0, index + 1).forEach((step, i) => {
      const li = document.createElement("li");
      li.textContent = `${i + 1}. ${step.title}`;
      if (i === index) li.setAttribute("aria-current", "step");
      fields.trace.append(li);
    });
    back.disabled = index === 0;
    next.disabled = index === steps.length - 1;
    next.textContent = index === steps.length - 1 ? "終了" : "次へ（1ステップ）";
  }

  function clearPrediction() { prediction.value = ""; }
  next.addEventListener("click", () => {
    const steps = scenarios[scenario.value];
    if (index >= steps.length - 1) return;
    const guess = prediction.value;
    index += 1;
    const result = steps[index];
    const actual = result.medium.includes("衝突") ? "collision" :
      result.medium.includes("使用中") ? "busy" : "idle";
    feedback = guess ? (guess === actual ? "予想どおりです。" : "予想とは異なりました。") : "次の状態を確認しました。";
    clearPrediction();
    render();
  });
  back.addEventListener("click", () => {
    if (index === 0) return;
    index -= 1;
    feedback = "1ステップ戻りました。次の変化を予想してみましょう。";
    clearPrediction();
    render();
  });
  function start() {
    index = 0;
    feedback = "初期状態です。次のステップを予想してみましょう。";
    clearPrediction();
    render();
  }
  reset.addEventListener("click", start);
  scenario.addEventListener("change", start);
  render();
})();
