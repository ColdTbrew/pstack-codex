---
name: setup-pstack
description: Configure the Codex custom agents used by pstack-codex. Use for setup-pstack, configuring pstack models, or changing pstack's builder, explorer, reviewer, and worker profiles.
---

# Set up pstack for Codex

Configure the `pstack_*`, `poteto_agent`, and `comment_sicko` profiles under
`~/.codex/agents/`. Each profile is a standalone Codex custom-agent TOML file.

## Workflow

1. Inspect the currently available Codex models and the existing files under
   `~/.codex/agents/`. Never invent a model slug.
2. Show the current role mapping and flag unavailable models.
3. Read [model routing](../poteto-mode/references/model-routing.md) for role defaults, reasoning settings, escalation, and mode composition. Keep model-named profiles on their named family. The root chat model is selected separately; updating `poteto_agent` does not switch it.
4. Update only the requested TOML files. Keep `name`, `description`, and
   `developer_instructions` intact unless the user asks to change behavior.
5. Validate every TOML file by parsing it and tell the user to start a new Codex task
   if the active task does not pick up the changed profiles.
