from django.shortcuts import render
from notification.models import Notification
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Template, Context, RequestContext

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

