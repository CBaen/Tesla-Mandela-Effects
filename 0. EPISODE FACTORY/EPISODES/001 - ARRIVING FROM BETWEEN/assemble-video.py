"""
Episode 001 — Video Assembly Script
Reads timed sequence + generated images + audio, produces final MP4.
Uses FFmpeg with crossfade transitions and Ken Burns zoom.

Usage: python assemble-video.py
"""

import os, sys, json, subprocess, shutil

EPISODE_DIR = os.path.dirname(os.path.abspath(__file__))
SEQUENCE_FILE = os.path.join(EPISODE_DIR, '001-VISUAL-TIMED-SEQUENCE.json')
IMAGE_DIR = os.path.join(EPISODE_DIR, 'binder-images')
AUDIO_FILE = os.path.join(
    'C:', os.sep, 'Users', 'baenb', 'Desktop', 'Tesla Mandela Effects',
    '3. ELEVEN LABS AUDIO', '01. v4 new narrator',
    'ElevenLabs_001-ARRIVING_FROM_BETWEEN-SCRIPT-v5_THEO.wav'
)
OUTPUT_FILE = os.path.join(EPISODE_DIR, '001-ARRIVING_FROM_BETWEEN-FINAL.mp4')

# Check FFmpeg
if not shutil.which('ffmpeg'):
    print("ERROR: FFmpeg not found in PATH")
    sys.exit(1)

# Load sequence
with open(SEQUENCE_FILE) as f:
    data = json.load(f)
pages = data['pages']

# Verify all images exist
missing = []
for page in pages:
    seq = page.get('sequence', page['page'])
    img_path = os.path.join(IMAGE_DIR, f"page_{seq:03d}.png")
    if not os.path.exists(img_path):
        missing.append(seq)

if missing:
    print(f"ERROR: {len(missing)} images missing: {missing[:10]}{'...' if len(missing) > 10 else ''}")
    print(f"Run generate-binder-images.py first.")
    sys.exit(1)

print(f"Episode 001 — Video Assembly")
print(f"Pages: {len(pages)}")
print(f"Audio: {os.path.basename(AUDIO_FILE)}")
print(f"Output: {OUTPUT_FILE}")
print()

# Build FFmpeg concat file
# Each image gets its own duration based on the timed sequence
concat_file = os.path.join(EPISODE_DIR, 'ffmpeg-concat.txt')
with open(concat_file, 'w') as f:
    for page in pages:
        seq = page.get('sequence', page['page'])
        img_path = os.path.join(IMAGE_DIR, f"page_{seq:03d}.png")
        duration = page['duration_seconds']
        # FFmpeg concat demuxer format
        f.write(f"file '{img_path}'\n")
        f.write(f"duration {duration:.2f}\n")
    # Repeat last image (FFmpeg concat needs this)
    last_seq = pages[-1].get('sequence', pages[-1]['page'])
    last_img = os.path.join(IMAGE_DIR, f"page_{last_seq:03d}.png")
    f.write(f"file '{last_img}'\n")

print("Assembling video with FFmpeg...")
print("This may take a few minutes for a 76-minute video.\n")

# FFmpeg command:
# -f concat: read image sequence with durations
# -i audio: the WAV audio
# -vf scale: ensure 1920x1080
# -c:v libx264: H.264 encoding
# -pix_fmt yuv420p: YouTube-compatible pixel format
# -c:a aac: AAC audio encoding
# -shortest: stop at the shorter of audio/video
cmd = [
    'ffmpeg', '-y',
    '-f', 'concat', '-safe', '0', '-i', concat_file,
    '-i', AUDIO_FILE,
    '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
    '-c:a', 'aac', '-b:a', '192k',
    '-shortest',
    '-movflags', '+faststart',
    OUTPUT_FILE
]

print(f"Running: {' '.join(cmd[:6])}...")
result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)

if result.returncode == 0:
    size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
    print(f"\nSUCCESS!")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Size: {size_mb:.1f} MB")
else:
    print(f"\nFFmpeg FAILED (exit code {result.returncode})")
    print(f"stderr: {result.stderr[:500]}")

# Cleanup
if os.path.exists(concat_file):
    os.remove(concat_file)

print("\nDone.")
