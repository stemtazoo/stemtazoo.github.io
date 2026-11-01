"""Regression checks against real Jekyll output; run after the preview build."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from audit_rendered_content import inspect_html


class RenderedElements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.headings = []
        self.rows = []
        self.items = []
        self.options = []
        self.capture = None
        self.text = ''
        self.row = None
        self.in_datalist = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag in ('h2', 'td', 'li'):
            self.capture, self.text = tag, ''
        if tag == 'tr':
            self.row = []
        if tag == 'datalist':
            self.in_datalist = True
        if tag == 'option' and self.in_datalist:
            self.options.append(dict(attrs).get('value'))

    def handle_data(self, data):
        if self.capture:
            self.text += data

    def handle_endtag(self, tag):
        if tag == self.capture:
            if tag == 'h2':
                self.headings.append(self.text.strip())
            elif tag == 'td' and self.row is not None:
                self.row.append(self.text.strip())
            elif tag == 'li':
                self.items.append(self.text.strip())
            self.capture = None
        if tag == 'tr' and self.row is not None:
            self.rows.append(self.row)
            self.row = None
        if tag == 'datalist':
            self.in_datalist = False


@unittest.skipUnless((ROOT / '_site').is_dir(), 'requires the Jekyll preview build')
class ArticleRenderingTests(unittest.TestCase):
    def page(self, slug):
        html = (ROOT / '_site' / 'fe' / slug / 'index.html').read_text(encoding='utf-8')
        self.assertEqual([], inspect_html(html), slug)
        return RenderedElements(html)

    def test_gui_example_does_not_swallow_later_markdown(self):
        page = self.page('gui-controls')
        self.assertIn('定義・仕組み', page.headings)
        self.assertIn('まとめ（試験直前用）', page.headings)
        self.assertEqual(['ノート', 'ペン', '消しゴム'], page.options)
        self.assertTrue(any(len(row) == 3 and row[0] == 'ラジオボタン' for row in page.rows))

    def test_waf_comparison_rows_and_summary_render_separately(self):
        page = self.page('waf')
        for heading in ('科目Bでどう使う？', 'どんな場面で使う？', 'よくある誤解・混同'):
            self.assertIn(heading, page.headings)
        misconceptions = [row for row in page.rows if row and (
            row[0].startswith('WAFは') or row[0] in (
                '通常のファイアウォールと同じ', 'HTTPSならWAFはどこに置いてもよい',
                'DBサーバの直前に置けばよい'))]
        self.assertEqual(7, len(misconceptions))
        self.assertTrue(all(len(row) == 2 for row in misconceptions))
        for phrase in ('OSのセキュリティホールを修正する', 'ウイルスやワームを検出・駆除する',
                       'SSL/TLSの暗号化・復号処理を肩代わりする'):
            self.assertTrue(any(len(row) == 2 and row[0] == phrase for row in page.rows), phrase)
        self.assertTrue(any(item.startswith('脆弱性そのものを修正するのではなく') for item in page.items))


if __name__ == '__main__':
    unittest.main()
