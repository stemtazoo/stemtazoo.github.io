document.querySelectorAll('[data-gk-cnn-demo]').forEach(root => {
  const fields = ['n', 'k', 's', 'p'].map(key => root.querySelector('[data-field="' + key + '"]'));
  const svg = root.querySelector('svg');
  const out = root.querySelector('[data-output]');
  const note = root.querySelector('[data-note]');
  const next = root.querySelector('[data-next]');
  if (fields.some(field => !field) || !svg || !out || !note || !next) return;
  let step = 0;

  function readValues() {
    let valid = true;
    const values = fields.map(field => {
      const raw = field.value.trim();
      const value = Number(raw);
      const allowed = raw !== '' && Number.isInteger(value)
        && value >= Number(field.min) && value <= Number(field.max);
      field.setAttribute('aria-invalid', String(!allowed));
      valid = valid && allowed;
      return value;
    });
    return valid ? values : null;
  }

  function draw() {
    const values = readValues();
    next.disabled = !values;
    if (!values) {
      svg.replaceChildren();
      svg.style.display = 'none';
      out.textContent = '入力を確認してください。';
      note.textContent = '入力サイズ5〜12、カーネル1〜3、ストライド1〜3、パディング0〜2の整数を入力してください（空欄不可）。';
      return;
    }
    svg.style.removeProperty('display');
    const [n, k, s, p] = values;
    const size = n + 2 * p;
    const count = Math.floor((size - k) / s) + 1;
    const total = count * count;
    step = Math.min(step, total - 1);
    const cell = 240 / size;
    let markup = '';
    for (let y = 0; y < size; y++) {
      for (let x = 0; x < size; x++) {
        markup += '<rect x="' + x * cell + '" y="' + y * cell + '" width="' + cell
          + '" height="' + cell + '" fill="' + (x < p || y < p || x >= n + p || y >= n + p ? '#d6e0e4' : '#91b9c3')
          + '" stroke="#6d8e97" stroke-width=".7"/>';
      }
    }
    const xx = (step % count) * s;
    const yy = Math.floor(step / count) * s;
    markup += '<rect x="' + xx * cell + '" y="' + yy * cell + '" width="' + k * cell
      + '" height="' + k * cell + '" fill="#dfaa64" fill-opacity=".25" stroke="#a36d32" stroke-width="3"/>';
    svg.innerHTML = markup;
    out.textContent = '出力：' + count + ' × ' + count + '（窓の位置 ' + (step + 1) + ' / ' + total + '）';
    note.textContent = '窓の左上：(' + (xx - p) + ', ' + (yy - p) + ') ／ 計算：floor(('
      + n + ' + 2×' + p + ' − ' + k + ') ÷ ' + s + ') + 1 = ' + count;
  }

  fields.forEach(field => field.addEventListener('input', () => {
    step = 0;
    draw();
  }));
  next.addEventListener('click', () => {
    const values = readValues();
    if (!values) { draw(); return; }
    const [n, k, s, p] = values;
    const count = Math.floor((n + 2 * p - k) / s) + 1;
    step = (step + 1) % (count * count);
    draw();
  });
  draw();
});
