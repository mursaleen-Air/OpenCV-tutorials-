#Find and Draw Contours
import cv2
import numpy as np

#Cotours is a Python list of all the contours in the image.Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object 
#heirarchy is the optionl output vectr which is containing the info about the image topology
img = cv2.imread("opencv-logo-white.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray, 127, 255, 0, )
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of Contours = " +str(len(contours)))
print(contours[0])#it will give the numpy array for the x and y coordinates

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)#-1 will join all the contours

cv2.imshow("image", img)
cv2.imshow("image GRAY", imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
