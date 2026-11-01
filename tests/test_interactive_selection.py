"""CI selection must cover shared changes without claiming unrelated article coverage."""
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('selection', Path(__file__).resolve().parents[1] / 'scripts/select_interactive_checks.py')
selection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(selection)
REGISTRY = {'lock': {'source': 'pages/fe/shared-exclusive-lock.md'},
            'commit': {'source': 'pages/fe/two-phase-commit.md'}}


class SelectionTests(unittest.TestCase):
    def test_article_changes_only_select_registered_page(self):
        self.assertEqual(selection.select(['pages/fe/shared-exclusive-lock.md'], REGISTRY)['pages'], ['lock'])

    def test_shared_changes_select_all_consumers(self):
        for path in ['assets/css/study-demo.css', '_layouts/page.html', '_includes/study_demo_assets.html',
                     '_config.yml', 'tests/browser/pilot.json', 'scripts/check_interactive_demos.py']:
            with self.subTest(path=path):
                self.assertEqual(selection.select([path], REGISTRY)['pages'], list(REGISTRY))

    def test_unregistered_articles_are_explicitly_uncovered(self):
        self.assertEqual(selection.select(['pages/gk/example.md'], REGISTRY),
                         {'pages': [], 'uncovered_articles': ['pages/gk/example.md']})

    def test_documentation_alone_does_not_build_site(self):
        self.assertEqual(selection.select(['docs/agent/interactive-learning-rules.md'], REGISTRY)['pages'], [])
