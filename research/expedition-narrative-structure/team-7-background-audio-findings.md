# Team 7 — Background Audio Standards for Long-Form Narrated Content

**Date:** 2026-03-17
**Scope:** 60-90+ minute narrated YouTube/podcast content. Period instrumentation (piano, strings, woodwinds), mystery/thriller mood, ADHD-compatible. No electrical/Tesla cliches.

---

## Question 1: Should long-form narrated content have background music at all?

**Short answer: Yes, but at significant deficit to voice — and music must never compete for attention.**

The research picture is nuanced. A PMC-published EEG/physiological study found that enjoyment of narrated content is often *higher with no background music* than with music. However, music increases listener engagement, long-term memory of content (+22%), and emotional intensity (+40%) when it supports rather than competes.

The critical distinction is *function*: music used as a mood bed (supporting attention, masking ambient noise, sustaining emotional register) improves retention. Music that has its own melodic interest pulls cognitive load away from narrative comprehension.

**Implication for Tesla Mandela Effects:** Period instrumentation at low level functions as mood bed, not musical performance. The listener should not consciously process it. If they notice it, it is too present.

Podcast retention data shows the largest drop-off occurs in the first 30 seconds. Background music that establishes atmosphere immediately may reduce that initial drop, but sustained presence matters less than quality of narration.

---

## Question 2: What dB level should background music sit at relative to narration?

**Standard: -18 to -20 dB below voice. Never less than -15 dB.**

The W3C WCAG 2.0 accessibility standard (G56) specifies non-speech sounds must be **at least 20 dB lower** than speech. This is the most widely cited and conservatively safe standard.

Professional audio production consensus:
- **-18 to -20 dB** below dialogue: gold standard for sustained background beds
- **-15 dB minimum**: below this threshold, music begins masking speech, especially on small speakers and mobile devices (where most YouTube is consumed)
- Integrated loudness: music should be **6-12 LU lower than dialogue** depending on prominence
- Energetic sequences (not applicable here): -8 to -12 dB
- Calm, sustained narrative beds: -20 to -25 dB

**Practical starting point:** Set music at -20 dB below narration peak. Test on phone speaker — if any word is obscured, lower further.

---

## Question 3: What frequency ranges should music avoid to not compete with speech?

**Protect the 1-4 kHz range. Cut music there; presence lives there for voice.**

Human speech intelligibility concentrates in **1,000 Hz to 4,000 Hz**. Consonants — the sounds that distinguish words from each other — cluster between 1.5 kHz and 4 kHz. This is also where the ear is most sensitive.

Practical EQ approach:
- Apply a **5-10 dB parametric cut** to the music track in the **1-4 kHz range**
- This opens a "window" for the voice without requiring additional volume reduction
- Do not cut the voice in this range — boost 3-5 dB here instead if intelligibility is a concern
- Cutting 2-5 kHz in the voice track makes vocals woolly and lifeless

**For period instrumentation specifically:**
- Piano has presence peaks around 2-4 kHz (attack/brightness) — this is exactly the conflict zone
- Strings have presence in 2-6 kHz
- Woodwinds (oboe, clarinet) have fundamental energy 250-1500 Hz but overtones into 4 kHz
- EQ cuts on the music at 2-4 kHz will reduce the most problematic competition without destroying the character of the instruments
- A gentle high-shelf roll-off on the music above 3-4 kHz will also help

---

## Question 4: How long should a background music loop be? What's the research on loop perception?

**Minimum 2-3 minutes for a loop. For 90-minute content, 5+ minutes or multiple pieces preferred.**

Loop fatigue research from game audio, workplace psychology, and studio production converges on several findings:

- **Repetition tolerance:** A loop heard 2x is generally tolerable. 3-5 repetitions is where listeners begin experiencing irritation or cognitive fatigue.
- **At 90 minutes with a 2-minute loop:** 45 repetitions. This is severely fatiguing.
- **At 90 minutes with a 5-minute loop:** 18 repetitions. Marginal.
- **At 90 minutes with a 30-minute loop:** 3 repetitions. Acceptable for ambient material with internal variation.

Workplace psychology research (confirmed 2025, retail BGM context) showed that repetitive BGM reduces employee performance and job satisfaction — the same mechanism applies to sustained listener attention.

The perception of repetition is also context-dependent: music heard *subconsciously* in the background is noticed less than music heard consciously. But once a listener locks onto a repeating phrase, they cannot un-hear it.

**Practical strategies to extend effective loop length:**
1. Use multiple pieces — 3-5 distinct beds, switched at natural narrative breaks
2. Use long-form ambient pieces (5+ minutes) with internal evolution
3. Apply subtle variation at the loop point: reverb tail bleed, slight EQ shift, filter movement
4. Layer two or more complementary loops with different cycle lengths (polyrhythmic drift prevents predictable repetition points)

**Reference ceiling:** Brian Eno's *Music for Airports* (1978) — 17-minute ambient pieces designed for indefinite repetition without fatigue. This is the format model, not pop music loops.

---

## Question 5: What do successful mystery/history YouTube channels actually use?

**LEMMiNO is the clearest reference case. Approach: custom ambient electronic compositions, not licensed music.**

LEMMiNO (David Wångstedt) — the benchmark for long-form mystery documentary YouTube — composes all his own music using FL Studio. His approach:
- Ambient and electronic soundtracks designed specifically for documentary pacing
- Subtle synth layering and drones that support narrative without melodic competition
- Music aligns with the narrative's *emotional register*, not its specific moments (non-reactive bed)
- All music released free to use on SoundCloud and a secondary YouTube channel

His music is not period-authentic — it is modern ambient — but the *function* is identical to what Tesla Mandela Effects needs: atmospheric tension without distraction.

**Wendigoon** (conspiracy/iceberg content, 2-9 hour videos): Uses ambient/drone beds. Known for sustaining attention over extreme durations. Music is functional texture, not melodic. Specific sources unclear but the approach is consistent with low-intensity ambient material.

**What these channels do NOT do:** They do not use recognizable melodic themes that repeat obviously. They do not use genre-coded music (no horror stings, no heroic swells). The music is textural.

**The applicable lesson:** The most successful long-form mystery channels treat music as acoustic environment, not accompaniment. The listener should feel the room the narrator is standing in — not hear a score.

---

## Question 6: What musical characteristics prevent a non-reactive bed from becoming annoying over 90 minutes?

**Seven characteristics of fatigue-resistant ambient beds:**

1. **Slow harmonic movement.** Few or no chord changes per minute. Sustained notes, pedal tones, drone roots. The listener has nothing to "track" melodically.

2. **Rhythmic ambiguity.** No pulse strong enough to feel like a loop endpoint. If there is no audible beat, there is no obvious repetition point to notice.

3. **Gradual evolution, not sudden change.** Slow filter sweeps, gentle dynamic swell and recession, timbre shifts over 2-3 minutes. Ambient music "breathes" — it inhales and exhales slowly.

4. **Acoustic instrumentation or acoustic simulation.** Piano with long reverb tails, bowed strings with slow bow changes, soft woodwind tones — these have natural micro-variation built in. Perfectly quantized electronic loops lack this and fatigue faster.

5. **Low density.** Silence and space are as important as sound. Sparse arrangements (solo piano line, single string layer) give the brain fewer elements to track and categorize.

6. **Low high-frequency content.** Bright, cutting sounds demand attention. Music with gentle roll-off above 4-6 kHz recedes naturally without EQ intervention.

7. **No melodic hooks.** A recognizable tune will be hummed internally by the listener, pulling cognitive resources from narration. The music should be evocative without being memorable in that way.

**For period instrumentation specifically:** 1880s-1920s parlor piano in the style of Erik Satie's Gymnopédies is the structural model — slow, non-repetitive in the obvious sense, melancholy, spacious. Satie himself called it "furniture music" (*musique d'ameublement*) — sound that exists like wallpaper, present but undemanding. That is the target.

---

## Summary Recommendations for Tesla Mandela Effects

| Parameter | Recommendation |
|-----------|---------------|
| Music vs. silence | Use music — but as acoustic environment, not accompaniment |
| Volume relative to voice | -18 to -20 dB below narration peak |
| EQ on music | Cut 5-10 dB at 2-4 kHz; gentle high-shelf roll-off above 4 kHz |
| Loop/piece length | Minimum 5 minutes per piece; 3+ distinct beds per episode |
| Musical style | Slow harmonic movement, rhythmic ambiguity, no melodic hooks |
| Instrumentation | Piano + sparse strings; Satie *Gymnopédies* register; long reverb |
| Model channels | LEMMiNO (function), Wendigoon (duration tolerance) |
| What to avoid | Recognizable themes, strong pulse, short loops, bright upper frequencies |

---

## Sources

- [Radio, Podcasts, and Music Streaming — EEG Analysis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11047838/)
- [WCAG 2.0 G56: Mixing audio so non-speech sounds are 20 dB lower](https://www.w3.org/TR/WCAG20-TECHS/G56.html)
- [Background Music Volume: How Loud Should It Be? — Pure Audio Insight](https://pureaudioinsight.com/blogs/content-production/background-music-volume-how-loud-should-it-be)
- [Top Tips for Balancing Voiceovers and Background Music — ProTunesOne](https://protunesone.com/blog/top-tips-for-balancing-voiceovers-with-background-music-in-videos/)
- [How to EQ Speech for Maximum Intelligibility — Behind The Mixer](https://www.behindthemixer.com/how-eq-speech-maximum-intelligibility/)
- [Facts about Speech Intelligibility — DPA Microphones](https://www.dpamicrophones.com/mic-university/facts-about-speech-intelligibility/)
- [How to Keep Repetition in Music Interesting — iZotope](https://www.izotope.com/en/learn/how-to-keep-repetition-in-music-interesting.html)
- [The Hidden Problem of Store BGM / 3-Hour Non-Repetitive BGM](https://www.kinonuketahito.com/2025/11/the-hidden-problem-of-store-bgm-why.html)
- [Rethinking the Audio Loop in Games — Game Developer](https://www.gamedeveloper.com/audio/rethinking-the-audio-loop-in-games)
- [Ambient Music Guide: 5 Characteristics — MasterClass](https://www.masterclass.com/articles/ambient-music-guide)
- [Ambient 1: Music for Airports — Wikipedia](https://en.wikipedia.org/wiki/Ambient_1:_Music_for_Airports)
- [LEMMiNO Background Music — SoundCloud](https://soundcloud.com/lemmino/sets/background-music)
- [LEMMiNO Music Page](https://www.lemmi.no/music)
- [LEMMiNO — Wikitubia](https://youtube.fandom.com/wiki/LEMMiNO)
- [Ideal Loop Length — Gearspace Forum](https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/1216594-ideal-length-loop.html)
