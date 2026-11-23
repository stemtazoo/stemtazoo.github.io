(() => {
  "use strict";
  const root = document.getElementById("fe-channel-demo");
  if (!root) return;
  const selectors = Array.from(root.querySelectorAll("[data-channel]"));
  const preset = root.querySelector("[data-preset]");
  const overlap = root.querySelector("[data-overlap]");
  const explanation = root.querySelector("[data-explanation]");
  const bands = Array.from(root.querySelectorAll("[data-band]"));
  const predictions = root.querySelector("[data-prediction]");
  const feedback = root.querySelector("[data-feedback]");
  // Teaching approximation: 2.4 GHz, 20 MHz-class 802.11 channels represented
  // as 22 MHz-wide bands; channel centers 2412 + 5*(channel-1) MHz.
  // This is an overlap illustration, not a measured spectrum or RF site survey.
  const WIDTH = 22;
  const MIN = 2399;
  const MAX = 2484;
  const names = ["AP1", "AP2", "AP3"];

  function calculate() {
    const channels = selectors.map(s => Number(s.value));
    const centers = channels.map(ch => 2412 + (ch - 1) * 5);
    const pairs = [];
    for (let i = 0; i < channels.length; i++) {
      for (let j = i + 1; j < channels.length; j++) {
        if (Math.abs(centers[i] - centers[j]) < WIDTH) {
          pairs.push(`${names[i]}(ch${channels[i]})－${names[j]}(ch${channels[j]})`);
        }
      }
    }
    return { channels, centers, pairs };
  }
  function render(reveal) {
    const {channels, centers, pairs} = calculate();
    bands.forEach((band, i) => {
      const left = Math.max(0, ((centers[i] - WIDTH / 2 - MIN) / (MAX - MIN)) * 100);
      const width = (WIDTH / (MAX - MIN)) * 100;
      band.style.left = left + "%";
      band.style.width = width + "%";
      band.textContent = `ch${channels[i]}`;
      band.setAttribute("aria-label", `${names[i]}、チャネル${channels[i]}、中心周波数${centers[i]}MHz`);
    });
    root.querySelectorAll("[data-center]").forEach((item,i)=>{
      item.textContent = `${centers[i]} MHz`;
    });
    if (!reveal) {
      overlap.textContent = "判定前";
      explanation.textContent = "予想を選ぶか、そのまま「重なりを確認」を押してください。";
      feedback.textContent = "チャネル番号が近いほど、使う周波数帯が重なりやすくなります。";
      return;
    }
    overlap.textContent = pairs.length ? `重なる組合せ：${pairs.length}組` : "重なる組合せ：0組";
    explanation.textContent = pairs.length
      ? `模式的に重なる組：${pairs.join("、")}。近くにあるAPは互いの通信に影響する可能性があります。`
      : "このモデルでは3つの帯域に重なりがありません。近隣APへの代表的な割り当て例です。";
    const guess = predictions.value;
    feedback.textContent = (guess === "" ? "" : guess === (pairs.length ? "yes" : "no")
      ? "予想どおりです。 " : "予想とは違いました。 ")
      + "SSIDの名前を変えても周波数の重なりは変わりません。";
    predictions.value = "";
  }
  function setChannels(values) {
    selectors.forEach((s,i)=>{ s.value = String(values[i]); });
    predictions.value="";
    render(false);
  }
  preset.addEventListener("change", () => {
    const values = preset.value === "near" ? [1,2,3] : [1,6,11];
    setChannels(values);
  });
  selectors.forEach(s=>s.addEventListener("change",()=>{
    preset.value="custom";
    predictions.value="";
    render(false);
  }));
  root.querySelector("[data-check]").addEventListener("click",()=>render(true));
  root.querySelector("[data-reset]").addEventListener("click",()=>{
    preset.value="near";
    setChannels([1,2,3]);
  });
  setChannels([1,2,3]);
})();