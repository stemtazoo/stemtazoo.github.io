// Manual DOM execution check. Install jsdom@26 outside the repository and set NODE_PATH.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const { JSDOM } = require('jsdom');
const article = fs.readFileSync('pages/fe/uml-multiplicity.md', 'utf8');
const start = article.indexOf('<div class="fe-multiplicity"');
const fragment = article.slice(start, article.indexOf('<script src=', start));
const script = fs.readFileSync('assets/js/fe-uml-multiplicity-demo.js', 'utf8');
const dom = new JSDOM(fragment + fragment, { runScripts: 'outside-only' });
const roots = [...dom.window.document.querySelectorAll('[data-fe-multiplicity]')];
assert.equal(roots.length, 2);
roots.forEach(root => assert.equal(root.querySelector('[data-multiplicity-controls]').hidden, true));
assert.match(roots[0].textContent, /顧客1人から見た注文は0件以上/);
dom.window.eval(script);
const root = roots[0];
const controls = ['order-multiplicity', 'viewpoint', 'example-count'].map(name => root.querySelector(`[data-${name}]`));
const reading = () => root.querySelector('[data-multiplicity-reading]').textContent;
const example = () => root.querySelector('[data-multiplicity-example]').textContent;
function change(index, value) {
  controls[index].value = String(value);
  controls[index].dispatchEvent(new dom.window.Event('change', { bubbles: true }));
}
// Independent enumerated expectations, not a copy of the production predicate.
const allowed = { '0..1': [0,1], '1': [1], '0..*': [0,1,2,3], '1..*': [1,2,3] };
let cases = 0;
for (const rule of Object.keys(allowed)) {
  change(0, rule);
  for (const direction of ['customer', 'order']) {
    change(1, direction);
    for (let count = 0; count <= 3; count++) {
      change(2, count);
      const expected = direction === 'customer' ? allowed[rule].includes(count) : count === 1;
      assert.equal(example().includes('許されません'), !expected, `${rule}/${direction}/${count}`);
      assert.match(reading(), direction === 'customer' ? /反対側の注文側/ : /反対側の顧客側の1/);
      const active = root.querySelectorAll('.fe-multiplicity__end--read');
      assert.equal(active.length, 1);
      assert.equal(active[0].hasAttribute(direction === 'customer' ? 'data-order-end' : 'data-customer-end'), true);
      cases++;
    }
  }
}
// Another instance must remain at its initial state.
assert.match(roots[1].querySelector('[data-multiplicity-reading]').textContent, /顧客1人から見た注文は0件以上/);
root.querySelector('[data-multiplicity-reset]').click();
assert.deepEqual(controls.map(x => x.value), ['0..*', 'customer', '1']);
assert.match(example(), /許されます/);
assert.equal(root.querySelector('[data-multiplicity-controls]').hidden, false);
const initialReading = reading();
root.querySelector('[data-multiplicity-reset]').click();
assert.equal(reading(), initialReading);
console.log(`${cases} combinations passed; read-position, reset, repeated reset, no-JS markup and instance isolation passed. Not a browser/layout test.`);
