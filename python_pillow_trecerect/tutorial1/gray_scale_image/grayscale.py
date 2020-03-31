from PIL import Image
import sys
import time
try:
    img = Image.open(sys.argv[1])
    ## converting it to grayscale
    print("image loaded")
    time.sleep(1)
    print("converted to grayscale")
    time.sleep(1)
    gray = img.convert('L')
    gray.show()

except:
    print("Problem loading image")
    print("Aborting program")
