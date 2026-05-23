# Pre-Upload Readiness Review - 2026-05-21

Status on 2026-05-23: historical readiness record. The videos are now public.
For current status, use `launch-video-urls.md`,
`launch-retrospective-2026-05-21.md`, and
`POST_LAUNCH_HANDOFF_2026-05-23.md`.

Local time checked: 2026-05-21 00:45 Mountain.
Studio/settings recheck updated: 2026-05-21 01:37 Mountain.
Private-upload and scheduling pass updated: 2026-05-21 04:25 Mountain.

## Access Lanes

### Verified

- Official YouTube Data API channel read succeeded with `python .\youtube_api_cli.py whoami`.
- Authenticated channel: `Tesla Mandela Effects`.
- Channel ID: `UCYNUNx3Dk30fK9BVpYliXvQ`.
- Handle/custom URL: `@teslamandelaeffects`.
- Country: `US`.
- Current API stats: `1` subscriber, `0` videos.
- API status: public channel, linked, `longUploadsStatus` is `allowed`, not made for kids, channel monetization is not enabled.
- Chrome is running locally, the Codex Chrome Extension is installed/enabled, and the native messaging host check passed.
- YouTube Studio channel surface visibly resolves to `Tesla Mandela Effects`.
- Earn tab shows the channel is not yet eligible for YPP/ads because it has `1` subscriber, `0` uploads, `0` valid public watch hours, and `0` valid public Shorts views.
- Studio settings show currency `USD - US Dollar`.
- Channel advanced settings show the channel default is `No, set this channel as not made for kids`.
- Feature eligibility shows Standard, Intermediate, and Advanced features all `Enabled`.
- Upload defaults advanced settings show category `Film & Animation`, video language `English`, caption certification `None`, title/description language `English`, comments `On`, moderation `Basic`, and visible like counts enabled.
- Community moderation shows comments on new videos/posts `On`, comment moderation `Basic`, live chat moderation `None`, viewer community posts `Off`, blocked words configured for conspiracy/tabloid framing, and links/hashtags held for review.
- Permissions show Cameron Paul as Owner and Cameron Baen as Editor.
- Content page shows no existing videos yet.
- API upload tooling now defaults videos to `privacyStatus: private`, `selfDeclaredMadeForKids: false`, and `containsSyntheticMedia: true`.
- Channel About copy now matches `professional-channel-setup.md` and explicitly says the series is storytelling, not a factual documentary.
- Final launch category decision: keep `Film & Animation`.
- Final public schedule decision: stagger Episode 001, then Episode 003 fifteen minutes later, then Episode 002 fifteen minutes after that.
- T+0 target: Thursday, 2026-05-21, 9:00 AM Mountain / 11:00 AM Eastern / 8:00 AM Pacific.
- Schedule target: Episode 001 at 9:00 AM Mountain, Episode 003 at 9:15 AM Mountain, Episode 002 at 9:30 AM Mountain.
- Episode 003 pinned comment decision: keep the current single-question comment.

### Verified After Private Upload

- Episode 001 uploaded privately as `ro5_fFx8Cz0`, processed successfully, custom thumbnail attached, English SRT serving, playlists attached, Studio `Notices` shows `-`, and Studio copyright says no copyright issues or visibility restrictions.
- Episode 003 uploaded privately as `WYXAipQkZTo`, processed successfully, custom thumbnail attached, English SRT serving, playlists attached, Studio `Notices` shows `-`, and Studio copyright says no copyright issues or visibility restrictions.
- Episode 002 uploaded privately as `jTGZGrqttTM`, processed successfully, custom thumbnail attached, English SRT serving, playlists attached, Studio `Notices` shows `-`, and Studio copyright says no copyright issues or visibility restrictions.
- Studio advanced settings verified on all three: Film & Animation, English video language, not made for kids, no age restriction, altered content `Yes`, paid promotion unchecked, Standard YouTube License, embedding allowed, notify subscribers checked, and comments on.
- Caption spot-check artifacts were fixed and reuploaded for Episode 001 and Episode 002: `O'Neill`, `principles or methods`, and `100,000`.
- API schedule is set:
  - Episode 001: `2026-05-21T15:00:00Z` / 8:00 AM Pacific / 9:00 AM Mountain.
  - Episode 003: `2026-05-21T15:15:00Z` / 8:15 AM Pacific / 9:15 AM Mountain.
  - Episode 002: `2026-05-21T15:30:00Z` / 8:30 AM Pacific / 9:30 AM Mountain.

### Unverified
- Explicit account-level 2FA proof was not opened; Studio feature eligibility is already enabled, so no visible feature blocker was found in Studio.
- Active-strike status was not found as a separate explicit label in the checked Studio surfaces; no visible strike blocker appeared on Dashboard, Earn, Content, Settings, or Feature eligibility.
- 1440p-specific public playback quality is not directly proven by the API; the uploads are processed successfully as HD and remain scheduled.
- Post-publish tasks are still pending until the videos are live: pin comments, add end screens, fill any remaining Community-post URLs, post the Community copy, and monitor first-hour comments.

### Blocked Or Hold Points

- Do not public-publish from API or Studio before copyright/processing/checks are reviewed.
- Do not expect launch revenue yet: API reports `isChannelMonetizationEnabled: false`.
- Do not use Premiere for the current 1440p masters unless separate 1080p Premiere files are prepared.

## Official Current-Source Refresh

Sources checked on 2026-05-21:

- Notifications: https://support.google.com/youtube/answer/7457584
- Tags: https://support.google.com/youtube/answer/146402
- Chapters: https://support.google.com/youtube/answer/9884579
- Thumbnails: https://support.google.com/youtube/answer/72431
- Search: https://support.google.com/youtube/answer/16090438
- YPP eligibility: https://support.google.com/youtube/answer/72851
- Altered/synthetic disclosure: https://support.google.com/youtube/answer/14328491
- Long uploads/account verification: https://support.google.com/youtube/answer/71673
- Premieres: https://support.google.com/youtube/answer/9080341
- YouTube Data API `videos.insert`: https://developers.google.com/youtube/v3/docs/videos/insert

Current rules preserved:

- Viewers can receive at most 3 upload/live notifications from one channel in a 24-hour period.
- Tags play a minimal discovery role except for misspellings and variants; title, thumbnail, description, and content matter more.
- Manual chapters should start at `00:00`, include at least three ascending timestamps, and each chapter should be at least 10 seconds.
- Custom thumbnails require a verified account and must follow Community Guidelines.
- Search ranking considers relevance, engagement, and quality signals.
- Realistic altered/synthetic content needs disclosure in the upload flow.
- Verified accounts can upload videos longer than 15 minutes.
- Current YouTube Premiere guidance still says output greater than 1080p is not supported for Premieres.
- `videos.insert` uploads from unverified API projects created after 2020-07-28 are restricted to private viewing until audit.

## Local Asset Verification

| Episode | File | Duration | Video | Audio | Size | Status |
|---|---|---:|---|---|---:|---|
| 001 | `11. MASTER COMPOSITIONS/TESLA S1E1/Tesla 001 v2/Tesla 001 v2.mp4` | 1:16:59 | HEVC 2560x1440 30fps | AAC stereo 44.1kHz | 14,199,944,359 bytes | Ready for private/scheduled upload |
| 002 | `11. MASTER COMPOSITIONS/TESLA S1E2/S1E2 V2/TESLA S1E2 V2/TESLA S1E2 V2.mp4` | 1:26:27 | HEVC 2560x1440 30fps | AAC stereo 44.1kHz | 16,012,417,482 bytes | Ready for private/scheduled upload |
| 003 | `11. MASTER COMPOSITIONS/TESLA S1E3/TESLA S1E3 V3/TESLA S1E3/TESLA S1E3 v3.mp4` | 1:07:16 | HEVC 2560x1440 30fps | AAC stereo 44.1kHz | 12,499,705,995 bytes | Ready for private/scheduled upload |

Do not upload the Episode 003 V2 32-minute file.

Thumbnails:

- `13. YOUTUBE THUMBNAILS/1.png`: 1280x720, 1,605,447 bytes.
- `13. YOUTUBE THUMBNAILS/2.png`: 1280x720, 1,587,425 bytes.
- `13. YOUTUBE THUMBNAILS/3.png`: 1280x720, 1,594,111 bytes.

Caption files exist and were cleaned for high-risk entity/search errors. Still spot-check in Studio after upload because the final SRT timestamps end before the full rendered files by roughly 42-59 seconds, likely trailing outro/padding.

## Metadata Changes Made

- Normalized each first manual chapter timestamp from `0:00` to `00:00`.
- Corrected all over-60-minute manual chapter timestamps to hour format:
  `1:14:49`, `1:15:19`, `1:19:42`, and `1:06:10`.
- Applied the user-approved Episode 002 title:
  `Tesla Lit the White City in 1893. Then It Stopped Acting Temporary.`
- Moved the recurring release line above the docufiction disclaimer so each
  description's final paragraph before hashtags is the disclaimer.
- Trimmed all three tag lists toward entity names, alternate spellings, and misspellings.
- Updated `youtube-api/launch_manifest.json` to match the current title,
  descriptions, safer tags, `00:00` starts, and hour-format chapters.
- Corrected caption errors:
  - Episode 001: `leaker`/`Leaker` to `Lika`, `Smillion` to `Smiljan`, `Nicola Tesla` to `Nikola Tesla`.
  - Episode 002: `Nicola Tesla` to `Nikola Tesla`.
  - Episode 003: `Konsei`/garbled French expansion to ASCII `Conseil Europeen pour la Recherche Nucleaire`, `Winfred` to `Winfried`, spaced decimals like `7 .9` to `7.9`, `Berenstain Bear's` to `Berenstain Bears`, `Higgs Boson` to `Higgs boson`, and one isolated `Fabiola` to `Amara Fabiola`.

## Episode 001 SEO/AEO/GEO Review

### Keep

- Title is strong and entity-clear: `Tesla Died Alone. The Room Smelled Like Lightning.`
- First two description lines name Nikola Tesla, Room 3327, Hotel New Yorker, date, genre, and premise.
- Thumbnail is broad enough to work as a channel entry point.
- Disclaimer is strong and says the series is historical docufiction, not a factual documentary.

### Change Before Upload

- Done: tags were narrowed to Tesla/Room 3327/entity variants.
- Done: first chapter now starts with `00:00`; final chapter is now `1:14:49`.
- Done: disclaimer is the final paragraph before hashtags.
- Studio spot-check: first five minutes, `Smiljan`, `Lika`, `Office of Alien Property`, and final five minutes.

### AEO/GEO Additions

- Companion page should answer: what is historical docufiction, what real history appears, what is fictionalized, and whether the viewer needs prior episodes. Do not create `VideoObject` until the real YouTube URL exists.

### Monetization / Policy Notes

- Keep away from `cover-up`, `truth`, `exposed`, or graphic death framing.
- Select altered/synthetic disclosure as yes.
- Monetization cannot be enabled unless Studio shows YPP/Watch Page Ads access.

## Episode 002 SEO/AEO/GEO Review

### Keep

- First description line is strong: White City, World's Columbian Exposition, Chicago, Tesla, Westinghouse, Jackson Park, Manufactures Building, and docufiction.
- Thumbnail is click-driven but not tabloid.
- Disclaimer is visible and direct.

### Change Before Upload

- Done: tags were narrowed toward White City/World's Fair/entity variants.
- Done: title now names `Tesla`, `White City`, and `1893`.
- Done: first chapter now starts with `00:00`; over-60-minute chapters are now
  `1:15:19` and `1:19:42`.
- Done: disclaimer is the final paragraph before hashtags.
- Studio spot-check: `World's Columbian Exposition`, `Westinghouse`, `Manufactures Building`, `Jackson Park`, and final five minutes.

### AEO/GEO Additions

- Companion page should separate the real 1893 World's Fair history from the fictional letter/report/survey. Keep `historical docufiction` near the top.

### Monetization / Policy Notes

- Avoid mud-flood, hidden-history, or old-world certainty framing.
- Select altered/synthetic disclosure as yes.
- Monetization cannot be enabled unless Studio shows YPP/Watch Page Ads access.

## Episode 003 SEO/AEO/GEO Review

### Keep

- Title names both central entities: Tesla and CERN/God Particle.
- First description line gives a very clear entity map: Nikola Tesla, CERN, LHC, Higgs boson, Berenstain/Berenstein, Schumann resonance, Wardenclyffe.
- Disclaimer is especially important here and is already present.

### Change Before Upload

- Done: tags were narrowed toward CERN/LHC/Higgs/Berenstain-Schumann-Wardenclyffe variants.
- Done: first chapter now starts with `00:00`; final chapter is now `1:06:10`.
- Done: disclaimer is the final paragraph before hashtags.
- Done: caption entity and decimal errors were cleaned.
- Studio spot-check: `CERN`, `Higgs boson`, `Berenstain/Berenstein`, `Schumann`, `Wardenclyffe`, and final five minutes.

### AEO/GEO Additions

- Companion page should say plainly that the CERN/Tesla causal link is the fictional premise, not a factual science claim.

### Monetization / Policy Notes

- Avoid framing as proof that CERN changed reality.
- Select altered/synthetic disclosure as yes.
- Monetization cannot be enabled unless Studio shows YPP/Watch Page Ads access.

## Launch Timing Recommendation

Default target is Thursday, 2026-05-21 at 9:00 AM Mountain only if all three private uploads finish SD/HD/1440p processing, Checks, thumbnail/caption setup, and caption spot-checking before 8:30 AM Mountain.

If any upload is still processing, missing captions/thumbnails, blocked by feature eligibility, or has unresolved Checks by 8:30 AM Mountain, use the fallback next Thursday, 2026-05-28, at the same 9:00 / 9:15 / 9:30 AM Mountain stagger.

## Next Safe Action

Wait for the scheduled public release, then run the post-publish checklist:

1. Confirm all three public watch pages are live.
2. Pin the prepared episode comments.
3. Add end screens pointing to the launch playlist and another episode.
4. Post the prepared Community launch copy using the playlist URL.
5. Monitor and reply to first-hour comments.
