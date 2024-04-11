import cv2

#read_webcam
webcam = cv2.VideoCapture(0)

#visualize webcam
while True:
    ret,frame = webcam.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): #if pressed q break out of loop
        break

webcam.release()
cv2.destroyAllWindows()