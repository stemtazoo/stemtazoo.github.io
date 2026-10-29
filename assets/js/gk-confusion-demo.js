document.querySelectorAll('[data-gk-matrix]').forEach(root => {
  const keys = ['tp', 'fn', 'fp', 'tn'];
  const inputs = Object.fromEntries(keys.map(key => [key, root.querySelector('[data-' + key + ']')]));
  const output = root.querySelector('[data-results]');
  const feedback = root.querySelector('[data-input-feedback]');
  if (!output || keys.some(key => !inputs[key])) return;

  function draw() {
    const values = {};
    for (const key of keys) {
      const input = inputs[key];
      const raw = input.value.trim();
      const number = Number(raw);
      const valid = raw !== '' && Number.isInteger(number) && number >= 0 && number <= 999;
      input.setAttribute('aria-invalid', String(!valid));
      if (!valid) {
        output.textContent = '入力を確認してください。';
        if (feedback) feedback.textContent = 'TP・FN・FP・TNには0〜999の整数を入力してください。';
        return;
      }
      values[key] = number;
    }
    keys.forEach(key => inputs[key].setAttribute('aria-invalid', 'false'));
    if (feedback) feedback.textContent = '';
    const v = values;
    const div = (a, b) => b ? (100 * a / b).toFixed(1) + '%' : '—';
    output.textContent = 'Precision ' + div(v.tp, v.tp + v.fp)
      + ' ／ Recall ' + div(v.tp, v.tp + v.fn)
      + ' ／ Accuracy ' + div(v.tp + v.tn, v.tp + v.tn + v.fp + v.fn)
      + ' ／ F1 ' + (2 * v.tp + v.fp + v.fn ? (200 * v.tp / (2 * v.tp + v.fp + v.fn)).toFixed(1) + '%' : '—');
  }
  Object.values(inputs).forEach(input => input.addEventListener('input', draw));
  draw();
});
