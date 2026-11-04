/* FE DISTINCT column-and-row comparison */
(function () {
  "use strict";
  var source=[
    ["大山商店","テレビ",25000],
    ["大山商店","テレビ",25000],
    ["大山商店","テレビ",30000],
    ["小川商店","テレビ",30000],
    ["小川商店","テレビ",30000]
  ];
  var options={customer:[0],pair:[0,1],all:[0,1,2]};
  var labels=["顧客名","商品名","単価"];
  function compute(columns,distinct) {
    var selected=source.map(function(row){return columns.map(function(i){return row[i];});});
    if(!distinct)return selected;
    var seen=new Set();
    return selected.filter(function(row){
      var key=JSON.stringify(row);
      if(seen.has(key))return false;
      seen.add(key);
      return true;
    });
  }
  function init() {
    var root=document.getElementById("fe-sql-distinct-demo");
    if(!root || root.dataset.ready==="true")return;
    var choices=Array.prototype.slice.call(root.querySelectorAll('input[name="fe-distinct-columns"]'));
    var enabled=root.querySelector("#fe-distinct-enable");
    var guess=root.querySelector("#fe-distinct-guess");
    var query=root.querySelector("[data-query]");
    var show=root.querySelector("[data-show]");
    var reset=root.querySelector("[data-reset]");
    var result=root.querySelector("[data-result]");
    var feedback=root.querySelector("[data-feedback]");
    var header=root.querySelector("[data-head]");
    var body=root.querySelector("[data-body]");
    var reason=root.querySelector("[data-reason]");
    if(choices.length!==3||!enabled||!guess||!query||!show||!reset||!result||!feedback||!header||!body||!reason)return;
    function selected() {
      var option=choices.find(function(c){return c.checked;});
      return option?option.value:"pair";
    }
    function updateControls(){
      var columns=options[selected()];
      query.textContent="SELECT "+(enabled.checked?"DISTINCT ":"")+columns.map(function(i){return labels[i];}).join(", ")+" FROM 注文表;";
      result.hidden=true;
      guess.value="";
    }
    function put(tag,value,parent){
      var item=document.createElement(tag);
      item.textContent=String(value);
      parent.appendChild(item);
      return item;
    }
    function evaluate(){
      var columns=options[selected()];
      var rows=compute(columns,enabled.checked);
      header.replaceChildren();body.replaceChildren();
      var tr=document.createElement("tr");
      columns.forEach(function(i){put("th",labels[i],tr).setAttribute("scope","col");});
      header.appendChild(tr);
      rows.forEach(function(row){
        var line=document.createElement("tr");
        row.forEach(function(v){put("td",typeof v==="number"?v.toLocaleString("ja-JP"):v,line);});
        body.appendChild(line);
      });
      var predicted=guess.value;
      feedback.textContent=(predicted?(Number(predicted)===rows.length?"予想どおり！ ":"予想とは違いました。 "):"")+"抽出結果は"+rows.length+"行です。";
      reason.textContent=enabled.checked
        ? "選んだ"+columns.length+"列の値の組合せが同じ行は、1行だけ残します。元の注文表5行は変更されません。"
        : "DISTINCTがないので、選択した列の値が同じでも5行すべて残ります。";
      result.hidden=false;
    }
    choices.forEach(function(choice){choice.addEventListener("change",updateControls);});
    enabled.addEventListener("change",updateControls);
    show.addEventListener("click",evaluate);
    reset.addEventListener("click",function(){
      choices.forEach(function(choice){choice.checked=choice.value==="pair";});
      enabled.checked=true;updateControls();
    });
    updateControls();
    root.dataset.ready="true";
  }
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);
  else init();
}());
