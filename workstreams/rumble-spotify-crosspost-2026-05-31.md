# Rumble / Spotify Cross-Post Handoff - 2026-05-31

## Objective

Move the first three completed Tesla Mandela Effects episodes from the YouTube
launch package into Rumble and Spotify with platform-specific profile copy,
episode metadata, delivery files, and clean project documentation.

## Account Context

The user is moving this work from the `locallytwisted@gmail.com` business
account context to the `cameronbpaul@gmail.com` personal account context.

Before any live action:

- verify the active Rumble account without exposing secrets;
- verify the active Spotify account without exposing secrets;
- verify whether the user wants publish-now or save-draft behavior;
- do not assume an already-open browser tab is safely automatable.

## Current Status

Ready:

- Rumble and Spotify profile copy is drafted in
  `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/profile-copy.md`.
- Rumble and Spotify episode metadata is drafted in
  `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/episode-metadata.md`.
- Platform requirement notes live in
  `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/platform-requirements-and-assets.md`.
- Upload-safe H.264/AAC delivery files were generated and verified locally.
  Details live in
  `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/delivery-summary-2026-05-29.md`.

Not done:

- No Rumble profile edit was made.
- No Spotify profile edit was made.
- No Rumble upload was started.
- No Spotify upload was started.
- No YouTube title correction was made.

## Source Order

1. `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/README.md`
2. `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/episode-metadata.md`
3. `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/profile-copy.md`
4. `../14. RUMBLE SPOTIFY LAUNCH PACKAGE/delivery-summary-2026-05-29.md`
5. `../12. YOUTUBE LAUNCH PACKAGE/POST_LAUNCH_HANDOFF_2026-05-23.md`
6. `../12. YOUTUBE LAUNCH PACKAGE/launch-video-urls.md`

## Decisions To Preserve

- Copy should lead with discoverable hooks: Nikola Tesla, Mandela Effect,
  lost papers, Hotel New Yorker, White City, CERN, God Particle, archive
  anomalies, and historical mystery.
- The docufiction disclaimer stays visible, but it is not the hook.
- Episode 003 must be labeled `S1E3` on new platforms.
- Rumble default license is `Rumble Player` unless the user chooses otherwise.
  Do not choose any license that gives Rumble YouTube channel control without
  explicit approval.
- Spotify default is video podcast using the 1080p delivery files. Prefer
  `History` if Spotify accepts the show framing; fall back to `Fiction` only if
  platform/category review forces the format lane.

## Upload Checklist

1. Verify active account identity in Rumble and Spotify.
2. Confirm publish-now versus save-draft behavior with the user if it is not
   obvious from the session.
3. Apply profile/show copy from `profile-copy.md`.
4. Rumble uploads:
   - use `delivery/TME-S1E1-rumble-1440p-h264.mp4`;
   - use `delivery/TME-S1E2-rumble-1440p-h264.mp4`;
   - use `delivery/TME-S1E3-rumble-1440p-h264.mp4`;
   - use titles, descriptions, and tags from `episode-metadata.md`;
   - choose `Rumble Player` unless explicitly changed.
5. Spotify uploads:
   - use `delivery/TME-S1E1-spotify-1080p-h264.mp4`;
   - use `delivery/TME-S1E2-spotify-1080p-h264.mp4`;
   - use `delivery/TME-S1E3-spotify-1080p-h264.mp4`;
   - use titles, descriptions, and chapters from `episode-metadata.md`;
   - keep the category decision in the show/package docs.
6. Use matching YouTube thumbnails from `../13. YOUTUBE THUMBNAILS/` unless a
   platform-specific image is created.
7. After publish or draft creation, record:
   - platform URL;
   - platform ID if visible;
   - account verified;
   - category/license choices;
   - publish or draft state;
   - date/time checked;
   - any manual follow-up needed.

## Known Issue From YouTube Review

Public YouTube metadata on 2026-05-29 returned Episode 003 as:

`S1E1 Tesla Found the Frequency. CERN Found the God Particle.`

The intended title is:

`S1E3 Tesla Found the Frequency. CERN Found the God Particle.`

Do not copy the wrong numbering to Rumble or Spotify. Correct YouTube when
Studio/API access is approved.

## Cleanup Boundary

Delivery MP4s are large local upload payloads and are ignored by Git. Keep them
until uploads are complete. Transcode logs, status JSON, and delivery manifests
were transient runtime state and were removed after the durable summary was
written.

## Backlinks

- Project status: `../PROJECT-STATUS.md`
- Queue: `../tesla-mandela-queue.md`
- Decisions: `../tesla-mandela-decisions.md`
- Lessons: `../lessons-learned.md`
- Project capability: `../capabilities/cards/platform-crosspost-release.md`
