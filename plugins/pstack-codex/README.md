# pstack for Codex

This is a Codex-native port of
[`cursor/plugins/pstack`](https://github.com/cursor/plugins/tree/main/pstack).
It preserves pstack's engineering principles and playbooks while replacing
Cursor-specific model rules, agent calls, skill locations, and loop mechanics.

## Use it

Start a new Codex task after installation, then invoke:

```text
$pstack-codex:poteto-mode investigate this bug, reproduce it, fix the root cause, and verify it.
```

Useful direct workflows include `$pstack-codex:how`, `$pstack-codex:why`,
`$pstack-codex:arena`, `$pstack-codex:swarm`,
`$pstack-codex:interrogate`, `$pstack-codex:tdd`,
`$pstack-codex:unslop`, and `$pstack-codex:technical-writing`.

Use `$pstack-codex:ketchup` for a read-only catch-up on this chat since your
last message, including pending decisions. Use `$pstack-codex:recall` to
rebuild context on a topic across chats. All 54 skills are explicit-only.

Use `$pstack-codex:in-your-own-words` to restate the goal before work, and `$pstack-codex:sharpen` to improve the approach and then execute it.

The chat receiving `$pstack-codex:poteto-mode` owns the playbook and task plan. `poteto_agent` handles delegated slices; do not launch it as the playbook runner.

Run `$pstack-codex:setup-pstack` to review or change the custom-agent model
mapping. The companion agent installation includes the `poteto_agent`, `comment_sicko`,
`pstack_builder_*`, `pstack_reviewer_*`, `pstack_explorer`, and
`pstack_worker` profiles under `~/.codex/agents/`.

The 10 profiles use `gpt-6-astra`, `gpt-6.1-sol`, and `gpt-6-luna`.
See [model routing](skills/poteto-mode/references/model-routing.md) for each
role's model and reasoning effort. The agent installer removes retired Terra
builder and reviewer profiles when updating an existing installation.

## Port boundary

The Cursor-only Grok Bot webhook and Benny automation sources are retained
under `upstream-cursor-only/` for provenance but are not registered in Codex.
See `CODEX_PORT.md` for the runtime mapping.

The public source, installation instructions, and upstream update workflow are
maintained at <https://github.com/ColdTbrew/pstack-codex>.

Original pstack is by Lauren Tan and distributed under the MIT license.

Use `$pstack-codex:create-formal-verification-skill` to verify a property that tests rarely reach and leave a project-local recheck workflow. Each result states its bounds and assumptions.
