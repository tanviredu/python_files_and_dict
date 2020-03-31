from PIL import Image
import pytesseract
#import cv2
import os
import sys



class ImageTranslation():

    def __init__(self,name):
        self.name = name 

    def load_image(self):
        self.im = Image.open(self.name)
        # gray convert
        self.final = self.im.convert('L')
        return self.final 

    def translate(self):
        self.text = pytesseract.image_to_string(self.final)
        return self.text

i = ImageTranslation(str(sys.argv[1]))
i.load_image()
print(i.translate())
