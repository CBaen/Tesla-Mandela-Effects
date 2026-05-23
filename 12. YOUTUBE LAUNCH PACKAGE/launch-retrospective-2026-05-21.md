# Tesla Mandela Effects Launch Retrospective - 2026-05-21

Review time: 2026-05-21 09:48 Mountain / 08:48 Pacific.
Monitor closeout updated: 2026-05-23 15:01 Mountain / 14:01 Pacific.

## Current Reality

The three launch videos are live on the correct channel, `Tesla Mandela Effects`
(`UCYNUNx3Dk30fK9BVpYliXvQ`).

| Episode | Video ID | Public state | API processing | Captions | Comments | Public playback quality observed |
|---|---|---|---|---|---|---|
| 001 | `ro5_fFx8Cz0` | Public, oEmbed 200 | Succeeded, `definition=hd` | Auto + uploaded English SRT serving | Prepared comment present | SD/360p observed; viewer-facing HD not yet observed in CLI extraction |
| 003 | `WYXAipQkZTo` | Public, oEmbed 200 | Succeeded, `definition=hd` | Auto + uploaded English SRT serving | Prepared comment present | SD plus 720p/1080p/1440p observed in CLI extraction |
| 002 | `jTGZGrqttTM` | Public, oEmbed 200 | Succeeded, `definition=hd` | Auto + uploaded English SRT serving | Prepared comment present | SD observed; an earlier extraction showed 720p/1080p/1440p, later extraction showed only 360p |

Plain-English read: YouTube says all three uploads have processed as HD, but
viewer-facing playback ladders are still inconsistent by public extraction. SD
is available on all three. Do not claim all three are publicly 1440p-complete
until a fresh public player or format-ladder check shows 1440p on each video.

Analytics is available as a YouTube surface automatically. The YouTube
Analytics API accepted a same-day channel query, but returned zero rows at this
early check. That is normal enough for launch morning and does not mean
analytics is broken. The channel is not monetized, so revenue analytics are not
expected yet.

The `tesla-upload-monitor` heartbeat was concluded on 2026-05-23 after stable
public checks. Final public counters before closeout were Episode 001: 9 views
/ 1 channel comment, Episode 003: 7 views / 1 channel comment, and Episode 002:
6 views / 1 channel comment. No viewer comments required reply during the
monitor window.

## What Went Well

- The release used the right safety shape: private upload first, then processing,
  captions, thumbnails, playlists, checks, schedule, and public confirmation.
- The wrong Episode 003 file was caught and avoided. The uploaded file was the
  full V3 render, not the 32-minute V2 file.
- Metadata cleanup mattered. Chapter timestamp formatting, Episode 002 title,
  description disclaimer placement, altered-content disclosure, and caption
  entity fixes were all handled before launch.
- The API/Studio split worked. The official API gave durable proof for channel,
  upload, captions, comments, playlists, and public status. Studio was used for
  the policy/checks/settings surfaces that the public API does not fully expose.
- The final schedule was coherent: Episode 001, then Episode 003, then Episode
  002, staggered by 15 minutes at the user's Seattle morning launch window.
- The launch monitor helped preserve the conditional go-ahead while the user
  slept. It kept the decision rule simple: if clean, schedule/release; if yellow
  or red, stop and report.

## What Nearly Went Wrong

- There were too many overlapping source documents. Older root-level strategy
  docs still describe different launch plans, including Premiere and different
  timing. The launch package became the real source of truth, but this should be
  more explicit next time.
- A timezone interpretation error briefly caused a false alarm that two videos
  had gone public early. The underlying UTC schedule was correct. Future launch
  docs need one schedule table with Pacific, Mountain, Eastern, and UTC on the
  same row.
- A delegated QA lane drifted into the episode factory instead of the active
  YouTube launch package. It reported missing metadata/captions because it was
  looking at production assets, not the release assets. Future subagent prompts
  need to say which folder is authoritative and which folders are archive-only
  for the current question.
- Pinning, end screens, and Community posting are still manual/Studio work. The
  YouTube Data API posted comments, but it does not expose pin-comment,
  end-screen, or Community-post actions.
- HD status has two layers and they got blurred. API `definition=hd` means the
  video processed as HD; it does not prove every viewer can already select
  720p/1080p/1440p. Public playback quality needs its own check.

## What Should Be Reused

- Keep a current launch source of truth inside the release package. Older
  strategy docs should be marked stale or superseded when the live release plan
  changes.
- Split readiness into gates:
  1. local asset gate: file, duration, resolution, audio, thumbnail, caption file;
  2. metadata gate: title, description, chapters, disclaimer, tags, pinned comment;
  3. account gate: channel identity, features, category, comments, monetization state;
  4. private upload gate: processing, captions, thumbnail, playlists, checks;
  5. schedule gate: exact local and UTC times, notification intent, fallback;
  6. public surface gate: watch pages, comments, captions, playback quality ladder;
  7. post-launch gate: pinned comments, end screens, Community post, analytics.
- Treat Studio-only tasks as a separate lane. Do not promise automation where
  YouTube does not expose a supported API action.
- Record exact video IDs and public URLs immediately after upload, not only
  after public release.
- Keep the user's conditional go-ahead in the handoff, with stop conditions
  written in plain language.

## Remaining Work

- Recheck viewer-facing playback quality later and confirm 1440p on all three
  public watch pages.
- Pin the prepared comments manually in YouTube Studio or on the watch pages.
- Add end screens pointing to the Full Episodes playlist plus one other episode.
- Post the prepared Community launch copy with the playlist URL.
- Watch comments for confusion about docufiction vs factual documentary.
- Review YouTube Studio Analytics after enough data exists, then record CTR,
  average view duration, traffic source, and subscriber conversion per episode.
- Do not restart `tesla-upload-monitor`; use an explicit new monitor only if a
  new post-launch watch task is requested.
