import sys

sys.path.append('/home/kali/.local/lib/python3.11/site-packages')

import cv2 as cv

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()