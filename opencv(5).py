import numpy as np
import cv2
#More Mouse click event

#dir shows everything in our cv2 package but we are only seeing the event or properties which has the keyword 'EVENT" in them
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print (events)

#img = cv2.imread("lean.jpg")
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5 ) 

            #points[-1] is the last element of the array and points[-2] is the 2nd last


        cv2.imshow('image', img)
img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("image", img)
#the image name should be the same
cv2.setMouseCallback('image', click_event)
points = []
cv2.waitKey(0)
cv2.destroyAllWindows()