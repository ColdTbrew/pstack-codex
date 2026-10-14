### Opening a PR

Invoked at the end of every other playbook.

**Worktree.** Work in a git worktree off main; subagents inherit it. Multiple Codex subagent calls on one branch need separate worktrees or `git fetch && git reset --hard origin/<branch>` between calls. If unrelated work dirties the branch, patch it out and use a fresh worktree. If the worktree is snarled, reset from main and redo minimally.

**Commits.** Commit liberally, then rebase into small, ordered, landable commits before opening PRs. Each commit is a future PR and tells the story. Amend a fix into the latest commit when it belongs there; otherwise make a separate commit.

**PRs.** Before commit, run `$pstack-codex:unslop` from `Codex built-ins` over the diff and `$pstack-codex:no-comments` before review. Write every title, description, and commit body with `$pstack-codex:technical-writing`, applying every layer except Diátaxis, then apply `$pstack-codex:unslop`. Use one word per action, keep articles, and prefer a plain verb to `-ing` when it works.

**Titles.** Use `type(scope): subject` Conventional Commits. Choose `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, or `perf`; use the changed area as scope. Keep the subject short and imperative, name a real symbol when useful, and omit the period. Example: `fix(pstack): retarget opening-a-pr babysit trigger`.

**Descriptions.** Write a one-minute briefing for a reviewer with the diff: why the change exists, what it excludes, what could break, and how it was verified. Use short sentences and few identifiers. The body becomes the squash commit body, so keep it under about 40 lines. Use `##` headings in this order and omit empty sections:

- `## Why`: problem and approach in one to three short sentences; no SHAs, rebase history, or "based on main" preamble.
- `## What changed`: one to three bullets. Name symbols or paths only when they carry the change; name both sides of a rename or retarget.
- `## Scope`: always state coverage and deliberate exclusions in one to three short items. No paths, symbols, or file-by-file essay.
- `## Tradeoffs`: rejected alternatives a reviewer might ask about; omit if there was no real choice.
- `## Blast Radius`: one or two sentences on what changes and why it is safe or risky. If main is red, state the cost of leaving it red.
- `## Verification`: one to three bullets, each with the real run path and outcome. For performance, give one primary number with units as `before → after` and link the arena or swarm directory for other evidence.

Attach videos or screenshots that prove a claim. Put full SHAs, swarm or arena lane recitals, lever-correction essays, file checklists, and "CLEAN" verdicts in a linked artifact, not the body.

**Forge.** Resolve the forge before the first PR operation and use it consistently for create, edit, view, watch, and merge. Default to `gh`; prefer `origin pr ...` only when `command -v origin` succeeds and Origin resolves the repo. Otherwise stay on `gh` and record the fallback. Do not require `gt`.

**Built-in PR tool.** If the run provides one, create, edit, retarget, and mark ready through it, never a forge CLI. Use the resolved forge for operations it does not cover and for all PR operations when no built-in tool exists.

**Size and stacks.** The execution playbook decides who may rebase or retarget. In Autopilot-stack those operations belong only to the root; child owners must report the needed move instead. Prefer five narrow PRs to one large PR. A stack is a base-branch chain: the root targets trunk; each child rebases onto its parent's exact tip and targets that branch. As a parent merges, move its child onto trunk per `playbooks/shipping.md` step 4. Without a built-in PR tool, create a child with `origin pr create --status open --base <parent-branch>` or `gh pr create --base <parent-branch>`, and retarget it with the matching `origin pr edit <pr> --base <parent-branch>` or `gh pr edit <pr> --base <parent-branch>`. Branch from trunk only for independent work. Rebase on trunk before substantial stack work.

**Readiness.** Open every PR ready, never as a draft. For a built-in tool, set `draft: false`; with Origin pass `--status open`; with `gh` omit `--draft`. If it still opens as draft, mark it ready through the PR tool or `origin pr ready <number>` or `gh pr ready <number>`, according to the resolved forge. Run `origin pr view <number>` or `gh pr view <number>` before stating PR status.

**Babysit.** Opening a PR does not start a babysit. Post its URL and keep building until the phase or stack is done. Run a separate babysit only when the user asks after the whole stack exists; a pass for every PR stalls work and repeats checks on commits later waves restart. Push back when feedback drifts from intent.

A subagent that opens a PR runs `interrogate`, `$pstack-codex:unslop`, and `$pstack-codex:no-comments`, then posts the URL and returns to the parent without babysitting. Exception: an Autopilot-full or Autopilot-stack owner whose brief assigns the babysit loop and satisfies the ask in `playbooks/babysit.md`. That owner starts after its code-ready report and reports merge-ready or STACK-READY as its playbook says. The normal hold-until-the-stack-exists rules here and in `playbooks/babysit.md` do not apply to that owner.
