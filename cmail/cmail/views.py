from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
# Create your views here.


def homev(request):
	v= '43'
	user=request.user
	t=get_template('home.html')
	html = t.render(RequestContext(request, {'vor':v,'username':user}))
	return HttpResponse(html)

def accountv(request):
	v= '46'
	user=request.user
	t=get_template('account.html')
	html = t.render(RequestContext(request, {'vor':v,'username':user}))
	return HttpResponse(html)

def loginv(request):
	v= '44'
	if request.method == 'GET':	
		user=request.user
		t=get_template('loginsave.html')
		html = t.render(Context({'vor':v,'username':user}))
		return HttpResponse(html)
	elif request.method =='POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			# Correct password, and the user is marked "active"
			auth.login(request, user)
			# Redirect to a success page.
			return HttpResponseRedirect("/account/")
		else:
        	# Show an error page
			return HttpResponseRedirect("/home/")
	else:
		return HttpresponseRedirect("/template/")

def logoutv(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/home/")

def registerv(request):
	if request.method == 'POST':
        	form = UserCreationForm(request.POST)
        	if form.is_valid():
            		new_user = form.save()
            		return HttpResponseRedirect("/account/")
	else:
		request.user.is_authenticated=False
		form = UserCreationForm()
		return render(request, 'register.html', {
		'form': form,
    })

def templatev(request):
	v= '47'
	user=request.user
	t=get_template('template.html')
	html = t.render(RequestContext(request, {'vor':v,'username':user}))
	return HttpResponse(html)
