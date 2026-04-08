"""
Episode 001 — Misspelling Scanner (Gemini 2.5 Flash Vision)
Scans all binder images for visible English text and reports misspellings.
Uses Gemini's vision to understand context, not just OCR.

Usage: python scan-misspellings-gemini.py [start] [end]
"""

import requests, base64, os, sys, json, time

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(EPISODE_DIR, 'binder-images')

env_path = os.path.join('C:', os.sep, 'Users', 'baenb', 'projects', 'WARDENCLYFFE UNIFIED', '.env')
API_KEY = None
with open(env_path) as f:
    for line in f:
        if line.startswith('VITE_GOOGLE_VERTEX_API_KEY='):
            API_KEY = line.strip().split('=', 1)[1]
            break

if not API_KEY:
    print("ERROR: No API key"); sys.exit(1)

URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}'

PROMPT = """Look at this journal page image. List ONLY clearly misspelled English words you can see.
For each misspelling, give: the word as it appears, what it likely should be, and where on the page (top/middle/bottom, left/center/right).
If there are NO clearly misspelled English words (illegible handwriting doesn't count as misspelling), say "CLEAN".
Be brief. Only flag obvious misspellings of real English words, not illegible script or non-English text."""

start = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
end = int(sys.argv[2]) if len(sys.argv) >= 3 else 150

files = sorted([f for f in os.listdir(IMAGE_DIR) if f.endswith('.png')])
files = [f for f in files if start <= int(f.replace('page_','').replace('.png','')) <= end]

print(f"Scanning {len(files)} images with Gemini 2.5 Flash...")
print(f"Output: 001-misspelling-report.json\n")

clean = 0
flagged = 0
errors = 0
report = []

for i, filename in enumerate(files):
    page_num = filename.replace('page_','').replace('.png','')
    filepath = os.path.join(IMAGE_DIR, filename)

    print(f"[{i+1}/{len(files)}] {filename}...", end=" ", flush=True)

    try:
        with open(filepath, 'rb') as f:
            img_b64 = base64.b64encode(f.read()).decode()

        body = {
            'contents': [{
                'parts': [
                    {'text': PROMPT},
                    {'inline_data': {'mime_type': 'image/png', 'data': img_b64}}
                ]
            }]
        }

        resp = requests.post(URL, json=body, timeout=60)
        if resp.status_code != 200:
            print(f"ERROR {resp.status_code}")
            errors += 1
            continue

        result = resp.json()
        text = result['candidates'][0]['content']['parts'][0]['text'].strip()

        if 'CLEAN' in text.upper() and len(text) < 50:
            print("CLEAN")
            clean += 1
        else:
            print(f"FLAGGED")
            flagged += 1
            report.append({
                'page': page_num,
                'file': filename,
                'findings': text
            })

    except Exception as e:
        print(f"ERROR: {e}")
        errors += 1

    time.sleep(1)

print(f"\n{'='*60}")
print(f"SUMMARY")
print(f"Clean: {clean} | Flagged: {flagged} | Errors: {errors}")

if report:
    # Save report FIRST before printing (in case print fails on Unicode)
    report_path = os.path.join(EPISODE_DIR, '001-misspelling-report.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nFull report saved: {report_path}")
    print(f"\nFLAGGED PAGES:")
    for r in report:
        safe_findings = r['findings'].encode('ascii', errors='replace').decode('ascii')
        print(f"\n  Page {r['page']}:")
        for line in safe_findings.split('\n')[:5]:
            print(f"    {line}")

    report_path = os.path.join(EPISODE_DIR, '001-misspelling-report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nFull report: {report_path}")
