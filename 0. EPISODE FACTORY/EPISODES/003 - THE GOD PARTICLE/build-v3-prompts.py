"""
Episode 003 "The God Particle" — Build v3 prompts from whisper timing data
Uses the locked visual formula with contextual sections mapped to narrative arc
"""

import json, os, random

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
WHISPER_FILE = os.path.join(EPISODE_DIR, '003-whisper.json')
V3_FILE = os.path.join(EPISODE_DIR, '003-VISUAL-TIMED-SEQUENCE-v3.json')

SECTIONS = {
    "Opening": {
        "topic": "collective memory anomalies — millions of adults who remember a childhood name differently than the publisher's records show",
        "items": [
            "aged children's book cover photograph with ambiguous spine lettering, handwritten memory testimony fragment, vintage cognition study diagram, pencil-marked survey form, dried pressed book page, small amber specimen",
            "publisher's catalog page with highlighted title, handwritten recollection note fragment, cognitive encoding diagram, survey response clipping, vintage memory research letterhead, pressed paper fiber sample",
            "photograph of bookshelves at odd angle, torn survey form with written responses, neural encoding chart, handwritten testimony with underline, vintage psychology journal fragment, small crystalline specimen",
        ]
    },
    "CERN Founded": {
        "topic": "the European Organization for Nuclear Research — twelve founding nations, a site straddling the Franco-Swiss border, the construction of a twenty-seven-kilometer ring buried one hundred meters underground",
        "items": [
            "aerial photograph of circular ring outline in farmland, twelve-nation founding charter fragment, Franco-Swiss border survey map, tunnel cross-section engineering diagram, superconducting magnet blueprint, vintage CERN letterhead",
            "map of Geneva with ring overlay, treaty document fragment with twelve signatures, underground tunnel schematic, magnet assembly photograph, particle beam path diagram, aged institutional funding document",
            "LHC ring circumference diagram, founding document corner fragment, French-Swiss border marker photograph, tunnel boring machine schematic, proton beam path illustration, construction timeline chart",
        ]
    },
    "Selassie First": {
        "topic": "a calibration engineer monitoring background electromagnetic fields during the LHC's first beam run on September 10 2008 — instruments showing 7.9 hertz where the floor should be 7.83",
        "items": [
            "electromagnetic field calibration chart with 7.9 Hz circled, control room monitoring screen photograph, frequency anomaly log printout, calibration engineer shift schedule fragment, instrument array diagram, operational log page",
            "frequency deviation graph with annotated baseline, CERN sector map showing three-four, calibration instrument diagram, operational log with handwritten note, monitoring screen photograph, shift record fragment",
            "ambient field measurement chart, calibration log printout with anomaly noted, sector three-four schematic, instrument calibration certificate, monitoring timeline, frequency comparison diagram",
        ]
    },
    "Helium Explosion": {
        "topic": "the September 19 2008 liquid helium explosion that destroyed fifty-three magnets and shut down the LHC — a pre-incident memo logged nine minutes before, noting the 7.9 Hz anomaly from first beam",
        "items": [
            "RESTRICTED internal memo with INTERNAL USE ONLY stamp, damaged magnet cross-section photograph, helium venting damage diagram, pre-incident documentation batch, incident timeline chart, magnet repair cost ledger fragment",
            "institutional memo with classification header, LHC sector damage map, cryogenic explosion schematic, pre-incident operational log page, helium isotope specimen vial, engineering damage assessment fragment",
            "stamped RESTRICTED memo fragment, photograph of tunnel damage aftermath, liquid helium containment diagram, operational log timestamped before incident, magnet replacement timeline, institutional investigation report cover",
        ]
    },
    "Colorado Springs": {
        "topic": "Tesla's 1899 magnifying transmitter experiment in Colorado Springs — a 9-meter primary coil striking the Earth like a bell and discovering the planet's resonant frequency of approximately 8 hertz",
        "items": [
            "Tesla coil schematic with nine-meter diameter notation, Colorado Springs laboratory photograph, ozone smell sensation note fragment, 135-foot lightning bolt discharge diagram, Earth resonance wave illustration, battery-powered instrument reading chart",
            "magnifying transmitter blueprint fragment, Colorado altitude barometric pressure chart, arc discharge photograph, standing wave propagation diagram, El Paso Electric Company grid failure record, laboratory floor plan sketch",
            "large-scale coil winding diagram, Colorado Springs topographic map with laboratory site marked, lightning channel photograph, frequency measurement log page, Earth conductivity diagram, oscillation instrument reading",
        ]
    },
    "Schumann": {
        "topic": "three independent measurements of the Earth's resonant frequency across one hundred and nine years — Tesla 1899, Schumann 1952, and the LHC's calibration instruments in 2008 — all finding the same register",
        "items": [
            "three frequency measurement charts layered side by side, Schumann resonance derivation equation fragment, 1899-1952-2008 timeline diagram, ionosphere cavity cross-section illustration, measurement comparison chart with three columns, vintage physics journal page",
            "frequency convergence diagram showing three independent readings, Schumann mathematical derivation fragment, Earth-ionosphere cavity schematic, timeline spanning 109 years, instrument comparison table, aged physics letterhead",
            "overlapping frequency charts from three different instruments and eras, Schumann resonance formula fragment, global cavity resonance illustration, measurement log comparison, timeline with three circled dates, physics diagram with annotated margins",
        ]
    },
    "False Floor": {
        "topic": "the false floor of the investigation — the Mandela Effect community forming in 2009, LHC operational calendar correlation, reporting spikes aligned with Run 1 and Run 2 milestones",
        "items": [
            "two overlapping datasets with correlation lines drawn, LHC operational calendar with highlighted run dates, Mandela Effect forum archive timestamp fragment, statistical correlation chart, laptop screen photograph at research desk, data overlay diagram",
            "side-by-side dataset comparison chart, CERN run schedule fragment with circled dates, forum report volume graph, correlation coefficient notation, researcher's desk photograph, timeline alignment diagram",
            "statistical correlation chart with spike annotations, LHC calendar excerpt with Run 1 and Run 2 dates, archived forum data printout, scatter plot with trend line, dataset comparison table, analysis notes fragment",
        ]
    },
    "Selassie Letter": {
        "topic": "a letter on CERN internal stationery from a former calibration engineer — four years of privately logged anomaly data showing readings that correlate with the LHC's firing schedule, a shape that is not random",
        "items": [
            "CERN institutional stationery with PERSONAL — NOT FOR DISTRIBUTION handwritten above letterhead, water-stained third page fragment, blue spiral notebook cover, private anomaly log with dated entries, formal anomaly report IM-34 form, photocopy of three-page letter",
            "letter on institutional letterhead showing CERN logo, partially legible third page, spiral notebook entry fragment, four-year observation log table, anomaly report stamp WITHIN TOLERANCE, hand-folded multi-page letter",
            "CERN letterhead fragment with handwritten notation, water stain across letter page lower third, spiral notebook blue cover with handwritten dates, private log frequency column, closed institutional anomaly report, letter fold-crease photograph",
        ]
    },
    "Wardenclyffe": {
        "topic": "the July 4 1917 demolition of Tesla's Wardenclyffe Tower — dynamite fired at the root system that extended 300 feet into Long Island bedrock, the tower suspended mid-fall before the earth released its grip",
        "items": [
            "Wardenclyffe tower demolition photograph with tower mid-lean, root system cross-section diagram showing 300-foot depth, Smiley Steel Company contract fragment, July 4 1917 demolition foreman report page, iron pipe specimen from root system, copper hemisphere schematic",
            "tower silhouette photograph at demolition angle, underground root system depth diagram, dynamite placement schematic, Long Island bedrock cross-section, Waldorf-Astoria mortgage document fragment, crater exposed root photograph",
            "photograph of tower in intermediate fall position, iron pipe cross-section specimen, demolition permit fragment dated 1917, root system anchor diagram, scrap metal appraisal document, tower base foundation photograph",
        ]
    },
    "July Fourth": {
        "topic": "July 4 2012 — the Higgs boson confirmation at CERN and the Tromsø Geophysical Observatory baseline shift — ninety-five years to the day from the Wardenclyffe demolition",
        "items": [
            "five-sigma statistical curve from Higgs announcement, Tromsø observatory monitoring log with July 4 margin annotation, 95-year timeline from 1917 to 2012, Higgs field diagram, Norwegian monitoring station photograph, Peter Higgs attendance record fragment",
            "particle physics discovery curve with five-sigma threshold marked, Norwegian monitoring log with handwritten margin note, timeline diagram July 4 1917 to July 4 2012, CERN auditorium photograph, magnetometer reading chart, Higgs boson confirmation press release fragment",
            "statistical significance curve photograph, Tromsø station log open to July 4 entry, 95-year calendar diagram with both dates circled, Higgs field quantum excitation illustration, observatory instrument photograph, discovery announcement cover page",
        ]
    },
    "Synthesis": {
        "topic": "the electromagnetic substrate that Tesla found in 1899 and CERN operates within unknowingly — the question of which version of the baseline made you",
        "items": [
            "Colorado Springs oscillation field survey report footnote, memory encoding electromagnetic diagram, Schumann resonance substrate illustration, CERN frequency baseline chart, fossil record analogy diagram, question mark beside frequency comparison table",
            "geological survey footnote about ground remembering, brain electromagnetic activity diagram, Earth resonant substrate cross-section, all four frequency readings overlaid, frequency floor shift illustration, aged personal photograph beside measurement chart",
            "survey report footnote fragment, memory-as-fossil-record diagram, electromagnetic floor shift visualization, overlapping frequency charts from 1899 to 2015, Colorado Springs archive document, final question as handwritten notation on journal page",
        ]
    },
    "Interstitial": {
        "topic": "an inter-dimensional investigator's private observations about frequencies that persist after the machines that found them are gone",
        "items": [
            "strange translucent artifact casting prismatic shadow, hand-drawn map of impossible geography, pressed flower from unknown species, vintage astronomical chart, small carved stone, aged personal photograph",
            "metallic disc with unknown engravings, sketch of technology that does not exist, pressed geometric leaf, crystal vial, fragment of map showing no known continent, vintage magnifying glass",
            "carved bone fragment with spiral symbols, iridescent fabric swatch, dried specimen of impossible plant, vintage pocket mirror, fragment of hand-drawn star chart, small sealed metal container",
        ]
    },
}

def get_section(page_seconds, total_duration):
    """Map a timestamp to the narrative section based on story arc percentage."""
    pct = page_seconds / total_duration

    if pct < 0.08:
        return "Opening"
    elif pct < 0.18:
        return "CERN Founded"
    elif pct < 0.26:
        return "Selassie First"
    elif pct < 0.34:
        return "Helium Explosion"
    elif pct < 0.46:
        return "Colorado Springs"
    elif pct < 0.54:
        return "Schumann"
    elif pct < 0.62:
        return "False Floor"
    elif pct < 0.72:
        return "Selassie Letter"
    elif pct < 0.82:
        return "Wardenclyffe"
    elif pct < 0.90:
        return "July Fourth"
    elif pct < 0.97:
        return "Synthesis"
    else:
        return "Interstitial"

TEMPLATE = (
    "A photo of an aged journal page, overhead flat lay, Flemish still life density. "
    "Yellowed lined paper crammed edge to edge: {items}. "
    "Dense illegible mixed-script notation in dark ink fills every gap. "
    "Dozens more items relevant to {topic}. "
    "Kodachrome vivid colors, worn tactile textures. 16:9."
)

# --- Load whisper and build timed sequence ---
print("Loading Whisper transcription...")
with open(WHISPER_FILE) as f:
    whisper = json.load(f)

duration = whisper['duration']
segments = whisper['segments']
print(f"Duration: {duration:.1f}s ({duration/60:.1f}min), {len(segments)} segments")

# Build ~150 pages evenly distributed across the audio
target_pages = 150
avg_duration = duration / target_pages

pages = []
current_time = 0.0
for i in range(target_pages):
    start = current_time
    end = min(start + avg_duration, duration)
    if i == target_pages - 1:
        end = duration

    section = get_section(start, duration)
    sec_data = SECTIONS.get(section, SECTIONS["Interstitial"])
    items = random.choice(sec_data["items"])
    topic = sec_data["topic"]

    # Find narration cue at this timestamp
    cue = ""
    for seg in segments:
        if seg['start'] >= start:
            cue = seg['text'][:60]
            break

    mins = int(start // 60)
    secs = int(start % 60)

    pages.append({
        "page": i + 1,
        "sequence": i + 1,
        "start_seconds": round(start, 1),
        "end_seconds": round(end, 1),
        "start_timecode": f"{mins}:{secs:02d}",
        "end_timecode": f"{int(end//60)}:{int(end%60):02d}",
        "duration_seconds": round(end - start, 1),
        "section": section,
        "narration_cue": cue,
        "prompt": TEMPLATE.format(items=items, topic=topic)
    })

    current_time = end

# Write v3
output = {
    "episode": "003",
    "title": "The God Particle",
    "duration_seconds": duration,
    "total_pages": len(pages),
    "pages": pages
}

with open(V3_FILE, 'w') as f:
    json.dump(output, f, indent=2)

# Stats
sections_used = {}
for p in pages:
    s = p['section']
    sections_used[s] = sections_used.get(s, 0) + 1

print(f"\nWritten: {V3_FILE}")
print(f"Pages: {len(pages)}")
print(f"\nSection distribution:")
for s, count in sorted(sections_used.items(), key=lambda x: -x[1]):
    print(f"  {s:20s}: {count} pages")

lengths = [len(p['prompt']) for p in pages]
words = [len(p['prompt'].split()) for p in pages]
print(f"\nPrompt lengths: min={min(lengths)}, max={max(lengths)}, avg={sum(lengths)//len(lengths)}")
print(f"Word counts: min={min(words)}, max={max(words)}, avg={sum(words)//len(words)}")
