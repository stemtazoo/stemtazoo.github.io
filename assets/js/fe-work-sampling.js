(function(){"use strict";
var root=document.getElementById("fe-work-sampling");if(!root)return;
var run=document.getElementById("fe-ws-run"),again=document.getElementById("fe-ws-again");
var result=document.getElementById("fe-ws-result"),summary=document.getElementById("fe-ws-summary"),explain=document.getElementById("fe-ws-explain"),fill=document.getElementById("fe-ws-fill"),bar=document.getElementById("fe-ws-bar");
var seed=20261107;
function random(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;}
function reset(){result.hidden=true;again.disabled=true;summary.textContent="";explain.textContent="";fill.style.width="0%";}
function sample(){var checked=root.querySelector('input[name="fe-ws-count"]:checked');if(!checked)return;var n=Number(checked.value),hits=0;
for(var i=0;i<n;i++){if(random()<0.65)hits++;}
var pct=100*hits/n;summary.textContent=n+"回中、組立を観測したのは"+hits+"回。推定割合は"+pct.toFixed(1)+"%。";
fill.style.width=pct+"%";bar.setAttribute("aria-label","組立 "+pct.toFixed(1)+"%、その他 "+(100-pct).toFixed(1)+"%");
explain.textContent="480分中、組立時間は約"+(480*pct/100).toFixed(1)+"分と推定。仮定した真の割合65%との差は"+Math.abs(pct-65).toFixed(1)+"ポイントです。観測回数が多くても毎回真の割合に近づくとは限りません。";
result.hidden=false;again.disabled=false;}
root.querySelectorAll('input[name="fe-ws-count"]').forEach(function(el){el.addEventListener("change",reset);});
run.addEventListener("click",sample);again.addEventListener("click",sample);reset();
}());
