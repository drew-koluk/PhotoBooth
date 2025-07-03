import cv2 as cv


def openCamera():
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    while True:
        ret, frame = cap.read()
        if not ret:
           break
        cv.imshow('Camera', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv.destroyAllWindows()