"""Exercise the audit against real local Git worktrees and fake forge CLIs."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'plugins/pstack-codex/skills/poteto-mode/scripts/worktree-audit.sh'

class WorktreeAudit(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='pstack-audit-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / 'repo'
        self.remote = self.root / 'origin.git'
        self.wt = self.root / 'worktree'
        self.command('git', 'init', '--bare', str(self.remote))
        self.command('git', 'init', '--initial-branch=main', str(self.repo))
        self.git('config', 'user.name', 'Audit Test')
        self.git('config', 'user.email', 'audit@example.com')
        (self.repo / 'file.txt').write_text('main\n')
        self.git('add', '.')
        self.git('commit', '-m', 'main')
        self.git('remote', 'add', 'origin', str(self.remote))
        self.git('push', 'origin', 'main')
        self.git('checkout', '-b', 'integration')
        (self.repo / 'integration.txt').write_text('integration\n')
        self.git('add', '.')
        self.git('commit', '-m', 'integration')
        self.git('push', 'origin', 'integration')
        self.git('checkout', 'main')
        self.git('worktree', 'add', '-b', 'candidate', str(self.wt), 'integration')
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        for name, body in {
            'gh': '#!/usr/bin/env bash\nprintf "%s" "${AUDIT_GH_JSON:-[]}"\n',
            'origin': '#!/usr/bin/env bash\n[ "${AUDIT_ORIGIN_ENABLED:-no}" = yes ] || exit 1\nprintf "%s" "${AUDIT_ORIGIN_JSON:-[]}"\n',
        }.items():
            p = self.bin / name
            p.write_text(body)
            p.chmod(0o755)
        self.env = dict(os.environ, PATH=f'{self.bin}:{os.environ["PATH"]}', CODEX_HOME=str(self.root / 'codex'))

    def command(self, *args, **kwargs):
        return subprocess.run(args, check=True, text=True, capture_output=True, **kwargs)

    def git(self, *args):
        return self.command('git', '-C', str(self.repo), *args)

    def audit(self, *args, expected=0):
        result = subprocess.run(['bash', str(SCRIPT), *args], text=True, capture_output=True, env=self.env)
        self.assertEqual(result.returncode, expected, result.stderr)
        return result

    def row(self, result):
        row = next(line for line in result.stdout.splitlines() if line.endswith(str(self.wt)))
        return dict(zip('SIZE AGE MERGED DIRTY REMOTE PR LAST_CHAT BUCKET WORKTREE'.split(), row.split('\t')))

    def test_base_controls_merge_classification_and_ref_fetch(self):
        main = self.row(self.audit('-b', 'origin/main', str(self.repo)))
        self.assertEqual(main['MERGED'], 'no')
        self.git('update-ref', '-d', 'refs/remotes/origin/integration')
        integration = self.row(self.audit('--base', 'origin/integration', str(self.repo)))
        self.assertEqual(integration['MERGED'], 'YES')
        self.git('rev-parse', '--verify', 'refs/remotes/origin/integration')
        self.git('symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/integration')
        result = self.audit(str(self.repo))
        self.assertIn('# base: origin/integration', result.stdout)
        self.git('symbolic-ref', '--delete', 'refs/remotes/origin/HEAD')
        self.assertIn('# base: origin/main', self.audit(str(self.repo)).stdout)
        self.git('update-ref', 'refs/remotes/origin/master', 'main')
        self.git('update-ref', '-d', 'refs/remotes/origin/main')
        result = self.audit(str(self.repo))
        self.assertIn('# base: origin/master', result.stdout)
        self.assertIn('could not fetch origin/master', result.stderr)
        self.assertTrue(self.wt.exists())

    def test_codex_transcripts_wip_and_both_forges_hold_work(self):
        self.env['AUDIT_GH_JSON'] = json.dumps([dict(number=4, state='OPEN', headRefName='candidate')])
        self.assertEqual(self.row(self.audit('-b', 'origin/integration', str(self.repo)))['BUCKET'], 'hold-open-pr')
        self.env['AUDIT_ORIGIN_ENABLED'] = 'yes'
        self.env['AUDIT_ORIGIN_JSON'] = json.dumps([dict(number=5, status='draft', headRef='candidate')])
        row = self.row(self.audit('-b', 'origin/integration', str(self.repo)))
        self.assertEqual(row['PR'], '#5/draft')
        self.assertEqual(row['BUCKET'], 'hold-open-pr')
        self.env['AUDIT_ORIGIN_JSON'] = '[]'
        archive = Path(self.env['CODEX_HOME']) / 'archived_sessions'
        archive.mkdir(parents=True)
        (archive / 'rollout.jsonl').write_text(json.dumps({'cwd': str(self.wt)})+'\n')
        self.assertEqual(self.row(self.audit('-b', 'origin/integration', str(self.repo)))['BUCKET'], 'verify-recent-chat')
        (self.wt / 'file.txt').write_text('uncommitted\n')
        self.assertEqual(self.row(self.audit('-b', 'origin/integration', str(self.repo)))['BUCKET'], 'hold-wip')
        self.assertEqual((self.wt / 'file.txt').read_text(), 'uncommitted\n')
        self.assertEqual(len(self.git('worktree', 'list', '--porcelain').stdout.split('worktree '))-1, 2)

    def test_usage_and_missing_inputs_fail(self):
        self.assertIn('--base', self.audit('--help').stdout)
        self.audit('-b', expected=2)
        self.audit('--unknown', expected=2)
        self.audit('-b', 'missing', str(self.repo), expected=1)
        self.audit(str(self.root), expected=1)
        self.git('update-ref', '-d', 'refs/remotes/origin/main')
        self.audit(str(self.repo), expected=1)

if __name__ == '__main__':
    unittest.main()
