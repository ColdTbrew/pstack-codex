### Autopilot-stack

Run the Autopilot-full playbook, but do not merge or arm auto-merge. The operator owns landing. Read both playbooks from the installed absolute plugin paths supplied by the root, and let this one win where they differ.

1. **In place of step 5, stop at verified.** Stop when each PR is independently verified and green at its current head, then hand the PRs to the operator. After handoff, nobody pushes without the operator's go. Every audit or wait prompt names this file so the no-merge rule survives. Do not create an active goal or scheduled automation unless requested.
2. **Stack a PR only when it builds on another PR.** Independent PRs branch from trunk. A dependent PR targets its parent's branch per **Size and stacks** in `playbooks/opening-a-pr.md`. Its owner rebases onto that parent's branch instead of trunk; the stack root rebases onto trunk. Only the owner writes, rebases, or retargets its branch, on the root's topology decision. A lower PR's new head requires its child owners to restack in dependency order. Apply Shipping's patch-id rule per link, then check CI at every new head. Preserve pinned force-with-lease and operator gates.

**Reply:** list each PR with its live state and verdict, dependency order where applicable, and parked follow-ups, with links. The operator lands the verified PRs.
