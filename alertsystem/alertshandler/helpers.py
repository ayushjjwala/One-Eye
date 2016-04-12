import urllib, cStringIO
from PIL import Image
from string import letters, digits
from random import sample
from django.conf import settings
from django.shortcuts import render
import ipdb
from django.http import HttpResponse
from django.core.mail import send_mail
import traceback
import sys
import urllib2
import time
from pytz import timezone
from datetime import datetime

def get_image_from_url(image_url):
    file = cStringIO.StringIO(urllib.urlopen(image_url).read())
    img = Image.open(file)
    return img
def get_random_name():
    temp=''.join(sample(letters + digits, 10)) + '.jpg'
    return temp

def send_alert(file_name,fnMugShot,ip,sendalert=False):
    #img=Image.open(settings.MEDIA_ROOT+"/" +settings.MEDIA_URL+'/mugshots/1.jpg')

    #alert_url="http://localhost:8000/alerts/" + file_name + "__" + fnMugShot + "__" + "1__" + datetime.now(timezone('Asia/Kolkata')).strftime("%Y-%m-%d---%H:%M:%S")
    alert_url=ip + "/alerts/" + file_name + "__" + fnMugShot + "__" + "1__" + datetime.now(timezone('Asia/Kolkata')).strftime("%Y-%m-%d---%H:%M:%S")
    print alert_url
    if sendalert:
        send_alert_mail(alert_url)
        send_alert_sms(alert_url)

def send_alert_mail(alert_url):
    send_mail('Alert detected ', 'Click this url to view the alert '+ alert_url, 'OneEye@imaginate.in',
                        ['abhimanyu@imaginate.in','hemanth@imaginate.in'], fail_silently=False)
def send_alert_sms(alert_url):
    urllib2.urlopen(settings.SMS_SEND_STRING.format(alert_url)).read()

def test_send_alert():

    url='http://172.16.49.115:8080/shot.jpg'
    img=get_image_from_url(url)
    mug='1.jpg'
    print 'testing send alert'
    print 'Cam URl ' +  url
    print 'using mugshots/'+mug

    send_alert(img,mug)
