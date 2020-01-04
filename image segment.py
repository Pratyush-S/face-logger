import matplotlib.pyplot as plt
from PIL import Image 
from PIL import ImageOps
import numpy as np  
import PIL
#filename = "raw_image_1.JPG"

filename1 = "image00.jpg"
filename2 = "image01.jpg"
filename3 = "image02.jpg"
filename4 = "image03.jpg"

with Image.open(filename1) as image: 
    width, height = image.size 
    
    
    
image = Image.open(filename1)
basewidth = 300
wpercent = (basewidth / float(image.size[0]))

hsize = int((float(image.size[1]) * float(wpercent)))

img = image.resize((basewidth, hsize))

img_array=np.array(img)

mean_1=np.mean((img_array))

print(mean_1)



