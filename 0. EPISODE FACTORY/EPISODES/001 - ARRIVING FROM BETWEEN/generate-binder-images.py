"""
Episode 001 — Archivist Binder Image Generator (Gemini 3.1 Flash)
Reads the timed visual sequence, generates one image per page.

Usage: python generate-binder-images.py [start_page] [end_page]
"""

import requests, base64, os, sys, json, time

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
SEQUENCE_FILE = os.path.join(EPISODE_DIR, '001-VISUAL-TIMED-SEQUENCE-v3.json')
OUTPUT_DIR = os.path.join(EPISODE_DIR, 'binder-images')
os.makedirs(OUTPUT_DIR, exist_ok=True)

env_path = os.path.join('C:', os.sep, 'Users', 'baenb', 'projects', 'WARDENCLYFFE UNIFIED', '.env')
API_KEY = None
with open(env_path, 'r') as f:
    for line in f:
        if line.startswith('VITE_GOOGLE_VERTEX_API_KEY='):
            API_KEY = line.strip().split('=', 1)[1]
            break

if not API_KEY:
    print("ERROR: No API key"); sys.exit(1)

MODEL = 'gemini-3.1-flash-image-preview'
ENDPOINT = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'

# Gemini structured prompt — MAXIMALIST density, use available character space
PROMPT_PREFIX = """Generate an image of an obsessive inter-dimensional investigator's journal page photographed from directly above. This must overwhelm the senses with detail.

BACKGROUND: A single aged yellowed lined journal page fills the entire frame edge to edge. Coffee ring stains, foxing spots, tea stains at corners, tape residue, pushpin holes from previous arrangements. The paper is worn from handling — soft at the edges, slightly warped from moisture.

DENSITY REQUIREMENT: Every single square centimeter of the page must be covered. No bare paper visible. Objects overlap, stack, crowd each other. Items are pinned over other items. Photographs overlap documents. Specimens sit on top of handwriting. This is the work of someone manic, brilliant, and obsessive who cannot stop collecting evidence.

OBJECTS (all physically present on the page, pinned, taped, clipped, or glued): """

PROMPT_SUFFIX = """. Also scattered across every remaining gap: red thread connecting items through brass pushpins, copper paper clips holding torn scraps, dried pressed flowers and leaves, aged wax seals, antique coins from different eras, small glass vials with cork stoppers containing colored liquids, fabric swatches pinned with gold specimen pins, carved bone fragments with spiral patterns, small crystal fragments catching light with prismatic reflections, vintage postage stamps, rusted skeleton keys, magnifying loupe, compass rose, pencil stubs, ink bottles.

HANDWRITING: Dense illegible notation in dark ink fills every remaining gap between objects — not English, a mix of unknown scripts and symbols. The handwriting of someone not entirely from this dimension.

STYLE: Victorian Wunderkammer cabinet of curiosities meets crime scene evidence board meets hoarder's obsessive archive. Kodachrome vivid saturated colors against the worn aged paper. Photorealistic overhead flat lay photograph. Maximalist — every surface obscured by overlapping evidence. No readable English text anywhere. 16:9 aspect ratio."""

with open(SEQUENCE_FILE) as f:
    data = json.load(f)
pages = data['pages']

start_page = 1
end_page = len(pages)
if len(sys.argv) >= 2: start_page = int(sys.argv[1])
if len(sys.argv) >= 3: end_page = int(sys.argv[2])

pages_to_gen = [p for p in pages if start_page <= p.get('sequence', p['page']) <= end_page]

def extract_items(prompt):
    """Extract the items portion from the v3 prompt for re-wrapping in Gemini format."""
    # The v3 prompt has items between "edge to edge:" and "Dense illegible"
    if 'edge to edge:' in prompt and 'Dense illegible' in prompt:
        start = prompt.index('edge to edge:') + len('edge to edge:')
        end = prompt.index('Dense illegible')
        return prompt[start:end].strip().rstrip('.')
    # Fallback: use the middle portion
    return "photographs, documents, specimens, artifacts, diagrams, red thread, brass pins, dried flowers"

def generate_image(prompt, output_path):
    """Generate one image with Gemini 3.1 Flash Image."""
    body = {
        'contents': [{'parts': [{'text': prompt}]}],
        'generationConfig': {'responseModalities': ['image', 'text']}
    }
    response = requests.post(ENDPOINT, json=body, timeout=120)
    if response.status_code != 200:
        return False, f"HTTP {response.status_code}"

    result = response.json()
    for part in result.get('candidates', [{}])[0].get('content', {}).get('parts', []):
        if 'inlineData' in part:
            img = base64.b64decode(part['inlineData']['data'])
            with open(output_path, 'wb') as f:
                f.write(img)
            return True, f"{len(img)//1024}KB"

    # Check for safety/filter
    finish_reason = result.get('candidates', [{}])[0].get('finishReason', 'unknown')
    return False, f"no image (reason: {finish_reason})"

print(f"Episode 001 — Gemini 3.1 Flash Image Generator")
print(f"Model: {MODEL}")
print(f"Pages: {start_page} to {end_page} ({len(pages_to_gen)} images)")
print(f"Output: {OUTPUT_DIR}")
print(f"Est cost: ~${len(pages_to_gen) * 0.067:.2f}\n")

success = 0
failed = 0
for i, page in enumerate(pages_to_gen):
    seq = page.get('sequence', page['page'])
    filepath = os.path.join(OUTPUT_DIR, f"page_{seq:03d}.png")

    if os.path.exists(filepath):
        print(f"[{i+1}/{len(pages_to_gen)}] Page {seq:3d} — SKIP (exists)")
        success += 1
        continue

    print(f"[{i+1}/{len(pages_to_gen)}] Page {seq:3d} | {page.get('start_timecode',''):>5s} | {page.get('section',''):16s} |", end=" ", flush=True)

    # Build Gemini structured prompt from v3 items
    items = extract_items(page.get('prompt', ''))
    prompt = PROMPT_PREFIX + items + PROMPT_SUFFIX

    ok, msg = generate_image(prompt, filepath)
    if ok:
        print(f"done ({msg})")
        success += 1
    else:
        print(f"FAILED — {msg}")
        failed += 1

    time.sleep(1)

print(f"\nDone: {success} generated, {failed} failed. Images: {OUTPUT_DIR}")
