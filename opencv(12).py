#matplotib with opencv
#opencv reads image in bgr format
#matplotlib reads image in rgb format

import cv2
from matplotlib import pyplot as plt


img = cv2.imread("lena.jpg")
cv2.imshow("image", img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
#plt.xticks([]), plt.yticks([])         #this hides the X and Y on image of matplotlib






plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
