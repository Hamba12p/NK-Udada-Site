import os
import glob

files = glob.glob('assets/**/*', recursive=True)
files = [f for f in files if os.path.isfile(f)]
files_sorted = sorted(files, key=lambda f: os.path.getsize(f), reverse=True)
for f in files_sorted[:20]:
    size = os.path.getsize(f)
    print(f"{f}: {size/1024/1024:.1f} MB")
