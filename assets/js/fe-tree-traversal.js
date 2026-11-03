(function () {
  "use strict";
  const root = document.getElementById("fe-tree-traversal-demo");
  if (!root) return;

  // Same tree as the article: A(B(D(G),E),C(,F)).
  const children = {
    A: ["B", "C"], B: ["D", "E"], C: [null, "F"],
    D: ["G", null], E: [null, null], F: [null, null], G: [null, null]
  };
  const expected = {
    pre: "ABDGECF", inside: "GDBEACF", post: "GDEBFCA"
  };
  const labels = { pre: "先行順", inside: "中間順", post: "後行順" };
  const $ = (selector) => root.querySelector(selector);
  const mode = $("#fe-tree-mode");
  const guess = $("#fe-tree-guess");
  const next = $("#fe-tree-next");
  const back = $("#fe-tree-back");
  const reset = $("#fe-tree-reset");
  const output = $("#fe-tree-output");
  const progress = $("#fe-tree-progress");
  const feedback = $("#fe-tree-feedback");
  const reason = $("#fe-tree-reason");
  const treeNodes = Array.from(root.querySelectorAll("[data-tree-node]"));
  const edges = Array.from(root.querySelectorAll("[data-tree-edge]"));

  function trace(which) {
    const result = [];
    function visit(node, parents) {
      if (!node) return;
      const [left, right] = children[node];
      if (which === "pre") result.push({ node, parents, moment: "左右の部分木を調べる前" });
      visit(left, parents.concat(node));
      if (which === "inside") result.push({ node, parents, moment: "左部分木を調べ終え、右部分木に進む前" });
      visit(right, parents.concat(node));
      if (which === "post") result.push({ node, parents, moment: "左右の部分木を両方調べ終えた後" });
    }
    visit("A", []);
    return result;
  }

  let steps = trace(mode.value);
  let index = 0;
  function render(message) {
    const current = index ? steps[index - 1] : null;
    const recorded = new Set(steps.slice(0, index).map((s) => s.node));
    const ancestors = new Set(current ? current.parents : []);
    treeNodes.forEach((node) => {
      const id = node.getAttribute("data-tree-node");
      let state = "idle";
      if (recorded.has(id)) state = "done";
      if (ancestors.has(id) && !recorded.has(id)) state = "ancestor";
      if (current && current.node === id) state = "current";
      node.setAttribute("data-state", state);
    });
    const activePath = current ? current.parents.concat(current.node) : [];
    edges.forEach((edge) => {
      const pair = edge.getAttribute("data-tree-edge").split("-");
      const a = activePath.indexOf(pair[0]);
      const b = activePath.indexOf(pair[1]);
      edge.setAttribute("data-active", String(a !== -1 && b === a + 1));
    });
    progress.textContent = labels[mode.value] + "： " + index + " / " + steps.length + " 節点を記録";
    output.textContent = index ? steps.slice(0, index).map((s) => s.node).join(" → ") : "まだ記録していません。";
    feedback.textContent = message || (index === 0 ? "次に記録する節点を予想してから「次へ」を押しましょう。" : "次の節点を予想して進めましょう。");
    reason.textContent = !current
      ? "線をたどる順番と、節点名を記録するタイミングは同じとは限りません。"
      : current.node + "を記録：" + current.moment + "。"
        + (current.parents.length ? " 通った部分木：" + current.parents.join(" → ") + "。" : " 全体の根です。")
        + (index === steps.length ? " すべての節点を1回ずつ記録しました。" : "");
    next.disabled = index === steps.length;
    back.disabled = index === 0;
    guess.disabled = index === steps.length;
    next.textContent = index === steps.length ? "完了" : "次へ（1節点記録）";
  }

  function restart() {
    steps = trace(mode.value);
    index = 0;
    guess.value = "";
    render("方式を選びました。次の節点を予想しましょう。");
  }
  mode.addEventListener("change", restart);
  reset.addEventListener("click", restart);
  back.addEventListener("click", () => {
    if (index === 0) return;
    index--;
    guess.value = "";
    render("1節点戻しました。記録順と強調表示を確認しましょう。");
  });
  next.addEventListener("click", () => {
    if (index >= steps.length) return;
    const predicted = guess.value;
    const actual = steps[index].node;
    index++;
    guess.value = "";
    const evaluation = predicted
      ? (predicted === actual ? "予想正解！ " : "予想とは違いました。 ")
      : "予想は省略しました。 ";
    render(evaluation + index + "番目は" + actual + "です。"
      + (index === steps.length ? " 全節点の記録が完了しました。" : ""));
  });
  // Record-only steps by design: traversal can pass a node before recording it.
  // Assert the example order at startup to guard against accidental tree edits.
  Object.keys(expected).forEach((key) => {
    if (trace(key).map((s) => s.node).join("") !== expected[key]) {
      throw new Error("binary tree traversal example mismatch: " + key);
    }
  });
  render();
})();
