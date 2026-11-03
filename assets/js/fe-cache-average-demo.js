(function () {
  "use strict";
  const root = document.getElementById("fe-cache-demo");
  if (!root) return;
  const $ = (q) => root.querySelector(q);
  const hit = $("#fe-cache-hit"), hitNumber = $("#fe-cache-hit-number");
  const guess = $("#fe-cache-guess"), check = $("#fe-cache-check");
  const answer = $("#fe-cache-answer"), feedback = $("#fe-cache-feedback");
  const error = $("#fe-cache-error"), equal = $("#fe-cache-equal"), reset = $("#fe-cache-reset");
  const timeFields = ["a-cache", "a-memory", "b-cache", "b-memory"].map((id) => $("#fe-cache-" + id));
  const defaults = [60,300,20,420];
  let revealed = false;
  const parse = (field) => {
    const s = field.value.trim();
    return s !== "" && Number.isFinite(Number(s)) && Number(s) >= 0 && Number(s) <= 10000 ? Number(s) : null;
  };
  const fmt = (n) => Number.isInteger(n) ? String(n) : n.toFixed(2).replace(/0+$/, "").replace(/\.$/, "");
  function calc() {
    const nums = timeFields.map(parse), p = parse(hitNumber);
    const valid = nums.every((x) => x !== null) && p !== null && p <= 100;
    if (!valid) return null;
    const [ac,am,bc,bm] = nums, frac = p / 100;
    return { nums, p, a:ac*frac+am*(1-frac), b:bc*frac+bm*(1-frac) };
  }
  function update(note) {
    const result = calc(), valid = result !== null;
    error.hidden = valid;
    error.textContent = valid ? "" : "時間は0〜10000ns、ヒット率は0〜100%で入力してください。";
    check.disabled = !valid;
    equal.disabled = !valid;
    timeFields.concat(hitNumber).forEach((f) => f.setAttribute("aria-invalid", String(!valid && (parse(f) === null || (f === hitNumber && parse(f) > 100)))));
    if (!valid) {
      ["a","b"].forEach((key) => {
        $("#fe-cache-"+key+"-value").textContent = "—";
        $("#fe-cache-"+key+"-formula").textContent = "有効な数値を入力してください。";
        $("#fe-cache-"+key+"-fill").style.width = "0%";
      });
      answer.textContent = "入力を修正してください。";
    } else {
      [["a",result.a,0],["b",result.b,2]].forEach(([key,value,index]) => {
        const cache = result.nums[index], memory = result.nums[index+1];
        const bar = $("#fe-cache-"+key+"-fill");
        bar.style.width = revealed ? Math.min(100, Math.max(0, value/Math.max(1,...result.nums)*100)) + "%" : "0%";
        $("#fe-cache-"+key+"-value").textContent = revealed ? fmt(value) + " ns" : "？";
        $("#fe-cache-"+key+"-formula").textContent = revealed
          ? fmt(cache)+" × "+fmt(result.p/100)+" + "+fmt(memory)+" × "+fmt(1-result.p/100)+" = "+fmt(value)+" ns"
          : "判定後に計算式と結果を表示します。";
      });
      answer.textContent = revealed
        ? (Math.abs(result.a-result.b) < 1e-7 ? "CPU AとCPU Bの平均アクセス時間は同じです。" : result.a < result.b ? "CPU Aの平均アクセス時間が短いです。" : "CPU Bの平均アクセス時間が短いです。")
        : "どちらが短いか予想してから判定しましょう。";
    }
    feedback.textContent = note || (revealed ? "予想と計算結果を比較しましょう。" : "CPU AとCPU Bのどちらが速いか予想しましょう。");
  }
  function changed() {
    revealed = false; guess.value = "";
    update("値を変更しました。どちらが速いか予想しましょう。");
  }
  hit.addEventListener("input", () => { hitNumber.value = hit.value; changed(); });
  hitNumber.addEventListener("input", () => {
    const p = parse(hitNumber);
    if (p !== null && p <= 100) hit.value = String(p);
    changed();
  });
  timeFields.forEach((field) => field.addEventListener("input", changed));
  check.addEventListener("click", () => {
    const result = calc();
    if (!result) return;
    const actual = Math.abs(result.a-result.b) < 1e-7 ? "equal" : result.a < result.b ? "a" : "b";
    const prediction = guess.value;
    revealed = true;
    const message = prediction === "" ? "予想を省略しました。" :
      actual === prediction ? "予想正解！" : "予想とは異なりました。";
    update(message + " ヒット率"+fmt(result.p)+"%、ミス率"+fmt(100-result.p)+"%です。");
  });
  equal.addEventListener("click", () => {
    const result = calc();
    if (!result) return;
    const [ac,am,bc,bm] = result.nums;
    const slope = (ac-am) - (bc-bm);
    const intercept = bm-am;
    if (Math.abs(slope) < 1e-9) {
      feedback.textContent = Math.abs(intercept) < 1e-9
        ? "どのヒット率でも同じ平均アクセス時間です。"
        : "0〜100%に交点はありません（直線が平行です）。";
      return;
    }
    const p = intercept/slope;
    if (p < -1e-9 || p > 1+1e-9) {
      feedback.textContent = "0〜100%の範囲に交点はありません。";
      return;
    }
    const rounded = Math.max(0,Math.min(100,Math.round(p*10000)/100));
    hit.value = String(rounded);hitNumber.value = String(rounded);
    revealed = false;guess.value = "";
    update("交点を計算しました。理論上のヒット率は"+fmt(p*100)+"%。表示は小数第2位までです。");
  });
  reset.addEventListener("click", () => {
    timeFields.forEach((field,i) => { field.value = defaults[i]; });
    hit.value = "0";hitNumber.value = "0";
    revealed = false;guess.value = "";
    update("最初の条件に戻しました。");
  });
  update();
})();
