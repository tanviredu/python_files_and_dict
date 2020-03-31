from PIL import Image
import pytesseract
#import cv2
import os
import sys


def im(image):
        im = Image.open(image)
        gray = im.convert('L')
        text = pytesseract.image_to_string(im)
        print(text)



im(str(sys.argv[1]))
