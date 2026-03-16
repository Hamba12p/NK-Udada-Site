import moviepy
import pkgutil

print('moviepy version', moviepy.__version__)
print('submodules:')
for m in pkgutil.iter_modules(moviepy.__path__):
    if m.name.startswith('video') or m.name.startswith('editor') or m.name.startswith('audio'):
        print(' ', m.name)
