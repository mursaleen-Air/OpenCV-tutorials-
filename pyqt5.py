import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'v', 'I', 'D')#WVID is a fourcc code
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))#(name, fourcc, fps, size(tuple))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

    
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)

    
    
        Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



        cv2.imshow("frame", Gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
