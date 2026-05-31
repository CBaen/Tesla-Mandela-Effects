# Platform Requirements And Assets

Date checked: 2026-05-29

## Source Links

- Rumble YouTube reposting: https://rumble.support/en/help/can-only-new-videos-be-uploaded-to-rumble-dot-com-or-can-videos-which-are-currently-on-youtube-be-uploaded-as-well
- Rumble licensing: https://rumble.support/en/help/a-simple-explanation-of-the-differences-between-licensing-options
- Rumble backsplash: https://rumble.support/en/help/channel-backsplash-dimensions-and-best-practices
- Spotify video specs: https://support.spotify.com/is-en/creators/article/video-specs/
- Spotify publishing videos: https://support.spotify.com/si-en/creators/article/publishing-videos/
- Spotify video thumbnails: https://support.spotify.com/ve-en/creators/article/thumbnails/
- Spotify show art guide: https://creators.spotify.com/resources/create/dos-donts-showart

## Rumble

Official support says YouTube videos can also be uploaded to Rumble, but
monetization and rights depend on the selected Rumble license:

- `Exclusive Video Management` can involve YouTube distribution and claims.
- `Video Management excluding YouTube` avoids YouTube distribution but remains
  exclusive outside YouTube.
- `Rumble Player` is non-exclusive, monetized on Rumble, and excludes YouTube
  plus third-party partners.
- `Personal Use` keeps control but disables Rumble monetization, category
  listing, and stats.

Recommended for this launch: `Rumble Player`.

Rumble channel backsplash:

- 3600 x 600 px.
- JPG or PNG.
- Profile and backsplash image files should be under 2 MB.

Upload-file caution: the current project render spec says Rumble can reuse the
YouTube master, but the current masters are very large HEVC files. Episode 002
is especially risky because it is 14.91 GiB / 16,012,417,482 bytes. If Rumble
enforces a decimal 15 GB cap, that file can fail. Create Rumble-safe H.264
derivatives before upload unless the Rumble UI accepts the masters.

## Spotify

Spotify for Creators video upload:

- Video upload is on Spotify for Creators web.
- The account must be verified before publishing the first episode.
- Supported video file types include MOV, MPG, and MP4.
- Spotify recommends H.264 High Profile, 16:9 widescreen, native frame rate,
  AAC-LC stereo at 192 Kbps or higher.
- Recommended general target is under 10 GB and under 4 hours, while the
  compatible ceiling is up to 60 GB and 12 hours.
- The file should contain one video track and one audio track, with matching
  duration.
- Video episodes are available as video on Spotify; audio from the video is
  available through RSS.

Recommended for this launch: video podcast episodes from 1080p H.264
derivatives.

Spotify thumbnails:

- Horizontal.
- 16:9.
- Suggested resolution 1920 x 1080.

Existing YouTube thumbnails are 1280 x 720 PNG files. They have the correct
aspect ratio and strong consistency, but they are below Spotify's suggested
1920 x 1080 thumbnail size.

Spotify show art:

- Use square 1:1 cover art.
- Spotify's creator guide recommends 1400 x 1400 to 3000 x 3000.
- Keep text minimal and readable at mobile size.

## Local Master Files

| Episode | Master | Size | Codec | Resolution | Duration |
|---|---|---:|---|---:|---:|
| 001 | `11. MASTER COMPOSITIONS/TESLA S1E1/Tesla 001 v2/Tesla 001 v2.mp4` | 13.22 GiB | HEVC | 2560 x 1440 | 1:16:59 |
| 002 | `11. MASTER COMPOSITIONS/TESLA S1E2/S1E2 V2/TESLA S1E2 V2/TESLA S1E2 V2.mp4` | 14.91 GiB | HEVC | 2560 x 1440 | 1:26:27 |
| 003 | `11. MASTER COMPOSITIONS/TESLA S1E3/TESLA S1E3 V3/TESLA S1E3/TESLA S1E3 v3.mp4` | 11.64 GiB | HEVC | 2560 x 1440 | 1:07:16 |

Do not upload:

`11. MASTER COMPOSITIONS/TESLA S1E3/TESLA S1E3 V2/002 Tesla/TESLA S1E3 V2.mp4`

It is the old 32-minute Episode 003 V2 file.

## Local Audio Files

| Episode | WAV | Size | Codec | Sample Rate | Channels |
|---|---|---:|---|---:|---:|
| 001 | `11. MASTER COMPOSITIONS/TESLA S1E1/Tesla 001 v2/Tesla 001 v2.WAV` | 777.2 MiB | PCM s16le | 44.1 kHz | 2 |
| 002 | `11. MASTER COMPOSITIONS/TESLA S1E2/S1E2 V2/TESLA S1E2 V2/TESLA S1E2 V2.WAV` | 872.6 MiB | PCM s16le | 44.1 kHz | 2 |
| 003 | `11. MASTER COMPOSITIONS/TESLA S1E3/TESLA S1E3 V3/TESLA S1E3/TESLA S1E3.WAV` | 679.0 MiB | PCM s16le | 44.1 kHz | 2 |

Use these only if the decision changes to audio-only podcast distribution.
