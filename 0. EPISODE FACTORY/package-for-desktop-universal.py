"""
Universal Package for Wardenclyffe Desktop — handles any episode.

Usage: python package-for-desktop-universal.py <episode_dir> <episode_num> <episode_slug>
Example: python package-for-desktop-universal.py "EPISODES/002 - THE WHITE CITY" 002 THE_WHITE_CITY

- Loads all prompts-v4-*.json files from episode_dir
- Uses timestamp_start/timestamp_end for scene durations
- Assigns Ken Burns based on narrative position
- Outputs ###-desktop-render.json
"""
import json, os, sys, glob, random

if len(sys.argv) < 4:
    print("Usage: package-for-desktop-universal.py <episode_dir> <episode_num> <episode_slug>")
    sys.exit(1)

EPISODE_DIR = os.path.abspath(sys.argv[1])
EPISODE_NUM = sys.argv[2]
EPISODE_SLUG = sys.argv[3]
IMAGE_DIR = os.path.join(EPISODE_DIR, 'binder-images')
OUTPUT_FILE = os.path.join(EPISODE_DIR, f'{EPISODE_NUM}-desktop-render.json')

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
print(f"Whisper total: {whisper_total:.1f}s" if whisper_total else "No whisper")
print(f"Uniform duration per page: {uniform_duration:.2f}s")

def assign_ken_burns(idx, total, duration):
    if idx < 3:
        return {'type': 'zoom-out', 'intensity': 0.12}
    if idx >= total - 5:
        return {'type': 'zoom-in', 'intensity': 0.10}
    if duration > 30:
        return {'type': 'zoom-in', 'intensity': 0.12}
    if duration < 15:
        return {'type': random.choice(['pan-left', 'pan-right']), 'intensity': 0.15}
    weights = {'zoom-in': 40, 'zoom-out': 15, 'pan-left': 15, 'pan-right': 15, 'pan-up': 8, 'pan-down': 7}
    choices = []
    for t, w in weights.items():
        choices.extend([t] * w)
    return {'type': random.choice(choices), 'intensity': round(random.uniform(0.10, 0.18), 2)}

scenes = []
missing = []
for i, page in enumerate(all_pages):
    num = page['page']
    img_path = os.path.join(IMAGE_DIR, f'page_{num:03d}.png')
    if not os.path.exists(img_path):
        missing.append(num)
        continue
    # Prefer per-page timestamps if present; otherwise use whisper-derived uniform
    ts_start = page.get('start_sec', page.get('timestamp_start'))
    ts_end = page.get('end_sec', page.get('timestamp_end'))
    if ts_start is not None and ts_end is not None:
        duration = max(5.0, float(ts_end) - float(ts_start))
    else:
        duration = uniform_duration
    scene = {
        'imagePath': os.path.abspath(img_path),
        'duration': round(duration, 2),
        'kenBurns': assign_ken_burns(i, len(all_pages), duration),
    }
    if i == 0:
        scene['isIntro'] = True
    scenes.append(scene)

render_config = {
    'scenes': scenes,
    'outputPath': os.path.join(EPISODE_DIR, f'{EPISODE_NUM}-{EPISODE_SLUG}-KENBURNS.mp4'),
    'fps': 30,
    'resolution': {'width': 1920, 'height': 1080},
    'quality': 'high',
    'crossfade': 0.5,
}

with open(OUTPUT_FILE, 'w') as f:
    json.dump(render_config, f, indent=2)

kb_used = {}
for s in scenes:
    t = s['kenBurns']['type']
    kb_used[t] = kb_used.get(t, 0) + 1

total_dur = sum(s['duration'] for s in scenes)
print(f"Packaged {len(scenes)} scenes -> {OUTPUT_FILE}")
print(f"Total duration: {total_dur:.0f}s ({total_dur/60:.1f}min)")
print(f"Ken Burns: {kb_used}")
if missing:
    print(f"MISSING IMAGES (pages): {missing}")
