/* FE response time: deterministic timeline, same boundary as article. */
(function () {
  "use strict";
  function setup() {
    var root = document.getElementById("fe-response-demo");
    if (!root || root.dataset.ready === "true") return;
    var ids = ["wait", "work", "output"];
    var inputs = ids.map(function (name) { return root.querySelector("#fe-response-" + name); });
    var labels = ids.map(function (name) { return root.querySelector("#fe-response-" + name + "-value"); });
    var bars = ids.map(function (name) { return root.querySelector('[data-bar="' + name + '"]'); });
    var timeline = root.querySelector("[data-timeline]");
    var response = root.querySelector("[data-response]");
    var turnaround = root.querySelector("[data-turnaround]");
    var reason = root.querySelector("[data-reason]");
    var feedback = root.querySelector("[data-feedback]");
    var apply = root.querySelector("[data-apply]");
    var reset = root.querySelector("[data-reset]");
    var guesses = Array.prototype.slice.call(root.querySelectorAll('input[name="fe-response-guess"]'));
    if (inputs.some(function (x) { return !x; }) || labels.some(function (x) { return !x; }) || bars.some(function (x) { return !x; }) || !timeline || !response || !turnaround || !reason || !feedback || !apply || !reset || guesses.length !== 3) return;
    var previous = [3,4,5];
    function read() { return inputs.map(function (x) { return Number(x.value); }); }
    function preview() { read().forEach(function (v,i) { labels[i].textContent = v + "秒"; }); }
    function render(values, message) {
      var r = values[0] + values[1], t = r + values[2];
      values.forEach(function (value,i) {
        bars[i].style.flexGrow = String(value);
        bars[i].style.flexBasis = "0";
        bars[i].hidden = value === 0;
        bars[i].textContent = ["待ち","処理","出力"][i] + " " + value + "秒";
      });
      response.textContent = "最初の応答：" + r + "秒（待ち" + values[0] + "＋処理" + values[1] + "）";
      turnaround.textContent = "全出力完了：" + t + "秒（" + r + "＋出力" + values[2] + "）";
      reason.textContent = "最初の応答までが" + r + "秒、残りの出力" + values[2] + "秒を含めた全完了が" + t + "秒です。";
      timeline.setAttribute("aria-label","待ち" + values[0] + "秒、処理" + values[1] + "秒、残りの出力" + values[2] + "秒");
      feedback.textContent = message;
    }
    function applyValues() {
      var values = read();
      var guess = guesses.find(function (x) { return x.checked; });
      var changeOutputOnly = values[0] === previous[0] && values[1] === previous[1] && values[2] > previous[2];
      var msg = changeOutputOnly
        ? "出力時間だけが増えました。最初の応答時刻は同じで、全完了だけ遅くなります。"
        : "設定した時間で再計算しました。最初の応答と全完了の区間を見比べてください。";
      if (guess) msg += (guess.value === "turnaround" ? " 予想の考え方は正しいです。" : " 出力だけを延ばす場合は、最初の応答は変わりません。");
      render(values,msg);
      previous = values;
    }
    inputs.forEach(function (input) { input.addEventListener("input",preview); });
    apply.addEventListener("click",applyValues);
    reset.addEventListener("click",function () {
      [3,4,5].forEach(function (v,i) { inputs[i].value = v; });
      guesses.forEach(function (g) { g.checked = false; });
      preview(); previous = [3,4,5];
      render(previous,"初期条件に戻しました。出力時間だけを変えると、どちらの指標が変化するか予想してください。");
    });
    preview();
    render(previous,"初期条件：待ち3秒、処理4秒、出力5秒。変更して結果を比べてください。");
    root.dataset.ready = "true";
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded",setup);
  else setup();
}());
