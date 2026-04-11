"""
Universal Package for Wardenclyffe Desktop — produces importable .zip files.

Usage: python package-for-desktop-universal.py <episode_dir> <episode_num> <episode_slug> [--audio <wav>]
Example: python package-for-desktop-universal.py "EPISODES/002 - THE WHITE CITY" 002 THE_WHITE_CITY

Output: ###-EPISODE_SLUG.zip containing:
  project.json  (Wardenclyffe Desktop format)
  images/       (scene_N_16x9.png files)

Source-of-truth hierarchy for scene timing:
  1. Per-episode sequence JSON ({episode_num}-VISUAL-TIMED-SEQUENCE*.json)
     Has pages[] with duration_seconds / start_seconds / end_seconds.
     This is the authoritative source. Use when present.
  2. Fallback: prompts-v4-*.json files — only have start_seconds per page,
     so durations are computed as next.start - this.start. Last page falls
     back to the whisper-derived uniform estimate.
  3. Last resort: hardcoded 30.0s per page (emits a warning).

Audio is auto-discovered under {TME root}/3. ELEVEN LABS AUDIO/01. v4 new narrator/
by episode number, or can be passed explicitly with --audio. The discovered
audio path and duration are embedded in project.json so the downstream
Wardenclyffe Desktop duration-check hook can compare video-vs-audio drift.
"""
import json, os, sys, glob, random, uuid, zipfile, wave


def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


# -------- CLI parsing (positional + optional --audio) --------
argv = sys.argv[1:]
audio_override = None
if '--audio' in argv:
    idx = argv.index('--audio')
    if idx + 1 < len(argv):
        audio_override = argv[idx + 1]
        del argv[idx:idx + 2]
    else:
        die("--audio flag requires a path argument")

if len(argv) < 3:
    print("Usage: package-for-desktop-universal.py <episode_dir> <episode_num> <episode_slug> [--audio <wav>]")
    sys.exit(1)

EPISODE_DIR = os.path.abspath(argv[0])
EPISODE_NUM = argv[1]
EPISODE_SLUG = argv[2]
IMAGE_DIR = os.path.join(EPISODE_DIR, 'binder-images')
ZIP_OUTPUT = os.path.join(EPISODE_DIR, f'{EPISODE_NUM}-{EPISODE_SLUG}.zip')


# -------- Load pages from the best available source --------
all_pages = []
sequence_used = None

# Prefer the sequence JSON — it has explicit per-page duration_seconds.
sequence_candidates = sorted(
    glob.glob(os.path.join(EPISODE_DIR, f'{EPISODE_NUM}-VISUAL-TIMED-SEQUENCE*.json')),
    key=os.path.getmtime,
    reverse=True,
)
if sequence_candidates:
    sequence_used = sequence_candidates[0]
    with open(sequence_used, encoding='utf-8-sig') as f:
        seq = json.load(f)
    all_pages = list(seq.get('pages', []))
    print(f"Using sequence JSON: {os.path.basename(sequence_used)} ({len(all_pages)} pages)")
else:
    # Legacy fallback: merge prompts-v4-*.json files.
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
    print(f"Sequence JSON not found — fell back to prompts-v4-*.json ({len(all_pages)} pages)")

if not all_pages:
    die("No pages found. Need {num}-VISUAL-TIMED-SEQUENCE*.json or prompts-v4-*.json in episode dir.")


# -------- Whisper total (fallback signal for pages missing duration/end) --------
# Match any whisper JSON (was previously `*-whisper.json`, which missed Ep001's
# `001-whisper-v2.json` / `-clean.json` / `-transcription.json` files).
whisper_total = None
whisper_found = None
for f in sorted(os.listdir(EPISODE_DIR)):
    if 'whisper' in f.lower() and f.endswith('.json'):
        try:
            with open(os.path.join(EPISODE_DIR, f), encoding='utf-8') as fh:
                w = json.load(fh)
            if isinstance(w, dict):
                if isinstance(w.get('duration'), (int, float)):
                    whisper_total = float(w['duration'])
                    whisper_found = f
                    break
                segs = w.get('segments') or []
                if segs and isinstance(segs[-1], dict):
                    end = segs[-1].get('end')
                    if isinstance(end, (int, float)):
                        whisper_total = float(end)
                        whisper_found = f
                        break
        except Exception as e:
            print(f"  (whisper candidate {f} unreadable: {e})")
            continue

if whisper_total:
    print(f"Whisper total (from {whisper_found}): {whisper_total:.1f}s")
else:
    print("No whisper found in episode dir")

uniform_fallback = (whisper_total / len(all_pages)) if whisper_total else 30.0


# -------- Audio discovery (optional, for drift-check metadata) --------
def find_tme_root(start):
    """Walk up looking for the '3. ELEVEN LABS AUDIO' sibling."""
    cur = os.path.abspath(start)
    for _ in range(6):
        if os.path.isdir(os.path.join(cur, '3. ELEVEN LABS AUDIO')):
            return cur
        nxt = os.path.dirname(cur)
        if nxt == cur:
            break
        cur = nxt
    return None


audio_path = None
audio_duration_sec = None

if audio_override:
    if os.path.isfile(audio_override):
        audio_path = os.path.abspath(audio_override)
    else:
        print(f"WARNING: --audio override path not found: {audio_override}")

if not audio_path:
    tme_root = find_tme_root(EPISODE_DIR)
    if tme_root:
        audio_dir = os.path.join(tme_root, '3. ELEVEN LABS AUDIO', '01. v4 new narrator')
        if os.path.isdir(audio_dir):
            # Sorted so a v5/v6 variant wins over v4 alphabetically.
            candidates = sorted(glob.glob(os.path.join(audio_dir, f'ElevenLabs_{EPISODE_NUM}-*.wav')))
            if candidates:
                audio_path = candidates[-1]

if audio_path:
    try:
        with wave.open(audio_path, 'rb') as w:
            frames = w.getnframes()
            rate = float(w.getframerate())
            audio_duration_sec = frames / rate if rate else None
        if audio_duration_sec:
            print(f"Audio: {os.path.basename(audio_path)} ({audio_duration_sec:.2f}s)")
    except Exception as e:
        print(f"WARNING: audio file found but duration unreadable ({e}): {audio_path}")
        audio_path = None
        audio_duration_sec = None
else:
    print("Audio: not auto-discovered (pass --audio <wav> to override)")


# -------- Ken Burns assignment (unchanged behavior) --------
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


# -------- Resolve per-page durations with explicit source tracking --------
def resolve_page_duration(page, next_page):
    """Return (duration_sec, source_label). duration_sec is never None."""
    # 1. Authoritative: explicit duration field from sequence JSON.
    d = page.get('duration_seconds')
    if isinstance(d, (int, float)) and d > 0:
        return float(d), 'duration_seconds'
    # 2. Explicit start/end range in either naming convention.
    ts_start = page.get('start_seconds', page.get('start_sec', page.get('timestamp_start')))
    ts_end = page.get('end_seconds', page.get('end_sec', page.get('timestamp_end')))
    if ts_start is not None and ts_end is not None:
        try:
            dur = max(0.1, float(ts_end) - float(ts_start))
            return dur, 'start_end'
        except (TypeError, ValueError):
            pass
    # 3. Prompts-v4 style: only start_seconds per page. Use next page's start
    #    as an implicit end, or whisper_total for the final page.
    if ts_start is not None and next_page is not None:
        next_start = next_page.get('start_seconds', next_page.get('start_sec', next_page.get('timestamp_start')))
        if next_start is not None:
            try:
                dur = max(0.1, float(next_start) - float(ts_start))
                return dur, 'next_start_diff'
            except (TypeError, ValueError):
                pass
    if ts_start is not None and whisper_total is not None:
        try:
            dur = max(0.1, float(whisper_total) - float(ts_start))
            return dur, 'whisper_tail'
        except (TypeError, ValueError):
            pass
    # 4. Last resort: uniform fallback.
    return float(uniform_fallback), 'uniform_fallback'


# -------- Build scenes --------
project_id = str(uuid.uuid4())
episode_name = f"Episode {EPISODE_NUM} - {EPISODE_SLUG.replace('_', ' ').title()}"
scenes = []
missing = []
cumulative_ms = 0
source_counts = {}

for i, page in enumerate(all_pages):
    num = page.get('page') or page.get('sequence') or (i + 1)
    img_path = os.path.join(IMAGE_DIR, f'page_{num:03d}.png')
    if not os.path.exists(img_path):
        missing.append(num)
        continue

    next_page = all_pages[i + 1] if i + 1 < len(all_pages) else None
    duration_sec, source = resolve_page_duration(page, next_page)
    source_counts[source] = source_counts.get(source, 0) + 1

    scene_num = i + 1
    img_filename = f"scene_{scene_num}_16x9.png"
    start_ms = int(cumulative_ms)
    end_ms = int(cumulative_ms + duration_sec * 1000)

    scene = {
        'id': str(uuid.uuid4()),
        'sceneNumber': scene_num,
        'segmentText': page.get('narrative_beat', page.get('narration_cue', page.get('cue', f'Page {num}'))),
        'imagePrompt': page.get('prompt', ''),
        'estimatedDuration': round(duration_sec, 3),
        'startMs': start_ms,
        'endMs': end_ms,
        'images': {'16:9': f'zip:{img_filename}'},
        'status': 'completed',
        'kenBurns': assign_ken_burns(i, len(all_pages), duration_sec),
        'isIntro': i == 0,
    }
    scenes.append((scene, img_path, img_filename))
    cumulative_ms = end_ms


# -------- Build project.json --------
total_video_duration_sec = cumulative_ms / 1000.0
audio_ms = int(round((audio_duration_sec or whisper_total or total_video_duration_sec) * 1000))

project = {
    'id': project_id,
    'name': episode_name,
    'aspectRatio': '16:9',
    'audioDuration': audio_ms,
    'sceneCount': len(scenes),
    'scenes': [s[0] for s in scenes],
    'masterAssets': [],
    # New backward-compatible fields for the duration-check hook. Ignored by
    # older Wardenclyffe Desktop builds.
    'totalSceneDurationSec': round(total_video_duration_sec, 3),
}
if audio_path:
    project['audioPath'] = audio_path
if audio_duration_sec is not None:
    project['audioDurationSec'] = round(audio_duration_sec, 3)
if sequence_used:
    project['sourceSequenceJson'] = os.path.basename(sequence_used)


# -------- Write zip --------
with zipfile.ZipFile(ZIP_OUTPUT, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('project.json', json.dumps(project, indent=2))
    for scene, img_path, img_filename in scenes:
        zf.write(img_path, f'images/{img_filename}')


# -------- Stats --------
kb_used = {}
for s, _, _ in scenes:
    t = s['kenBurns']['type']
    kb_used[t] = kb_used.get(t, 0) + 1

total_dur = sum(s[0]['estimatedDuration'] for s in scenes)
zip_size_mb = os.path.getsize(ZIP_OUTPUT) / (1024 * 1024)
print(f"\nPackaged {len(scenes)} scenes -> {ZIP_OUTPUT}")
print(f"ZIP size: {zip_size_mb:.1f} MB")
print(f"Total video duration: {total_dur:.2f}s ({total_dur/60:.2f} min)")
if audio_duration_sec:
    drift = total_dur - audio_duration_sec
    status = "OK" if abs(drift) < 2.0 else "DRIFT WARNING"
    print(f"Audio duration:       {audio_duration_sec:.2f}s ({audio_duration_sec/60:.2f} min)")
    print(f"Drift (video-audio):  {drift:+.2f}s   [{status}]")
print(f"Duration sources: {source_counts}")
if source_counts.get('uniform_fallback', 0) > 0:
    print(f"WARNING: {source_counts['uniform_fallback']} pages fell back to uniform {uniform_fallback:.2f}s. Sequence JSON may be incomplete.")
print(f"Ken Burns: {kb_used}")
if missing:
    print(f"MISSING IMAGES (pages): {missing}")
print(f"\nImport this .zip into Wardenclyffe Desktop via 'Import Project'.")
