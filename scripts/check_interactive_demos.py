#!/usr/bin/env python3
"""Run registered pilot lessons against real Jekyll output in Chromium (CI)."""
from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import threading
import traceback
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
WIDTHS = (320, 390, 1280)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def contained(page, root):
    """Inspect inputs, choices and action buttons, not intentionally scrollable tables."""
    result = page.locator(root).evaluate('''root => {
      const bounds = root.getBoundingClientRect();
      const overflow = Array.from(root.querySelectorAll('input,select,fieldset,button')).filter(el => {
        if (el.closest('.fe-cpu-demo__scroll')) return false;
        const r = el.getBoundingClientRect();
        return r.width && (r.left < bounds.left - 1 || r.right > bounds.right + 1);
      }).map(el => el.id || el.textContent);
      return {overflow, left: bounds.left, right: bounds.right, viewport: innerWidth};
    }''')
    assert not result['overflow'], f'Controls outside lesson: {result}'
    assert result['left'] >= -1 and result['right'] <= result['viewport'] + 1, result
    if page.viewport_size['width'] <= 360 and page.locator(root + ' .study-demo__actions').count():
        layout = page.locator(root + ' .study-demo__actions').evaluate('''group => {
          const buttons = Array.from(group.querySelectorAll('button')).map(b => b.getBoundingClientRect());
          return buttons.every((b, i) => !i || b.top >= buttons[i-1].bottom - 1);
        }''')
        assert layout, 'Narrow action buttons should occupy separate rows'


def selection(page, root, value):
    buttons = page.locator(root + ' [data-demo-choice]')
    actual = buttons.evaluate_all('buttons => buttons.filter(b => b.getAttribute("aria-pressed") === "true").map(b => b.dataset.demoChoice)')
    assert actual == ([] if value is None else [value]), actual
    if value is not None:
        styles = page.locator(root + f' [data-demo-choice="{value}"]').evaluate('''b => ({
          background: getComputedStyle(b).backgroundColor, color: getComputedStyle(b).color,
          marker: getComputedStyle(b, '::after').content
        })''')
        assert styles == {'background': 'rgb(30, 64, 175)', 'color': 'rgb(255, 255, 255)', 'marker': '"選択中"'}, styles


def lock(page, expect):
    root = '#fe-lock-compat-demo'
    selection(page, root, 'SS')
    # Native keyboard activation must update the same state as a pointer click.
    page.locator('[data-lock-case="SX"]').focus()
    page.locator('[data-lock-case="SX"]').press('Enter')
    selection(page, root, 'SX')
    page.locator('input[name="fe-lock-guess"][value="no"]').check()
    expect(page.locator('#fe-lock-guide')).to_contain_text('T1がロック取得')
    page.locator('#fe-lock-next').click()
    expect(page.locator('#fe-lock-guide')).to_contain_text('T2がロック要求')
    page.locator('#fe-lock-next').click()
    expect(page.locator('#fe-lock-feedback')).to_contain_text('予想正解')
    expect(page.locator('#fe-lock-state-t2')).to_contain_text('待機中')
    expect(page.locator('#fe-lock-guide')).to_contain_text('T1がロック解放')
    page.locator('#fe-lock-next').click()
    expect(page.locator('#fe-lock-state-t2')).to_contain_text('T1解放後に専有ロック')
    expect(page.locator('#fe-lock-next')).to_be_disabled()
    page.locator('#fe-lock-prev').click()
    expect(page.locator('#fe-lock-state-t2')).to_contain_text('待機中')
    page.locator('#fe-lock-reset').click()
    selection(page, root, 'SX')
    expect(page.locator('#fe-lock-prev')).to_be_disabled()
    # Correctness is defined from the lesson, separately from the UI helper.
    for case in ('SS', 'SX', 'XS', 'XX'):
        page.locator(f'[data-lock-case="{case}"]').click()
        selection(page, root, case)
        page.locator('input[name="fe-lock-guess"][value="yes"]').check()
        page.locator('#fe-lock-next').click()
        page.locator('#fe-lock-next').click()
        expect(page.locator('#fe-lock-state-t2')).to_contain_text('取得済み' if case == 'SS' else '待機中')
        expect(page.locator('#fe-lock-feedback')).to_contain_text('予想正解' if case == 'SS' else '予想と異なりました')
    page.locator('#fe-lock-reset').click()
    page.locator('#fe-lock-t1').select_option('S')
    page.locator('#fe-lock-t2').select_option('S')
    selection(page, root, 'SS')
    contained(page, root)


def two_phase(page, expect):
    root = '#fe-2pc-demo'
    selection(page, root, 'all')
    for preset, guess, verdict in [('one', 'abort', 'ABORT'), ('all', 'commit', 'COMMIT')]:
        page.locator(f'[data-preset="{preset}"]').click()
        selection(page, root, preset)
        page.locator(f'input[name="fe-2pc-guess"][value="{guess}"]').check()
        expect(page.locator('#fe-2pc-guide')).to_contain_text('第1相へ：準備確認')
        page.locator('#fe-2pc-next').click()
        expect(page.locator('#fe-2pc-guide')).to_contain_text('第2相へ：最終決定')
        expect(page.locator('#fe-2pc-status-A')).to_contain_text('未確定')
        page.locator('#fe-2pc-next').click()
        expect(page.locator('#fe-2pc-decision')).to_contain_text(verdict)
        expect(page.locator('#fe-2pc-feedback')).to_contain_text('予想正解')
        expect(page.locator('#fe-2pc-next')).to_be_disabled()
        page.locator('#fe-2pc-prev').click()
        expect(page.locator('#fe-2pc-status-A')).to_contain_text('未確定')
        page.locator('#fe-2pc-reset').click()
        selection(page, root, preset)
    page.locator('[data-participant="A"]').select_option('no')
    selection(page, root, None)
    page.locator('[data-participant="A"]').select_option('yes')
    selection(page, root, 'all')
    # Incorrect prediction and skipped prediction also remain operable.
    page.locator('input[value="abort"]').check()
    page.locator('#fe-2pc-next').click()
    page.locator('#fe-2pc-next').click()
    expect(page.locator('#fe-2pc-feedback')).to_contain_text('予想と違いました')
    page.locator('#fe-2pc-reset').click()
    page.locator('#fe-2pc-next').click()
    page.locator('#fe-2pc-next').click()
    expect(page.locator('#fe-2pc-decision')).to_contain_text('COMMIT')
    page.locator('#fe-2pc-reset').click()
    contained(page, root)


def disk(page, expect):
    root = '#fe-disk-demo'
    for method, first, total in [('fcfs', 120, 220), ('sstf', 95, 120), ('scan', 110, 120)]:
        page.locator('#fe-disk-method').select_option(method)
        contained(page, root)  # Includes the longest SCAN label.
        page.locator('#fe-disk-guess').fill(str(first))
        expect(page.locator('#fe-disk-guide')).to_contain_text('1要求進める')
        page.locator('#fe-disk-next').click()
        expect(page.locator('#fe-disk-current')).to_have_text(str(first))
        expect(page.locator('#fe-disk-feedback')).to_contain_text('予想正解')
        page.locator('#fe-disk-prev').click()
        expect(page.locator('#fe-disk-current')).to_have_text('100')
        page.locator('#fe-disk-all').click()
        expect(page.locator('#fe-disk-distance')).to_have_text(str(total))
        expect(page.locator('#fe-disk-next')).to_be_disabled()
        page.locator('#fe-disk-reset').click()
        expect(page.locator('#fe-disk-distance')).to_have_text('0')
    page.locator('#fe-disk-guess').fill('199')
    page.locator('#fe-disk-next').click()
    expect(page.locator('#fe-disk-feedback')).to_contain_text('予想と異なりました')
    for requests, start, total in [('0,199', '0', 199), ('199,0', '199', 199)]:
        page.locator('#fe-disk-start').fill(start)
        page.locator('#fe-disk-start').press('Tab')
        page.locator('#fe-disk-requests').fill(requests)
        page.locator('#fe-disk-requests').press('Tab')
        page.locator('#fe-disk-all').click()
        expect(page.locator('#fe-disk-distance')).to_have_text(str(total))
    page.locator('#fe-disk-requests').fill('')
    page.locator('#fe-disk-requests').press('Tab')
    expect(page.locator('#fe-disk-feedback')).to_contain_text('入力を確認')
    expect(page.locator('#fe-disk-next')).to_be_disabled()
    expect(page.locator('#fe-disk-guide')).to_contain_text('入力内容を修正')
    page.locator('#fe-disk-start').fill('100')
    page.locator('#fe-disk-requests').fill('120,95,70,80,140,110,60')
    page.locator('#fe-disk-requests').press('Tab')
    contained(page, root)


def cpu(page, expect):
    for method, task in [('fcfs', 'A'), ('sjf', 'B'), ('priority', 'C'), ('rr', 'A')]:
        page.locator('#fe-cpu-kind').select_option(method)
        page.locator(f'input[name="fe-cpu-prediction"][value="{task}"]').check()
        page.locator('#fe-cpu-next').click()
        expect(page.locator('#fe-cpu-feedback')).to_contain_text('正解')
        expect(page.locator('#fe-cpu-timeline [data-task]').first).to_have_attribute('data-task', task)
        page.locator('#fe-cpu-prev').click()
        expect(page.locator('#fe-cpu-prev')).to_be_disabled()
        page.locator('#fe-cpu-all').click()
        expect(page.locator('#fe-cpu-status')).to_contain_text('時刻10')
        expect(page.locator('#fe-cpu-next')).to_be_disabled()
        page.locator('#fe-cpu-reset').click()
    page.locator('#fe-cpu-quantum').select_option('1')
    page.locator('#fe-cpu-next').click()
    page.locator('#fe-cpu-next').click()
    assert page.locator('#fe-cpu-timeline [data-task]').evaluate_all('es=>es.map(e=>e.dataset.task)') == ['A', 'B']
    page.locator('#fe-cpu-reset').click()
    contained(page, '#fe-cpu-demo')


def matrix(page, expect):
    # Root containment alone misses fields hidden by the table's own scroll port.
    clipped = page.locator('.gk-matrix-guided').evaluate('''table => {
      const b = table.getBoundingClientRect();
      return Array.from(table.querySelectorAll('label,input')).filter(el => {
        const r = el.getBoundingClientRect();
        return r.left < b.left - 1 || r.right > b.right + 1 || el.scrollWidth > el.clientWidth + 1;
      }).map(el => el.textContent || el.dataset);
    }''')
    assert not clipped, f'Matrix fields or labels clipped: {clipped}'
    page.locator('[data-fn]').fill('12')
    expect(page.locator('[data-results]')).to_contain_text('Recall 40.0%')
    expect(page.locator('[data-results]')).to_contain_text('Precision 80.0%')
    page.locator('[data-fn]').fill('2')
    page.locator('[data-fp]').fill('12')
    expect(page.locator('[data-results]')).to_contain_text('Precision 40.0%')
    expect(page.locator('[data-results]')).to_contain_text('Recall 80.0%')
    for key in ('tp', 'fn', 'fp', 'tn'):
        page.locator(f'[data-{key}]').fill('0')
    expect(page.locator('[data-results]')).to_have_text('Precision — ／ Recall — ／ Accuracy — ／ F1 —')
    page.locator('[data-tp]').fill('')
    expect(page.locator('[data-results]')).to_contain_text('入力を確認')
    for key, value in [('tp', '8'), ('fn', '2'), ('fp', '2'), ('tn', '88')]:
        page.locator(f'[data-{key}]').fill(value)
    contained(page, '[data-gk-matrix]')


def attention(page, expect):
    # A second consumer of gk-interactive-pilot.css must retain its own layout.
    for query, weights in [('0', [10, 10, 20, 60]), ('2', [5, 10, 70, 15]), ('3', [5, 10, 65, 20])]:
        page.locator('[data-gk-attention] select').select_option(query)
        bars = page.locator('.gk-attention-bar')
        assert bars.count() == 4
        for i, weight in enumerate(weights):
            expect(bars.nth(i)).to_contain_text(f'{weight}%')
        expect(page.locator('[data-summary]')).to_contain_text('QとKで重みを決め')
        contained(page, '[data-gk-attention]')


CHECKS = {'shared-exclusive-lock': lock, 'two-phase-commit': two_phase, 'disk-scheduling': disk,
          'cpu-scheduling': cpu, 'confusion-matrix': matrix, 'attention': attention}


def run(args):
    # A missing build or missing dependency is a failure, never a skipped success.
    from playwright.sync_api import sync_playwright, expect
    registry = json.loads((ROOT / 'tests/browser/pilot.json').read_text())
    plan = json.loads(args.selection.read_text())
    args.artifacts.mkdir(parents=True, exist_ok=True)
    records = []
    report = {'commit': os.environ.get('GITHUB_SHA', 'local-uncommitted'),
              'records': records, 'uncovered_articles': plan['uncovered_articles'],
              'manual_follow_up': ['Instruction clarity and prediction/state proximity',
                                   'Real Android/iOS browser and screen-reader checks',
                                   'Deployed-page confirmation after merge'],
              'environment': 'Chromium, local HTTP server, actual Jekyll output; external requests blocked'}
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(args.site.resolve())))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            report['browser_version'] = browser.version
            for slug in plan['pages']:
                if slug not in CHECKS or slug not in registry:
                    raise ValueError(f'Unknown pilot: {slug}')
                url = registry[slug]['url']
                if not (args.site / url.strip('/') / 'index.html').is_file():
                    raise FileNotFoundError(f'Missing rendered page: {slug}')
                for width in WIDTHS:
                    record = {'page': slug, 'width': width, 'status': 'failed'}
                    records.append(record)
                    context = browser.new_context(viewport={'width': width, 'height': 900})
                    context.route('**/*', lambda route: route.continue_() if urlsplit(route.request.url).hostname == '127.0.0.1' else route.abort())
                    context.tracing.start(screenshots=True, snapshots=True)
                    page = context.new_page()
                    errors = []
                    page.on('pageerror', lambda error: errors.append(str(error)))
                    try:
                        response = page.goto(f'http://127.0.0.1:{server.server_port}{url}', wait_until='load')
                        assert response and response.status == 200
                        expect(page.locator(registry[slug]['root'])).to_be_visible()
                        contained(page, registry[slug]['root'])
                        CHECKS[slug](page, expect)
                        assert not errors, errors
                        page.locator(registry[slug]['root']).screenshot(path=str(args.artifacts / f'{slug}-{width}.png'))
                        record['status'] = 'passed'
                    except Exception:
                        record['error'] = traceback.format_exc()
                        page.screenshot(path=str(args.artifacts / f'{slug}-{width}-failure.png'), full_page=True)
                    finally:
                        context.tracing.stop(path=str(args.artifacts / f'{slug}-{width}.zip'))
                        context.close()
                    print(f"{record['status'].upper()}: {slug} / {width}px", flush=True)
                    if 'error' in record:
                        print(record['error'], flush=True)
                # Static learning fallback is independently checked with scripting off.
                context = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 900})
                context.route('**/*', lambda route: route.continue_() if urlsplit(route.request.url).hostname == '127.0.0.1' else route.abort())
                page = context.new_page()
                try:
                    page.goto(f'http://127.0.0.1:{server.server_port}{url}', wait_until='load')
                    fallback = registry[slug].get('static', {'selector': 'noscript'})
                    expect(page.locator(fallback['selector'])).to_be_visible()
                    expect(page.locator(fallback['selector'])).not_to_be_empty()
                    if 'text' in fallback:
                        expect(page.locator(fallback['selector'])).to_contain_text(fallback['text'])
                    records.append({'page': slug, 'width': 390, 'mode': 'javascript-disabled', 'status': 'passed'})
                except Exception:
                    records.append({'page': slug, 'mode': 'javascript-disabled', 'status': 'failed', 'error': traceback.format_exc()})
                finally:
                    context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        (args.artifacts / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return 1 if any(r['status'] != 'passed' for r in records) else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, default=ROOT / '_site')
    parser.add_argument('--selection', type=Path, required=True)
    parser.add_argument('--artifacts', type=Path, default=ROOT / 'artifacts/interactive-demo')
    raise SystemExit(run(parser.parse_args()))
