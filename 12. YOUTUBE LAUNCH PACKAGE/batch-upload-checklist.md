# Batch Upload Checklist

## Before Upload

- [x] Confirm Episode 3 fresh rerender:
  - [x] Use `TESLA S1E3 V3/TESLA S1E3/TESLA S1E3 v3.mp4`.
  - [x] Do not use `TESLA S1E3 V2/002 Tesla/TESLA S1E3 V2.mp4`; it verifies at 0:32:36 and is wrong.
  - [x] Do not use `TESLA S1E3 V1.mp4`; V3 is now the selected cut.
  - [x] Verified V3 with ffprobe.
- [x] Verify the YouTube account is enabled for videos longer than 15 minutes and custom thumbnails.
- [x] Confirm advanced features are enabled for manual chapters and thumbnail testing.
- [x] Create playlists:
  - [x] `Tesla Mandela Effects — Full Episodes`
  - [x] `Start Here`
  - [x] `The Tesla Timeline`
- [x] Confirm final channel About copy and keywords from `professional-channel-setup.md`.
- [x] Verify launch thumbnails in `13. YOUTUBE THUMBNAILS`.
- [x] Generate captions into `12. YOUTUBE LAUNCH PACKAGE/captions/`.
- [x] Upload captions from `captions/`.

## Upload Settings For All Three

- [x] Visibility: private first; schedule only after checks/processing are reviewed.
- [x] Final publish pattern: stagger 001 -> 003 -> 002 by 15 minutes.
- [x] Premiere: off for 1440p masters.
- [x] Notify subscribers: on.
- [x] Category: Film & Animation.
- [x] Language: English.
- [x] Made for kids: No.
- [x] Age restriction: No.
- [x] Altered/synthetic content: Yes.
- [x] Paid promotion: No, unless this changes.
- [x] License: Standard YouTube License.
- [x] Embedding: allowed.
- [x] Comments: on.
- [ ] Shorts remixing: decide intentionally; default off if you want stronger audio/control boundaries.

## Per Video

- [x] Paste title from the episode metadata file.
- [x] Paste description from the episode metadata file.
- [x] Paste tags from the episode metadata file.
- [x] Upload thumbnail.
- [x] Add to playlists.
- [x] Upload captions.
- [x] Confirm chapter blocks are named, ascending, start at `00:00`, and use hour-format timestamps where needed in the uploaded descriptions.
- [x] Run copyright checks before publish.
- [ ] Recheck public 1440p playback on every watch page before claiming the viewer-facing 1440p ladder is complete.

## Episode 3 Fresh Render Verification

Verified upload candidate:

`C:\Users\baenb\Desktop\Tesla Mandela Effects\11. MASTER COMPOSITIONS\TESLA S1E3\TESLA S1E3 V3\TESLA S1E3\TESLA S1E3 v3.mp4`

Verification command used:

```powershell
ffprobe -v error -show_entries format=duration,size,bit_rate -show_entries stream=index,codec_type,codec_name,width,height,avg_frame_rate,sample_rate,channels -of json "C:\Users\baenb\Desktop\Tesla Mandela Effects\11. MASTER COMPOSITIONS\TESLA S1E3\TESLA S1E3 V3\TESLA S1E3\TESLA S1E3 v3.mp4"
```

Verified result:

- [x] Duration is over 3600 seconds: 4036.401995 seconds / 1:07:16.
- [x] Video is 2560x1440.
- [x] Audio exists: stereo AAC, 44.1 kHz.
- [x] The file timestamp matches the fresh rerender.
- [x] The first and last two minutes decode cleanly with ffmpeg.

## Launch Window

- [x] T+0 launch target: Thursday, 2026-05-21, 9:00 AM Mountain / 11:00 AM Eastern / 8:00 AM Pacific.
- [x] Schedule target: Episode 001 at 9:00 AM Mountain, Episode 003 at 9:15 AM Mountain, Episode 002 at 9:30 AM Mountain.
- [x] All three videos were clean before 8:30 AM Mountain; fallback not needed.
- [x] Schedule all three at the chosen time using the 001 -> 003 -> 002 stagger.
- [x] Publish all three at the chosen time using the 001 -> 003 -> 002 stagger.
- [x] Do not publish any other upload/live stream within 24 hours.
- [ ] Pin each episode's prepared comment immediately after publish. Comments are posted; pinning still needs Studio/watch-page confirmation.
- [x] First 48-hour automated public-counter/comment monitoring finished with no viewer comments needing reply.
- [ ] After the first day, start thumbnail Test & Compare on each public long-form video if the account is eligible.
- [ ] Track CTR, average view duration, traffic source, and subscriber conversion per episode.
- [x] Conclude the `tesla-upload-monitor` heartbeat after stable first-48-hour checks.

## Same-Time Release Reality

Final decision: stagger the public release by 15 minutes in this order: Episode 001, Episode 003, Episode 002. Same-time release would prove channel depth immediately, but staggering gives each video cleaner first-hour attention while keeping the three-episode launch intact.
