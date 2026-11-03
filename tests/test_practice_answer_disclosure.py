"""Regression checks for detection of accidentally exposed practice answers."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_practice_answer_disclosure import audit


class AnswerDisclosureAuditTests(unittest.TestCase):
    def test_finds_unprotected_answer_after_question(self):
        sample = "## 確認問題\n\nどれか。\n\n- ア: x\n\n**正解：ア**\n"
        self.assertEqual("exposed_practice_answer", audit(sample)[0]["level"])

    def test_ignores_answer_inside_details(self):
        sample = (
            "## 確認問題\n\nどれか。\n\n<details markdown=\"1\">\n"
            "<summary>正解を見る</summary>\n\n**正解：イ**\n\n</details>\n"
        )
        self.assertEqual([], audit(sample))

    def test_ignores_fenced_example_and_flags_after_closing(self):
        sample = (
            "## 問題1\n\n```md\n正解：ア\n```\n"
            "<details><summary>開く</summary>\n正解：ア\n</details>\n"
            "**正解：ウ**\n"
        )
        findings = audit(sample)
        self.assertEqual(1, len(findings))
        self.assertEqual("exposed_practice_answer", findings[0]["level"])

    def test_four_theme_answer_formats(self):
        samples = [
            ("FE", "## 確認問題（科目A）\n\nどれか。\n\n**正解：イ**"),
            ("GK", "### 問題3\n\nA. ...\n\n**正解：B**"),
            ("DS", "## 演習問題\n\nどれか。\n\n**正解：3**"),
            ("SG", "## 確認問題（SG試験対策）\n\n- ア：...\n\n**正解：エ**"),
        ]
        for theme, source in samples:
            with self.subTest(theme=theme):
                self.assertEqual("exposed_practice_answer", audit(source)[0]["level"])

    def test_open_details_is_not_accepted_as_hidden(self):
        sample = "## 確認問題\n\n<details open>\n正解：ア\n</details>"
        self.assertEqual("exposed_practice_answer", audit(sample)[0]["level"])

    def test_existing_protected_fe_gk_examples(self):
        for relative in [
            "pages/fe/dfs-vs-bfs.md",
            "pages/fe/binary-tree-traversal.md",
            "pages/gk/optimizer-trick-questions.md",
        ]:
            with self.subTest(relative=relative):
                content = (ROOT / relative).read_text(encoding="utf-8")
                self.assertFalse(
                    any(x["level"] == "exposed_practice_answer" for x in audit(content)),
                    relative,
                )


if __name__ == "__main__":
    unittest.main()
