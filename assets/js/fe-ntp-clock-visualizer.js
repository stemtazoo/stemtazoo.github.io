/* NTP four-timestamp demo. All timestamps are device-local clock readings in μs. */
(function () {
  "use strict";
  function setup() {
    var root = document.getElementById("fe-ntp-clock-demo");
    if (!root || root.dataset.ready === "true") return;
    var offsetInput = root.querySelector("[data-offset]");
    var processInput = root.querySelector("[data-process]");
    var interactive = root.querySelector("[data-interactive]");
    var fallback = root.querySelector("[data-fallback]");
    if (!offsetInput || !processInput || !interactive || !fallback) return;
    var fields = {};
    ["offset-value","process-value","t1","t2","t3","t4","apparent-forward","apparent-return","roundtrip","server-process","network-roundtrip","oneway","offset-result","explanation"].forEach(function (name) {
      fields[name] = root.querySelector('[data-field="' + name + '"]');
    });
    if (Object.keys(fields).some(function (key) { return !fields[key]; })) return;
    function put(name, value) { fields[name].textContent = String(value); }
    function render() {
      var offset = Number(offsetInput.value); // PC reading minus server reading, at the same instant
      var processing = Number(processInput.value);
      var delay = 300; // symmetric one-way network delay, fixed for this demonstration
      var t1 = 100; // PC clock at query transmission
      var t2 = t1 + delay - offset; // server clock at query reception
      var t3 = t2 + processing; // server clock at response transmission
      var t4 = t1 + 2 * delay + processing; // PC clock at response reception
      var apparentForward = t2 - t1;
      var apparentReturn = t4 - t3;
      var roundtrip = t4 - t1;
      var networkRoundtrip = roundtrip - (t3 - t2);
      var oneWay = networkRoundtrip / 2;
      var estimatedOffset = apparentReturn - oneWay; // PC is ahead when positive
      put("offset-value", (offset > 0 ? "+" : "") + offset + " μs");
      put("process-value", processing + " μs");
      put("t1", t1);
      put("t2", t2);
      put("t3", t3);
      put("t4", t4);
      put("apparent-forward", t2 + " − " + t1 + " = " + apparentForward);
      put("apparent-return", t4 + " − " + t3 + " = " + apparentReturn);
      put("roundtrip", t4 + " − " + t1 + " = " + roundtrip);
      put("server-process", t3 + " − " + t2 + " = " + processing);
      put("network-roundtrip", roundtrip + " − " + processing + " = " + networkRoundtrip);
      put("oneway", networkRoundtrip + " ÷ 2 = " + oneWay);
      put("offset-result", apparentReturn + " − " + oneWay + " = " + (estimatedOffset > 0 ? "+" : "") + estimatedOffset + " μs");
      put("explanation", offset > 0 ? "同じ瞬間ならPCがサーバより" + offset + " μs進んでいます。復路の見かけの差は実際の通信遅延より長くなります。" : offset < 0 ? "同じ瞬間ならPCがサーバより" + Math.abs(offset) + " μs遅れています。復路の見かけの差は実際の通信遅延より短くなります。" : "2台の時計は一致しています。往路・復路の見かけの差は、どちらも実際の片道通信遅延と一致します。");
    }
    offsetInput.addEventListener("input", render);
    processInput.addEventListener("input", render);
    root.querySelector("[data-zero-process]").addEventListener("click", function () {
      processInput.value = "0";
      render();
    });
    root.querySelector("[data-reset]").addEventListener("click", function () {
      offsetInput.value = "200";
      processInput.value = "200";
      render();
    });
    render();
    interactive.hidden = false;
    fallback.hidden = true;
    root.dataset.ready = "true";
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", setup);
  else setup();
}());
