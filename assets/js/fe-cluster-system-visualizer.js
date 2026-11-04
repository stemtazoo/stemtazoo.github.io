/* FE cluster system: deterministic, accessible three-mode comparison. */
(function () {
  "use strict";
  function setup() {
    var root = document.getElementById("fe-cluster-demo");
    if (!root || root.dataset.ready === "true") return;
    var modes = Array.prototype.slice.call(root.querySelectorAll("[data-mode]"));
    var nodes = Array.prototype.slice.call(root.querySelectorAll("[data-node]"));
    var question = root.querySelector("[data-question]");
    var status = root.querySelector("[data-status]");
    var reason = root.querySelector("[data-reason]");
    var toggle = root.querySelector("[data-toggle]");
    var reset = root.querySelector("[data-reset]");
    if (modes.length !== 3 || nodes.length !== 3 || !question || !status || !reason || !toggle || !reset) return;
    var mode = "load", failed = false;
    var scenarios = {
      load: {
        question: "サーバ1が故障すると、残り2台の負荷はどうなる？",
        before: [["稼働中","30件の要求"],["稼働中","30件の要求"],["稼働中","30件の要求"]],
        after: [["故障","処理できない"],["稼働中","45件の要求"],["稼働中","45件の要求"]],
        statusBefore: "通常時：3台で90件を分担し、各30件を処理しています。",
        statusAfter: "故障後：残り2台が合計90件を分担し、各45件になりました。",
        reasonBefore: "見るポイント：普段から要求を振り分けています。",
        reasonAfter: "判断：30件→45件に負荷が増えました。残りのサーバに余力がなければ処理能力が不足する場合があります。"
      },
      failover: {
        question: "現用系のサーバ1が故障したとき、処理を担当するのは？",
        before: [["現用系","業務処理中"],["待機系","待機中"],["予備（未使用）","待機中"]],
        after: [["故障","処理できない"],["新しい現用系","業務を引継ぎ"],["予備（未使用）","待機中"]],
        statusBefore: "通常時：サーバ1が処理し、サーバ2と3は待機しています。",
        statusAfter: "故障後：サーバ2が待機系から現用系に切り替わりました。",
        reasonBefore: "見るポイント：負荷分散とは異なり、平常時の業務をサーバ1が担当します。",
        reasonAfter: "判断：現用系から待機系へ処理を引き継ぐのがフェールオーバーです。切替え中に短い停止が生じることもあります。"
      },
      hpc: {
        question: "並列計算中に計算ノード1が故障したら、ジョブは必ず継続する？",
        before: [["計算中","計算タスクA"],["計算中","計算タスクB"],["計算中","計算タスクC"]],
        after: [["故障","タスクA中断"],["稼働中","タスクB"],["稼働中","タスクC"]],
        statusBefore: "通常時：3ノードが異なるタスクを並列に計算しています。",
        statusAfter: "故障後：ノード1のタスクAが中断しました。この例ではジョブ全体の完了に支障が生じます。",
        reasonBefore: "見るポイント：HPCの主目的は計算の高速化です。",
        reasonAfter: "判断：残りのノードが動いていても、ジョブが自動で継続できるとは限りません。復旧は別の仕組みに依存します。"
      }
    };
    function render() {
      var scenario = scenarios[mode];
      var data = failed ? scenario.after : scenario.before;
      modes.forEach(function (button) { button.setAttribute("aria-pressed", String(button.dataset.mode === mode)); });
      nodes.forEach(function (node, index) {
        var role = data[index][0];
        node.classList.toggle("is-failed", role === "故障");
        node.classList.toggle("is-standby", role.indexOf("待機") !== -1 || role.indexOf("予備") !== -1);
        node.querySelector("[data-role]").textContent = role;
        node.querySelector("[data-work]").textContent = data[index][1];
      });
      question.textContent = scenario.question;
      status.textContent = failed ? scenario.statusAfter : scenario.statusBefore;
      reason.textContent = failed ? scenario.reasonAfter : scenario.reasonBefore;
      toggle.textContent = failed ? "サーバ1を復旧する" : "サーバ1を故障させる";
    }
    modes.forEach(function (button) {
      button.addEventListener("click", function () {
        if (!scenarios[button.dataset.mode]) return;
        mode = button.dataset.mode;
        failed = false;
        render();
      });
    });
    toggle.addEventListener("click", function () { failed = !failed; render(); });
    reset.addEventListener("click", function () { mode = "load"; failed = false; render(); });
    render();
    root.dataset.ready = "true";
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
}());
