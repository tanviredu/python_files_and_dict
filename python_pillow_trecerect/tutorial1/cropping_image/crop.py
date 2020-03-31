### crooping and rotate image
### written in oop style

from PIL import Image
import sys

class ImageManupulation():

    def __init__(self,image):

        self.image = image

    def crop(self):
        self.img = Image.open(self.image)
        self.crop = self.img.crop((100,100,300,300))
        self.crop.save('cropimage.jpg')

    def rotate(self):
        self.img = Image.open(self.image)
        self.rotate = self.img.rotate(180)
        self.rotate.save('rotatedimage.jpg')


i = ImageManupulation('../image.jpg')
i.crop()
i.rotate()


