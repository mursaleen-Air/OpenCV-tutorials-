import cv2
import numpy as np
#lines ,rectangles, And putting text on the vedeo capture
img = cv2.imread('lena.jpg', 1)

#img = np.zeros([512, 512, 3], np.unit8)
#in this we can make images by numpy using zeroes method ([height, width, 3], np.unit8 gives the datatype)


img = cv2.line(img, (0, 0), (255, 255), (0, 255, 0), 1)
#This is going to draw a red line on our image and (img, starting point, ending point, color in BGR form, thickness)
img = cv2.arrowedLine(img, (255, 255), (255, 0), (255, 0, 0), 5 )

img = cv2.rectangle(img, (384, 0), (510, 120), (0, 0, 255 ), 10)
#(img, tpoleft verteces, bottom right verteces, )
img = cv2.circle(img, (447, 63), 63, (0, 255,0), -1 )

# for circle (img, center vertex, radius, color, thivkness)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (0, 500), font, 1, (255,255,255), 1, cv2.LINE_AA )
#putting in text(img, 'Text Here for the line', Starting point, variable in whch font type is stored , size of font, color, thickness, line type)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()