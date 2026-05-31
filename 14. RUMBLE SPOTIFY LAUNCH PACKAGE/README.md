# Rumble / Spotify Launch Package

Date: 2026-05-29
Handoff updated: 2026-05-31

This folder is the working source for cross-posting the first three Tesla
Mandela Effects episodes to Rumble and Spotify.

Current account context: the project is moving from the
`locallytwisted@gmail.com` business account context to the
`cameronbpaul@gmail.com` personal account context. Verify the active account on
Rumble and Spotify before changing profiles, creating drafts, or publishing.

## Current Decision

Do not blindly copy the YouTube drop into Rumble and Spotify.

Public YouTube metadata and counters are useful, but they are not the full
launch signal. The public data is still tiny and cannot answer CTR, retention,
traffic source, subscriber conversion, or geography. It did reveal one
important consistency issue: Episode 003 is currently returned by public
YouTube metadata as `S1E1 Tesla Found the Frequency. CERN Found the God
Particle.` New platform metadata should use `S1E3`, and the YouTube title
should be corrected if Studio/API access is approved.

Copy mode was sharpened on 2026-05-29 after review. Current profile and episode
metadata should lead with Tesla, Mandela Effect, historical mystery,
science-history, lost records, strange architecture, and archive anomalies.
The docufiction disclaimer stays present, but it should not be the hook.

## Read Order

1. `../PROJECT-STATUS.md`
2. `../workstreams/rumble-spotify-crosspost-2026-05-31.md`
3. `youtube-data-review-2026-05-29.md`
4. `platform-requirements-and-assets.md`
5. `profile-copy.md`
6. `episode-metadata.md`
7. `delivery-summary-2026-05-29.md`
8. `asset-export-commands.md`

## Verified

- The three YouTube videos are public.
- Public counters increased since the 2026-05-23 closeout.
- The correct local master files exist.
- Episode 003 V3 remains the correct full-length file.
- Spotify and Rumble requirements were refreshed against current platform
  docs where official docs were available.
- Upload-safe Rumble and Spotify H.264 derivatives were generated locally on
  2026-05-29. See `delivery-summary-2026-05-29.md`.
- Transcode logs, status JSON, and manifest JSON were removed after the durable
  delivery summary was recorded.

## Not Done

- No Rumble profile changes were made.
- No Spotify profile changes were made.
- No Rumble uploads were started.
- No Spotify uploads were started.
- No YouTube title correction was made.
- No private YouTube Studio Analytics were read.
- No live account changes were made from the personal account handoff.

## Approval Needed

1. Rumble license: recommended default is `Rumble Player`, because it is
   non-exclusive and monetizes on Rumble without giving Rumble YouTube control.
2. Spotify format: recommended default is video podcast episodes, not
   audio-only, using 1080p H.264 derivatives.
3. Spotify category: prefer `History` if the platform accepts the docufiction
   framing; use `Fiction` only if category review forces the format lane.
4. YouTube fix: approve correcting Episode 003 from `S1E1` to `S1E3`.
5. Publishing mode: approve whether to publish immediately or save drafts first.

## Browser Access Note

The accounts may be open in Brave, but this session does not have safe
app-level access to those Brave tabs. Brave was not launched with a remote
debugging port. Use browser UI manually, move the sessions to an automatable
Chrome/Studio lane, or approve an official API path where a platform supports
it.

Do not use host desktop control for profile edits or uploads unless the user
explicitly approves that input-risk path for the task.
