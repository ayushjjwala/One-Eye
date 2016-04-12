import os
import sys
import cv2
import cv2.cv as cv
import numpy as np
import pickle
import time

def enlarge(rect,top_frac,bottom_frac):
  x1,y1,x2,y2 = rect
  rect1 = (inbetween(x1,x2,-top_frac), inbetween(y1,y2,-top_frac), inbetween(x1,x2,bottom_frac), inbetween(y1,y2,bottom_frac))
  return array(rect1)

def detect(img,cascade,neighs):
  rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=neighs, minSize=(5,5), flags=cv.CV_HAAR_SCALE_IMAGE)
  if len(rects) == 0:
    return []
  rects[:,2:] += rects[:,:2]
  return rects

def find_contours(im):
  imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
  ret,thresh = cv2.threshold(imgray,127,255,0)
  contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  return contours, hierarchy

if __name__ == "__main__":
 
  cap = cv2.VideoCapture(0)
  while True:
    ret,cv_image = cap.read()
    contours, hierarchy = find_contours(cv_image)
    cv2.drawContours(cv_image, contours, -1, (0,255,0), 3)
    cv2.imshow('Test subject',cv_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    
  cap.release()
  cv2.destroyAllWindows()

  
