
from django.conf.urls import patterns, url

from testmailerapp import views

urlpatterns = patterns('',  url(r'^send_test_mail/$', views.send_test_mail, name='send_test_mail'),
        					url(r'^send_test_sms/$', views.send_test_sms, name='send_test_sms'),
		)

