"""Regression tests for FE duplicate and redirect candidate discovery."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "fe_duplicate_audit", Path(__file__).resolve().parents[1] / "scripts" / "audit_fe_duplicate_content.py"
)
module = importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class DuplicateAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def article(self, name, content):
        return self.write(
            name + ".md", f"---\nlayout: page\ntitle: {name}\npermalink: /fe/{name}/\n---\n"
            "## まず結論\n" + content + "\n## まとめ\n**試験で迷わないために**\n"
        )

    def test_detects_meta_refresh_regardless_of_file_size(self):
        self.article("source", "要件を満たすための設計方法を考えることが大切です。" * 6)
        self.write("old.md", "---\nlayout: null\npermalink: /fe/old/\n---\n"
                   '<!doctype html>\n<meta http-equiv="refresh" content="0; url=/fe/source/">\n'
                   + "説明文" * 1800)
        pages = module.read_pages(self.root)
        redirects = [p for p in pages if p.redirect]
        self.assertEqual(len(redirects), 1)
        self.assertEqual(redirects[0].target, "/fe/source/")
        self.assertEqual(len([p for p in pages if not p.redirect]), 1)

    def test_detects_duplicate_even_when_titles_differ(self):
        shared = (
            "入力した情報が正しく処理されるかを確認するには、複数の条件と境界値を比較して判断します。"
            "判断対象となる条件が変わると、調べる範囲や試験で注目する言葉も変わります。"
        ) * 4
        self.article("alpha", shared + "固有の説明はこちらです。")
        self.article("beta", shared + "こちらは別の補足です。")
        self.article("gamma", "企業が投資額を決めるには、予算制約と将来の市場環境を確認します。" * 4)
        pages = module.read_pages(self.root)
        pairs = module.candidate_pairs(pages)
        names = {(pages[i].path.stem, pages[j].path.stem) for i, j, *_ in pairs}
        self.assertIn(("alpha", "beta"), names)
        self.assertNotIn(("alpha", "gamma"), names)

    def test_headings_alone_do_not_create_similarities(self):
        self.article("one", "試験を受ける人は必ず具体例を使い、前提条件の範囲を確かめます。" * 4)
        self.article("two", "製造現場では工程変更の記録を残し、変更前後の情報を整理します。" * 4)
        pages = module.read_pages(self.root)
        self.assertEqual(module.candidate_pairs(pages), [])

    def test_source_text_is_never_rewritten(self):
        original = "---\nlayout: page\npermalink: /fe/unchanged/\n---\n大切な考え方を説明します。" * 3
        path = self.write("unchanged.md", original)
        module.read_pages(self.root)
        self.assertEqual(path.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
