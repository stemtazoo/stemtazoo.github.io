(function () {
  "use strict";
  const root = document.getElementById("fe-logic-demo");
  if (!root) return;
  const $ = (selector) => root.querySelector(selector);
  const values = ["x", "y", "z"].map((name) => $("#fe-logic-" + name));
  const guess = $("#fe-logic-guess");
  const check = $("#fe-logic-check"), next = $("#fe-logic-next"), reset = $("#fe-logic-reset");
  const original = $("#fe-logic-original"), simplified = $("#fe-logic-simplified");
  const details = $("#fe-logic-details"), feedback = $("#fe-logic-feedback"), count = $("#fe-logic-count");
  const rows = Array.from(root.querySelectorAll("[data-logic-combination]"));
  // A= X∧Y∧Z, B= ¬X∧Y∧Z, F=A∨B and simplified G=Y∧Z.
  function evaluate(x, y, z) {
    const a = x & y & z, b = (1 - x) & y & z;
    return { a, b, f: a | b, g: y & z };
  }
  let revealed = false, checked = new Set();
  function input() {
    return values.map((v) => Number(v.value));
  }
  function update(message) {
    const [x, y, z] = input();
    const key = "" + x + y + z;
    const result = evaluate(x, y, z);
    original.textContent = revealed ? String(result.f) : "？";
    simplified.textContent = revealed ? String(result.g) : "？";
    original.setAttribute("data-value", revealed ? String(result.f) : "");
    simplified.setAttribute("data-value", revealed ? String(result.g) : "");
    details.textContent = revealed
      ? "元の式： (X∧Y∧Z)=" + result.a + "、(¬X∧Y∧Z)=" + result.b
        + "、OR=" + result.f + "。簡単化した式：Y∧Z=" + result.g
        + "。両方の出力は一致します。"
      : "まず結果を予想してください。判定するまで出力を隠しています。";
    feedback.textContent = message || (revealed
      ? "元の式と簡単化後の式は同じ出力です。"
      : "X・Y・Zを選び、出力を予想してから判定してください。");
    count.textContent = checked.size + " / 8 通りを確認済み";
    rows.forEach((tr) => {
      const id = tr.getAttribute("data-logic-combination");
      tr.setAttribute("data-selected", String(revealed && key === id));
      tr.setAttribute("data-checked", String(checked.has(id)));
      const actual = evaluate(...id.split("").map(Number));
      tr.querySelector("[data-logic-original]").textContent = checked.has(id) ? String(actual.f) : "—";
      tr.querySelector("[data-logic-simple]").textContent = checked.has(id) ? String(actual.g) : "—";
    });
  }
  function changeInput() {
    revealed = false;
    guess.value = "";
    update("入力を変更しました。次の結果を予想しましょう。");
  }
  values.forEach((v) => v.addEventListener("change", changeInput));
  check.addEventListener("click", () => {
    const [x,y,z] = input(), result = evaluate(x,y,z);
    checked.add("" + x + y + z);
    revealed = true;
    const predicted = guess.value;
    const response = predicted === "" ? "予想を省略しました。" :
      Number(predicted) === result.f ? "予想正解！" : "予想とは異なりました。";
    update(response + " 元の式も簡単化後の式も" + result.f + "です。");
  });
  next.addEventListener("click", () => {
    const [x,y,z] = input();
    const n = (x * 4 + y * 2 + z + 1) % 8;
    values[0].value = String((n >> 2) & 1);
    values[1].value = String((n >> 1) & 1);
    values[2].value = String(n & 1);
    changeInput();
  });
  reset.addEventListener("click", () => {
    values.forEach((v) => { v.value = "0"; });
    checked = new Set();
    changeInput();
  });
  for (let x = 0; x <= 1; x++) for (let y = 0; y <= 1; y++) for (let z = 0; z <= 1; z++) {
    const {f,g} = evaluate(x,y,z);
    if (f !== g) throw new Error("FE logic lesson: original and simplified expressions differ");
  }
  update();
})();
