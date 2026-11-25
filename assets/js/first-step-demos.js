(() => {
  "use strict";

  function renderList(board, items) {
    board.replaceChildren(...items.map(text => {
      const item = document.createElement("li");
      item.textContent = text;
      return item;
    }));
  }

  function raid(root, board, result, button) {
    const modes = {
      "0": {
        disks: ["データ A", "データ B"],
        result: "復元できません。ディスク1のデータAを補う情報がありません。"
      },
      "1": {
        disks: ["データ A", "データ A の複製"],
        result: "復元できます。ディスク2にデータAの複製があります。"
      },
      "5": {
        disks: ["データ A", "データ B", "パリティ P"],
        result: "復元できます。残ったデータBとパリティPからデータAを求められます。"
      }
    };
    let failed = false;

    function draw() {
      const mode = root.querySelector("input:checked").value;
      const layout = modes[mode];
      renderList(board, layout.disks.map((disk, i) =>
        "ディスク" + (i + 1) + (failed && i === 0 ? "：故障（読めない）" : "：" + disk)));
      board.firstElementChild.classList.toggle("is-failed", failed);
      result.textContent = failed ? layout.result : "全ディスクが正常です。";
      button("fail").disabled = failed;
      button("reset").disabled = !failed;
    }

    root.addEventListener("change", draw);
    button("fail").addEventListener("click", () => { failed = true; draw(); });
    button("reset").addEventListener("click", () => { failed = false; draw(); });
    draw();
  }

  function join(root, board, result) {
    const clause = root.querySelector("[data-join-clause]");

    function draw() {
      const on = root.querySelector("input:checked").value === "on";
      clause.textContent = (on ? " AND" : "WHERE") + " P.status = 'active';";
      const rows = ["佐藤：進行中の案件"];
      if (on) rows.push("鈴木：NULL", "田中：NULL");
      renderList(board, rows);
      result.textContent = on
        ? "3行。ONで結合相手を絞っても、左側の社員は全員残ります。"
        : "1行。WHEREで結合後に絞るため、案件がない鈴木と終了済み案件の田中は結果から外れます。";
    }

    root.addEventListener("change", draw);
    draw();
  }

  function kmeans(root, board, result, button) {
    const points = [1, 2, 4, 6, 9, 10];
    const labels = ["A", "B"];
    const colors = ["#145ea8", "#9d4b12"];
    const position = value => 20 + value * 25;
    let centers;
    let assignments;
    let phase;

    function draw(message) {
      const pointMarks = points.map((point, i) => {
        const group = assignments[i];
        const x = position(point);
        return '<circle cx="' + x + '" cy="55" r="5" fill="' + (colors[group] ?? "#667085") + '"/>'
          + '<text x="' + x + '" y="76">' + point + '</text>'
          + (group === undefined ? "" : '<text x="' + x + '" y="95">' + labels[group] + '</text>');
      });
      const centerMarks = centers.map((center, i) => {
        const x = position(center);
        return '<line x1="' + x + '" x2="' + x + '" y1="26" y2="48" stroke="' + colors[i] + '" stroke-width="2"/>'
          + '<text x="' + x + '" y="19">中心' + labels[i] + '</text>';
      });
      board.innerHTML = '<path d="M20 55H270" fill="none" stroke="#7b8795"/>'
        + pointMarks.join("") + centerMarks.join("");
      const displayedCenters = centers.map((center, i) =>
        labels[i] + "＝" + Number(center.toFixed(2))).join("、");
      board.setAttribute("aria-label", "数直線。中心 " + displayedCenters + "。" + message);
      result.textContent = "中心 " + displayedCenters + "。" + message;
      button("next").textContent = phase === "update" ? "重心を更新する" : "近い中心に割り当てる";
      button("next").disabled = phase === "done";
    }

    function reset() {
      centers = [1, 4];
      assignments = [];
      phase = "assign";
      draw("まだどの点も割り当てていません。");
    }

    button("next").addEventListener("click", () => {
      if (phase === "update") {
        centers = centers.map((center, group) => {
          const members = points.filter((_, i) => assignments[i] === group);
          return members.reduce((sum, point) => sum + point, 0) / members.length;
        });
        phase = "assign";
        draw("所属はそのままで、中心を各グループの平均へ移しました。");
        return;
      }
      const next = points.map(point =>
        Math.abs(point - centers[0]) <= Math.abs(point - centers[1]) ? 0 : 1);
      const stable = next.every((group, i) => group === assignments[i]);
      assignments = next;
      phase = stable ? "done" : "update";
      const groups = labels.map((label, group) => label + "は" +
        points.filter((_, i) => assignments[i] === group).join("・")).join("、");
      draw(groups + (stable ? "。所属が変わらないため完了です。" : "です。"));
    });

    button("reset").addEventListener("click", reset);
    reset();
  }

  function time(root, board, result, button) {
    let validation = 4;

    function draw() {
      const mixed = root.querySelector("input:checked").value === "mixed";
      const testMonth = mixed ? 2 : validation;
      const months = Array.from({length: 6}, (_, i) => i + 1);
      renderList(board, months.map(month => {
        let role = "未使用";
        if (month === testMonth) role = "検証";
        else if (mixed && month > testMonth) role = "学習（未来）";
        else if (month < testMonth) role = "学習";
        return month + "月：" + role;
      }));
      result.textContent = mixed
        ? "2月を検証するとき、3〜6月を学習に使うと未来の情報が混ざります。"
        : "1〜" + (validation - 1) + "月で学習し、" + validation + "月で検証します。";
      button("next").disabled = mixed || validation === 6;
      button("reset").disabled = !mixed && validation === 4;
    }

    root.addEventListener("change", () => { validation = 4; draw(); });
    button("next").addEventListener("click", () => { validation += 1; draw(); });
    button("reset").addEventListener("click", () => {
      root.querySelector('input[value="time"]').checked = true;
      validation = 4;
      draw();
    });
    draw();
  }

  function hamming(root, board, result, button) {
    const transmitted = [0, 1, 1, 0, 0, 1, 1];
    const checks = [1, 2, 4];
    const checkList = root.querySelector("[data-checks]");
    let flipped = 0;
    let syndrome = 0;

    const buttons = transmitted.map((_, index) => {
      const element = document.createElement("button");
      element.type = "button";
      element.dataset.bit = String(index + 1);
      element.addEventListener("click", () => {
        flipped = flipped === index + 1 ? 0 : index + 1;
        draw();
      });
      return element;
    });
    board.append(...buttons);

    function draw(corrected = 0) {
      const received = transmitted.map((bit, index) => flipped === index + 1 ? 1 - bit : bit);
      buttons.forEach((element, index) => {
        element.textContent = (index + 1) + "：" + received[index];
        element.setAttribute("aria-label", "位置" + (index + 1) + "、値" + received[index]);
        element.setAttribute("aria-pressed", String(flipped === index + 1));
      });
      const failed = [];
      renderList(checkList, checks.map(check => {
        const positions = received.map((_, index) => index + 1).filter(position => position & check);
        const ones = positions.reduce((sum, position) => sum + received[position - 1], 0);
        if (ones % 2) failed.push(check);
        return "検査" + check + "（位置" + positions.join("・") + "）：" + (ones % 2 ? "不一致" : "一致");
      }));
      syndrome = failed.reduce((sum, check) => sum + check, 0);
      button("correct").disabled = syndrome === 0;
      if (syndrome) {
        result.textContent = failed.join("＋") + " → 誤りは位置" + syndrome + "です。";
      } else {
        result.textContent = (corrected ? "位置" + corrected + "を訂正しました。" : "すべての検査が一致しています。")
          + "受信ビット列：" + received.join("");
      }
    }

    button("correct").addEventListener("click", () => {
      const error = syndrome;
      if (error === 0) return;
      flipped = 0;
      draw(error);
      buttons[error - 1].focus();
    });
    button("reset").addEventListener("click", () => { flipped = 0; draw(); });
    draw();
  }

  const lessons = {raid, join, kmeans, time, hamming};
  document.querySelectorAll("[data-first-step]").forEach(root => {
    const mount = lessons[root.dataset.firstStep];
    if (!mount) return;
    mount(root, root.querySelector("[data-board]"), root.querySelector("[data-result]"),
      action => root.querySelector('[data-action="' + action + '"]'));
    root.hidden = false;
  });
})();
