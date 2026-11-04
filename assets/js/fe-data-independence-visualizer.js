/* Three schema levels: predict, reveal, compare; no external dependencies. */
(function () {
  "use strict";
  var cases = {
    physical: {
      type: "physical",
      question: "索引を追加するとき、守りたいのはどの層の定義でしょうか？",
      changed: "internal",
      kept: ["conceptual", "external"],
      details: ["利用者の見え方はそのまま","表や列の論理構造はそのまま","索引を追加して保存方法を変更"],
      explanation: "索引など内部スキーマの変更を、概念スキーマに影響させないようにするのが物理的データ独立性です。"
    },
    logical: {
      type: "logical",
      question: "表の論理構造を変更するとき、利用者側の見え方を保てる性質は？",
      changed: "conceptual",
      kept: ["external"],
      details: ["従来のビュー・画面は維持","表を分割し、マッピングを調整","格納方法はこの例では変更しない"],
      explanation: "概念スキーマの変更の影響を外部スキーマに及ぼさないようにするのが論理的データ独立性です。従来のビューを保つには調整が必要なことがあります。"
    },
    external: {
      type: "other",
      question: "利用者向けの表示列そのものを変えるのは、どの独立性の例？",
      changed: "external",
      kept: ["conceptual","internal"],
      details: ["表示列を変更","表の構造はそのまま","格納方法はそのまま"],
      explanation: "外部スキーマ自体を変更する例です。下位層の変更の影響を上位層から隠すという、二つのデータ独立性の典型例ではありません。"
    }
  };
  function init() {
    var root = document.getElementById("fe-data-independence");
    if (!root || root.dataset.ready === "true") return;
    var choices = Array.prototype.slice.call(root.querySelectorAll("[data-case]"));
    var guesses = Array.prototype.slice.call(root.querySelectorAll('input[name="fe-data-independence-guess"]'));
    var question = root.querySelector("[data-question]");
    var result = root.querySelector("[data-result]");
    var feedback = root.querySelector("[data-feedback]");
    var explanation = root.querySelector("[data-explanation]");
    var reveal = root.querySelector("[data-reveal]");
    var reset = root.querySelector("[data-reset]");
    var levels = ["external","conceptual","internal"];
    var boxes = levels.map(function (name) { return root.querySelector('[data-layer="' + name + '"]'); });
    var desc = levels.map(function (name) { return root.querySelector('[data-detail="' + name + '"]'); });
    if (choices.length !== 3 || guesses.length !== 3 || !question || !result || !feedback || !explanation || !reveal || !reset || boxes.some(function(x){return !x;}) || desc.some(function(x){return !x;})) return;
    var mode = "physical";
    function choose(next) {
      if (!cases[next]) return;
      mode = next;
      choices.forEach(function (button) { button.setAttribute("aria-pressed",String(button.dataset.case === mode)); });
      guesses.forEach(function (g) { g.checked = false; });
      question.textContent = cases[mode].question;
      result.hidden = true;
      feedback.textContent = "";
      explanation.textContent = "";
    }
    function show() {
      var spec = cases[mode], selected = guesses.find(function (g) { return g.checked; });
      var label = {physical:"物理的データ独立性",logical:"論理的データ独立性",other:"いずれの定義でもない"}[spec.type];
      boxes.forEach(function (box,i) {
        box.classList.toggle("is-changed",levels[i] === spec.changed);
        box.classList.toggle("is-kept",spec.kept.indexOf(levels[i]) !== -1);
        desc[i].textContent = spec.details[i];
      });
      feedback.textContent = (selected ? (selected.value === spec.type ? "予想どおり！ " : "ここを確認しましょう。 ") : "") + "この例は「" + label + "」です。";
      explanation.textContent = spec.explanation;
      result.hidden = false;
    }
    choices.forEach(function (b) { b.addEventListener("click",function(){choose(b.dataset.case);}); });
    reveal.addEventListener("click",show);
    reset.addEventListener("click",function(){choose("physical");});
    choose("physical");
    root.dataset.ready = "true";
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded",init); else init();
}());
