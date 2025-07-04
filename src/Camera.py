import cv2 as cv
import threading
import os
import datetime
#from PIL import Image

def openCamera():
    global frame
    cap = cv.VideoCapture(0)
    # width, height =  500, 500   # Width of camera, #Height of Camera
    # cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
    # cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)
  
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




def takephoto():
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]  # Remove last 3 microsecond digits
    filename = f"./Images/{timestamp}.png"
    cv.imwrite(filename, frame)





