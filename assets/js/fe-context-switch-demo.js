(() => {
  "use strict";
  const steps = [
    {
      label: "開始：Aを実行中", cpu: "CPU：Aを実行中（PC=120）",
      a: "A：実行状態（PC=120）", b: "B：実行可能状態（保存済みPC=320）",
      action: "タイマー割込みが発生する前の状態です。",
      note: "予想：Aの処理を後から再開するには何を残す必要がありますか？"
    },
    {
      label: "① Aの実行状態を退避", cpu: "OS：切替え処理中（AのPC=120を保存）",
      a: "A：実行可能状態（PC=120を保存）", b: "B：実行可能状態（保存済みPC=320）",
      action: "AのPCなどを退避して、あとから続きを再開できるようにします。",
      note: "確認：Aは終了せず、CPUの次の順番を待ちます。"
    },
    {
      label: "② 次に実行するBを選択", cpu: "OS：Bを次の実行対象に選択",
      a: "A：実行可能状態（PC=120を保存）", b: "B：実行対象に選択（保存済みPC=320）",
      action: "OSのスケジューラが実行可能なBを選びます。",
      note: "確認：まだBの状態をCPUへ回復していません。"
    },
    {
      label: "③ Bの実行状態を回復", cpu: "OS：Bの保存済みPC=320などを復元",
      a: "A：実行可能状態（PC=120を保存）", b: "B：実行再開の準備（PC=320を回復）",
      action: "Bの命令位置やレジスタなど、再開に必要な状態をCPUへ復元します。",
      note: "確認：AのPC=120は保存されたままです。"
    },
    {
      label: "完了：Bを実行中", cpu: "CPU：Bを実行中（PC=320から再開）",
      a: "A：実行可能状態（PC=120を保存）", b: "B：実行状態（PC=320から再開）",
      action: "CPUの使用権がAからBへ移りました。",
      note: "結論：Aを退避 → Bを選択 → Bを回復。Bが実行を再開しました。"
    }
  ];
  function start(root) {
    const el = (name) => root.querySelector("[data-context-" + name + "]");
    const step = el("step"), cpu = el("cpu"), a = el("a"), b = el("b");
    const action = el("action"), note = el("note");
    const next = el("next"), back = el("back"), reset = el("reset");
    if ([step,cpu,a,b,action,note,next,back,reset].some((e) => !e)) return;
    let index = 0;
    const render = () => {
      const item = steps[index];
      step.textContent = "段階 " + (index + 1) + " / " + steps.length + "： " + item.label;
      cpu.textContent = item.cpu;
      a.textContent = item.a;
      b.textContent = item.b;
      action.textContent = item.action;
      note.textContent = item.note;
      back.disabled = index === 0;
      next.disabled = index === steps.length - 1;
      next.textContent = index < steps.length - 1 ? "次へ：" + steps[index + 1].label.replace(/^[①②③] /,"") : "すべて完了";
    };
    next.addEventListener("click", () => { if (index < steps.length - 1) { index += 1; render(); } });
    back.addEventListener("click", () => { if (index > 0) { index -= 1; render(); } });
    reset.addEventListener("click", () => { index = 0; render(); });
    render();
  }
  const init = () => document.querySelectorAll("[data-fe-context-demo]").forEach(start);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
