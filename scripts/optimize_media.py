import json
import subprocess
from pathlib import Path

from PIL import Image
import pillow_heif
import imageio_ffmpeg

# Register HEIC opener with Pillow
pillow_heif.register_heif_opener()

# Configure paths
ROOT = Path(__file__).resolve().parent.parent
UDADA = ROOT / "UDADA"
OUT_IMAGES = ROOT / "assets" / "images"
OUT_VIDEOS = ROOT / "assets" / "videos"

OUT_IMAGES.mkdir(parents=True, exist_ok=True)
OUT_VIDEOS.mkdir(parents=True, exist_ok=True)

# Image processing config
MAX_DIM = 1920
JPG_QUALITY = 78

# Video processing config
MAX_VIDEO_WIDTH = 960
TARGET_BITRATE = "1000k"

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

manifest = {"images": [], "videos": []}

print("Scanning UDADA folder for media...")

for src in sorted(UDADA.iterdir()):
    if not src.is_file():
        continue

    ext = src.suffix.lower()

    # --- Images ---
    if ext in {".jpg", ".jpeg", ".png", ".heic"}:
        out_name = src.stem + ".jpg"
        out_path = OUT_IMAGES / out_name

        try:
            img = Image.open(src)
            img = img.convert("RGB")
            w, h = img.size
            scale = min(1.0, MAX_DIM / max(w, h))
            if scale < 1.0:
                img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

            img.save(out_path, format="JPEG", quality=JPG_QUALITY, optimize=True, progressive=True)
            print(f"Optimized image: {src.name} → {out_path.relative_to(ROOT)}")
            manifest["images"].append((Path("assets") / "images" / out_name).as_posix())
        except Exception as e:
            print(f"Failed optimizing image {src.name}: {e}")

    # --- Videos ---
    if ext in {".mp4", ".mov"}:
        out_name = src.stem + ".mp4"
        out_path = OUT_VIDEOS / out_name
        if out_path.exists() and out_path.stat().st_mtime >= src.stat().st_mtime:
            manifest["videos"].append((Path("assets") / "videos" / out_name).as_posix())
            continue

        cmd = [
            FFMPEG,
            "-y",
            "-i",
            str(src),
            "-vf",
            f"scale='min({MAX_VIDEO_WIDTH},iw):min({MAX_VIDEO_WIDTH},ih):force_original_aspect_ratio=decrease'",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-b:v",
            TARGET_BITRATE,
            "-movflags",
            "+faststart",
            "-an",
            str(out_path),
        ]

        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(f"Compressed video: {src.name} → {out_path.relative_to(ROOT)}")
            manifest["videos"].append((Path("assets") / "videos" / out_name).as_posix())
        except subprocess.CalledProcessError as e:
            print(f"Failed compressing video {src.name}: {e}; stderr: {e.stderr}")

# Save manifest
with open(ROOT / "media_manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2)

print("Done. Manifest written to media_manifest.json")
