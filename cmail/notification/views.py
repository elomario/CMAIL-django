from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from notification.models import Notification
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from member.models import Member
from box.models import Box

# Create your views here.

def send_notificationv(request):
        v=55
        user=request.user
        if request.method == 'GET':
                for notif in Notification.objects.all():
                        mynotif=notif
        lastnotif=mynotif.title
        t=get_template('notification.html')
        html = t.render(RequestContext(request, {'vor':v,'username':user,'notification':lastnotif}))
        return HttpResponse(html)

def show_notification(request):
	mynotification_list=[]
	useru=request.user
	myusername=User.objects.get(username=useru)
	mymember=Member.objects.get(member=myusername)
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login/")
	else:	
		if request.method == 'GET':
			for boxu in Box.objects.filter(member=mymember):
				for notificationu in Notification.objects.filter(box=boxu):
					mynotification_list.append(notificationu)
			t=get_template('mynotification.html')
			html = t.render(RequestContext(request, {'username':useru,'member':mymember,'mynotification_list':mynotification_list}))
		return HttpResponse(html)