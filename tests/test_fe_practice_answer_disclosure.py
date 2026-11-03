"""Prevent FE practice-question answers from being exposed before the learner opens them."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
TARGETS = (
    "pages/fe/dfs-vs-bfs.md",
    "pages/fe/binary-tree-traversal.md",
)

class PracticeAnswerDisclosureTests(unittest.TestCase):
    def test_answers_are_inside_closed_native_details(self):
        for relative_path in TARGETS:
            with self.subTest(page=relative_path):
                source = (ROOT / relative_path).read_text(encoding="utf-8")
                section = re.search(
                    r"^## 確認問題[^\n]*\n(.*?)(?=^## |\Z)",
                    source, re.MULTILINE | re.DOTALL
                )
                self.assertIsNotNone(section, "Missing confirmation question")
                body = section.group(1)
                answer = re.search(r"\*\*正解[：:][^\n]+\*\*", body)
                self.assertIsNotNone(answer, "Missing answer")
                before_answer = body[:answer.start()]
                after_answer = body[answer.end():]
                self.assertRegex(before_answer, r'<details\s+markdown="1">[\s\S]*<summary>[^\n]+</summary>')
                self.assertIn("</details>", after_answer)
                self.assertNotRegex(before_answer, r'<details[^>]*\sopen(?:\s|=|>)')

if __name__ == "__main__":
    unittest.main()
