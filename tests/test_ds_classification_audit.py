"""Redirects must not become unclassified DS articles after consolidation."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/audit_ds_ver6_classification.py"
spec = importlib.util.spec_from_file_location("ds_classification", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class ClassificationTests(unittest.TestCase):
    def test_requires_layout_null_and_refresh(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "page.md"
            for layout, markup, expected in [
                ("null", '<META content="0; url=/ds/new/" HTTP-EQUIV="Refresh">', True),
                ("page", '<meta http-equiv="refresh" content="0; url=/ds/new/">', False),
                ("null", "通常の説明文", False),
            ]:
                p.write_text(f"---\nlayout: {layout}\n---\n{markup}\n")
                self.assertEqual(audit.is_redirect(p, audit.front_matter(p)), expected)

    def test_report_keeps_real_unclassified_pages_and_separate_denominators(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixtures = {
                "redirect.md": 'layout: null\n---\n<meta http-equiv="refresh" content="0; url=/ds/target/">',
                "classified.md": "layout: page\nds_area: datascience\nds_section: statistics\n---\n説明",
                "unclassified.md": "layout: page\ntitle: 未分類の実記事\n---\n説明",
                "null-without-refresh.md": "layout: null\n---\n転送と断定できないページ",
                "index.md": "layout: page\n---\n索引",
            }
            for name, text in fixtures.items():
                (root / name).write_text("---\n" + text + "\n")
            output = root / "report.md"
            with patch.object(audit, "DS_DIR", root), patch.object(audit, "OUT", output):
                self.assertEqual(audit.main(), 0)
            report = output.read_text()
            for text in ["総数: **5**", "特殊ページ除外: **1**", "転送ページ除外: **1**", "通常記事母数: **3**", "分類済み: **1**", "未分類: **2**"]:
                self.assertIn(text, report)
            ordinary = report.split("## 未分類の通常記事")[1].split("## 分類母数から除外した特殊ページ")[0]
            self.assertNotIn("`redirect.md`", ordinary)
            self.assertIn("`unclassified.md`", ordinary)
            self.assertIn("`null-without-refresh.md`", ordinary)

    def test_redirect_only_has_zero_article_denominator(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "old.md").write_text('---\nlayout: null\n---\n<meta http-equiv="refresh" content="0; url=/ds/new/">')
            output = root / "report.md"
            with patch.object(audit, "DS_DIR", root), patch.object(audit, "OUT", output):
                audit.main()
            self.assertIn("通常記事母数: **0**", output.read_text())


if __name__ == "__main__":
    unittest.main()
