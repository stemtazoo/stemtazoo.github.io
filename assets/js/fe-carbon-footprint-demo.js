(() => {
  "use strict";
  const root=document.getElementById("fe-carbon-footprint-demo");
  if(!root || root.dataset.ready) return;
  root.dataset.ready="1";
  const specs=[["raw",4],["make",3],["ship",2],["use",0],["end",1]];
  const inputs=specs.map(([name])=>root.querySelector("#cfp-"+name));
  const outputs=specs.map(([name])=>root.querySelector("#cfp-"+name+"-value"));
  const total=root.querySelector("#cfp-total");
  const comparison=root.querySelector("#cfp-comparison");
  const bars=root.querySelector("#cfp-bars");
  const feedback=root.querySelector("#cfp-feedback");
  const guesses=[...root.querySelectorAll("[data-cfp-guess]")];
  let guess=null;
  const getValues=()=>inputs.map(input=>Math.round(Number(input.value)*10));
  function render(){
    const values=getValues();
    const sum=values.reduce((a,b)=>a+b,0);
    outputs.forEach((out,i)=>out.textContent=(values[i]/10).toFixed(1));
    total.textContent=(sum/10).toFixed(1)+" kg-CO₂e";
    const delta=sum-10;
    comparison.textContent="初期値からの変化："+(delta>0?"+":"")+(delta/10).toFixed(1)+" kg-CO₂e";
    bars.replaceChildren();
    values.forEach(v=>{const bar=document.createElement("span");bar.style.width=(sum===0?0:v/sum*100)+"%";bars.appendChild(bar);});
    if(guess===null){feedback.textContent="原材料調達を0.2にすると、合計はどう変わるでしょうか？";}
    else if(delta===0){feedback.textContent="現在は初期値と同じ合計です。原材料調達を動かして変化を確かめましょう。";}
    else {
      const actual=delta<0?"down":"up";
      const right=guess===actual;
      feedback.textContent=(right?"予想どおりです！":"予想とは違いました。")+" 5工程の合計が"+Math.abs(delta/10).toFixed(1)+" kg-CO₂e "+(delta<0?"減りました。":"増えました。")+" CFPは各工程の排出量の合計です。";
    }
  }
  guesses.forEach(b=>{b.setAttribute("aria-pressed","false");b.addEventListener("click",()=>{guess=b.dataset.cfpGuess;guesses.forEach(x=>x.setAttribute("aria-pressed",String(x===b)));render();});});
  inputs.forEach(i=>i.addEventListener("input",render));
  root.querySelector("#cfp-reset").addEventListener("click",()=>{inputs.forEach((i,n)=>i.value=(specs[n][1]/10).toFixed(1));guess=null;guesses.forEach(b=>b.setAttribute("aria-pressed","false"));render();});
  render();
})();