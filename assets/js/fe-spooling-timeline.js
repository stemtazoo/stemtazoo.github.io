(() => {
  "use strict";
  const defaults = [[30, 45], [20, 15], [40, 25]];
  const jobs = ["A", "B", "C"];
  const colors = ["#b6d5ed", "#b7dfc1", "#f0d8a5"];
  function calculate(values) {
    let cpuEnd = 0, printEnd = 0;
    return values.map(([cpu, print], i) => {
      const cpuStart = cpuEnd;
      cpuEnd += cpu;
      const printStart = Math.max(cpuEnd, printEnd);
      const wait = printStart - cpuEnd;
      printEnd = printStart + print;
      return { name: jobs[i], cpu, print, cpuStart, cpuEnd, printStart, printEnd, wait };
    });
  }
  const node = (tag, text, className) => {
    const el = document.createElement(tag);
    if (text !== null && text !== undefined) el.textContent = String(text);
    if (className) el.className = className;
    return el;
  };
  function setup(root) {
    const cpuInputs = jobs.map((_, i) => root.querySelector('[data-spool-cpu="' + i + '"]'));
    const printInputs = jobs.map((_, i) => root.querySelector('[data-spool-print="' + i + '"]'));
    const run = root.querySelector("[data-spool-run]");
    const reset = root.querySelector("[data-spool-reset]");
    const notice = root.querySelector("[data-spool-notice]");
    const output = root.querySelector("[data-spool-output]");
    if ([...cpuInputs, ...printInputs, run, reset, notice, output].some((x) => !x)) return;
    [...cpuInputs, ...printInputs].forEach((input) => input.addEventListener("input", () => {
      output.replaceChildren();
      notice.textContent = "数値が変わりました。終了時刻を予想してから再計算してください。";
    }));
    run.addEventListener("click", () => {
      const values = jobs.map((_, i) => [Number(cpuInputs[i].value), Number(printInputs[i].value)]);
      if (values.some((pair) => pair.some((n) => !Number.isInteger(n) || n < 1 || n > 120))) {
        output.replaceChildren();
        notice.textContent = "各時間を1～120秒の整数で入力してください。";
        return;
      }
      const rows = calculate(values);
      const total = rows[rows.length - 1].printEnd;
      const cpuLast = rows[rows.length - 1].cpuEnd;
      const serial = rows.reduce((sum, x) => sum + x.cpu + x.print, 0);
      output.replaceChildren();
      const summary = node("p", "CPU終了 " + cpuLast + "秒 ／ 全印刷完了 " + total + "秒 ／ 全処理を直列に足すと " + serial + "秒", "fe-spool-time__summary");
      output.appendChild(summary);
      const chart = node("div", null, "fe-spool-time__chart");
      chart.setAttribute("role", "img");
      chart.setAttribute("aria-label", "CPUとプリンターの時間帯。詳細は下の表を参照してください。");
      [["CPU", "cpuStart", "cpuEnd"], ["プリンター", "printStart", "printEnd"]].forEach(([label, begin, end]) => {
        const lane = node("div", null, "fe-spool-time__lane");
        lane.appendChild(node("span", label, "fe-spool-time__lane-label"));
        const track = node("div", null, "fe-spool-time__track");
        rows.forEach((r, i) => {
          const bar = node("span", null, "fe-spool-time__bar");
          bar.style.left = (r[begin] / total * 100) + "%";
          bar.style.width = ((r[end] - r[begin]) / total * 100) + "%";
          bar.style.backgroundColor = colors[i];
          bar.title = r.name + " " + r[begin] + "～" + r[end] + "秒";
          bar.setAttribute("aria-hidden", "true");
          track.appendChild(bar);
        });
        lane.appendChild(track);
        chart.appendChild(lane);
      });
      output.appendChild(chart);
      output.appendChild(node("p", "横棒は左からA・B・Cの順です。A＝水色、B＝緑、C＝黄。各時刻は次の表で確認できます。", "fe-spool-time__legend"));
      const wrap = node("div", null, "fe-spool-time__table-wrap");
      const table = node("table", null, "fe-spool-time__table");
      const head = node("thead");
      const hr = node("tr");
      ["ジョブ", "CPU時間帯", "印刷時間帯", "印刷待ち"].forEach((s) => hr.appendChild(node("th", s)));
      head.appendChild(hr); table.appendChild(head);
      const body = node("tbody");
      rows.forEach((r) => {
        const tr = node("tr");
        [r.name, r.cpuStart + "～" + r.cpuEnd, r.printStart + "～" + r.printEnd, r.wait + "秒"].forEach((s) => tr.appendChild(node("td", s)));
        body.appendChild(tr);
      });
      table.appendChild(body); wrap.appendChild(table); output.appendChild(wrap);
      const note = rows.map((r) => r.name + "はCPUが" + r.cpuEnd + "秒で終わり、印刷は" + r.printStart + "秒に開始（待ち" + r.wait + "秒）").join("。");
      output.appendChild(node("p", note + "。最後の印刷終了は" + total + "秒です。", "fe-spool-time__reason"));
      notice.textContent = "計算しました。CPUと印刷が同時に動く区間を確認しましょう。";
    });
    reset.addEventListener("click", () => {
      defaults.forEach(([cpu, print], i) => {
        cpuInputs[i].value = String(cpu);
        printInputs[i].value = String(print);
      });
      output.replaceChildren();
      notice.textContent = "初期値に戻しました。全印刷完了時刻を予想してから計算してください。";
    });
  }
  function init() { document.querySelectorAll("[data-fe-spool-time]").forEach(setup); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
