from django.shortcuts import render

def display_alert(request,frame=0,mug=0,cam=0,timestamp=0):
    return render(request,'display_alert.html',{'frame': frame ,'mug' : mug,'cam' : cam,'timestamp' : timestamp})
# Create your views here.
