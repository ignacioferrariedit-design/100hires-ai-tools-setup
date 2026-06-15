"""Fetch a public YouTube transcript with Supadata and save it as Markdown."""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from dotenv import load_dotenv
from supadata import Supadata, SupadataError


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "research" / "youtube-transcripts"
ENV_VAR_NAME = "SUPADATA_API_KEY"


class TranscriptFetchError(Exception):
    """Raised for expected user-facing failures."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a native public YouTube transcript with Supadata."
    )
    parser.add_argument("--url", required=True, help="Public YouTube video URL.")
    parser.add_argument("--author", required=True, help="Expert or speaker name.")
    parser.add_argument("--title", required=True, help="Content title.")
    parser.add_argument(
        "--publication-date",
        required=True,
        help="Publication date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output Markdown filename, without a folder path.",
    )
    parser.add_argument(
        "--lang",
        default="en",
        help="Preferred transcript language. Defaults to en.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite an existing transcript file.",
    )
    return parser.parse_args()


def validate_youtube_url(raw_url: str) -> None:
    parsed = urlparse(raw_url)
    host = parsed.netloc.lower()
    valid_hosts = {
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
        "music.youtube.com",
        "youtu.be",
    }

    if parsed.scheme not in {"http", "https"} or host not in valid_hosts:
        raise TranscriptFetchError("The --url value must be a valid YouTube URL.")

    if host == "youtu.be" and not parsed.path.strip("/"):
        raise TranscriptFetchError("The YouTube URL does not include a video ID.")

    if host != "youtu.be" and parsed.path == "/watch" and "v=" not in parsed.query:
        raise TranscriptFetchError("The YouTube watch URL does not include a video ID.")


def validate_publication_date(raw_date: str) -> str:
    try:
        return datetime.strptime(raw_date, "%Y-%m-%d").date().isoformat()
    except ValueError as exc:
        raise TranscriptFetchError(
            "The --publication-date value must use YYYY-MM-DD format."
        ) from exc


def resolve_output_path(raw_output: str, overwrite: bool) -> Path:
    output_name = Path(raw_output)

    if output_name.name != raw_output:
        raise TranscriptFetchError(
            "The --output value must be a filename only, not a folder path."
        )

    if output_name.suffix.lower() != ".md":
        output_name = output_name.with_suffix(output_name.suffix + ".md")

    output_path = OUTPUT_DIR / output_name.name
    if output_path.exists() and not overwrite:
        raise TranscriptFetchError(
            f"Output file already exists: {output_path}. Use --overwrite to replace it."
        )

    return output_path


def load_api_key() -> str:
    load_dotenv(REPO_ROOT / ".env")

    from os import getenv

    api_key = getenv(ENV_VAR_NAME)
    if not api_key:
        raise TranscriptFetchError(
            f"Missing {ENV_VAR_NAME}. Add it to your local .env file before running."
        )
    return api_key


def get_field(response: Any, names: tuple[str, ...]) -> Any:
    if isinstance(response, dict):
        for name in names:
            if name in response:
                return response[name]
        return None

    for name in names:
        if hasattr(response, name):
            return getattr(response, name)

    return None


def ensure_synchronous_response(response: Any) -> None:
    job_id = get_field(response, ("job_id", "jobId"))
    status = get_field(response, ("status", "state"))

    if job_id:
        raise TranscriptFetchError(
            "Supadata returned an asynchronous job. This first version only supports "
            "immediate transcript content."
        )

    if isinstance(status, str) and status.lower() in {
        "queued",
        "pending",
        "processing",
        "running",
        "active",
    }:
        raise TranscriptFetchError(
            "Supadata returned an asynchronous job. This first version only supports "
            "immediate transcript content."
        )


def extract_transcript(response: Any, requested_language: str) -> tuple[str, str]:
    ensure_synchronous_response(response)

    if isinstance(response, str):
        transcript = response
        language = requested_language
    else:
        transcript = get_field(response, ("text", "transcript", "content"))
        language = get_field(response, ("language", "lang", "transcript_language"))

    if not isinstance(transcript, str) or not transcript.strip():
        raise TranscriptFetchError("Supadata did not return transcript text.")

    if not isinstance(language, str) or not language.strip():
        raise TranscriptFetchError("Supadata did not return a transcript language.")

    return transcript, language


def format_supadata_error(error: SupadataError) -> str:
    message = getattr(error, "message", None)
    if isinstance(message, str) and message.strip():
        return message.strip()

    return "Supadata request failed. Review the API response and your input values."


def fetch_transcript(api_key: str, video_url: str, language: str) -> tuple[str, str]:
    supadata = Supadata(api_key=api_key)
    response = supadata.transcript(
        url=video_url,
        lang=language,
        text=True,
        mode="native",
    )
    return extract_transcript(response, language)


def markdown_clean(value: str) -> str:
    return value.replace("\r\n", "\n").replace("\r", "\n").strip()


def build_markdown(
    *,
    title: str,
    author: str,
    url: str,
    publication_date: str,
    collection_date: str,
    language: str,
    transcript: str,
) -> str:
    clean_title = markdown_clean(title)
    clean_author = markdown_clean(author)
    clean_url = markdown_clean(url)
    clean_transcript = transcript.replace("\r\n", "\n").replace("\r", "\n").strip()

    return (
        f"# {clean_title}\n\n"
        f"* Author: {clean_author}\n"
        f"* Content title: {clean_title}\n"
        f"* Original source URL: {clean_url}\n"
        f"* Publication date: {publication_date}\n"
        "* Collection method: Supadata Python SDK using native YouTube transcript\n"
        f"* Collection date: {collection_date}\n"
        f"* Transcript language: {language}\n\n"
        "## Transcript\n\n"
        f"{clean_transcript}\n"
    )


def main() -> int:
    args = parse_args()

    try:
        validate_youtube_url(args.url)
        publication_date = validate_publication_date(args.publication_date)
        output_path = resolve_output_path(args.output, args.overwrite)
        api_key = load_api_key()

        transcript, transcript_language = fetch_transcript(
            api_key=api_key,
            video_url=args.url,
            language=args.lang,
        )

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            build_markdown(
                title=args.title,
                author=args.author,
                url=args.url,
                publication_date=publication_date,
                collection_date=date.today().isoformat(),
                language=transcript_language,
                transcript=transcript,
            ),
            encoding="utf-8",
        )
    except TranscriptFetchError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except SupadataError as exc:
        print(f"Supadata error: {format_supadata_error(exc)}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"File system error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Unexpected error: {exc.__class__.__name__}: {exc}", file=sys.stderr)
        return 1

    print(f"Transcript saved to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
