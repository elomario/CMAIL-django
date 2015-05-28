from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.


def homev(request):
	loggedin=True
	if(loggedin!=True):
		return loginv(request)
	else:
		return HttpResponse("<html><body>YOU ARE HOME</body></html>")
def loginv(request):
	loggedin=False
	if(loggedin==True):
		return(homev(request))
	return HttpResponse("<html><body>YOU ARE NOT LOGGED IN</body></html>")
def accountv(request):
	loggedin=False
	if(loggedin!=True):
		return(homev(request))
	return HttpResponse("<html><body>YOU ARE ON YOUR ACCOUNT SETTINGS</body></html>")

