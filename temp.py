# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

# p a c k a g e i m p o r t s
import numpy as np
import requests # f o r s a v i n g ima ge s f rom t h e i n t e r n e t
import skimage.io as io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from PIL import Image

url="https://media.wired.com/photos/5a55457ef41e4c2cd9ee6cb5/master/w_2400,c_limit/Doggo-TopArt-104685145.jpg" 

r = requests.get(url)
with open('doggo', "wb") as f:
    f.write(r.content)  
    
doggo=io.imread('doggo')

plt.imshow(doggo)
plt.subplot()
plt.show()
#plt.plot(3000,1600)
#---------------------------------
#cmap=plt.get.cmap(doggo)
plt.subplot(2, 2,3)
plt.imshow(doggo, cmap='gray')
plt.title('Perro Gris')

doggo_gris=rgb2gray('doggo')
plt.savefig('Perro Gris')

img = Image.open('doggo.PNG').convert('RGBA')
a = np.array(img)
plt.hist(a)











