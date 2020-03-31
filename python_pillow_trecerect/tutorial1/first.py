from PIL import Image
import sys

### try to load a n image

try:
    im = Image.open('image.jpg')
except:
    print("cant load image")
    sys.exit(1)

im.show()
