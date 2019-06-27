import numpy as np
import cv2

video = cv2.VideoCapture(1)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = video.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

video.release()
cv2.destroyAllWindows()
