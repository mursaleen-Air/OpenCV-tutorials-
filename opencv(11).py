#Adaptive Thresholding
#It calculates the threshold for the the smaller region of images so we get different thresholdig values of different regions for the same image


import cv2
import numpy as np

img = cv2.imread("sudoku.png", 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("image", img)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)


cv2.waitKey(0)
cv2.destroyAllWindows()