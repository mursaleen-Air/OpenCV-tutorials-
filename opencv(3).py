import cv2
import datetime
#Showing date and time
cap = cv2.VideoCapture(0)


#print(cap.get (cv2.get(CAP_PROP_FRAME_WIDTH)))



#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
#they have associated numbers e.g cv2.CAP_PROP_FRAME_WIDTH is equal to 3 (cap,set(3, 1208))

#print(cap.get(3))
#print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width :'+ str(cap.get(3))+ 'Height :'+ str(cap.get(4))
        datet = str(datetime.datetime.now())
        #shows current date time
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1)  & 0xFF == ord ('q'):
            break
    else:
        print('nonononononononn')
        break

cap.release()
cv2.destroyAllWindows()    
