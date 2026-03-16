import os, glob

def total(path, patterns):
    files=[]
    for pat in patterns:
        files.extend(glob.glob(os.path.join(path, pat)))
    files=[f for f in files if os.path.isfile(f)]
    total_bytes=sum(os.path.getsize(f) for f in files)
    return total_bytes, len(files)

orig_images=total('UDADA',['*.jpg','*.jpeg','*.png','*.heic'])
orig_videos=total('UDADA',['*.mp4','*.mov'])
opt_images=total('assets/images',['*.jpg','*.jpeg','*.png'])
opt_videos=total('assets/videos',['*.mp4'])

def mb(x):
    return x/1024/1024

print(f'Original photos: {orig_images[1]} files, {mb(orig_images[0]):.1f} MB')
print(f'Original videos: {orig_videos[1]} files, {mb(orig_videos[0]):.1f} MB')
print(f'Optimized photos: {opt_images[1]} files, {mb(opt_images[0]):.1f} MB')
print(f'Optimized videos: {opt_videos[1]} files, {mb(opt_videos[0]):.1f} MB')
