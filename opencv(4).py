import numpy as np
import cv2
#Mouse click event

#dir shows everything in our cv2 package but we are only seeing the event or properties which has the keyword 'EVENT" in them
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print (events)

img = cv2.imread('lena.jpg')
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0] # its the BGR chanel
        green = img[y, x, 1]
        red = img[y, x, 2] 
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)  

#img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("image", img)
#the image name should be the same
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()