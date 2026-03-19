# Lessons Learned — Tesla Mandela Effects

Reviewed by every instance on arrival. Append-only. Keep entries atomic and actionable.

## How to Use

**On arrival:** Scan this file for patterns relevant to your current task.
**After correction:** Append a new entry. Format below. One pattern per entry. No narrative.

---

### Documentary essays are not stories
- **Pattern**: All 10 episodes scored avg 4.6/10 on thesis, 4.2/10 on dread, 2.4/10 on Tesla-as-non-human. Episodes presented information linearly toward conclusions with no twists, no narrative, no mystery.
- **Rule**: Episodes need 7-point narrative structure with 5 twist beats and 4 integration beats. Every episode needs a SITUATION (someone at risk, something unresolved), not just a TOPIC (information about a subject). Information must be structured as reveals, not dumps.
- **Why**: GL listened to Episode 001 and found it boring. The first episode is the front door — if it doesn't grab attention, the series fails. All 10 episodes approved for full rewrite.

### This is NOT a conspiracy show
- **Pattern**: Multiple instances framed the series as "conspiracy content" and structured episodes around conspiracy templates (hidden truth → suppressed evidence → government villain → revelation).
- **Rule**: This is a faux-historical documentary from a parallel timeline. Some episodes document real history, some document events from a different timeline. The Mandela Effect is the seam between timelines. The government is sometimes a player, sometimes irrelevant, sometimes unaware. Never use the word "conspiracy" to describe this series.
- **Why**: The conspiracy framing reduced the series to a genre it was never supposed to be. It limited the show to "Tesla was suppressed" when the actual vision is much broader — a documentary of a world the listener may not live in.

### The Grid is absent from all current episodes
- **Pattern**: The geometric intelligence from the old scripts (squares, enters through Tesla's birth, catalogs reality for deletion) was completely stripped from all 10 production episodes. None of the writers included it because the Production Guide never required it.
- **Rule**: Three-tier mythology system. 60% of episodes: Grid implied (background dread). 30%: Grid surfaces indirectly (witnesses describe geometry, documents mention patterns). 10%: Grid direct (dimensional deletion as the subject). The Grid is made of SQUARES (from Tesla's actual biography), not triangles.
- **Why**: The Production Guide is the source of truth for writers. If it doesn't encode the Grid, writers won't include it. The old scripts had the Grid because the writer was GL. The new scripts don't because the writer was an AI following the guide.

### No stereotypical Tesla sounds in audio design
- **Pattern**: Research team recommended electrical hum, Tesla coil discharge, radio static, metallic resonance as the series' sonic signature.
- **Rule**: Background audio must be enjoyable to listen to on its own. 1880s-1920s period instrumentation (piano, strings, woodwinds). No stereotypical Tesla/science sounds. Must be ADHD-compatible. The standard is enjoyment, not tolerance.
- **Why**: GL has ADHD. Electrical hum for 90 minutes is torture, not atmosphere. The show is about mystery and consciousness, not about Tesla's inventions.

### 3-act structure is wrong for audio-first content
- **Pattern**: Initial research recommended 3-act structure with 3 reveals for 90-minute episodes.
- **Rule**: Use 7-point hybrid structure with 5 twist beats and 4 integration beats. Audio-first content needs MORE structural density than film because the listener has no visuals to carry them through slow sections. A twist/reveal approximately every 15 minutes.
- **Why**: The 3-act middle section runs 55 minutes — too long for audio-only listeners. Research confirmed the 8-12 minute attention cycle requires structural refresh more often than 3-act provides.

### Word count is a guideline, not a ceiling
- **Pattern**: Episodes constrained to 10,000-13,000 words. Opus compressed quality to hit the word count target, sacrificing storytelling for arbitrary limits.
- **Rule**: Focus on emotional beats and great storytelling. Episodes target 10,000-16,000 words, governed by 400-paragraph limit. Never sacrifice quality for a word count.
- **Why**: GL wants maximum quality. The stories are movie-length and should be treated as movies — the runtime serves the story, not the other way around.

### 1M context changes the writing process
- **Pattern**: Episode Factory agents used condensed per-role prompt extractions because of 200K token limits. Writers couldn't read all reference files or prior episodes.
- **Rule**: Writing agents now have 1M tokens. They MUST read ALL prior episodes (anti-cloning), the FULL Production Guide, the FULL Voice Reference, and the FULL Series Bible. No more condensed prompts.
- **Why**: Condensed prompts caused writers to miss rules, clone patterns from recent episodes, and produce work that didn't follow the guide because they never read the full guide.

### Caption Key must be a separate file
- **Pattern**: Caption Key was embedded in the script file.
- **Rule**: Caption Key is its own file: ###-EPISODE_TITLE-CAPTION_KEY.md. Four artifacts per episode: Script, Caption Key, Manifest JSON, Series Bible update.
- **Why**: GL requested separation for cleaner pipeline management.

### Factual validation needs external multi-auditor process
- **Pattern**: Claude Code alone does fact-checking during pre-delivery verification.
- **Rule**: Claude Code does initial check, then critical facts must be confirmed via Claude web browser. Multiple auditors required. The Quote Rule and Attribution Rule carry legal liability.
- **Why**: Claude Code's fact-checking has limits. Training knowledge is unreliable for specific historical details (see global lessons-learned: "Training Data Is Never an Acceptable Source for Legal or Regulatory Facts").

### The narrator does not already know the answer
- **Pattern**: Writing agents produce narrators who already know where the investigation leads and manage when the listener gets to find out. This creates condescending, herding narrator behavior ("we will come back to this," "we are not going to answer that yet," "hold that number").
- **Rule**: The narrator is discovering WITH the listener. The narrator has the documents but not the meaning. The narrator is a brilliant researcher pulling threads at 2 AM, genuinely confused by what the evidence produces, questioning things INTELLIGENTLY. The narrator doesn't know the destination. The narrator's genuine curiosity pulls the listener forward. The audience is intelligent and high-brow — they will hate a narrator that talks down to them, herds them, or dangles knowledge over their heads.
- **Why**: GL said: "We only like narrators when they're just as confused and joining us and pushing the story forward." The voice of the archive has access to documents, not answers. The meaning is being discovered in real time.

### Three FORBIDDEN narrator patterns
- **Pattern**: (1) Narrator crutches: "We will come back to this," "We are not going to answer that yet." (2) Source provenance as word stretching: paragraphs about who wrote a source and where it's archived before revealing what it says. (3) Explaining after impact: following a powerful line with paragraphs about why it's powerful.
- **Rule**: (1) NEVER promise future content — if the material is compelling, the listener stays without being told to. (2) Lead with what the source SAYS, not who wrote it or where it's stored, unless the source is a character. (3) Let detonations land in silence. Don't explain what the listener just felt.
- **Why**: GL said "I hate that a lot" about crutches, "that's a cheap way to stretch words" about provenance, and these are band-aids over weak content. Fix the content, not the framing.

### The audience is intelligent and high-brow
- **Pattern**: Writing agents default to over-explaining, hand-holding, and spelling out implications.
- **Rule**: The audience is smart. They are history buffs, conspiracy researchers, and intellectually curious listeners who chose a 90-minute investigation. Trust them. Present evidence and let them draw conclusions. Never explain why something is significant — present it and let the significance work. Dumb questions from the narrator destroy credibility instantly.
- **Why**: GL specified the audience is intelligent, high-brow. Condescension causes drop-off. The show treats listeners as co-investigators, not students.

### Save scripts and caption keys as .txt in addition to .md
- **Pattern**: ElevenLabs and other apps can't read .md files.
- **Rule**: Always output both .md and .txt versions of the script and caption key. The .md is the working copy; the .txt is the upload copy. Manifest stays as .json.
- **Why**: GL's production pipeline uses ElevenLabs for TTS and other apps that require .txt input.
