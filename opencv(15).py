#Changing resolution of cam
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
#resolution HD(1280 x 720)

def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()        
           


