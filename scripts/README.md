# Scripts

This folder contains scripts used to collect public research material through APIs.

## YouTube Transcript Collection

`fetch_youtube_transcript.py` retrieves an existing public YouTube transcript through the Supadata Python SDK and saves it as a Markdown file in `research/youtube-transcripts/`.

## Setup Requirements

Install the direct Python dependencies listed in the repository root:

```bash
pip install -r requirements.txt
```

Create a local `.env` file with the required Supadata API key:

```bash
SUPADATA_API_KEY=your_api_key_here
```

The script loads `SUPADATA_API_KEY` from `.env` with `python-dotenv`. The key is never hardcoded into the script, written to generated Markdown, or intentionally printed.

## Example Command

```bash
python scripts/fetch_youtube_transcript.py --url "YOUTUBE_URL" --author "AUTHOR_NAME" --title "VIDEO_TITLE" --publication-date "YYYY-MM-DD" --output "author-name_video-title_YYYY-MM-DD.md"
```

The script uses Supadata with `mode="native"`, which means it requests only an existing public transcript. This first version does not request AI-generated transcription and does not support asynchronous transcript jobs.

Only public videos with an available transcript can be processed. After a Markdown file is generated, it must be manually reviewed before being used as research material.

## Output Metadata

Generated transcript Markdown files include:

- Author
- Content title
- Original source URL
- Publication date
- Collection method
- Collection date
- Transcript language
