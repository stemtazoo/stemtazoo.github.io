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
    const next = button("next");
    const fixedReason = root.querySelector("[data-fixed-reason]");
    const isMixed = () => root.querySelector("input:checked").value === "mixed";
    let validation = 4;

    function draw() {
      const mixed = isMixed();
      fixedReason.textContent = "";
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
      next.textContent = mixed ? "固定例の理由を見る" : "次の分割";
      next.disabled = !mixed && validation === 6;
      button("reset").disabled = !mixed && validation === 4;
    }

    root.addEventListener("change", () => { validation = 4; draw(); });
    next.addEventListener("click", () => {
      if (isMixed()) {
        fixedReason.textContent = "2月より後の3〜6月が学習に混ざる様子を時間順の分割と比べられるよう、この例では月の配置を固定しています。";
        return;
      }
      validation += 1;
      draw();
    });
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
    const receivedCode = root.querySelector("[data-received]");
    const guide = root.querySelector("[data-hamming-guide]");
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

    function draw(message = "すべての検査が一致しています。") {
      const received = transmitted.map((bit, index) => flipped === index + 1 ? 1 - bit : bit);
      buttons.forEach((element, index) => {
        element.textContent = "位置" + (index + 1) + "：" + received[index];
        element.setAttribute("aria-label", "位置" + (index + 1) + "、値" + received[index]);
        element.setAttribute("aria-pressed", String(flipped === index + 1));
      });
      const failed = [];
      renderList(checkList, checks.map(check => {
        const positions = received.map((_, index) => index + 1).filter(position => position & check);
        const bits = positions.map(position => received[position - 1]);
        const ones = bits.reduce((sum, bit) => sum + bit, 0);
        const odd = ones % 2 === 1;
        if (odd) failed.push(check);
        return "検査" + check + "（位置" + positions.join("・") + "）："
          + bits.join("") + " → 1が" + ones + "個（" + (odd ? "奇数）→ 不一致" : "偶数）→ 一致");
      }));
      syndrome = failed.reduce((sum, check) => sum + check, 0);
      receivedCode.textContent = received.join("");
      button("correct").disabled = syndrome === 0;
      guide.textContent = syndrome
        ? "不一致になった検査の内訳を見てから「誤りを訂正」を押してください。"
        : "「位置6：1」を押して、左から6番目のビットを反転させてください。";
      const binary = syndrome.toString(2).padStart(3, "0");
      result.textContent = syndrome
        ? "検査4・2・1の結果は " + binary + "（不一致＝1）。"
          + failed.slice().reverse().join("＋") + "＝" + syndrome + " → 左から位置" + syndrome + "です。"
        : message;
    }

    button("correct").addEventListener("click", () => {
      const error = syndrome;
      if (error === 0) return;
      flipped = 0;
      draw("位置" + error + "を訂正しました。すべての検査が一致しています。");
      buttons[error - 1].focus();
    });
    button("reset").addEventListener("click", () => {
      flipped = 0;
      draw("最初の状態に戻しました。「位置6：1」から試せます。");
    });
    draw();
  }

  function conditional(root, board, result) {
    const labels = ["会員・利用あり：24件", "会員・利用なし：56件",
      "非会員・利用あり：16件", "非会員・利用なし：104件"];
    const cases = {
      all: {den: [0, 1, 2, 3], num: [0, 2], label: "全体でクーポン利用あり"},
      member: {den: [0, 1], num: [0], label: "会員の注文のうちクーポン利用あり"},
      coupon: {den: [0, 2], num: [0], label: "クーポン利用ありのうち会員"}
    };
    const counts = [24, 56, 16, 104];
    const sum = indexes => indexes.reduce((total, i) => total + counts[i], 0);

    function draw() {
      const {den, num, label} = cases[root.querySelector("input:checked").value];
      renderList(board, labels.map((text, i) =>
        text + "（" + (num.includes(i) ? "分子・分母" : den.includes(i) ? "分母" : "対象外") + "）"));
      Array.from(board.children).forEach((card, i) => {
        card.classList.toggle("is-included", den.includes(i));
        card.classList.toggle("is-selected", num.includes(i));
      });
      const numerator = sum(num), denominator = sum(den);
      result.textContent = label + "：分子" + numerator + " ÷ 分母" + denominator
        + " ＝ " + (100 * numerator / denominator) + "%";
    }

    root.addEventListener("change", draw);
    draw();
  }

  function markov(root, board, result, button) {
    const calculation = root.querySelector("[data-calculation]");
    const format = value => Number(value.toFixed(3)).toString();
    let time, a, b;

    function draw(previous) {
      renderList(board, ["状態A：" + format(a * 100) + "%", "状態B：" + format(b * 100) + "%"]);
      const graphValues = {
        "[data-markov-time]": "時点" + time,
        "[data-markov-a]": format(a * 100) + "%",
        "[data-markov-b]": format(b * 100) + "%"
      };
      Object.entries(graphValues).forEach(([selector, value]) => {
        const label = root.querySelector(selector);
        if (label) label.textContent = value;
      });
      calculation.replaceChildren();
      if (previous) {
        const [oldA, oldB] = previous;
        const terms = [[0.7, 0.4, a], [0.3, 0.6, b]];
        terms.forEach(([fromA, fromB, value], i) => {
          const line = document.createElement("p");
          line.textContent = "状態" + ["A", "B"][i] + "：" + format(oldA * 100) + "% × " + fromA
            + " ＋ " + format(oldB * 100) + "% × " + fromB + " ＝ " + format(value * 100) + "%";
          calculation.append(line);
        });
      }
      button("next").disabled = time === 3;
      result.textContent = time === 0
        ? "時点0。Aから始まります。「次の時点へ」を押してください。"
        : "時点" + time + "。各到達先への確率を掛けて足しました。合計は100%。"
          + (time === 3 ? "この教材は3回までの例です。「最初から」で戻れます。" : "");
    }

    function reset() {
      time = 0; a = 1; b = 0;
      draw();
    }

    button("next").addEventListener("click", () => {
      const previous = [a, b];
      a = previous[0] * 0.7 + previous[1] * 0.4;
      b = previous[0] * 0.3 + previous[1] * 0.6;
      time += 1;
      draw(previous);
    });
    button("reset").addEventListener("click", reset);
    reset();
  }

  function adder(root, board, result, button) {
    const names = ["A", "B", "Cin"];
    const keys = ["a", "b", "cin"];
    const values = [0, 0, 0];

    function draw() {
      const [a, b, cin] = values;
      const ab = a ^ b;
      const s = ab ^ cin;
      const c = (a & b) | (ab & cin);
      keys.forEach((key, i) => {
        button(key).textContent = names[i] + "：" + values[i];
        button(key).setAttribute("aria-pressed", String(values[i] === 1));
      });
      renderList(board, [
        "A XOR B ＝ " + ab,
        "A AND B ＝ " + (a & b),
        "(A XOR B) AND Cin ＝ " + (ab & cin),
        "S（和）＝ " + s,
        "C（桁上げ・2つのANDのOR）＝ " + c
      ]);
      result.textContent = values.join("＋") + "＝" + (a + b + cin)
        + "（2進数 " + c + s + "） → C＝" + c + "、S＝" + s + (a + b + cin === 0 ? "。「A：0」から試せます。" : "");
    }

    keys.forEach((key, i) => button(key).addEventListener("click", () => {
      values[i] = 1 - values[i];
      draw();
    }));
    button("reset").addEventListener("click", () => { values.fill(0); draw(); });
    draw();
  }

  function dropout(root, board, result, button) {
    const examples = [
      [0.12, 0.81, 0.31, 0.92, 0.56, 0.20, 0.67, 0.47],
      [0.88, 0.05, 0.43, 0.71, 0.11, 0.37, 0.93, 0.62],
      [0.49, 0.68, 0.03, 0.36, 0.14, 0.78, 0.22, 0.32]
    ];
    const rate = root.querySelector("[data-rate]");
    let example = 0;

    function draw() {
      const training = root.querySelector("input:checked").value === "train";
      const threshold = Number(rate.value) / 100;
      const inactive = examples[example].map(score => training && score < threshold);
      renderList(board, inactive.map((off, i) =>
        "ニューロン" + (i + 1) + "：" + (off ? "無効（出力0）" : "有効")));
      Array.from(board.children).forEach((card, i) => card.classList.toggle("is-failed", inactive[i]));
      const count = inactive.filter(Boolean).length;
      button("next").disabled = !training;
      result.textContent = training
        ? "学習例" + (example + 1) + "。確率" + rate.value + "%で無効になったのは"
          + count + "個、有効は" + (8 - count) + "個です。次の学習例で別の抽選結果を見られます。"
          + (threshold === 0 ? "確率0%なので次の学習例でも全て有効です。" : "")
        : "通常の推論時はDropoutを使わないため全8個が有効です。学習例を進める操作は停止します。確率を変えても配置は変わりません。";
    }

    root.addEventListener("change", draw);
    button("next").addEventListener("click", () => { example = (example + 1) % examples.length; draw(); });
    button("reset").addEventListener("click", () => {
      root.querySelector('input[value="train"]').checked = true;
      rate.value = "25";
      example = 0;
      draw();
    });
    draw();
  }

  function impurity(root, board, result, button) {
    const proportions = root.querySelector("[data-proportions]");
    const giniValue = root.querySelector("[data-gini]");
    const entropyValue = root.querySelector("[data-entropy]");
    const giniFormula = root.querySelector("[data-gini-formula]");
    const entropyFormula = root.querySelector("[data-entropy-formula]");
    let a = 5;
    const entropyTerm = p => p === 0 ? 0 : -p * Math.log2(p);
    const format = value => Number(value.toFixed(3)).toString();

    function draw() {
      const b = 10 - a, p = a / 10, q = b / 10;
      const gini = 1 - p * p - q * q;
      const entropy = entropyTerm(p) + entropyTerm(q);
      renderList(board, Array.from({length: 10}, (_, i) => i < a ? "A" : "B"));
      Array.from(board.children).forEach((card, i) => card.classList.toggle("is-selected", i < a));
      proportions.textContent = "10個中 A：" + a + "個（" + a * 10 + "%）、B：" + b + "個（" + b * 10 + "%）";
      giniValue.textContent = format(gini);
      entropyValue.textContent = format(entropy);
      giniFormula.textContent = "1 − (" + p + "² ＋ " + q + "²) ＝ " + format(gini);
      entropyFormula.textContent = "Aの項 " + format(entropyTerm(p)) + " ＋ Bの項 "
        + format(entropyTerm(q)) + " ≈ " + format(entropy);
      button("increase").disabled = a === 10;
      button("decrease").disabled = a === 0;
      result.textContent = "Aが" + a + "個、Bが" + b + "個。"
        + (a === 0 || a === 10 ? "1種類だけなので両方0です。10個が上限です。"
          : a === 5 ? "半々のとき混ざり具合が最大です。「Aを1つ増やす」から試せます。" : "半々から偏るため両方の値が小さくなります。");
    }

    button("increase").addEventListener("click", () => { a += 1; draw(); });
    button("decrease").addEventListener("click", () => { a -= 1; draw(); });
    button("reset").addEventListener("click", () => { a = 5; draw(); });
    draw();
  }

  const lessons = {raid, join, kmeans, time, hamming, conditional, markov, adder, dropout, impurity};
  document.querySelectorAll("[data-first-step]").forEach(root => {
    const mount = lessons[root.dataset.firstStep];
    if (!mount) return;
    mount(root, root.querySelector("[data-board]"), root.querySelector("[data-result]"),
      action => root.querySelector('[data-action="' + action + '"]'));
    root.hidden = false;
  });
})();
