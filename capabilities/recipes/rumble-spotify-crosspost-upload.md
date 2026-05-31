---
id: rumble-spotify-crosspost-upload
name: Rumble Spotify Cross-Post Upload
schema_version: 2.1
profile: foundation
level: recipe
maturity: candidate
scope: Tesla Mandela Effects
currently_true: true
last_verified: 2026-05-31
tags:
  - rumble
  - spotify
  - upload
  - video podcast
  - release documentation
---

# Rumble Spotify Cross-Post Upload

## Use When

Uploading or drafting Tesla Mandela Effects Episodes 001-003 on Rumble and
Spotify after the YouTube launch.

## Inputs

- Workstream:
  `../../workstreams/rumble-spotify-crosspost-2026-05-31.md`
- Package:
  `../../14. RUMBLE SPOTIFY LAUNCH PACKAGE/README.md`
- Profile copy:
  `../../14. RUMBLE SPOTIFY LAUNCH PACKAGE/profile-copy.md`
- Episode metadata:
  `../../14. RUMBLE SPOTIFY LAUNCH PACKAGE/episode-metadata.md`
- Delivery summary:
  `../../14. RUMBLE SPOTIFY LAUNCH PACKAGE/delivery-summary-2026-05-29.md`

## Steps

1. Verify the active Rumble and Spotify account identities without reading or
   exposing secrets.
2. Confirm whether the user wants immediate publish or saved drafts if the
   current instruction is not explicit.
3. Update profile/show copy from `profile-copy.md`.
4. Upload Rumble files from `delivery/*-rumble-1440p-h264.mp4`.
5. Upload Spotify files from `delivery/*-spotify-1080p-h264.mp4`.
6. Use the titles, descriptions, tags, and chapters from `episode-metadata.md`.
7. Preserve the Episode 003 title as `S1E3`.
8. For Rumble, use `Rumble Player` unless explicitly changed.
9. For Spotify, prefer video podcast format and `History` as the first category
   if accepted.
10. Record URLs, IDs, publish/draft state, categories, licenses, and account
    identity checks in the package README and `PROJECT-STATUS.md`.
11. Update `tesla-mandela-queue.md`, `tesla-mandela-decisions.md`, and
    `lessons-learned.md` only for decisions or lessons actually made.
12. After uploads are complete and verified, ask before deleting local delivery
    MP4s if the user has not already approved cleanup of those payloads.

## Safety Boundaries

- Do not use host desktop control unless the user explicitly approves it for
  this task.
- Do not read cookies, OAuth tokens, credentials, billing pages, or secrets.
- Do not select exclusive licenses or YouTube-control options on Rumble without
  explicit approval.
- Do not claim Studio Analytics were reviewed unless private analytics were
  actually opened and recorded.
