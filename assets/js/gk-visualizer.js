document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-gk-activation-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-function]"));
    const slider = demo.querySelector("[data-activation-x]");
    const curve = demo.querySelector("[data-activation-curve]");
    const point = demo.querySelector("[data-activation-point]");
    const axes = Array.from(demo.querySelectorAll(".gk-activation-demo__axis"));
    const xAxis = axes[0];
    const yAxis = axes[1];
    const inputLabel = demo.querySelector("[data-activation-input]");
    const outputLabel = demo.querySelector("[data-activation-output]");
    const note = demo.querySelector("[data-activation-note]");

    const width = 600;
    const height = 260;
    const margin = 30;
    const xMin = -6;
    const xMax = 6;
    let current = "relu";

    const functions = {
      relu: {
        fn: (x) => Math.max(0, x),
        yMin: -0.5,
        yMax: 6.2,
        note: "ReLU：負の入力は0、正の入力はそのまま。中間層で使われやすい。",
      },
      sigmoid: {
        fn: (x) => 1 / (1 + Math.exp(-x)),
        yMin: -0.1,
        yMax: 1.1,
        note: "Sigmoid：出力は0〜1。二値分類の出力層で使われやすい。",
      },
      tanh: {
        fn: (x) => Math.tanh(x),
        yMin: -1.2,
        yMax: 1.2,
        note: "tanh：出力は-1〜1で0中心。端では傾きが小さくなりやすい。",
      },
    };

    function sx(x) {
      return margin + ((x - xMin) / (xMax - xMin)) * (width - margin * 2);
    }

    function sy(y) {
      const setting = functions[current];
      return height - margin - ((y - setting.yMin) / (setting.yMax - setting.yMin)) * (height - margin * 2);
    }

    function drawCurve() {
      const fn = functions[current].fn;
      const points = [];
      for (let i = 0; i <= 120; i += 1) {
        const x = xMin + (i / 120) * (xMax - xMin);
        points.push(`${i === 0 ? "M" : "L"}${sx(x).toFixed(1)},${sy(fn(x)).toFixed(1)}`);
      }
      curve.setAttribute("d", points.join(" "));
      if (xAxis) {
        const y0 = sy(0);
        xAxis.setAttribute("x1", margin);
        xAxis.setAttribute("x2", width - margin);
        xAxis.setAttribute("y1", y0);
        xAxis.setAttribute("y2", y0);
      }
      if (yAxis) {
        const x0 = sx(0);
        yAxis.setAttribute("x1", x0);
        yAxis.setAttribute("x2", x0);
        yAxis.setAttribute("y1", margin);
        yAxis.setAttribute("y2", height - margin);
      }
      updatePoint();
    }

    function updatePoint() {
      const x = Number(slider.value);
      const y = functions[current].fn(x);
      point.setAttribute("cx", sx(x));
      point.setAttribute("cy", sy(y));
      inputLabel.textContent = x.toFixed(1);
      outputLabel.textContent = y.toFixed(3).replace(/0+$/, "").replace(/\.$/, "");
      note.textContent = functions[current].note;
    }

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        current = button.dataset.function;
        buttons.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
        drawCurve();
      });
    });

    slider.addEventListener("input", updatePoint);
    drawCurve();
  });

  document.querySelectorAll("[data-gk-softmax-demo]").forEach((demo) => {
    const sliders = Array.from(demo.querySelectorAll("[data-softmax-score]"));
    const bars = Array.from(demo.querySelectorAll("[data-softmax-bar]"));
    const labels = Array.from(demo.querySelectorAll("[data-softmax-prob]"));
    const scoreLabels = Array.from(demo.querySelectorAll("[data-softmax-score-label]"));
    const total = demo.querySelector("[data-softmax-total]");

    function render() {
      const scores = sliders.map((slider) => Number(slider.value));
      const maxScore = Math.max(...scores);
      const exps = scores.map((score) => Math.exp(score - maxScore));
      const sum = exps.reduce((acc, value) => acc + value, 0);
      const probabilities = exps.map((value) => value / sum);

      probabilities.forEach((probability, index) => {
        bars[index].style.width = `${(probability * 100).toFixed(1)}%`;
        labels[index].textContent = `${(probability * 100).toFixed(1)}%`;
        scoreLabels[index].textContent = scores[index].toFixed(1);
      });
      total.textContent = probabilities.reduce((acc, value) => acc + value, 0).toFixed(2);
    }

    sliders.forEach((slider) => slider.addEventListener("input", render));
    render();
  });
});
