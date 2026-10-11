document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-fe-three-stacks]").forEach(root => {
    const steps = [
      {label:"開始",a:[1,2,3],b:[1,2,3],c:[1,2,3],calls:[],message:"3つのデータ用スタックを初期化します。"},
      {label:"行き①",a:[1,2],b:[1,2,3],c:[1,2,3,3],calls:["f()①：再帰の後を待機"],message:"Aの3をCに移し、f()を呼び出します。"},
      {label:"行き②",a:[1],b:[1,2,3],c:[1,2,3,3,2],calls:["f()①：待機","f()②：待機"],message:"Aの2をCに移します。"},
      {label:"行き③",a:[],b:[1,2,3],c:[1,2,3,3,2,1],calls:["f()①：待機","f()②：待機","f()③：待機"],message:"Aの1をCに移します。"},
      {label:"終了条件",a:[],b:[1,2,3],c:[1,2,3,3,2,1],calls:["f()①：待機","f()②：待機","f()③：待機","f()④：Aが空"],message:"Aが空なので4回目のf()は何もせず戻ります。"},
      {label:"戻り③",a:[],b:[1,2,3,1],c:[1,2,3,3,2],calls:["f()①：待機","f()②：待機"],message:"3回目の続きで、Cの1をBに移します。"},
      {label:"戻り②",a:[],b:[1,2,3,1,2],c:[1,2,3,3],calls:["f()①：待機"],message:"2回目の続きで、Cの2をBに移します。"},
      {label:"戻り①",a:[],b:[1,2,3,1,2,3],c:[1,2,3],calls:[],message:"1回目の続きで、Cの3をBに移して終了です。"}
    ];
    let position=0;
    const data=root.querySelector("[data-three-stacks-data]");
    const calls=root.querySelector("[data-three-stacks-calls]");
    const phase=root.querySelector("[data-three-stacks-phase]");
    const message=root.querySelector("[data-three-stacks-message]");
    const prev=root.querySelector("[data-three-stacks-prev]");
    const next=root.querySelector("[data-three-stacks-next]");
    function render(){
      const s=steps[position];
      phase.textContent="ステップ "+position+"/"+(steps.length-1)+"： "+s.label;
      data.replaceChildren();
      ["a","b","c"].forEach(key=>{
        const row=document.createElement("p");
        row.style.margin=".35rem 0";
        const name=document.createElement("strong");
        name.textContent=key.toUpperCase()+"：";
        const values=document.createElement("span");
        values.textContent="["+s[key].join(", ")+"]";
        values.style.overflowWrap="anywhere";
        row.append(name,values);
        data.appendChild(row);
      });
      calls.replaceChildren();
      if(!s.calls.length){calls.textContent="空（待機中の呼び出しなし）";}
      s.calls.forEach((label,i)=>{
        const line=document.createElement("div");
        line.className="fe-recursion-trace__return-card"+(i===s.calls.length-1?" is-latest":"");
        line.textContent=label;
        calls.appendChild(line);
      });
      message.textContent=s.message;
      prev.disabled=position===0;
      next.disabled=position===steps.length-1;
    }
    prev.addEventListener("click",()=>{if(position>0){position--;render();}});
    next.addEventListener("click",()=>{if(position<steps.length-1){position++;render();}});
    root.querySelector("[data-three-stacks-reset]").addEventListener("click",()=>{position=0;render();});
    render();
  });
});
