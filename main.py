# Its our first CNN 
import cv2
import numpy as np
import functions as fcn
import Datasets as DS


for file in DS.BlueMouseNormalFiles:
    path = DS.BlueMouseNormal + file
    img = cv2.imread(path)
       
    masked = fcn.BlueMouseColorRange(img) 
   
    contours, hierarchy = cv2.findContours(
        masked, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        M = cv2.moments(contour)
        area = cv2.contourArea(contour)
       
        if (area > 7500):
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
       
            radius = int(radius)
            circle = cv2.circle(img, center, radius, (0, 255, 0), 2)
            fcn.AddText(img, str(area), x, y)
            cv2.imshow('circles', img)
  
       
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # break
    
