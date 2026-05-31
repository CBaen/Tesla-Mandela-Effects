# Asset Export Commands

Use these only if we decide not to upload the current HEVC masters directly.

Output folder:

`14. RUMBLE SPOTIFY LAUNCH PACKAGE/delivery`

Create it first:

```powershell
New-Item -ItemType Directory -Force -Path 'C:\Users\baenb\Desktop\Tesla Mandela Effects\14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery' | Out-Null
```

## Rumble Derivatives

Goal: 1440p H.264 MP4, AAC stereo, one keyframe per second, smaller and more
upload-compatible than the current HEVC masters.

Episode 001:

```powershell
ffmpeg -y -i 'C:\Users\baenb\Desktop\Tesla Mandela Effects\11. MASTER COMPOSITIONS\TESLA S1E1\Tesla 001 v2\Tesla 001 v2.mp4' -map 0:v:0 -map 0:a:0 -vf 'scale=2560:1440:flags=lanczos,format=yuv420p' -c:v libx264 -profile:v high -level 5.1 -preset slow -crf 21 -maxrate 14000k -bufsize 28000k -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 320k -ac 2 -ar 48000 -movflags +faststart 'C:\Users\baenb\Desktop\Tesla Mandela Effects\14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery\TME-S1E1-rumble-1440p-h264.mp4'
```

Episode 002:

```powershell
ffmpeg -y -i 'C:\Users\baenb\Desktop\Tesla Mandela Effects\11. MASTER COMPOSITIONS\TESLA S1E2\S1E2 V2\TESLA S1E2 V2\TESLA S1E2 V2.mp4' -map 0:v:0 -map 0:a:0 -vf 'scale=2560:1440:flags=lanczos,format=yuv420p' -c:v libx264 -profile:v high -level 5.1 -preset slow -crf 21 -maxrate 14000k -bufsize 28000k -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 320k -ac 2 -ar 48000 -movflags +faststart 'C:\Users\baenb\Desktop\Tesla Mandela Effects\14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery\TME-S1E2-rumble-1440p-h264.mp4'
```

Episode 003:

```powershell
ffmpeg -y -i 'C:\Users\baenb\Desktop\Tesla Mandela Effects\11. MASTER COMPOSITIONS\TESLA S1E3\TESLA S1E3 V3\TESLA S1E3\TESLA S1E3 v3.mp4' -map 0:v:0 -map 0:a:0 -vf 'scale=2560:1440:flags=lanczos,format=yuv420p' -c:v libx264 -profile:v high -level 5.1 -preset slow -crf 21 -maxrate 14000k -bufsize 28000k -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 320k -ac 2 -ar 48000 -movflags +faststart 'C:\Users\baenb\Desktop\Tesla Mandela Effects\14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery\TME-S1E3-rumble-1440p-h264.mp4'
```

## Spotify Video Derivatives

Goal: 1080p H.264 MP4, AAC stereo, one keyframe per second, under the safer
10 GB target.

Episode 001:

```powershell
ffmpeg -y -i 'C:\Users\baenb\Desktop\Tesla Mandela Effects\11. MASTER COMPOSITIONS\TESLA S1E1\Tesla 001 v2\Tesla 001 v2.mp4' -map 0:v:0 -map 0:a:0 -vf 'scale=1920:1080:flags=lanczos,format=yuv420p' -c:v libx264 -profile:v high -level 4.2 -preset slow -crf 22 -maxrate 10000k -bufsize 20000k -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 320k -ac 2 -ar 48000 -movflags +faststart 'C:\Users\baenb\Desktop\Tesla Mandela Effects\14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery\TME-S1E1-spotify-1080p-h264.mp4'
```

Episode 002:

```powershell
ffmpeg -y -i 'C:\Users\baenb\Desktop\Tesla Mandela Effects\11. MASTER COMPOSITIONS\TESLA S1E2\S1E2 V2\TESLA S1E2 V2\TESLA S1E2 V2.mp4' -map 0:v:0 -map 0:a:0 -vf 'scale=1920:1080:flags=lanczos,format=yuv420p' -c:v libx264 -profile:v high -level 4.2 -preset slow -crf 22 -maxrate 10000k -bufsize 20000k -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 320k -ac 2 -ar 48000 -movflags +faststart 'C:\Users\baenb\Desktop\Tesla Mandela Effects\14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery\TME-S1E2-spotify-1080p-h264.mp4'
```

Episode 003:

```powershell
ffmpeg -y -i 'C:\Users\baenb\Desktop\Tesla Mandela Effects\11. MASTER COMPOSITIONS\TESLA S1E3\TESLA S1E3 V3\TESLA S1E3\TESLA S1E3 v3.mp4' -map 0:v:0 -map 0:a:0 -vf 'scale=1920:1080:flags=lanczos,format=yuv420p' -c:v libx264 -profile:v high -level 4.2 -preset slow -crf 22 -maxrate 10000k -bufsize 20000k -r 30 -g 30 -keyint_min 30 -c:a aac -b:a 320k -ac 2 -ar 48000 -movflags +faststart 'C:\Users\baenb\Desktop\Tesla Mandela Effects\14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery\TME-S1E3-spotify-1080p-h264.mp4'
```

## Verify Outputs

```powershell
Get-ChildItem 'C:\Users\baenb\Desktop\Tesla Mandela Effects\14. RUMBLE SPOTIFY LAUNCH PACKAGE\delivery' -Filter *.mp4 | ForEach-Object {
  ffprobe -v error -show_entries format=duration,size,bit_rate -show_streams -of json $_.FullName
}
```

Do not publish from any derivative until its duration matches the source episode
and the file plays locally.
