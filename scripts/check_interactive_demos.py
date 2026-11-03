#!/usr/bin/env python3
"""Run registered pilot lessons against real Jekyll output in Chromium (CI)."""
from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import re
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


def binary_search(page, expect):
    root = '[data-fe-binary-demo]'
    for rapid in (False, True):
        page.locator('[data-binary-reset]').click()
        for left, right in [('4', '6'), ('4', '4')]:
            page.locator('[data-binary-next]').press('Enter')
            expect(page.locator('[data-binary-left]')).to_have_text(left)
            expect(page.locator('[data-binary-right]')).to_have_text(right)
            if not rapid:
                page.wait_for_timeout(250)
        page.locator('[data-binary-next]').click()
        # The former 180ms callback must not erase the completed state.
        page.wait_for_timeout(250)
        expect(page.locator('[data-binary-cell]').nth(4)).to_have_class(re.compile(r'\bis-found\b'))
        expect(page.locator('[data-binary-mid]')).to_have_text('4')
        expect(page.locator('[data-binary-count]')).to_have_text('3回')
        expect(page.locator('[data-binary-status]')).to_contain_text('発見')
        expect(page.locator('[data-binary-next]')).to_be_disabled()
    page.locator('[data-binary-reset]').click()
    page.locator('[data-binary-next]').click()
    page.locator('[data-binary-reset]').click()  # Reset while a repaint is pending.
    page.wait_for_timeout(250)
    expect(page.locator('[data-binary-count]')).to_have_text('0回')
    expect(page.locator('[data-binary-mid]')).to_have_text('-')
    expect(page.locator('[data-binary-next]')).to_be_enabled()
    for _ in range(3):
        page.locator('[data-binary-next]').click()
    page.wait_for_timeout(250)
    expect(page.locator('[data-binary-mid]')).to_have_text('4')
    expect(page.locator('[data-binary-cell]').nth(4)).to_have_class(re.compile(r'\bis-found\b'))
    contained(page, root)


def cnn(page, expect):
    root = '[data-gk-cnn-demo]'
    def values(n='7', k='3', s='2', p='1'):
        for key, value in [('n', n), ('k', k), ('s', s), ('p', p)]:
            page.locator(f'[data-field="{key}"]').fill(value)
    expect(page.locator('[data-output]')).to_contain_text('4 × 4（窓の位置 1 / 16）')
    page.locator('[data-next]').click()
    expect(page.locator('[data-note]')).to_contain_text('(1, -1)')
    for n, size in [('11', '7'), ('10', '6')]:
        values(n=n, p='2')
        expect(page.locator('[data-output]')).to_contain_text(f'{size} × {size}')
    values(n='5', s='3', p='0')
    page.locator('[data-next]').click()
    expect(page.locator('[data-output]')).to_contain_text('1 × 1（窓の位置 1 / 1）')
    values(n='12', k='1', s='1', p='2')
    expect(page.locator('[data-output]')).to_contain_text('16 × 16')
    values(p='0')
    for _ in range(9):
        page.locator('[data-next]').click()
    expect(page.locator('[data-output]')).to_contain_text('3 × 3（窓の位置 1 / 9）')
    values()
    invalid = [(key, '') for key in ('n', 'k', 's', 'p')]
    invalid += [('n', '4'), ('n', '13'), ('k', '0'), ('k', '4'),
                ('s', '0'), ('s', '4'), ('p', '-1'), ('p', '3')]
    invalid += [(key, '1.5' if key != 'n' else '7.5') for key in ('n', 'k', 's', 'p')]
    for key, value in invalid:
        field = page.locator(f'[data-field="{key}"]')
        field.fill(value)
        expect(field).to_have_value(value)
        expect(field).to_have_attribute('aria-invalid', 'true')
        expect(page.locator('[data-output]')).to_have_text('入力を確認してください。')
        expect(page.locator('[data-next]')).to_be_disabled()
        assert page.locator(root + ' svg rect').count() == 0
        expect(page.locator(root + ' svg')).not_to_be_visible()
        assert not re.search('Infinity|NaN', page.locator(root).inner_text())
        contained(page, root)
        values()
        expect(page.locator('[data-output]')).to_contain_text('4 × 4（窓の位置 1 / 16）')
        expect(page.locator('[data-next]')).to_be_enabled()
        expect(page.locator(root + ' svg')).to_be_visible()
        for field in page.locator(root + ' input').all():
            expect(field).to_have_attribute('aria-invalid', 'false')
        page.locator('[data-next]').click()
        expect(page.locator('[data-output]')).to_contain_text('窓の位置 2 / 16')
    # The final screenshot records the readable input guidance, not an invalid result.
    page.locator('[data-field="n"]').fill('')
    expect(page.locator('[data-output]')).to_have_text('入力を確認してください。')
    contained(page, root)


def adjacency(page, expect):
    root = '[data-fe-adj-demo]'
    # Check the table's own scroll port as well as the lesson boundary.
    clipped = page.locator('.fe-adj-demo__matrix').evaluate('''table => {
      const b = table.getBoundingClientRect();
      return Array.from(table.querySelectorAll('button')).some(button => {
        const r = button.getBoundingClientRect();
        return r.left < b.left - 1 || r.right > b.right + 1;
      }) || table.scrollWidth > table.clientWidth + 1;
    }''')
    assert not clipped, 'Adjacency controls should be visible without table scrolling'
    readable = page.locator('.fe-adj-demo__matrix').evaluate('''table => {
      const headers = Array.from(table.querySelectorAll('th')).filter(th => th.textContent.trim());
      return headers.every(th => {
        const range = document.createRange();
        range.selectNodeContents(th);
        return range.getClientRects().length === 1;
      }) && (innerWidth > 520 || Array.from(table.querySelectorAll('button')).every(b => b.getBoundingClientRect().width >= 24));
    }''')
    assert readable, 'Short matrix labels should remain on one line; narrow-screen buttons must be at least 24px wide'

    # This is a second consumer of fe-visualizer.js; the matrix and graph stay in sync.
    for edge in ('12', '13', '24', '34'):
        page.locator(f'[data-adj-edge="{edge}"]').first.press('Enter')
        for button in page.locator(f'[data-adj-edge="{edge}"]').all():
            expect(button).to_have_text('0')
            expect(button).to_have_attribute('aria-pressed', 'false')
        expect(page.locator(f'[data-graph-edge="{edge}"]')).to_have_class(re.compile(r'\bis-off\b'))
    expect(page.locator('[data-adj-status]')).to_contain_text('辺はありません')
    page.locator('[data-adj-edge="14"]').first.click()
    expect(page.locator('[data-adj-status]')).to_contain_text('V1―V4')
    page.locator('[data-adj-reset]').click()
    for edge in ('12', '13', '24', '34'):
        expect(page.locator(f'[data-graph-edge="{edge}"]')).not_to_have_class(re.compile(r'\bis-off\b'))
    for edge in ('14', '23'):
        expect(page.locator(f'[data-graph-edge="{edge}"]')).to_have_class(re.compile(r'\bis-off\b'))
    contained(page, root)


def binary_tree_traversal(page, expect):
    root = '#fe-tree-traversal-demo'
    sequences = {
        'pre': 'ABDGECF',
        'inside': 'GDBEACF',
        'post': 'GDEBFCA',
    }
    expect(page.locator('#fe-tree-progress')).to_contain_text('0 / 7')
    expect(page.locator('#fe-tree-back')).to_be_disabled()
    # Each traversal: correct guess, incorrect guess, skipped prediction, 7 steps, rollback, reset.
    for mode, sequence in sequences.items():
        page.locator('#fe-tree-mode').select_option(mode)
        expect(page.locator('#fe-tree-output')).to_have_text('まだ記録していません。')
        for i, letter in enumerate(sequence):
            if i == 0:
                page.locator('#fe-tree-guess').select_option(letter)
            elif i == 1:
                page.locator('#fe-tree-guess').select_option('A' if letter != 'A' else 'G')
            page.locator('#fe-tree-next').click()
            expect(page.locator('#fe-tree-output')).to_have_text(' → '.join(sequence[:i + 1]))
            expect(page.locator(f'[data-tree-node="{letter}"]')).to_have_attribute('data-state', 'current')
            if i == 0:
                expect(page.locator('#fe-tree-feedback')).to_contain_text('予想正解')
            if i == 1:
                expect(page.locator('#fe-tree-feedback')).to_contain_text('予想とは違いました')
        expect(page.locator('#fe-tree-next')).to_be_disabled()
        expect(page.locator('#fe-tree-progress')).to_contain_text('7 / 7')
        page.locator('#fe-tree-back').click()
        expect(page.locator('#fe-tree-next')).to_be_enabled()
        expect(page.locator('#fe-tree-output')).to_have_text(' → '.join(sequence[:-1]))
        page.locator('#fe-tree-reset').click()
        expect(page.locator('#fe-tree-output')).to_have_text('まだ記録していません。')
        expect(page.locator('#fe-tree-back')).to_be_disabled()
        expect(page.locator('#fe-tree-next')).to_be_enabled()
    # Native keyboard activation and mobile-size control containment.
    page.locator('#fe-tree-next').focus()
    page.locator('#fe-tree-next').press('Enter')
    expect(page.locator('#fe-tree-output')).to_have_text('G')
    expect(page.locator('#fe-tree-reason')).to_contain_text('左右の部分木を両方調べ終えた後')
    contained(page, root)


def twos_complement(page, expect):
    root = '#fe-twos-demo'
    cases = [
        ('00110110', '11001001', '11001010', '-54'),
        ('11001101', '00110010', '00110011', '51'),
        ('10000000', '01111111', '10000000', '-128'),
        ('00000000', '11111111', '00000000', '0'),
        ('11111111', '00000000', '00000001', '1'),
        ('01111111', '10000000', '10000001', '-127'),
    ]
    expect(page.locator('#fe-twos-back')).to_be_disabled()
    for source, inverted, final, signed in cases:
        page.locator('#fe-twos-preset').select_option(source)
        expect(page.locator('#fe-twos-output')).to_have_text(source)
        page.locator('#fe-twos-prediction').fill(final)
        # The answer is not revealed until both operations have been performed.
        expect(page.locator('#fe-twos-result')).to_contain_text('元の値')
        page.locator('#fe-twos-next').click()
        expect(page.locator('#fe-twos-output')).to_have_text(inverted)
        expect(page.locator('#fe-twos-result')).to_contain_text('まだ表示していません')
        page.locator('#fe-twos-next').click()
        expect(page.locator('#fe-twos-output')).to_have_text(final)
        expect(page.locator('#fe-twos-result')).to_contain_text('整数：' + signed)
        expect(page.locator('#fe-twos-feedback')).to_contain_text('予想正解')
        expect(page.locator('#fe-twos-next')).to_be_disabled()
        if source == '10000000':
            expect(page.locator('#fe-twos-reason')).to_contain_text('+128は8ビット')
        if source == '00000000':
            expect(page.locator('#fe-twos-reason')).to_contain_text('9ビット目への桁上がり')
        page.locator('#fe-twos-back').click()
        expect(page.locator('#fe-twos-output')).to_have_text(inverted)
        page.locator('#fe-twos-reset').click()
        expect(page.locator('#fe-twos-output')).to_have_text(source)
        expect(page.locator('#fe-twos-back')).to_be_disabled()
    # Incorrect prediction, skipped prediction, invalid input, recovery and keyboard use.
    page.locator('#fe-twos-preset').select_option('00110110')
    page.locator('#fe-twos-prediction').fill('00000000')
    page.locator('#fe-twos-next').click()
    page.locator('#fe-twos-next').click()
    expect(page.locator('#fe-twos-feedback')).to_contain_text('予想とは異なりました')
    page.locator('#fe-twos-reset').click()
    page.locator('#fe-twos-next').focus()
    page.locator('#fe-twos-next').press('Enter')
    expect(page.locator('#fe-twos-output')).to_have_text('11001001')
    page.locator('#fe-twos-reset').click()
    page.locator('#fe-twos-input').fill('0000012')
    expect(page.locator('#fe-twos-next')).to_be_disabled()
    expect(page.locator('#fe-twos-error')).to_be_visible()
    page.locator('#fe-twos-input').fill('00000001')
    expect(page.locator('#fe-twos-next')).to_be_enabled()
    page.locator('#fe-twos-next').click()
    page.locator('#fe-twos-next').click()
    expect(page.locator('#fe-twos-output')).to_have_text('11111111')
    expect(page.locator('#fe-twos-feedback')).to_contain_text('予想を省略')
    contained(page, root)


def absolute_relative_path(page, expect):
    root = '#fe-path-demo'
    expect(page.locator('#fe-path-current')).to_have_text('¥a¥a¥b¥c')
    expect(page.locator('#fe-path-back')).to_be_disabled()
    cases = [
        ('example', ['¥a¥a¥b¥c', '¥a¥a¥b', '¥a¥a', '¥a¥a¥a', '¥a¥a¥a¥b', '¥a¥a¥a¥b¥file'],
         ['same', 'up', 'up', 'down', 'down', 'file']),
        ('parent', ['¥a¥a¥b', '¥a¥a'], ['up', 'up']),
        ('same', ['¥a¥a¥b¥c'], ['same']),
    ]
    for case, expected, guesses in cases:
        page.locator('#fe-path-case').select_option(case)
        expect(page.locator('#fe-path-current')).to_have_text('¥a¥a¥b¥c')
        for i, (destination, guess) in enumerate(zip(expected, guesses)):
            page.locator('#fe-path-guess').select_option(guess)
            page.locator('#fe-path-next').click()
            expect(page.locator('#fe-path-current')).to_have_text(destination)
            expect(page.locator('#fe-path-feedback')).to_contain_text('予想正解')
            expect(page.locator('#fe-path-progress')).to_contain_text(str(i + 1) + ' / ')
        expect(page.locator('#fe-path-next')).to_be_disabled()
        page.locator('#fe-path-back').click()
        expect(page.locator('#fe-path-next')).to_be_enabled()
        page.locator('#fe-path-reset').click()
        expect(page.locator('#fe-path-current')).to_have_text('¥a¥a¥b¥c')
        expect(page.locator('#fe-path-back')).to_be_disabled()
    page.locator('#fe-path-case').select_option('example')
    page.locator('#fe-path-guess').select_option('up')  # Incorrect prediction for '.'.
    page.locator('#fe-path-next').click()
    expect(page.locator('#fe-path-feedback')).to_contain_text('予想とは異なりました')
    page.locator('#fe-path-reset').click()
    page.locator('#fe-path-next').focus()
    page.locator('#fe-path-next').press('Enter')
    expect(page.locator('#fe-path-current')).to_have_text('¥a¥a¥b¥c')
    expect(page.locator('#fe-path-feedback')).to_contain_text('予想を省略')
    page.locator('#fe-path-next').click()
    expect(page.locator('#fe-path-current')).to_have_text('¥a¥a¥b')
    expect(page.locator('[data-path-node="b1"]')).to_have_attribute('data-state', 'current')
    contained(page, root)


def er_diagram(page, expect):
    root = '#fe-er-demo'
    cases = [
        ('customer', 'one-many', 3, '1対多', 'C01 → O02'),
        ('product', 'many-many', 4, '多対多', 'O02 → P02'),
        ('badge', 'one-one', 2, '1対1', 'E02 → K02'),
    ]
    expect(page.locator('#fe-er-back')).to_be_disabled()
    for case, guess, count, label, pair in cases:
        page.locator('#fe-er-case').select_option(case)
        expect(page.locator('[data-er-link]')).to_have_count(0)
        page.locator('#fe-er-guess').select_option(guess)
        expect(page.locator('#fe-er-reason')).not_to_contain_text('判定：')
        for n in range(1, count + 1):
            page.locator('#fe-er-next').click()
            expect(page.locator('[data-er-link]')).to_have_count(n)
            expect(page.locator('#fe-er-pairs li')).to_have_count(n)
        expect(page.locator('#fe-er-pairs')).to_contain_text(pair)
        expect(page.locator('#fe-er-reason')).to_contain_text('判定：' + label)
        expect(page.locator('#fe-er-feedback')).to_contain_text('予想正解')
        expect(page.locator('#fe-er-next')).to_be_disabled()
        if case == 'product':
            expect(page.locator('#fe-er-reason')).to_contain_text('中間テーブル')
        page.locator('#fe-er-back').click()
        expect(page.locator('[data-er-link]')).to_have_count(count - 1)
        expect(page.locator('#fe-er-next')).to_be_enabled()
        page.locator('#fe-er-reset').click()
        expect(page.locator('[data-er-link]')).to_have_count(0)
        expect(page.locator('#fe-er-back')).to_be_disabled()
    # Wrong guess, no guess, keyboard activation and a mid-way scenario change.
    page.locator('#fe-er-case').select_option('customer')
    page.locator('#fe-er-guess').select_option('one-one')
    for _ in range(3):
        page.locator('#fe-er-next').click()
    expect(page.locator('#fe-er-feedback')).to_contain_text('予想とは異なりました')
    page.locator('#fe-er-case').select_option('product')
    expect(page.locator('[data-er-link]')).to_have_count(0)
    page.locator('#fe-er-next').focus()
    page.locator('#fe-er-next').press('Enter')
    expect(page.locator('[data-er-link]')).to_have_count(1)
    for _ in range(3):
        page.locator('#fe-er-next').click()
    expect(page.locator('#fe-er-feedback')).to_contain_text('予想を省略')
    contained(page, root)


def logic_circuit_boolean_expression(page, expect):
    root = '#fe-logic-demo'
    # Android/Chromium: NOT must have a drawn overline, not a combining mark.
    overbars = page.locator('.fe-logic-overbar')
    assert overbars.count() >= 20, 'Missing NOT markers in explanations'
    for selector in ('.fe-logic-equation .fe-logic-overbar',
                     '#fe-logic-demo .fe-logic-overbar',
                     'table .fe-logic-overbar'):
        marker = page.locator(selector).first
        expect(marker).to_be_visible()
        style = marker.evaluate('el => ({line:getComputedStyle(el).textDecorationLine, letter:el.textContent, width:el.getBoundingClientRect().width})')
        assert 'overline' in style['line'] and style['letter'] in ('X', 'A') and style['width'] > 0, style
    assert not page.locator('body').evaluate("el => /[AX]\\u0305/.test(el.textContent)"), 'Combining overline remains'
    expect(page.locator('#fe-logic-original')).to_have_text('？')
    expect(page.locator('#fe-logic-count')).to_have_text('0 / 8 通りを確認済み')
    combos = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    for x, y, z in combos:
        key = f'{x}{y}{z}'
        result = y & z
        page.locator('#fe-logic-x').select_option(str(x))
        page.locator('#fe-logic-y').select_option(str(y))
        page.locator('#fe-logic-z').select_option(str(z))
        expect(page.locator('#fe-logic-original')).to_have_text('？')
        expect(page.locator('#fe-logic-simplified')).to_have_text('？')
        page.locator('#fe-logic-guess').select_option(str(result))
        page.locator('#fe-logic-check').click()
        expect(page.locator('#fe-logic-original')).to_have_text(str(result))
        expect(page.locator('#fe-logic-simplified')).to_have_text(str(result))
        expect(page.locator('#fe-logic-feedback')).to_contain_text('予想正解')
        expect(page.locator('#fe-logic-details')).to_contain_text('両方の出力は一致')
        row = page.locator(f'[data-logic-combination="{key}"]')
        expect(row.locator('[data-logic-original]')).to_have_text(str(result))
        expect(row.locator('[data-logic-simple]')).to_have_text(str(result))
        expect(row).to_have_attribute('data-selected', 'true')
    expect(page.locator('#fe-logic-count')).to_have_text('8 / 8 通りを確認済み')
    # Wrong prediction and skipped prediction.
    page.locator('#fe-logic-x').select_option('0')
    page.locator('#fe-logic-y').select_option('1')
    page.locator('#fe-logic-z').select_option('1')
    page.locator('#fe-logic-guess').select_option('0')
    page.locator('#fe-logic-check').click()
    expect(page.locator('#fe-logic-feedback')).to_contain_text('予想とは異なりました')
    page.locator('#fe-logic-next').click()
    expect(page.locator('#fe-logic-original')).to_have_text('？')
    expect(page.locator('#fe-logic-guess')).to_have_value('')
    page.locator('#fe-logic-check').focus()
    page.locator('#fe-logic-check').press('Enter')
    expect(page.locator('#fe-logic-feedback')).to_contain_text('予想を省略')
    page.locator('#fe-logic-reset').click()
    expect(page.locator('#fe-logic-count')).to_have_text('0 / 8 通りを確認済み')
    expect(page.locator('#fe-logic-original')).to_have_text('？')
    for row in page.locator('[data-logic-combination]').all():
        expect(row.locator('[data-logic-original]')).to_have_text('—')
    contained(page, root)


def parity_check(page, expect):
    root = '#fe-parity-demo'
    expect(page.locator('#fe-parity-send')).to_be_enabled()
    expect(page.locator('#fe-parity-one')).to_be_disabled()
    scenarios = [
        ('1011010', 'even', '0', '01011010'),
        ('1111010', 'even', '1', '11111010'),
        ('0000000', 'odd', '1', '10000000'),
        ('1111111', 'odd', '0', '01111111'),
    ]
    for source, kind, bit, expected in scenarios:
        page.locator('#fe-parity-preset').select_option(source)
        page.locator('#fe-parity-mode').select_option(kind)
        page.locator('#fe-parity-guess-bit').select_option(bit)
        page.locator('#fe-parity-send').click()
        expect(page.locator('#fe-parity-sent-text')).to_have_text(expected)
        expect(page.locator('#fe-parity-feedback')).to_contain_text('予想正解')
        expect(page.locator('#fe-parity-sent .fe-parity-demo__bit')).to_have_count(8)
        expect(page.locator('#fe-parity-one')).to_be_enabled()
        # No bit corruption: the receiver accepts the word.
        page.locator('#fe-parity-none').click()
        page.locator('#fe-parity-guess-detect').select_option('no')
        page.locator('#fe-parity-check').click()
        expect(page.locator('#fe-parity-verdict')).to_contain_text('検出しませんでした')
        expect(page.locator('#fe-parity-feedback')).to_contain_text('予想正解')
        # One-bit corruption: change the overall parity, always detected.
        page.locator('#fe-parity-one').click()
        page.locator('#fe-parity-guess-detect').select_option('yes')
        page.locator('#fe-parity-check').click()
        expect(page.locator('#fe-parity-verdict')).to_contain_text('誤りを検出しました')
        expect(page.locator('#fe-parity-feedback')).to_contain_text('予想正解')
        expect(page.locator('#fe-parity-received [data-flipped="true"]')).to_have_count(1)
        # Two-bit corruption: changes the message without changing parity.
        page.locator('#fe-parity-two').click()
        page.locator('#fe-parity-guess-detect').select_option('yes')
        page.locator('#fe-parity-check').click()
        expect(page.locator('#fe-parity-verdict')).to_contain_text('検出しませんでした')
        expect(page.locator('#fe-parity-verdict')).to_contain_text('2ビット反転')
        expect(page.locator('#fe-parity-feedback')).to_contain_text('予想とは異なりました')
        expect(page.locator('#fe-parity-received [data-flipped="true"]')).to_have_count(2)
        assert page.locator('#fe-parity-sent-text').inner_text() != page.locator('#fe-parity-received-text').inner_text()
    # Invalid input, valid recovery, ignored prediction and native keyboard.
    page.locator('#fe-parity-data').fill('0101012')
    expect(page.locator('#fe-parity-send')).to_be_disabled()
    expect(page.locator('#fe-parity-error')).to_be_visible()
    page.locator('#fe-parity-data').fill('1111010')
    page.locator('#fe-parity-mode').select_option('even')
    expect(page.locator('#fe-parity-send')).to_be_enabled()
    page.locator('#fe-parity-send').focus()
    page.locator('#fe-parity-send').press('Enter')
    expect(page.locator('#fe-parity-sent-text')).to_have_text('11111010')
    expect(page.locator('#fe-parity-feedback')).to_contain_text('予想を省略')
    page.locator('#fe-parity-one').click()
    page.locator('#fe-parity-check').click()
    expect(page.locator('#fe-parity-feedback')).to_contain_text('予想を省略')
    page.locator('#fe-parity-reset').click()
    expect(page.locator('#fe-parity-one')).to_be_disabled()
    expect(page.locator('#fe-parity-sent-text')).to_contain_text('送信前')
    contained(page, root)


def cache_hit_rate_average_access_time(page, expect):
    root = '#fe-cache-demo'
    cases = [
        (0, '300 ns', '420 ns', 'a'),
        (50, '180 ns', '220 ns', 'a'),
        (75, '120 ns', '120 ns', 'equal'),
        (100, '60 ns', '20 ns', 'b'),
    ]
    for p, expected_a, expected_b, winner in cases:
        page.locator('#fe-cache-hit-number').fill(str(p))
        expect(page.locator('#fe-cache-a-value')).to_have_text('？')
        page.locator('#fe-cache-guess').select_option(winner)
        page.locator('#fe-cache-check').click()
        expect(page.locator('#fe-cache-a-value')).to_have_text(expected_a)
        expect(page.locator('#fe-cache-b-value')).to_have_text(expected_b)
        expect(page.locator('#fe-cache-feedback')).to_contain_text('予想正解')
        expect(page.locator('#fe-cache-a-formula')).to_contain_text('ns')
        if p == 75:
            expect(page.locator('#fe-cache-answer')).to_contain_text('同じ')
    # Slider and the numeric input are synchronized; results are hidden again.
    page.locator('#fe-cache-hit').evaluate(
        "el => { el.value = '80'; el.dispatchEvent(new Event('input', {bubbles:true})); }")
    expect(page.locator('#fe-cache-hit-number')).to_have_value('80')
    expect(page.locator('#fe-cache-b-value')).to_have_text('？')
    page.locator('#fe-cache-guess').select_option('a')
    page.locator('#fe-cache-check').click()
    expect(page.locator('#fe-cache-feedback')).to_contain_text('予想とは異なりました')
    # The same-as average intersection from the original article is 75%.
    page.locator('#fe-cache-equal').click()
    expect(page.locator('#fe-cache-hit-number')).to_have_value('75')
    expect(page.locator('#fe-cache-a-value')).to_have_text('？')
    page.locator('#fe-cache-check').focus()
    page.locator('#fe-cache-check').press('Enter')
    expect(page.locator('#fe-cache-answer')).to_contain_text('同じ')
    # Change time assumptions and test invalid input / recovery.
    page.locator('#fe-cache-a-cache').fill('40')
    expect(page.locator('#fe-cache-a-value')).to_have_text('？')
    page.locator('#fe-cache-a-cache').fill('-1')
    expect(page.locator('#fe-cache-check')).to_be_disabled()
    expect(page.locator('#fe-cache-error')).to_be_visible()
    page.locator('#fe-cache-a-cache').fill('60')
    expect(page.locator('#fe-cache-check')).to_be_enabled()
    # Degenerate intersection cases must not divide by zero or invent a solution.
    page.locator('#fe-cache-a-cache').fill('20')
    page.locator('#fe-cache-a-memory').fill('420')
    page.locator('#fe-cache-equal').click()
    expect(page.locator('#fe-cache-feedback')).to_contain_text('どのヒット率でも同じ')
    page.locator('#fe-cache-b-cache').fill('30')
    page.locator('#fe-cache-b-memory').fill('430')
    page.locator('#fe-cache-equal').click()
    expect(page.locator('#fe-cache-feedback')).to_contain_text('直線が平行')
    page.locator('#fe-cache-reset').click()
    expect(page.locator('#fe-cache-hit-number')).to_have_value('0')
    expect(page.locator('#fe-cache-a-cache')).to_have_value('60')
    expect(page.locator('#fe-cache-a-value')).to_have_text('？')
    contained(page, root)


def five_stage_pipeline(page, expect):
    root = '#fe-pipe-demo'
    expect(page.locator('#fe-pipe-cycle')).to_have_text('0 / 10 サイクル')
    expect(page.locator('#fe-pipe-back')).to_be_disabled()
    for n in (1, 3, 6, 10):
        page.locator('#fe-pipe-count').select_option(str(n))
        expect(page.locator('#fe-pipe-table tbody tr')).to_have_count(n)
        expect(page.locator('#fe-pipe-cycle')).to_have_text(f'0 / {n+4} サイクル')
        page.locator('#fe-pipe-guess').select_option('0')
        page.locator('#fe-pipe-next').click()
        expect(page.locator('#fe-pipe-feedback')).to_contain_text('予想正解')
        expect(page.locator('[data-instruction="1"][data-stage="IF"]')).to_have_attribute('data-active', 'true')
        for cycle in range(2, n+5):
            page.locator('#fe-pipe-next').click()
            expect(page.locator('#fe-pipe-cycle')).to_have_text(f'{cycle} / {n+4} サイクル')
            expect(page.locator('#fe-pipe-completed')).to_have_text(
                f'{max(0, min(n, cycle-4))} / {n} 命令完了')
            active = max(0, min(n, cycle) - max(1, cycle-4) + 1)
            expect(page.locator('#fe-pipe-table td[data-active="true"]')).to_have_count(active)
            if cycle == 5 and n >= 5:
                expect(page.locator('[data-instruction="1"][data-stage="WB"]')).to_have_attribute('data-active', 'true')
                expect(page.locator('[data-instruction="5"][data-stage="IF"]')).to_have_attribute('data-active', 'true')
        expect(page.locator('#fe-pipe-next')).to_be_disabled()
        expect(page.locator('#fe-pipe-completed')).to_have_text(f'{n} / {n} 命令完了')
        page.locator('#fe-pipe-back').click()
        expect(page.locator('#fe-pipe-next')).to_be_enabled()
        page.locator('#fe-pipe-reset').click()
        expect(page.locator('#fe-pipe-cycle')).to_have_text(f'0 / {n+4} サイクル')
    # Incorrect prediction and keyboard.
    page.locator('#fe-pipe-count').select_option('6')
    page.locator('#fe-pipe-guess').select_option('1')
    page.locator('#fe-pipe-next').focus()
    page.locator('#fe-pipe-next').press('Enter')
    expect(page.locator('#fe-pipe-feedback')).to_contain_text('予想とは異なりました')
    page.locator('#fe-pipe-finish').click()
    expect(page.locator('#fe-pipe-cycle')).to_have_text('10 / 10 サイクル')
    expect(page.locator('#fe-pipe-completed')).to_have_text('6 / 6 命令完了')
    contained(page, root)


def sql_group_by_aggregate_functions(page, expect):
    root = '#fe-group-demo'
    def choose(where, kind, having):
        page.locator('#fe-group-where').select_option(str(where))
        page.locator('#fe-group-kind').select_option(kind)
        page.locator('#fe-group-having').select_option(str(having))
        expect(page.locator('#fe-group-stage')).to_contain_text('FROM')
        expect(page.locator('#fe-group-table tbody tr')).to_have_count(5)

    def advance():
        for stage in ('WHERE', 'GROUP BY', 'HAVING', 'SELECT'):
            page.locator('#fe-group-next').click()
            expect(page.locator('#fe-group-stage')).to_contain_text(stage)

    choose(0, 'SUM', 0)
    page.locator('#fe-group-guess').select_option('3')
    advance()
    expect(page.locator('#fe-group-table tbody tr')).to_have_count(3)
    expect(page.locator('#fe-group-table tbody')).to_contain_text('30')
    expect(page.locator('#fe-group-table tbody')).to_contain_text('20')
    expect(page.locator('#fe-group-table tbody')).to_contain_text('8')
    expect(page.locator('#fe-group-feedback')).to_contain_text('予想正解')
    expect(page.locator('#fe-group-next')).to_be_disabled()
    # Back from SELECT re-exposes HAVING result with excluded rows.
    page.locator('#fe-group-back').click()
    expect(page.locator('#fe-group-stage')).to_contain_text('HAVING')
    page.locator('#fe-group-next').click()
    choose(10, 'SUM', 20)
    page.locator('#fe-group-guess').select_option('1')
    page.locator('#fe-group-next').click()
    expect(page.locator('#fe-group-table tbody tr[data-selected="true"]')).to_have_count(3)
    expect(page.locator('#fe-group-table tbody tr[data-selected="false"]')).to_have_count(2)
    page.locator('#fe-group-next').click()
    expect(page.locator('#fe-group-table tbody tr')).to_have_count(2)
    page.locator('#fe-group-next').click()
    expect(page.locator('#fe-group-table tbody tr[data-selected="true"]')).to_have_count(1)
    page.locator('#fe-group-next').click()
    expect(page.locator('#fe-group-table tbody tr')).to_have_count(1)
    expect(page.locator('#fe-group-table tbody')).to_contain_text('8月1日')
    expect(page.locator('#fe-group-table tbody')).to_contain_text('30')
    expect(page.locator('#fe-group-feedback')).to_contain_text('予想正解')
    # AVG is calculated from rows surviving WHERE, and HAVING uses the aggregate.
    choose(0, 'AVG', 10)
    page.locator('#fe-group-guess').select_option('1')
    advance()
    expect(page.locator('#fe-group-table tbody tr')).to_have_count(1)
    expect(page.locator('#fe-group-table tbody')).to_contain_text('15')
    # COUNT counts rows, not summed quantities.
    choose(0, 'COUNT', 0)
    page.locator('#fe-group-guess').select_option('3')
    advance()
    expect(page.locator('#fe-group-table tbody tr')).to_have_count(3)
    expect(page.locator('#fe-group-table tbody')).to_contain_text('8月3日')
    expect(page.locator('#fe-group-table tbody')).to_contain_text('1')
    # Empty input after WHERE: no phantom group and zero-result feedback.
    choose(25, 'SUM', 0)
    page.locator('#fe-group-guess').select_option('0')
    advance()
    expect(page.locator('#fe-group-table tbody tr')).to_have_count(0)
    expect(page.locator('#fe-group-explanation')).to_contain_text('0グループ')
    expect(page.locator('#fe-group-feedback')).to_contain_text('予想正解')
    # Wrong guess, keyboard Enter, reset and responsive containment.
    choose(0, 'SUM', 0)
    page.locator('#fe-group-guess').select_option('0')
    page.locator('#fe-group-next').focus()
    page.locator('#fe-group-next').press('Enter')
    for _ in range(3):
        page.locator('#fe-group-next').click()
    expect(page.locator('#fe-group-feedback')).to_contain_text('予想とは異なりました')
    page.locator('#fe-group-reset').click()
    expect(page.locator('#fe-group-stage')).to_contain_text('FROM')
    expect(page.locator('#fe-group-where')).to_have_value('0')
    expect(page.locator('#fe-group-kind')).to_have_value('SUM')
    expect(page.locator('#fe-group-guess')).to_have_value('')
    contained(page, root)


def packet_filtering_port_rules(page, expect):
    root = '#fe-port-demo'
    rules = page.locator('[data-fe-port-rule]')
    expect(rules).to_have_count(3)
    fixed_table = page.locator('.fe-port-demo__rules').inner_text()
    cases = [
        # TCP, fixed policy R1, R2 and R3 each genuinely match.
        ('80', '50000', 'request', 'TCP', 'allow', 'R1',
         '192.0.2.10:50000', '198.51.100.20:80'),
        ('80', '50000', 'reply', 'TCP', 'allow', 'R2',
         '198.51.100.20:80', '192.0.2.10:50000'),
        ('443', '51000', 'request', 'TCP', 'allow', 'R3',
         '192.0.2.10:51000', '198.51.100.20:443'),
        # Only packet fields change, but policy remains unchanged.
        ('80', '51000', 'request', 'TCP', 'deny', None,
         '192.0.2.10:51000', '198.51.100.20:80'),
        ('443', '50000', 'request', 'TCP', 'deny', None,
         '192.0.2.10:50000', '198.51.100.20:443'),
        ('443', '51000', 'reply', 'TCP', 'deny', None,
         '198.51.100.20:443', '192.0.2.10:51000'),
        ('80', '50000', 'request', 'UDP', 'deny', None,
         '192.0.2.10:50000', '198.51.100.20:80'),
    ]
    for service, client, direction, protocol, expected, rule, src, dst in cases:
        page.locator('#fe-port-service').select_option(service)
        page.locator('#fe-port-client').select_option(client)
        page.locator('#fe-port-direction').select_option(direction)
        page.locator('#fe-port-protocol').select_option(protocol)
        expect(page.locator('#fe-port-verdict')).to_contain_text('判定前')
        expect(page.locator('#fe-port-packet')).to_contain_text(protocol)
        expect(page.locator('#fe-port-packet')).to_contain_text('送信元 ' + src)
        expect(page.locator('#fe-port-packet')).to_contain_text('宛先 ' + dst)
        assert page.locator('.fe-port-demo__rules').inner_text() == fixed_table
        expect(page.locator('[data-matched="true"]')).to_have_count(0)
        page.locator('#fe-port-guess').select_option(expected)
        page.locator('#fe-port-check').click()
        expect(page.locator('#fe-port-verdict')).to_have_text(
            '判定：許可' if expected == 'allow' else '判定：拒否')
        expect(page.locator('#fe-port-feedback')).to_contain_text('予想正解')
        if rule:
            expect(page.locator('#fe-port-explanation')).to_contain_text(rule)
            expect(page.locator('[data-matched="true"]')).to_have_count(1)
            expect(page.locator(f'[data-fe-port-rule="{rule}"]')).to_have_attribute('data-matched', 'true')
        else:
            expect(page.locator('#fe-port-explanation')).to_contain_text('一致しません')
            expect(page.locator('[data-matched="true"]')).to_have_count(0)
    # A wrong prediction and concrete mismatch reason for changing only client port.
    page.locator('#fe-port-protocol').select_option('TCP')
    page.locator('#fe-port-service').select_option('80')
    page.locator('#fe-port-client').select_option('51000')
    page.locator('#fe-port-direction').select_option('request')
    page.locator('#fe-port-guess').select_option('allow')
    page.locator('#fe-port-check').click()
    expect(page.locator('#fe-port-feedback')).to_contain_text('予想とは異なりました')
    expect(page.locator('#fe-port-explanation')).to_contain_text('送信元ポート')
    # A change to a single header field hides the old answer before prediction.
    page.locator('#fe-port-client').select_option('50000')
    expect(page.locator('#fe-port-verdict')).to_contain_text('判定前')
    expect(page.locator('#fe-port-guess')).to_have_value('')
    page.locator('#fe-port-check').focus()
    page.locator('#fe-port-check').press('Enter')
    expect(page.locator('#fe-port-feedback')).to_contain_text('予想を省略')
    expect(page.locator('#fe-port-verdict')).to_have_text('判定：許可')
    page.locator('#fe-port-reset').click()
    expect(page.locator('#fe-port-service')).to_have_value('80')
    expect(page.locator('#fe-port-client')).to_have_value('50000')
    expect(page.locator('#fe-port-direction')).to_have_value('request')
    expect(page.locator('#fe-port-protocol')).to_have_value('TCP')
    expect(page.locator('#fe-port-verdict')).to_contain_text('判定前')
    assert page.locator('.fe-port-demo__rules').inner_text() == fixed_table
    contained(page, root)

CHECKS = {'shared-exclusive-lock': lock, 'two-phase-commit': two_phase, 'disk-scheduling': disk,
          'cpu-scheduling': cpu, 'confusion-matrix': matrix, 'attention': attention,
          'binary-search': binary_search, 'cnn-output-size': cnn, 'adjacency-matrix': adjacency,
          'binary-tree-traversal': binary_tree_traversal,
          'twos-complement': twos_complement,
          'absolute-relative-path': absolute_relative_path,
          'er-diagram': er_diagram,
          'logic-circuit-boolean-expression': logic_circuit_boolean_expression,
          'parity-check': parity_check,
          'cache-hit-rate-average-access-time': cache_hit_rate_average_access_time,
          'five-stage-pipeline': five_stage_pipeline,
          'sql-group-by-aggregate-functions': sql_group_by_aggregate_functions,
          'packet-filtering-port-rules': packet_filtering_port_rules}


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
                        if slug == 'cnn-output-size':
                            page.locator(registry[slug]['root']).screenshot(path=str(args.artifacts / f'{slug}-{width}-initial.png'))
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
