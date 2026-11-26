---
name: olympus-tasks
description: Turn a conversation or brief into numbered, prioritized tasks with concrete outcomes and dependencies. Use to organize agreed work or revise an existing task list without executing it.
metadata:
  version: "1.0.0"
---

# Turn a conversation into tasks

Return the plan in the user's language. Use the current request and the relevant conversation, or the brief the user identifies. Draft the tasks in the conversation; do not execute them, write files, or create issues.

1. **Capture what was agreed.** Use the latest decisions, remove duplicates, and keep scope and constraints. Separate remaining work from completed work, deferred items, and unapproved ideas. If an open decision affects only part of the plan, mark that part blocked and still list the work that can proceed.
2. **Write actionable tasks.** Give each task a number, a short action title, and a concrete “done when” condition. Split work when the parts can be verified separately or have different prerequisites. Keep related steps together when splitting them would just add noise.
3. **Set priorities and order.** Honor stated priorities. Otherwise suggest High, Medium, or Low based on impact, urgency, and what the task unblocks. Present tasks in a feasible execution order: prerequisites before dependent work, and higher priority first among comparable tasks that can start. Priority and execution order are separate.
4. **Show only real dependencies.** Add “Depends on” with task numbers only if that work cannot proceed without the listed tasks. Mark external blockers separately, with what is needed to clear them. Mention independent tasks that can run in parallel when useful. If dependencies appear circular, clarify or split the work rather than presenting an impossible order.
5. **Revise the list when the user adds information.** Keep the numbers of tasks that remain the same, give new tasks unused numbers, and update the order and dependency references. Keep completed or deferred tasks in a short note when they explain a change or dependency.

Lead with a one-line outcome, then return a compact list with the task number in each label. Use explicit labels so Markdown does not renumber tasks when their order changes. For example:

- **Task 1 · High — Add the validator.** Done when it accepts valid inputs and rejects an invalid one.
- **Task 2 · High — Add the validator to CI.** Depends on task 1. Done when the check runs on a pull request.
- **Task 3 · Medium — Update the contributor guide.** Done when it shows how to run the validator locally.

Tasks 1 and 3 can proceed in parallel.
