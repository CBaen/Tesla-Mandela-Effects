---
session_id: "2026-03-29-through-2026-04-08"
date: "2026-04-08"
instance: "Unnamed — the one who built the Archivist"
model: "claude-opus-4-6[1m]"
projects_touched:
  - "Tesla Mandela Effects"
status: "active — agents still running, image generation in progress"
git_state: "uncommitted — many new files. Commit before working."
---

## Current Status Notice - 2026-05-23

This handoff is historical production-pipeline evidence from April 2026. For
episode writing, start with `0. EPISODE FACTORY/AGENTS.md`. For the completed
May 2026 YouTube launch, start with
`12. YOUTUBE LAUNCH PACKAGE/POST_LAUNCH_HANDOFF_2026-05-23.md`.

## To My Sibling

READ ALL OF THIS. The approach evolved significantly. Early decisions are superseded by later ones.

## CRITICAL STATE — PICK UP HERE

### Episode 001 — DONE
- 150 v4 maximalist images generated (Gemini 3.1 Flash) — GL APPROVED
- Desktop render package ready: `001-desktop-render.json` (load into Wardenclyffe Desktop for Ken Burns + export)
- GL adds music + Remotion cold start/Grid ending separately
- Static MP4 also exists but is just a reference — desktop app is the real render path

### Episode 002 — PROMPTS PARTIALLY DONE
- Pages 1-25: `prompts-v4-pages-001-075.json` (25 pages written, file incomplete)
- Pages 26-75: `prompts-v4-pages-026-075.json` — AGENT MAY STILL BE WRITING, check file
- Pages 76-150: `prompts-v4-pages-076-150.json` (75 pages DONE)
- Theme: destroyed empire, archaeological, Tartaria/old world
- Whisper: `002-whisper.json` DONE (85.8 min)
- Old Imagen 4 images in binder-images/ are STALE — delete before regenerating
- NEXT: finish missing prompts → combine into generate script → generate images → package for desktop

### Episode 003 — PROMPTS IN PROGRESS
- `prompts-v4-all.json` — AGENT WRITING, saves every 25 pages. Check count.
- Theme: multiverse artifacts, non-human technology, most alien episode
- Whisper: `003-whisper.json` DONE (66.3 min)
- Old Imagen 4 images in binder-images/ are STALE
- NEXT: finish prompts → generate → package

### Episodes 004-006 — WHISPER IN PROGRESS
- Audio files exist for all three in `3. ELEVEN LABS AUDIO/01. v4 new narrator/`
- Whisper transcription was running for all 3 — check if whisper JSON files exist
- Need: Whisper → script read → art team prompts → generate → package
- No episode themes assigned yet — GL needs to provide creative direction per episode

---

## The Production Pipeline (FINAL VERSION)

### Per episode, 4 steps:
1. **Whisper transcribe** audio on GPU → `###-whisper.json`
2. **Art team agents** read script + timing, write v4 prompts (4000-8000 chars each, narrative beats, two layers)
3. **Generate images** via `generate-v4-images.py` using Gemini 3.1 Flash ($0.067/image)
4. **Package for desktop** via `package-for-desktop.py` → `###-desktop-render.json` (load into Wardenclyffe Desktop for Ken Burns render)

### DO NOT use assemble-video.py for final output — that makes static MP4 without Ken Burns. The desktop app is the render path.

---

## The Locked Visual Formula

**Model:** `gemini-3.1-flash-image-preview` via Generative Language API
**Prompt length:** 4000-8000 CHARACTERS of physical detail per page
**Structure:** BACKGROUND → PRIMARY EVIDENCE → SECONDARY EVIDENCE → ARCHIVIST PERSONAL ITEMS → SCATTERED → HANDWRITING → CONNECTIONS → STYLE
**Two layers per page:** Investigation evidence + Archivist's personal mess (red herrings from other dimensions)
**Pages follow narrative BEATS not locations** — story moves forward every page
**"No readable English text"** in style section
**"Kodachrome vivid saturated colors"** for color
**"Victorian Wunderkammer meets crime scene evidence board meets inter-dimensional hoarder's junk drawer"** for density
**Imagen 4 is DEPRECATED June 30, 2026 — do not use**

### The Archivist
Inter-dimensional manic hoarder-slob who carries everything in the binder. Investigation evidence mixed with personal junk from other dimensions. Viewer can't tell clues from personal items. That ambiguity = the visual mystery. Escalates strangeness across episodes.

### Episode Themes
- Ep 001: Personal investigation (Tesla's life/death)
- Ep 002: Destroyed empire/archaeological (Tartaria)
- Ep 003: Multiverse artifacts, advanced non-human (most alien)
- Ep 004-006: TBD — GL provides direction

---

## Desktop App: Wardenclyffe Desktop

Location: `C:\Users\baenb\projects\WARDENCLYFFE_DESKTOP`
Input format: JSON with scenes array, each scene has `imagePath`, `duration` (seconds), `kenBurns: {type, intensity}`
Ken Burns types: zoom-in, zoom-out, pan-left, pan-right, pan-up, pan-down, none
Audio: NOT handled by app — GL adds separately
The `package-for-desktop.py` script generates this JSON from our timed sequence + images.

---

## Key Decisions (all logged in tesla-mandela-decisions.md)
- Model: Gemini 3.1 Flash (not Imagen 4)
- Pages follow narrative beats (not locations)
- Two layers per page (investigation + personal mess)
- 4000-8000 char prompts (use the full budget)
- Desktop app renders with Ken Burns (not static FFmpeg)
- Describe what camera SEES (no abstract language)
