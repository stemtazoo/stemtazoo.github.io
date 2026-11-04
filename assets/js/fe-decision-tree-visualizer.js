/* Decision tree: evaluate right to left; choices are not weighted averages. */
(function () {
  "use strict";
  function setup() {
    var root = document.getElementById("fe-decision-tree-demo");
    if (!root || root.dataset.ready === "true") return;
    var interactive = root.querySelector("[data-interactive]");
    var next = root.querySelector("[data-next]");
    var reset = root.querySelector("[data-reset]");
    var progress = root.querySelector("[data-progress]");
    var feedback = root.querySelector("[data-feedback]");
    var question = root.querySelector("[data-question]");
    var base = root.querySelector("[data-base]");
    var other = root.querySelector("[data-other]");
    var buttons = Array.prototype.slice.call(root.querySelectorAll("[data-choice]"));
    var modeButtons = Array.prototype.slice.call(root.querySelectorAll("[data-mode]"));
    if (!interactive || !next || !reset || !progress || !feedback || !question || !base || !other || buttons.length !== 2 || modeButtons.length !== 2) return;
    var mode = "profit", stage = 0, chosen = null;
    var configs = {
      profit: {label:"利益最大化", best:70, other:120, initial:30, rival:65, rule:"大きい利益を選ぶ", comparator: "引く", total:70, sign:"−", unit:"利益"},
      cost: {label:"費用最小化", best:50, other:90, initial:15, rival:92, rule:"小さい費用を選ぶ", comparator: "加える", total:89, sign:"+", unit:"費用"}
    };
    function display(text) {
      feedback.hidden = false;
      feedback.replaceChildren();
      var item = document.createElement("p");
      item.textContent = text;
      feedback.appendChild(item);
    }
    function render() {
      var config = configs[mode];
      modeButtons.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.mode === mode)); });
      buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(Number(b.dataset.choice) === chosen)); });
      progress.textContent = "ステップ " + (stage + 1) + " / 3（右から左へ）";
      base.textContent = (mode === "profit" ? "初期費用" : "初期費用") + config.initial + "万円";
      other.textContent = config.other + "万円";
      feedback.hidden = stage === 0 && chosen === null;
      feedback.replaceChildren();
      question.textContent = "□の枝は70万円と50万円です。" + (mode === "profit" ? "利益が大きい方" : "費用が小さい方") + "を一つ選んでください。";
      if (stage === 0) {
        buttons.forEach(function (b) { b.disabled = false; b.hidden = false; });
        next.disabled = chosen === null;
        next.textContent = "○の計算へ進む";
        if (chosen !== null) {
          var correct = chosen === config.best;
          display((correct ? "適切な選択です。" : "選び直すともっと有利になります。") +
            " □では両枝を平均しません。" + config.rule + "ため、" + config.best +
            "万円だけを左側の○に戻します。");
        }
      } else {
        buttons.forEach(function (b) { b.disabled = true; b.hidden = false; });
        buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(Number(b.dataset.choice) === config.best)); });
        next.disabled = false;
        if (stage === 1) {
          next.textContent = "最初の□で比較する";
          display("○は確率で平均します。途中の□から戻す" + config.best +
            "万円×0.4 ＋ もう一方の枝" + config.other + "万円×0.6 = " +
            (config.best * .4 + config.other * .6) + "万円。ここでは2本とも計算に使います。");
        } else {
          next.textContent = "最初に戻る";
          display("施策A：" + config.best + "×0.4 ＋ " + config.other + "×0.6 " +
            config.sign + " " + config.initial + " = " + config.total +
            "万円。比較相手の施策Bは" + config.rival + "万円です。" +
            (mode === "profit" ? "利益は70 > 65なのでAを選びます。" : "費用は89 < 92なのでAを選びます。") +
            " □では最終的にも、条件に合う一つの施策を選びます。");
        }
      }
    }
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        if (stage !== 0) return;
        chosen = Number(b.dataset.choice);
        render();
      });
    });
    modeButtons.forEach(function (b) {
      b.addEventListener("click", function () {
        mode = b.dataset.mode;
        stage = 0;
        chosen = null;
        render();
      });
    });
    next.addEventListener("click", function () {
      if (stage === 0 && chosen === null) return;
      stage = (stage + 1) % 3;
      if (stage === 0) chosen = null;
      render();
    });
    reset.addEventListener("click", function () {
      stage = 0;
      chosen = null;
      render();
    });
    render();
    interactive.hidden = false;
    root.dataset.ready = "true";
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
}());
