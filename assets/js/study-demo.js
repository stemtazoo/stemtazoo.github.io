/* No automatic initialization: each teaching aid owns its calculation and state. */
(function () {
  "use strict";
  window.StudyDemoUI = {
    selectChoice: function (root, value) {
      root.querySelectorAll("[data-demo-choice]").forEach(function (button) {
        button.setAttribute("aria-pressed", String(button.dataset.demoChoice === value));
      });
    },
    nextAction: function (button, guide, message) {
      button.setAttribute("aria-describedby", guide.id);
      guide.textContent = message;
    }
  };
})();
