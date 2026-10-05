"""Regression cases for broken routing links, not prose/agent-behavior assertions."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("instruction_check", Path(__file__).resolve().parents[1] / "scripts/check_agent_instructions.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ReferenceChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("AGENTS.md", "See `docs/agent/README.md`.\n")
        self.write("README.md", "Overview\n")
        self.write("docs/agent/README.md", "[Guide](source.md#freshness)\n")
        self.write("docs/agent/source.md", "# Freshness\n")

    def write(self, path, text):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding="utf-8")

    def test_valid_links_with_fragments_and_external_sources(self):
        self.write("docs/agent/source.md", "[External](https://example.org/absent.md)\n[Local](#freshness)\n")
        self.assertEqual(module.check(self.root), [])

    def test_missing_rule_reports_source_and_line(self):
        self.write("AGENTS.md", "Intro\nRead `docs/agent/missing.md`.\n")
        self.assertIn("AGENTS.md:2", "\n".join(module.check(self.root)))

    def test_case_mismatch_is_not_accepted(self):
        self.write("docs/agent/README.md", "[Guide](Source.md)\n")
        self.assertTrue(module.check(self.root))

    def test_relative_link_and_escaping_link(self):
        self.write("docs/agent/README.md", "[Guide](../../AGENTS.md)\n")
        self.assertEqual(module.check(self.root), [])
        self.write("docs/agent/README.md", "[Outside](../../../outside.md)\n")
        self.assertIn("escapes repository", "\n".join(module.check(self.root)))


if __name__ == "__main__":
    unittest.main()
