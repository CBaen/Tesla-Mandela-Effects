"""
Package Episode for Wardenclyffe Desktop App
Converts timed sequence + generated images into the desktop app's Ken Burns render format.

Usage: python package-for-desktop.py
Output: 001-desktop-render.json (load into Wardenclyffe Desktop to render with Ken Burns)
"""

import json, os, random

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
EPISODE_NUM = "001"
IMAGE_DIR = os.path.join(EPISODE_DIR, 'binder-images')
SEQUENCE_FILE = os.path.join(EPISODE_DIR, f'{EPISODE_NUM}-VISUAL-TIMED-SEQUENCE-v3.json')
OUTPUT_FILE = os.path.join(EPISODE_DIR, f'{EPISODE_NUM}-desktop-render.json')

# Load timing
with open(SEQUENCE_FILE) as f:
    data = json.load(f)

pages = data['pages']

# Ken Burns type assignment based on narrative function
# Motivated motion: zoom INTO evidence during reveals, pan during transitions
KB_TYPES = ['zoom-in', 'zoom-out', 'pan-left', 'pan-right', 'pan-up', 'pan-down']

def assign_ken_burns(page, index):
    """Smart Ken Burns assignment based on narrative position."""
    section = page.get('section', '').lower()
    duration = page.get('duration_seconds', 30)

    # Intro/establishing pages: slow zoom out (show the whole page)
    if index < 3:
        return {'type': 'zoom-out', 'intensity': 0.12}

    # Final pages: slow zoom in (closing in on the question)
    if index >= len(pages) - 5:
        return {'type': 'zoom-in', 'intensity': 0.10}

    # Longer holds (30+ sec): gentle zoom in to draw viewer into detail
    if duration > 30:
        return {'type': 'zoom-in', 'intensity': 0.12}

    # Short transitional pages: pan
    if duration < 15:
        direction = random.choice(['pan-left', 'pan-right'])
        return {'type': direction, 'intensity': 0.15}

    # Alternate between zoom and pan for variety, weighted toward zoom-in
    weights = {
        'zoom-in': 40,
        'zoom-out': 15,
        'pan-left': 15,
        'pan-right': 15,
        'pan-up': 8,
        'pan-down': 7,
    }
    choices = []
    for kb_type, weight in weights.items():
        choices.extend([kb_type] * weight)

    # Avoid repeating the same type 3 times in a row
    selected = random.choice(choices)
    return {'type': selected, 'intensity': round(random.uniform(0.10, 0.18), 2)}

# Build scenes array
scenes = []
for i, page in enumerate(pages):
    seq = page.get('sequence', page.get('page', i + 1))
    img_path = os.path.join(IMAGE_DIR, f'page_{seq:03d}.png')

    if not os.path.exists(img_path):
        print(f"WARNING: Missing image {img_path}")
        continue

    scene = {
        'imagePath': os.path.abspath(img_path),
        'duration': page.get('duration_seconds', 30.0),
        'kenBurns': assign_ken_burns(page, i),
    }

    if i == 0:
        scene['isIntro'] = True

    scenes.append(scene)

# Build the full render config
render_config = {
    'scenes': scenes,
    'outputPath': os.path.join(EPISODE_DIR, f'{EPISODE_NUM}-ARRIVING_FROM_BETWEEN-KENBURNS.mp4'),
    'fps': 30,
    'resolution': {'width': 1920, 'height': 1080},
    'quality': 'high',
    'crossfade': 0.5,
}

with open(OUTPUT_FILE, 'w') as f:
    json.dump(render_config, f, indent=2)

# Stats
kb_types_used = {}
for s in scenes:
    t = s['kenBurns']['type']
    kb_types_used[t] = kb_types_used.get(t, 0) + 1

print(f"Packaged {len(scenes)} scenes for Wardenclyffe Desktop")
print(f"Output: {OUTPUT_FILE}")
print(f"\nKen Burns distribution:")
for t, count in sorted(kb_types_used.items(), key=lambda x: -x[1]):
    print(f"  {t:12s}: {count}")
print(f"\nTotal duration: {sum(s['duration'] for s in scenes):.0f}s ({sum(s['duration'] for s in scenes)/60:.1f}min)")
print(f"Crossfade: {render_config['crossfade']}s between scenes")
print(f"\nLoad {OUTPUT_FILE} into Wardenclyffe Desktop to render with Ken Burns.")
