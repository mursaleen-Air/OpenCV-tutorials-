#trackBar to opencv
import cv2
import numpy as np

#img = np.zeros((300, 512, 3), np.uint8 )


cv2.namedWindow("image")#we crested namedwindows so we can provide window to trackbar
#cv2.imshow("image", img)

def nothing(x):
    print(x)

cv2.createTrackbar("CP", "image", 10, 400, nothing)#("B(name)", name of the window, 0"trackbar initial value", 255, "trackbar final value", nothing"callback function when trackbar value changes")


switch = 'color/gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
while(1):
    img = cv2.imread("lena.jpg")
    #img = cv2.imshow("image", img)
    pos = cv2.getTrackbarPos('CP', 'image')
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255), 10, cv2.LINE_AA )


    if cv2.waitKey(1) &0xFF == 27:
        break


    
    s = cv2.getTrackbarPos(switch, "image")
    
    

    if s == 0:
        pass
    else:
        img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = cv2.imshow("image", img)


    #img[:] = [b, g, r]





cv2.destroyAllWindows()