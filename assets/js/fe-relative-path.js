(function () {
  "use strict";
  const root = document.getElementById("fe-path-demo");
  if (!root) return;
  const $ = (q) => root.querySelector(q);
  const nodes = {
    root: { name: "", parent: null },
    a1: { name: "a", parent: "root" },
    a2: { name: "a", parent: "a1" },
    b1: { name: "b", parent: "a2" },
    c: { name: "c", parent: "b1" },
    a3: { name: "a", parent: "a2" },
    b2: { name: "b", parent: "a3" },
    file: { name: "file", parent: "b2" }
  };
  const cases = {
    example: { tokens: [".", "..", "..", "a", "b", "file"], text: ".\\..\\..\\a\\b\\file" },
    parent: { tokens: ["..", ".."], text: "..\\.." },
    same: { tokens: ["."], text: "." }
  };
  const children = (id, label) => Object.keys(nodes).find((key) => nodes[key].parent === id && nodes[key].name === label);
  const pathOf = (id) => {
    const parts = [];
    let node = id;
    while (node && node !== "root") {
      parts.unshift(nodes[node].name);
      node = nodes[node].parent;
    }
    return "¥" + parts.join("¥");
  };
  const kindOf = (token) => token === "." ? "same" : token === ".." ? "up" : token === "file" ? "file" : "down";
  const names = { same: "今の場所のまま", up: "親へ戻る", down: "子へ進む", file: "ファイルを指定" };
  const mode = $("#fe-path-case"), guess = $("#fe-path-guess"), next = $("#fe-path-next");
  const back = $("#fe-path-back"), reset = $("#fe-path-reset");
  const current = $("#fe-path-current"), upcoming = $("#fe-path-upcoming"), progress = $("#fe-path-progress");
  const feedback = $("#fe-path-feedback"), reason = $("#fe-path-reason"), history = $("#fe-path-history");
  const tree = Array.from(root.querySelectorAll("[data-path-node]"));
  let step = 0, trail = ["c"], positions = ["c"];
  // All cases start in ¥a¥a¥b¥c (the original article's directory).
  function destination(from, token) {
    if (token === ".") return from;
    if (token === "..") return nodes[from].parent || "root";
    return children(from, token) || null;
  }
  function display(message) {
    const example = cases[mode.value], now = positions[step], done = step === example.tokens.length;
    const visited = new Set(positions.slice(0, step));
    tree.forEach((el) => {
      const id = el.getAttribute("data-path-node");
      const state = id === now ? "current" : id === "c" && step === 0 ? "start" : visited.has(id) ? "past" : "idle";
      el.setAttribute("data-state", state);
    });
    progress.textContent = step + " / " + example.tokens.length + " 要素";
    current.textContent = pathOf(now);
    upcoming.textContent = done ? "すべて処理済み" : example.tokens[step];
    history.textContent = step === 0 ? "まだ処理していません。" : example.tokens.slice(0, step).join(" → ");
    reason.textContent = !step
      ? "まずカレントディレクトリから始めます。各要素を左から一つずつ解釈します。"
      : (example.tokens[step - 1] === "." ? "「.」は現在の場所を変えません。" :
        example.tokens[step - 1] === ".." ? "「..」は親ディレクトリに戻ります。" :
        example.tokens[step - 1] === "file" ? "最後はファイルを指定します。途中の要素は左から処理しました。" :
        "名前が示す子ディレクトリへ進みます。");
    feedback.textContent = message || (done ? "完了しました。絶対パスを確認しましょう。" : "次の要素の意味を予想しましょう。");
    next.disabled = done; back.disabled = step === 0; guess.disabled = done;
    next.textContent = done ? "完了" : "次へ（1要素進む）";
  }
  function restart() {
    step = 0; positions = ["c"]; guess.value = "";
    display("最初の状態です。次の要素の意味を予想してください。");
  }
  mode.addEventListener("change", restart);
  reset.addEventListener("click", restart);
  back.addEventListener("click", () => {
    if (step === 0) return;
    step--; positions.pop(); guess.value = "";
    display("1要素戻しました。現在地を確かめましょう。");
  });
  next.addEventListener("click", () => {
    const data = cases[mode.value];
    if (step >= data.tokens.length) return;
    const token = data.tokens[step], dest = destination(positions[step], token);
    if (!dest) { feedback.textContent = "指定先がありません。教材の経路を確認してください。"; return; }
    const correct = kindOf(token), predicted = guess.value;
    positions.push(dest); step++; guess.value = "";
    const text = !predicted ? "予想を省略しました。" :
      predicted === correct ? "予想正解！" : "予想とは異なりました。";
    display(text + " 「" + token + "」：" + names[correct] + "。");
  });
  // Fail visibly when an example path is edited inconsistently.
  Object.keys(cases).forEach((key) => {
    let id = "c";
    cases[key].tokens.forEach((token) => {
      id = destination(id, token);
      if (!id) throw new Error("FE path lesson: unknown target in " + key);
    });
    if (key === "example" && pathOf(id) !== "¥a¥a¥a¥b¥file") {
      throw new Error("FE path lesson: original article's result does not match");
    }
  });
  display();
})();
