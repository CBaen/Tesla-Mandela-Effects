"""
Retry missing images with exponential backoff for rate-limited episodes.
Usage: python retry-with-backoff.py <episode_dir>
"""
import requests, base64, os, sys, json, time

if len(sys.argv) < 2:
    print("Usage: retry-with-backoff.py <episode_dir>")
    sys.exit(1)

EPISODE_DIR = os.path.abspath(sys.argv[1])
OUTPUT_DIR = os.path.join(EPISODE_DIR, 'binder-images')

env_path = os.path.join('C:', os.sep, 'Users', 'baenb', 'projects', 'WARDENCLYFFE UNIFIED', '.env')
with open(env_path) as f:
    for line in f:
        if line.startswith('VITE_GOOGLE_VERTEX_API_KEY='):
            API_KEY = line.strip().split('=', 1)[1]
            break

MODEL = 'gemini-3.1-flash-image-preview'
ENDPOINT = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'

import glob
all_pages = []
seen = set()
for fp in sorted(glob.glob(os.path.join(EPISODE_DIR, 'prompts-v4-*.json'))):
    with open(fp, encoding='utf-8') as f:
        d = json.load(f)
    pages = d.get('pages', d) if isinstance(d, dict) else d
    for p in pages:
        if p['page'] not in seen:
            seen.add(p['page'])
            all_pages.append(p)
all_pages.sort(key=lambda p: p['page'])

# Find missing
existing = set()
for f in os.listdir(OUTPUT_DIR):
    if f.startswith('page_') and f.endswith('.png'):
        existing.add(int(f[5:8]))
missing_pages = [p for p in all_pages if p['page'] not in existing]
print(f"Missing: {len(missing_pages)} pages")

def generate(prompt, path, max_retries=5):
    body = {'contents': [{'parts': [{'text': prompt}]}], 'generationConfig': {'responseModalities': ['image', 'text']}}
    backoff = 10
    for attempt in range(max_retries):
        try:
            r = requests.post(ENDPOINT, json=body, timeout=180)
        except Exception as e:
            print(f"    timeout, sleep {backoff}s", flush=True)
            time.sleep(backoff); backoff = min(backoff * 2, 120); continue
        if r.status_code == 429:
            print(f"    429 rate limited, sleep {backoff}s", flush=True)
            time.sleep(backoff); backoff = min(backoff * 2, 120); continue
        if r.status_code != 200:
            return False, f"HTTP {r.status_code}"
        result = r.json()
        for part in result.get('candidates', [{}])[0].get('content', {}).get('parts', []):
            if 'inlineData' in part:
                img = base64.b64decode(part['inlineData']['data'])
                with open(path, 'wb') as f: f.write(img)
                return True, f"{len(img)//1024}KB"
        finish = result.get('candidates', [{}])[0].get('finishReason', 'unknown')
        return False, f"no image ({finish})"
    return False, "max retries"

success = failed = 0
for i, page in enumerate(missing_pages):
    num = page['page']
    fp = os.path.join(OUTPUT_DIR, f'page_{num:03d}.png')
    print(f"[{i+1}/{len(missing_pages)}] Page {num:3d} |", end=" ", flush=True)
    ok, msg = generate(page['prompt'], fp)
    if ok:
        print(f"done ({msg})")
        success += 1
    else:
        print(f"FAILED {msg}")
        failed += 1
    time.sleep(3)  # longer base delay to avoid rate limit

print(f"\nDone: {success} generated, {failed} failed")
