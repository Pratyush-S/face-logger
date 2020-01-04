import matplotlib.pyplot as plt
from PIL import Image 
from PIL import ImageOps
import numpy as np  
import PIL
filename = "raw_image_1.JPG"

filename = "raw_3.jpeg"

with Image.open(filename) as image: 
    width, height = image.size 
    
    
    
    
img = Image.open(filename).convert('L')

#RESIZE
basewidth = 300
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    

#image to numpy array
c=np.array(img)

d=np.array(img)
img.size

d=c*0

a = Image.fromarray(d)

a1 = Image.fromarray(c)



i=0

border=(0,0,0,100)
x=ImageOps.crop(img,border)
c=np.array(x)
x.size
d=x*0


print(x)

d=c.tolist()

e=np.array(d)
arr2im

for k in range(3):
    for i in range( len(c)):
        for j in range(len(c)):
            d[i][j][k]=255-c[i][j][k]

#####
############################################################

gray = cv2.imread('filename', 0)
plt.figure(x)

plt.imshow(c[:][:][:], cmap='gray')

plt.show()



