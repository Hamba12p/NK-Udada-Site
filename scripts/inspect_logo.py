from PIL import Image
import collections

path = r"d:/PROBOOK/NK Udada Site/Logo.jpeg"
im = Image.open(path).convert('RGB')
print('size', im.size)
pal = im.resize((200, 200)).quantize(colors=5, method=2)
colors = pal.getpalette()[:15]
dominant = [tuple(colors[i:i+3]) for i in range(0, 15, 3)]
print('dominant', dominant)
count = collections.Counter(pal.getdata()).most_common(5)
print('counts', count)
print('hex', [f"#{r:02x}{g:02x}{b:02x}" for (r, g, b) in dominant])
