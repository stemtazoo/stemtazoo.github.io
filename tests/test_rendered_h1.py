#!/usr/bin/env python3
"""Regression tests for rendered H1 structure."""
import unittest
from scripts.audit_rendered_content import inspect_html


def document(head, body):
    return '<!doctype html><html><head>' + head + '</head><body>' + body + '</body></html>'


class HeadingAuditTests(unittest.TestCase):
    def codes(self, html):
        return [item['code'] for item in inspect_html(html)]

    def test_normal_article_one_h1(self):
        html = document('<title>共有ロック | 学習ノート</title>',
                        '<header><h1>共有ロック</h1></header>'
                        '<main><article><h2>まず結論</h2><p>解説</p></article></main>')
        self.assertFalse([c for c in self.codes(html) if 'h1' in c])

    def test_missing_h1(self):
        html = document('<title>記事</title>', '<main><article><h2>説明</h2></article></main>')
        self.assertIn('missing_h1', self.codes(html))

    def test_multiple_h1(self):
        html = document('<title>記事</title>', '<h1>記事</h1><main><h1>重複</h1></main>')
        self.assertIn('multiple_h1', self.codes(html))

    def test_h1_title_mismatch(self):
        html = document('<title>別の記事 | 学習ノート</title>', '<h1>共有ロック</h1><main>本文</main>')
        self.assertIn('h1_title_mismatch', self.codes(html))

    def test_jekyll_redirect_excluded(self):
        html = document('<link rel="canonical" href="https://example.org/gk/merged/">'
                        '<meta http-equiv="refresh" content="0; url=/gk/merged/">',
                        '<p>記事は統合しました。</p>')
        self.assertNotIn('missing_h1', self.codes(html))


if __name__ == '__main__':
    unittest.main()
