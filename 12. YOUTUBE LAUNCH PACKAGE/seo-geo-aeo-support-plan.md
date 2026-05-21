# SEO / GEO / AEO Support Plan

## The Plain-English Reality

There is no metadata trick that forces YouTube notifications. For notifications, the practical controls are:

- publish to subscriptions feed and notify subscribers;
- stay within YouTube's 3 upload/live notifications per channel per 24 hours;
- schedule cleanly after processing completes;
- do not use Premiere for these 1440p files unless separate 1080p Premiere exports are made;
- make the first public hour count with comments, pinned questions, and playlist chaining.

SEO/GEO/AEO support should make the videos easy for YouTube, Google, and AI search systems to understand:

- exact entities in the title, first description lines, chapters, tags, captions, and companion pages;
- clear docufiction disclaimer so the channel is classified as story/mystery, not factual conspiracy content;
- answer-shaped sections that AI search can quote without mangling the premise;
- stable thumbnails, playlist names, and watch-page embeds if a website exists.

## YouTube Discovery Stack

Use this priority order:

1. Title and thumbnail: create the click.
2. First two description lines: name the exact entities and genre.
3. Captions/transcript: give YouTube the full searchable text.
4. Chapters: create key moments for YouTube and Google.
5. Playlist/end screens: create session time after the click.
6. Pinned comment: create a discussion prompt.
7. Tags: cover misspellings, alternate names, and entity variants.

## Companion Page Template

If there is a website or Substack, create one indexed page per episode. Each page should embed the YouTube video after it is public.

Page title:

`Tesla Mandela Effects Episode 001: Tesla Died Alone. The Room Smelled Like Lightning.`

Page structure:

- H1: exact YouTube title.
- One-sentence answer: what the episode is.
- Embedded YouTube video.
- Short docufiction disclaimer.
- Episode summary, 150-250 words.
- Key entities list.
- Chapters/key moments.
- "Is this a factual documentary?" answer block.
- "What real history appears in this episode?" answer block.
- "What parts are speculative or fabricated for story?" answer block.
- Full transcript or cleaned transcript excerpt if available.
- Links to the full playlist and next episode.

## Answer Blocks

Use direct Q&A sections. These are for AEO/GEO and also help skeptical viewers.

### Is Tesla Mandela Effects a factual documentary?

No. Tesla Mandela Effects is historical docufiction. It uses documented events from Nikola Tesla's life and real historical entities, but it also includes speculative reconstruction and fictional sources for narrative purposes.

### What is historical docufiction?

Historical docufiction is storytelling that uses documentary texture, real places, real dates, and real historical figures while openly including fictional reconstruction. The goal is an immersive investigation, not a factual claim that every source exists.

### Should viewers treat the fabricated sources as real?

No. The series is designed as an immersive narrative. The description and channel framing should always say that some sources are created for storytelling.

## Episode Entity Targets

### Episode 001

- Nikola Tesla
- Hotel New Yorker
- Room 3327
- Office of Alien Property
- Tesla papers
- Tesla pigeons
- Smiljan
- historical docufiction
- Mandela Effect

### Episode 002

- World's Columbian Exposition
- White City Chicago
- Nikola Tesla
- Westinghouse
- Jackson Park
- Museum of Science and Industry
- Daniel Burnham
- Manufactures Building
- staff construction
- historical docufiction

### Episode 003

- Nikola Tesla
- CERN
- Large Hadron Collider
- Higgs boson
- God Particle
- Berenstain Bears
- Berenstein Bears
- Schumann resonance
- Colorado Springs
- Wardenclyffe Tower
- Mandela Effect

## Structured Data For Companion Pages

Use `VideoObject` only after the YouTube watch URL and thumbnail are known. Keep `name`, `description`, `thumbnailUrl`, and `embedUrl` consistent with the YouTube metadata.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "PASTE_EXACT_YOUTUBE_TITLE",
  "description": "PASTE_SHORT_EPISODE_DESCRIPTION",
  "thumbnailUrl": ["PASTE_STABLE_THUMBNAIL_URL"],
  "uploadDate": "2026-05-21T15:00:00-04:00",
  "duration": "PT1H16M59S",
  "embedUrl": "https://www.youtube.com/embed/VIDEO_ID",
  "genre": "Historical docufiction",
  "isFamilyFriendly": true
}
</script>
```

Do not invent the YouTube URL or `VIDEO_ID` before upload. Fill it in after the scheduled upload creates the private/scheduled video entry.

## Post-Launch External Support

Within the first 24 hours:

- Add each watch URL to the companion page.
- Add each video to the full-episode playlist.
- Post one YouTube Community post pointing to the three-episode launch.
- Pin the prepared question on each episode.
- Reply to every good-faith comment.

Within the first week:

- Publish one companion page per episode.
- Submit or inspect the companion pages in Google Search Console if a site exists.
- Add the playlist link to each companion page and the channel About section.
- Start thumbnail Test & Compare once the videos are public and eligible.
- Review YouTube Analytics for traffic source, CTR, retention, and subscriber conversion.

## What Not To Do

- Do not stuff hashtags or tags into the description.
- Do not use "truth," "exposed," "cover-up," or "they do not want you to know" framing.
- Do not describe fabricated sources as verified.
- Do not publish Episode 3 from the old 32-minute V2 file. Use the verified V3 file only.
- Do not upload more than three videos or live streams in the same 24-hour notification window.
