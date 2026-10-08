---
name: poteto-help
description: Guides users through pstack-codex setup, $pstack-codex:poteto-mode, and choosing a skill, playbook, or principle. Use for $pstack-codex:poteto-help or an explicit pstack help question.
---

# Poteto help

Answer the user's question about pstack, give them a prompt they can send, and link the source of the answer. A help question does not authorize starting the work. A message asking for work, such as "use pstack to fix this bug", does: read [poteto-mode](../poteto-mode/SKILL.md) and follow its workflow within the user's scope.

Read the file you route to before quoting it. The files own the details and take precedence over this map. For public links, use `https://github.com/ColdTbrew/pstack-codex/blob/main/plugins/pstack-codex/` followed by the file's path relative to the plugin root. Installation instructions live in the [repository README](https://github.com/ColdTbrew/pstack-codex#install).

## Find out what they need

Infer the need from the message and conversation. A named situation goes straight to its section. If it is still unclear, ask one question with these choices, then answer the selected section:

- Get set up
- Start a task with `$pstack-codex:poteto-mode`
- Pick a skill for a situation
- Fix a run that went wrong
- Make pstack my own

Check state only when it changes the answer:

- Inspect the relevant `~/.codex/agents/*.toml` files. An existing directory does not prove pstack's profiles are installed. Missing profiles need the companion installation from the repository README; distinguish shipped defaults from installed overrides.
- If the project has no `verify-*` skill or app harness, mention [create-verification-skill](../create-verification-skill/SKILL.md) when the question is about proving an app change works. Respect the project's test-file creation policy.
- When setup or cost depends on model choice, offer [setup-pstack](../setup-pstack/SKILL.md) once. It inspects real models and changes only requested profiles. Do not invent a model or modify profiles during a help question.

## Get set up

Use the repository README's installation commands and inspect configured marketplaces before recommending an update. The standard public marketplace is `pstack-codex`; an existing local installation may use a different name such as `personal`.

1. Install the Codex plugin and companion custom-agent profiles as described in the README.
2. Invoke `$pstack-codex:setup-pstack` if the user wants to change the role mapping. It updates TOML profiles, not the root chat model.
3. Start a new Codex task after installation or profile changes, then invoke `$pstack-codex:poteto-mode` with a goal and a check that can pass or fail.

All registered pstack-codex skills require explicit invocation through `$pstack-codex:<skill-name>`. Installing the plugin alone does not activate its workflows. Do not promise Cursor Custom Modes, keyboard shortcuts, or slash commands in Codex.

For cost questions, explain where tokens go: candidate agents, review panels, and retries. Smaller scopes and fewer meaningful candidates can reduce use; role choices and reasoning settings follow [model routing](../poteto-mode/references/model-routing.md). Preserve explicitly selected models and verify supported reasoning levels before changing them. Profiles do not switch the root chat model.

The Codex port uses Codex subagents, shared workspaces or isolated worktrees, and wait/monitor tools. Raw Cursor guides and Grok Bot/Benny sources under `upstream-cursor-only/` are provenance, not executable Codex instructions.

## Start a task with `$pstack-codex:poteto-mode`

`$pstack-codex:poteto-mode` matches the task to a playbook and runs the needed skills. A good prompt states the goal and the done check. Read [prompting](references/prompting.md) before helping word one. For a new task, invoke the skill explicitly and say "new task" when the subject changes. Preserve corrections and ongoing work when the user is steering the active task.

Pstack's model routing and companion TOML profiles define the subagent roles. Use available Codex subagent tools and keep launches within the active session limit. Subagents share files unless assigned separate worktrees; they do not each receive a separate machine.

## Pick a skill

The usual entry point for a requested non-trivial task is `$pstack-codex:poteto-mode`. Name another skill directly when the user wants a specific workflow. Read it before recommending it, and give one example prompt.

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | [`$pstack-codex:poteto-mode`](../poteto-mode/SKILL.md) |
| Know how code works now, or where new code should live | [`$pstack-codex:how`](../how/SKILL.md) |
| Know why code is shaped this way, or where a number came from | [`$pstack-codex:why`](../why/SKILL.md) |
| Understand a change or subsystem, explained plainly | [`$pstack-codex:teach`](../teach/SKILL.md) |
| Catch up on their own recent work on a topic | [`$pstack-codex:recall`](../recall/SKILL.md) |
| Know what a small diff could break outside itself | [`$pstack-codex:blast-radius`](../blast-radius/SKILL.md) |
| Settle types and module shape before code that crosses a function boundary | [`$pstack-codex:architect`](../architect/SKILL.md) |
| Get several attempts at one brief, merged into the best one | [`$pstack-codex:arena`](../arena/SKILL.md) |
| Run parallel checks over slices, or race workers, as Codex subagents | [`$pstack-codex:swarm`](../swarm/SKILL.md) |
| Have different models review a diff and try to break it | [`$pstack-codex:interrogate`](../interrogate/SKILL.md) |
| Fix a bug test-first when a cheap local test exists | [`$pstack-codex:tdd`](../tdd/SKILL.md) |
| Apply TypeScript rules to `.ts` or `.tsx` work | [`$pstack-codex:typescript-best-practices`](../typescript-best-practices/SKILL.md) |
| Strip comments before review, using a reviewer that didn't write them | [`$pstack-codex:no-comments`](../no-comments/SKILL.md) |
| Review prose for AI tells | [`$pstack-codex:unslop`](../unslop/SKILL.md) |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | [`$pstack-codex:technical-writing`](../technical-writing/SKILL.md) |
| Hear the last reply again in plain words | [`$pstack-codex:bro`](../bro/SKILL.md) |
| Give agents a scripted way to drive the app and prove behavior | [`$pstack-codex:create-verification-skill`](../create-verification-skill/SKILL.md) |
| Bring a verification skill and its feature map back in line with the app | [`$pstack-codex:maintain-verification-skill`](../maintain-verification-skill/SKILL.md) |
| Vet a performance number before reporting or acting on it | [`$pstack-codex:benchmark-checklist`](../benchmark-checklist/SKILL.md) |
| Run a large or cross-cutting change, or one to review after stepping away | [`$pstack-codex:figure-it-out`](../figure-it-out/SKILL.md) |
| Keep a decision log during a run, and review it afterward | [`$pstack-codex:show-me-your-work`](../show-me-your-work/SKILL.md) |
| Pick a model for each role and a reasoning budget | [`$pstack-codex:setup-pstack`](../setup-pstack/SKILL.md) |
| Turn their own working habits into a personal mode skill | [`$pstack-codex:automate-me`](../automate-me/SKILL.md) |
| Turn what a finished task taught into skill edits | [`$pstack-codex:reflect`](../reflect/SKILL.md) |
| Stop agents from repeating the same mistakes in this repo | [`$pstack-codex:correct`](../correct/SKILL.md) |
| Find their way around pstack | `$pstack-codex:poteto-help` |


If a skill next to this one is missing from the table, read its frontmatter and route by its description. The `principle-*` directories are covered below.

Close calls:

- `how` explains mechanics, `why` explains reasons, and `teach` builds a plain explanation from one or both.
- `arena` gives candidates the same brief and synthesizes their results; `swarm` divides work into slices or a race.
- `architect` implements after settling the design. Add "with checkpoint" to review the design first.
- `interrogate` reviews a diff; `blast-radius` investigates effects outside it and proves the load-bearing safety claim.
- `recall` rebuilds context across chats. Resuming one particular branch uses Session pickup.

The port ships `unslop`. Browser and terminal automation depend on the tools available in the active Codex session. Grok Bot's make-bot-ui remains Cursor-only. There is no pstack `orchestrate` skill; Orchestrate is a poteto-mode playbook.

## Playbooks and principles

Playbooks are step lists inside [poteto-mode](../poteto-mode/SKILL.md), not separate skill commands. Read its Playbooks section for the complete mapping:

- "check on pr 123" or "babysit this pr": Babysit. Stop at merge-ready unless merging is authorized.
- "land the stack": Shipping.
- "take over this branch": Session pickup.
- "pause safely": Pause safely.
- "full autopilot on this queue": Autopilot-full. "stack them, don't ship": Autopilot-stack.
- "run the eval playbook": Eval.

For a plan spanning phases or stacked PRs, use [Multi-phase plan](../poteto-mode/playbooks/multi-phase-plan.md). For unresolved design choices, Prototype or `architect` gathers evidence before planning.

Principles are focused skills read when relevant. Invoke one as `$pstack-codex:principle-<name>` or name it while steering an active pstack run.

## Fix a run that went wrong

| Symptom | Fix |
|---|---|
| A new task didn't use pstack | Invoke `$pstack-codex:poteto-mode` explicitly for the task. |
| A question became the next step of the last task | State that it is a help question or a new task. |
| Profile changes had no effect | Verify the installed TOML and start a new Codex task. The root model is selected separately. |
| Runs cost more than expected | Check scope, candidate count, and role settings under Get set up. |
| A skill didn't load automatically | All pstack-codex skills are explicit-only. Invoke the named skill. |
| Agents overwrote each other's files | Assign separate worktrees or non-overlapping file ownership; Codex agents share the workspace. |
| An overnight run finished nothing | Give it observable completion checks and a stop condition. Read the Autonomous run playbook. |
| Success was claimed from a green build alone | Ask for the real command, app flow, stored value, or profile. |

For short steers, read [prompting](references/prompting.md).

## Make pstack my own

- [automate-me](../automate-me/SKILL.md) drafts a personal skill from the user's history.
- [reflect](../reflect/SKILL.md) turns a completed session's lessons into proposed skill edits.
- A skill-authoring task follows Codex's `$skill-creator`; a requested evaluation can use the Eval playbook.
- A broken skill discovered during feature work gets a separate scoped fix rather than expanding the feature change.

## Reply

Lead with the answer. Give at most one example prompt, adapted from [recipes](references/recipes.md), then a link to the supporting file. Keep it short unless the user asked for the whole map.
