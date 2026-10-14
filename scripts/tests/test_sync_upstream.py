"""Ensure staging keeps Codex-owned behavior across future upstream updates."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts import sync_upstream as sync

class SyncCandidate(unittest.TestCase):
    def test_future_stage_preserves_codex_tests_and_provenance_boundary(self):
        # Use the tracked provenance plus the port as a self-contained source tree.
        plugin = ROOT / 'plugins/pstack-codex'
        with tempfile.TemporaryDirectory(prefix='pstack-sync-') as directory:
            source = Path(directory) / 'source'
            source.mkdir()
            (source / 'skills/poteto-mode/scripts').mkdir(parents=True)
            (source / 'skills/poteto-mode/SKILL.md').write_text('---\nname: Poteto Mode\ndescription: Upstream workflow\n---\n')
            (source / 'skills/poteto-mode/scripts/check-plan.mjs').write_text('throw new Error("Cursor only");\n')
            cursor_test = 'throw new Error("Ten lanes and /loop fixture");\n'
            (source / 'skills/poteto-mode/scripts/check-plan.test.ts').write_text(cursor_test)
            (source / 'skills/poteto-mode/scripts/package.json').write_text('{"scripts":{"test":"bun test check-plan.test.ts"}}')
            (source / 'plugin.json').write_text('{"name":"pstack","version":"9.0.0"}')
            candidate = Path(directory) / 'candidate'
            sync.build_candidate(source, candidate, '9.0.0', True)
            for relative in ('skills/poteto-mode/scripts/check-plan.mjs', 'skills/poteto-mode/scripts/check-plan.test.mjs', 'skills/poteto-mode/scripts/package.json', 'codex-agents/pstack_builder_luna.toml'):
                self.assertEqual((candidate / relative).read_bytes(), (plugin / relative).read_bytes())
            self.assertFalse((candidate / 'plugin.json').exists())
            self.assertFalse((candidate / 'skills/poteto-mode/scripts/check-plan.test.ts').exists())
            self.assertEqual((candidate / 'upstream-cursor-only/check-plan.test.ts').read_text(), cursor_test)
            self.assertTrue((candidate / 'upstream-cursor-only/plugin.json').is_file())
            sync.validate_plugin(candidate)

    def test_upstream_test_manifest_and_test_command_require_review(self):
        for path in ('plugin.json', 'skills/poteto-mode/scripts/check-plan.test.ts', 'skills/poteto-mode/scripts/package.json'):
            self.assertTrue(sync.needs_manual_merge(path), path)

if __name__ == '__main__':
    unittest.main()
