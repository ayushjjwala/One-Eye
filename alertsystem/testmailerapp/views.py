from django.shortcuts import render
import ipdb
from django.http import HttpResponse
from django.core.mail import send_mail
import traceback
import sys
import urllib2
from django.conf import settings

# Create your views here.

def send_test_mail(request):

	try:
		send_mail('testing mailer', 'This is a test mail', 'OneEye@imaginate.in',
			['abhimanyu@imaginate.in','hemanth@imaginate.in'], fail_silently=False)

		return HttpResponse("Sent mail successfully")
	except Exception, err:
		
		print traceback.format_exc()
		return HttpResponse("Exception")


def send_test_sms(request):
    try:
        r = urllib2.urlopen(settings.SMS_SEND_STRING).read()
        return HttpResponse("Success " + r)
    except Exception, err:
        return HttpResponse("Exception")
