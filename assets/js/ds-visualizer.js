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

  document.querySelectorAll("[data-ds-causal-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-causal-mode]"));
    const left = demo.querySelector("[data-causal-left]");
    const right = demo.querySelector("[data-causal-right]");
    const arrow = demo.querySelector("[data-causal-arrow]");
    const third = demo.querySelector("[data-causal-third]");
    const verdict = demo.querySelector("[data-causal-verdict]");
    const note = demo.querySelector("[data-causal-note]");

    const settings = {
      correlation: {
        left: "広告費が多い",
        right: "売上が高い",
        arrow: "↔",
        third: "観察データでは、一緒に増えていることまでは分かる",
        verdict: "相関あり / 因果は未確定",
        note: "売上が高い会社ほど広告費を増やしている可能性もあり、向きまでは決められません。",
      },
      confounder: {
        left: "アイス売上",
        right: "飲料売上",
        arrow: "↔",
        third: "気温 ↑ → アイス売上 ↑ ＋ 飲料売上 ↑",
        verdict: "第三の要因（交絡）を疑う",
        note: "2つが一緒に増えていても、共通の原因である気温が両方を動かしているかもしれません。",
      },
      randomized: {
        left: "施策を実施",
        right: "結果を比較",
        arrow: "→",
        third: "ランダムに群分けして、他の条件の偏りを減らす",
        verdict: "因果を検討しやすい設計",
        note: "ランダム化比較は因果を議論しやすくします。ただし、サンプル数や実験条件の確認は必要です。",
      },
    };

    function render(mode) {
      const setting = settings[mode];
      left.textContent = setting.left;
      right.textContent = setting.right;
      arrow.textContent = setting.arrow;
      third.textContent = setting.third;
      verdict.textContent = setting.verdict;
      note.textContent = setting.note;
      buttons.forEach((button) => {
        button.setAttribute("aria-pressed", String(button.dataset.causalMode === mode));
      });
    }

    buttons.forEach((button) => {
      button.addEventListener("click", () => render(button.dataset.causalMode));
    });

    render("correlation");
  });
});

// Keep scores and actual labels fixed; only the prediction threshold changes.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-ds-threshold-demo]").forEach((demo) => {
    const find = (name) => demo.querySelector(`[data-dt-${name}]`);
    const slider = find("slider");
    const samples = Array.from(demo.querySelectorAll("[data-dt-score]"));
    const presets = Array.from(demo.querySelectorAll("[data-dt-preset]"));
    const percentage = (numerator, denominator) => denominator
      ? `${(100 * numerator / denominator).toFixed(1)}%` : "算出不可（陽性判定0件）";

    function render() {
      const threshold = Number(slider.value);
      const label = (threshold / 100).toFixed(2);
      const counts = { tp: 0, fp: 0, fn: 0, tn: 0 };
      samples.forEach((sample) => {
        const predicted = Number(sample.dataset.dtScore) >= threshold;
        const actual = sample.dataset.dtActual === "positive";
        const kind = predicted ? (actual ? "tp" : "fp") : (actual ? "fn" : "tn");
        counts[kind] += 1;
        sample.classList.toggle("is-error", kind === "fp" || kind === "fn");
        sample.querySelector("[data-dt-prediction]").textContent = `判定：${predicted ? "陽性" : "陰性"}（${kind.toUpperCase()}）`;
      });
      Object.keys(counts).forEach((key) => { find(key).textContent = String(counts[key]); });
      const { tp, fp, fn } = counts;
      const precision = percentage(tp, tp + fp);
      const recall = percentage(tp, tp + fn);
      find("value").textContent = label;
      slider.setAttribute("aria-valuetext", label);
      find("precision").textContent = `${tp} / (${tp} + ${fp}) = ${precision}`;
      find("recall").textContent = `${tp} / (${tp} + ${fn}) = ${recall}`;
      find("status").textContent = `しきい値${label}：見逃し（FN）${fn}件、誤検出（FP）${fp}件。適合率${precision}、再現率${recall}。`;
    }

    slider.disabled = false;
    slider.addEventListener("input", render);
    presets.forEach((button) => {
      button.disabled = false;
      button.addEventListener("click", () => {
        slider.value = button.dataset.dtPreset;
        render();
      });
    });
    render();
  });
});