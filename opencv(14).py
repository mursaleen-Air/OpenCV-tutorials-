#Smoothing or Blurring the image
#Homogenous filter is the simple filter , each outpuut is the of its kernel neightbours
import cv2     
import numpy as np        
from matplotlib import pyplot as plt
img = cv2.imread("opencv-logo.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((7, 7), np.uint8)/49
#we have to divide by multiplication og width and height(5, 5) which is "25"
#And the matirx like(7, 7) should be oddand the more the value, the more the blurr
dst = cv2.filter2D(img , -1, kernel) 

#Gaussian Blurr
Gauss = cv2.GaussianBlur(img, (7,7), 0)

#Edge Detection
Edge = cv2.Canny(img, 48,48)

#Thickness of Edges
dilated = cv2.dilate(Edge, (7,7), iterations = 1)

titles = ['image', '2dConnvolution', "Gaussian-Blurr","Canny-Image", "Edge-Thickness"]
images = [img, dst, Gauss, Edge, dilated]

for i in range (5):
    plt.subplot(2, 3, i +1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()    