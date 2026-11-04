/* FE virtualization layers: prediction -> reveal -> compare. */
(function () {
  "use strict";
  var cases = {
    host: {
      guest: true,
      layers: [
        ["アプリA","guest"],["アプリB","guest"],
        ["ゲストOS A","guest"],["ゲストOS B","guest"],
        ["仮想化ソフト","full"],["ホストOS","host full"],["物理サーバ","physical full"]
      ],
      text: "ホスト型はホストOS上に仮想化ソフトを置き、各仮想マシンでゲストOSを動かします。"
    },
    hypervisor: {
      guest: true,
      layers: [
        ["アプリA","guest"],["アプリB","guest"],
        ["ゲストOS A","guest"],["ゲストOS B","guest"],
        ["ハイパーバイザ","full"],["物理サーバ","physical full"]
      ],
      text: "ベアメタル型ハイパーバイザは物理サーバ上で直接VMを管理します。VMごとのゲストOSは必要です。"
    },
    container: {
      guest: false,
      layers: [
        ["アプリA（コンテナ）","guest"],["アプリB（コンテナ）","guest"],
        ["コンテナ実行基盤","full"],["ホストOSのカーネル","host full"],["物理サーバ","physical full"]
      ],
      text: "コンテナ型はホストOSのカーネルを共有し、通常はコンテナごとに完全なゲストOSを起動しません。"
    }
  };
  function setup() {
    var root = document.getElementById("fe-server-virtualization-demo");
    if (!root || root.dataset.ready === "true") return;
    var buttons = Array.prototype.slice.call(root.querySelectorAll("[data-mode]"));
    var reveal = root.querySelector("[data-reveal]");
    var reset = root.querySelector("[data-reset]");
    var result = root.querySelector("[data-result]");
    var layers = root.querySelector("[data-layers]");
    var feedback = root.querySelector("[data-feedback]");
    var explanation = root.querySelector("[data-explanation]");
    var guesses = Array.prototype.slice.call(root.querySelectorAll('input[name="fe-virtualization-guess"]'));
    if (buttons.length !== 3 || guesses.length !== 2 || !reveal || !reset || !result || !layers || !feedback || !explanation) return;
    var mode = "host";
    function clearPrediction() {
      guesses.forEach(function (input) { input.checked = false; });
      result.hidden = true;
      layers.replaceChildren();
      feedback.textContent = "";
      explanation.textContent = "";
      reveal.disabled = false;
    }
    function choose(next) {
      if (!cases[next]) return;
      mode = next;
      buttons.forEach(function (button) {
        button.setAttribute("aria-pressed", String(button.dataset.mode === mode));
      });
      clearPrediction();
    }
    function show() {
      var config = cases[mode];
      var selected = guesses.find(function (input) { return input.checked; });
      if (!config) return;
      layers.replaceChildren();
      config.layers.forEach(function (entry) {
        var cell = document.createElement("div");
        cell.className = "fe-server-virtualization-demo__layer";
        entry[1].split(" ").forEach(function (flag) {
          if (flag) cell.classList.add("fe-server-virtualization-demo__layer--" + flag);
        });
        cell.textContent = entry[0];
        layers.appendChild(cell);
      });
      var right = config.guest ? "必要" : "原則不要";
      feedback.textContent = selected
        ? ((selected.value === (config.guest ? "yes" : "no") ? "予想どおり！ " : "ここが重要です。 ") + "ゲストOSは「" + right + "」です。")
        : "ゲストOSは「" + right + "」です。";
      explanation.textContent = config.text;
      result.hidden = false;
    }
    buttons.forEach(function (button) {
      button.addEventListener("click", function () { choose(button.dataset.mode); });
    });
    reveal.addEventListener("click", show);
    reset.addEventListener("click", function () { choose("host"); });
    root.dataset.ready = "true";
    choose("host");
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
}());
