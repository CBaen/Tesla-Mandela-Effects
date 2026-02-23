---
session_id: "2026-02-23-caption-key-and-release"
date: "2026-02-23"
instance: "Caption Key + Release Strategy Session"
model: "claude-opus-4-6"
projects_touched:
  - "Tesla Mandela Effects"
status: "complete"
git_state: "clean"
---

## Orientation

Continuation of production audit. Created release strategy document (RELEASE_STRATEGY.md). Discovered and fixed Caption Key system — body text lacked cultural diacritics, middle column used phonetic notation instead of TTS-readable spelling, ARPAbet had wrong vowel mappings for Serbian names. Production Guide updated with correct Caption Key rules.

## What Happened This Session

### Release Strategy
- Researched YouTube algorithm behavior for conspiracy-adjacent content (no keyword blacklist, but "conspiracy" framing attracts bounce-prone audiences)
- Created RELEASE_STRATEGY.md with SEO-optimized YouTube titles, descriptions, channel setup, framing rules, thumbnail strategy
- Batch drop strategy: all 5 episodes released simultaneously
- Playlist order: 001 → 002 → 005 → 003 → 004

### Caption Key Overhaul (all 5 episodes)
- **Body text diacritics:** Djuka→Đuka, Gospic→Gospić, Kosanovic→Kosanović, Gracac→Gračac, Mandic→Mandić, Munster→Münster, Lac Leman→Lac Léman, Conseil Europeen→Conseil Européen (37 instances across 4 episodes)
- **Caption Key format:** Middle column changed from phonetic notation ("JOO-kah", "Gospeech", "NIH-koh-lah") to TTS-readable spelling ("Duka", "Gospic", "Nikola")
- **ARPAbet corrections:** Serbian vowels AA (not AH) for "a", AO (not OW) for "o", IY (not IH) for "i". Nikola stress corrected to first syllable. Dane Tesla fixed from /D EY1 N/ to /D AA1 N EH0/. Robert Brout from /B R UW1/ to /B R AW1 T/. Gračac č from /S/ to /CH/. Felix Bloch from /F EY1/ to /F IY1/. Russian names (Vasin, Mikhail, Kozyrev, Shcherbakov) stress and devoicing corrected.
- **Ep 002 format:** Converted hyphens to arrows. **Ep 005 format:** Removed blank lines between entries, removed brackets from header.
- **Production Guide updated** with Caption Key three-column rules (line 217) and pre-delivery checklist verification requirements (line 306).

## Episode Status

| Episode | Title | Status | Word Count |
|---------|-------|--------|-----------|
| 001 | Arriving from Between | PRODUCTION-READY | ~9,700 |
| 002 | The Buried Floor | PRODUCTION-READY | ~9,500 |
| 003 | The God Particle | PRODUCTION-READY | ~9,600 |
| 004 | The Tesla Brothers | PRODUCTION-READY | ~10,022 |
| 005 | The Bell | PRODUCTION-READY | ~13,400 |

## What's Next

- **Episode 006 topic selection** — Check Series Bible for anti-cloning constraints
- **TTS testing** — Run Caption Keys through ElevenLabs to verify ARPAbet overrides produce correct pronunciation
- **Thumbnail creation** — See RELEASE_STRATEGY.md for image guidance per episode
- **YouTube channel setup** — Channel description, tags, category (Education) in RELEASE_STRATEGY.md

## Document Parity

| Document | Location | Last Updated |
|----------|----------|-------------|
| Production Guide | `0. EPISODE FACTORY/PRODUCTION_GUIDE.md` | 2026-02-23 |
| The Process | `0. EPISODE FACTORY/The Process- How to Rewrite Term Violations.txt` | 2026-02-16 |
| Series Bible | `0. EPISODE FACTORY/SERIES_BIBLE.md` | 2026-02-22 |
| Voice Reference | `0. EPISODE FACTORY/VOICE_REFERENCE.txt` | 2026-02-16 |
| Term Violations Definition | `0. EPISODE FACTORY/TERM_VIOLATIONS_DEFINITION.md` | 2026-02-16 |
| Factory CLAUDE.md | `0. EPISODE FACTORY/CLAUDE.md` | 2026-02-23 |
| Root CLAUDE.md | `CLAUDE.md` | 2026-02-16 |
| Release Strategy | `RELEASE_STRATEGY.md` | 2026-02-23 |
| Decisions Log | `tesla-mandela-decisions.md` | 2026-02-17 |
| Queue | `tesla-mandela-queue.md` | 2026-02-13 |
| Session Memory | `C:\Users\baenb\.claude\projects\C--Users-baenb-Desktop-Tesla-Mandela-Effects\memory\MEMORY.md` | 2026-02-23 |
| Handoff | `HANDOFF.md` | 2026-02-23 |
