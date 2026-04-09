# Visual Production Guide — Tesla Mandela Effects

## The Complete Audio-to-Video Pipeline

This document describes every step from audio file to final rendered video. Follow it exactly. Do not skip steps. Do not simplify.

---

## Step 1: Whisper Transcription

**Input:** ElevenLabs WAV file from `3. ELEVEN LABS AUDIO/01. v4 new narrator/`
**Output:** `###-whisper.json` in the episode folder
**Tool:** faster-whisper on GPU (CUDA)

```python
from faster_whisper import WhisperModel
model = WhisperModel('small', device='cuda', compute_type='float16')
segments, info = model.transcribe(audio_path, word_timestamps=True)
```

This gives word-level timestamps for the entire episode. The JSON contains segments with start/end times and text.

---

## Step 2: Build Timed Sequence

**Input:** Whisper JSON
**Output:** `###-VISUAL-TIMED-SEQUENCE-v3.json`
**Tool:** `build-v3-prompts.py` in episode folder

This divides the audio into 150 evenly-spaced pages and assigns each to a narrative section based on timestamp position. Each page gets a basic prompt from section templates.

NOTE: For v4 quality, this step is SUPERSEDED by Step 3. The v3 sequence is used only for timing data.

---

## Step 3: Art Team Prompts (v4 — CURRENT STANDARD)

**Input:** Script + Whisper timing
**Output:** `prompts-v4-pages-###-###.json` files
**Tool:** Subagent art teams (2-3 per episode, each handling 50-75 pages)

CRITICAL RULES for art teams:
- **EACH PAGE = ONE NARRATIVE BEAT** — story moves forward every page. No repeating locations.
- **TWO LAYERS per page:** Investigation evidence + Archivist's personal mess (red herrings from other dimensions)
- **4000-8000 CHARACTERS per prompt** — describe what a camera would SEE. Material + color + condition + position for every object. No abstract language.
- **The Archivist is a manic hoarder-slob** — personal items from impossible cities, snack wrappers in unknown languages, trinkets with zero investigative relevance, mixed in with evidence.
- **Escalation:** Final 20 pages of each episode get progressively stranger — Archivist's non-human nature bleeds through more overtly.

Prompt structure:
```
Generate an image of an investigation journal page photographed from directly above.

BACKGROUND: [unique page — specific stains, damage, wear]
PRIMARY EVIDENCE (this narrative beat): [2-3 items, exhaustive physical detail]
SECONDARY EVIDENCE: [4-6 related items]
THE ARCHIVIST'S PERSONAL ITEMS: [4-6 from other dimensions — red herrings]
SCATTERED FILLING EVERY GAP: [8-12 small objects with materials described]
HANDWRITING: [dense illegible non-English notation — ink color, pressure, density]
CONNECTIONS: [red thread paths, brass pins, arrows]
STYLE: Victorian Wunderkammer meets crime scene evidence board meets inter-dimensional hoarder's junk drawer. Every square centimeter covered. Kodachrome vivid saturated colors. Photorealistic overhead flat lay. No readable English text. 16:9.
```

Episode-specific themes:
- Ep 001: Personal investigation (Tesla's life/death)
- Ep 002: Destroyed empire, archaeological (Tartaria/old world)
- Ep 003: Multiverse artifacts, non-human technology (most alien)
- Ep 004-006: GL provides direction per episode

---

## Step 4: Generate Images

**Input:** v4 prompt JSON files
**Output:** PNG images in episode `binder-images/` folder
**Tool:** `generate-v4-images.py` — calls Gemini 3.1 Flash Image
**Model:** `gemini-3.1-flash-image-preview` via Generative Language API
**Cost:** ~$0.067/image, ~$10/episode
**API key:** `VITE_GOOGLE_VERTEX_API_KEY` in `WARDENCLYFFE UNIFIED/.env`

The script:
- Reads all v4 prompt JSON files
- Generates one image per page
- Skips existing files (restartable if connection drops)
- Supports page ranges: `python generate-v4-images.py 50 75`

DO NOT generate all 150 without GL approving a 5-page test batch first.

**Imagen 4 is DEPRECATED June 30, 2026 — do not use.**

---

## Step 5: Package for Desktop App

**Input:** Generated images + timed sequence
**Output:** `###-desktop-render.json` in episode folder
**Tool:** `package-for-desktop.py`

This script creates the render config for Wardenclyffe Desktop:
```json
{
  "scenes": [{"imagePath": "absolute/path.png", "duration": 30.5, "kenBurns": {"type": "zoom-in", "intensity": 0.15}}],
  "outputPath": "path/to/output.mp4",
  "fps": 30,
  "resolution": {"width": 1920, "height": 1080},
  "quality": "high",
  "crossfade": 0.5
}
```

Ken Burns types: zoom-in, zoom-out, pan-left, pan-right, pan-up, pan-down, none.
Smart assignment: zoom-in for reveals, pan for transitions, zoom-out for establishing.

---

## Step 6: Copy Images to Correct Directory

**Images go to:** `C:\Users\baenb\Desktop\Tesla Mandela Effects\4. EPISODE IMAGES\`

NOT in random episode subdirectories. The `4. EPISODE IMAGES/` directory is the established location for production-ready images.

---

## Step 7: Render in Wardenclyffe Desktop

**App location:** `C:\Users\baenb\projects\WARDENCLYFFE_DESKTOP`
**Input:** The `###-desktop-render.json` from Step 5
**Output:** MP4 with Ken Burns motion effects (silent — no audio)

Load the JSON into the desktop app. It renders each scene with the assigned Ken Burns motion and crossfade transitions.

**DO NOT use assemble-video.py (FFmpeg static) as the final render.** That script exists only as a quick reference preview. The desktop app is the production render path.

---

## Step 8: GL Finalizes

GL handles:
- Music editing and timing
- Remotion cold start → rushing sound → content → Grid ending (series signature)
- Audio layering onto the Ken Burns video
- YouTube upload with chapter markers

---

## Misspelling Scanner

**Tool:** `scan-misspellings-gemini.py` — uses Gemini 2.5 Flash vision
**When:** After image generation, before packaging
**Output:** `###-misspelling-report.json` listing pages with visible misspelled English

GL reviews flagged pages and fixes in Canva if needed.
