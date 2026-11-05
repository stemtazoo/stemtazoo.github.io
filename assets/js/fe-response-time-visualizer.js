/* FE response time: explicitly scoped input/output measurement boundaries. */
(function () {
  "use strict";
  function setup() {
    var root = document.getElementById("fe-response-demo");
    if (!root || root.dataset.ready === "true") return;
    var ids = ["input", "wait", "work", "output"];
    var inputs = ids.map(function (name) { return root.querySelector("#fe-response-" + name); });
    var labels = ids.map(function (name) { return root.querySelector("#fe-response-" + name + "-value"); });
    var bars = ids.map(function (name) { return root.querySelector('[data-bar="' + name + '"]'); });
    var selectors = ["timeline", "phases", "response", "turnaround", "response-endpoints", "turnaround-endpoints", "response-range", "feedback", "apply", "reset"];
    var nodes = {};
    selectors.forEach(function (name) { nodes[name] = root.querySelector("[data-" + name + "]"); });
    var guesses = Array.prototype.slice.call(root.querySelectorAll('input[name="fe-response-guess"]'));
    if (inputs.concat(labels, bars).some(function (x) { return !x; }) || selectors.some(function (name) { return !nodes[name]; }) || guesses.length !== 3) return;
    var initial = [2, 3, 4, 5], previous = initial.slice();
    function read() { return inputs.map(function (x) { return Number(x.value); }); }
    function preview() { read().forEach(function (v, i) { labels[i].textContent = v + "秒"; }); }
    function render(values, message) {
      var r = values[1] + values[2], start = values[0], first = start + r, total = first + values[3];
      var names = ["入力", "待ち", "処理", "残りの出力"];
      values.forEach(function (value, i) {
        bars[i].style.flexGrow = String(value);
        bars[i].style.flexBasis = "0";
        bars[i].hidden = value === 0;
      });
      var phases = values.map(function (v, i) { return names[i] + v + "秒"; });
      nodes.timeline.setAttribute("aria-label", phases.join("、"));
      nodes.phases.textContent = phases.join(" → ");
      nodes.response.textContent = "レスポンスタイム：" + r + "秒（待ち" + values[1] + "＋処理" + values[2] + "）";
      nodes.turnaround.textContent = "ターンアラウンドタイム：" + total + "秒（入力" + start + "＋待ち" + values[1] + "＋処理" + values[2] + "＋出力" + values[3] + "）";
      nodes["response-endpoints"].textContent = "入力完了" + start + "秒 → 出力開始" + first + "秒";
      nodes["turnaround-endpoints"].textContent = "入力開始0秒 → 全出力完了" + total + "秒";
      nodes["response-range"].style.marginLeft = (100 * start / total) + "%";
      nodes["response-range"].style.width = (100 * r / total) + "%";
      nodes.feedback.textContent = message;
    }
    function applyValues() {
      var values = read(), guess = guesses.find(function (x) { return x.checked; });
      var outputOnly = values.slice(0, 3).every(function (v, i) { return v === previous[i]; }) && values[3] > previous[3];
      var msg = outputOnly ? "出力時間だけが増えました。レスポンスタイムは同じで、ターンアラウンドタイムだけ長くなります。" : "設定した時間で再計算しました。両指標の開始・終了位置を見比べてください。";
      if (guess) msg += guess.value === "turnaround" ? " 出力だけを延ばす場合の予想は正しいです。" : " 出力だけを延ばす場合はターンアラウンドタイムだけが長くなります。";
      render(values, msg);
      previous = values.slice();
    }
    inputs.forEach(function (input) { input.addEventListener("input", function () {
      preview();
      nodes.feedback.textContent = "条件を変更しました。「反映して比較」を押すと下の結果が更新されます。現在の図と結果は反映前です。";
    }); });
    nodes.apply.addEventListener("click", applyValues);
    nodes.reset.addEventListener("click", function () {
      initial.forEach(function (v, i) { inputs[i].value = v; });
      guesses.forEach(function (g) { g.checked = false; });
      preview(); previous = initial.slice();
      render(previous, "初期条件に戻しました。出力時間だけを変えると、どちらの指標が変化するか予想してください。");
    });
    preview();
    render(initial, "初期条件：入力2秒、待ち3秒、処理4秒、出力5秒。変更して結果を比べてください。");
    root.dataset.ready = "true";
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
}());
