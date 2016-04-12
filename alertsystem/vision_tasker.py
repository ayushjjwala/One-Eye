from alertshandler.helpers import send_alert
from PIL import Image
#import ipdb
import numpy as np
import cv2
import urllib
from random import sample
from string import letters, digits
from face_recog_latest import predict
from pytz import timezone
from datetime import datetime
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#image_url='http://172.16.49.115:8080/shot.jpg'
image_url='http://192.168.43.1:8080/shot.jpg'
#ip = 'http://192.168.43.17:8000'
ip = "http://localhost:8000"
sms = False

while True:

    req = urllib.urlopen(image_url)
    print 'Image fetched from Cam ' + datetime.now(timezone('Asia/Kolkata')).strftime("%Y-%m-%d---%H:%M:%S")
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr,-1) # 'load it as it is'

    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = detector.detectMultiScale(gray, 1.3, 5)
    #detected = detector.detectMultiScale(gray,1.1,3,cv2.cv.CV_HAAR_DO_CANNY_PRUNING,(10,10)).tolist()
    #frame_save_to_name="/Users/Hemanth/Documents/Code/FaceRec/OneEye/imaginate_oneeye/alertsystem/media" + '/captures/' + datetime.now(timezone('Asia/Kolkata')).strftime("%Y-%m-%d---%H:%M:%S.jpg")
    #cv2.imwrite(frame_save_to_name,img)
    found = None
    found = predict(img)
    print 'Image recognition done ' + datetime.now(timezone('Asia/Kolkata')).strftime("%Y-%m-%d---%H:%M:%S")
    if (found != None ):
        random =''.join(sample(letters + digits, 10)) + '.jpg'
        save_to_name =  "/Users/Hemanth/Documents/Code/FaceRec/OneEye/imaginate_oneeye/alertsystem/media" + '/frames/' + random
        cv2.imwrite(save_to_name,img)
        print found
        if (found[0] == 0) and (found[1] < 1300.0):
            send_alert(random, "abhimanyu.jpg", ip, sms)
        elif (found[0] == 1) and (found[1] < 1300.0):
            send_alert(random,"hemanth.jpg", ip, sms)
        elif (found[0] == 2) and (found[1] < 1300.0):
            send_alert(random, "subbu.jpg", ip, sms)
        elif (found[0] == 3) and (found[1] < 1300.0):
            send_alert(random,"vamsi.jpg", ip, sms)

