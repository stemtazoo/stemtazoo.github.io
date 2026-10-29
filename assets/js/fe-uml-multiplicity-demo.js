document.querySelectorAll('[data-fe-multiplicity]').forEach(root => {
  const multiplicity = root.querySelector('[data-order-multiplicity]');
  const viewpoint = root.querySelector('[data-viewpoint]');
  const count = root.querySelector('[data-example-count]');
  const customerEnd = root.querySelector('[data-customer-end]');
  const orderEnd = root.querySelector('[data-order-end]');
  const descriptions = {'0..1': '0件または1件', '1': '必ず1件', '0..*': '0件以上', '1..*': '1件以上'};
  function render() {
    const fromCustomer = viewpoint.value === 'customer';
    const rule = fromCustomer ? multiplicity.value : '1';
    const n = Number(count.value);
    const valid = rule === '0..*' || (rule === '1..*' ? n >= 1 : rule === '0..1' ? n <= 1 : n === 1);
    customerEnd.textContent = fromCustomer ? '1' : '1（読む）';
    orderEnd.textContent = multiplicity.value + (fromCustomer ? '（読む）' : '');
    customerEnd.classList.toggle('fe-multiplicity__end--read', !fromCustomer);
    orderEnd.classList.toggle('fe-multiplicity__end--read', fromCustomer);
    const origin = fromCustomer ? '顧客1人' : '注文1件';
    const target = fromCustomer ? '注文' : '顧客';
    const end = fromCustomer ? '注文側' : '顧客側';
    root.querySelector('[data-multiplicity-reading]').textContent = `${origin}から見た${target}は${descriptions[rule]}。反対側の${end}の${rule}を読みます。`;
    root.querySelector('[data-multiplicity-example]').textContent = `${origin}に対応する${target}${n}件は、この多重度で${valid ? '許されます' : '許されません'}。`;
  }
  [multiplicity, viewpoint, count].forEach(control => control.addEventListener('change', render));
  root.querySelector('[data-multiplicity-reset]').addEventListener('click', () => {
    multiplicity.value = '0..*';
    viewpoint.value = 'customer';
    count.value = '1';
    render();
  });
  render();
  root.querySelector('[data-multiplicity-controls]').hidden = false;
});
