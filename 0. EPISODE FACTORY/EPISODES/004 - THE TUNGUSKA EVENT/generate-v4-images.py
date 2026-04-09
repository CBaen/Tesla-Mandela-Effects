"""
Episode 004 — V4 Maximalist Image Generator (Gemini 3.1 Flash)
"""
import requests, base64, os, sys, json, time

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
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

with open(os.path.join(EPISODE_DIR, 'prompts-v4-all.json'), encoding='utf-8') as f:
    data = json.load(f)
    all_pages = data.get('pages', data) if isinstance(data, dict) else data

all_pages.sort(key=lambda p: p.get('page', 0))
print(f"Loaded {len(all_pages)} pages")

start_page = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
end_page = int(sys.argv[2]) if len(sys.argv) >= 3 else len(all_pages)
pages_to_gen = [p for p in all_pages if start_page <= p['page'] <= end_page]

def generate_image(prompt, output_path):
    body = {
        'contents': [{'parts': [{'text': prompt}]}],
        'generationConfig': {'responseModalities': ['image', 'text']}
    }
    try:
        response = requests.post(ENDPOINT, json=body, timeout=180)
    except Exception as e:
        return False, f"timeout/error: {e}"
    if response.status_code != 200:
        return False, f"HTTP {response.status_code}"
    result = response.json()
    for part in result.get('candidates', [{}])[0].get('content', {}).get('parts', []):
        if 'inlineData' in part:
            img = base64.b64decode(part['inlineData']['data'])
            with open(output_path, 'wb') as f: f.write(img)
            return True, f"{len(img)//1024}KB"
    finish_reason = result.get('candidates', [{}])[0].get('finishReason', 'unknown')
    return False, f"no image ({finish_reason})"

print(f"\nEpisode 004 — V4 Generation")
print(f"Pages: {start_page}-{end_page} ({len(pages_to_gen)} images)")

success = 0
failed = 0
for i, page in enumerate(pages_to_gen):
    num = page['page']
    filepath = os.path.join(OUTPUT_DIR, f"page_{num:03d}.png")
    if os.path.exists(filepath):
        print(f"[{i+1}/{len(pages_to_gen)}] Page {num:3d} SKIP")
        success += 1
        continue
    prompt = page.get('prompt', '')
    print(f"[{i+1}/{len(pages_to_gen)}] Page {num:3d} ({len(prompt)} chars) |", end=" ", flush=True)
    ok, msg = generate_image(prompt, filepath)
    if ok:
        print(f"done ({msg})")
        success += 1
    else:
        print(f"FAILED — {msg}")
        failed += 1
    time.sleep(1)

print(f"\nDone: {success} generated, {failed} failed")
