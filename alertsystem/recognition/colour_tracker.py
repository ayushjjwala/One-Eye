#! /usr/bin/env python 

import cv2
import numpy as np
import cv2.cv as cv

color_tracker_window = "Color Tracker"

class ColorTracker:
    
    def __init__(self):
        cv2.namedWindow( color_tracker_window, cv2.WINDOW_NORMAL)
        self.capture = cv2.VideoCapture(0)
        
    def run(self):
        while True:
            ret, img = self.capture.read()
            
            #blur the source image to reduce color noise 
            cv2.blur(img, (3,3));

            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # yellow is 10-30, blue is 110-130, green is 50-70, red is 160-179
            thresholded_img = cv2.inRange(hsv_img, (110, 80, 80), (130, 255, 255))

            moments = cv2.moments(thresholded_img)
            area = moments['m00']

            print area
            #there can be noise in the video so ignore objects with small areas 
            if(area > 100000):
                #determine the x and y coordinates of the center of the object 
                #we are tracking by dividing the 1, 0 and 0, 1 moments by the area 
                x = int(moments['m10']/area)
                y = int(moments['m01']/area)

                cv2.circle(img, (x, y), 2, (255, 255, 255),10)

            #display the image  
            cv2.imshow(color_tracker_window, img)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

if __name__=="__main__":
    #cap = cv2.VideoCapture(0)
    color_tracker = ColorTracker()
    color_tracker.run()

