import cv2
# Replace with your actual RTSP URL
rtsp_url = "rtsp://pbzmif:Tashfeen300$@192.168.1.8:540"

# Create a VideoCapture object
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open video stream. Check your URL and camera settings.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Display the frame
    cv2.imshow('EZVIZ Camera Stream', frame)

    # Press 'q' to exit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()

