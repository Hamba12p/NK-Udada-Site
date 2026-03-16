# NK Udada Foundation Website

This is a simple static site intended to be hosted on GitHub Pages.

## How to use

- The entry point is `index.html`.
- Media assets are stored under `assets/images` and `assets/videos`.
- A manifest file (`media_manifest.json`) is used to drive the gallery on the page.

## Re-generating optimized media

If you add new photos or videos to the `UDADA/` folder, run:

```sh
python scripts/optimize_media.py
```

This will:

- Convert HEIC images to JPEG
- Resize images to a maximum of 1920px
- Compress videos to 960px width (maintaining aspect ratio) and remove audio
- Update `media_manifest.json` used by the gallery

## Publishing to GitHub Pages

1. Create a GitHub repository and push this folder as the repository root.
2. In the repository settings, enable **GitHub Pages** and set the source to the `main` branch (or your default branch) and the `/ (root)` folder.

The site will be available at `https://<your-username>.github.io/<repo-name>/`.
