import argparse
import json
import os
import re
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


SCOPES = [
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube.upload",
]

API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
CLIENT_SECRET_SECTIONS = ("installed", "web")


def load_manifest(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_episode(manifest, episode_id):
    try:
        episode = manifest["episodes"][episode_id]
    except KeyError as exc:
        raise SystemExit(f"Episode {episode_id!r} is not in the manifest.") from exc
    defaults = manifest.get("defaults", {})
    merged = dict(defaults)
    merged.update(episode)
    return merged


def load_manifest_if_available(args):
    manifest_path = getattr(args, "manifest", None)
    if not manifest_path:
        return None
    try:
        return load_manifest(manifest_path)
    except (OSError, KeyError, json.JSONDecodeError):
        return None


def verify_file(path, label):
    value = Path(path)
    if not value.exists():
        raise SystemExit(f"{label} does not exist: {value}")
    return str(value)


def read_client_secret_metadata(path):
    client_secret_path = Path(path)
    if not client_secret_path.exists():
        raise SystemExit(f"OAuth client secret file does not exist: {client_secret_path}")

    try:
        data = json.loads(client_secret_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"OAuth client secret file is not valid JSON: {client_secret_path}") from exc

    section_name = next((name for name in CLIENT_SECRET_SECTIONS if name in data), None)
    if not section_name:
        raise SystemExit("OAuth client secret file does not contain an installed or web client section.")

    section = data[section_name]
    return {
        "type": section_name,
        "project_id": section.get("project_id"),
        "client_id": section.get("client_id"),
    }


def get_expected_project_id(args, manifest=None):
    explicit = getattr(args, "expected_project_id", None)
    if explicit:
        return explicit
    if manifest is None:
        manifest = load_manifest_if_available(args)
    if not manifest:
        return None
    return manifest.get("defaults", {}).get("expectedGoogleCloudProjectId")


def validate_client_secret_project(args, manifest=None):
    metadata = read_client_secret_metadata(args.client_secret)
    expected_project_id = get_expected_project_id(args, manifest)
    actual_project_id = metadata.get("project_id")
    if expected_project_id and actual_project_id != expected_project_id:
        raise SystemExit(
            "OAuth client project mismatch. "
            f"Expected Google Cloud project {expected_project_id}, but credentials/client_secret.json "
            f"belongs to {actual_project_id or 'an unknown project'}. "
            "Download a Desktop OAuth client JSON from the Tesla Mandela Effects project and replace "
            "credentials/client_secret.json."
        )
    return metadata


def validate_token_matches_client(token_path, client_metadata):
    if not token_path.exists():
        return
    try:
        token = json.loads(token_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"OAuth token file is not valid JSON: {token_path}") from exc

    token_client_id = token.get("client_id")
    client_id = client_metadata.get("client_id")
    if token_client_id and client_id and token_client_id != client_id:
        raise SystemExit(
            "OAuth token/client mismatch. credentials/token.json was created for a different OAuth client. "
            "Delete credentials/token.json and rerun auth with the current client_secret.json."
        )


def get_credentials(args):
    token_path = Path(args.token)
    manifest = load_manifest_if_available(args)
    client_metadata = validate_client_secret_project(args, manifest)
    validate_token_matches_client(token_path, client_metadata)
    credentials = None
    if token_path.exists():
        credentials = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if credentials and credentials.valid:
        return credentials

    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        credentials = run_oauth_flow(args)

    token_path.parent.mkdir(parents=True, exist_ok=True)
    token_path.write_text(credentials.to_json(), encoding="utf-8")
    return credentials


class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        if "error" in query:
            self.server.oauth_error = query["error"][0]
        else:
            self.server.authorization_response = f"http://localhost:{self.server.server_port}{self.path}"

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            b"<html><body><h1>YouTube API authorization received.</h1>"
            b"<p>You can close this browser tab and return to Codex.</p></body></html>"
        )

    def log_message(self, format, *args):
        return


def run_oauth_flow(args):
    # Installed-app OAuth is allowed to use a localhost HTTP redirect.
    # oauthlib requires this explicit opt-in for local desktop flows.
    os.environ.setdefault("OAUTHLIB_INSECURE_TRANSPORT", "1")

    client_secret = verify_file(args.client_secret, "OAuth client secret file")
    server = HTTPServer(("localhost", args.port), OAuthCallbackHandler)
    server.timeout = args.timeout

    flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
    flow.redirect_uri = f"http://localhost:{server.server_port}/"
    auth_url, _ = flow.authorization_url(
        access_type="offline",
        prompt="consent",
        include_granted_scopes="true",
    )

    if args.auth_url_file:
        auth_url_file = Path(args.auth_url_file)
        auth_url_file.parent.mkdir(parents=True, exist_ok=True)
        auth_url_file.write_text(auth_url, encoding="utf-8")

    print("Open this official Google OAuth URL if a browser did not open automatically:")
    print(auth_url, flush=True)

    if args.open_browser:
        webbrowser.open(auth_url, new=1)

    server.handle_request()
    if getattr(server, "oauth_error", None):
        raise SystemExit(f"OAuth failed: {server.oauth_error}")
    authorization_response = getattr(server, "authorization_response", None)
    if not authorization_response:
        raise SystemExit("OAuth timed out before Google returned a callback.")

    flow.fetch_token(authorization_response=authorization_response)
    return flow.credentials


def get_youtube(args):
    credentials = get_credentials(args)
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def print_json(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))


def get_expected_channel_id(args, manifest=None):
    explicit = getattr(args, "expected_channel_id", None)
    if explicit:
        return explicit
    if manifest is None:
        try:
            manifest = load_manifest(args.manifest)
        except (OSError, KeyError, json.JSONDecodeError):
            return None
    return manifest.get("defaults", {}).get("expectedChannelId")


def get_current_channel(youtube):
    response = youtube.channels().list(
        part="id,snippet,statistics,status",
        mine=True,
    ).execute()
    items = response.get("items", [])
    if not items:
        raise SystemExit("No YouTube channel was returned for this OAuth token.")
    return response, items[0]


def require_expected_channel(args, youtube, manifest=None):
    expected = get_expected_channel_id(args, manifest)
    if not expected:
        return None

    _, channel = get_current_channel(youtube)
    actual = channel.get("id")
    title = channel.get("snippet", {}).get("title", "unknown title")
    if actual != expected:
        raise SystemExit(
            "Authenticated channel mismatch. "
            f"Expected Tesla Mandela Effects ({expected}), but this token controls "
            f"{title} ({actual}). No upload or write action was attempted. "
            "Delete credentials/token.json and rerun auth with the correct Google or Brand Account access."
        )
    print(f"Authenticated channel verified: {title} ({actual})")
    return channel


def format_http_error(exc):
    content = getattr(exc, "content", b"")
    if isinstance(content, bytes):
        content = content.decode("utf-8", errors="replace")

    message = str(exc)
    reason = ""
    try:
        payload = json.loads(content)
        error = payload.get("error", {})
        message = error.get("message") or message
        details = error.get("details", [])
        reasons = [
            item.get("reason")
            for item in error.get("errors", [])
            if isinstance(item, dict) and item.get("reason")
        ]
        reason = ", ".join(reasons)
        if details:
            reason = reason or json.dumps(details, ensure_ascii=False)
    except (TypeError, json.JSONDecodeError):
        pass

    project_match = re.search(r"project\s+(\d+)", message)
    project = project_match.group(1) if project_match else None
    lines = [message]

    if "youtube.googleapis.com" in message and ("accessNotConfigured" in reason or "disabled" in message):
        if project:
            lines.append(
                "Action needed: enable YouTube Data API v3 for Google Cloud project "
                f"{project}: https://console.developers.google.com/apis/api/youtube.googleapis.com/overview?project={project}"
            )
        else:
            lines.append("Action needed: enable YouTube Data API v3 for this Google Cloud project.")
        lines.append("After enabling it, wait a minute or two, then rerun: python youtube_api_cli.py whoami")
    elif reason:
        lines.append(f"Reason: {reason}")

    return "\n".join(lines)


def cmd_auth(args):
    get_credentials(args)
    print(f"OAuth token ready: {args.token}")


def cmd_whoami(args):
    youtube = get_youtube(args)
    response, channel = get_current_channel(youtube)
    print_json(response)
    expected = get_expected_channel_id(args)
    if expected:
        actual = channel.get("id")
        title = channel.get("snippet", {}).get("title", "unknown title")
        if actual != expected:
            raise SystemExit(
                "Authenticated channel mismatch. "
                f"Expected Tesla Mandela Effects ({expected}), but this token controls {title} ({actual})."
            )
        print(f"Authenticated channel verified: {title} ({actual})")


def cmd_list_episodes(args):
    manifest = load_manifest(args.manifest)
    for episode_id, episode in manifest["episodes"].items():
        print(f"{episode_id}: {episode['title']}")
        print(f"  video: {episode['video_file']}")
        print(f"  thumbnail: {episode['thumbnail_file']}")
        print(f"  captions: {episode['caption_file']}")


def cmd_upload(args):
    manifest = load_manifest(args.manifest)
    episode = load_episode(manifest, args.episode)
    video_file = verify_file(episode["video_file"], "Video file")

    privacy_status = args.privacy_status or episode.get("privacyStatus", "private")
    if privacy_status != "private" and not args.allow_non_private:
        raise SystemExit(
            "Refusing non-private upload. Re-run with --allow-non-private if this is intentional."
        )

    body = {
        "snippet": {
            "title": episode["title"],
            "description": episode["description"],
            "tags": episode.get("tags", []),
            "categoryId": episode.get("categoryId", "1"),
            "defaultLanguage": episode.get("defaultLanguage", "en"),
        },
        "status": {
            "privacyStatus": privacy_status,
            "selfDeclaredMadeForKids": bool(episode.get("selfDeclaredMadeForKids", False)),
            "containsSyntheticMedia": bool(episode.get("containsSyntheticMedia", True)),
        },
    }

    if args.publish_at:
        body["status"]["publishAt"] = args.publish_at
        body["status"]["privacyStatus"] = "private"

    youtube = get_youtube(args)
    require_expected_channel(args, youtube, manifest)
    media = MediaFileUpload(video_file, chunksize=args.chunk_size, resumable=True)
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
        notifySubscribers=args.notify_subscribers,
    )

    print(f"Uploading Episode {args.episode}: {episode['title']}")
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload progress: {int(status.progress() * 100)}%")

    record = {
        "episode": args.episode,
        "video_id": response["id"],
        "title": episode["title"],
        "privacyStatus": response.get("status", {}).get("privacyStatus"),
    }
    append_upload_record(args.state, record)
    print_json(record)


def append_upload_record(path, record):
    state_path = Path(path)
    state = []
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
    state.append(record)
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def cmd_thumbnail(args):
    manifest = load_manifest(args.manifest)
    episode = load_episode(manifest, args.episode)
    thumbnail_file = verify_file(episode["thumbnail_file"], "Thumbnail file")
    youtube = get_youtube(args)
    require_expected_channel(args, youtube, manifest)
    response = youtube.thumbnails().set(
        videoId=args.video_id,
        media_body=MediaFileUpload(thumbnail_file),
    ).execute()
    print_json(response)


def cmd_caption(args):
    manifest = load_manifest(args.manifest)
    episode = load_episode(manifest, args.episode)
    caption_file = verify_file(episode["caption_file"], "Caption file")
    body = {
        "snippet": {
            "videoId": args.video_id,
            "language": args.language,
            "name": episode.get("caption_name", f"English captions - Episode {args.episode}"),
            "isDraft": args.draft,
        }
    }
    youtube = get_youtube(args)
    require_expected_channel(args, youtube, manifest)
    response = youtube.captions().insert(
        part="snippet",
        body=body,
        media_body=MediaFileUpload(caption_file, mimetype="application/x-subrip"),
    ).execute()
    print_json(response)


def cmd_video(args):
    youtube = get_youtube(args)
    response = youtube.videos().list(
        part="id,snippet,status,processingDetails,contentDetails",
        id=args.video_id,
    ).execute()
    print_json(response)


def cmd_create_playlist(args):
    youtube = get_youtube(args)
    require_expected_channel(args, youtube)
    body = {
        "snippet": {
            "title": args.title,
            "description": args.description or "",
        },
        "status": {
            "privacyStatus": args.privacy_status,
        },
    }
    response = youtube.playlists().insert(part="snippet,status", body=body).execute()
    print_json(response)


def cmd_add_to_playlist(args):
    youtube = get_youtube(args)
    require_expected_channel(args, youtube)
    body = {
        "snippet": {
            "playlistId": args.playlist_id,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": args.video_id,
            },
        }
    }
    response = youtube.playlistItems().insert(part="snippet", body=body).execute()
    print_json(response)


def add_common_args(parser):
    parser.add_argument(
        "--client-secret",
        default="credentials/client_secret.json",
        help="Path to OAuth Desktop client JSON from Google Cloud Console.",
    )
    parser.add_argument(
        "--token",
        default="credentials/token.json",
        help="Path where the OAuth token will be stored.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=0,
        help="Localhost OAuth callback port. Use 0 for an automatic free port.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="Seconds to wait for the OAuth browser callback.",
    )
    parser.add_argument(
        "--open-browser",
        action="store_true",
        help="Ask Python to open the official Google OAuth URL in the default browser.",
    )
    parser.add_argument(
        "--auth-url-file",
        default="credentials/auth-url.txt",
        help="Write the generated OAuth URL to this file.",
    )
    parser.add_argument(
        "--expected-channel-id",
        help="Refuse write actions unless OAuth resolves to this YouTube channel ID.",
    )
    parser.add_argument(
        "--expected-project-id",
        help="Refuse auth/API use unless the OAuth client JSON belongs to this Google Cloud project ID.",
    )


def build_parser():
    parser = argparse.ArgumentParser(description="Official YouTube Data API CLI for Tesla Mandela Effects.")
    parser.add_argument("--manifest", default="launch_manifest.json")
    parser.add_argument("--state", default="uploaded-videos.json")
    subparsers = parser.add_subparsers(dest="command", required=True)

    auth = subparsers.add_parser("auth", help="Run official Google OAuth for YouTube Data API.")
    add_common_args(auth)
    auth.set_defaults(func=cmd_auth)

    whoami = subparsers.add_parser("whoami", help="Show authenticated YouTube channel identity.")
    add_common_args(whoami)
    whoami.set_defaults(func=cmd_whoami)

    list_episodes = subparsers.add_parser("list-episodes", help="List local launch manifest episodes.")
    list_episodes.set_defaults(func=cmd_list_episodes)

    upload = subparsers.add_parser("upload", help="Upload one episode through videos.insert.")
    add_common_args(upload)
    upload.add_argument("episode", choices=["001", "002", "003"])
    upload.add_argument("--privacy-status", choices=["private", "unlisted", "public"])
    upload.add_argument("--allow-non-private", action="store_true")
    upload.add_argument("--publish-at", help="RFC3339 publish time for scheduled public release.")
    upload.add_argument("--notify-subscribers", action="store_true")
    upload.add_argument("--chunk-size", type=int, default=8 * 1024 * 1024)
    upload.set_defaults(func=cmd_upload)

    thumbnail = subparsers.add_parser("thumbnail", help="Set thumbnail through thumbnails.set.")
    add_common_args(thumbnail)
    thumbnail.add_argument("episode", choices=["001", "002", "003"])
    thumbnail.add_argument("video_id")
    thumbnail.set_defaults(func=cmd_thumbnail)

    caption = subparsers.add_parser("caption", help="Upload SRT caption through captions.insert.")
    add_common_args(caption)
    caption.add_argument("episode", choices=["001", "002", "003"])
    caption.add_argument("video_id")
    caption.add_argument("--language", default="en")
    caption.add_argument("--draft", action="store_true")
    caption.set_defaults(func=cmd_caption)

    video = subparsers.add_parser("video", help="Inspect a video through videos.list.")
    add_common_args(video)
    video.add_argument("video_id")
    video.set_defaults(func=cmd_video)

    playlist = subparsers.add_parser("create-playlist", help="Create a playlist through playlists.insert.")
    add_common_args(playlist)
    playlist.add_argument("title")
    playlist.add_argument("--description")
    playlist.add_argument("--privacy-status", choices=["private", "unlisted", "public"], default="public")
    playlist.set_defaults(func=cmd_create_playlist)

    playlist_item = subparsers.add_parser("add-to-playlist", help="Add a video to a playlist through playlistItems.insert.")
    add_common_args(playlist_item)
    playlist_item.add_argument("playlist_id")
    playlist_item.add_argument("video_id")
    playlist_item.set_defaults(func=cmd_add_to_playlist)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except HttpError as exc:
        print(format_http_error(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
