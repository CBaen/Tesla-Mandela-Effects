"""
Universal Package for Wardenclyffe Desktop — produces importable .zip files.

Usage: python package-for-desktop-universal.py <episode_dir> <episode_num> <episode_slug>
Example: python package-for-desktop-universal.py "EPISODES/002 - THE WHITE CITY" 002 THE_WHITE_CITY

Output: ###-EPISODE_SLUG.zip containing:
  project.json  (Wardenclyffe Desktop format)
  images/       (scene_N_16x9.png files)
"""
import json, os, sys, glob, random, uuid, zipfile

if len(sys.argv) < 4:
    print("Usage: package-for-desktop-universal.py <episode_dir> <episode_num> <episode_slug>")
    sys.exit(1)

EPISODE_DIR = os.path.abspath(sys.argv[1])
EPISODE_NUM = sys.argv[2]
EPISODE_SLUG = sys.argv[3]
IMAGE_DIR = os.path.join(EPISODE_DIR, 'binder-images')
ZIP_OUTPUT = os.path.join(EPISODE_DIR, f'{EPISODE_NUM}-{EPISODE_SLUG}.zip')

# Load all prompts-v4-*.json files
all_pages = []
seen = set()
for fpath in sorted(glob.glob(os.path.join(EPISODE_DIR, 'prompts-v4-*.json'))):
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    pages = data.get('pages', data) if isinstance(data, dict) else data
    for p in pages:
        num = p.get('page')
        if num and num not in seen:
            seen.add(num)
            all_pages.append(p)

all_pages.sort(key=lambda p: p.get('page', 0))
print(f"Loaded {len(all_pages)} pages")

# Load whisper total duration for accurate pacing
whisper_total = None
for f in os.listdir(EPISODE_DIR):
    if f.endswith('-whisper.json'):
        with open(os.path.join(EPISODE_DIR, f), encoding='utf-8') as fh:
            w = json.load(fh)
        segs = w.get('segments', [])
        if segs:
            whisper_total = segs[-1].get('end', 0)
        break

uniform_duration = (whisper_total / len(all_pages)) if whisper_total and all_pages else 30.0
print(f"Whisper total: {whisper_total:.1f}s" if whisper_total else "No whisper found")
print(f"Uniform duration per page: {uniform_duration:.2f}s")

def assign_ken_burns(idx, total, duration):
    if idx < 3:
        return {'type': 'zoom-out', 'intensity': 0.12}
    if idx >= total - 5:
        return {'type': 'zoom-in', 'intensity': 0.10}
    weights = {'zoom-in': 40, 'zoom-out': 15, 'pan-left': 15, 'pan-right': 15, 'pan-up': 8, 'pan-down': 7}
    choices = []
    for t, w in weights.items():
        choices.extend([t] * w)
    return {'type': random.choice(choices), 'intensity': round(random.uniform(0.10, 0.18), 2)}

# Build scenes in Wardenclyffe Desktop format
project_id = str(uuid.uuid4())
episode_name = f"Episode {EPISODE_NUM} - {EPISODE_SLUG.replace('_', ' ').title()}"
scenes = []
missing = []
cumulative_ms = 0

for i, page in enumerate(all_pages):
    num = page['page']
    img_path = os.path.join(IMAGE_DIR, f'page_{num:03d}.png')
    if not os.path.exists(img_path):
        missing.append(num)
        continue

    # Duration from per-page timestamps or uniform fallback
    ts_start = page.get('start_sec', page.get('timestamp_start'))
    ts_end = page.get('end_sec', page.get('timestamp_end'))
    if ts_start is not None and ts_end is not None:
        duration_sec = max(5.0, float(ts_end) - float(ts_start))
    else:
        duration_sec = uniform_duration

    scene_num = i + 1
    img_filename = f"scene_{scene_num}_16x9.png"
    scene_id = str(uuid.uuid4())
    start_ms = int(cumulative_ms)
    end_ms = int(cumulative_ms + duration_sec * 1000)

    scene = {
        'id': scene_id,
        'sceneNumber': scene_num,
        'segmentText': page.get('narrative_beat', page.get('narration_cue', page.get('cue', f'Page {num}'))),
        'imagePrompt': page.get('prompt', ''),
        'estimatedDuration': round(duration_sec, 2),
        'startMs': start_ms,
        'endMs': end_ms,
        'images': {
            '16:9': f'zip:{img_filename}'
        },
        'status': 'completed',
        'kenBurns': assign_ken_burns(i, len(all_pages), duration_sec),
        'isIntro': i == 0,
    }
    scenes.append((scene, img_path, img_filename))
    cumulative_ms = end_ms

# Build project.json
project = {
    'id': project_id,
    'name': episode_name,
    'aspectRatio': '16:9',
    'audioDuration': int((whisper_total or cumulative_ms / 1000) * 1000),
    'sceneCount': len(scenes),
    'scenes': [s[0] for s in scenes],
    'masterAssets': [],
}

# Write zip
with zipfile.ZipFile(ZIP_OUTPUT, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('project.json', json.dumps(project, indent=2))
    for scene, img_path, img_filename in scenes:
        zf.write(img_path, f'images/{img_filename}')

# Stats
kb_used = {}
for s, _, _ in scenes:
    t = s['kenBurns']['type']
    kb_used[t] = kb_used.get(t, 0) + 1

total_dur = sum(s[0]['estimatedDuration'] for s in scenes)
zip_size_mb = os.path.getsize(ZIP_OUTPUT) / (1024 * 1024)
print(f"\nPackaged {len(scenes)} scenes -> {ZIP_OUTPUT}")
print(f"ZIP size: {zip_size_mb:.1f} MB")
print(f"Total duration: {total_dur:.0f}s ({total_dur/60:.1f}min)")
print(f"Ken Burns: {kb_used}")
if missing:
    print(f"MISSING IMAGES (pages): {missing}")
print(f"\nImport this .zip into Wardenclyffe Desktop via 'Import Project'.")
