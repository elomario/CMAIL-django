from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from notification.models import Notification
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from member.models import Member
from box.models import Box
from photo.models import Photo

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
	myphoto_list=[]
	myunreadnotification_list=[]
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
					photou=Photo.objects.get(notification=notificationu)
					myphoto_list.append(photou)
					if notificationu.checked==1:
						myunreadnotification_list.append(notificationu)
			t=get_template('mynotification.html')
			mynotification_list=list(reversed(mynotification_list))
			myphoto_list=list(reversed(myphoto_list))
			
			html = t.render(RequestContext(request, {'username':useru,'member':mymember,'mynotification_list':mynotification_list, 'myunreadnotification_list':myunreadnotification_list, 'myphoto_list':myphoto_list}))
			return HttpResponse(html)
		if request.method =='POST':
			mynotification_id=request.POST.get('notif_id','')
			mynotification_id=int(mynotification_id)
			print(mynotification_id)
			notificationu=Notification.objects.get(id=mynotification_id)
			read=request.POST.get('READ','')
			
			unread=request.POST.get('UNREAD','')			
			if read == 'Mark this notification as Read':
				notificationu.checked=0
				notificationu.save()
			if unread == 'Mark this notification as Unread':
				notificationu.checked=1
				notificationu.save()
			
			return HttpResponseRedirect("/mynotification/")