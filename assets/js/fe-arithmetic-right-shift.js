(function(){
  function init(){
    document.querySelectorAll('[data-fe-signshift]').forEach(function(root){
      if(root.dataset.initialized)return;
      root.dataset.initialized='yes';
      var valueSelect=root.querySelector('[data-signshift-value]');
      var modeSelect=root.querySelector('[data-signshift-mode]');
      var amount=root.querySelector('[data-signshift-amount]');
      var amountLabel=root.querySelector('[data-signshift-amount-label]');
      var original=root.querySelector('[data-signshift-original]');
      var shifted=root.querySelector('[data-signshift-shifted]');
      var before=root.querySelector('[data-signshift-before]');
      var after=root.querySelector('[data-signshift-after]');
      var summary=root.querySelector('[data-signshift-summary]');
      function paint(el,n,fillCount){
        el.textContent='';
        var bits=(n&255).toString(2).padStart(8,'0');
        bits.split('').forEach(function(bit,i){
          var span=document.createElement('span');
          span.className='fe-signshift__bit'+(i<fillCount?' fe-signshift__bit--filled':'');
          span.textContent=bit;
          span.setAttribute('aria-hidden','true');
          el.appendChild(span);
        });
        el.setAttribute('aria-label',bits);
      }
      function update(){
        var raw=Number(valueSelect.value), shift=Number(amount.value);
        var arithmetic=modeSelect.value==='arithmetic';
        var signed=(raw&128)?raw-256:raw;
        var numericStart=arithmetic?signed:raw;
        var result=arithmetic?(signed>>shift):(raw>>>shift);
        var resultBits=result&255;
        amountLabel.textContent=String(shift);
        paint(original,raw,0);
        paint(shifted,resultBits,shift);
        before.textContent='元の8ビット：'+raw.toString(2).padStart(8,'0')+'（'+(arithmetic?'符号付き':'符号なし')+' '+numericStart+'）';
        after.textContent='結果の8ビット：'+resultBits.toString(2).padStart(8,'0')+'（'+(arithmetic?'符号付き':'符号なし')+' '+result+'）';
        var divisor=Math.pow(2,shift);
        var fill=arithmetic && signed<0?'1':'0';
        summary.textContent='左端に補う値：'+fill+'。'+numericStart+' ÷ '+divisor+' = '+(numericStart/divisor)+' → シフト後 '+result+'。'+(arithmetic?'2の補数表現として解釈し、整数に割り切れないときは負の無限大方向に丸めます。':'8ビットを符号なし整数として解釈し、端数を切り捨てます。');
      }
      [valueSelect,modeSelect,amount].forEach(function(node){node.addEventListener('change',update);node.addEventListener('input',update)});
      update();
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
