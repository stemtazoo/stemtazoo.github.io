document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-recursion-trace]").forEach((root) => {
    const input = root.querySelector("[data-recursion-input]");
    const code = Array.from(root.querySelectorAll("[data-recursion-line]"));
    const stack = root.querySelector("[data-recursion-stack]");
    const returns = root.querySelector("[data-recursion-returns]");
    const message = root.querySelector("[data-recursion-message]");
    const previous = root.querySelector("[data-recursion-prev]");
    const next = root.querySelector("[data-recursion-next]");
    const reset = root.querySelector("[data-recursion-reset]");
    let states = [];
    let position = 0;
    function build(n) {
      const frames = [];
      const values = [];
      const result = [];
      const record = (line, description) => result.push({
        line, description,
        frames: frames.map(f => ({n: f.n, status: f.status})),
        values: values.slice()
      });
      record(-1, "開始前です。次のステップを押してください。");
      function visit(k) {
        frames.push({n:k,status:"active"});
        record(0, "f(" + k + ") を呼び出しました。新しいフレームを積みます。");
        record(1, "n = " + k + " なので、終了条件 n = 1 を判定します。");
        let value;
        if (k === 1) {
          value = 1;
          record(2, "終了条件が真です。1を返します。");
        } else {
          frames[frames.length - 1].status = "waiting";
          record(3, "f(" + k + ") は f(" + (k-1) + ") の結果を待ちます。");
          const child = visit(k-1);
          frames[frames.length - 1].status = "active";
          value = k * child;
          record(3, "f(" + k + ") を再開。戻り値 " + child + " に " + k + " を掛けて " + value + " を返します。");
        }
        frames.pop();
        values.push("f(" + k + ") = " + value);
        record(-1, "f(" + k + ") のフレームを取り除き、戻り値 " + value + " を呼び出し元に渡します。");
        return value;
      }
      visit(n);
      result[result.length - 1].description += " 全体の処理が終了しました。";
      return result;
    }
    function render() {
      const state = states[position];
      code.forEach((node,index) => {
        const active = index === state.line;
        node.classList.toggle("is-active",active);
        if (active) node.setAttribute("aria-current","step");
        else node.removeAttribute("aria-current");
      });
      stack.replaceChildren();
      if (!state.frames.length) stack.textContent = "スタックは空です。";
      state.frames.forEach((frame,index) => {
        const item = document.createElement("div");
        item.className = "fe-recursion-trace__frame" + (frame.status === "active" ? " is-active" : "");
        item.textContent = "深さ" + (index+1) + "：f(" + frame.n + ") / n=" + frame.n +
          (frame.status === "active" ? "［実行中］" : "［戻り値待ち］");
        stack.appendChild(item);
      });
      returns.textContent = state.values.length ? state.values.join(" → ") : "まだ戻り値はありません。";
      message.textContent = "ステップ " + position + "/" + (states.length-1) + "：" + state.description;
      previous.disabled = position === 0;
      next.disabled = position === states.length - 1;
    }
    function initialize() {
      states = build(Number(input.value));
      position = 0;
      render();
    }
    next.addEventListener("click", () => {if (position < states.length-1) {position++;render();}});
    previous.addEventListener("click", () => {if (position > 0) {position--;render();}});
    reset.addEventListener("click",initialize);
    input.addEventListener("change",initialize);
    initialize();
  });
});
