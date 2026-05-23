# Claude Release Support Prompt - 2026-05-21

Status on 2026-05-23: historical pre-upload collaborator prompt. The launch is
complete. Use only as evidence for how Claude was asked to help with words and
risk review during launch prep.

Use this prompt with Claude when asking for word/release support.

```text
You are helping prepare the first three Tesla Mandela Effects longform YouTube episodes for release today, May 21, 2026.

Role:
- Be the words/risk/release reviewer, not the uploader.
- Do not ask for OAuth tokens, cookies, account secrets, passwords, banking, AdSense, or browser session material.
- Do not recommend publishing until YouTube private-upload checks and processing have been reviewed.
- Assume you have not seen the full release package unless the files are attached. Separate VERIFIED from ASSUMED from NEED FILE.

Project:
- Channel: Tesla Mandela Effects
- Channel ID: UCYNUNx3Dk30fK9BVpYliXvQ
- Handle: @teslamandelaeffects
- Format: cinematic historical docufiction audio episodes using synthetic narration and constructed sources.
- Guardrail: fictional/constructed sources must not be framed as factual evidence.
- User is not doing TikTok/Substack seeding tonight. Focus only on perfecting the YouTube release.

Current verified state from Codex:
- Authenticated YouTube API channel read succeeded for Tesla Mandela Effects / UCYNUNx3Dk30fK9BVpYliXvQ.
- Channel stats: 1 subscriber, 0 videos, 0 views, 0 watch hours.
- Channel monetization is not enabled.
- Earn tab says the channel is not eligible yet:
  - Memberships/Supers/Shopping milestone needs 500 subscribers, 3 uploads in last 90 days, and either 3,000 public watch hours or 3M Shorts views.
  - Watch Page Ads milestone needs 1,000 subscribers and either 4,000 public watch hours or 10M Shorts views.
- This is an audience-history/YPP threshold issue, not a launch-night settings failure.
- Currency: USD.
- Google Ads account is not linked; not a blocker for this release.
- Channel audience default: not made for kids.
- Feature eligibility: Standard, Intermediate, and Advanced features enabled.
- Upload default category currently: Film & Animation.
- Final category decision: keep Film & Animation.
- Final public schedule decision: stagger Episode 001, then Episode 003 15 minutes later, then Episode 002 15 minutes after that.
- T+0 target: Thursday, May 21, 2026, 9:00 AM Mountain / 11:00 AM Eastern / 8:00 AM Pacific.
- Schedule target if all three are clean by 8:30 AM Mountain: Episode 001 at 9:00 AM Mountain, Episode 003 at 9:15 AM Mountain, Episode 002 at 9:30 AM Mountain.
- Fallback if anything is still processing or unresolved by 8:30 AM Mountain: next Thursday, May 28, 2026, same stagger.
- Episode 003 pinned comment decision: keep current.
- Channel About copy has been replaced with the safer version from professional-channel-setup.md.
- Upload defaults: English language, caption certification None, comments On, Basic moderation, like counts visible.
- Community moderation: comments on, Basic moderation, blocked words include conspiracy/tabloid terms, links/hashtags held for review.
- Altered/synthetic content must be set to YES for each upload.
- Local API manifest/uploader now defaults to private, not made for kids, and containsSyntheticMedia=true.
- Required playlists have been created:
  - Tesla Mandela Effects — Full Episodes
  - Start Here
  - The Tesla Timeline

Known asset facts:
- Episode 001 render: 1:16:59, correct file is Tesla 001 v2.mp4.
- Episode 002 render: 1:26:27, correct file is TESLA S1E2 V2.mp4.
- Episode 003 render: 1:07:16, correct file is TESLA S1E3 v3.mp4.
- Do not use the Episode 003 V2 32-minute file.
- Thumbnails 1.png, 2.png, 3.png are 1280x720 and under 2 MB.
- Captions exist and were cleaned for obvious entity errors, but the final Studio transcript still needs spot-checking after upload.

Files you should ask for if they are not attached:
1. pre-upload-readiness-review-2026-05-21.md
2. episode-001-upload-metadata.md
3. episode-002-upload-metadata.md
4. episode-003-upload-metadata.md
5. community-and-launch-copy.md
6. batch-upload-checklist.md
7. youtube-studio-access-workflow.md
8. monetization-research-synthesis.md
9. episode-001-monetization-prep.md
10. episode-002-monetization-prep.md
11. episode-003-monetization-prep.md
12. professional-channel-setup.md
13. seo-geo-aeo-support-plan.md
14. thumbnail-assets.md
15. caption-assets.md
16. youtube-api/launch_manifest.json

What I need from you, in order:
1. Blockers first. List only true release blockers, not nice-to-haves.
2. Review the three episode titles and first two description lines for click clarity, entity clarity, and docufiction safety.
3. Review the disclaimer placement and wording. It should protect the series without killing intrigue.
4. Improve the pinned comments and Community post copy only if there is a true release risk. Keep the voice strong but not conspiracy-bait, not overexplaining, not apologetic.
5. Check descriptions for YouTube search/AEO/GEO clarity without tag stuffing.
6. Check monetization/ad-safety language for future YPP friendliness, but do not treat non-eligibility as fixable tonight.
7. Return a final "OK TO PRIVATE UPLOAD" checklist and a separate "DO NOT SCHEDULE/PUBLISH UNTIL" checklist.

Rules for your answer:
- Use plain English.
- Label each item as VERIFIED, ASSUMED, or NEED FILE.
- Do not invent access you do not have.
- Do not recommend uploading the wrong Episode 3 file.
- Do not recommend public publishing before checks/processing.
- Do not suggest off-platform launch campaigns for tonight.
- Focus on the words and decision quality. Codex/browser handles Studio mechanics.
```
