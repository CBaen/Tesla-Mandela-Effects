"""
Build v3 prompts from v2 timing data using the locked final formula.
Reads v2 sequence, applies contextual prompt template, writes v3.
"""

import json, os, random

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
V2_FILE = os.path.join(EPISODE_DIR, '001-VISUAL-TIMED-SEQUENCE-v2.json')
V3_FILE = os.path.join(EPISODE_DIR, '001-VISUAL-TIMED-SEQUENCE-v3.json')

with open(V2_FILE) as f:
    data = json.load(f)

# --- Section definitions with contextual items ---
SECTIONS = {
    "Room 3327": {
        "topic": "a 1943 hotel room death investigation",
        "items": [
            "hotel corridor photograph, brass room key, torn registration card, vintage door sign, glass specimen vial, old pocket watch",
            "hotel floor plan fragment, brass room key, faded guest log page, vintage thermometer, sealed evidence envelope, antique magnifying lens",
            "surveillance photograph of hotel exterior, worn leather wallet, aged telegram, copper wire sample, vintage light bulb, hotel matchbook",
            "hotel window photograph, brass door handle, yellowed receipt, small glass bottle with cork, vintage compass, aged fabric swatch",
            "corridor photograph at odd angle, room service menu fragment, tarnished silver spoon, aged newspaper clipping, vintage pen nib, small amber specimen",
        ]
    },
    "Smiljan": {
        "topic": "an 1856 Serbian lightning-storm birth in a mountain village",
        "items": [
            "hand-drawn topographic map of limestone plateau, pressed wildflower with geometric veins, Cyrillic diary fragment, carved wooden amulet, dried herb bundle, old compass",
            "daguerreotype of mountain village, pressed oak leaf, fragment of weather log, hand-carved bone pendant, dried lavender sprig, vintage barometer diagram",
            "sketch of farmhouse floor plan, pressed fern with unusual symmetry, aged letter in Cyrillic script, clay seal stamp, dried thyme bundle, antique thermometer",
            "valley panorama photograph, specimen of limestone rock, aged midwife's tools diagram, woven textile swatch, dried mountain flower, iron nail from old construction",
            "topographic contour drawing, pressed moth specimen, fragment of parish record, carved stone disc, dried rosemary sprig, vintage optical lens",
        ]
    },
    "Witness": {
        "topic": "independent witnesses documenting atmospheric anomalies in 1856 Serbia",
        "items": [
            "fragment of schoolteacher diary, livestock census sketch, water sample vial, pressed valley grass, aged meteorological form, vintage field compass",
            "cassette tape in clear case, handwritten interview transcript fragment, dried pressed flower, old university letterhead, vintage microphone diagram, worn leather journal cover",
            "meteorological station sketch, barometer reading chart, soil sample in glass tube, aged institutional letterhead, vintage measurement calipers, pressed leaf specimen",
        ]
    },
    "Childhood": {
        "topic": "childhood electrical phenomena and geometric visions in 1859",
        "items": [
            "pencil sketch of electrical discharge arcs, sealed bag of dark animal fur, Victorian apparatus diagram, glass vial of luminescent blue liquid, small amber specimen, copper wire coil",
            "hand-drawn diagram of static electricity, vintage Leyden jar illustration, pressed moth with geometric wing pattern, small quartz crystal, aged physics textbook page, antique brass fitting",
            "sketch of geometric vision patterns, child's tin fork taped flat, Victorian eye anatomy diagram, small prism casting spectrum, dried insect specimen, fragment of school notebook",
            "diagram of electromagnetic fields, vintage battery illustration, small mineral specimen, aged optician's lens, pressed butterfly, fragment of mathematics primer",
        ]
    },
    "Dane": {
        "topic": "childhood grief and the death of a brother in 1860s Serbia",
        "items": [
            "photograph of empty coat hook on whitewashed wall, worn leather shoe sole fragment, pressed wildflower from a grave, aged family photograph, dark wool fabric swatch, vintage iron key",
            "sketch of a farmhouse doorway, small wooden button, dried memorial flower, fragment of family Bible page, aged ink drawing of a horse, tarnished locket",
        ]
    },
    "Life": {
        "topic": "an immigrant inventor's rise and fall from Wardenclyffe to poverty",
        "items": [
            "four old copper pennies taped flat, vintage ship manifest fragment, patent diagram, aged stock certificate, newspaper headline clipping, vintage electrical plug",
            "torn blueprint of transmission tower, aged financial ledger page, photograph of demolished industrial building, vintage resistor, newspaper clipping about bankruptcy, antique drafting tool",
            "hotel address list in descending order, aged contract fragment, vintage vacuum tube, photograph of grand hotel lobby, torn engineering diagram, small brass gear",
        ]
    },
    "Pigeon": {
        "topic": "an elderly inventor and a white pigeon who visited his window for years",
        "items": [
            "warm Polaroid of white pigeon in golden window light, single white feather pressed in clear tape, iridescent crystal shard casting rainbow, anatomical bird diagram, small glass bottle with cork, dried flower",
            "photograph of pigeon on windowsill, white down feather, small prism, vintage ornithology illustration, aged breadcrumb in sealed bag, pressed park leaf",
            "sketch of pigeon wing anatomy, gray-tipped feather specimen, crystal fragment, vintage hotel window photograph, dried seed pod, small iridescent shell",
        ]
    },
    "FBI": {
        "topic": "1943 government seizure of classified scientific documents",
        "items": [
            "government memo with classification stamps and redaction bars, photograph of stacked wooden crates, red wax-sealed envelope, carbon-copy inventory form, military dog tag, tarnished badge",
            "FBI letterhead fragment with redaction bars, photograph of filing cabinets, aged inventory tag, vintage padlock, government seal impression, classified folder tab",
            "declassified document cover page, photograph of warehouse storage, official stamp impression, vintage combination lock, aged shipping label, government envelope fragment",
        ]
    },
    "Mandela": {
        "topic": "anomalies in collective memory and changes in the color of the sky",
        "items": [
            "color paint swatches comparing warm yellow to cold white, vintage sky photograph, handwritten testimony fragments, small prism, aged survey form, dried flower losing color",
            "paired photographs of sky at different color temperatures, vintage sun diagram, collection of handwritten witness statements, crystal specimen, aged calendar page, spectrum analysis chart",
            "vintage globe with unusual coloring, sky photograph clipped from magazine, handwritten timeline, small mirror fragment, pressed leaf changing color, aged psychology journal page",
        ]
    },
    "Synthesis": {
        "topic": "the parallel between a birth and a death 86 years apart with the same atmospheric signature",
        "items": [
            "paired photographs of Serbian village and New York hotel, ozone molecule diagram, timeline spanning 1856 to 1943, glass vial of clear liquid, gray-tipped feather, aged letter fragment",
            "hand-drawn circle connecting birth and death, atmospheric pressure chart, vintage clock face, iridescent crystal, hotel napkin fragment, lightning photograph",
            "map connecting Smiljan to Manhattan with red thread, comparative atmospheric readings, vintage compass, small metallic fragment from unknown origin, aged memoir page, spectrum diagram",
        ]
    },
    "Final": {
        "topic": "the unanswered question of what Nikola Tesla actually was",
        "items": [
            "collection of case file fragments layered and overlapping, vintage portrait photograph, iridescent crystal cluster, strange metallic mesh, timeline with question marks, aged wax seal",
            "many overlapping photographs and documents, strange geometric artifact, vintage scientific instrument, crystal shard, aged manuscript page in unknown script, compass pointing wrong direction",
        ]
    },
    "Interstitial": {
        "topic": "an inter-dimensional investigator's private observations between evidence sections",
        "items": [
            "strange translucent artifact casting prismatic shadow, hand-drawn map of impossible geography, pressed flower from unknown species, vintage astronomical chart, small carved stone, aged personal photograph",
            "metallic disc with unknown engravings, sketch of technology that does not exist, pressed geometric leaf, crystal vial, fragment of map showing no known continent, vintage magnifying glass",
            "carved bone fragment with spiral symbols, iridescent fabric swatch, dried specimen of impossible plant, vintage pocket mirror, fragment of hand-drawn star chart, small sealed metal container",
        ]
    }
}

def get_section(page):
    """Determine which section a page belongs to based on timing."""
    seq = page.get('sequence', page.get('page', 0))
    section_name = page.get('section', '')
    s = section_name.lower()

    if seq <= 14 or 'room 3327' in s or 'hotel' in s:
        return "Room 3327"
    elif seq <= 26 or 'smiljan' in s or 'birth' in s:
        return "Smiljan"
    elif seq <= 36 or 'witness' in s or 'katarina' in s or 'meteoro' in s or 'convergence' in s:
        return "Witness"
    elif seq <= 55 or 'childhood' in s or 'cat' in s or 'fork' in s or 'counting' in s:
        return "Childhood"
    elif seq <= 60 or 'dane' in s or 'coat' in s:
        return "Dane"
    elif seq <= 67 or 'life' in s or 'immigrant' in s or 'westinghouse' in s or 'wardenclyffe' in s:
        return "Life"
    elif seq <= 83 or 'pigeon' in s:
        return "Pigeon"
    elif seq <= 95 or 'fbi' in s or 'institutional' in s or 'seizure' in s or 'government' in s:
        return "FBI"
    elif seq <= 110 or 'mandela' in s or 'sky' in s or 'sun' in s:
        return "Mandela"
    elif seq <= 127 or 'synth' in s or 'final' in s or 'question' in s or 'return' in s:
        return "Synthesis"
    elif 'interstitial' in s.lower():
        return "Interstitial"
    else:
        return "Final"

TEMPLATE = (
    "A photo of an aged journal page, overhead flat lay, Flemish still life density. "
    "Yellowed lined paper crammed edge to edge: {items}. "
    "Dense illegible mixed-script notation in dark ink fills every gap. "
    "Dozens more items relevant to {topic}. "
    "Kodachrome vivid colors, worn tactile textures. 16:9."
)

# Build v3
for page in data['pages']:
    section = get_section(page)
    sec_data = SECTIONS.get(section, SECTIONS["Interstitial"])
    items = random.choice(sec_data["items"])
    topic = sec_data["topic"]
    page['prompt'] = TEMPLATE.format(items=items, topic=topic)

# Write v3
with open(V3_FILE, 'w') as f:
    json.dump(data, f, indent=2)

# Stats
sections_used = {}
for page in data['pages']:
    s = get_section(page)
    sections_used[s] = sections_used.get(s, 0) + 1

print(f"Written: {V3_FILE}")
print(f"Pages: {len(data['pages'])}")
print(f"\nSection distribution:")
for s, count in sorted(sections_used.items(), key=lambda x: -x[1]):
    print(f"  {s:15s}: {count} pages")

# Verify prompt lengths
lengths = [len(p['prompt']) for p in data['pages']]
print(f"\nPrompt lengths: min={min(lengths)}, max={max(lengths)}, avg={sum(lengths)//len(lengths)}")
words = [len(p['prompt'].split()) for p in data['pages']]
print(f"Word counts: min={min(words)}, max={max(words)}, avg={sum(words)//len(words)}")
