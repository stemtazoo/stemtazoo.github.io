document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-branch-demo]").forEach((demo) => {
    const rates = {
      A: Number(demo.dataset.rateA || 0),
      B: Number(demo.dataset.rateB || 0),
      C: Number(demo.dataset.rateC || 0),
    };

    const buttons = Array.from(demo.querySelectorAll("[data-order]"));
    const steps = Array.from(demo.querySelectorAll("[data-step]"));
    const average = demo.querySelector("[data-average]");
    const total = demo.querySelector("[data-total-comparisons]");
    const breakdown = demo.querySelector("[data-breakdown]");

    function render(order) {
      const first = order[0];
      const firstRate = rates[first];
      const remainingRate = 100 - firstRate;
      const averageComparisons = (firstRate + remainingRate * 2) / 100;
      const totalComparisons = firstRate + remainingRate * 2;

      buttons.forEach((button) => {
        const selected = button.dataset.order.split(",")[0] === first;
        button.setAttribute("aria-pressed", String(selected));
      });

      steps.forEach((step, index) => {
        const category = order[index];
        step.classList.toggle("is-first", index === 0);
        step.innerHTML = index === 0
          ? `<strong>${category}区分 ${rates[category]}%</strong><br>1回で判定`
          : `<strong>${category}区分 ${rates[category]}%</strong><br>2回で判定`;
      });

      if (average) {
        average.textContent = `${averageComparisons.toFixed(1)}回`;
      }

      if (total) {
        total.textContent = `${totalComparisons}回`;
      }

      if (breakdown) {
        breakdown.innerHTML = `
          <li>${first}区分 ${firstRate}件 × 1回 = ${firstRate}回</li>
          <li>残り ${remainingRate}件 × 2回 = ${remainingRate * 2}回</li>
        `;
      }
    }

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        render(button.dataset.order.split(","));
      });
    });

    if (buttons.length > 0) {
      render(buttons[0].dataset.order.split(","));
    }
  });

  document.querySelectorAll("[data-fe-binary-demo]").forEach((demo) => {
    const values = (demo.dataset.values || "").split(",").map(Number);
    const target = Number(demo.dataset.target);
    const cells = Array.from(demo.querySelectorAll("[data-binary-cell]"));
    const nextButton = demo.querySelector("[data-binary-next]");
    const resetButton = demo.querySelector("[data-binary-reset]");
    const status = demo.querySelector("[data-binary-status]");
    const leftLabel = demo.querySelector("[data-binary-left]");
    const midLabel = demo.querySelector("[data-binary-mid]");
    const rightLabel = demo.querySelector("[data-binary-right]");
    const countLabel = demo.querySelector("[data-binary-count]");

    let left;
    let right;
    let comparisons;
    let finished;

    function paint(mid = null, found = false) {
      cells.forEach((cell, index) => {
        const active = index >= left && index <= right;
        cell.classList.toggle("is-discarded", !active);
        cell.classList.toggle("is-mid", index === mid);
        cell.classList.toggle("is-found", found && index === mid);
      });

      if (leftLabel) leftLabel.textContent = String(left);
      if (rightLabel) rightLabel.textContent = String(right);
      if (midLabel) midLabel.textContent = mid === null ? "-" : String(mid);
      if (countLabel) countLabel.textContent = `${comparisons}回`;
    }

    function reset() {
      left = 0;
      right = values.length - 1;
      comparisons = 0;
      finished = false;
      paint();
      if (status) status.textContent = `探す値は ${target}。まず探索範囲の中央を確認します。`;
      if (nextButton) {
        nextButton.disabled = false;
        nextButton.textContent = "次の比較";
      }
    }

    function step() {
      if (finished || left > right) return;

      const mid = Math.floor((left + right) / 2);
      const value = values[mid];
      comparisons += 1;

      if (value === target) {
        finished = true;
        paint(mid, true);
        if (status) status.innerHTML = `<strong>${comparisons}回目：</strong> a[${mid}] = ${value}。探している ${target} と一致したので発見です。`;
        if (nextButton) {
          nextButton.disabled = true;
          nextButton.textContent = "見つかりました";
        }
        return;
      }

      if (target > value) {
        if (status) status.innerHTML = `<strong>${comparisons}回目：</strong> a[${mid}] = ${value}。${target} は ${value} より大きいので、左側を捨てます。`;
        left = mid + 1;
      } else {
        if (status) status.innerHTML = `<strong>${comparisons}回目：</strong> a[${mid}] = ${value}。${target} は ${value} より小さいので、右側を捨てます。`;
        right = mid - 1;
      }

      paint(mid);
      window.setTimeout(() => paint(), 180);
    }

    if (nextButton) nextButton.addEventListener("click", step);
    if (resetButton) resetButton.addEventListener("click", reset);
    reset();
  });

  document.querySelectorAll("[data-fe-adj-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-adj-edge]"));
    const lines = Array.from(demo.querySelectorAll("[data-graph-edge]"));
    const status = demo.querySelector("[data-adj-status]");
    const initial = new Set(["12", "13", "24", "34"]);
    const active = new Set(initial);

    function render() {
      buttons.forEach((button) => {
        const edge = button.dataset.adjEdge;
        const on = active.has(edge);
        button.textContent = on ? "1" : "0";
        button.setAttribute("aria-pressed", String(on));
      });

      lines.forEach((line) => {
        line.classList.toggle("is-off", !active.has(line.dataset.graphEdge));
      });

      if (status) {
        const edges = Array.from(active).sort().map((edge) => `V${edge[0]}―V${edge[1]}`);
        status.innerHTML = edges.length
          ? `<strong>現在の辺：</strong> ${edges.join("、")}`
          : "現在、辺はありません。";
      }
    }

    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        const edge = button.dataset.adjEdge;
        if (active.has(edge)) active.delete(edge);
        else active.add(edge);
        render();
      });
    });

    const reset = demo.querySelector("[data-adj-reset]");
    if (reset) {
      reset.addEventListener("click", () => {
        active.clear();
        initial.forEach((edge) => active.add(edge));
        render();
      });
    }

    render();
  });

  document.querySelectorAll("[data-fe-sjf-demo]").forEach((demo) => {
    const segments = Array.from(demo.querySelectorAll("[data-sjf-segment]"));
    const nextButton = demo.querySelector("[data-sjf-next]");
    const resetButton = demo.querySelector("[data-sjf-reset]");
    const status = demo.querySelector("[data-sjf-status]");
    const decision = demo.querySelector("[data-sjf-decision]");
    const completion = demo.querySelector("[data-sjf-completion]");

    const steps = [
      {
        time: 0,
        job: "A",
        text: "時刻0：到着済みはAだけなので、Aを実行します。",
        decision: "候補：A(2秒) → Aを選択",
        completion: "A：0〜2秒"
      },
      {
        time: 2,
        job: "C",
        text: "時刻2：Aが完了。待っているB(4秒)とC(3秒)を比べ、短いCを選びます。",
        decision: "候補：B(4秒)、C(3秒) → Cを選択",
        completion: "A：0〜2秒 / C：2〜5秒"
      },
      {
        time: 5,
        job: "E",
        text: "時刻5：Cが完了。B(4秒)、D(2秒)、E(1秒)の中で最短のEを選びます。",
        decision: "候補：B(4秒)、D(2秒)、E(1秒) → Eを選択",
        completion: "A：0〜2秒 / C：2〜5秒 / E：5〜6秒"
      },
      {
        time: 6,
        job: "D",
        text: "時刻6：Eが完了。B(4秒)とD(2秒)を比べ、Dを選びます。",
        decision: "候補：B(4秒)、D(2秒) → Dを選択",
        completion: "A：0〜2秒 / C：2〜5秒 / E：5〜6秒 / D：6〜8秒"
      },
      {
        time: 8,
        job: "B",
        text: "時刻8：残っているのはBだけなので、Bを実行します。",
        decision: "候補：B(4秒) → Bを選択",
        completion: "A：0〜2秒 / C：2〜5秒 / E：5〜6秒 / D：6〜8秒 / B：8〜12秒"
      },
      {
        time: 12,
        job: "完了",
        text: "時刻12：すべてのジョブが完了しました。処理順は A → C → E → D → B です。",
        decision: "すべて完了",
        completion: "処理順：A → C → E → D → B"
      }
    ];

    let currentStep = 0;

    function render() {
      demo.classList.add("is-js");

      segments.forEach((segment, index) => {
        const visibleCount = Math.min(currentStep + 1, steps.length - 1);
        segment.classList.toggle("is-future", index >= visibleCount);
        segment.classList.toggle("is-current", index === currentStep && currentStep < steps.length - 1);
      });

      const step = steps[currentStep];
      if (status) status.textContent = step.text;
      if (decision) decision.textContent = step.decision;
      if (completion) completion.textContent = step.completion;

      if (nextButton) {
        nextButton.disabled = currentStep >= steps.length - 1;
        nextButton.textContent = currentStep >= steps.length - 1 ? "完了" : "次の判断";
      }
    }

    if (nextButton) {
      nextButton.addEventListener("click", () => {
        if (currentStep < steps.length - 1) {
          currentStep += 1;
          render();
        }
      });
    }

    if (resetButton) {
      resetButton.addEventListener("click", () => {
        currentStep = 0;
        render();
      });
    }

    render();
  });
});

// Compare identical operations while keeping each structure's removal order.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-stack-queue-demo]").forEach((demo) => {
    const find = (name) => demo.querySelector(`[data-sq-${name}]`);
    const add = find("add");
    const remove = find("remove");
    const reset = find("reset");
    let stack, queue, nextValue;

    function paintItems(name, values, nextIndex) {
      const container = find(name);
      container.replaceChildren();
      if (!values.length) {
        container.textContent = "空です";
        return;
      }
      values.forEach((value, index) => {
        const cell = document.createElement("span");
        cell.textContent = `${value}${index === nextIndex ? "（次）" : ""}`;
        cell.classList.toggle("is-next", index === nextIndex);
        container.appendChild(cell);
      });
    }

    function render(message) {
      paintItems("stack", stack, stack.length - 1);
      paintItems("queue", queue, 0);
      add.textContent = `${nextValue}を追加`;
      add.disabled = stack.length >= 6;
      remove.disabled = stack.length === 0;
      const next = stack.length
        ? `次に出るのはスタックが${stack[stack.length - 1]}、キューが${queue[0]}です。`
        : "両方とも空なので取り出せません。追加すると再開できます。";
      find("status").textContent = `${message} ${next}${add.disabled ? " 表示上限の6個です。追加するには1個取り出してください。" : ""}`;
    }

    function initialize() {
      stack = [1, 2, 3];
      queue = [1, 2, 3];
      nextValue = 4;
      find("stack-out").textContent = "まだありません";
      find("queue-out").textContent = "まだありません";
      reset.disabled = false;
      render("1、2、3の順に入れた状態です。");
    }

    add.addEventListener("click", () => {
      if (stack.length >= 6) return;
      const value = nextValue++;
      stack.push(value);
      queue.push(value);
      render(`${value}をスタックの上とキューの末尾に追加しました。`);
    });
    remove.addEventListener("click", () => {
      if (!stack.length) return;
      const stackValue = stack.pop();
      const queueValue = queue.shift();
      find("stack-out").textContent = String(stackValue);
      find("queue-out").textContent = String(queueValue);
      render(`スタックの上から${stackValue}、キューの先頭から${queueValue}を取り出しました。`);
    });
    reset.addEventListener("click", initialize);
    initialize();
  });
});

// FE: alternating-bit right-shift visualizer
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-alternating-bits-demo]").forEach((demo) => {
    const slider = demo.querySelector("[data-alt-n]");
    const nLabel = demo.querySelector("[data-alt-n-label]");
    const xContainer = demo.querySelector("[data-alt-x]");
    const halfContainer = demo.querySelector("[data-alt-half]");
    const sumContainer = demo.querySelector("[data-alt-sum]");
    const result = demo.querySelector("[data-alt-result]");

    if (!slider || !xContainer || !halfContainer || !sumContainer || !result) return;

    function renderBits(container, bits) {
      container.replaceChildren();
      bits.split("").forEach((bit) => {
        const cell = document.createElement("span");
        cell.className = "fe-alt-bits-demo__bit";
        cell.textContent = bit;
        container.appendChild(cell);
      });
    }

    function render() {
      const n = Number(slider.value);
      const length = n * 2;
      const xBits = Array.from({ length }, (_, index) => index % 2 === 0 ? "1" : "0").join("");
      const halfBits = "0" + xBits.slice(0, -1);
      const sumBits = "1".repeat(length);
      const sumValue = (2 ** length) - 1;

      if (nLabel) nLabel.textContent = String(n);
      renderBits(xContainer, xBits);
      renderBits(halfContainer, halfBits);
      renderBits(sumContainer, sumBits);
      result.textContent = `${length}ビットすべてが1なので、合計は 2^${length} - 1 = ${sumValue} です。`;
    }

    slider.addEventListener("input", render);
    render();
  });
});

// FE: scalar argument passing, shown at four call stages.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-arg-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-arg-stage]"));
    const find = (name) => demo.querySelector("[data-arg-" + name + "]");
    const labels = ["value-x", "value-p", "value-note", "ref-x", "ref-p", "ref-note", "status"];
    const outputs = labels.map(find);
    if (!buttons.length || outputs.some((node) => !node)) return;
    const stages = [
      ["x = 10", "p はまだありません", "値のコピーを渡します。",
       "x = 10", "p はまだありません", "元の変数への参照を渡します。",
       "呼出し前：どちらも x = 10 です。"],
      ["x = 10", "p = 10", "x と p は、同じ値を持つ別々の変数です。",
       "x = 10", "p から見ても10", "p は x と同じ変数を参照します。",
       "受渡し直後：値呼出しは10をコピー。参照呼出しは元の x を参照します。"],
      ["x = 10", "p = 99", "変わるのはコピーの p だけです。",
       "x = 99", "p から見ても99", "p を通して、元の x が変わりました。",
       "p ← 99 の直後：値呼出しの x は10のまま。参照呼出しの x は99になります。"],
      ["x = 10", "p の役割は終了", "p の99は x に書き戻されません。",
       "x = 99", "p の役割は終了", "元の x に行った変更が残ります。",
       "終了後：値呼出しは x = 10、参照呼出しは x = 99 です。"]
    ];
    function render(index) {
      outputs.forEach((node, i) => { node.textContent = stages[index][i]; });
      buttons.forEach((button) => {
        button.setAttribute("aria-pressed", String(Number(button.dataset.argStage) === index));
      });
    }
    buttons.forEach((button) => {
      const index = Number(button.dataset.argStage);
      if (!Number.isInteger(index) || !stages[index]) return;
      button.disabled = false;
      button.addEventListener("click", () => render(index));
    });
    render(0);
  });
});

// FE: compaction changes the largest free extent, not total free capacity.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-compaction-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-compact-state]"));
    const memory = demo.querySelector("[data-compact-memory]");
    const status = demo.querySelector("[data-compact-status]");
    if (!memory || !status || !buttons.length) return;
    const layouts = {
      before: [["A", 60], ["空き", 40], ["B", 80], ["空き", 30], ["C", 40], ["空き", 50]],
      after: [["A", 60], ["B", 80], ["C", 40], ["空き", 120]]
    };
    function render(state) {
      const layout = layouts[state];
      if (!layout) return;
      memory.replaceChildren();
      layout.forEach(([name, size]) => {
        const block = document.createElement("span");
        block.className = "fe-compaction-demo__block" + (name === "空き" ? " is-free" : "");
        block.style.flexGrow = String(size);
        block.setAttribute("aria-label", name + (name === "空き" ? "" : " 使用中") + size + "KB");
        block.textContent = name;
        const number = document.createElement("strong");
        number.textContent = String(size);
        block.appendChild(number);
        memory.appendChild(block);
      });
      const free = layout.filter(([name]) => name === "空き").map(([, size]) => size);
      const total = free.reduce((sum, size) => sum + size, 0);
      const largest = Math.max(...free);
      status.textContent = (state === "before" ? "整理前" : "整理後") +
        "：空きの合計は" + total + "KB、最大の連続した空きは" + largest + "KBです。" +
        (largest >= 80 ? "80KBを連続配置できます。空きの合計は増えていません。" : "80KBを連続配置できません。");
      buttons.forEach((button) => {
        button.setAttribute("aria-pressed", String(button.dataset.compactState === state));
      });
    }
    buttons.forEach((button) => {
      if (!layouts[button.dataset.compactState]) return;
      button.disabled = false;
      button.addEventListener("click", () => render(button.dataset.compactState));
    });
    render("before");
  });
});

// FE: NOR flash erase/program states; sector size is a teaching abstraction.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-flash-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-flash-stage]"));
    const bits = demo.querySelector("[data-flash-bits]");
    const status = demo.querySelector("[data-flash-status]");
    if (!bits || !status || !buttons.length) return;
    const stages = [
      ["1111", "消去済み：1111。ここから必要なビットを0に書き込みます。"],
      ["1010", "書込み後：1010。左から2番目と4番目を1から0にしました。"],
      ["1010", "1110に変更したい：左から2番目の0を1に戻す必要があります。書込みだけではできないため、1010のままです。"],
      ["1111", "消去後：範囲全体が1111に戻りました。変更したかったビット以外も消去されます。"],
      ["1110", "再書込み後：1110。消去済みの状態から、左から4番目を0に書き込みました。"]
    ];
    function render(index) {
      const [value, note] = stages[index];
      bits.replaceChildren();
      Array.from(value).forEach((bit, position) => {
        const cell = document.createElement("span");
        cell.className = "fe-flash-demo__bit" + (bit === "0" ? " is-zero" : "") +
          (index === 2 && position === 1 ? " is-blocked" : "");
        cell.textContent = bit;
        bits.appendChild(cell);
      });
      bits.setAttribute("aria-label", "ビットの状態：" + value);
      status.textContent = note;
      buttons.forEach((button) => {
        button.setAttribute("aria-pressed", String(Number(button.dataset.flashStage) === index));
      });
    }
    buttons.forEach((button) => {
      const index = Number(button.dataset.flashStage);
      if (!Number.isInteger(index) || !stages[index]) return;
      button.disabled = false;
      button.addEventListener("click", () => render(index));
    });
    render(0);
  });
});

// FE: show representatives and boundary values for a fixed integer specification.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-boundary-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-boundary-mode]"));
    const values = Array.from(demo.querySelectorAll("[data-boundary-kind]"));
    const status = demo.querySelector("[data-boundary-status]");
    const modes = ["representative", "boundary", "both"];
    if (!status || !values.length || !buttons.length) return;
    function render(mode) {
      if (!modes.includes(mode)) return;
      values.forEach((value) => {
        value.hidden = mode !== "both" && value.dataset.boundaryKind !== mode;
      });
      const visible = values.filter((value) => !value.hidden);
      const representatives = visible.filter((value) => value.dataset.boundaryKind === "representative").length;
      const boundaries = visible.filter((value) => value.dataset.boundaryKind === "boundary").length;
      const messages = {
        representative: "代表値だけ：" + representatives + "個。境界ではない20と120を、有効クラスから1個ずつ選びます。",
        boundary: "境界値だけ：" + boundaries + "個。0と1、40と41、200と201で、3か所の境目を確認します。",
        both: "両方：代表値" + representatives + "個＋境界値" + boundaries + "個＝" + visible.length + "個。代表値は境界値と重ならない値を選んでいます。"
      };
      status.textContent = messages[mode];
      buttons.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.boundaryMode === mode)));
    }
    buttons.forEach((button) => {
      if (!modes.includes(button.dataset.boundaryMode)) return;
      button.disabled = false;
      button.addEventListener("click", () => render(button.dataset.boundaryMode));
    });
    render("both");
  });
});

// FE: ordinary BST insertion, one comparison or insertion per step.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-bst-demo]").forEach((demo) => {
    const next = demo.querySelector("[data-bst-next]");
    const reset = demo.querySelector("[data-bst-reset]");
    const status = demo.querySelector("[data-bst-status]");
    const svg = demo.querySelector("svg");
    const nodes = Array.from(demo.querySelectorAll("[data-bst-value]"));
    const edges = Array.from(demo.querySelectorAll("[data-bst-child]"));
    const values = (demo.dataset.bstValues || "").split(",").map(Number);
    if (!next || !reset || !status || !svg || !nodes.length ||
        values.some(v => !Number.isFinite(v)) || new Set(values).size !== values.length ||
        values.length !== nodes.length) return;
    const events = [];
    const tree = new Map();
    const visible = [];
    let root = null;
    values.forEach(value => {
      if (root === null) {
        root = value;
        tree.set(value, { left: null, right: null });
        visible.push(value);
        events.push({ visible: visible.slice(), current: value, added: true,
          note: value + "を根に追加しました。" });
        return;
      }
      let current = root;
      while (true) {
        const side = value < current ? "left" : "right";
        const child = tree.get(current)[side];
        const direction = side === "left" ? "左" : "右";
        events.push({ visible: visible.slice(), current, child,
          note: value + (side === "left" ? " < " : " > ") + current + " → " + direction +
            (child === null ? "の子が空なので、次の操作で追加します。" : "の子" + child + "へ進みます。") });
        if (child === null) {
          tree.get(current)[side] = value;
          tree.set(value, { left: null, right: null });
          visible.push(value);
          events.push({ visible: visible.slice(), current: value, added: true, child: value,
            note: value + "を" + current + "の" + direction + "の子に追加しました。" });
          break;
        }
        current = child;
      }
    });
    let index = -1;
    function render() {
      const event = events[index];
      const shown = event ? event.visible : [];
      nodes.forEach(node => {
        const value = Number(node.dataset.bstValue);
        node.classList.toggle("is-hidden", !shown.includes(value));
        node.classList.toggle("is-current", !!event && !event.added && event.current === value);
        node.classList.toggle("is-new", !!event && !!event.added && event.current === value);
      });
      edges.forEach(edge => {
        const child = Number(edge.dataset.bstChild);
        edge.classList.toggle("is-hidden", !shown.includes(child));
        edge.classList.toggle("is-path", !!event && event.child === child);
      });
      const done = index === events.length - 1;
      status.textContent = event ? event.note + (done ? " 全" + values.length + "個の挿入が完了しました。" : "") :
        "木は空です。「次の比較・追加」で" + values[0] + "を根に入れます。各値の比較は毎回根から始まります。";
      svg.setAttribute("aria-label", "挿入済み：" + (shown.length ? shown.join("、") : "なし") +
        "。" + status.textContent);
      next.disabled = done;
      reset.disabled = false;
    }
    next.addEventListener("click", () => {
      if (index < events.length - 1) { index += 1; render(); }
    });
    reset.addEventListener("click", () => { index = -1; render(); });
    render();
  });
});

// FE: preview an UPDATE and validate the primary key before showing a saved result.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-pk-demo]").forEach(demo => {
    const cases = Array.from(demo.querySelectorAll("[data-pk-case]"));
    const next = demo.querySelector("[data-pk-next]");
    const status = demo.querySelector("[data-pk-status]");
    const sql = demo.querySelector("[data-pk-sql]");
    const preview = demo.querySelector("[data-pk-preview]");
    const result = demo.querySelector("[data-pk-result]");
    const originals = Array.from(demo.querySelectorAll("[data-pk-original]"));
    if (!next || !status || !sql || !preview || !result || originals.length !== 4) return;
    const base = [
      {id:1001,name:"山田",department:"設計"},
      {id:1002,name:"鈴木",department:"営業"},
      {id:1003,name:"佐藤",department:"設計"},
      {id:1004,name:"高橋",department:"品質"}
    ];
    const scenarios = [
      {sql:"UPDATE 社員 SET 社員番号 = 1001 WHERE 社員番号 = 1002;",
        match:r=>r.id===1002, key:"id", value:1001},
      {sql:"UPDATE 社員 SET 社員番号 = 1010 WHERE 部署 = '設計';",
        match:r=>r.department==="設計", key:"id", value:1010},
      {sql:"UPDATE 社員 SET 社員番号 = NULL WHERE 社員番号 = 1002;",
        match:r=>r.id===1002, key:"id", value:null},
      {sql:"UPDATE 社員 SET 部署 = '企画' WHERE 社員番号 = 1002;",
        match:r=>r.id===1002, key:"department", value:"企画"},
      {sql:"UPDATE 社員 SET 社員番号 = 1010 WHERE 社員番号 = 1002;",
        match:r=>r.id===1002, key:"id", value:1010}
    ];
    let selected = 0;
    let stage = 0;
    function fill(body, rows, targets, badIds) {
      body.replaceChildren();
      rows.forEach((row,i) => {
        const tr = document.createElement("tr");
        if (targets.includes(i)) tr.classList.add("is-target");
        if (badIds.includes(row.id)) tr.classList.add("is-invalid");
        const marker = (targets.includes(i) ? "対象" : "対象外") +
          (badIds.includes(row.id) ? "・制約違反" : "");
        [row.id===null?"NULL":String(row.id),row.name,row.department,marker].forEach(value=>{
          const td=document.createElement("td");td.textContent=value;tr.appendChild(td);
        });
        body.appendChild(tr);
      });
    }
    function render() {
      const scenario = scenarios[selected];
      const targets = base.map((r,i)=>scenario.match(r)?i:-1).filter(i=>i>=0);
      const proposed = base.map((r,i)=>targets.includes(i)?{...r,[scenario.key]:scenario.value}:{...r});
      const badIds = proposed.filter((r,i,rows)=>r.id===null ||
        rows.some((other,j)=>i!==j && r.id===other.id)).map(r=>r.id);
      const invalid = badIds.length>0;
      sql.textContent = scenario.sql;
      originals.forEach((row,i)=>{
        row.classList.toggle("is-target",targets.includes(i));
        const marker=row.querySelector("[data-pk-marker]");
        if(marker) marker.textContent=targets.includes(i)?"対象":"対象外";
      });
      if(stage===0) {
        preview.replaceChildren();
        const tr=document.createElement("tr"),td=document.createElement("td");
        td.colSpan=4;td.textContent="まだ候補を作っていません。";
        tr.appendChild(td);preview.appendChild(tr);
      } else fill(preview,proposed,targets,badIds);
      fill(result,stage===2&&!invalid?proposed:base,[],[]);
      const messages = [
        "① WHERE：対象は"+targets.length+"行です。更新前の表で「対象」の行を確認します。",
        "② SET：変更後の候補です。まだ保存していません。次に主キーの重複とNULLを確認します。",
        invalid ? "③ 制約確認："+(badIds.includes(null)?"主キーがNULLになります。":"主キーが重複します。")+
          "更新不可。保存結果は更新前の表のままです。" :
          "③ 制約確認：主キーの重複もNULLもありません。更新でき、保存結果に反映されます。"
      ];
      status.textContent=messages[stage];
      next.disabled=stage===2;
      next.textContent=stage===0?"SETの候補を見る":stage===1?"制約と保存結果を見る":"確認完了";
      cases.forEach(button=>button.setAttribute("aria-pressed",String(Number(button.dataset.pkCase)===selected)));
    }
    cases.forEach(button=>{
      const index=Number(button.dataset.pkCase);
      if(!Number.isInteger(index)||!scenarios[index])return;
      button.disabled=false;
      button.addEventListener("click",()=>{selected=index;stage=0;render();});
    });
    next.addEventListener("click",()=>{if(stage<2){stage++;render();}});
    render();
  });
  // FE pseudocode trace: highlight the line just executed; show the next line separately.
  document.querySelectorAll("[data-fe-pseudocode-demo]").forEach((demo) => {
    const lines = Array.from(demo.querySelectorAll("[data-trace-line]"));
    const previous = demo.querySelector("[data-trace-prev]");
    const next = demo.querySelector("[data-trace-next-button]");
    const reset = demo.querySelector("[data-trace-reset]");
    const iOutput = demo.querySelector("[data-trace-i]");
    const totalOutput = demo.querySelector("[data-trace-total]");
    const nextOutput = demo.querySelector("[data-trace-next]");
    const message = demo.querySelector("[data-trace-message]");
    const values = [4, 7, 2];
    const states = [];
    let i;
    let total;
    const add = (executed, upcoming, explanation) =>
      states.push({executed, upcoming, i, total, explanation});
    add(-1, 0, "開始前です。次は i に1を代入します。");
    i = 1; add(0, 1, "i ← 1：添字を1にします。");
    total = 0; add(1, 2, "total ← 0：合計を初期化します。");
    while (true) {
      if (i > values.length) {
        add(2, 6, "while の条件は偽です。ループを抜けます。");
        add(6, -1, "終了です。最終的な total は " + total + " です。");
        break;
      }
      add(2, 3, "while の条件は真です。i = " + i + " なので、次は偶数判定です。");
      const value = values[i - 1];
      if (value % 2 === 0) {
        add(3, 4, "data[" + i + "] = " + value + " は偶数です。加算します。");
        total += value;
        add(4, 5, "total に " + value + " を加え、" + total + " になりました。");
      } else {
        add(3, 5, "data[" + i + "] = " + value + " は奇数です。加算を飛ばします。");
      }
      i += 1;
      add(5, 2, "i を " + i + " に更新しました。while の条件を再判定します。");
    }
    let position = 0;
    function render() {
      const state = states[position];
      iOutput.textContent = state.i === undefined ? "未設定" : String(state.i);
      totalOutput.textContent = state.total === undefined ? "未設定" : String(state.total);
      lines.forEach((line, index) => {
        const active = index === state.executed;
        line.classList.toggle("is-active", active);
        if (active) line.setAttribute("aria-current", "step");
        else line.removeAttribute("aria-current");
      });
      nextOutput.textContent = state.upcoming < 0
        ? "なし（終了）" : lines[state.upcoming].textContent.trim();
      message.textContent = state.explanation;
      previous.disabled = position === 0;
      next.disabled = position === states.length - 1;
    }
    next.addEventListener("click", () => {
      if (position < states.length - 1) { position++; render(); }
    });
    previous.addEventListener("click", () => {
      if (position > 0) { position--; render(); }
    });
    reset.addEventListener("click", () => { position = 0; render(); });
    render();
  });

  document.querySelectorAll("[data-fe-multi-stack-demo]").forEach((demo) => {
    const actions = [
      { label: "Aをスタック1にpush", type: "push", stack: 0, value: "A" },
      { label: "Cをスタック2にpush", type: "push", stack: 1, value: "C" },
      { label: "Kをスタック3にpush", type: "push", stack: 2, value: "K" },
      { label: "Sをスタック3にpush", type: "push", stack: 2, value: "S" },
      { label: "スタック3からSをpop・出力", type: "pop", stack: 2, value: "S" },
      { label: "Tをスタック3にpush", type: "push", stack: 2, value: "T" },
      { label: "スタック3からTをpop・出力", type: "pop", stack: 2, value: "T" },
      { label: "スタック1からAをpop・出力", type: "pop", stack: 0, value: "A" },
      { label: "スタック2からCをpop・出力", type: "pop", stack: 1, value: "C" },
      { label: "スタック3からKをpop・出力", type: "pop", stack: 2, value: "K" },
    ];
    const shafts = Array.from(demo.querySelectorAll("[data-ms-stack]"));
    const actionLabel = demo.querySelector("[data-ms-action]");
    const counter = demo.querySelector("[data-ms-counter]");
    const output = demo.querySelector("[data-ms-output]");
    const previous = demo.querySelector("[data-ms-prev]");
    const next = demo.querySelector("[data-ms-next]");
    const reset = demo.querySelector("[data-ms-reset]");
    if (shafts.length !== 3 || !actionLabel || !counter || !output || !previous || !next || !reset) return;
    let position = 0;

    function render() {
      const stacks = [[], [], []];
      const printed = [];
      for (let i = 0; i < position; i++) {
        const step = actions[i];
        if (step.type === "push") stacks[step.stack].push(step.value);
        else {
          const removed = stacks[step.stack].pop();
          if (removed !== step.value) throw new Error("Unexpected multi-stack trace");
          printed.push(removed);
        }
      }
      shafts.forEach((shaft, index) => {
        shaft.replaceChildren();
        if (stacks[index].length === 0) {
          const empty = document.createElement("span");
          empty.className = "fe-multi-stack-demo__empty";
          empty.textContent = "空";
          shaft.appendChild(empty);
        }
        stacks[index].forEach((value, valueIndex) => {
          const item = document.createElement("span");
          item.className = "fe-multi-stack-demo__item";
          if (position > 0 && actions[position - 1].type === "push" &&
              actions[position - 1].stack === index && valueIndex === stacks[index].length - 1) {
            item.classList.add("is-current");
          }
          item.textContent = value;
          shaft.appendChild(item);
        });
      });
      output.replaceChildren();
      if (printed.length === 0) output.textContent = "まだありません";
      printed.forEach((value) => {
        const item = document.createElement("span");
        item.className = "fe-multi-stack-demo__printed";
        item.textContent = value;
        output.appendChild(item);
      });
      actionLabel.textContent = position === 0 ? "開始前：次へ進んでください" : actions[position - 1].label;
      counter.textContent = position + " / " + actions.length + " 操作";
      previous.disabled = position === 0;
      next.disabled = position === actions.length;
      reset.disabled = position === 0;
    }
    previous.addEventListener("click", () => { if (position > 0) { position--; render(); } });
    next.addEventListener("click", () => { if (position < actions.length) { position++; render(); } });
    reset.addEventListener("click", () => { position = 0; render(); });
    render();
  });

  document.querySelectorAll("[data-fe-block-allocation-demo]").forEach((demo) => {
    const slider = demo.querySelector("[data-fba-slider]");
    const sizeLabel = demo.querySelector("[data-fba-size]");
    const blocksElement = demo.querySelector("[data-fba-blocks]");
    const result = demo.querySelector("[data-fba-result]");
    if (!slider || !sizeLabel || !blocksElement || !result) return;
    function render() {
      const size = Number(slider.value);
      const count = Math.ceil(size / 4000);
      const unused = count * 4000 - size;
      sizeLabel.textContent = size.toLocaleString("ja-JP");
      blocksElement.replaceChildren();
      for (let i = 0; i < count; i++) {
        const used = Math.max(0, Math.min(4000, size - i * 4000));
        const block = document.createElement("div");
        block.className = "fe-block-allocation-demo__block";
        const fill = document.createElement("div");
        fill.className = "fe-block-allocation-demo__fill";
        fill.style.width = (used / 4000 * 100) + "%";
        block.appendChild(fill);
        const label = document.createElement("span");
        label.textContent = "ブロック" + (i + 1);
        block.appendChild(label);
        block.setAttribute("aria-label", "ブロック" + (i + 1) + "：使用" + used + "バイト、未使用" + (4000 - used) + "バイト");
        blocksElement.appendChild(block);
      }
      result.textContent = size.toLocaleString("ja-JP") + "バイト → " + count +
        "ブロック → " + (count * 8) + "セクタ（未使用 " + unused.toLocaleString("ja-JP") + "バイト）";
    }
    slider.addEventListener("input", render);
    demo.querySelectorAll("[data-fba-set]").forEach((button) => {
      button.addEventListener("click", () => {
        slider.value = button.dataset.fbaSet;
        render();
      });
    });
    render();
  });

  document.querySelectorAll("[data-fe-bi-demo]").forEach((demo) => {
    const rows = [
      { store: "A店", product: "商品X", sales: 100 },
      { store: "A店", product: "商品Y", sales: 50 },
      { store: "B店", product: "商品X", sales: 60 },
      { store: "B店", product: "商品Y", sales: 90 }
    ];
    const chart = demo.querySelector("[data-bi-chart]");
    const insight = demo.querySelector("[data-bi-insight]");
    const buttons = Array.from(demo.querySelectorAll("[data-bi-view]"));
    if (!chart || !insight || !buttons.length) return;
    function render(view) {
      const key = view === "product" ? "product" : "store";
      const labels = key === "store" ? ["A店", "B店"] : ["商品X", "商品Y"];
      const totals = labels.map(label => rows.filter(row => row[key] === label).reduce((sum, row) => sum + row.sales, 0));
      const max = Math.max(...totals);
      chart.replaceChildren();
      labels.forEach((label, index) => {
        const row = document.createElement("div");
        row.className = "fe-bi-demo__row";
        const name = document.createElement("span");
        name.textContent = label;
        const track = document.createElement("div");
        track.className = "fe-bi-demo__track";
        const bar = document.createElement("div");
        bar.className = "fe-bi-demo__bar";
        bar.style.width = (totals[index] / max * 100) + "%";
        track.appendChild(bar);
        const value = document.createElement("strong");
        value.textContent = totals[index] + "万円";
        row.append(name, track, value);
        chart.appendChild(row);
      });
      buttons.forEach(button => button.setAttribute("aria-pressed", String(button.dataset.biView === key)));
      insight.textContent = key === "store"
        ? "店舗別ではA店もB店も150万円。合計だけでは商品の売れ方の違いは分かりません。"
        : "商品別では商品Xが160万円、商品Yが140万円。商品別の合計だけでは店舗ごとの売れ方は分かりません。";
    }
    buttons.forEach(button => button.addEventListener("click", () => render(button.dataset.biView)));
    render("store");
  });


  // Addressing modes: show which register value is added to the instruction field.
  document.querySelectorAll("[data-fe-address-demo]").forEach((demo) => {
    const modes = {
      index: { label: "指標レジスタ（R2）", value: 50, description: "指標レジスタR2の値50を加えて、主記憶の150番地を参照します。" },
      base: { label: "ベースレジスタ", value: 200, description: "ベースレジスタの値200を基準にして、主記憶の300番地を参照します。" },
      relative: { label: "プログラムカウンタ", value: 400, description: "プログラムカウンタの値400を基準にして、主記憶の500番地を参照します。" }
    };
    const buttons = Array.from(demo.querySelectorAll("[data-address-mode]"));
    const register = demo.querySelector("[data-address-register]");
    const offset = demo.querySelector("[data-address-offset]");
    const result = demo.querySelector("[data-address-result]");
    const formula = demo.querySelector("[data-address-formula]");
    const explanation = demo.querySelector("[data-address-explanation]");
    function render(mode) {
      const data = modes[mode];
      if (!data) return;
      const address = 100 + data.value;
      register.textContent = data.label;
      offset.textContent = String(data.value);
      result.textContent = address + "番地";
      formula.textContent = "100 ＋ " + data.value + " ＝ " + address;
      explanation.textContent = data.description;
      buttons.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.addressMode === mode)));
    }
    buttons.forEach((button) => button.addEventListener("click", () => render(button.dataset.addressMode)));
    render("index");
  });


  // Nash equilibrium: compare each player's best response to the other player's choice.
  document.querySelectorAll("[data-fe-nash-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-nash-view]"));
    const cells = Array.from(demo.querySelectorAll("[data-nash-cell]"));
    const status = demo.querySelector("[data-nash-status]");
    const messages = {
      a: "A社：B社がb1でもb2でも、左の数値が大きいa1を選びます（縦に比較）。",
      b: "B社：A社がa1でもa2でも、右の数値が大きいb2を選びます（横に比較）。",
      both: "両社の最適反応が重なる（a1, b2）がナッシュ均衡です。"
    };
    function render(view) {
      if (!Object.prototype.hasOwnProperty.call(messages, view)) return;
      cells.forEach((cell) => {
        const bestA = cell.dataset.bestA === "true";
        const bestB = cell.dataset.bestB === "true";
        const equilibrium = bestA && bestB;
        cell.classList.toggle("is-best-a", (view === "a" || view === "both") && bestA);
        cell.classList.toggle("is-best-b", (view === "b" || view === "both") && bestB);
        cell.classList.toggle("is-equilibrium", view === "both" && equilibrium);
        const marker = cell.querySelector("[data-nash-marker]");
        if (marker) marker.textContent = view === "a" && bestA ? "A社の最適反応" : view === "b" && bestB ? "B社の最適反応" : view === "both" && equilibrium ? "★ ナッシュ均衡" : "";
      });
      status.textContent = messages[view];
      buttons.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.nashView === view)));
    }
    buttons.forEach((button) => button.addEventListener("click", () => render(button.dataset.nashView)));
    render("both");
  });


  // Linked-list reference demo: moving prev does not rewrite links.
  document.querySelectorAll("[data-fe-linked-demo]").forEach((demo) => {
    const nodes = demo.querySelector("[data-fe-linked-nodes]");
    const status = demo.querySelector("[data-fe-linked-status]");
    const move = demo.querySelector("[data-fe-linked-move]");
    const remove = demo.querySelector("[data-fe-linked-delete]");
    const resetButton = demo.querySelector("[data-fe-linked-reset]");
    const labels = ["A", "B", "C", "D"];
    let prevIndex = 0;
    let next = [1, 2, 3, -1];

    function render(message) {
      const reachable = [];
      let at = 0;
      while (at !== -1 && !reachable.includes(at)) {
        reachable.push(at);
        at = next[at];
      }
      nodes.replaceChildren();
      labels.forEach((label, index) => {
        const item = document.createElement("div");
        item.className = "fe-linked-demo__node";
        if (!reachable.includes(index)) item.classList.add("is-detached");
        if (prevIndex === index) item.classList.add("is-prev");
        const value = document.createElement("strong");
        value.textContent = label;
        const nextLabel = document.createElement("span");
        nextLabel.textContent = "next → " + (next[index] < 0 ? "なし" : labels[next[index]]);
        item.append(value, nextLabel);
        if (prevIndex === index) {
          const marker = document.createElement("em");
          marker.textContent = "← prev";
          item.append(marker);
        }
        nodes.append(item);
      });
      if (status) status.textContent = message;
      move.disabled = next[prevIndex] === -1;
      remove.disabled = next[prevIndex] === -1;
    }

    move.addEventListener("click", () => {
      const from = labels[prevIndex];
      prevIndex = next[prevIndex];
      render("prev が " + from + " から " + labels[prevIndex] + " を指すようになりました。next のつながりは変わりません。");
    });
    remove.addEventListener("click", () => {
      const target = next[prevIndex];
      const after = next[target];
      next[prevIndex] = after;
      render(labels[prevIndex] + " の next を " + labels[target] + " から " + (after < 0 ? "なし" : labels[after]) + " に変更。 " + labels[target] + " は先頭からたどれなくなりました。");
    });
    resetButton.addEventListener("click", () => {
      prevIndex = 0;
      next = [1, 2, 3, -1];
      render("prev は A を指しています。まず移動を押してみましょう。");
    });
    render("prev は A を指しています。まず移動を押してみましょう。");
  });
});


// FE Subject B: compare non-progressing and corrected binary-search bounds.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-loop-demo]").forEach((demo) => {
    const buttons = Array.from(demo.querySelectorAll("[data-loop-mode]"));
    const cells = Array.from(demo.querySelectorAll("[data-loop-cell]"));
    const lowLabel = demo.querySelector("[data-loop-low]");
    const highLabel = demo.querySelector("[data-loop-high]");
    const middleLabel = demo.querySelector("[data-loop-middle]");
    const countLabel = demo.querySelector("[data-loop-count]");
    const update = demo.querySelector("[data-loop-update]");
    const status = demo.querySelector("[data-loop-status]");
    const nextButton = demo.querySelector("[data-loop-next]");
    const resetButton = demo.querySelector("[data-loop-reset]");

    const steps = {
      bug: [
        { low: 1, high: 2, mid: null, note: "まだ比較していません。", change: "まず探索範囲の中央を確認します。" },
        { low: 1, high: 2, mid: 1, note: "data[1] = 3 は target = 8 より小さい。low ← middle でも low は1のままです。", change: "1回目：low ← middle = 1（変化なし）" },
        { low: 1, high: 2, mid: 1, repeat: true, note: "2回目も low=1・high=2・middle=1。終了条件は真のままで、同じ処理が続きます。", change: "2回目：low ← middle = 1（変化なし）" }
      ],
      fixed: [
        { low: 1, high: 2, mid: null, note: "まだ比較していません。", change: "まず探索範囲の中央を確認します。" },
        { low: 2, high: 2, mid: 1, note: "data[1] = 3 は target = 8 より小さい。中央を除外して low を2に更新します。", change: "1回目：low ← middle + 1 = 2" },
        { low: 2, high: 2, mid: 2, found: true, note: "data[2] = 8 が target と一致。要素番号2を返して終了します。", change: "2回目：return 2（探索終了）" }
      ]
    };
    let mode = "bug";
    let current = 0;

    function render() {
      const entry = steps[mode][current];
      lowLabel.textContent = String(entry.low);
      highLabel.textContent = String(entry.high);
      middleLabel.textContent = entry.mid === null ? "―" : String(entry.mid);
      countLabel.textContent = current + "回";
      update.textContent = entry.change;
      status.textContent = entry.note;
      status.classList.toggle("is-warning", Boolean(entry.repeat));
      status.classList.toggle("is-found", Boolean(entry.found));
      cells.forEach((cell) => {
        const index = Number(cell.dataset.loopCell);
        cell.classList.toggle("is-mid", index === entry.mid);
        cell.classList.toggle("is-found", Boolean(entry.found) && index === entry.mid);
        cell.classList.toggle("is-discarded", index < entry.low || index > entry.high);
        const marker = cell.querySelector("[data-loop-mark]");
        if (marker) {
          marker.textContent = index === entry.mid
            ? (entry.found ? "見つかった" : "比較した位置")
            : (index === 2 ? "target" : (index < entry.low ? "除外済み" : "候補"));
        }
      });
      buttons.forEach((button) => {
        button.setAttribute("aria-pressed", String(button.dataset.loopMode === mode));
      });
      nextButton.disabled = current === steps[mode].length - 1;
      nextButton.textContent = entry.repeat ? "同じ状態の再発を確認" : entry.found ? "探索終了" : "次の比較 →";
    }

    buttons.forEach((button) => button.addEventListener("click", () => {
      mode = button.dataset.loopMode;
      current = 0;
      render();
    }));
    nextButton.addEventListener("click", () => {
      current = Math.min(current + 1, steps[mode].length - 1);
      render();
    });
    resetButton.addEventListener("click", () => {
      current = 0;
      render();
    });
    render();
  });
});
