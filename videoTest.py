# Its our first CNN
import cv2
import numpy as np
import functions as fcn
import Datasets as DS



cap = cv2.VideoCapture(r'Raw Data\Test Videos\WIN_20211028_19_27_47_Pro.mp4')
cap = cv2.VideoCapture(r'Raw Data\Test Videos\WIN_20211028_19_28_09_Pro.mp4')


# Loop until the end of the video
while (cap.isOpened()):
    ret, frame = cap.read()
    img = frame
    masked = fcn.BlueMouseColorRange(img)

    contours, hierarchy = cv2.findContours(masked, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



    for contour in contours:
        # M = cv2.moments(contour)
        area = cv2.contourArea(contour)
        
        if (area > 7500):
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
        
            radius = int(radius)
            circle = cv2.circle(img, center, radius, (0, 255, 0), 2)
            fcn.AddText(img, str(area), x, y)
            cv2.imshow('circles', img)
            
            
     
    # define q as the exit button
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # release the video capture object
    

cap.release()
cv2.destroyAllWindows()

