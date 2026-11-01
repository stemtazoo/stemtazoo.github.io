import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from audit_rendered_content import RAW_TABLE, inspect_html, scan


class RenderedContentTests(unittest.TestCase):
    def codes(self, content):
        return {x['code'] for x in inspect_html('<body><main><div data-pagefind-body>' + content + '</div></main></body>')}

    def test_truncated_tool_output_is_reported(self):
        self.assertIn('truncation_marker', self.codes('<p>…1196 tokens truncated…査・遮断する |</p>'))
        self.assertEqual(set(), self.codes('<pre>…1196 tokens truncated…</pre>'))

    def test_unconverted_markdown_table_is_reported(self):
        self.assertIn('unrendered_markdown_table', self.codes('<p>| 誤解 | 正しい理解 |</p>'))
        self.assertEqual(set(), self.codes('<table><tr><td>誤解</td><td>正しい理解</td></tr></table>'))
        self.assertEqual(set(), self.codes('<pre>| 誤解 | 正しい理解 |</pre>'))

    def test_detects_newline_and_split_inline_text(self):
        self.assertIn('literal_newline', self.codes(r'<p>説明\<span>n</span>続き</p>'))
        self.assertIn('literal_newline', self.codes(r'<p>説明\r\n続き</p>'))
        self.assertNotIn('literal_newline', self.codes('<p>説明\n続き</p>'))

    def test_table_row_does_not_consume_surrounding_blank_lines(self):
        # A large blank region reproduces the previous cross-line backtracking.
        row = '\t | 誤解 | 正しい理解 | \t\r'
        text = (' \t\n' * 10000) + row + '\n' + (' \t\n' * 10000)
        self.assertEqual(row, RAW_TABLE.search(text).group())
        self.assertIsNone(RAW_TABLE.search(' \t\n' * 20000))
        self.assertIsNone(RAW_TABLE.search('| 誤解 |\n正しい理解 |'))

    def test_detects_leaked_header_in_paragraph_or_heading(self):
        for content in ('<p>--- layout: page title: test permalink: /fe/test/ ---</p>',
                        '<h2>layout: page</h2><p>title: test</p>'):
            self.assertIn('frontmatter_leak', self.codes(content))
        self.assertNotIn('frontmatter_leak', self.codes('<p>title: はタイトルです。</p>'))

    def test_tex_command_prefixes_are_not_newline_escapes(self):
        for command in (r'\rho', r'\right', r'\rvert', r'\nu', r'\neq', r'\nabla'):
            self.assertNotIn('literal_newline', self.codes('<p>' + command + '</p>'))
        self.assertIn('literal_newline', self.codes(r'<p>\rho 本文\n次の説明</p>'))

    def test_bodyless_jekyll_redirect_is_not_missing_article(self):
        head = ('<!DOCTYPE html><html><meta charset="utf-8">'
                '<link rel="canonical" href="https://stemtazoo.github.io/fe/new/">')
        self.assertEqual([], inspect_html(head + '<meta http-equiv="refresh" content="0; url=/fe/new/">'))
        # Missing or conflicting redirect metadata must still be reported.
        for ending in ('', '<meta http-equiv="refresh" content="0; url=/fe/other/">'):
            self.assertEqual('missing_content_region', inspect_html(head + ending)[0]['code'])
        self.assertIn('literal_newline', {x['code'] for x in inspect_html(
            head + '<meta http-equiv="refresh" content="0; url=/fe/new/"><body>本文\\n続き</body>')})

    def test_excludes_examples_and_invisible_text(self):
        for tag in ('code', 'pre', 'script', 'style', 'template'):
            self.assertEqual(set(), self.codes(f'<{tag}>layout: page title: x \\n {{{{ page.title }}}}</{tag}><p>通常本文</p>'))
        self.assertEqual(set(), self.codes(r'<div hidden>\n</div><span aria-hidden="true">\r</span>'))

    def test_liquid_and_escaped_html(self):
        self.assertIn('unresolved_liquid', self.codes('<p>{{ page.title }}</p>'))
        self.assertIn('unresolved_liquid', self.codes('<p>{% include test.html %}</p>'))
        self.assertIn('escaped_html_tag', self.codes('<p>&lt;div class="x"&gt;本文&lt;/div&gt;</p>'))
        self.assertIn('escaped_html_tag', self.codes('<p>&lt;!DOCTYPE html&gt;</p>'))
        self.assertEqual(set(), self.codes('<p><span>本文</span></p>'))

    def test_scopes_to_article_without_duplicate_nested_regions(self):
        html = r'<body>\n<main><div class="post-content"><div data-pagefind-body><p>正常</p></div></div></main></body>'
        self.assertEqual([], inspect_html(html))
        self.assertIn('frontmatter_leak', {x['code'] for x in inspect_html('<body>--- layout: page title: x ---</body>')})

    def test_block_boundaries_do_not_create_newline_token(self):
        self.assertNotIn('literal_newline', self.codes('<p>\\</p><p>n</p>'))

    def test_scans_all_themes_and_lost_permalink_location(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(ValueError):
                scan(root)
            for theme in ('fe', 'gk', 'ds', 'sg'):
                path = root / theme / 'sample' / 'index.html'
                path.parent.mkdir(parents=True)
                path.write_text(r'<body><main>本文\n続き</main></body>', encoding='utf-8')
            lost = root / 'pages' / 'fe' / 'broken.html'
            lost.parent.mkdir(parents=True)
            lost.write_text('<body>layout: page title: broken</body>', encoding='utf-8')
            result = scan(root)
            self.assertEqual(5, result['scanned_pages'])
            self.assertEqual(5, len(result['findings']))

    def test_progress_and_slow_page_timing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / 'fe'
            folder.mkdir()
            for index in range(101):
                (folder / f'{index:03}.html').write_text('<body>正常</body>', encoding='utf-8')
            clock = iter(range(1000))
            output = StringIO()
            with patch('audit_rendered_content.perf_counter', side_effect=lambda: next(clock)):
                with redirect_stdout(output):
                    result = scan(root)
            log = output.getvalue()
            self.assertIn('starting 101 pages', log)
            self.assertIn('Scanning 1/101: fe/000.html', log)
            self.assertIn('Scanning 101/101: fe/100.html', log)
            self.assertIn('Slow page: fe/000.html took 1.00s', log)
            self.assertIn('completed 101/101 pages', log)
            self.assertIn('Slowest pages:', log)
            self.assertEqual(101, result['scanned_pages'])
            self.assertEqual([], result['findings'])
            self.assertGreater(result['elapsed_seconds'], 0)
            self.assertEqual(5, len(result['slowest_pages']))
            self.assertTrue(all(item['seconds'] == 1 for item in result['slowest_pages']))


if __name__ == '__main__':
    unittest.main()
