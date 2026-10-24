import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";
import assert from "node:assert/strict";
import { test } from "node:test";

const checker = process.env.CHECK_PLAN_CHECKER ?? join(import.meta.dirname, "check-plan.mjs");
const rule =
	"Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.";

const validPlan = `# Demo

## How to read this
One box is one unit of work and names the evidence. Check a box only when its evidence exists. See playbooks/.
${rule}

## Program checklist
### Arm the program
### Spawn owners
### PR mechanics
### Verdict and merge
### Boot recipe
\`git show origin/main:\` audit cadence report only changed state

## PR 1
**Depends on.** None.
**Files.**
- [ ] Do the thing.
**Build.**
- [ ] Do the thing.
**You see.**
- [ ] Do the thing.
**Verify, unit.** ${rule}
- [ ] Check the thing.
**Verify, live.** ${rule} Declare the smallest set of materially distinct scenarios and run up to three lanes concurrently at the PR head
${Array.from({ length: 3 }, (_, i) => `- [ ] Lane ${i + 1}. Save \`lane-${i + 1}.png\`. Pass when evidence exists.`).join("\n")}
**Verify, perf.** ${rule}
- [ ] Metric. Recorded.
- [ ] Probe. Recorded.
- [ ] Baseline. Recorded.
- [ ] Rule. Recorded.
**Review gate.** None.
**Merge.**
- [ ] Merge when approved.

## Close the program
Close.

## Appendix Prototype evidence
Recorded.
`;

const runPlan = (example, expectedExit, plan = validPlan) => {
	const directory = mkdtempSync(join(tmpdir(), "check-plan-test-"));
	const file = join(directory, "plan.md");
	writeFileSync(file, plan + example);
	try {
		const result = spawnSync("node", [checker, file], { encoding: "utf8" });
		assert.equal(result.status, expectedExit, result.stderr);
		return result;
	} finally {
		rmSync(directory, { recursive: true, force: true });
	}
};

test("accepts ordinary, indented, and longer closing fences", () => {
	for (const indent of ["", " ", "  ", "   "])
		runPlan(`${indent}\`\`\`markdown\n## Example only\n${indent}\`\`\`\n`, 0);
	runPlan("```markdown\n## Example only\n````\n", 0);
});

test("accepts nested backticks and tilde info strings", () => {
	runPlan("````markdown\n```markdown\n## Example only\n```\n````\n", 0);
	runPlan("~~~markdown `info`\n## Example only\n ~~~\n", 0);
});

test("keeps mismatched, shorter, and suffixed closers inside the fence", () => {
	runPlan("````markdown\n~~~\n## Example only\n````\n", 0);
	runPlan("````markdown\n```\n## Example only\n````\n", 0);
	runPlan("````markdown\n``` info\n## Example only\n````\n", 0);
});

test("rejects headings and prose outside a proper close", () => {
	for (const suffix of ["  ", "\t"]) {
		const heading = runPlan(`\`\`\`markdown\n## Example only\n\`\`\`${suffix}\n## Example only\n`, 1);
		assert.ok(heading.stderr.includes('"## Example only" after Close the program is not an appendix'), heading.stderr);
	}

	const prose = runPlan("```markdown\nThis prose has a mid-sentence colon: inside code\n```\nThis prose has a mid-sentence colon: bad.\n", 1);
	assert.ok(prose.stderr.includes("mid-sentence colon"), prose.stderr);
});

test("rejects backtick info strings containing a backtick", () => {
	const result = runPlan("```markdown `invalid`\n## Example only\n```\n", 1);
	assert.ok(result.stderr.includes('"## Example only" after Close the program is not an appendix'), result.stderr);
});

test("accepts Codex plans with one, two, and three consecutive lanes", () => {
	for (const count of [1, 2, 3]) {
		const plan = validPlan.replace(/^- \[ \] Lane \d+\..*\n/gm, (line) =>
			Number(line.match(/Lane (\d+)/)[1]) <= count ? line : "",
		);
		runPlan("", 0, plan);
	}
});

test("retains Codex concurrency and monitoring requirements", () => {
	const cursorPlan = validPlan
		.replace("Declare the smallest set of materially distinct scenarios and run up to three lanes concurrently at the PR head", "Ten lanes on `example-model` at the PR head")
		.replace("audit cadence report only changed state", "/loop 1h status message");
	const result = runPlan("", 1, cursorPlan);
	assert.ok(result.stderr.includes("Codex concurrency rule"), result.stderr);
	assert.ok(result.stderr.includes('lacks "audit cadence"'), result.stderr);
	assert.ok(result.stderr.includes('lacks "report only changed state"'), result.stderr);
});

test("retains lane numbering, screenshots, pass predicates, and verification rule", () => {
	for (const [from, to, message] of [
		["Lane 2.", "Lane 4.", "expected consecutive lanes starting at 1"],
		["Save `lane-1.png`", "Record evidence", "names no screenshot"],
		["Pass when evidence exists.", "Evidence exists.", "has no pass predicate"],
		[`**Verify, unit.** ${rule}`, "**Verify, unit.** Tests only.", "does not open with the rule"],
		["- [ ] Baseline. Recorded.", "", "perf boxes are"],
	]) {
		const result = runPlan("", 1, validPlan.replace(from, to));
		assert.ok(result.stderr.includes(message), result.stderr);
	}
});

test("fenced headings and checkboxes cannot satisfy missing plan structure", () => {
	const plan = validPlan.replace("**Files.**\n- [ ] Do the thing.",
		"**Files.**\n~~~markdown\n- [ ] Fake evidence.\n## Fake PR\n~~~");
	const result = runPlan("", 1, plan);
	assert.ok(result.stderr.includes("Files. has no box"), result.stderr);
	assert.ok(result.stdout.includes("1 PR sections"), result.stdout);
});

test("prose diagnostics resume at their original line after a tilde close", () => {
	const appendix = "~~~text\n## Fake section\ncolon: inside — ‘code’\n~~~\ncolon: outside — ‘prose’\n";
	const result = runPlan(appendix, 1);
	const line = validPlan.split("\n").length + 4;
	for (const diagnostic of ["mid-sentence colon", "long dash", "curly quote"])
		assert.ok(result.stderr.includes(`plan.md:${line}: ${diagnostic}`), result.stderr);
});

test("ignores fenced examples through EOF and rejects four-space fence openers", () => {
	runPlan("~~~markdown\n## Example only\ncolon: code\n", 0);
	const result = runPlan("    ```markdown\n## Example only\n", 1);
	assert.ok(result.stderr.includes('"## Example only" after Close the program'), result.stderr);
});

test("keeps a four-space or suffixed closing fence inside code", () => {
	for (const closer of ["    ```", "``` info", "~~~", "``"])
		runPlan(`\`\`\`markdown\n${closer}\n## Example only\n\`\`\`\n`, 0);
});

test("ignores prose punctuation inside matching multi-backtick code spans", () => {
	for (const count of [2, 3, 4]) {
		const delimiter = "`".repeat(count);
		runPlan(`Use ${delimiter}echo \`x\`: “quoted” — example${delimiter}.\n`, 0);
	}
});

test("checks prose following a multi-backtick span and unmatched delimiters", () => {
	const outside = runPlan("Use ``echo `x`: y``. Bad: prose.\n", 1);
	assert.ok(outside.stderr.includes("mid-sentence colon"), outside.stderr);
	const unmatched = runPlan("Use ``unclosed: bad` here.\n", 1);
	assert.ok(unmatched.stderr.includes("mid-sentence colon"), unmatched.stderr);
});
