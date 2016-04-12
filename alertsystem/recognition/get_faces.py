
# #--------------import modules----------------------
import numpy as np
import cv2
import cv2.cv as cv
import sys
import time
# #------------------------------------


def detect(img,cascade,neighs):
    rects = cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=neighs, minSize=(50,50), flags=cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1,y1,x2,y2 in rects:
        cv2.rectangle(img,(x1,y1),(x2,y2),color,1)

if __name__ == '__main__':

    cascade_fn =  "d:\Imaginate\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml"
    nested_fn =  "d:\Imaginate\opencv\sources\data\haarcascades\haarcascade_eye.xml"
    nested_fn2 =  "d:\Imaginate\opencv\sources\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml"

    face_cascade = cv2.CascadeClassifier(cascade_fn)
    eye_cascade = cv2.CascadeClassifier(nested_fn)
    
    cap = cv2.VideoCapture(0)

    fname = "d:/Imaginate/hackathon/recognition/faces/"+sys.argv[1]+"/"
    i = 0;
    time.sleep(3)
    while (i<20):
        try:
            ret, img = cap.read();
        except:
            print 'loading error'
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        
        faces = detect(gray, face_cascade,5)

        if len(faces)>0:
            vis = img.copy()
            draw_rects(vis, [faces[0]], (255,0,0))
    
            cv2.imshow('img',vis)
            
            x1,y1,x2,y2 = faces[0]
            img2 = img[y1:y2, x1:x2]
            temp_name = fname + '%s' %(i)+'.jpg'
            cv2.imwrite(temp_name, img2)
            i = i + 1
            time.sleep(1)
        else:
            pass

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

