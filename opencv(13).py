#Morphological Transformations

#morphological transformations are normally performed on a binary image
#Kernal tells you how to change the value of the given pixel by combining it with different ammounts of neighbouring pixels
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)


_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV )

kernal = np.ones((2,2), np.uint8)#numpy ones method #kernel is 2x2 shape applied on the black dots in the smarties image
dilation = cv2.dilate(mask, kernal, iterations =2)#default iteration is 1 and the more the iterations the more it expands the object body

erosion = cv2.erode(mask, kernal, iterations = 1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
#opening is another another name for erosion followed by dialation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE ,kernal)
#Closing performs dilation first then erosion

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

th =cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)
#Top hat is the difference betwee nthe image and the opening of the image

titles = ['image', "mask", "dilation", "erosion", "Opening", "Closing", "mg", "th"]
images = [img, mask, dilation, erosion ,opening, closing, mg, th]


for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()    





