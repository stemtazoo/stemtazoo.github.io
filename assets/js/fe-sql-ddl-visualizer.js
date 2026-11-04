/* FE DDL visualizer: constraint decisions on illustrative fixed data. */
(function(){
"use strict";
var cases={
 primary:{
  rule:"社員コード：PRIMARY KEY（重複不可・NULL不可）",
  reference:"",
  headings:["社員コード","氏名"],
  rows:[["A001","田中"],["A002","鈴木"]],
  candidate:["A001","佐藤"],
  allowed:false,
  explanation:"社員コードA001が既存行と重複します。PRIMARY KEY制約に違反するため登録できません。"
 },
 foreign:{
  rule:"部署コード：FOREIGN KEY REFERENCES 部署(部署コード)",
  reference:"参照先の部署表に存在するコード：D01、D02",
  headings:["社員コード","部署コード"],
  rows:[["A001","D01"],["A002","D02"]],
  candidate:["A003","D99"],
  allowed:false,
  explanation:"部署表にD99が存在しないため参照整合性違反です。外部キーはNULLも許す場合があり、主キーとは別の制約です。"
 },
 notnull:{
  rule:"氏名：NOT NULL",
  reference:"",
  headings:["社員コード","氏名"],
  rows:[["A001","田中"],["A002","鈴木"]],
  candidate:["A003","NULL"],
  allowed:false,
  explanation:"氏名列がNOT NULLなのでNULL値を登録できません。文字列「NULL」ではなくSQLのNULL値です。"
 },
 check:{
  rule:"年齢：CHECK (年齢 >= 0)",
  reference:"",
  headings:["社員コード","年齢"],
  rows:[["A001","25"],["A002","30"]],
  candidate:["A003","-1"],
  allowed:false,
  explanation:"年齢-1はCHECK (年齢 >= 0)の条件を満たさないため登録できません。"
 },
 valid:{
  rule:"社員コード：PRIMARY KEY、部署コード：FOREIGN KEY",
  reference:"参照先の部署表に存在するコード：D01、D02",
  headings:["社員コード","部署コード"],
  rows:[["A001","D01"],["A002","D02"]],
  candidate:["A003","D01"],
  allowed:true,
  explanation:"社員コードA003は重複せず、部署コードD01も参照先にあります。この教材の制約を満たすため登録できます。"
 }
};
function init(){
 var root=document.getElementById("fe-ddl-demo");
 if(!root||root.dataset.ready==="true")return;
 var buttons=Array.prototype.slice.call(root.querySelectorAll("[data-case]"));
 var guess=Array.prototype.slice.call(root.querySelectorAll('input[name="fe-ddl-guess"]'));
 var rule=root.querySelector("[data-rule]");
 var reference=root.querySelector("[data-reference]");
 var heads=Array.prototype.slice.call(root.querySelectorAll("[data-heading]"));
 var existing=root.querySelector("[data-existing]");
 var incoming=root.querySelector("[data-new-row]");
 var result=root.querySelector("[data-result]");
 var feedback=root.querySelector("[data-feedback]");
 var explanation=root.querySelector("[data-explanation]");
 var check=root.querySelector("[data-check]");
 var reset=root.querySelector("[data-reset]");
 if(buttons.length!==5||heads.length!==2||guess.length!==2||!rule||!reference||!existing||!incoming||!result||!feedback||!explanation||!check||!reset)return;
 var mode="primary";
 function choose(next){
  if(!cases[next])return;
  mode=next;
  var c=cases[mode];
  buttons.forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.case===mode));});
  heads.forEach(function(h,i){h.textContent=c.headings[i];});
  rule.textContent=c.rule;
  reference.textContent=c.reference;
  existing.replaceChildren();
  c.rows.forEach(function(values){
   var tr=document.createElement("tr");
   values.forEach(function(value){var td=document.createElement("td");td.textContent=value;tr.appendChild(td);});
   existing.appendChild(tr);
  });
  incoming.textContent=c.candidate.join(" / ");
  guess.forEach(function(g){g.checked=false;});
  result.hidden=true;
  feedback.textContent="";
  explanation.textContent="";
 }
 function show(){
  var c=cases[mode],selected=guess.find(function(g){return g.checked;});
  var expected=c.allowed?"yes":"no";
  feedback.textContent=(selected?(selected.value===expected?"予想どおり！ ":"予想と違いました。 "):"")+(c.allowed?"登録できます。":"登録できません。");
  explanation.textContent=c.explanation;
  result.hidden=false;
 }
 buttons.forEach(function(b){b.addEventListener("click",function(){choose(b.dataset.case);});});
 check.addEventListener("click",show);
 reset.addEventListener("click",function(){choose("primary");});
 choose("primary");root.dataset.ready="true";
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
}());
