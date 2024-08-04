#How to change perspective of an image
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("sudoku.png")
plt.imshow(img)
plt.show()

#defining points
point1 = np.float32([[71, 85], [33, 515], [490, 69], [518, 521]])#[topleft, bottomleft, topright, bottomright]
width = 558
height = 563

point2 = np.float32([[0, 0],[0, height],[width ,0], [width, height]])#[topleft,topright, bottomleft,  bottomright]

matrix = cv2.getPerspectiveTransform(point1, point2)
out_image = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow('new', out_image)
cv2.waitKey(0)
cv2.destroyAllWindows()