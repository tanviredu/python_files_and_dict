### this script will fetch importmation
### from the image
from PIL import Image
import sys

def main():

    ###### try to load the image
    try:
        img = Image.open('image.jpg')
    except:
        print("problem loading image")
        sys.exit(1)

    print("image format {}".format(img.format))
    print("image size {}".format(img.size))
    print("image model {}".format(img.mode))


main()

