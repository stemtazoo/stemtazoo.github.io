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
  // FE pseudocode trace: each state is the result of exactly one executed line.
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
    const add = (line, explanation) => states.push({line, i, total, explanation});
    add(0, "開始前です。次は i に1を代入します。");
    i = 1; add(1, "i ← 1：添字を1にします。");
    total = 0; add(2, "total ← 0：合計を初期化します。");
    while (true) {
      if (i > values.length) {
        add(6, "while の条件は偽です。ループを抜けます。");
        add(-1, "終了です。最終的な total は " + total + " です。");
        break;
      }
      add(3, "while の条件は真です。i = " + i + " なので、次は偶数判定です。");
      const value = values[i - 1];
      if (value % 2 === 0) {
        add(4, "data[" + i + "] = " + value + " は偶数です。加算します。");
        total += value;
        add(5, "total に " + value + " を加え、" + total + " になりました。");
      } else {
        add(5, "data[" + i + "] = " + value + " は奇数です。加算を飛ばします。");
      }
      i += 1;
      add(2, "i を " + i + " に更新しました。while の条件を再判定します。");
    }
    let position = 0;
    function render() {
      const state = states[position];
      iOutput.textContent = state.i === undefined ? "未設定" : String(state.i);
      totalOutput.textContent = state.total === undefined ? "未設定" : String(state.total);
      lines.forEach((line, index) => {
        const active = index === state.line;
        line.classList.toggle("is-active", active);
        if (active) line.setAttribute("aria-current", "step");
        else line.removeAttribute("aria-current");
      });
      nextOutput.textContent = state.line < 0 ? "なし（終了）" : lines[state.line].textContent.trim();
      message.textContent = state.explanation;
      previous.disabled = position === 0;
      next.disabled = position === states.length - 1;
    }
    next.addEventListener("click", () => { if (position < states.length - 1) { position++; render(); } });
    previous.addEventListener("click", () => { if (position > 0) { position--; render(); } });
    reset.addEventListener("click", () => { position = 0; render(); });
    render();
  });

});
