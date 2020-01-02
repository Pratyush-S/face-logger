import matplotlib.pyplot as plt
from PIL import Image 
from PIL import ImageOps
  
filename = "raw_image_1.JPG"

filename = "raw_2.jpeg"

with Image.open(filename) as image: 
    width, height = image.size 
    
    
    
    
    
img = Image.open(filename).convert('L')
    
c=np.array(img)


a = Image.fromarray(c)


i=0

border=(50,100,50,200)
x=ImageOps.crop(img,border)

x.size


print(x)

d=c.tolist()

e=np.array(d)
arr2im



#################################################################

gray = cv2.imread('filename', 0)
plt.figure(x)

plt.imshow(c[:][:][:], cmap='gray')

plt.show()



