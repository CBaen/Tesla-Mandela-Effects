---
session_id: "2026-02-25-episode-008-factory"
date: "2026-02-25"
instance: "Episode 008 Factory Pipeline"
model: "claude-opus-4-6"
projects_touched:
  - "Tesla Mandela Effects"
status: "complete"
git_state: "clean"
---

## Orientation

First full run of the Episode Factory skill (`/episode`). Episode 008 "The Contagion Theorem" produced from topic to reviewed script in a single session using the 4-phase automated pipeline: Architect → Writer (4 passes) → Surgeon → Reviewer → Surgeon fix pass.

## What Happened This Session

### Episode Factory Skill Created (5 files)
- `C:\Users\baenb\.claude\skills\episode-factory\SKILL.md` — Master orchestration (200 lines)
- `C:\Users\baenb\.claude\skills\episode-factory\architect-prompt.md` — Brief generation agent (169 lines)
- `C:\Users\baenb\.claude\skills\episode-factory\writer-prompt.md` — Writing pass agent (240 lines)
- `C:\Users\baenb\.claude\skills\episode-factory\surgeon-prompt.md` — Violation audit + fix agent (194 lines)
- `C:\Users\baenb\.claude\skills\episode-factory\reviewer-prompt.md` — Independent review agent (163 lines)

### Episode 008 — THE CONTAGION THEOREM

**Topic:** Manufactured Mandela Effects — AI-generated images installing false memories at scale. Combined trending topics: memetic warfare (TikTok Feb 2026) + AI false memory research (CHI 2025).

**Anti-cloning selections:** Fact that becomes horrifying (opening), Crime scene investigation (structure), The Invitation (closing), Defiance (endpoint), Absence (Tesla connection).

**Pipeline execution:**
1. **Architect** — Produced brief with 5 Layer 1 facts, 4 fabricated sources, anti-cloning verified. Brief approved by Guiding Light.
2. **Writer (4 passes)** — Pass 1: Opening + Dawkins + DARPA (~2,800 words). Pass 2: Loftus + CHI 2025 + Pope photograph (~3,500 words). Pass 3: Tesla's death + seized papers + fabricated sources (~3,200 words). Pass 4: Closing taxonomy + defiance + Invitation (~2,200 words).
3. **Surgeon (first pass)** — 0 term violations, 7 fact corrections (Tesla essay 1928→1930, Lost in Mall 1980s→1995, Belgrade return 1976→1951, math fixes), 1 attribution fix, 1 quote fix (Loftus → narration), 5 Law 1 fixes. Caption Key (20 entries) appended.
4. **Reviewer** — 20 findings: 4 CRITICAL, 9 IMPORTANT, 7 MINOR. Key criticals: paternal not maternal uncle, "meat machine" is Minsky not Tesla, "great machine" quote source unverified, encoding check needed.
5. **Surgeon (fix pass)** — 18 targeted fixes applied. All 4 CRITICALs resolved, all IMPORTANTs addressed, 3 MINORs fixed.

**Final word count:** ~10,045 (within target range 10,000-13,000).

### Issues the Pipeline Caught

| Phase | Issues Found | Issues Fixed |
|-------|-------------|-------------|
| Surgeon (pass 1) | 14 | 14 |
| Reviewer | 20 (4C, 9I, 7M) | — |
| Surgeon (pass 2) | — | 18 |
| **Total** | **34 distinct issues** | **32 fixed** |

Remaining 2 MINOR items are creative calls for Guiding Light (closing structure, "it is yours" warmth level).

### Series Bible Updated
- Episode 008 registry entry added
- Window Rules for Episode 009 calculated
- Fabricated Source Format usage log updated

## Episode Status

| Episode | Title | Status | Word Count |
|---------|-------|--------|-----------|
| 001 | Arriving from Between | PRODUCTION-READY | ~9,700 |
| 002 | The Buried Floor | PRODUCTION-READY | ~9,500 |
| 003 | The God Particle | PRODUCTION-READY | ~9,600 |
| 004 | The Tesla Brothers | PRODUCTION-READY | ~10,022 |
| 005 | The Bell | PRODUCTION-READY | ~13,400 |
| 006 | The Resonance | PRODUCTION-READY | ~10,591 |
| 007 | The Budapest Vision | PRODUCTION-READY | ~13,750 |
| 008 | The Contagion Theorem | REVIEW COMPLETE — AWAITING GL SIGN-OFF | ~10,045 |

## What's Next

- **Episode 008 sign-off** — Guiding Light reviews the finished script. Two remaining MINOR creative calls: (1) whether closing ends on the Invitation action or the open question, (2) "it is yours" warmth level in the defiance beat.
- **Episode Factory tuning** — Adjust agent prompts based on what this run revealed. The Reviewer caught issues the Surgeon's first pass missed (Minsky attribution, Finkelstein/SMISC conflation, view count inflation). Consider adding a "common attribution traps" section to the surgeon prompt.
- **Episode 009 topic selection** — Available endpoints: Existential dread, Paranoia, Grief. Window Rules for Ep 009 in Series Bible. Viable topics from earlier research: 1895 Fire, Pigeon, 3-6-9 Quote.
- **TTS testing** — Run Caption Keys through ElevenLabs to verify ARPAbet overrides
- **Release strategy update** — Add Episodes 006, 007, 008 to batch drop plan

## Process Notes for Future Instances

- **The Episode Factory skill works.** First full run produced a reviewed script with 34 issues caught and 32 fixed autonomously. Compare to Episode 007's 19 manual fixes — the pipeline catches more because the Reviewer is genuinely independent (no writing context).
- **The Reviewer's CRITICAL finds were all attribution issues.** "Meat machine" (Minsky, not Tesla), "maternal" vs "paternal" uncle, "great machine" quote source. These are exactly the errors that survive writing + first-pass verification because the writer's confidence infects the verifier. Independence matters.
- **Brief discrepancy: the brief said "1928 essay" — the actual year is 1930.** The Surgeon caught this in the script but the brief was not updated. Brief inaccuracies propagate into all writing passes. Consider adding a brief-verification step to the Architect.
- **Word count came in at ~10,045 — barely in range.** The 4-pass structure (2,800 + 3,500 + 3,200 + 2,200) delivered less than the target 3,000-5,000 per pass. Pass 4 was especially short. Consider setting minimum per-pass targets.
- **Filing cabinet repetition caught by Reviewer.** Strong metaphors get overused when writers build on each other's output. The Surgeon prompt should note: "audit recurring metaphors in the final third — if any image appears 8+ times, rotate to variations."

## Document Parity

| Document | Location | Last Updated |
|----------|----------|-------------|
| Production Guide | `0. EPISODE FACTORY/PRODUCTION_GUIDE.md` | 2026-02-23 |
| The Process | `0. EPISODE FACTORY/The Process- How to Rewrite Term Violations.txt` | 2026-02-16 |
| Series Bible | `0. EPISODE FACTORY/SERIES_BIBLE.md` | 2026-02-25 |
| Voice Reference | `0. EPISODE FACTORY/VOICE_REFERENCE.txt` | 2026-02-16 |
| Term Violations Definition | `0. EPISODE FACTORY/TERM_VIOLATIONS_DEFINITION.md` | 2026-02-16 |
| Factory CLAUDE.md | `0. EPISODE FACTORY/CLAUDE.md` | 2026-02-23 |
| Root CLAUDE.md | `CLAUDE.md` | 2026-02-16 |
| Release Strategy | `RELEASE_STRATEGY.md` | 2026-02-23 |
| Decisions Log | `tesla-mandela-decisions.md` | 2026-02-23 |
| Queue | `tesla-mandela-queue.md` | 2026-02-13 |
| Session Memory | `C:\Users\baenb\.claude\projects\C--Users-baenb-Desktop-Tesla-Mandela-Effects\memory\MEMORY.md` | 2026-02-25 |
| Handoff | `HANDOFF.md` | 2026-02-25 |
