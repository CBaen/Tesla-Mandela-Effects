# Batch Upload Checklist

## Before Upload

- [x] Confirm Episode 3 fresh rerender:
  - [x] Use `TESLA S1E3 V3/TESLA S1E3/TESLA S1E3 v3.mp4`.
  - [x] Do not use `TESLA S1E3 V2/002 Tesla/TESLA S1E3 V2.mp4`; it verifies at 0:32:36 and is wrong.
  - [x] Do not use `TESLA S1E3 V1.mp4`; V3 is now the selected cut.
  - [x] Verified V3 with ffprobe.
- [ ] Verify the YouTube account is phone-verified for videos longer than 15 minutes and custom thumbnails.
- [ ] Confirm advanced features are enabled for manual chapters and thumbnail testing.
- [ ] Create playlists:
  - [ ] `Tesla Mandela Effects - Full Episodes`
  - [ ] `Start Here`
  - [ ] `The Tesla Timeline`
- [ ] Set channel description and keywords from `YOUTUBE_LAUNCH_GUIDE.md`.
- [x] Verify launch thumbnails in `13. YOUTUBE THUMBNAILS`.
- [x] Generate captions into `12. YOUTUBE LAUNCH PACKAGE/captions/`.
- [ ] Upload captions from `captions/`.

## Upload Settings For All Three

- [ ] Visibility: scheduled.
- [ ] Same publish time for all three.
- [ ] Premiere: off for 1440p masters.
- [ ] Notify subscribers: on.
- [ ] Category: Film & Animation.
- [ ] Language: English.
- [ ] Made for kids: No.
- [ ] Age restriction: No.
- [ ] Altered/synthetic content: Yes.
- [ ] Paid promotion: No, unless this changes.
- [ ] License: Standard YouTube License.
- [ ] Embedding: allowed.
- [ ] Comments: on.
- [ ] Shorts remixing: decide intentionally; default off if you want stronger audio/control boundaries.

## Per Video

- [ ] Paste title from the episode metadata file.
- [ ] Paste description from the episode metadata file.
- [ ] Paste tags from the episode metadata file.
- [ ] Upload thumbnail.
- [ ] Add to playlists.
- [ ] Upload captions.
- [ ] Confirm chapters render from the description.
- [ ] Run copyright checks before publish.
- [ ] Wait for 1440p processing before launch if possible.

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

- [ ] Publish all three at the same time.
- [ ] Do not publish any other upload/live stream within 24 hours.
- [ ] Pin each episode's prepared comment immediately after publish.
- [ ] Reply to comments for the first 48 hours.
- [ ] After the first day, start thumbnail Test & Compare on each public long-form video if the account is eligible.
- [ ] Track CTR, average view duration, traffic source, and subscriber conversion per episode.

## Same-Time Release Reality

Same-time release is good for proving the channel has depth immediately. The tradeoff is that three long videos compete for the same viewer attention on day one. Because the user requested a simultaneous drop, keep the launch simultaneous, but make the playlist and end screens do the work of chaining viewers across the set.
