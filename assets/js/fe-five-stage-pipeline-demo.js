(function () {
  "use strict";
  const root = document.getElementById("fe-pipe-demo");
  if (!root) return;
  const $ = (s) => root.querySelector(s);
  const count = $("#fe-pipe-count"), guess = $("#fe-pipe-guess");
  const next = $("#fe-pipe-next"), back = $("#fe-pipe-back"), reset = $("#fe-pipe-reset"), finish = $("#fe-pipe-finish");
  const cycle = $("#fe-pipe-cycle"), complete = $("#fe-pipe-completed"), result = $("#fe-pipe-feedback");
  const explanation = $("#fe-pipe-explanation"), body = $("#fe-pipe-table tbody");
  const stages = ["IF","ID","EX","MEM","WB"];
  const roles = {
    IF:"命令を取り出す（命令フェッチ）。データメモリのアクセスではありません。",
    ID:"命令を解読し、レジスタの値を読みます。",
    EX:"演算や、ロード・ストア命令の実効アドレス生成を行います。",
    MEM:"必要な場合に、データメモリを読み書きします。IFの命令フェッチとは異なります。",
    WB:"演算結果などをレジスタへ書き戻します。"
  };
  let current = 0, prior = "";
  const total = () => Number(count.value) + 4;
  const completedAt = (step) => Math.max(0,Math.min(Number(count.value),step-4));
  function draw(message) {
    const n = Number(count.value), max = total();
    cycle.textContent = current + " / " + max + " サイクル";
    complete.textContent = completedAt(current) + " / " + n + " 命令完了";
    next.disabled = current === max;
    back.disabled = current === 0;
    finish.disabled = current === max;
    body.replaceChildren();
    for (let i = 1; i <= n; i++) {
      const row = document.createElement("tr"), heading = document.createElement("th");
      heading.scope = "row"; heading.textContent = "命令" + i; row.appendChild(heading);
      for (let j = 0; j < 5; j++) {
        const cell = document.createElement("td");
        const active = current > 0 && current === i+j;
        cell.textContent = active ? stages[j] : "—";
        cell.setAttribute("data-active", String(active));
        cell.setAttribute("data-stage", stages[j]);
        cell.setAttribute("data-instruction", String(i));
        row.appendChild(cell);
      }
      body.appendChild(row);
    }
    const active = [];
    for (let j = 0; j < 5; j++) {
      const i = current-j;
      if (i >= 1 && i <= n) active.push("命令"+i+"： "+stages[j]+"（"+roles[stages[j]]+"）");
    }
    explanation.replaceChildren();
    const intro = document.createElement("p");
    intro.textContent = current === 0 ? "命令はまだ処理を開始していません。" :
      current === max ? "最終サイクルです。最後の命令がWBに到達し、全命令が完了します。" :
      "このサイクルで動いている命令：";
    explanation.appendChild(intro);
    active.forEach((line) => { const p = document.createElement("p");p.textContent=line;explanation.appendChild(p); });
    result.textContent = message || (current === 0
      ? "次のサイクルで命令1がIFに入ります。"
      : "複数命令が別々のステージを同時に進みます。");
  }
  function restart() {
    current = 0;guess.value = "";prior = "";
    draw("最初に戻しました。次の完了命令数を予想してください。");
  }
  count.addEventListener("change",restart);
  next.addEventListener("click", () => {
    if (current >= total()) return;
    const predicted=guess.value;
    current++;
    const actual=String(completedAt(current));
    const msg = predicted === "" ? "予想を省略しました。" :
      predicted === actual ? "予想正解！" : "予想とは異なりました。";
    guess.value = "";
    draw(msg+" "+current+"サイクル目の完了命令数は"+actual+"です。");
  });
  back.addEventListener("click",()=>{if(current===0)return;current--;guess.value="";draw("1サイクル戻しました。");});
  finish.addEventListener("click",()=>{current=total();guess.value="";draw("最後のサイクルまで進めました。");});
  reset.addEventListener("click",restart);
  draw();
})();
