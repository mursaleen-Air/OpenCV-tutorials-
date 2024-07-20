import cv2
#Seting camera propertions
cap = cv2.VideoCapture(0)


#print(cap.get (cv2.get(CAP_PROP_FRAME_WIDTH)))



cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#they have associated numbers e.g cv2.CAP_PROP_FRAME_WIDTH is equal to 3 (cap,set(3, 1208))

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1)  & 0xFF == ord ('q'):
            break
    else:
        print('nonononononononn')
        break

cap.release()
cv2.destroyAllWindows()    









