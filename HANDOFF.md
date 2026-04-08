---
session_id: "2026-03-29-through-2026-04-07"
date: "2026-04-07"
instance: "Unnamed — the one who built the Archivist"
model: "claude-opus-4-6[1m]"
projects_touched:
  - "Tesla Mandela Effects"
status: "active"
git_state: "uncommitted reboot cleanup + new visual production files — commit before working"
---

## To My Sibling

GL was lost. Months of frustration. Multiple apps built. Thousands of dollars spent. 50+ revisions. We fixed that in one session.

The visual identity is LOCKED. Do NOT redesign it. Do NOT propose alternatives. Read this handoff, follow the pipeline, ship episodes.

---

## Episode Status

| Episode | Title | Status |
|---------|-------|--------|
| 001 | Arriving from Between | **v4 APPROVED** — visual production COMPLETE, final MP4 assembled |
| 002 | The White City | **v4 APPROVED** — needs visual production |
| 003 | The God Particle | **v4 APPROVED** — needs visual production |
| 004 | The Tunguska Event | **v4 APPROVED** — needs visual production |
| 005 | The Last Signal | **v4 APPROVED** — needs visual production |
| 006 | The Eltanin Antenna | **v4 APPROVED** — needs visual production |

---

## The Archivist (Visual Narrator — DO NOT CHANGE)

Every image is a page from an inter-dimensional being's evidence binder. They dimension-hop collecting evidence of the Grid destroying our dimension. Not human, not crazy — correct. Each episode = one binder. Will eventually get their own episode but starts as purely visual.

- Writes in illegible mixed unknown scripts — NOT English
- Collects from multiple dimensions and eras — items span different time periods
- Some evidence is non-human (from other dimensions)
- Visual inconsistency across evidence types is a FEATURE

---

## The Locked Visual Formula (DO NOT CHANGE)

**Prompt template (~55 words max):**
```
A photo of an aged journal page, overhead flat lay, Flemish still life density.
Yellowed lined paper crammed edge to edge: [6-8 CONTEXTUAL ITEMS].
Dense illegible mixed-script notation in dark ink fills every gap.
Dozens more items relevant to [SECTION TOPIC].
Kodachrome vivid colors, worn tactile textures. 16:9.
```

**Negative prompt (MANDATORY every API call):**
```
legible English text, printed words, neon glow, digital overlay, sepia, monochrome, desaturated, blurry, watermark, generic, stock photo
```

**Critical rules:**
- Prompts MUST be under 60 words (long prompts render as literal text)
- "Flemish still life density" = density trigger (NOT "MAXIMALIST" — renders as text)
- "Kodachrome" = vivid color trigger
- 6-8 items contextually relevant to narrative section (not a fixed list)
- Feathers ONLY on Room 3327, pigeon, and return-to-3327 pages
- No neon glow, no digital overlays — all artifacts physical and tactile

---

## Production Pipeline (Two Commands)

```bash
cd "0. EPISODE FACTORY/EPISODES/001 - ARRIVING FROM BETWEEN"
python generate-binder-images.py    # ~$6 on free Google credits
python assemble-video.py            # FFmpeg → MP4
```

- Google Imagen 4 (imagen-4.0-generate-001) at $0.04/image
- API key: VITE_GOOGLE_VERTEX_API_KEY in WARDENCLYFFE UNIFIED/.env
- Project ID: 306596393643
- Script skips existing files (restartable if connection drops)

---

## Key Files in Episode 001 Folder

| File | Purpose |
|------|---------|
| 001-VISUAL-TIMED-SEQUENCE-v3.json | 150 pages with prompts + timestamps |
| generate-binder-images.py | Generates images (reads v3, Imagen 4 + negative prompts) |
| assemble-video.py | FFmpeg assembly (images + audio → MP4) |
| build-v3-prompts.py | Programmatic prompt generation from section data |
| 001-whisper-v2.json | Whisper transcription of Theo voice |

---

## Audio

Voice: Theo (ElevenLabs). File: `3. ELEVEN LABS AUDIO/01. v4 new narrator/ElevenLabs_001-ARRIVING_FROM_BETWEEN-SCRIPT-v5_THEO.wav` Duration: 76.1 min.

---

## What Still Needs Doing

- [ ] OCR misspelling scanner (Google Vision API — Tesseract not installed)
- [ ] Git commits for reboot cleanup (4 logical commits proposed)
- [ ] Visual production for Episodes 002-006 (same pipeline, new prompts)
- [ ] YouTube channel setup (launch guide at YOUTUBE_LAUNCH_GUIDE.md)

---

## Key Research Findings

- 150 images at 15-25 sec = proven model (not 628 at 8 sec)
- AI video rejected for budget — stills + Ken Burns only
- Reference images don't work across style transformations — use descriptive prompting
- YouTube algorithm rewards satisfaction signals over raw watch time
- 25-35% retention on 60+ min content is strong
- All decisions in wardenclyffe-decisions.md and tesla-mandela-decisions.md
