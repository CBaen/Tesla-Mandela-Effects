"""
Episode 001 — Misspelling Scanner
Uses Google Vision API to detect text in binder images, then spell-checks it.
Outputs a report of which pages have visible English text and any misspellings.

Usage: python scan-misspellings.py
"""

import requests, base64, os, sys, json, re

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(EPISODE_DIR, 'binder-images')

# Load API key
env_path = os.path.join('C:', os.sep, 'Users', 'baenb', 'projects', 'WARDENCLYFFE UNIFIED', '.env')
API_KEY = None
with open(env_path, 'r') as f:
    for line in f:
        if line.startswith('VITE_GOOGLE_VERTEX_API_KEY='):
            API_KEY = line.strip().split('=', 1)[1]
            break

if not API_KEY:
    print("ERROR: No API key found")
    sys.exit(1)

VISION_ENDPOINT = f'https://vision.googleapis.com/v1/images:annotate?key={API_KEY}'

# Common English words that are OK even if they appear
OK_WORDS = {
    'the', 'and', 'for', 'not', 'with', 'this', 'that', 'from', 'but', 'are',
    'was', 'were', 'been', 'have', 'has', 'had', 'will', 'can', 'may', 'all',
    'one', 'two', 'three', 'room', 'hotel', 'new', 'york', 'tesla', 'jan',
    'fbi', 'top', 'secret', 'classified', 'evidence', 'case', 'file', 'item',
    'date', 'note', 'page', 'inv', 'ref', 'no', 'vol', 'doc', 'report',
}

# Simple spell check using a basic word list approach
# We're looking for words that LOOK like English but are wrong
def looks_like_english(word):
    """Check if a word looks like it's trying to be English (Latin alphabet, 3+ chars)"""
    if len(word) < 3:
        return False
    if not re.match(r'^[a-zA-Z]+$', word):
        return False
    # Check vowel ratio - English words have vowels
    vowels = sum(1 for c in word.lower() if c in 'aeiou')
    if vowels == 0:
        return False
    return True

def is_likely_misspelled(word):
    """Very basic check - flags words that look English but aren't common"""
    w = word.lower().strip('.,;:!?()-"\'')
    if len(w) < 3:
        return False
    if w in OK_WORDS:
        return False
    if not looks_like_english(w):
        return False
    # Flag anything with unusual letter combinations
    weird_combos = ['dchange', 'ttion', 'classt', 'invesi', 'rotel', 'diadiry',
                    'dyern', 'sreal', 'otone', 'conlat', 'investory', 'cleast']
    for combo in weird_combos:
        if combo in w.lower():
            return True
    return False

def scan_image(filepath):
    """Send image to Google Vision API for text detection"""
    with open(filepath, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode()

    body = {
        "requests": [{
            "image": {"content": img_b64},
            "features": [{"type": "TEXT_DETECTION", "maxResults": 50}]
        }]
    }

    response = requests.post(VISION_ENDPOINT,
        headers={'Content-Type': 'application/json'},
        json=body,
        timeout=30)

    if response.status_code != 200:
        return None, f"API error {response.status_code}"

    data = response.json()
    annotations = data.get('responses', [{}])[0].get('textAnnotations', [])

    if not annotations:
        return [], None

    # First annotation is the full detected text
    full_text = annotations[0].get('description', '')
    # Individual words with bounding boxes
    words = []
    for ann in annotations[1:]:
        word = ann.get('description', '')
        vertices = ann.get('boundingPoly', {}).get('vertices', [])
        if vertices:
            x = vertices[0].get('x', 0)
            y = vertices[0].get('y', 0)
            words.append({'word': word, 'x': x, 'y': y})

    return words, full_text

# Scan all images
print("Episode 001 — Misspelling Scanner")
print(f"Scanning {IMAGE_DIR}")
print("=" * 60)

pages_with_text = 0
pages_with_issues = 0
report = []

files = sorted([f for f in os.listdir(IMAGE_DIR) if f.endswith('.png')])
total = len(files)

for i, filename in enumerate(files):
    filepath = os.path.join(IMAGE_DIR, filename)
    page_num = filename.replace('page_', '').replace('.png', '')

    print(f"[{i+1}/{total}] {filename}...", end=" ", flush=True)

    words, full_text = scan_image(filepath)

    if words is None:
        print(f"ERROR: {full_text}")
        continue

    if not words:
        print("no text detected")
        continue

    pages_with_text += 1

    # Find English-looking words
    english_words = [w for w in words if looks_like_english(w['word'])]

    if english_words:
        word_list = [w['word'] for w in english_words]
        print(f"{len(english_words)} English words: {', '.join(word_list[:8])}")
        report.append({
            'page': page_num,
            'file': filename,
            'english_words': word_list,
            'full_text': full_text[:200] if full_text else ''
        })
        pages_with_issues += 1
    else:
        print("text detected but no English words")

print("\n" + "=" * 60)
print(f"SUMMARY")
print(f"Total pages scanned: {total}")
print(f"Pages with detected text: {pages_with_text}")
print(f"Pages with English words: {pages_with_issues}")

if report:
    print(f"\n{'=' * 60}")
    print("PAGES NEEDING REVIEW (English text detected):")
    print("=" * 60)
    for r in report:
        print(f"\n  Page {r['page']}: {r['file']}")
        print(f"  Words: {', '.join(r['english_words'][:15])}")
        if len(r['english_words']) > 15:
            print(f"  ... and {len(r['english_words']) - 15} more")

    # Save report
    report_path = os.path.join(EPISODE_DIR, '001-misspelling-report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\nFull report saved: {report_path}")
else:
    print("\nNo English text detected in any images!")

print("\nDone.")
