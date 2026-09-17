document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-ds-layer-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-task]"));
    const hidden = demo.querySelector("[data-hidden-activation]");
    const output = demo.querySelector("[data-output-activation]");
    const result = demo.querySelector("[data-layer-result]");

    const settings = {
      binary: {
        hidden: "ReLU",
        output: "Sigmoid",
        result: "二値分類：中間層で特徴を非線形に変換し、出力層では0〜1に収めるSigmoidを使う組合せが代表的です。",
      },
      multiclass: {
        hidden: "ReLU",
        output: "Softmax",
        result: "多クラス分類：中間層はReLU、出力層では複数クラスの確率の合計を1にするSoftmaxが代表的です。",
      },
      regression: {
        hidden: "ReLU",
        output: "線形（恒等）",
        result: "回帰：中間層はReLUなどで非線形性を入れ、出力層は値をそのまま出せる線形（恒等）関数が代表的です。",
      },
    };

    function render(task) {
      const setting = settings[task];
      hidden.textContent = setting.hidden;
      output.textContent = setting.output;
      result.textContent = setting.result;
      buttons.forEach((button) => {
        button.setAttribute("aria-pressed", String(button.dataset.task === task));
      });
    }

    buttons.forEach((button) => {
      button.addEventListener("click", () => render(button.dataset.task));
    });

    render("binary");
  });
});
