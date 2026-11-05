(function () {
"use strict";
var jobs=[["T1",0,3],["T2",1,5],["T3",4,9],["T4",6,11]];
var cp=4;
function category(job,t){
 if(t<job[1])return ["未開始","対象外"];
 if(t<job[2])return ["未コミット","UNDO"];
 if(job[2]<=cp)return ["コミット・反映済み","対象外"];
 return ["コミット・未反映","REDO"];
}
function initialize(){
 var root=document.getElementById("fe-checkpoint-timeline");
 if(!root||root.dataset.ready)return;
 var slider=root.querySelector("#fe-checkpoint-failure");
 var number=root.querySelector("#fe-checkpoint-failure-value");
 var questionTime=root.querySelector("[data-question-time]");
 var result=root.querySelector("[data-result]");
 var msg=root.querySelector("[data-message]");
 var tbody=root.querySelector("[data-table]");
 var ticks=root.querySelector("[data-ticks]");
 var rows=root.querySelector("[data-rows]");
 var explanation=root.querySelector("[data-explanation]");
 var apply=root.querySelector("[data-evaluate]");
 var reset=root.querySelector("[data-reset]");
 var guesses=Array.prototype.slice.call(root.querySelectorAll('input[name="fe-checkpoint-guess"]'));
 if(!slider||!number||!result||!msg||!tbody||!ticks||!rows||!explanation||!apply||!reset)return;
 function syncTime(){
  number.textContent=slider.value;
  if(questionTime)questionTime.textContent=slider.value;
 }
 function node(tag,cls,txt){
  var e=document.createElement(tag);
  if(cls)e.className=cls;
  if(txt!==undefined)e.textContent=txt;
  return e;
 }
 function line(holder,type,t){
  var mark=node("span","fe-checkpoint-timeline__"+type);
  mark.style.left=(t/12*100)+"%";
  mark.setAttribute("aria-hidden","true");
  holder.appendChild(mark);
 }
 function show(){
  var t=Number(slider.value);
  ticks.replaceChildren();
  ticks.appendChild(node("span",null,"時刻"));
  var scale=node("div","fe-checkpoint-timeline__tick-track");
  [0,3,4,6,9,12].forEach(function(v){
   var tick=node("span","fe-checkpoint-timeline__tick",String(v));
   tick.style.left=(v/12*100)+"%";
   scale.appendChild(tick);
  });
  line(scale,"checkpoint",cp);
  line(scale,"failure",t);
  ticks.appendChild(scale);
  rows.replaceChildren();
  tbody.replaceChildren();
  jobs.forEach(function(job){
   var state=category(job,t);
   var row=node("div","fe-checkpoint-timeline__row");
   row.appendChild(node("strong",null,job[0]));
   var track=node("div","fe-checkpoint-timeline__track");
   var bar=node("span","fe-checkpoint-timeline__segment");
   bar.style.left=(job[1]/12*100)+"%";
   bar.style.width=((job[2]-job[1])/12*100)+"%";
   bar.title=job[0]+"：開始"+job[1]+"、コミット"+job[2];
   track.appendChild(bar);
   line(track,"checkpoint",cp);
   line(track,"failure",t);
   row.appendChild(track);
   rows.appendChild(row);
   var tr=node("tr");
   [job[0],state[0],state[1]].forEach(function(value){tr.appendChild(node("td",null,value));});
   tbody.appendChild(tr);
  });
  var outcome=category(jobs[1],t)[1];
  var chosen=guesses.find(function(g){return g.checked;});
  var expected=outcome==="UNDO"?"undo":outcome==="REDO"?"redo":"none";
  msg.textContent=(chosen?(chosen.value===expected?"予想どおり！ ":"もう一度確認しましょう。 "):"")+"時刻"+t+"：T2は"+outcome+"の対象です。";
  explanation.textContent="青い破線がチェックポイント、赤い線が障害時刻です。T1は反映済みです。T2は時刻5より前の障害でUNDO、それ以降は未反映という教材の仮定によってREDOになります。";
  result.hidden=false;
 }
 slider.addEventListener("input",function(){syncTime();result.hidden=true;});
 apply.addEventListener("click",show);
 reset.addEventListener("click",function(){
  slider.value="7";syncTime();
  guesses.forEach(function(g){g.checked=false;});
  result.hidden=true;
 });
 syncTime();
 root.dataset.ready="true";
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",initialize);
else initialize();
}());
