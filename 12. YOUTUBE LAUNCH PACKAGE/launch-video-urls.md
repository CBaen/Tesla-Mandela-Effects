# Launch Video URLs

Status: public on 2026-05-21. The `tesla-upload-monitor` heartbeat was
concluded on 2026-05-23 after stable public counter/comment checks.

Playlist:

- Tesla Mandela Effects - Full Episodes: https://www.youtube.com/playlist?list=PLvqKey8OjehargsjesVA-uUzZKnDLERfE
- Start Here: https://www.youtube.com/playlist?list=PLvqKey8OjehYYE3rcaqzkrLVkn8417d8w

Videos:

| Episode | Video ID | Watch URL | Scheduled Public Time |
|---|---|---|---|
| 001 | `ro5_fFx8Cz0` | https://www.youtube.com/watch?v=ro5_fFx8Cz0 | 2026-05-21 8:00 AM Pacific / 9:00 AM Mountain |
| 003 | `WYXAipQkZTo` | https://www.youtube.com/watch?v=WYXAipQkZTo | 2026-05-21 8:15 AM Pacific / 9:15 AM Mountain |
| 002 | `jTGZGrqttTM` | https://www.youtube.com/watch?v=jTGZGrqttTM | 2026-05-21 8:30 AM Pacific / 9:30 AM Mountain |

Post-publish done:

- Public watch pages confirmed by oEmbed.
- Prepared comments posted by `@TeslaMandelaEffects`:
  - Episode 001 comment/thread: `UgzHuvga5LtPk4KDYTZ4AaABAg`
  - Episode 003 comment/thread: `Ugx_M4G0pKXfhGGEEo14AaABAg`
  - Episode 002 comment/thread: `Ugx54LKy7oY3XfhNI1t4AaABAg`
- API post-launch check on 2026-05-21 08:48 Pacific confirmed all three videos
  are public, processed successfully, marked `definition=hd`, captioned, and
  still have no processing warnings/errors.
- Public playback extraction confirmed SD playback on all three. Viewer-facing
  1440p was observed for Episode 003; Episode 002 showed 1440p in one earlier
  extraction but not a later one; Episode 001 has not yet shown 1440p in the
  CLI extraction checks. Recheck the public quality ladders later before
  claiming all three are viewer-facing 1440p complete.
- YouTube Analytics API accepted a same-day channel query but returned zero
  rows at the early launch check. Studio Analytics should accumulate data as
  YouTube makes it available.
- Final automated public counter check before monitor closeout, 2026-05-23
  14:01 Pacific / 15:01 Mountain:
  - Episode 001: 9 public views, 1 comment.
  - Episode 003: 7 public views, 1 comment.
  - Episode 002: 6 public views, 1 comment.
  - The visible comment on each video was the prepared channel comment; no
    viewer comments required reply in the monitor window.
- Public metadata review for Rumble/Spotify prep on 2026-05-29:
  - Episode 001: 18 public views, 1 like, 1 comment.
  - Episode 003: 23 public views, 1 like, 1 comment.
  - Episode 002: 9 public views, likes unavailable, 1 comment.
  - Episode 003 public title was returned as `S1E1 Tesla Found the Frequency.
    CERN Found the God Particle.` Intended title is `S1E3 Tesla Found the
    Frequency. CERN Found the God Particle.`
  - Source notes:
    `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/youtube-data-review-2026-05-29.md`.

Post-publish pending:

- Pin the prepared comments in YouTube Studio or on the watch pages. The official API posted them, but pinning was not exposed through the API and the Studio comments page did not show a clear pin action during the automated pass.
- Add end screens.
- Post the prepared Community launch copy.
- Correct or verify Episode 003 title numbering in Studio/API.
- Recheck Studio Analytics after YouTube has populated retention, CTR, traffic
  source, and subscriber conversion data.
