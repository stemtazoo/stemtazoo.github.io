/* FE reverse Polish notation: step-by-step stack-depth visualizer */
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-rpn-depth-demo]").forEach((demo) => {
    const choice = demo.querySelector("[data-rpn-choice]");
    const tokens = demo.querySelector("[data-rpn-tokens]");
    const stackEl = demo.querySelector("[data-rpn-stack]");
    const action = demo.querySelector("[data-rpn-action]");
    const depth = demo.querySelector("[data-rpn-depth]");
    const maxDepth = demo.querySelector("[data-rpn-max]");
    const progress = demo.querySelector("[data-rpn-progress]");
    const prev = demo.querySelector("[data-rpn-prev]");
    const next = demo.querySelector("[data-rpn-next]");
    const reset = demo.querySelector("[data-rpn-reset]");
    const values = {a: 2, b: 3, c: 4, d: 5};
    let index = 0;

    function trace(expression) {
      const stack = [];
      const frames = [{stack: [], max: 0, message: "開始前です。「次へ」でaを積みます。"}];
      let max = 0;
      for (const token of expression) {
        let message;
        if (Object.prototype.hasOwnProperty.call(values, token)) {
          stack.push(values[token]);
          message = token + " = " + values[token] + " を積む（push）";
        } else if (token === "+" && stack.length >= 2) {
          const right = stack.pop();
          const left = stack.pop();
          stack.push(left + right);
          message = left + " と " + right + " を取り出し（pop）、" + (left + right) + " を積む（push）";
        } else {
          message = "処理できない記号です";
        }
        max = Math.max(max, stack.length);
        frames.push({stack: [...stack], max, message});
      }
      return frames;
    }

    function render() {
      const expression = choice.value;
      const frames = trace(expression);
      index = Math.min(index, expression.length);
      const frame = frames[index];
      tokens.replaceChildren();
      [...expression].forEach((token, i) => {
        const el = document.createElement("span");
        el.textContent = token;
        if (i === index - 1) el.classList.add("is-current");
        if (i < index - 1) el.classList.add("is-done");
        tokens.append(el);
      });
      stackEl.replaceChildren();
      if (frame.stack.length === 0) {
        const empty = document.createElement("span");
        empty.textContent = "空";
        stackEl.append(empty);
      } else {
        // Draw the top first without changing the calculation stack.
        [...frame.stack].reverse().forEach((value) => {
          const item = document.createElement("strong");
          item.textContent = String(value);
          stackEl.append(item);
        });
      }
      action.textContent = frame.message;
      depth.textContent = String(frame.stack.length);
      maxDepth.textContent = String(frame.max);
      progress.textContent = index + " / " + expression.length;
      prev.disabled = index === 0;
      next.disabled = index === expression.length;
    }
    choice.addEventListener("change", () => { index = 0; render(); });
    prev.addEventListener("click", () => { index = Math.max(0, index - 1); render(); });
    next.addEventListener("click", () => { index = Math.min(choice.value.length, index + 1); render(); });
    reset.addEventListener("click", () => { index = 0; render(); });
    render();
  });
});
