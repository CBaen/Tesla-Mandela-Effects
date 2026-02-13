# PRD v2.1: Tesla Mandela Effects Production Studio
## Context-Persistent Creative Collaboration System

**Version:** 2.1  
**Last Updated:** January 2026  
**Status:** Active Development

---

## Executive Summary

This document describes the production infrastructure for "Tesla Mandela Effects," a 200+ episode fictional documentary podcast. The system solves the core challenge of AI-assisted long-form creative work: **context persistence across sessions**.

Unlike automation pipelines that process content through predefined stages, this system supports **conversational creative collaboration**—dialogue-based discovery where human and AI explore research, brainstorm fiction, and refine content together.

---

## Problem Statement

### The Context Reset Problem

Claude.ai conversations hit context limits and reset. When this happens:

1. **Momentum dies** — Everything discussed is lost
2. **Rules require re-explanation** — Editorial guidelines forgotten
3. **Research scatters** — Verified facts must be re-verified
4. **Continuity breaks** — Episode connections, character details, timeline locks vanish
5. **Creative flow interrupts** — The collaborative "spark" must be rebuilt from scratch

### What Doesn't Work

- **Automation pipelines** — Creative work is dialogue, not batch processing
- **Multi-model orchestration** — Adds complexity without solving the core problem
- **Prompt engineering alone** — Can't overcome context window limits

### What's Actually Needed

- Memory that survives session resets
- Research accessible during conversation
- Rules that don't need re-explaining
- Continuity across 200 episodes
- A collaborative partner, not a processing engine

---

## Solution Architecture

### Core Principle: Files Persist, Conversations Don't

Claude.ai Projects persist uploaded files across all conversations. The solution is **structured documents that carry context between sessions**.

```
┌─────────────────────────────────────────────────────────────┐
│                    CLAUDE.AI PROJECT                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PERSISTENT FILES (survive session resets)                  │
│  ├── SESSION_HANDOFF.md    ← Where we left off              │
│  ├── RESEARCH_CODEX.md     ← Verified facts vs speculation  │
│  ├── EPISODE_STATUS.md     ← Production pipeline state      │
│  ├── QUICK_RULES.md        ← Top 10 editorial rules         │
│  ├── Editorial Guidelines  ← Full 14-priority reference     │
│  └── Episode Drafts        ← Work in progress               │
│                                                             │
│  CONVERSATION (resets on context limit)                     │
│  └── Current working session                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### The Four Persistence Documents

#### 1. SESSION_HANDOFF.md
**Purpose:** Capture exactly where you left off so the next session can continue without re-explanation.

**Contains:**
- Current episode and status
- Exact stopping point
- Decisions made this session
- Open questions
- Files to reference

**Updated:** End of every work session

**Used:** Start of every new conversation ("Read SESSION_HANDOFF.md and continue")

#### 2. RESEARCH_CODEX.md
**Purpose:** Single source of truth for what's historically verified vs. what's our fiction.

**Contains:**
- Verified facts [V] with sources
- Speculative fiction [S] clearly marked
- Needs verification [?] queue
- Character details (real vs. invented)
- Episode connections and continuity locks

**Updated:** When research is completed or facts are used in episodes

**Used:** During creative sessions to ground speculation in real history

#### 3. EPISODE_STATUS.md
**Purpose:** Track where each episode stands in production.

**Contains:**
- Status of all episodes (Concept → Produced)
- Editorial checklist per episode
- Continuity locks (facts that can't be contradicted)
- Recurring elements tracker (prevent exhaustion)

**Updated:** After each episode work session

**Used:** Planning sessions, continuity checks

#### 4. QUICK_RULES.md
**Purpose:** The 10 most common violations in condensed form.

**Contains:**
- Speculative Bridge (3:1 ratio)
- Invisible Narrator (no "we discovered")
- Term Frequency (2-use cap)
- Name Economy (≤6 per episode)
- Opening Hook (vertigo first)
- And 5 more critical rules

**Updated:** Rarely (when patterns emerge)

**Used:** Every editing session (faster than full guidelines)

---

## Session Protocol

### Starting a Session

```
USER: "Read SESSION_HANDOFF.md and continue where we left off."

CLAUDE: [Reads handoff, understands context, continues work]
```

If starting fresh work:
```
USER: "I'm working on Episode [X]. Read RESEARCH_CODEX.md for 
       relevant facts and QUICK_RULES.md for editorial guidelines."
```

### During a Session

**For Research Questions:**
```
USER: "What do we know about Dane's death? Check RESEARCH_CODEX.md."

CLAUDE: [References codex, distinguishes verified from speculative]
```

**For Rule Checks:**
```
USER: "Does this passage violate any rules?"

CLAUDE: [References QUICK_RULES.md, identifies issues]
```

**For Continuity:**
```
USER: "What's locked in previous episodes that I can't contradict?"

CLAUDE: [References EPISODE_STATUS.md continuity locks]
```

### Ending a Session

Before context runs out or you're done for the day:

```
USER: "Update SESSION_HANDOFF.md with where we are now."

CLAUDE: [Captures current state, decisions, next steps]
```

If research was done:
```
USER: "Add what we verified to RESEARCH_CODEX.md."

CLAUDE: [Updates codex with new [V], [S], or [?] entries]
```

If episode status changed:
```
USER: "Update EPISODE_STATUS.md."

CLAUDE: [Updates status, checks off completed items]
```

---

## Workflow: The Creative Conversation

This is NOT a pipeline. It's dialogue.

### Example: Brainstorming Episode Content

```
USER: "I'm working on Episode 4. Nikola is 7 and alone after 
       Dane's death. What real Tesla facts from this period 
       could we use? What's interesting to speculate about?"

CLAUDE: [Checks RESEARCH_CODEX.md for verified facts from 1863-1870]

"From Tesla's autobiography, we know:
- [V] He had the 'tongues of fire' visions intensely during this period
- [V] He nearly died from cholera at age 17
- [V] His father promised he could study engineering if he survived

For speculation:
- [S] We've established Dane saw 'the grid' — what if Nikola now 
  sees it too, but differently? Dane watched; Nikola receives?
- [S] The household dynamic shifts — he's no longer 'the other one'

What angle interests you most?"
```

### Example: Fact-Checking During Writing

```
USER: "I wrote that Tesla was 5 when Dane died. Is that right?"

CLAUDE: [Checks RESEARCH_CODEX.md]

"No — that's a micro-fact error. Born July 1856, Dane died 1863. 
Tesla was 6-7 years old. Want me to fix that reference?"
```

### Example: Editorial Review

```
USER: "Check this passage against QUICK_RULES.md"

[Passage provided]

CLAUDE: "Two issues:
1. Term frequency: 'tissue' appears 4 times (cap is 2)
2. Pronoun avalanche: 7 consecutive 'she' sentences without 
   re-anchoring Marta's name

Suggested fixes: [provides alternatives]"
```

---

## Research Integration

### The Speculative Fiction Challenge

Tesla Mandela Effects blends:
- **Verified history** (Tesla's actual life, documented events)
- **Speculative fiction** (alternate timelines, fictional causation)

The challenge: Keep these clearly distinguished while weaving them seamlessly in the narrative.

### RESEARCH_CODEX Structure

```
VERIFIED [V] = Documented fact with source
├── Tesla's autobiography "My Inventions"
├── Scholarly biographies (Carlson, Seifer)
├── Contemporary records (patents, newspapers, FBI files)

SPECULATIVE [S] = Our fictional interpretation
├── The Incision framework
├── The Grid
├── Medical metaphor (infection, rejection, etc.)
├── Fictional characters (Marta, Father Toma's vow)

NEEDS VERIFICATION [?] = Claimed but unconfirmed
├── Research queue
├── Blocking issues for current work
```

### Research Workflow

**Before Writing:**
```
1. Check RESEARCH_CODEX.md for what's already verified
2. Identify what needs verification for this episode
3. Do research (web search, source documents)
4. Update codex with findings: [V], [S], or [?]
5. Begin writing with clear fact/fiction boundaries
```

**During Writing:**
```
- Reference codex for consistency
- Mark new claims that need verification
- Distinguish narrator presenting facts vs. speculation
```

**After Writing:**
```
- Update codex with anything new
- Note which facts were used in which episode
- Add continuity locks for established details
```

---

## Editorial Enforcement

### The Rule Re-Explanation Problem

Full editorial guidelines are ~15,000 words. Loading them every session:
- Consumes context unnecessarily
- Still requires interpretation for each case
- Doesn't guarantee consistent application

### Tiered Rule System

```
TIER 1: QUICK_RULES.md (always loaded)
├── 10 most common violations
├── One-line rules with examples
├── Fast reference during editing
└── ~1,500 words

TIER 2: Full Guidelines (loaded when needed)
├── 14 priorities with deep reasoning
├── 4 good + 4 bad examples each
├── Edge cases and judgment calls
└── ~15,000 words

TIER 3: Episode-Specific Notes (in handoff)
├── Decisions made for this episode
├── Rule interpretations applied
├── Exceptions and justifications
```

### Editorial Workflow

**For Routine Editing:**
```
USER: "Edit this passage. Check QUICK_RULES.md."

CLAUDE: [Applies top 10 rules, flags violations]
```

**For Complex Judgment Calls:**
```
USER: "I'm not sure if this violates Speculative Bridge. 
       Check the full guidelines for Priority 1."

CLAUDE: [References full guidelines, explains reasoning]
```

**For Establishing Precedent:**
```
USER: "We decided X interpretation applies here. 
       Note it in SESSION_HANDOFF.md for continuity."

CLAUDE: [Records decision for future sessions]
```

---

## Future Expansion (Phase 2+)

### Browser Extensions for Cross-Session Memory

Tools like AI Context Flow or MemoryPlugin could provide:
- Persistent memory buckets (Tesla Facts, Writing Rules, Episode Continuity)
- One-click context injection when starting new conversations
- Works across Claude.ai conversations without file management

**Status:** Research complete, implementation optional

### MCP Server for Automated Persistence

A custom MCP server could:
- Auto-save session state on context warning
- Auto-load relevant context on session start
- Track term frequency across documents
- Verify facts against research database

**Status:** Requires Claude Code or API access, not Claude.ai

### Research Database

A structured database could:
- Store verified facts with source citations
- Track which facts used in which episodes
- Flag contradictions automatically
- Semantic search across research

**Status:** Future consideration

---

## Implementation Checklist

### Immediate (Phase 1)

- [x] Create SESSION_HANDOFF.md template
- [x] Create RESEARCH_CODEX.md structure
- [x] Create EPISODE_STATUS.md tracker
- [x] Create QUICK_RULES.md condensed reference
- [ ] Populate RESEARCH_CODEX with existing verified facts
- [ ] Update EPISODE_STATUS with current episode states
- [ ] First full session using new protocol

### Short-Term (Phase 1.5)

- [ ] Refine templates based on actual usage
- [ ] Identify patterns in context loss
- [ ] Build episode-specific continuity sections
- [ ] Create Caption Key management system

### Medium-Term (Phase 2)

- [ ] Evaluate browser extension options
- [ ] Consider external research database
- [ ] Explore MCP possibilities if using Claude Code

---

## Success Metrics

### Context Persistence
- Sessions resume without re-explanation: Target 90%+
- Research facts found on first reference: Target 95%+
- Rule violations caught before they compound: Target 80%+

### Production Velocity
- Time to resume work after context reset: <5 minutes
- Episodes completed per month: [baseline + improvement]
- Revision cycles before final: Reduced by [X]%

### Quality Consistency
- Editorial violations per episode: Decreasing trend
- Continuity errors caught in review: <2 per episode
- Research accuracy: 100% for [V] tagged facts

---

## Appendix: Document Templates

See attached files:
- SESSION_HANDOFF.md
- RESEARCH_CODEX.md
- EPISODE_STATUS.md
- QUICK_RULES.md

---

*This PRD is a living document. Update as the production system evolves.*
