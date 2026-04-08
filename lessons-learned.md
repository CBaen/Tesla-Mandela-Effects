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

### Every fabricated character gets a real name
- **Pattern**: Fabricated sources were given initials ("R.V.") or clinical designations ("Subject K.") instead of names, making them sound like case files rather than people.
- **Rule**: Anonymous means NOT attributable to a real person. It does NOT mean initials or letter designations. Every fabricated character — witness, source, interviewee — gets a real, human-sounding name. "Katarina" not "Subject K." "Walter Simmons" not "R.V." The listener needs to hear a person, not a file number.
- **Why**: GL said "I hate initial characters." Initials sound clinical and forgettable. Names sound like people. People activate oxytocin. File numbers don't.

### The first sentence creates a NEED, not a fact
- **Pattern**: AI writing defaults to informational opening lines ("Nikola Tesla died alone in Room 3327...") that read like obituaries or news reports. These present facts. Facts can be evaluated and dismissed.
- **Rule**: The first sentence must create a need the listener cannot walk away from. "The body hadn't even grown cold yet" — whose body? Where? Why? The listener NEEDS to know. An obituary gives you information. A rocket gives you a gap you have to close.
- **Why**: GL corrected the v3 opening: "What you gave me was a fucking obituary." The first sentence earns 3 seconds. Those 3 seconds buy one paragraph. That paragraph buys 2 minutes. Each moment must outperform the last.

### Progressive commitment — never assume listener commitment
- **Pattern**: The retention curve was presented as logarithmic — earn 10 minutes and sunk cost keeps them. This is too generous and dangerous.
- **Rule**: The listener has their finger on the skip button for 90 minutes. Every sentence earns the next sentence. There is no point of earned commitment. Sunk cost gives tolerance for a slow 30 seconds, not permission for a slow 5 minutes. Boosters every 400 words. 3-5 micro-stories nested inside the macro arc.
- **Why**: GL said listeners will abandon at minute 47 just as easily as minute 2. An hour and a half needs 3-5 complete narrative arcs that open and close, each with its own hook.

### Embodied scenes, not explained information
- **Pattern**: AI writing defaults to narrator explaining Tesla's experiences ("Tesla experienced flashes of blinding light"). This informs the prefrontal cortex. It does not activate the motor cortex.
- **Rule**: Put the listener INSIDE bodies. "The fork vanished. The table vanished. His hand was holding nothing." Concrete physical detail activates the listener's motor cortex — measured, fMRI-confirmed. The brain cannot distinguish a well-described scene from a memory. Every major moment must be a SCENE the listener lives through, not a FACT the narrator explains.
- **Why**: Neuroscience research confirmed: embodied narration triggers cortisol (attention), oxytocin (empathy), and dopamine (anticipation) simultaneously. Essays produce dopamine at best. Nobody bleeds, nobody listens for 90 minutes.

### The narrator reacts, never announces
- **Pattern**: Between scenes, the narrator defaults to tour guide mode: "We are now going to examine the childhood visions." "Next we will look at..."
- **Rule**: Between scenes, the narrator REACTS to what the listener just lived through. "But look at the timing." "That doesn't add up." The narrator is thinking out loud, disturbed by the evidence, building a case in real time. Never announcing what comes next. Always responding to what just happened.
- **Why**: The Voice Reference narrator, after Bliss is electrocuted, says "History calls this the Carrington Event... They describe it as weather... But look at the timing." That's reaction, not announcement. It pulls the listener forward through genuine confusion, not managed pacing.

### Fact-check the fact-checker
- **Pattern**: Browser Claude's fact-check of Episode 001 contained errors — called Mačak at age 3 "unverifiable" when Tesla wrote "Here I was, only three years old" in a 1939 piece. Said geometric visions weren't in the memoir when Tesla described "parallel and closely spaced lines at right angles to one another." Said Trump's review was "three days" without noting the three-week elapsed time.
- **Rule**: Never trust a single fact-check pass. Always verify corrections independently before applying them to the script. The fact-checker's confidence is not evidence of accuracy. Cross-reference every correction with web search before changing the script.
- **Why**: We nearly removed the geometric vision scene — the best scene in the episode — based on a wrong fact-check. And we nearly changed "three weeks" to "three days" without understanding that both numbers describe different real things.

### Tesla's visions show vivid places, not geometric patterns
- **Pattern**: The fork scene could show either geometric squares (supported by primary source) or vivid images of real places (also supported by primary source).
- **Rule**: GL chose vivid places. Tesla sees somewhere he inhabited — a place, not a pattern. This makes him a participant in the other dimension, not just a conduit for signals. The Grid is what's left behind in THIS world where the other place pressed against ours. The geometry question follows as narrator interpretation.
- **Why**: GL said geometric patterns make Tesla "more of a conduit and less of a participant." Seeing a vivid place means he was partially THERE, which is deeper than just receiving a signal.

### Fact-check request document is a standard pipeline output
- **Pattern**: Facts were verified ad hoc during production, with no systematic document for external review.
- **Rule**: Every episode produces a fact-check request document (.md + .txt) listing every verifiable claim, its source, and what specifically needs checking. This is the document GL pastes into Claude browser for external verification. Standard pipeline output alongside Script, Caption Key, and Manifest.
- **Why**: The multi-auditor fact-check process requires a structured document. Ad hoc checking misses claims and produces inconsistent coverage.

### Fact-checkers must provide source URLs and be cross-checked
- **Pattern**: Browser Claude provided verdicts without links. When challenged, some verdicts were wrong. No way to verify without re-doing the research from scratch.
- **Rule**: Every fact-check request must require source URLs for every verdict. Two independent browser instances fact-check the same document. Then each instance reviews the OTHER's findings and sources, challenging anything that doesn't hold up. All sources saved on file for the record.
- **Why**: One fact-checker with no links is an opinion. Two fact-checkers with links challenging each other is verification. The Episode 001 geometric visions near-disaster proved a single unchecked fact-checker can destroy the best scene in the episode.

### 628 scenes per episode was based on unverified advice
- **Pattern**: Someone advised GL to generate ~628 images at 8-second intervals for a 90-minute episode. This was presented as research-backed. It was not — no study supports 8-second image change frequency for long-form narrative content.
- **Rule**: 150-200 images at 15-25 second average hold time. Variable pacing: 8-15 seconds during tension, 20-40 seconds during atmosphere. Based on academic film research (15-sec documentary average) and cognitive load studies (rapid cuts impair retention for complex narrative). The proven model for the genre.
- **Why**: 628 images meant 80%+ were generic atmospheric filler with no story connection. GL described them as "random B-roll that doesn't enhance the story." Fewer images with more intention per image produces better results at lower cost ($8-12 vs unpredictable).

### AI image reference consistency does not work across style transformations
- **Pattern**: Attempted to use FLUX Kontext (fal.ai) and Google Imagen 3 capability-001 to preserve subject identity (feathers) across different artistic contexts (Polaroid, pencil sketch, X-ray). FLUX Kontext completely failed. Google Imagen 3 partially worked for simple compositions but failed for complex transformations.
- **Rule**: Do not rely on reference images for cross-style consistency. Use detailed descriptive prompting instead. Always explicitly describe recurring evidence items ("three gray-tipped pigeon feathers, 12 cm, barbs intact, spacing identical") rather than referencing a master image. Reserve Imagen 3 subject references only for evidence-directly-on-page compositions where both the prompt and the reference align on context.
- **Why**: Current AI image generators cannot reliably maintain subject identity across rendering style changes. The model prioritizes the creative transformation prompt over the reference image when they conflict. Descriptive prompting is more reliable and cheaper.

### The visual narrator concept (The Archivist) solves multiple production problems simultaneously
- **Pattern**: Previous visual approaches failed because they required 628 consistent images in a single photorealistic style. Style drift, reference mismatches, and generic B-roll resulted.
- **Rule**: Frame all images as pages from an inter-dimensional investigator's evidence binder. This makes visual inconsistency a feature (different evidence types from different dimensions), eliminates the need for photorealistic consistency, justifies mixed media, and creates I Spy density naturally. Every prompt starts with the binder page description, then describes the specific evidence.
- **Why**: The Archivist concept unifies visual identity without requiring technical consistency. It also adds a second narrative layer (who collected this evidence?) that enriches the series without conflicting with the standalone episode rule.

### Imagen 4 prompts must be under 60 words
- **Pattern**: Long prompts (100+ words) caused Imagen to render prompt text literally in the image. The word "MAXIMALIST" appeared as visible text. English words appeared misspelled throughout.
- **Rule**: Keep all image generation prompts under 60 words. Use dense noun-adjective phrases, not narrative sentences. Use "Flemish still life density" as density trigger instead of "MAXIMALIST." Structure: subject → scene → style → lighting → mood.
- **Why**: Confirmed by Google Dev Forum as known behavior with imagen-4.0-generate-001. Long contextual prompts are treated as visual content to render, not creative guidance to follow.

### Use negative prompts to prevent English text and sepia bias
- **Pattern**: Imagen defaulted to warm sepia tones when given aged/vintage keywords, and rendered English words with persistent misspellings ("Electricd Dischange", "Cleastitied").
- **Rule**: Every Imagen 4 API call must include negativePrompt in the parameters object: "legible English text, printed words, neon glow, digital overlay, sepia, monochrome, desaturated, blurry, watermark, generic, stock photo". All handwriting should be described as "illegible mixed-script notation" — never ask for readable English.
- **Why**: Negative prompts effectively suppress both the sepia color bias and the text rendering. AI image generators cannot spell reliably. Describing writing as illegible mixed scripts makes misspelling impossible since there's no correct version.

### Contextual filler items prevent visual repetition across 150 pages
- **Pattern**: Fixed item lists (crystals, keys, wax seals, fabric swatches) in every prompt would create 150 pages that all look the same.
- **Rule**: Name 6-8 specific items relevant to the current narrative section, then add "dozens more items relevant to [topic]" to let Imagen fill contextually. Change the items AND the topic per section. "Relevant to a 1943 hotel death" produces different filler than "relevant to an 1856 Serbian birth."
- **Why**: GL caught that fixed lists would make every page look identical. The topic description does the heavy lifting — it tells Imagen what KIND of objects to generate without specifying each one.

### "Kodachrome" triggers vivid color in Imagen 4 against aged backgrounds
- **Pattern**: Aged paper descriptions ("yellowed", "vintage", "antique") caused Imagen to default to monochrome sepia palette even for items taped onto the page.
- **Rule**: Include "Kodachrome vivid colors" in every prompt alongside aged page descriptions. This splits the palette: aged background + vivid foreground items. Also name specific color contrasts when needed: "warm Polaroid", "luminescent blue liquid", "iridescent crystal."
- **Why**: Imagen responds to film stock names as color triggers. "Kodachrome" overrides the sepia bias for foreground elements while allowing the page itself to remain aged.

### Imagen 4 is deprecated June 30, 2026 — switch to Gemini 3.1 Flash Image
- **Pattern**: Imagen 4 misspelled English in 82% of generated images despite negative prompts. Also approaching end-of-life.
- **Rule**: Use Gemini 3.1 Flash Image (`gemini-3.1-flash-image-preview`) via the Generative Language API. ~90% text accuracy, ~$0.067/image. Different API format than Imagen — uses `generateContent` with `responseModalities: ['image', 'text']`. Backup options: Ideogram V3 on fal.ai ($0.03-0.09), Recraft V3 on fal.ai ($0.04).
- **Why**: GL tested all available models side by side. Gemini 3.1 Flash was "BY FAR the highest quality" with correct text and better maximalism. Imagen 4 officially deprecated June 30, 2026.

### Binder pages follow the SCRIPT, not the location
- **Pattern**: 30 pages were assigned to "Room 3327" as a location-based group. This produced 30 images of the same room that didn't move the story forward.
- **Rule**: Each page must match the NARRATIVE BEAT at that timestamp. The narrator says something new every 15-30 seconds. The image must match what's NEW. Never assign pages by location — assign by what the narrator is revealing at that moment.
- **Why**: GL caught that 30 pages of the same room is "the same shit over and over." The images tell a parallel visual mystery that progresses alongside the audio. Both stories must move forward. Neither repeats.

### Every binder page needs TWO layers: investigation + personal mess
- **Pattern**: Pages were designed as clean evidence boards — organized investigation displays. This doesn't match the Archivist character.
- **Rule**: Every page has (1) evidence relevant to the current narrative beat AND (2) the Archivist's own personal belongings crammed in alongside — transit passes from impossible cities, snack wrappers in non-existent languages, personal photos of unknown people, trinkets with zero investigative relevance. The Archivist is a manic hoarder-slob who carries everything in the binder.
- **Why**: The viewer can't tell which items are clues and which are personal junk. That ambiguity IS the visual mystery. The Archivist's character bleeds through the evidence, and the audience has no idea who this person is.

### Use the FULL prompt character budget — describe what a camera would SEE
- **Pattern**: Prompts used 500-2000 characters when Gemini accepts ~8000. Images lacked detail because the model wasn't told enough.
- **Rule**: Every character in the prompt must describe something PHYSICAL and VISIBLE. Material, color, condition, position. No abstract language ("the air of absence"), no poetry, no mood descriptions. Describe every object: "a brass skeleton key with green patina taped flat with yellowing cellophane at a 15-degree angle across the lower-left corner of a torn registration card." Use 4000-8000 characters per prompt.
- **Why**: GL demanded maximalist detail that overwhelms the senses. Short prompts produce generic images. The model can only render what you describe — every unspent character is visual detail left on the table.
