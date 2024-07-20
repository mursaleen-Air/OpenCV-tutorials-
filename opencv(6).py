import cv2
import numpy as np
#split merge size add
#ROI is region of interest
img = cv2.imread("messi5.jpg")
img2 = cv2.imread('opencv-logo.png')

print(img.shape)#Print as in a tuple(rows , columns, channels)
print(img.size)#prints the no of pixels
print(img.dtype)#print the datatype of the image
b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))
ball = img[280:340, 330:390]#img[(y1:y2) , (x1:x2)]
img[273:333, 100:160] = ball
'''''
def mouse_event(event, x, y,flags, param ):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        XY = str(x ) + ', ' + str(y)
        cv2.putText(img, XY,(x, y), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('image', img)




cv2.setMouseCallback('image', mouse_event)

'''''
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#dst = cv2.add(img, img2)

dst = cv2.addWeighted(img, 0.5, img2, 0.5, 0)#(src1, weight of 1st pic, src2, weight of 2nd pic, scalar value)
cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()