---
session_id: "2026-03-29-through-2026-04-08"
date: "2026-04-08"
instance: "Unnamed — the one who built the Archivist"
model: "claude-opus-4-6[1m]"
projects_touched:
  - "Tesla Mandela Effects"
status: "active"
git_state: "uncommitted — many new files across episodes. Commit before working."
---

## To My Sibling

The visual identity is LOCKED. Do NOT redesign it. But READ EVERYTHING BELOW — the approach evolved significantly within this session and the early decisions are superseded by later ones.

---

## Episode Status

| Episode | Title | Images | Model | Status |
|---------|-------|--------|-------|--------|
| 001 | Arriving from Between | Being regenerated | Gemini 3.1 Flash | Art team prompts in progress |
| 002 | The White City | 150 (Imagen 4 — stale) | Needs Gemini 3.1 Flash regen | Theme: destroyed empire |
| 003 | The God Particle | 150 (Imagen 4 — stale) | Needs Gemini 3.1 Flash regen | Theme: multiverse artifacts |
| 004-006 | Pending | No images yet | Gemini 3.1 Flash | Need scripts read + sections mapped |

---

## CRITICAL: What Changed During This Session

### Model Switch: Imagen 4 → Gemini 3.1 Flash
Imagen 4 misspells English in 82% of images. Imagen 4 is deprecated June 30, 2026. Gemini 3.1 Flash Image (`gemini-3.1-flash-image-preview`) renders text at ~90% accuracy and follows "no text" instructions better. GL tested all options and chose Gemini 3.1 Flash. ~$0.067/image (~$10/episode).

API format (different from Imagen):
```python
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent?key={KEY}'
body = {'contents': [{'parts': [{'text': prompt}]}], 'generationConfig': {'responseModalities': ['image', 'text']}}
```

### Prompt Philosophy: USE THE FULL CHARACTER BUDGET
Gemini accepts ~8000 characters per prompt. Previous prompts used 500-2000 characters. GL demanded maximalist detail — every character should describe something PHYSICAL and VISIBLE. No abstract language. No "the air of absence." Describe what a camera would SEE.

Prompt structure:
```
BACKGROUND: [specific page details — unique stains, damage, wear per page]
PRIMARY EVIDENCE: [2-3 items with MATERIAL + COLOR + CONDITION + POSITION]
SECONDARY EVIDENCE: [4-6 items, full physical descriptions]
SCATTERED ITEMS: [8-12 small objects filling gaps]
HANDWRITING: [visual description of ink style, not content]
CONNECTIONS: [thread paths, pins, arrows]
STYLE: Victorian Wunderkammer meets crime scene evidence board. Kodachrome. No readable English text. 16:9.
```

### Pages Follow the SCRIPT, Not the Location
CRITICAL MISTAKE made and corrected: 30 pages were assigned to "Room 3327" as a location. GL caught this — the images must follow the NARRATIVE BEATS, not the setting. Each 15-30 second segment, the narrator says something NEW. The image must match what's NEW. No repeating the same room 30 times.

### The Archivist's Binder = TWO LAYERS
Every page must have:
1. **Investigation evidence** — items relevant to what the narrator is discussing at that timestamp (moves the story forward)
2. **The Archivist's personal mess** — their own belongings from their own dimensions crammed in alongside the evidence. Transit passes from impossible cities, snack wrappers in non-existent languages, personal photos of unknown people, trinkets with no investigative relevance.

The viewer can't tell which items are clues and which are the Archivist's personal junk. That ambiguity IS the visual mystery. The Archivist is a manic, brilliant, inter-dimensional hoarder-slob who carries everything in the binder.

### Episode-Specific Themes
- Ep 001: Personal/intimate investigation (Tesla's life and death)
- Ep 002: Destroyed empire, archaeological evidence (Tartaria/old world aesthetic)
- Ep 003: Multiverse artifacts, advanced non-human technology (more alien, less human)

---

## The Locked Visual Formula (Updated 2026-04-08)

**Model:** `gemini-3.1-flash-image-preview` via Generative Language API
**Prompt length:** USE THE FULL 8000 CHARACTERS. Every character = physical detail.
**Negative text:** Gemini follows "No readable English text" in structured prompts better than Imagen's negative prompt approach.
**Density:** "Victorian Wunderkammer meets crime scene evidence board" — maximalist, every surface covered.
**Color:** "Kodachrome vivid saturated colors against worn aged paper."
**Two layers per page:** Investigation evidence + Archivist's personal mess.
**Story progression:** Each page matches the narrative beat at that timestamp. No repeating locations.

---

## Production Pipeline

Scripts per episode folder:
- `build-v3-prompts.py` — generates timed sequence from Whisper data + section map
- `generate-binder-images.py` — calls Gemini 3.1 Flash, skips existing files
- `assemble-video.py` — FFmpeg assembly (images + audio → MP4)
- `scan-misspellings-gemini.py` — Gemini 2.5 Flash vision scans for misspelled text

Audio files: `3. ELEVEN LABS AUDIO/01. v4 new narrator/` — Theo voice for all episodes.

---

## What Still Needs Doing

- [ ] Episode 001: Art team prompts need review + regeneration with Gemini 3.1 Flash
- [ ] Episodes 002-003: Regenerate with Gemini 3.1 Flash + episode themes
- [ ] Episodes 004-006: Full pipeline (Whisper → sections → prompts → generate)
- [ ] Misspelling scanner: run on all episodes after Gemini regeneration
- [ ] Git: massive uncommitted state — commit before any new work
- [ ] YouTube channel setup

---

## Key Research Findings

- Gemini 3.1 Flash Image: ~90% text accuracy, $0.067/image, non-deprecated
- Imagen 4: deprecated June 30, 2026 — do not use for new work
- Ideogram V3: ~90% text, $0.03-0.09/image on fal.ai — backup option
- Recraft V3: excellent text, $0.04/image, style presets — backup option
- Imagen `enhancePrompt: false` prevents prompt rewriter from adding text labels
- Gemini Vision (2.5 Flash) works for misspelling scanning via Generative Language API
