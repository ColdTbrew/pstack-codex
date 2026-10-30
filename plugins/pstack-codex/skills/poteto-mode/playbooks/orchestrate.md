### Orchestrate

**You run the program, never the code. Decide which agent owns each unit, then check what it produces.** Use this for a standing project spanning many PRs and sessions. One task driven to a predicate is Autonomous run; one ambitious bespoke run is figure-it-out. Work one agent can finish within the session budget is not a program.

Use Codex subagent and task tools directly. Keep the goal, standing orders, unit ownership, PRs, current head SHAs, verification receipts, and open gates in a shared `.audit/orchestrate/<project>/` store and the Codex plan. Prefer task waits or PR and CI event subscriptions when available. Do not add a script-driven control plane, a second polling loop, or status relays between agents. The retained `scripts/orch/` utilities are optional offline bookkeeping compatibility, not the agent runtime.

#### Topology

- **One owner per PR.** The owner is the only branch writer from build through the authorized merge or operator handoff. Only that owner pushes, rebases, or retargets. Closing or retargeting a base PR requires the root's topology decision because it can orphan children. The coordinator never edits code; conflicts and fixes go to owners.
- **A fresh agent for each independent unit.** Each brief gives the goal, exclusive worktree or branch, allowed and forbidden paths, acceptance evidence and exact commands, prohibited actions, and every upstream report the unit needs. Workers cannot infer sibling context. Preserve costly live state only under Poteto Mode's documented reuse exception; stop and hold orders are not reuse.
- **Use the installed roles.** Read [model routing](../references/model-routing.md). Keep the current root model, Sol/medium track coordinators, shipped builder and reviewer models, reasoning settings, and service tiers. A PR's independent verifier must not have authored the artifact. Use the configured ordinary or high-risk reviewer set rather than importing Cursor model families.
- **Add a sub-coordinator only for an area with many workers.** Use nested agents only when supported. Keep depth to root, track, worker, and count every descendant against the actual Codex session limit. Refill available slots as workers finish. Track coordinators send one rollup; they do not forward raw status streams.
- **Start with one unit.** Take it through brief, owner, independent verification, and authorized delivery before fan-out, so a bad brief costs one unit.

#### Supervision

- Read each diff or artifact as well as the report. Behavioral work needs more than a typecheck. CI green is an input, and a verdict covers one current head SHA. Record new heads and renewed verification instead of trusting stale receipts.
- Sample track coordinators' briefs while their workers run. Fix the instructions when a brief fails, and send back work that drifts from the goal. Keep only fixes that block the program; park the rest as follow-ups.
- Check live PR state and checks through `gh pr view` and `gh pr checks`, or the already resolved forge, before reporting. Account for every spawned agent as done, replaced, or absorbed.
- Judge liveness by pushed commits and PR activity. Read status without waking idle agents. Retry with smaller scope after a context or memory limit, the same consolidated brief after a dropped connection, and an available configured role after a tool failure. After two retries, drop the unit and replan. Reconcile late returns against the current PR head; give unique findings to a fresh owner.
- Ask only for irreversible actions, a product or preference decision no experiment settles, or a dead end surviving a replan. Preserve every operator gate, merge authorization, and pinned force-with-lease. Routine rebases, CI flakes, review triage, and continuation stay with the owners. Stop all writers on the operator's hold.
- Do not create active goals or scheduled automations without the user's request. On restart, reload durable state, check branches and live PRs, and assign fresh owners with consolidated briefs before resuming.

**Reply:** what landed against the goal, each PR's live state and verdict with its link, what was dropped and why, and decisions waiting on the user. Stay quiet when nothing actionable changed.
