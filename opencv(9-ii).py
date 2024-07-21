#Object detection and Tracking using HSV(Hue,Saturation and Value) color space
#Hue(the color),Saturation(distance from the center of HSC cone) value (brightness)
#watch videos on hsv for better undrstanfing
import cv2
import numpy as np
def nothing(x):#dummy function
    pass


cap = cv2.VideoCapture(0)
   
cv2.namedWindow("Tracking")  #tracking window will be used when we use trackbar to the image to define the  lower and upper color values to hsv color space
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0 ,255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)


while True:
    #frame = cv2.imread("smarties.png")
    #cv2.imshow("frame", frame)
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")




    l_b = np.array([l_h, l_s, l_v])   #np.array([hue, saturation, value])
    u_b = np.array([u_h, u_s, u_v])
 

    mask = cv2.inRange(hsv, l_b, u_b )

    res = cv2.bitwise_and(frame, frame, mask = mask )# if mask value is White then original picture is retained, if mask value is black then original picture is set to 0(black)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()


