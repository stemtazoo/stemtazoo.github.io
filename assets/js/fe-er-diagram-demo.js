(function () {
  "use strict";
  const root = document.getElementById("fe-er-demo");
  if (!root) return;
  const $ = (q) => root.querySelector(q);
  const scenarios = {
    customer: {
      title: "顧客と注文", left: "顧客", right: "注文",
      lhs: ["C01", "C02"], rhs: ["O01", "O02", "O03"],
      pairs: [[0,0],[0,1],[1,2]], cardinality: "one-many",
      summary: "1人の顧客が複数の注文を持てます。各注文はこの例では1人の顧客に対応します。"
    },
    product: {
      title: "注文と商品", left: "注文", right: "商品",
      lhs: ["O01", "O02"], rhs: ["P01", "P02", "P03"],
      pairs: [[0,0],[0,1],[1,1],[1,2]], cardinality: "many-many",
      summary: "O01にはP01とP02が含まれ、P02はO01とO02の両方に含まれます。両側の1件が複数に対応するため多対多です。リレーショナルDBに実装する際は注文明細などの中間テーブルが使えます。"
    },
    badge: {
      title: "社員と社員証", left: "社員", right: "社員証",
      lhs: ["E01", "E02"], rhs: ["K01", "K02"],
      pairs: [[0,0],[1,1]], cardinality: "one-one",
      summary: "この例では各社員に1枚の社員証が対応し、各社員証にも1人の社員だけが対応します。"
    }
  };
  const choices = { "one-one": "1対1", "one-many": "1対多", "many-many": "多対多" };
  const select = $("#fe-er-case"), guess = $("#fe-er-guess"), next = $("#fe-er-next"), back = $("#fe-er-back"), reset = $("#fe-er-reset");
  const diagram = $("#fe-er-svg"), progress = $("#fe-er-progress"), pairs = $("#fe-er-pairs");
  const message = $("#fe-er-feedback"), reason = $("#fe-er-reason"), name = $("#fe-er-name");
  const NS = "http://www.w3.org/2000/svg";
  const make = (tag, props, text) => {
    const el = document.createElementNS(NS, tag);
    Object.keys(props).forEach((key) => el.setAttribute(key, String(props[key])));
    if (text !== undefined) el.textContent = text;
    return el;
  };
  let step = 0;
  function render(feedback) {
    const data = scenarios[select.value], done = step === data.pairs.length;
    name.textContent = data.title;
    progress.textContent = step + " / " + data.pairs.length + " 関連を表示";
    const lhsY = (i) => 80 + i * 80, rhsY = (i) => 65 + i * 62;
    const parts = [];
    parts.push(make("text", { x:90,y:24,class:"fe-er-demo__heading" }, data.left));
    parts.push(make("text", { x:310,y:24,class:"fe-er-demo__heading" }, data.right));
    data.pairs.slice(0,step).forEach(([l,r],i) => {
      const line=make("line",{x1:150,y1:lhsY(l),x2:250,y2:rhsY(r),class:"fe-er-demo__edge","data-er-link":i});
      parts.push(line);
    });
    data.lhs.forEach((text,i) => {
      parts.push(make("rect",{x:26,y:lhsY(i)-22,width:124,height:44,rx:8,class:"fe-er-demo__box"}));
      parts.push(make("text",{x:88,y:lhsY(i)+5,class:"fe-er-demo__instance"},text));
    });
    data.rhs.forEach((text,i) => {
      parts.push(make("rect",{x:250,y:rhsY(i)-22,width:124,height:44,rx:8,class:"fe-er-demo__box"}));
      parts.push(make("text",{x:312,y:rhsY(i)+5,class:"fe-er-demo__instance"},text));
    });
    diagram.replaceChildren(...parts);
    diagram.setAttribute("aria-label",data.left+"と"+data.right+"の対応。表示済みの関連は"+step+"本。");
    pairs.replaceChildren();
    data.pairs.slice(0,step).forEach(([l,r]) => {
      const li=document.createElement("li");
      li.textContent=data.lhs[l]+" → "+data.rhs[r];
      pairs.appendChild(li);
    });
    reason.textContent=done
      ? "判定："+choices[data.cardinality]+"。"+data.summary
      : "線を1本ずつ確認します。片側の1件から何件につながるか、両方向で調べましょう。";
    message.textContent=feedback || (done?"すべての関連を表示しました。":"次のつながりを予想して進めましょう。");
    next.disabled=done; back.disabled=step===0; guess.disabled=done;
    next.textContent=done?"完了":"次の関連を表示";
  }
  function restart() { step=0; guess.value=""; render("最初の状態です。対応関係を予想してください。"); }
  select.addEventListener("change",restart);
  reset.addEventListener("click",restart);
  back.addEventListener("click",()=>{if(!step)return;step--;render("1本戻しました。対応する件数を確認しましょう。");});
  next.addEventListener("click",()=>{
    const data=scenarios[select.value];if(step>=data.pairs.length)return;
    step++;
    if(step===data.pairs.length){
      const predicted=guess.value;
      render(!predicted?"予想を省略して判定を表示しました。":predicted===data.cardinality?"予想正解！ "+choices[data.cardinality]+"です。":"予想とは異なりました。 "+choices[data.cardinality]+"です。");
    } else render(step+"本目の関連を追加しました。あと"+(data.pairs.length-step)+"本です。");
  });
  render();
})();
