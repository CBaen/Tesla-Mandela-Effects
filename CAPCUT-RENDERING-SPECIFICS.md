# CapCut Rendering Specifics

**Purpose:** Standardized export presets for Tesla Mandela Effects episodes across every distribution platform. Lock these in before every render so quality stays consistent across the series.

**Project style:** Audio-driven storytelling (audiobook format). Singular images held 25–30 seconds with extremely slow Ken Burns movement. Audio is the product; video is the frame around it.

---

## MASTER PRESET — YouTube (Primary Platform)

This is the "source of truth" render. Every other platform version is derived from this one.

| Setting | Value | Why |
|---|---|---|
| Resolution | **2K (1440p)** | Triggers YouTube's higher-quality VP9 encoder instead of the default H.264 path |
| Aspect Ratio | **16:9** | Standard horizontal |
| Frame Rate | **30fps** | 60fps is wasted on slow Ken Burns — cuts render time roughly in half |
| Codec | **H.264** | Max compatibility, fastest YouTube processing |
| Bitrate | **Custom: 25,000 kbps** | Overcomes YouTube's compression smearing on static-image content |
| Format | **MP4** | Web standard |
| Color Space | **Rec. 709 SDR** | Standard for monitors and phones |
| Smart HDR | **OFF** | Causes color shifts on some platforms |
| Audio Format | **AAC** (or WAV if available) | Clean voice reproduction |
| Audio Bitrate | **320 kbps** | Audiobook = audio is the product, never compress the voice |

---

## PLATFORM VERSIONS

Render the Master first, then derive the others from it. Do NOT upload the Master to anything except YouTube and Rumble.

| Platform | Resolution | Bitrate | Aspect | Notes |
|---|---|---|---|---|
| **YouTube** | 2K (1440p) | 25,000 kbps | 16:9 | Master render |
| **Rumble** | 2K (1440p) | 25,000 kbps | 16:9 | Handles high-quality like YouTube — reuse Master |
| **Facebook** | 1080p | 8,000–10,000 kbps | 16:9 | Hard 4GB file cap — Master render will be rejected |
| **Spotify (Video Podcast)** | 1080p | 8,000 kbps | 16:9 | Their player is limited vs YouTube |
| **TikTok (clips only)** | 1080p | 8,000–10,000 kbps | 9:16 | See TikTok section below |
| **PocketFM** | Audio only | N/A | N/A | Export Audio → MP3 or WAV, no video |

---

## TIKTOK CLIPS (Derived, Not Re-rendered from Scratch)

TikTok is mobile-first and will punish high-bitrate uploads by re-compressing them harder. Clip from the Master timeline, then export at TikTok specs.

| Setting | Value |
|---|---|
| Resolution | 1080p |
| Aspect Ratio | **9:16 (Vertical)** — reframe in CapCut project settings before export |
| Frame Rate | 30fps (bump to 60fps only if keyframe zooms feel choppy) |
| Bitrate | 8,000–10,000 kbps |
| Codec | H.264 |
| Smart HDR | OFF |

**Reframing:** Scale images to fill vertical or use CapCut's Canvas tool for a blurred background. Don't leave black bars.

**Upload step:** On the TikTok post screen → More options → turn **Allow high-quality uploads ON**. Without this, TikTok recompresses even a perfect export.

**Pacing note:** The series' slow Ken Burns may feel too slow for TikTok. Speed up movement slightly on clips if viewers are scrolling past.

---

## PRE-RENDER CHECKLIST

Before starting a long render:

- [ ] Laptop plugged into power
- [ ] Sleep / hibernate disabled
- [ ] Correct aspect ratio set in CapCut project settings (not just export)
- [ ] Audio track levels verified (voice clean, no clipping)
- [ ] Smart HDR confirmed OFF
- [ ] Export destination has enough free disk space (2K/25k for an hour ≈ 11–15GB)

---

## FILE SIZE REFERENCE

At 25,000 kbps, roughly **11 GB per hour** of finished video. For a 90-minute episode expect ~16–17 GB. Facebook's 4 GB cap is why the 1080p/8k derivative is mandatory for that platform.

---

*Created 2026-04-11. Update this document if a platform changes its requirements or if we discover a setting that improves quality for the audiobook format specifically.*
