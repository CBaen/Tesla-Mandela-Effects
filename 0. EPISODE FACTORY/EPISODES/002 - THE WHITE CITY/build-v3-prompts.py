"""
Episode 002 "The White City" — Build v3 prompts from timed sequence
Uses the locked visual formula with contextual sections
"""

import json, os, random

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
WHISPER_FILE = os.path.join(EPISODE_DIR, '002-whisper.json')
V3_FILE = os.path.join(EPISODE_DIR, '002-VISUAL-TIMED-SEQUENCE-v3.json')

SECTIONS = {
    "Letter": {
        "topic": "a mysterious 1894 letter from a demolition laborer about walls that weren't what they should be",
        "items": [
            "aged letter with worn fold lines, faded sepia ink, oval water stain, small magnifying loupe, wax seal fragment, pressed paper fiber sample",
            "fragile envelope with period postmark, torn letter fragment, ink analysis chart, brass letter opener, vintage postal stamp, dried pressed flower from letter",
            "letter held in archival sleeves, fold-line damage photograph, ink composition diagram, vintage reading glasses, aged paper fragment, thread from envelope seal",
        ]
    },
    "Opening Night": {
        "topic": "the 1893 World's Columbian Exposition opening ceremony and 100000 electric lamps illuminating the White City",
        "items": [
            "panoramic photograph of illuminated White City, vintage light bulb specimen, electrical wiring diagram, torn admission ticket, silk ribbon from ceremony, aged official program fragment",
            "photograph of Court of Honor at dusk, copper wire cross-section, Westinghouse contract fragment, vintage telegraph key diagram, pressed ceremonial flower, aged newspaper announcement",
            "glass plate photograph of illuminated lagoon, vintage filament specimen in glass tube, electrical circuit diagram, torn fair program page, commemorative coin, aged blueprint of lamp placement",
        ]
    },
    "Standard Account": {
        "topic": "the official story of temporary plaster buildings designed to be demolished after six months",
        "items": [
            "cross-section diagram of staff plaster construction, wood frame photograph, calcium sulfate powder in vial, architectural specification page, construction timeline chart, wire lath specimen",
            "photograph of building under construction showing wood frame, plaster composition diagram, jute fiber sample pinned flat, vintage construction blueprint, torn specification document, aged contractor bid",
        ]
    },
    "Margaret Diary": {
        "topic": "a woman's diary entry about touching a White City column and feeling stone where plaster should be",
        "items": [
            "aged diary page with feminine handwriting, photograph of neoclassical column, small stone sample in specimen bag, pressed fair souvenir flower, vintage glove, torn admission ticket",
            "diary fragment under magnifying glass, column cross-section sketch, mineral sample, period dance card, vintage brooch, pressed leaf from Jackson Park",
        ]
    },
    "Halsted Negatives": {
        "topic": "six glass plate negatives showing completed building facades impossibly early in the construction timeline",
        "items": [
            "glass plate negative held in cotton gloves, date code magnification diagram, construction timeline with red circles, photograph of Manufactures Building facade, aged catalog card, vintage darkroom chemistry bottle",
            "glass plate fragment in archival mount, edge date code photograph, timeline discrepancy chart, vintage photographic loupe, archival finding aid page, chemical analysis of glass composition",
        ]
    },
    "Demolition": {
        "topic": "winter 1894 demolition of the largest building in the world on the Chicago lakefront",
        "items": [
            "photograph of building partially demolished against grey sky, vintage wrecking bar sketch, stone dust sample in vial, torn demolition permit, worker's leather glove, aged payroll ledger fragment",
            "demolition progress photograph, cross-section of wall layers, plaster fragment specimen, vintage tool catalog page, worn leather work boot sole, Chicago weather chart for February 1894",
        ]
    },
    "Inside Wall": {
        "topic": "a laborer discovering stone inside walls that should have been plaster, like ringing a pan and hearing a bell",
        "items": [
            "limestone cross-section specimen pinned flat, tuning fork beside stone sample, wall layer diagram showing unexpected density, vintage work glove with stone dust, acoustic resonance chart, thermal reading comparison",
            "stone core sample in glass tube, vibration frequency diagram, cross-section showing plaster over limestone, vintage chisel, density comparison chart, infrared thermal photograph of wall section",
        ]
    },
    "Missing Records": {
        "topic": "demolition documentation systematically absent from Chicago archives where it should exist",
        "items": [
            "empty archival folder with index number, photograph of museum filing cabinets, catalog search result showing no records, vintage library card stamped ABSENT, aged institutional letterhead, empty evidence envelope",
            "archival finding aid with gaps highlighted, photograph of empty shelf, catalog entry reading record not found, vintage file tab, institutional request form marked DECLINED, blank space where document should be",
        ]
    },
    "Buried City": {
        "topic": "the White City's ground floor sinking below grade as Chicago raised its streets over decades",
        "items": [
            "geological cross-section showing buried floor level, vintage street elevation survey, photograph of exposed foundation below sidewalk, soil layer diagram, vintage surveyor's transit sketch, core sample in glass tube",
            "paired photographs showing street level then and now, underground utility map of Jackson Park, soil stratification diagram, vintage city planning document, brick fragment from below grade, aged engineering survey",
        ]
    },
    "Soil Borings": {
        "topic": "1904 soil boring surveys finding cut limestone aggregate where construction records say plaster should be",
        "items": [
            "soil core sample in glass cylinder, boring location map with numbered sites, density reading chart, vintage calipers beside stone sample, engineering report cover page, geological composition diagram",
            "limestone aggregate specimen pinned to card, boring grid overlay on Jackson Park map, mineral analysis results, vintage geological hammer, typed engineering report fragment, stone density comparison chart",
        ]
    },
    "Tesla Current": {
        "topic": "Tesla's polyphase AC system running through the walls for six months and what it might have done to stone",
        "items": [
            "copper egg demonstration diagram, electromagnetic field visualization, AC waveform chart, vintage Tesla patent fragment, limestone conductivity specimen, rotating magnetic field diagram",
            "polyphase circuit diagram, photograph of electrical installation, stone conductivity test results, vintage Westinghouse catalog page, crystal resonance frequency chart, Tesla coil patent sketch",
        ]
    },
    "Museum": {
        "topic": "the Palace of Fine Arts surviving as the Museum of Science and Industry with its plaster skin removed revealing brick beneath",
        "items": [
            "paired photographs of building with and without plaster skin, brick specimen from exposed wall, vintage museum brochure, reconstruction blueprint, aged brick with plaster residue, before-and-after architectural sketch",
            "photograph of crumbling neoclassical facade revealing brick, brick fragment with mortar attached, vintage museum floor plan, restoration progress photograph, aged building survey, stone sample comparison",
        ]
    },
    "Oldest Building": {
        "topic": "the investigation asking the listener to find the oldest building on their street and look at what is below grade",
        "items": [
            "hand-drawn street map with oldest buildings circled, photograph of a foundation stone below sidewalk level, vintage brick specimen, small trowel, geological survey of urban foundations, aged city directory page",
            "photograph looking down at where a building meets the ground, foundation stone cross-section, vintage city block map, small stone sample, hand-drawn diagram of below-grade vs above-grade, aged property deed fragment",
        ]
    },
    "Synthesis": {
        "topic": "three independent sources pointing at the same anomaly in the walls of the White City from different angles",
        "items": [
            "three document fragments overlapping on the page, red thread connecting them, triangulation diagram, timeline spanning 1893 to 1904, limestone specimen, vintage Chicago map with Jackson Park circled",
            "paired evidence from Coburn and Alcott side by side, convergence diagram, density comparison chart, vintage compass, aged architectural drawing, crystal fragment from unknown origin",
        ]
    },
    "Interstitial": {
        "topic": "an inter-dimensional investigator's private notes about structures that exist in the wrong timeline",
        "items": [
            "strange translucent building material specimen unlike any known stone, hand-drawn map of impossible architecture, pressed crystalline leaf, vintage astronomical chart, carved disc with spiral pattern, aged personal photograph",
            "metallic fragment with unknown alloy composition, sketch of a building that exists in no known city, pressed geometric flower, iridescent fabric swatch, fragment of hand-drawn star chart, sealed metal container",
        ]
    },
}

def get_section(page_seconds, total_duration):
    """Map a timestamp to the narrative section."""
    pct = page_seconds / total_duration

    if pct < 0.08:
        return "Letter"
    elif pct < 0.15:
        return "Opening Night"
    elif pct < 0.22:
        return "Standard Account"
    elif pct < 0.28:
        return "Margaret Diary"
    elif pct < 0.36:
        return "Halsted Negatives"
    elif pct < 0.44:
        return "Demolition"
    elif pct < 0.52:
        return "Inside Wall"
    elif pct < 0.58:
        return "Missing Records"
    elif pct < 0.64:
        return "Buried City"
    elif pct < 0.72:
        return "Soil Borings"
    elif pct < 0.78:
        return "Tesla Current"
    elif pct < 0.84:
        return "Museum"
    elif pct < 0.90:
        return "Oldest Building"
    elif pct < 0.96:
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
    "episode": "002",
    "title": "The White City",
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
