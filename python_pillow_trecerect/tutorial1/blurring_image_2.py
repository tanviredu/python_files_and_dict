from PIL import Image,ImageFilter
import sys
import time
def blur_image(image):
    try:
        img = Image.open(image)
    except:
        print("Probelm loading image")
        sys.exit(1)
    print("image loaded blurring it")

    blurred_image = img.filter(ImageFilter.BLUR)
    
    blurred_image.save('blurred.png')

blur_image('image.jpg')
