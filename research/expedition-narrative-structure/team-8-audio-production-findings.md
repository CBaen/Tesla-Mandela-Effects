# Team 8: Audio Production Findings
# Practical Soundscape Production for Tesla Mandela Effects

**Research Date:** 2026-03-16
**Scope:** Loopable ambient background soundscapes for long-form narrated YouTube content using Audacity + ElevenLabs 10-minute AI music generation.

---

## 1. AI Music Generation: ElevenLabs vs. Alternatives

### ElevenLabs (Current Tool) — Verdict: Best for This Use Case

ElevenLabs Eleven Music is the strongest choice for ambient background beds, specifically because:

- **Speed:** 3-minute instrumental tracks generate in 25-30 seconds.
- **Instrumental accuracy:** 65% usable on first try for instrumentals (vs. lower rates for Suno on non-vocal work).
- **Commercial clearance:** Launched August 2025 with licensing through Merlin Network and Kobalt. First AI music generator explicitly cleared for YouTube monetization without copyright strikes. Paid plans are copyright-free commercial use with no attribution.
- **Section-by-section editing:** Generate an Intro, evaluate it, then use the "Continue" prompt box to build the next section. This gives granular control over a full ambient piece.
- **Better with electronic/ambient styles** than Suno.

**Key limitation:** Generates up to 3 minutes per generation pass (paid), not the full 10 minutes described in the brief. Multiple generations may be needed and stitched together.

### Suno — Verdict: Use for Vocal Tracks, Skip for Ambient Beds

Suno v4.5/v5 is the dominant AI music generator overall, but designed for song-with-vocals output. For ambient instrumentals, it produces a distinctive processed quality that becomes apparent on repeat listening. Better for: complete songs, experiments, high-volume iteration.

**For loopable ambient instrumental:** Suno can work with explicit prompting, but ElevenLabs outperforms it specifically in this category.

### Udio — Verdict: Highest Quality, Slowest Speed

Udio outputs 48kHz/32-bit audio with full frequency range to 20kHz — professional sample pack quality. The tradeoff is generation time (5-10 minutes per track) and a manual extension workflow. Best for: situations where audio polish matters more than iteration speed.

---

## 2. Prompting AI Music: Generic vs. Specific Results

### The Core Framework (Works for Both ElevenLabs and Suno)

Construct prompts by stacking six layers in sequence:

1. **Genre + Style** — Name the subgenre and reference era: "Dark ambient, cinematic underscore"
2. **Mood + Context** — Emotional tone and use case: "Unsettling, foreboding, for mystery documentary narration"
3. **Tempo + Key** — Musical specifics: "60 BPM in D minor" (ElevenLabs accurately follows BPM and key)
4. **Instrumentation** — Specific sounds: "Low rumbling drones, metallic textures, sparse piano, cold cavernous reverb"
5. **Structure** — Dynamic arc: "Evolves slowly with no obvious peaks, no percussion, no four-on-the-floor"
6. **Exclusions (Negative Prompts)** — What to prevent: "No vocals, no fade in/out, no reverb tails, no risers, no drums"

### Generic vs. Specific: The Practical Difference

**Generic (produces background music wallpaper):**
> "Atmospheric ambient music"

**Specific (produces usable bed):**
> "Dark ambient instrumental, 55 BPM, D minor. Evolving low drones, metallic resonance, distant wind textures, sparse dissonant strings. Cold cavernous reverb. No percussion, no vocals, no fade in/out, seamless loop. Suitable for mystery documentary narration."

**Key insight from ElevenLabs docs:** "Simple, evocative keywords often outperform lengthy prompts." The model interprets freely when given emotional texture. Over-specifying can limit creative output. Test both detailed and sparse versions of the same prompt.

### ElevenLabs-Specific Techniques

- Add **"instrumental only"** to block vocals — it does not add automatically.
- Specify **"seamless loop, no fade in/out, no reverb tails"** explicitly for loopable output.
- Use the **section-by-section workflow:** generate Intro first, refine it, then click "+" to specify style for the next section. Build the full piece incrementally.
- BPM and key are reliably followed — use them for consistency across multiple generations.
- The **"Continue the conversation"** prompt box allows extending a track once the Intro is approved.

### Suno-Specific Techniques (If Used)

- Style prompt: up to ~1,000 characters in v4.5+
- Do not name specific artists — describe genre/era instead
- To block vocals: include **"instrumental only"** or **"no vocals"** in style prompt AND put descriptive ambient text (not lyrics) in the lyrics field, e.g., "(dark ambient drone textures)"
- For looping: include **"seamless loop, no fade out"** in the style prompt
- Sample dark ambient horror prompt for Suno:
> "Dark ambient, loopable, no vocals, unsettling atmosphere, dissonant synths, sub-bass drones, industrial textures, seamless loop, no fade out, 50 BPM"

---

## 3. Time-Stretching: Paulstretch for Extending Source Material

### What Paulstretch Does

Paulstretch stretches audio by a factor — setting 10x turns 1 minute of audio into 10 minutes. It works by analyzing spectral windows and smearing them over time, which produces smooth, evolving textures rather than the robotic artifacts of standard time-stretching. It is specifically designed for ambient sound design, not rhythmic content.

### Where It Lives

- **In Audacity:** Effect > Pitch and Tempo > Paulstretch (built into modern Audacity, no separate download needed)
- **Standalone/Plugin:** PaulXStretch by Sonosaurus — available as a free standalone app and plugin for Windows and Mac (sonosaurus.com/paulxstretch)

### Settings That Work

| Parameter | Recommended | Effect |
|-----------|-------------|--------|
| Stretch Amount | 3x – 10x (start at 3-4x for texture, 10x+ for dissolution) | Higher = more smeared, more ambient |
| Window Size | 0.25 seconds (default) for most music; 7,000-12,000 samples for extreme stretch | Small windows = pitch artifacts; large windows = smearing |
| Internal Filter | Low-pass filter around 90Hz | Removes rumble, preserves mid/high content |
| Spread Effect | 0.571 frequency spread | Creates chorus-like texture without turning to white noise |
| Tonal vs. Noise | 0.323 preserve setting | Controls tonal character vs. textural noise quality |

### Source Material That Works Best

- **Lusher harmonic content** (orchestral, classical, piano) produces sweeping ambient textures
- Material **without drums or with drums mixed lower** stretches more smoothly — percussion becomes white noise smear at high ratios
- Vangelis-style synthesizer material is specifically recommended in community guides
- A 10-minute AI ambient track with low drones and sparse piano: stretch by 3x for a 30-minute evolving bed

### Paulstretch Workflow for This Project

1. Generate 10-minute ambient track in ElevenLabs (multiple passes if needed)
2. Import into Audacity
3. Apply Paulstretch at 3x–6x stretch ratio — produces 30–60 minutes of material
4. Apply a gentle low-pass filter around 90Hz to clean up rumble artifacts
5. Export as WAV, then create a seamless loop (see Section 4)

**Alternative approach (layering):** Record the Paulstretched output as a separate track, then layer it under the original unprocessed material at -6 to -10 dB. The original provides clarity; the stretched version provides depth and atmosphere.

---

## 4. Creating Seamless Loops

### The Core Loop Problem

A 10-20 minute piece looping for a 90-minute episode must not audibly reset. The listener should not be able to detect the loop point. There are two reasons loop points become audible: waveform discontinuity (the end amplitude doesn't match the start) and tonal discontinuity (the texture at the end doesn't sound like the texture at the beginning).

### The Reorder Method (Best for Ambient Content)

This technique from professional game audio avoids both problems:

1. Locate a point roughly one-quarter from the **end** of the audio — this becomes your split point.
2. Separate the audio into two regions at that point.
3. **Swap the order:** move the first region (beginning of the original) to follow the second region (the end of the original). You now have: [End section] [Beginning section].
4. Find a point where the **amplitude and tonal quality** of both sections are similar — this becomes your crossfade zone.
5. Apply a crossfade across that boundary.
6. The result begins mid-texture (not at a fade-in) and ends mid-texture (not at a fade-out), making the loop point inaudible.

### Crossfade Length Specifications

| Content Type | Crossfade Length |
|-------------|-----------------|
| Ambient/drone beds | 2–5 seconds (allows slow tonal blend) |
| Standard ambient music | 0.5–1 second |
| Low-frequency rumbles | 30–50ms minimum at endpoints |
| High-frequency elements | 10–20ms at endpoints |

For ambient content, err toward longer crossfades (2-5 seconds). The slower the music, the more time is needed to blend invisibly.

### Step-by-Step in Audacity

1. Import the loop candidate file.
2. Select all, duplicate the track (Edit > Duplicate).
3. On the duplicate track, use the Clip Handle to offset it so it overlaps the original by 2-5 seconds at the end.
4. Select the overlapping region.
5. Effect > Fading > Crossfade Tracks — Audacity applies fade-out to track 1, fade-in to track 2 simultaneously.
6. Flatten (Tracks > Mix > Mix and Render).
7. Test by copy-pasting the exported file back-to-back in a new project and playing through the seam.

### Verification Method

After creating the loop, do not trust your own ears on first pass. Test by duplicating the loop clip and placing the second copy immediately after the first in Audacity, then playing through the join point three times while looking away from the screen. If you cannot predict the loop point, it passes.

### Minimum Loop Duration

For ambient content, maintain **at least 20-30 seconds** of unique content before the loop repeats — otherwise, distinctive textures within the sound become recognizably repetitive. For the Tesla Mandela Effects use case, 10-20 minutes of material before looping is ideal and will be effectively inaudible to most listeners.

---

## 5. Layering Sound Effects for Organic Soundscapes

### The Design Philosophy

The goal is that sound effects feel like they are happening in the world, not placed by an editor. This requires three things: **irregular timing, dynamic variation, and spatial placement**.

- **Irregular intervals:** Do not place effects on regular beats or time marks. Use timing like 50ms, 120ms, 250ms gaps rather than regular intervals. The irregularity reads as natural.
- **Decay rate variation:** Each recurrence of a sound should have a slightly different amplitude and reverb tail. The same effect at the same level every time = obviously placed.
- **Silence as a tool:** A 2-3 second window with no sound effects creates more tension than continuous effects. Effects that emerge from silence land harder.

### The Three-Layer Soundscape Structure

**Layer 1 — Foundation (always present):** The ambient bed. Low drone, distant texture, sustained hum. This never stops. It is the room tone of the episode.

**Layer 2 — Mid-texture (occasional, irregular):** Sounds that occur every 30 seconds to 3 minutes. Electrical crackle, distant resonance, low metallic hum shift. These make the foundation feel alive.

**Layer 3 — Event sounds (rare, pointed):** Sounds that occur at most 2-3 times per episode. A sharp crackle, a sudden tonal shift, a brief mechanical click. These signal something has changed.

### Frequency-Based Organization

- **Low (below 200Hz):** Drones, subsonic rumbles, low hum. These go in the foundation layer.
- **Mid (200Hz-2kHz):** Most human voice lives here. Keep this region clear of sound effects that compete with narration. Mid-range effects should be filtered to sit below or above speech.
- **High (above 4kHz):** Electrical crackle, distant interference, metallic shimmer. These live above speech and do not compete.

### Tools for Organic Placement in Audacity

- Use the **Envelope Tool** to draw volume automation per clip — vary each instance of a repeated effect by 1-3 dB for natural variation.
- Apply different amounts of reverb to the same effect at different appearances — closer or more distant.
- **Delay (irregular):** Effect > Delay with non-musical intervals creates smeared, unplaceable echoes.
- **Reverse + Reverb:** Reverse an electrical crackle, apply heavy reverb, then reverse again. The result is a swell that peaks and dies unnaturally — perfect for cosmic tension.

### ElevenLabs Sound Effects V2 (September 2025)

ElevenLabs SFX V2 now generates up to 30-second clips with **seamless looping built in** at 48kHz quality. Free tier requires attribution to elevenlabs.io; paid plans are commercial-use cleared.

Useful prompts for Tesla/electromagnetic atmosphere:
- "Electrical crackle, tesla coil discharge, intermittent, high voltage"
- "Low electrical hum, power transformer, industrial, continuous"
- "Distant thunder, low rumble, fading, atmospheric"
- "Metallic resonance, struck metal bowl, long decay, reverberant"
- "Radio static, shortwave interference, fragmented signal"

Generate these as 20-30 second clips, then loop them independently as Layer 2 effects, using Envelope Tool to vary their volume automation across the episode.

---

## 6. Free Sound Effect Libraries

These are all no-attribution-required for commercial use:

| Library | What It Has | Notes |
|---------|-------------|-------|
| **Freesound.org** | 685,000+ sounds; 315,000+ under CC0 | Search: "electrical hum," "tesla coil," "industrial drone," "low frequency rumble" — filter by CC0 for commercial use |
| **Shaping Waves** | 3.6GB sampler; circuits, machines, atmospheric | Free sampler; strong for industrial/mechanical |
| **Boom Library** | 7 free collections including cinematic series | Strong for dramatic, cinematic textures |
| **Bluezone Corporation** | 24+ free packs including electrical, industrial | Well-organized categories |
| **Airborne Sound** | 13 collections; industrial, thunder, ambient | Airport ambiences, industrial sounds |
| **Back Pocket Sound** | 60+ mini packs (20GB total) | Ambient field recordings |
| **Glitchmachines** | Spore (sci-fi) and Teratoma (dark atmospheric) | Specifically designed for dark/unsettling atmospheres |
| **Free To Use Sounds** | 140,000+ downloads | Field recordings worldwide |

**BBC Sound Effects:** 16,000+ professional recordings — but commercial use is **not** permitted (personal/educational/research only). Do not use for YouTube monetization without verifying current licensing terms.

**Zapsplat:** Free tier requires attribution. Good quality, but upgrade to Gold account needed for commercial no-attribution use.

---

## 7. Mixing Background Music Under Narration

### Target Levels

| Element | Target Level |
|---------|-------------|
| TTS narration (peak) | -6 dB to -12 dB |
| Background music | -18 dB to -20 dB below narration |
| Overall mix ceiling | Never exceed 0 dB; target -3 dB peak |
| YouTube dialogue target | -12 dB maximum peak |

**The W3C standard** (accessibility and intelligibility): non-speech sounds should be at least 20 dB lower than speech. At 20 dB separation, voice is perceived as 4x louder than the background.

**The BBC principle** (practical): "Viewers never complain about background music being too low, but will quickly criticize when it's too loud." When in doubt, push the music down an additional 2 dB.

### EQ: Preventing Music from Competing with Speech

Human voice occupies 250Hz to 5kHz, with critical intelligibility information concentrated in 1kHz to 4kHz.

**Cuts to make on the background music track:**
- Apply a **high-pass filter at 80-100Hz** on the narration track to remove low-frequency rumble from the TTS output.
- On the music track: apply a **narrow notch cut (Q = 2-3) of 2-4 dB** in the 2-4kHz range — this is the speech presence zone. Reducing here creates a "hole" in the music where the voice sits.
- On the music track: apply a **low-pass filter above 8kHz** if the music has high-frequency content that creates harshness against TTS audio.
- For ambient/drone beds with heavy low end: apply a **high-pass filter at 150-200Hz** on the music to reduce muddiness and prevent low-frequency masking of voice warmth.

**Audacity Compressor settings for narration leveling (from official tutorial):**
- Threshold: -12 dB (adjust to -18 dB if quiet sections are too quiet)
- Ratio: 6:1
- Attack: 0.5 seconds
- Release: 1.0 seconds
- Noise Floor: -80 dB

### Volume Automation Approach

Two methods in Audacity:

1. **Envelope Tool (preferred for ambient content):** Draw volume curves manually on the music track. Drop the music 3-6 dB during dialogue-heavy sections, let it rise slightly during longer pauses. This feels organic.
2. **Auto Duck effect:** Automatic volume reduction when narration is present. Permanent alteration — use on a duplicate track, not the original.

### YouTube Normalization Warning

YouTube applies audio normalization that alters perceived loudness on upload. Export the final mix and test it at three different device types: studio monitors, laptop speakers, and a phone speaker. Laptop and phone speakers are where most YouTube listeners are — test there specifically.

---

## 8. The Tesla / Cosmic Horror Aesthetic

### Genre Identity: Dark Documentary

The reference channels (Nexpo, LEMMiNO, Barely Sociable) share a common audio signature:

- **Music is present through most of the video** — sometimes loud, sometimes barely audible. It is not a score that swells dramatically; it is a texture that persists.
- **Calm narration over unsettling music** creates more psychological tension than urgent narration over calm music. The contrast does the work.
- **Strategic silence:** Nexpo's most effective technique is fading everything out — music, sound effects, narration — to black for a beat, then using a single sharp sound (a click, a door, a static burst) to reset attention. Use sparingly, once or twice per episode maximum.
- **LEMMiNO** composes all his own music (FL Studio) and uses Adobe Audition for narration. The music is minimal, slow-evolving, and lives in the low-mid frequency range. It never calls attention to itself.

### Signature Sounds for the Tesla Series

These specific sounds define the Tesla/electromagnetic/cosmic horror space:

**Foundation elements:**
- Low electrical hum (50Hz or 60Hz AC hum — literally the sound of electrical current)
- Subsonic drone (below 80Hz, felt more than heard)
- Distant transformers or high-voltage equipment ambience

**Periodic textures:**
- Tesla coil discharge (sharp electrical crackle with long electromagnetic tail)
- Radio interference/shortwave static (fragmented signal, partially decodable)
- Metallic resonance (struck metal sustaining into silence)
- Low mechanical rotation (motors, generators, distant machinery)

**Rare event sounds:**
- A single clean bell or resonant tone that does not resolve
- Sudden silence (the most unsettling sound in this genre)
- A human voice fragment in static that may or may not be intelligible

**What to avoid:**
- Jump-scare sounds (anything percussive and sharp)
- Music with obvious rhythm or groove
- Anything that sounds like a recognizable genre (no cinematic trailer horns, no electronic music beat drops)

### Frequency Design Principles for Cosmic Horror

The horror and dread in this genre live in two frequency zones:

**Infrasonic/subsonic (below 80Hz):** Inaudible or barely audible but physically felt. Creates unease without the listener understanding why. Keep this extremely quiet — it works at -30 dB to -40 dB under the mix.

**Adjacent semitones (dissonance):** Playing two tonal elements a semitone apart (e.g., C and C#) creates irresolvable harmonic tension. This is a specific technique used in horror sound design — the ear constantly tries to resolve the interval and cannot. Apply this principle when generating music prompts: specify "dissonant" or "atonal" rather than "minor."

**Electrical character:** Real electrical sounds (hum, crackle, discharge) carry harmonic overtones at multiples of the fundamental frequency (50Hz, 100Hz, 150Hz, etc.). This is physically distinct from synthesized drones. Freesound.org has real field recordings of electrical infrastructure — these sound more authentic than synthesized versions.

---

## 9. Open-Source and Free Tools Reference

| Tool | Purpose | Where to Get |
|------|---------|--------------|
| **Paulstretch (in Audacity)** | Extreme time-stretching without artifacts | Built into Audacity: Effect > Pitch and Tempo > Paulstretch |
| **PaulXStretch** | Standalone version + VST plugin, more control | sonosaurus.com/paulxstretch |
| **Audacity** | Full DAW for all mixing, looping, EQ work | audacityteam.org |
| **INFINILOOP (GitHub)** | Real-time local AI music generator, seamless loops | github.com/davidegat/infiniloop |
| **YuE (GitHub)** | Open-source full-song music generation (Suno-equivalent, local) | github.com/multimodal-art-projection/YuE |
| **AudioCraft (Meta, GitHub)** | PyTorch library for audio generation | github.com |
| **Freesound.org** | Sound effect library, 315,000+ CC0 sounds | freesound.org |
| **Glitchmachines Teratoma** | Dark atmospheric sound effects pack (free) | glitchmachines.com |

---

## 10. Recommended Production Workflow for This Project

Given the specific constraints (Audacity, ElevenLabs 10-minute AI music, TTS narration), here is the recommended production order:

**Step 1 — Generate ambient bed in ElevenLabs**
Use the section-by-section workflow. Generate a 30-second Intro, approve it, then continue building to 3 minutes. Repeat for a second variation. Combine for ~6 minutes of source material.

**Prompt template for Tesla/cosmic horror bed:**
> "Dark ambient instrumental, 55 BPM, D minor. Low evolving drones, metallic resonance, sparse dissonant strings, distant electrical interference. Cold cavernous reverb. No percussion, no vocals, seamless loop, no fade in/out, no reverb tails. Mystery documentary narration bed."

**Step 2 — Time-stretch in Audacity (optional)**
Import into Audacity. Apply Paulstretch at 3x stretch to turn 6 minutes into 18 minutes. Window size: 0.25 seconds. Apply gentle low-pass filter at 90Hz post-stretch to clean rumble.

**Step 3 — Create seamless loop**
Use the Reorder Method above. Find where the end and beginning have similar amplitude and tonal quality. Crossfade 2-5 seconds. Export as WAV. Test by copy-pasting back-to-back.

**Step 4 — Generate sound effects in ElevenLabs SFX V2**
Generate 6-8 individual effect clips (electrical crackle, low hum, metallic resonance, radio static). Each: 20-30 seconds. These will be placed as Layer 2 elements.

**Step 5 — Build the episode mix in Audacity**
- Track 1: TTS narration (compressed, -12 dB target peak)
- Track 2: Ambient bed loop (looped for episode duration)
- Track 3-4: Sound effect placement (irregular intervals, Envelope Tool automation)
- Music track volume: set ambient bed at -18 to -20 dB below narration
- EQ: cut 2-4 dB at 2-4kHz on music track; high-pass narration at 80Hz

**Step 6 — Test and export**
Listen on laptop speakers. Check loop seam is inaudible. Verify narration is clear at all points. Export stereo WAV.

---

## Sources

- [ElevenLabs Music Best Practices Documentation](https://elevenlabs.io/docs/overview/capabilities/music/best-practices)
- [ElevenLabs Sound Effects V2 Launch](https://blockchain.news/ainews/elevenlabs-launches-sfx-model-v2-high-quality-ai-sound-effects-with-seamless-looping-and-extended-duration)
- [AI Music Prompts Guide 2026: Suno & ElevenLabs — MusicSmith](https://musicsmith.ai/blog/ai-music-generation-prompts-best-practices)
- [Ambient Music Prompts for Suno AI — SunoPrompt](https://sunoprompt.com/music-style-genre/ambient-music-genre)
- [Suno vs Udio vs ElevenLabs: 6-Month Test — HumAI Blog](https://www.humai.blog/ai-music-creation-suno-vs-udio-vs-elevenlabs-music-my-comprehensive-experience-after-6-months-of-testing/)
- [Paulstretch — Audacity Manual](https://manual.audacityteam.org/man/paulstretch.html)
- [PaulXStretch Standalone Plugin — Sonosaurus](https://sonosaurus.com/paulxstretch/)
- [Bonobo-Style Haunting Ambience with PaulStretch — Attack Magazine](https://www.attackmagazine.com/technique/synth-secrets/bonobo-style-haunting-ambience-with-paulstretch/)
- [How to Seamlessly Loop Any Ambience Audio File — FrontierSoundFX](https://www.frontiersoundfx.com/how-to-seamlessly-loop-any-ambience-audio-file/)
- [Seamless Loop in Audacity — Game Dev Beginner](https://gamedevbeginner.com/create-looping-sound-effects-for-games-for-free-with-audacity/)
- [Audacity Narration + Background Music Tutorial](https://manual.audacityteam.org/man/tutorial_mixing_a_narration_with_background_music.html)
- [Background Music Volume — Pure Audio Insight](https://pureaudioinsight.com/blogs/content-production/background-music-volume-how-loud-should-it-be)
- [W3C Accessibility Standard — Non-Speech at -20dB](https://www.w3.org/WAI/WCAG22/Techniques/general/G56.html)
- [9 Horror Sound Design Techniques — A Sound Effect](https://www.asoundeffect.com/horror-sound-design-techniques/)
- [Sound Design for Ambient Music — Sound On Sound](https://www.soundonsound.com/techniques/sound-design-ambient-music)
- [Horror Anthology Podcast Sound Design — Krotos Audio](https://www.krotosaudio.com/horror-anthology-podcast-sound-design/)
- [Nexpo Audio Analysis — Teens in Print](https://teensinprint.com/how-nexpos-fear-of-the-deep-video-fills-you-with-dread/)
- [Free Sound Effects Libraries 2025 — Production Expert](https://www.production-expert.com/production-expert-1/free-sound-effects-2023)
- [Freesound.org](https://freesound.org/)
- [INFINILOOP GitHub — Seamless AI Loop Generator](https://github.com/davidegat/infiniloop)
- [YuE Open Source Music Generation](https://github.com/multimodal-art-projection/YuE)
- [LEMMiNO FAQ — Tools and Process](https://www.lemmi.no/faq)
