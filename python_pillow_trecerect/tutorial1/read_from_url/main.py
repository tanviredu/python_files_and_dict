from PIL import Image
import requests
import sys 

url = 'https://i.ytimg.com/vi/vEYsdh6uiS4/maxresdefault.jpg'

try:
    resp = requests.get(url,stream=True).raw 
    try:
        img = Image.open(resp)
    except:
        sys.exit(1)
except:
    print("Something is wrong")

img.save('sid.jpg','jpeg')

