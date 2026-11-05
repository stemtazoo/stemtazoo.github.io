/* FE wireless LAN modes: choose, predict, reveal. */
(function(){
"use strict";
var modes={
 infra:{needsAP:true,top:"アクセスポイント（AP）",left:"PC",right:"スマートフォン",note:"両方の端末が既設APを介して通信します。",explain:"インフラストラクチャモードは既設のアクセスポイントが必要です。端末の通信は通常APを経由します。"},
 adhoc:{needsAP:false,top:"APなし：従来のIBSS",left:"端末A",right:"端末B",note:"APなしで端末同士が直接接続",explain:"アドホックモード（IBSS）は、既設APを使わずに端末同士で通信する従来の方式です。"},
 direct:{needsAP:false,top:"スマートフォン：Group Owner",left:"Group Owner",right:"プリンタ：Client",note:"機器の1台がグループを管理",explain:"Wi-Fi Directは既設APを必要としません。ただしGroup Ownerがアクセスポイントに似た役割で接続を管理します。"}
};
function init(){
 var root=document.getElementById("fe-wireless-modes-demo");
 if(!root||root.dataset.ready==="true")return;
 var choices=Array.prototype.slice.call(root.querySelectorAll("[data-mode]"));
 var guesses=Array.prototype.slice.call(root.querySelectorAll('input[name="fe-wireless-modes-guess"]'));
 var result=root.querySelector("[data-result]");
 var feedback=root.querySelector("[data-feedback]");
 var diagram=root.querySelector("[data-diagram]");
 var explanation=root.querySelector("[data-explanation]");
 var reveal=root.querySelector("[data-reveal]");
 var reset=root.querySelector("[data-reset]");
 if(choices.length!==3||guesses.length!==2||!result||!feedback||!diagram||!explanation||!reveal||!reset)return;
 var active="infra";
 function add(tag,className,value){
  var element=document.createElement(tag);
  if(className)element.className=className;
  element.textContent=value;
  diagram.appendChild(element);
 }
 function choose(mode){
  if(!modes[mode])return;
  active=mode;
  choices.forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.mode===active));});
  guesses.forEach(function(g){g.checked=false;});
  result.hidden=true;
  feedback.textContent="";
  explanation.textContent="";
  diagram.replaceChildren();
 }
 function show(){
  var spec=modes[active];
  var selected=guesses.find(function(x){return x.checked;});
  var correct=spec.needsAP?"no":"yes";
  feedback.textContent=(selected?(selected.value===correct?"予想どおり！ ":"予想と違いました。 "):"")+"既設APは"+(spec.needsAP?"必要です。":"不要です。");
  diagram.replaceChildren();
  add("div","fe-wireless-modes-demo__node fe-wireless-modes-demo__node--center",spec.top);
  add("div","fe-wireless-modes-demo__node",spec.left);
  add("span","fe-wireless-modes-demo__arrow","⇄");
  add("div","fe-wireless-modes-demo__node",spec.right);
  add("p","fe-wireless-modes-demo__caption",spec.note);
  explanation.textContent=spec.explain;
  result.hidden=false;
 }
 choices.forEach(function(b){b.addEventListener("click",function(){choose(b.dataset.mode);});});
 reveal.addEventListener("click",show);
 reset.addEventListener("click",function(){choose("infra");});
 choose("infra");
 root.dataset.ready="true";
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
}());
