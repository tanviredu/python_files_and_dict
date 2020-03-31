from PIL import Image,ImageDraw,ImageFont
import sys


class ImageManupulation():

    def __init__(self,img):
        self.img = img
        try:
            self.img = Image.open(self.img)
        except:
            print("something is wrong")

        self.idraw = ImageDraw.Draw(self.img)
        self.text = "Tanvir Rahman"
        #self.font = ImageFont.truetype("arial.ttf",size=18)
        self.idraw.text((100,100),self.text)
        self.img.save('water.jpg')

i = ImageManupulation('../image.jpg')
print(i)



