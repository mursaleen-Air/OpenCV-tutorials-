#trackBar to opencv
import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8 )
cv2.namedWindow("image")#we crested namedwindows so we can provide window to trackbar
#cv2.imshow("image", img)

def nothing(x):
    print(x)

cv2.createTrackbar("B", "image", 0, 255, nothing)#("B(name)", name of the window, 0"trackbar initial value", 255, "trackbar final value", nothing"callback function when trackbar value changes")
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("R", "image", 0, 255, nothing )

switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
while(1):
    cv2.imshow("image", img)
    if cv2.waitKey(1) &0xFF == 27:
        break


    b = cv2.getTrackbarPos("B", "image")#(B"trackbar namr, "name of window in which trackbar is present")
    g = cv2.getTrackbarPos("G", "image")
    r = cv2.getTrackbarPos("R", "image")
    s = cv2.getTrackbarPos(switch, "image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
    

    #img[:] = [b, g, r]





cv2.destroyAllWindows()


