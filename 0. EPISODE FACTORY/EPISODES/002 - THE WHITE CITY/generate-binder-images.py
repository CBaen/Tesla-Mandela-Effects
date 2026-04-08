"""
Episode 002 "The White City" — Archivist Binder Image Generator
Reads the timed visual sequence, generates one Imagen 4 image per page.

Usage: python generate-binder-images.py [start_page] [end_page]
"""

import requests, base64, os, sys, json, time

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
SEQUENCE_FILE = os.path.join(EPISODE_DIR, '002-VISUAL-TIMED-SEQUENCE-v3.json')
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
    print("ERROR: No VITE_GOOGLE_VERTEX_API_KEY in .env"); sys.exit(1)

PROJECT_ID = '306596393643'
MODEL_ID = 'imagen-4.0-generate-001'
ENDPOINT = f'https://aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict?key={API_KEY}'
NEGATIVE = 'legible English text, printed words, neon glow, digital overlay, sepia, monochrome, desaturated, blurry, watermark, generic, stock photo'

with open(SEQUENCE_FILE) as f:
    data = json.load(f)
pages = data['pages']

start_page = 1
end_page = len(pages)
if len(sys.argv) >= 2: start_page = int(sys.argv[1])
if len(sys.argv) >= 3: end_page = int(sys.argv[2])

pages_to_gen = [p for p in pages if start_page <= p.get('sequence', p['page']) <= end_page]

print(f"Episode 002 — Archivist Binder Image Generator")
print(f"Pages: {start_page} to {end_page} ({len(pages_to_gen)} images)")
print(f"Output: {OUTPUT_DIR}")
print(f"Cost: ~${len(pages_to_gen) * 0.04:.2f}\n")

success = 0
for i, page in enumerate(pages_to_gen):
    seq = page.get('sequence', page['page'])
    filepath = os.path.join(OUTPUT_DIR, f"page_{seq:03d}.png")

    if os.path.exists(filepath):
        print(f"[{i+1}/{len(pages_to_gen)}] Page {seq:3d} — SKIP (exists)")
        success += 1; continue

    print(f"[{i+1}/{len(pages_to_gen)}] Page {seq:3d} | {page.get('start_timecode',''):>5s} | {page.get('section',''):16s} |", end=" ", flush=True)

    prompt = page.get('prompt', '')
    if len(prompt) > 1480: prompt = prompt[:1480]

    try:
        response = requests.post(ENDPOINT,
            headers={'Content-Type': 'application/json'},
            json={'instances': [{'prompt': prompt}],
                  'parameters': {'sampleCount': 1, 'aspectRatio': '16:9', 'negativePrompt': NEGATIVE}},
            timeout=120)
        if response.status_code != 200:
            print(f"ERROR {response.status_code}"); continue
        result = response.json()
        if result.get('predictions') and result['predictions'][0].get('bytesBase64Encoded'):
            img_bytes = base64.b64decode(result['predictions'][0]['bytesBase64Encoded'])
            with open(filepath, 'wb') as f: f.write(img_bytes)
            print(f"done ({len(img_bytes)//1024}KB)"); success += 1
        else:
            reason = result.get('predictions', [{}])[0].get('raiFilteredReason', 'unknown')
            print(f"FILTERED: {reason}")
    except Exception as e:
        print(f"ERROR: {e}")
    time.sleep(1)

print(f"\nDone: {success} generated. Images: {OUTPUT_DIR}")
