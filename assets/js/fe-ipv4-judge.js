(function(){
"use strict";
const root=document.getElementById("fe-ipv4-judge");if(!root)return;
const data=[
["172.31.10.5","private","2番目が31です。172.16〜172.31のプライベート範囲に含まれます。"],
["172.32.10.5","public","2番目が32なので172.16〜172.31の範囲外です。一般のグローバルIPの範囲です。"],
["10.24.3.8","private","先頭が10なので10.0.0.0/8のプライベート範囲です。"],
["127.24.6.8","loopback","127.0.0.0/8の全体がループバック用です。"],
["192.168.14.20","private","先頭2つが192.168なのでプライベート範囲です。"],
["169.254.12.9","special","169.254.0.0/16はリンクローカルの特殊用途です。"]
];
const names={private:"プライベートIP",loopback:"ループバック",public:"グローバルIP",special:"その他の特殊用途"};
const el=id=>document.getElementById(id), progress=el("fe-ipv4-progress"),ip=el("fe-ipv4-address"),choices=el("fe-ipv4-choices"),check=el("fe-ipv4-check"),feedback=el("fe-ipv4-feedback"),prev=el("fe-ipv4-prev"),next=el("fe-ipv4-next"),reset=el("fe-ipv4-reset");
let index=0;
function display(){
 progress.textContent=(index+1)+" / "+data.length;ip.textContent=data[index][0];
 choices.querySelectorAll("input").forEach(input=>{input.checked=false;input.disabled=false});
 check.disabled=true;feedback.hidden=true;feedback.textContent="";feedback.className="fe-ipv4-judge__feedback";
 prev.disabled=index===0;next.disabled=index===data.length-1;
}
choices.addEventListener("change",()=>{check.disabled=false;feedback.hidden=true});
check.addEventListener("click",()=>{
 const chosen=choices.querySelector("input:checked");if(!chosen)return;
 const item=data[index],correct=chosen.value===item[1];
 feedback.textContent=(correct?"正解です。":"正解は"+names[item[1]]+"です。")+" "+item[2];
 feedback.className="fe-ipv4-judge__feedback "+(correct?"is-correct":"is-incorrect");
 feedback.hidden=false;check.disabled=true;choices.querySelectorAll("input").forEach(input=>input.disabled=true);
});
prev.addEventListener("click",()=>{if(index>0){index--;display()}});
next.addEventListener("click",()=>{if(index<data.length-1){index++;display()}});
reset.addEventListener("click",()=>{index=0;display()});
display();
}());
