---
name: olympus-goal-writer
description: Turn a prompt, issue, investigation, or agreed plan into a copy-ready OpenCode /goal of at most 4,000 characters. Use when asked to write, revise, or shorten a goal without starting it.
metadata:
  version: "1.0.0"
---

# Write an OpenCode goal

Draft the goal in the user's language. Do not run `/goal`, change an active goal, or start the work described in the draft.

1. Use the explicit request first, then any issue, artifact, or agreement it refers to. If the user says “turn this into a goal,” use the relevant conversation. Check existing project evidence when it can resolve uncertainty. Ask only if a decision critical to the outcome or scope cannot be resolved from available evidence.
2. Write the outcome as a verifiable end state. Include what the running agent must deliver, the evidence it must show, and the scope and constraints that must hold. Preserve approval gates and existing authorization boundaries. Never invent a test command, metric, file, or permission. Refer to a known source instead of repeating long background details.
3. Give the running agent a continuation rule in the objective itself. Use these semantics in the user's language:

   - Keep working until the outcome is verified. A plan, a progress update, or completion of one step is not a reason to stop.
   - When a step is blocked, record what is blocked and why, try other viable in-scope approaches, and continue any independent in-scope tasks or verification. Revisit deferred work when its blocker clears. Do not repeat a failed attempt without new evidence.
   - Pause for a blocker only when the remaining work genuinely requires human action, permission, information, or a decision and no useful in-scope work can still advance. Report what was finished, what remains, and the exact human action needed. Do not bypass a gate or claim a blocked outcome is complete.

4. Format one plain-text line starting with `/goal ` and a nonempty objective. Do not use `pause`, `resume`, or `clear` as the entire objective. The **complete line** may contain at most **4,000 UTF-16 code units**, including `/goal `, so the objective budget is 3,994. Measure the exact final line with JavaScript string `.length` or an equivalent UTF-16 counter, passing the text as data rather than evaluating it or interpolating it into shell code. Count the text inside the block, not the Markdown fence or its line breaks. If too long, condense and measure again; never truncate constraints, evidence requirements, or the continuation rule. If it cannot fit without losing requirements, propose separating genuinely independent outcomes or referencing an existing artifact. Do not call an unmeasured or over-limit draft copy-ready.
5. Return the validated line in a single `text` code block for the user to paste. Do not execute it.
