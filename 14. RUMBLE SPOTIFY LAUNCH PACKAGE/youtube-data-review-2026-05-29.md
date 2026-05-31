# YouTube Data Review - 2026-05-29

Source: public YouTube metadata via `yt-dlp` from the three public watch URLs.
This is not Studio Analytics.

## Public Metadata Snapshot

| Episode | Video ID | Public title returned | Duration | Views | Likes | Comments |
|---|---|---|---:|---:|---:|---:|
| 001 | `ro5_fFx8Cz0` | `S1E1 Tesla Died Alone. The Room Smelled Like Lightning.` | 1:17:00 | 18 | 1 | 1 |
| 003 | `WYXAipQkZTo` | `S1E1 Tesla Found the Frequency. CERN Found the God Particle.` | 1:07:16 | 23 | 1 | 1 |
| 002 | `jTGZGrqttTM` | `S1E2 Tesla Lit the White City in 1893. Then It Stopped Acting Temporary.` | 1:26:27 | 9 | unavailable | 1 |

## Read

Episode 003 is the highest public-view video in the tiny sample, but the
sample is too small to optimize around. The useful signal is not "chase CERN
everywhere"; it is that the God Particle / Mandela Effect hook is probably the
clearest public click hook of the first three.

The stronger decision-grade signal still needs YouTube Studio Analytics:

- impressions;
- click-through rate;
- average view duration;
- retention graph, especially first 30 seconds and first 5 minutes;
- traffic source;
- subscriber conversion;
- geography;
- device mix.

## Issue Found

Episode 003 is publicly returned as `S1E1`, not `S1E3`.

Recommended correction:

`S1E3 Tesla Found the Frequency. CERN Found the God Particle.`

Do not propagate the wrong `S1E1` label to Rumble or Spotify.

## Quality-Ladder Note

The same public tool run returned only 360p format ladders on 2026-05-29. That
conflicts with earlier launch-package evidence where Episode 003 had 1440p and
Episode 002 had shown 1440p once. Treat this as inconclusive until checked in
the public player or Studio. API `definition=hd` is not enough proof of
viewer-facing 1440p.

## Decision Impact

Post to Rumble and Spotify using corrected episode numbering and platform-fit
metadata. Do not delay cross-posting solely for more YouTube data unless the
goal is to revise titles/thumbnails first. If the goal is consistency, fix the
Episode 003 YouTube title before or during cross-posting.
