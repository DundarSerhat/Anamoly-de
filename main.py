# Its our first CNN 
import cv2
import numpy as np
import functions as fcn
import Datasets as DS
from pathlib import Path
import os

for file in DS.BlueMouseNormalFiles:
    path = DS.BlueMouseNormal + file
    img = cv2.imread(path)
       
    #cv2.imshow('Masked', masked)    
    
    
    org = img
    # org = fcn.AddPadding(org, 10)
    # #cv2.imshow('ORG', org)
    #imgB = cv2.GaussianBlur(img, (5, 5), 0)
    masked = fcn.BlueMouseColorRange(img) 
    # opening = fcn.Thresholds(imgB)

    contours, hierarchy = cv2.findContours(
        masked, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cntrs = cv2.drawContours(org, contours, -1, (0, 255, 0), 2)

   
    img = fcn.AddPadding(img, 10)
    i = 1
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
            
            tolarance = 0
            cirlce_x1 = int(x - radius) - tolarance
            cirlce_y1 = int(y - radius) - tolarance
            cirlce_x2 = int(x + radius) 
            cirlce_y2 = int(y + radius) 
            #print(str(cirlce_x1) + '\t' + str(cirlce_y1) + '\t' + str(cirlce_x2) + '\t' + str(cirlce_y2))
            # coreFolder = 'ABO\\Outputs\\Cores\\' + file.replace('.png', '')
            # if not os.path.exists(coreFolder):
            #     os.makedirs(coreFolder)
           
        i = i + 1
        #cv2.imshow('circles', cntrs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # break
    
