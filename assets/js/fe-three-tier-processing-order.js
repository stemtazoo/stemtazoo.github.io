(function(){
  function init(){
    document.querySelectorAll('[data-fe-order-demo]').forEach(function(root){
      if(root.dataset.ready==='yes')return;
      root.dataset.ready='yes';
      var steps=[
        {id:'request',label:'検索条件を確認する',note:'受信した条件を業務処理で確認する'},
        {id:'sql',label:'問い合わせ用SQLを準備する',note:'どのデータを取得するか決める'},
        {id:'db',label:'DBで商品情報を検索する',note:'SQLをDBMSで実行し、結果を取得する'},
        {id:'calculate',label:'取得した価格に割引を適用する',note:'取得した値を業務ルールに従って加工する'},
        {id:'response',label:'結果をHTMLにして返す',note:'利用者が見られる応答を作る'}
      ];
      var order=['response','db','request','calculate','sql'];
      var picked=[], checked=false;
      var choiceBox=root.querySelector('[data-choices]');
      var sequence=root.querySelector('[data-sequence]');
      var status=root.querySelector('[data-status]');
      var check=root.querySelector('[data-check]');
      var undo=root.querySelector('[data-undo]');
      var reset=root.querySelector('[data-reset]');
      function find(id){return steps.filter(function(s){return s.id===id})[0]}
      function render(){
        choiceBox.textContent='';
        order.forEach(function(id){
          var s=find(id),used=picked.indexOf(id)!==-1;
          var button=document.createElement('button');
          button.type='button';
          button.textContent=s.label;
          button.disabled=used;
          button.setAttribute('aria-pressed',String(used));
          button.addEventListener('click',function(){
            if(used || picked.length===steps.length)return;
            picked.push(id);checked=false;render();
          });
          choiceBox.appendChild(button);
        });
        sequence.textContent='';
        picked.forEach(function(id){var li=document.createElement('li');li.textContent=find(id).label;sequence.appendChild(li)});
        check.disabled=picked.length!==steps.length;
        undo.disabled=picked.length===0;
        reset.disabled=picked.length===0;
        if(!checked){
          status.dataset.result='';
          status.textContent=picked.length===0?'最初に行う処理を選び、順番に並べてください。':picked.length+' / '+steps.length+' 件選択中。全部並べたら「判定する」を押してください。';
        }
      }
      check.addEventListener('click',function(){
        if(picked.length!==steps.length)return;
        var correct=steps.every(function(s,i){return picked[i]===s.id});
        checked=true;status.dataset.result=correct?'ok':'retry';
        if(correct){
          status.textContent='正解です。条件確認 → SQL準備 → DB検索 → 価格計算 → HTML応答の順です。取得前には価格を計算できず、結果を返す前には応答を作る必要があります。';
        }else{
          var first=steps.findIndex(function(s,i){return picked[i]!==s.id});
          status.textContent='順番を見直しましょう。'+(first+1)+'番目の処理に注目。「検索する前に条件とSQLは準備できているか」「価格計算にはDBの結果が必要か」を確認してください。';
        }
      });
      undo.addEventListener('click',function(){if(picked.length){picked.pop();checked=false;render()}});
      reset.addEventListener('click',function(){picked=[];checked=false;render()});
      render();
    });
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init)}else{init()}
})();
