# Delivery Summary - 2026-05-29

Generated locally for Rumble and Spotify cross-posting.

## Rumble Files

| Episode | File | Size | Duration | Video | Audio |
|---|---|---:|---:|---|---|
| S1E1 | `delivery/TME-S1E1-rumble-1440p-h264.mp4` | 7.994 GiB | 4619.85 sec | H.264, 2560x1440 | AAC stereo, 48 kHz |
| S1E2 | `delivery/TME-S1E2-rumble-1440p-h264.mp4` | 9.017 GiB | 5187.26 sec | H.264, 2560x1440 | AAC stereo, 48 kHz |
| S1E3 | `delivery/TME-S1E3-rumble-1440p-h264.mp4` | 7.106 GiB | 4036.40 sec | H.264, 2560x1440 | AAC stereo, 48 kHz |

## Spotify Files

| Episode | File | Size | Duration | Video | Audio |
|---|---|---:|---:|---|---|
| S1E1 | `delivery/TME-S1E1-spotify-1080p-h264.mp4` | 4.446 GiB | 4619.85 sec | H.264, 1920x1080 | AAC stereo, 48 kHz |
| S1E2 | `delivery/TME-S1E2-spotify-1080p-h264.mp4` | 4.985 GiB | 5187.26 sec | H.264, 1920x1080 | AAC stereo, 48 kHz |
| S1E3 | `delivery/TME-S1E3-spotify-1080p-h264.mp4` | 3.988 GiB | 4036.40 sec | H.264, 1920x1080 | AAC stereo, 48 kHz |

## Verification

All six files were probed with `ffprobe` after transcode. Durations match the
verified YouTube master durations in the launch package.

No Rumble or Spotify upload was performed from this session because no safe
authenticated browser or platform API control path was available.

## Cleanup

Generated delivery MP4s remain local and ignored by Git because they are the
current upload payloads. Transcode logs, status JSON, and manifest JSON were
removed after this durable summary was recorded.
