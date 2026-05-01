(function () {
  function getSelected(question) {
    return question.querySelector('input[type="radio"]:checked');
  }

  function markQuestion(question) {
    var selected = getSelected(question);
    var output = question.querySelector("[data-sg-result]");
    var answer = question.getAttribute("data-answer");
    var details = question.querySelector("details");

    if (!selected) {
      output.textContent = "未回答です。選択肢を選んでから確認してください。";
      output.className = "sg-past-result sg-past-result--empty";
      return null;
    }

    if (selected.value === answer) {
      output.textContent = "正解です。";
      output.className = "sg-past-result sg-past-result--correct";
    } else {
      output.textContent = "不正解です。正解は " + answer + " です。";
      output.className = "sg-past-result sg-past-result--wrong";
    }

    if (details) {
      details.open = true;
    }

    return selected.value === answer;
  }

  function scoreAll(container) {
    var questions = Array.prototype.slice.call(document.querySelectorAll(".sg-past-question"));
    var answered = 0;
    var correct = 0;

    questions.forEach(function (question) {
      var selected = getSelected(question);

      if (!selected) {
        return;
      }

      answered += 1;
      if (selected.value === question.getAttribute("data-answer")) {
        correct += 1;
      }
    });

    var output = container.querySelector("[data-sg-score-output]");
    if (!answered) {
      output.textContent = "未回答";
      return;
    }

    var percent = Math.round((correct / answered) * 100);
    output.textContent = answered + "問中 " + correct + "問正解（" + percent + "%）";
  }

  function resetAll(container) {
    document.querySelectorAll('.sg-past-question input[type="radio"]').forEach(function (input) {
      input.checked = false;
    });

    document.querySelectorAll(".sg-past-result").forEach(function (output) {
      output.textContent = "";
      output.className = "sg-past-result";
    });

    document.querySelectorAll(".sg-past-question details").forEach(function (details) {
      details.open = false;
    });

    var output = container.querySelector("[data-sg-score-output]");
    output.textContent = "未採点";
  }

  document.addEventListener("click", function (event) {
    var checkButton = event.target.closest("[data-sg-check]");
    if (checkButton) {
      markQuestion(checkButton.closest(".sg-past-question"));
      return;
    }

    var scoreButton = event.target.closest("[data-sg-score]");
    if (scoreButton) {
      scoreAll(scoreButton.closest("[data-sg-past-actions]"));
      return;
    }

    var resetButton = event.target.closest("[data-sg-reset]");
    if (resetButton) {
      resetAll(resetButton.closest("[data-sg-past-actions]"));
    }
  });
})();
