#Simple Image Thresholding
#in the Left hand side of the graidient.png the pixel values are closer to '0' and in hte R.H.S the pixel values are closer to 255
#result of threshoding gives two results,one is ret value and other is the thresholded value of the image
import cv2
import numpy as np

img = cv2.imread("gradient.png", 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#127: This is the threshold value. Any pixel value in the image greater than this threshold will be set to the maximum value (255), and any pixel value less than or equal to this threshold will be set to the minimum value (0).
#255: This is the maximum value to use with the cv2.THRESH_BINARY thresholding type. In this case, it means that pixel values above the threshold (127) will be set to 255.
_,th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
#this does the inverse of the THRESH_BINARY
_,th3 = cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)
#In THRESH_TRUNC the value of the pixels will remain same after threshold until the 255
_,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
#In Thresh_TOZERO the value is assigned to 0 lesser than the threshold value
_,th5 = cv2.threshold(img , 127, 255, cv2.THRESH_TOZERO_INV)
#Opposite of THRESHOLD_TOZERO

cv2.imshow("image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", th4)
cv2.imshow("th5", th5)
cv2.waitKey(0)
cv2.destroyAllWindows()
