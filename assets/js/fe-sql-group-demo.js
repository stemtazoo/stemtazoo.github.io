(function () {
  "use strict";
  const root = document.getElementById("fe-group-demo");
  if (!root) return;
  const $ = (selector) => root.querySelector(selector);
  const inputRows = [
    { date: "8月1日", qty: 10 }, { date: "8月1日", qty: 20 },
    { date: "8月2日", qty: 15 }, { date: "8月2日", qty: 5 },
    { date: "8月3日", qty: 8 }
  ];
  const where = $("#fe-group-where"), having = $("#fe-group-having");
  const kind = $("#fe-group-kind"), guess = $("#fe-group-guess");
  const next = $("#fe-group-next"), back = $("#fe-group-back"), reset = $("#fe-group-reset");
  const stageLabel = $("#fe-group-stage"), feedback = $("#fe-group-feedback");
  const explanation = $("#fe-group-explanation"), table = $("#fe-group-table");
  const sql = $("#fe-group-sql");
  let stage = 0, lastFeedback = "";
  const stages = ["FROM：元データ", "WHERE：集計前の行", "GROUP BY：日付別集計", "HAVING：集計後のグループ", "SELECT：最終結果"];
  function compute() {
    const threshold = Number(where.value), limit = Number(having.value);
    const rows = inputRows.filter((r) => r.qty >= threshold);
    const map = new Map();
    rows.forEach((r) => {
      if (!map.has(r.date)) map.set(r.date, []);
      map.get(r.date).push(r.qty);
    });
    const grouped = Array.from(map, ([date, qtys]) => {
      const sum = qtys.reduce((a, b) => a + b, 0);
      const aggregate = kind.value === "SUM" ? sum : kind.value === "COUNT" ? qtys.length : sum / qtys.length;
      return { date, values: qtys.join("、"), aggregate, count: qtys.length };
    });
    return { rows, grouped, selected: grouped.filter((g) => g.aggregate > limit) };
  }
  function format(v) { return String(Number(v.toFixed(2))); }
  function renderTable(headers, entries) {
    table.replaceChildren();
    const thead = document.createElement("thead"), headerRow = document.createElement("tr");
    headers.forEach((h) => { const th = document.createElement("th"); th.scope = "col"; th.textContent = h; headerRow.appendChild(th); });
    thead.appendChild(headerRow); table.appendChild(thead);
    const tbody = document.createElement("tbody");
    entries.forEach((entry) => {
      const tr = document.createElement("tr"); tr.setAttribute("data-selected", String(entry.selected));
      entry.cells.forEach((v) => { const td = document.createElement("td"); td.textContent = String(v); tr.appendChild(td); });
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
  }
  function display(message) {
    const state = compute();
    stageLabel.textContent = (stage + 1) + " / 5　" + stages[stage];
    next.disabled = stage === 4; back.disabled = stage === 0;
    guess.disabled = stage !== 0;
    const fn = kind.value + "(数量)";
    sql.textContent = "SELECT 注文日, " + fn + "\nFROM 注文明細\nWHERE 数量 >= " + where.value
      + "\nGROUP BY 注文日\nHAVING " + fn + " > " + having.value + ";";
    if (stage === 0) {
      renderTable(["注文日", "数量"], inputRows.map((r) => ({ selected:true, cells:[r.date,r.qty] })));
      explanation.textContent = "元の5行を確認します。WHEREの条件はまだ適用していません。";
    } else if (stage === 1) {
      renderTable(["注文日", "数量"], inputRows.map((r) => ({selected:r.qty >= Number(where.value), cells:[r.date,r.qty]})));
      explanation.textContent = "WHERE 数量 >= " + where.value + "：条件に合わない行を灰色にしています。残るのは"+state.rows.length+"行です。";
    } else {
      const chosen = stage < 3 ? state.grouped : state.selected;
      renderTable(stage === 2 ? ["注文日", "残った数量",fn] : ["注文日",fn],
        (stage === 2 ? state.grouped : state.grouped).map((r) => ({
          selected:stage === 2 || r.aggregate > Number(having.value),
          cells:stage === 2 ? [r.date,r.values,format(r.aggregate)] : [r.date,format(r.aggregate)]
        })).filter((r) => stage !== 4 || r.selected));
      explanation.textContent = stage === 2
        ? "WHEREを通った行だけを日付ごとにまとめて"+kind.value+"を計算します。グループ数は"+state.grouped.length+"です。"
        : stage === 3
          ? "HAVING "+fn+" > "+having.value+"：集計後のグループを絞ります。残るのは"+state.selected.length+"グループです。"
          : "SELECTで最終結果を表示します。結果は"+state.selected.length+"グループ（0なら該当なし）です。";
    }
    feedback.textContent = message || (stage === 0 ? "最終結果のグループ数を予想しましょう。" : "各段階で、どの行やグループが対象か確認しましょう。");
  }
  function change() { stage = 0; guess.value = ""; display("条件を変更しました。新しい結果を予想しましょう。"); }
  [where,having,kind].forEach((field) => field.addEventListener("change", change));
  next.addEventListener("click", () => {
    if (stage >= 4) return;
    const prediction = guess.value;
    stage++;
    if (stage === 4) {
      const actual = String(compute().selected.length);
      const message = prediction === "" ? "予想を省略しました。" :
        prediction === actual ? "予想正解！" : "予想とは異なりました。";
      display(message+" 最終結果は"+actual+"グループです。");
    } else display("次の処理段階に進みました。");
  });
  back.addEventListener("click", () => { if (stage === 0) return; stage--; display("前の処理段階に戻りました。"); });
  reset.addEventListener("click", () => {
    where.value = "0"; having.value = "0"; kind.value = "SUM";
    stage = 0; guess.value = ""; display("初期設定へ戻しました。");
  });
  display();
})();
