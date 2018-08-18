import cv2
# object detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# screen capture
video_capture = cv2.VideoCapture(0)

while True:
    if not video_capture.isOpened:
        print("error loading camera")
        pass
    # read each frame
    ret,frame = video_capture.read()
    # convert it to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    # drawing a circle around faces on screen capture
    for(x,y,w,h) in faces:
        cv2.circle(frame,(x+int(w/2),y+int(h/2)),int(w/2),(0, 255, 0),2)
    # show video
    cv2.imshow('Video', frame)
    # detect if user has pressed q (quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release capture
video_capture.release()
cv2.destroyAllWindows()