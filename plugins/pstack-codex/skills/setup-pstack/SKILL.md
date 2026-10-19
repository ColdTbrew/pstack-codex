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
   If the user asks for a reasoning budget, offer `unlimited` (max), `large`
   (xhigh), `medium` (high), or `small` (medium). An explicitly chosen preset
   sets the target effort for each requested profile; `unlimited` targets max
   rather than leaving existing efforts unchanged. Check the model's supported
   efforts and use the highest supported effort at or below the target, or
   flag the profile for a choice when none fits. Keep model IDs and families
   intact; reasoning is a separate TOML field. Without a budget request, retain
   each profile's existing or shipped effort instead of imposing a preset.
4. Update only the requested TOML files. Keep `name`, `description`, and
   `developer_instructions` intact unless the user asks to change behavior.
5. Validate every TOML file by parsing it and tell the user to start a new Codex task
   if the active task does not pick up the changed profiles.

## Optional project verification

After setup, check whether the project has an app harness or a `verify-*` skill. If it has neither, offer once to generate one with `$pstack-codex:create-verification-skill`. Run it only if the user accepts.

If the project has no formal verification skill, offer once to generate one with `$pstack-codex:create-formal-verification-skill` for a property that tests rarely reach. Explain that a proof covers its stated model, bounds, and assumptions. Run it only if the user accepts; move on after a decline. Respect the project's test-file creation policy.
