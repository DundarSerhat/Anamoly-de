# Its our first CNN 
import cv2
import numpy as np
import functions as fcn
import Datasets as DS


# 



def SaveMouseImages():
    i = 0
    for file in DS.BlueDatasets[1]["RawFiles"]:
        path = file
        img = cv2.imread(path)
        originalImage = img.copy()
        masked = fcn.BlueMouseColorRange(img) 
        ##cv2.imshow('mask', masked)
        contours, hierarchy = cv2.findContours(
            masked, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            
            area = cv2.contourArea(contour)
        
            if (area > 7500):
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))

                radius = int(radius)
                circle = cv2.circle(img, center, radius, (0, 255, 0), 2)
                
                if(int(x-radius) > 0 ):  
                    x_start = int(x-radius) 
                else:  
                    x_start = 0
                    
                if(int(x+radius) > 0 ): 
                    x_end =  int(x+radius) 
                else: 
                    x_end = 0 
                    
                if(int(y-radius) > 0 ): 
                    y_start = int(y-radius) 
                else:
                    y_start = 0 
                    
                if(int(y+radius) > 0 ):
                    y_end =  int(y+radius)
                else:
                    y_end = 0 
                
                cropped_image = originalImage[y_start:y_end, x_start:x_end]
                resizedImage = fcn.reSizeImage(cropped_image)
                
                #fcn.AddText(img, str(area), x, y)
                #cv2.imshow('resized', resizedImage)
                fileName = DS.BlueDatasets[1]["DatasetPath"] + DS.BlueDatasets[1]["Label"] + '_' + str(i) + '.jpg'
                cv2.imwrite(fileName, resizedImage)
                i = i + 1

                
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # break
    
SaveMouseImages()