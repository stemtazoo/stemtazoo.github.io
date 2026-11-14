(() => {
  "use strict";
  const names = {stopped:"停止中", running:"運転中", fault:"異常停止"};
  const events = {start:"開始", stop:"停止", alarm:"異常検知", reset:"安全確認後のリセット"};
  const valid = {
    "stopped:start":"running",
    "running:stop":"stopped",
    "running:alarm":"fault",
    "fault:reset":"stopped"
  };
  function init() {
    document.querySelectorAll("[data-fe-state-test]").forEach((root) => {
      const state = root.querySelector("[data-stt-state]");
      const event = root.querySelector("[data-stt-event]");
      const bug = root.querySelector("[data-stt-bug]");
      const run = root.querySelector("[data-stt-run]");
      const reset = root.querySelector("[data-stt-reset]");
      const result = root.querySelector("[data-stt-result]");
      if (![state,event,bug,run,reset,result].every(Boolean)) return;
      const display = (message, fail) => {
        result.replaceChildren();
        const p = document.createElement("p");
        p.textContent = message;
        result.appendChild(p);
        result.classList.toggle("is-fail", Boolean(fail));
        result.classList.toggle("is-pass", fail === false);
      };
      function clearResult() {
        display("条件を変更しました。「テスト実行」を押して期待状態と実際の状態を確認してください。", null);
      }
      function test() {
        const key = state.value + ":" + event.value;
        const specified = Object.hasOwn(valid,key) || key === "fault:start";
        if (!specified) {
          display("この組合せは学習用仕様表に動作を定義していません。結果を勝手に「状態変化なし」とみなさず、仕様を確認してください。", null);
          return;
        }
        const expected = valid[key] || state.value;
        const actual = bug.checked && key === "fault:start" ? "running" : expected;
        const passed = actual === expected;
        const kind = Object.hasOwn(valid,key) ? "許可された遷移" : "禁止された遷移";
        const message = "現在状態：" + names[state.value] + " ／ イベント：" + events[event.value] +
          " ／ " + kind +
          " ／ 期待状態：" + names[expected] +
          " ／ 実際の状態：" + names[actual] +
          " ／ 判定：" + (passed ? "合格（一致）" : "不合格（不一致）");
        display(message, !passed);
      }
      state.addEventListener("change",clearResult);
      event.addEventListener("change",clearResult);
      bug.addEventListener("change",clearResult);
      run.addEventListener("click",test);
      reset.addEventListener("click",() => {
        state.value="stopped"; event.value="start"; bug.checked=false;
        display("初期条件に戻しました。停止中＋開始のテストを実行してみましょう。",null);
      });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded",init);
  else init();
})();
