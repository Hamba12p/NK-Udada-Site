import sys
try:
    import moviepy
    print('moviepy', moviepy.__version__)
except Exception as e:
    print('moviepy import failed:', e)
    sys.exit(1)
