# Official YouTube Data API CLI

This folder is for an official API connection only. It uses Google's OAuth flow and the YouTube Data API v3.

It does not use browser scraping, desktop automation, unofficial upload tools, cookies, or saved browser sessions.

Status on 2026-05-23: the first three launch videos are already public. Use
`..\POST_LAUNCH_HANDOFF_2026-05-23.md` and `..\launch-video-urls.md` for
durable video IDs, comment IDs, playlists, and remaining Studio-only tasks.
Generated upload result JSON, upload logs, PID files, and `__pycache__` are
runtime byproducts and should not be committed.

## What This Can Do

- Confirm the authenticated YouTube channel with `channels.list`.
- Upload videos with `videos.insert`.
- Set metadata during upload.
- Set thumbnails with `thumbnails.set`.
- Upload SRT captions with `captions.insert`.
- Create playlists with `playlists.insert`.
- Add videos to playlists with `playlistItems.insert`.
- Inspect video status with `videos.list`.

## What This Cannot Replace

- YouTube Studio Earn/YPP review.
- Monetization module acceptance.
- AdSense/payment setup.
- Ad suitability self-certification UI.
- Copyright/ad checks UI.
- End screens/cards if they are not exposed for the needed action.
- Contract acceptance.

Important official API constraint: Google says videos uploaded through `videos.insert` from unverified API projects created after July 28, 2020 are restricted to private viewing mode until the API project passes audit. For launch safety, this CLI defaults to private upload.

## Official Docs

- OAuth for desktop apps: `https://developers.google.com/youtube/v3/guides/auth/installed-apps`
- API auth overview: `https://developers.google.com/youtube/v3/guides/authentication`
- Upload videos: `https://developers.google.com/youtube/v3/docs/videos/insert`
- Set thumbnails: `https://developers.google.com/youtube/v3/docs/thumbnails/set`
- Upload captions: `https://developers.google.com/youtube/v3/docs/captions/insert`
- Playlists: `https://developers.google.com/youtube/v3/docs/playlists/insert`
- Playlist items: `https://developers.google.com/youtube/v3/docs/playlistItems/insert`

## Setup

Use the Tesla Mandela Effects Google Cloud project:

- Project ID: `tesla-mandela-effects`
- Project number: `995465249984`

1. Select the Google Cloud project above.
2. Enable `YouTube Data API v3`.
3. Configure OAuth consent.
4. Create an OAuth Client ID for a desktop app.
5. Download the client JSON.
6. Save it here:

`12. YOUTUBE LAUNCH PACKAGE/youtube-api/credentials/client_secret.json`

Do not paste the client secret into chat.

The current CLI checks that `client_secret.json` belongs to `tesla-mandela-effects`. If it belongs to any other project, API commands stop before upload.

If OAuth shows `Error 403: access_denied` and says the app is being tested, go to Google Auth Platform -> Audience -> Test users and add the Google account you are using for authorization. For this setup, add `cameronbpaul@gmail.com` and any separate Google account that owns or manages the Tesla Mandela Effects Brand Account.

## Install

From this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Authenticate

```powershell
.\.venv\Scripts\python .\youtube_api_cli.py auth --open-browser
```

This starts Google's official OAuth flow in a browser. Choose the correct YouTube account/channel.

For this launch, the manifest pins the expected channel ID:

`UCYNUNx3Dk30fK9BVpYliXvQ`

Write actions refuse to continue unless the API confirms that exact channel. If OAuth signs into a personal channel or another Brand Account, delete `credentials/token.json` and rerun auth.

After replacing `credentials/client_secret.json` with a client from the Tesla project, delete `credentials/token.json` if it exists. Tokens are tied to the OAuth client that created them.

If the OAuth consent screen says another project name, such as `aicompliance`, that is the Google Cloud/OAuth app branding. It is not automatically the YouTube channel being managed. The channel is determined by the Google/Brand Account selected during OAuth and confirmed by `whoami`.

Important channel-access limitation: YouTube Studio channel permissions are not the same as Brand Account ownership for API access. YouTube says invited Studio-permission users can manage in YouTube/Studio but cannot manage through YouTube APIs. For API uploads, authenticate as the Google account that directly owns the channel or owns/manages the Brand Account connected to the channel.

If no browser opens, the CLI writes the URL here:

`credentials/auth-url.txt`

Open that URL manually while the auth command is still running.

## Verify Channel

```powershell
.\.venv\Scripts\python .\youtube_api_cli.py whoami
```

If this says `YouTube Data API v3 has not been used ... or it is disabled`, enable `YouTube Data API v3` in the Google Cloud project named in the error, wait a minute or two, and rerun `whoami`.

## List Prepared Episodes

```powershell
.\.venv\Scripts\python .\youtube_api_cli.py list-episodes
```

## Private Upload

Use private first. Do not public-launch from the CLI until Studio checks are reviewed.

```powershell
.\.venv\Scripts\python .\youtube_api_cli.py upload 001
.\.venv\Scripts\python .\youtube_api_cli.py upload 002
.\.venv\Scripts\python .\youtube_api_cli.py upload 003
```

The CLI writes uploaded video IDs to `uploaded-videos.json`.

## Add Thumbnail And Captions

Replace `VIDEO_ID` with the ID returned by upload.

```powershell
.\.venv\Scripts\python .\youtube_api_cli.py thumbnail 001 VIDEO_ID
.\.venv\Scripts\python .\youtube_api_cli.py caption 001 VIDEO_ID
```

## Inspect Uploaded Video

```powershell
.\.venv\Scripts\python .\youtube_api_cli.py video VIDEO_ID
```

## Safe Launch Rule

The CLI can get files into YouTube privately. Studio is still the final gate for processing, checks, monetization status, and publishing decisions.
