# NK Udada Foundation Website

A fast, static website for NK Udada Foundation, built for GitHub Pages.

The site highlights the foundation's mission, impact, programs, team, volunteer sign-up, and a media gallery sourced from optimized assets.

## Overview

- Tech stack: HTML, CSS, vanilla JavaScript
- Hosting target: GitHub Pages
- Entry point: `index.html`
- Gallery source of truth: `media_manifest.json`

## Features

- Fully static and deployment-friendly (no build step required)
- Responsive single-page layout
- Manifest-driven gallery for images and videos
- Media optimization pipeline for performance-conscious assets

## Repository Structure

```text
.
├── index.html
├── media_manifest.json
├── README.md
├── assets/
│   ├── images/
│   └── videos/
└── scripts/
		├── optimize_media.py
		├── summarize_sizes.py
		├── check_sizes.py
		├── ffmpeg_check.py
		├── check_moviepy.py
		├── list_moviepy.py
		├── inspect_clip.py
		└── inspect_logo.py
```

## Run Locally

You can open `index.html` directly, but using a local server is recommended.

```bash
python -m http.server 8000
```

Then open:

`http://localhost:8000`

## Media Workflow

The gallery reads from `media_manifest.json`, so keeping this file current is essential.

### Source Folder

Place raw media in:

- `UDADA/` (images and videos)

### Build Optimized Media + Manifest

```bash
python scripts/optimize_media.py
```

This script:

- Converts images (`.jpg`, `.jpeg`, `.png`, `.heic`) to optimized JPEG
- Resizes images to max dimension 1920px
- Compresses videos (`.mp4`, `.mov`) to H.264 MP4 (max width 960px)
- Removes video audio tracks
- Writes updated `media_manifest.json`

### Utility Scripts

- `scripts/summarize_sizes.py`: compare original vs optimized media sizes
- `scripts/check_sizes.py`: list largest generated assets
- `scripts/ffmpeg_check.py`: confirm bundled FFmpeg path/version
- `scripts/check_moviepy.py`: verify MoviePy installation
- `scripts/list_moviepy.py`: inspect available MoviePy modules
- `scripts/inspect_clip.py`: inspect resize-related MoviePy methods
- `scripts/inspect_logo.py`: inspect logo color palette

## Dependencies For Media Processing

If you plan to run the Python media scripts, install:

```bash
pip install pillow pillow-heif imageio-ffmpeg moviepy
```

## Deployment

This repository is designed for GitHub Pages deployment.

Typical workflow:

1. Update content/media
2. Regenerate media and manifest if needed
3. Commit and push to `main`
4. Let GitHub Pages publish the latest commit

## Notes

- If deleted media still appears on the live site, first confirm it is removed from both:
	- `assets/images` or `assets/videos`
	- `media_manifest.json`
- After deploy, do a hard refresh to clear browser cache.

## License

No license file is currently included.
