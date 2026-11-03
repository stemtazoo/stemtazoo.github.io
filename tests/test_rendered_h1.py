#!/usr/bin/env python3
"""Regression tests for rendered H1 structure."""
import unittest
from scripts.audit_rendered_content import inspect_headings


def document(head, body):
    return '<!doctype html><html><head>' + head + '</head><body>' + body + '</body></html>'


class HeadingAuditTests(unittest.TestCase):
    def codes(self, html):
        return [item['code'] for item in inspect_headings(html)]

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

    def test_title_over_70_is_reported(self):
        html = document('<title>' + 'A' * 71 + '</title>', '<h1>説明</h1>')
        self.assertIn('title_too_long', self.codes(html))

    def test_intentional_shorter_seo_title_keeps_h1(self):
        html = document('<title>短いSEOタイトル【G検定】</title>'
                        '<meta name="stemtazoo-seo-title-override" content="true">',
                        '<header><h1>長い可視タイトルの説明【G検定】</h1></header>')
        self.assertEqual([], self.codes(html))

    def test_non_overridden_page_still_checks_h1_title(self):
        html = document('<title>短いSEOタイトル【G検定】</title>',
                        '<h1>別のタイトル【G検定】</h1>')
        self.assertIn('h1_title_mismatch', self.codes(html))

    def test_jekyll_redirect_excluded(self):
        html = document('<link rel="canonical" href="https://example.org/gk/merged/">'
                        '<meta http-equiv="refresh" content="0; url=/gk/merged/">',
                        '<p>記事は統合しました。</p>')
        self.assertNotIn('missing_h1', [f['code'] for f in inspect_headings(html, redirect=True)])


if __name__ == '__main__':
    unittest.main()
