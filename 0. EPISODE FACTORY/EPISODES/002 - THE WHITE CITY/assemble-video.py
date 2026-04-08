"""
Episode 002 "The White City" — Video Assembly
Reads timed sequence + generated images + audio, produces final MP4.

Usage: python assemble-video.py
"""

import os, sys, json, subprocess, shutil

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
SEQUENCE_FILE = os.path.join(EPISODE_DIR, '002-VISUAL-TIMED-SEQUENCE-v3.json')
IMAGE_DIR = os.path.join(EPISODE_DIR, 'binder-images')
AUDIO_FILE = os.path.join(
    'C:', os.sep, 'Users', 'baenb', 'Desktop', 'Tesla Mandela Effects',
    '3. ELEVEN LABS AUDIO', '01. v4 new narrator',
    'ElevenLabs_002-THE_WHITE_CITY-SCRIPT-v4_THEO_SILK.wav'
)
OUTPUT_FILE = os.path.join(EPISODE_DIR, '002-THE_WHITE_CITY-FINAL.mp4')

if not shutil.which('ffmpeg'):
    print("ERROR: FFmpeg not found"); sys.exit(1)

with open(SEQUENCE_FILE) as f:
    data = json.load(f)
pages = data['pages']

missing = [p.get('sequence', p['page']) for p in pages
           if not os.path.exists(os.path.join(IMAGE_DIR, f"page_{p.get('sequence', p['page']):03d}.png"))]
if missing:
    print(f"ERROR: {len(missing)} images missing. Run generate-binder-images.py first."); sys.exit(1)

print(f"Episode 002 — Video Assembly")
print(f"Pages: {len(pages)}, Audio: {os.path.basename(AUDIO_FILE)}\n")

concat_file = os.path.join(EPISODE_DIR, 'ffmpeg-concat.txt')
with open(concat_file, 'w') as f:
    for page in pages:
        seq = page.get('sequence', page['page'])
        img = os.path.join(IMAGE_DIR, f"page_{seq:03d}.png")
        f.write(f"file '{img}'\nduration {page['duration_seconds']:.2f}\n")
    last = pages[-1].get('sequence', pages[-1]['page'])
    f.write(f"file '{os.path.join(IMAGE_DIR, f'page_{last:03d}.png')}'\n")

cmd = ['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_file,
       '-i', AUDIO_FILE,
       '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p',
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
       '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart',
       OUTPUT_FILE]

print("Assembling with FFmpeg...")
result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)

if result.returncode == 0:
    size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    print(f"\nSUCCESS! Output: {OUTPUT_FILE} ({size_mb:.1f} MB)")
else:
    print(f"\nFFmpeg FAILED: {result.stderr[:500]}")

if os.path.exists(concat_file): os.remove(concat_file)
