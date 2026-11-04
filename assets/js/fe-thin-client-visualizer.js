/* FE thin-client demo: mode / predict / reveal / reset. */
(function () {
  "use strict";
  var cases = {
    fat: {
      target: "client",
      client: ["入力・画面表示", "アプリケーション実行", "業務データを端末に保存する場合もある"],
      server: ["必要な共有データやサービスを提供"],
      explanation: "ファットクライアントの典型例では、端末自身がOSと業務アプリを動かします。サーバを利用することもあります。"
    },
    thin: {
      target: "server",
      client: ["入力・画面表示", "ネットワーク通信"],
      server: ["業務アプリを実行", "業務データを集中管理"],
      explanation: "シンクライアントは端末に必要最小限の機能を持たせ、業務処理や管理をサーバ側に集約する考え方です。"
    },
    vdi: {
      target: "server",
      client: ["キーボード・マウス操作を送信", "仮想デスクトップの画面を表示"],
      server: ["利用者ごとの仮想デスクトップ", "仮想環境内でOS・アプリを実行", "業務データを管理"],
      explanation: "VDIはサーバ上に仮想デスクトップを作り、その画面を端末から操作する仕組みです。一般的なPCからも利用できます。"
    }
  };
  function setup() {
    var root = document.getElementById("fe-thin-client-demo");
    if (!root || root.dataset.ready === "true") return;
    var modes = Array.prototype.slice.call(root.querySelectorAll("[data-mode]"));
    var guesses = Array.prototype.slice.call(root.querySelectorAll('input[name="fe-thin-client-guess"]'));
    var result = root.querySelector("[data-result]");
    var feedback = root.querySelector("[data-feedback]");
    var client = root.querySelector("[data-client]");
    var server = root.querySelector("[data-server]");
    var explanation = root.querySelector("[data-explanation]");
    var reveal = root.querySelector("[data-reveal]");
    var reset = root.querySelector("[data-reset]");
    if (modes.length !== 3 || guesses.length !== 2 || !result || !feedback || !client || !server || !explanation || !reveal || !reset) return;
    var mode = "fat";
    function populate(list, items) {
      list.replaceChildren();
      items.forEach(function (item) {
        var li = document.createElement("li");
        li.textContent = item;
        list.appendChild(li);
      });
    }
    function choose(next) {
      if (!cases[next]) return;
      mode = next;
      modes.forEach(function (button) {
        button.setAttribute("aria-pressed", String(button.dataset.mode === mode));
      });
      guesses.forEach(function (input) { input.checked = false; });
      result.hidden = true;
      feedback.textContent = "";
      client.replaceChildren();
      server.replaceChildren();
      explanation.textContent = "";
    }
    function show() {
      var selected = guesses.find(function (input) { return input.checked; });
      var config = cases[mode];
      var correctText = config.target === "client" ? "端末側" : "サーバ側";
      populate(client, config.client);
      populate(server, config.server);
      feedback.textContent = selected
        ? (selected.value === config.target ? "予想どおり！ " : "ここを確認しましょう。 ") + "アプリの主な実行場所は「" + correctText + "」です。"
        : "アプリの主な実行場所は「" + correctText + "」です。";
      explanation.textContent = config.explanation;
      result.hidden = false;
    }
    modes.forEach(function (button) { button.addEventListener("click", function () { choose(button.dataset.mode); }); });
    reveal.addEventListener("click", show);
    reset.addEventListener("click", function () { choose("fat"); });
    choose("fat");
    root.dataset.ready = "true";
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
}());
