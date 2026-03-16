from moviepy.video.io.VideoFileClip import VideoFileClip
from pathlib import Path

# Use a small video file as test (if available). Otherwise just inspect class methods.
print('VideoFileClip class attributes containing "resize":')
for m in dir(VideoFileClip):
    if 'resize' in m.lower():
        print(' ', m)

# Instantiate a clip to inspect instance methods too
try:
    sample = Path(__file__).resolve().parents[1] / 'UDADA' / 'IMG_2064.MOV'
    clip = VideoFileClip(str(sample))
    print('instance methods containing "resize":')
    for m in dir(clip):
        if 'resize' in m.lower():
            print(' ', m)
    clip.close()
except Exception as e:
    print('failed to open sample video:', e)
