/* FE subquery comparison: IN, NOT IN, EXISTS, NOT EXISTS, three-valued NULL behavior. */
(function(){
"use strict";
var employees=[["001","田中"],["002","鈴木"],["003","佐藤"],["004","高橋"]];
var skillRows=[["001","FE"],["002","IP"],["002","FE"],["004","DB"]];
function outcome(person,mode,hasNull){
 var matched=person==="002";
 if(mode==="exists")return {truth:matched?"TRUE":"FALSE",why:"外側の社員番号と一致し、スキルがIPである内側の行が"+(matched?"1件あります。":"0件です。")};
 if(mode==="notexists")return {truth:matched?"FALSE":"TRUE",why:"外側の社員番号と一致するIPスキルの行が"+(matched?"存在するためFALSEです。":"存在しないためTRUEです。")+" NULLの社員番号は等号比較で一致しません。"};
 if(mode==="in")return {truth:matched?"TRUE":hasNull?"UNKNOWN":"FALSE",why:matched?"候補集合に社員番号002が存在します。":hasNull?"候補集合(002, NULL)に一致はなく、NULLとの比較がUNKNOWNです。":"候補集合(002)に社員番号が含まれません。"};
 return {truth:matched?"FALSE":hasNull?"UNKNOWN":"TRUE",why:matched?"候補集合に002があるためNOT INはFALSEです。":hasNull?"NOT IN (002, NULL)は、未一致でもNULLのためUNKNOWNです。":"候補集合(002)に含まれないためTRUEです。"};
}
function init(){
 var root=document.getElementById("fe-subquery-demo");
 if(!root||root.dataset.ready==="true")return;
 var person=root.querySelector("#fe-subquery-person");
 var mode=root.querySelector("#fe-subquery-mode");
 var nullBox=root.querySelector("#fe-subquery-null");
 var skills=root.querySelector("[data-skills]");
 var query=root.querySelector("[data-query]");
 var result=root.querySelector("[data-result]");
 var feedback=root.querySelector("[data-feedback]");
 var detail=root.querySelector("[data-detail]");
 var check=root.querySelector("[data-check]");
 var reset=root.querySelector("[data-reset]");
 var guesses=Array.prototype.slice.call(root.querySelectorAll('input[name="fe-subquery-guess"]'));
 if(!person||!mode||!nullBox||!skills||!query||!result||!feedback||!detail||!check||!reset||guesses.length!==2)return;
 function addSkillRow(id,skill){
  var row=document.createElement("tr");
  [id,skill].forEach(function(value){var cell=document.createElement("td");cell.textContent=value;row.appendChild(cell);});
  skills.appendChild(row);
 }
 function refresh(){
  result.hidden=true;
  feedback.textContent="";
  detail.textContent="";
  guesses.forEach(function(g){g.checked=false;});
  skills.replaceChildren();
  skillRows.forEach(function(row){addSkillRow(row[0],row[1]);});
  if(nullBox.checked)addSkillRow("NULL","IP");
  if(mode.value==="in"||mode.value==="notin"){
   query.textContent="WHERE e.社員番号 "+(mode.value==="in"?"IN":"NOT IN")+" (SELECT s.社員番号 FROM 社員スキル s WHERE s.スキルコード = 'IP')";
  }else{
   query.textContent="WHERE "+(mode.value==="exists"?"EXISTS":"NOT EXISTS")+" (SELECT 1 FROM 社員スキル s WHERE s.社員番号 = e.社員番号 AND s.スキルコード = 'IP')";
  }
 }
 function evaluate(){
  var value=outcome(person.value,mode.value,nullBox.checked);
  var extracted=value.truth==="TRUE";
  var chosen=guesses.find(function(g){return g.checked;});
  feedback.textContent=(chosen?(chosen.value===(extracted?"yes":"no")?"予想どおり！ ":"もう一度確認しましょう。 "):"")+"SQLの条件は"+value.truth+"。この社員は"+(extracted?"抽出されます。":"抽出されません。");
  detail.textContent=value.why+(value.truth==="UNKNOWN"?" WHEREではUNKNOWNは抽出対象になりません。":"");
  result.hidden=false;
 }
 person.addEventListener("change",refresh);
 mode.addEventListener("change",refresh);
 nullBox.addEventListener("change",refresh);
 check.addEventListener("click",evaluate);
 reset.addEventListener("click",function(){person.value="002";mode.value="exists";nullBox.checked=false;refresh();});
 refresh();root.dataset.ready="true";
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
}());
