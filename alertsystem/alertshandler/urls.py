
from django.conf.urls import patterns, url

from alertshandler import views

urlpatterns = patterns('',url(r'^(?P<frame>[0-9A-Za-z.]+)__(?P<mug>[0-9A-Za-z.]+)__(?P<cam>[0-9A-Za-z]+)__(?P<timestamp>[0-9A-Za-z-:]+)', views.display_alert, name='display_alert'),
                    url(r'^(?P<frame>[0-9A-Fa-f]+)/?$', views.display_alert, name='display_alert'),
        )

