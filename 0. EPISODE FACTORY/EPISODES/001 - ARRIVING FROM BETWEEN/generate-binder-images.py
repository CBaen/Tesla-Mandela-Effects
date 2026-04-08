"""
Episode 001 — Archivist Binder Image Generator
Reads the timed visual sequence, generates one Imagen 4 image per page.
Cost: ~$6 for 150 images on free Google credits.

Usage: python generate-binder-images.py [start_page] [end_page]
  No args = generate all 150
  python generate-binder-images.py 1 10 = generate pages 1-10 only
"""

import requests, base64, os, sys, json, time

# --- Config ---
EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
SEQUENCE_FILE = os.path.join(EPISODE_DIR, '001-VISUAL-TIMED-SEQUENCE-v3.json')
OUTPUT_DIR = os.path.join(EPISODE_DIR, 'binder-images')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Load API key ---
env_path = os.path.join('C:', os.sep, 'Users', 'baenb', 'projects', 'WARDENCLYFFE UNIFIED', '.env')
API_KEY = None
with open(env_path, 'r') as f:
    for line in f:
        if line.startswith('VITE_GOOGLE_VERTEX_API_KEY='):
            API_KEY = line.strip().split('=', 1)[1]
            break

if not API_KEY:
    print("ERROR: No VITE_GOOGLE_VERTEX_API_KEY in .env")
    sys.exit(1)

PROJECT_ID = '306596393643'
MODEL_ID = 'imagen-4.0-generate-001'
ENDPOINT = f'https://aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict?key={API_KEY}'

# --- V2.5 Binder Page Style Anchor ---
BINDER_STYLE = (
    "Extreme close-up of a single aged journal page filling the entire frame edge to edge. "
    "Yellowed paper with faint blue ruled lines, slight foxing spots, tea stains at corners, "
    "a partial coffee ring. Warm overhead lighting, paper texture visible. "
    "Hyper-realistic photograph. 16:9 aspect ratio."
)

# --- Load sequence ---
with open(SEQUENCE_FILE) as f:
    data = json.load(f)

pages = data['pages']

# --- Parse args for page range ---
start_page = 1
end_page = len(pages)
if len(sys.argv) >= 2:
    start_page = int(sys.argv[1])
if len(sys.argv) >= 3:
    end_page = int(sys.argv[2])

# Filter to requested range (by sequence number)
pages_to_generate = [p for p in pages if start_page <= p.get('sequence', p['page']) <= end_page]

def build_prompt(page):
    """Get the image generation prompt for this page."""
    # V2: prompts are pre-written with full evidence descriptions
    if 'prompt' in page and page['prompt']:
        prompt = page['prompt']
    else:
        # Fallback: build from brief (V1 behavior)
        brief = page.get('brief', '')
        prompt = f"{BINDER_STYLE} {brief}"

    # Ensure we don't exceed Imagen's ~1500 char limit
    if len(prompt) > 1480:
        prompt = prompt[:1480]

    return prompt

def generate_image(prompt, output_path):
    """Generate one image with Imagen 4."""
    response = requests.post(ENDPOINT,
        headers={'Content-Type': 'application/json'},
        json={
            'instances': [{'prompt': prompt}],
            'parameters': {'sampleCount': 1, 'aspectRatio': '16:9'}
        },
        timeout=120)

    if response.status_code != 200:
        return False, f"HTTP {response.status_code}: {response.text[:200]}"

    data = response.json()
    if data.get('predictions') and data['predictions'][0].get('bytesBase64Encoded'):
        img_bytes = base64.b64decode(data['predictions'][0]['bytesBase64Encoded'])
        with open(output_path, 'wb') as f:
            f.write(img_bytes)
        return True, f"{len(img_bytes)//1024}KB"

    reason = data.get('predictions', [{}])[0].get('raiFilteredReason', 'unknown')
    return False, f"FILTERED: {reason}"

# --- Generate ---
print(f"Episode 001 — Archivist Binder Image Generator")
print(f"Pages: {start_page} to {end_page} ({len(pages_to_generate)} images)")
print(f"Output: {OUTPUT_DIR}")
print(f"Estimated cost: ~${len(pages_to_generate) * 0.04:.2f}")
print()

success = 0
failed = 0
for i, page in enumerate(pages_to_generate):
    seq = page.get('sequence', page['page'])
    filename = f"page_{seq:03d}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Skip if already generated
    if os.path.exists(filepath):
        print(f"[{i+1}/{len(pages_to_generate)}] Page {seq:3d} — SKIP (exists)")
        success += 1
        continue

    print(f"[{i+1}/{len(pages_to_generate)}] Page {seq:3d} | {page.get('start_timecode','?'):>5s} | {page.get('evidence_type','?'):16s} |", end=" ", flush=True)

    prompt = build_prompt(page)
    ok, msg = generate_image(prompt, filepath)

    if ok:
        print(f"done ({msg})")
        success += 1
    else:
        print(f"FAILED — {msg}")
        failed += 1

    time.sleep(1)  # Rate limiting

print(f"\nDone: {success} generated, {failed} failed.")
print(f"Images: {OUTPUT_DIR}")
