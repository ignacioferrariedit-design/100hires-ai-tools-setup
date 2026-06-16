# AI-Powered SEO Content Production for B2B SaaS

## Project Objective

This repository organizes research for a hiring-focused project on AI-powered SEO content production for B2B SaaS. The goal is to understand what skills, workflows, judgment, and quality controls are needed to build useful AI-assisted content systems without relying on generic content volume.

The research focuses on practical evidence from SEO, content strategy, AI search, technical search systems, conversion-focused content, distribution, and commercial measurement.

## Research Scope

The project covers public source material related to:

- AI-assisted SEO research, outlining, drafting, editing, and content updates.
- AI search optimization, GEO, AEO, LLMO, and generative search visibility.
- B2B SaaS content operations, product-led SEO, and distribution.
- Passage-level clarity, structured answers, citations, and brand mentions.
- Content gap analysis for product, use-case, comparison, pricing, and landing pages.
- AI-search measurement, including citations, conversions, pipeline, and revenue.

The canonical source index is [research/sources.md](research/sources.md).

## Selected Experts

- Ryan Law: Selected for his concrete production workflow for SEO content research, outlining, drafting, internal linking, product integration, fact verification, and content updates.
- Aleyda Solis: Selected for her practical frameworks comparing traditional SEO, AI search optimization, and scalable organic growth.
- Mike King: Selected for his technical systems perspective on generative search, retrieval, personalization, passage-level relevance, and citations.
- Kevin Indig: Selected for his technical and growth SEO perspective on automation for scalable research, insight extraction, ideation, draft generation, and programmatic workflows.
- Andy Crestodina: Selected for his conversion-focused approach to using AI for webpage content gap analysis, buyer questions, objections, and evidence.
- Ross Simmonds: Selected for his expertise in B2B SaaS content strategy, distribution, SEO, AI-driven discovery, and repurposing expert assets across channels.
- Bernard Huang: Selected for his strategic view that AI should improve intelligence, semantic coverage, knowledge structure, originality, and brand recognition rather than automate content volume.
- Lily Ray: Selected for her work connecting established SEO foundations with AI-search visibility tactics, brand authority, citations, and expanded measurement.
- Gael Breton: Selected for his practical SEO experimentation, digital publishing systems, content operations, and testing AI workflows against business outcomes.
- Patrick Stox: Selected for his measurement perspective on AI-search traffic, signups, conversions, citations, landing-page performance, and downstream revenue.

## Research Methodology

OpenAI Codex in Cursor was used to assist with repository operations, file organization, structured research collection, and documentation updates.

YouTube transcripts were collected through Supadata using the repository's Python script, [scripts/fetch_youtube_transcript.py](scripts/fetch_youtube_transcript.py). The script stores transcript Markdown files in [research/youtube-transcripts/](research/youtube-transcripts/).

LinkedIn posts, public articles, public presentations, podcasts, show notes, and public transcripts were reviewed manually. Research notes and summaries in this repository are original and do not reproduce complete copyrighted sources.

## Source Types Collected

- YouTube interview transcripts collected through Supadata.
- Public LinkedIn post research notes.
- Public web article research notes.
- Public technical article research notes.
- Public presentation, transcript, and research notes.
- Public podcast interview, show notes, transcript, and research notes.
- Public data study research notes.

## Repository Structure

- [research/sources.md](research/sources.md): The master index of the selected topic, expert selection criteria, selected experts, documented sources, source URLs, local research files, collection methods, rationales, and relevance notes.
- [research/linkedin-posts/](research/linkedin-posts/): Original research notes based on public LinkedIn posts.
- [research/youtube-transcripts/](research/youtube-transcripts/): Markdown transcript files collected from publicly available YouTube videos.
- [research/other/](research/other/): Original notes for public articles, studies, presentations, podcast pages, show notes, and public transcripts that do not fit the LinkedIn or YouTube transcript folders.
- [scripts/](scripts/): Python scripts and documentation for collecting public research material through APIs. See [scripts/README.md](scripts/README.md).

## Transcript Collection Workflow

The transcript workflow uses Python, `supadata`, and `python-dotenv`.

Install dependencies from the repository root:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create a local `.env` file in the repository root and add the Supadata API key:

```text
SUPADATA_API_KEY=your_api_key_here
```

Do not commit `.env` or expose the API key. The script reads `SUPADATA_API_KEY` through `python-dotenv`.

Example Windows command:

```powershell
.\.venv\Scripts\python.exe scripts\fetch_youtube_transcript.py --url "YOUTUBE_URL" --author "AUTHOR_NAME" --title "VIDEO_TITLE" --publication-date "YYYY-MM-DD" --output "author-name_video-title_YYYY-MM-DD.md"
```

The script requests native public YouTube transcripts through Supadata with `mode="native"`. It does not request AI-generated transcription and does not support asynchronous transcript jobs. Generated Markdown files should be manually reviewed before being used as research material.

## Cross-Source Findings

- AI should augment human expertise rather than mass-produce generic content.
- Original research, proprietary data, customer evidence, and expert viewpoints create defensibility.
- Clear passage-level answers and structured information support both traditional and generative search.
- Discovery now happens across Google, AI assistants, LinkedIn, YouTube, Reddit, podcasts, and communities.
- Strong primary assets can be repurposed into multiple formats with AI.
- Human review is required for accuracy, positioning, evidence, and editorial quality.
- AI-search measurement should include citations, visibility, conversions, pipeline, and revenue, not traffic alone.

## Security and Responsible Use

The repository is configured to exclude `.env`, API keys, virtual environments, Python cache folders, and compiled Python files from Git through [.gitignore](.gitignore).

No real API key, password, token, or private credential should be committed. AI-generated or AI-assisted output requires human verification before it is treated as reliable research, published content, or hiring guidance.

## Limitations

This repository contains a curated set of public sources, not an exhaustive literature review. Some materials are summaries or notes based on public pages, presentations, podcasts, show notes, or transcripts. The research reflects the collected materials and should be revisited as AI search systems, SEO tools, attribution methods, and platform behavior change.

Transcript collection depends on public transcript availability and Supadata API behavior. Sources without public transcripts or sources requiring asynchronous processing may not be collectible with the first version of the script.

## Copyright and Attribution

This repository is for research organization and analysis. It links to original public sources and includes original summaries, notes, metadata, and locally collected transcript files where permitted by the collection workflow.

Research notes do not reproduce complete copyrighted articles, LinkedIn posts, slide decks, podcast transcripts, or datasets. Readers should consult the linked original sources for the authors' full arguments, examples, methodology, and supporting evidence.
