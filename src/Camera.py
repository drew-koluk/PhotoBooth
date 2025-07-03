import cv2 as cv
import threading


def openCamera():
    cap = cv.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        if not ret:
           break
        cv.imshow('Camera', frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
        if cv.getWindowProperty('Camera',cv.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv.destroyAllWindows()
