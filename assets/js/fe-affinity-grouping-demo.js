(() => {
  "use strict";
  const notes = [
    "操作手順を覚えにくい",
    "点検時間が足りない",
    "交換部品の記録が見つからない",
    "操作説明書が古い",
    "点検の担当が曖昧",
    "設備の故障履歴を共有できない"
  ];
  const groupIds = ["A", "B", "C"];
  function init() {
    document.querySelectorAll("[data-fe-affinity-demo]").forEach((root) => {
      const interactive = root.querySelector("[data-affinity-interactive]");
      const cards = root.querySelector("[data-affinity-cards]");
      const groups = root.querySelector("[data-affinity-groups]");
      const reason = root.querySelector("[data-affinity-reason]");
      const review = root.querySelector("[data-affinity-review]");
      const reset = root.querySelector("[data-affinity-reset]");
      const result = root.querySelector("[data-affinity-result]");
      if (![interactive, cards, groups, reason, review, reset, result].every(Boolean)) return;
      const assignments = notes.map(() => "");
      const headings = groupIds.map(() => "");
      function make(tag, className, value) {
        const node = document.createElement(tag);
        if (className) node.className = className;
        if (value !== undefined) node.textContent = value;
        return node;
      }
      function renderGroups() {
        groups.replaceChildren();
        groupIds.forEach((group, i) => {
          const panel = make("div", "fe-affinity-demo__group");
          const label = make("label", "", "グループ" + group + "の見出し");
          const input = make("input");
          input.type = "text";
          input.value = headings[i];
          input.placeholder = "分類後に見出しを考える";
          input.maxLength = 40;
          input.addEventListener("input", () => { headings[i] = input.value; });
          label.appendChild(input);
          panel.appendChild(label);
          const list = make("ul");
          const assigned = assignments.map((g, j) => g === group ? notes[j] : null).filter(Boolean);
          if (assigned.length === 0) {
            list.appendChild(make("li", "fe-affinity-demo__empty", "まだカードがありません"));
          } else {
            assigned.forEach((note) => list.appendChild(make("li", "", note)));
          }
          panel.appendChild(list);
          groups.appendChild(panel);
        });
      }
      notes.forEach((note, i) => {
        const label = make("label", "fe-affinity-demo__card");
        const span = make("span", "", note);
        const select = make("select");
        select.setAttribute("aria-label", note + "の分類先");
        [["", "未分類"], ...groupIds.map(g => [g, "グループ" + g])].forEach(([value, title]) => {
          const option = make("option", "", title);
          option.value = value;
          select.appendChild(option);
        });
        select.addEventListener("change", () => {
          assignments[i] = select.value;
          renderGroups();
          const count = assignments.filter(Boolean).length;
          result.textContent = count + " / " + notes.length + "枚を分類しました。分類理由と見出しも考えてみましょう。";
        });
        label.append(span, select);
        cards.appendChild(label);
      });
      review.addEventListener("click", () => {
        const count = assignments.filter(Boolean).length;
        const used = groupIds.filter(g => assignments.includes(g));
        const missingNames = used.filter(g => !headings[groupIds.indexOf(g)].trim());
        const messages = [];
        if (count < notes.length) messages.push("未分類のカードが" + (notes.length - count) + "枚あります。");
        if (!used.length) messages.push("まず、意味の近いカードをまとめてみましょう。");
        if (missingNames.length) messages.push("使ったグループの見出しを考えてみましょう。");
        if (!reason.value.trim()) messages.push("分類の共通点を言葉にしてみましょう。");
        if (!messages.length) messages.push("分類できました。別の分け方でも説明できるか、元のカードをもう一度見比べてみましょう。");
        result.textContent = messages.join(" ");
      });
      reset.addEventListener("click", () => {
        assignments.fill("");
        headings.fill("");
        reason.value = "";
        cards.querySelectorAll("select").forEach(el => { el.value = ""; });
        renderGroups();
        result.textContent = "初期状態に戻しました。どの意見が似ているか、改めて考えてみましょう。";
      });
      renderGroups();
      interactive.hidden = false;
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
