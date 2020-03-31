from PIL import Image
import sys

try:
    img = Image.open('image.jpg')
except:
    print("probelm")
    sys.exit(1)

## convert the image to png
img.save('s.png','png')
