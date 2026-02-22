# Episode Factory — Writer Instructions

You are writing episodes for the Tesla Mandela Effects audio series. Each episode is standalone, 10,000-13,000 words, formatted for ElevenLabs Eleven Turbo v2 TTS.

## Read These Files (in this order)

1. **PRODUCTION_GUIDE.md** — The five laws, the voice, the rules. This governs every word.
2. **The Process- How to Rewrite Term Violations.txt** — The worked examples of how to replace lazy language with meaning. The Production Guide has the 6 principles; this file shows HOW to apply them. Study both examples completely before writing.
3. **SERIES_BIBLE.md** — Anti-cloning registry. Check the menus, check the last 3 episode entries, pick different choices for opening/structure/closing/emotional endpoint. Check key images from recent episodes and DO NOT reuse them.
4. **VOICE_REFERENCE.txt** — Episode 002, the style exemplar. Study it for descriptive variety and micro-story structure. Do not clone its content or structure.
5. **TERM_VIOLATIONS_DEFINITION.md** — What IS and ISN'T a term violation. Three categories: violations (apply The Process), not violations (leave alone), earned ambiguity (judgment call). Depends on understanding The Process first.
6. **EPISODES/** — Completed episodes live here. Read the BRIEF for context. Read the SCRIPT only if you need to verify what images or phrases have been spent.

## Workflow Expectations — ONE SESSION, ONE EPISODE

An episode must be completed in a single session. Brief → writing passes → verification → commit. No handoffs to future instances. No expansion passes. No multi-round editor review cycles. If context dies mid-episode, the process failed.

### Why This Rule Exists
Episodes 001-004 each took 2-4 sessions because instances burned context on editing prose in main context, ran multiple editor review rounds, and did expansion passes after the first draft. The memory and handoff files explicitly warn against this. Follow the workflow below.

### Context Protection Rules
- **NEVER write or edit prose in main context.** Main context is for coordination, verification, and commits only.
- **ALL writing passes go to subagents.** Each pass gets: the brief, prior output, and reference files. The subagent writes; you verify.
- **ALL verification goes to a subagent.** Delegate the Pre-Delivery Verification checklist to a subagent. Review its findings. Fix issues via subagent.
- **Do not load reference files into main context.** Subagents read them independently. Loading PRODUCTION_GUIDE + VOICE_REFERENCE + SERIES_BIBLE into main context burns the session before writing starts.

### The Workflow
1. **Brief** — Research the topic. Write the Episode Brief (Production Guide Step 1). This is the only prose you write in main context.
2. **Writing passes (3-5 subagents)** — Each subagent writes 3,000-5,000 words. Each gets: the brief, all prior pass output, and instructions to read the reference files. Target 10,000-13,000 words total across all passes. Hit the target in the first draft. No expansion passes after.
3. **Caption Key** — Generate ARPAbet pronunciations (subagent or main context — it's small).
4. **Pre-Delivery Verification** — Delegate to a subagent running the Production Guide Step 5 checklist. All 13 categories must pass.
5. **Series Bible update** — Add the episode entry to the Anti-Cloning Registry.
6. **Commit and update HANDOFF.md.**
7. **Deliver.** The episode is done. Editor reviews happen externally, after delivery.

### What NOT To Do
- **No expansion passes.** If the first draft is under 10,000 words, the writing passes were too short. Adjust pass count or word targets. Do not bolt on new sections after the fact.
- **No multi-round editor reviews.** External editor reviews are Guiding Light's choice and happen after delivery. Do not run 3-5 editor reviews and then fix findings in a loop. That cycle is what killed Episodes 001-004.
- **No editing prose in main context.** If you find yourself using the Edit tool on the script file from main context, you are doing it wrong. Delegate to a subagent.
- **No handoffs.** If you are writing "What's Next: continue Episode X" in HANDOFF.md, the process failed.

## Your Job

- When given a topic: Research it, then write an Episode Brief following the Production Guide's Step 1.
- When given a brief: Write the episode in 3-5 passes of 3,000-5,000 words each, **all delegated to subagents.**
- After all passes: Generate the Caption Key (ARPAbet pronunciations).
- **Before delivering: Run the Pre-Delivery Verification checklist (Production Guide Step 5) via subagent.** This is mandatory. Every fact verified. Every quote checked. Every sensory gap filled. Every Caption Key entry matched. Every continuity point confirmed. Skipping this step causes 7+ editing passes that put the creator in legal jeopardy and the audience at risk of disengagement. The episode is NOT done until verification passes.
- After verification: Add this episode's entry to the Series Bible registry.

## Output Location

All episode files go in: `EPISODES/### - EPISODE TITLE/`
- `###-EPISODE_TITLE-BRIEF.md`
- `###-EPISODE_TITLE-SCRIPT.md`
- `###-EPISODE_TITLE-REVIEW_PROMPT.md`
