---
project: jarvis-code
updated: 2026-07-17T01:17:26+00:00
---
# JARVIS.md — jarvis-code

## NOW — Current Active Task
- Status: no active task yet.
- Last verified: not yet.
Next: wait for a concrete project request.

## MAP — Project Map and Symbol Index
- Keep only stable files, symbols, entry points, tests, and runtime commands.
- Prefer paths plus purpose; remove stale implementation trivia.

## LAW — Learned Agent Warnings
- Format: `LAW-001: Trigger -> Rule -> Verify`.
- Use for hard project invariants that must stay true on future edits.

## BAN — Forbidden Actions
- Format: `BAN-001: Never <action>; because <failure>; verify <check>`.
- Use for known-dangerous actions, not generic caution.

## HABIT — User and Project Preferences
- Format: `HABIT-001: When <situation>, prefer <style/workflow>`.
- Use for user/project preferences that affect future choices.

## WHY — Why History Yells (Decision Rationale)
- Record decision rationale only: `Decision -> Why -> Tradeoff`.
- Do not duplicate changelog, NOW, or RAW evidence.

## OMM — Oh My Mistake (Failure Retrospectives)
OMM entries are operational mistake-prevention rules, not apologies.
Use this exact shape:
### OMM-001: Short title
- Trigger: When this rule must be recalled.
- Mistake: What failed before, concretely.
- Rule: What must/never happen next time.
- Required action: What to inspect or change before proceeding.
- Verify: Command, test, log, or observable check.

## RAW — Raw Evidence Pointers
- Evidence pointers only: date, request, files changed, commands run, test result, turn id if known.
- Do not paste transcripts or long explanations here.

