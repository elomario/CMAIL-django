from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from box.models import Box
from member.models import Member
from sim.models import Sim 
from notification.models import Notification
from phonenumber_field.modelfields import PhoneNumberField
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
	if request.user.is_authenticated():
		mymember=Member.objects.get(member=user)
		if request.method=='POST':
			name = request.POST.get('name', '')
			surname = request.POST.get('surname', '')
			phonenumber=request.POST.get('phone_number','')
			billing_address = request.POST.get('billing_address', '')
			ancien_pwd=request.POST.get('apassword','')
			passwd= request.POST.get('bpassword','')
			mymember.phone=phonenumber		
			mymember.name=name
			mymember.surname=surname
			if billing_address!='':
				mymember.billingaddress= billing_address
			mymember.save()
			print mymember.phone
			if user.check_password(ancien_pwd):	
				user.set_password(passwd)
				user.save()
			return HttpResponseRedirect("/account/")	
		else:
			t=get_template('account.html')	
			html = t.render(RequestContext(request, {'current_phone_number':mymember.phone,'vor':v,'username':user,'current_name':mymember.name,'current_surname':mymember.surname,'current_billing_address':mymember.billingaddress}))
			return HttpResponse(html)
	else:
		return HttpResponseRedirect("/login/")

def boxv(request):
	v='48'
	user=request.user
	box_list=[]
	notexist=True
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/login/")
	else:	
		myusername=User.objects.get(username=user)
		mymember=Member.objects.get(member=myusername)
		mybox=Box.objects.filter(member=mymember)	
		if request.method =='POST':
			new_simn=request.POST.get('simn','')
			new_adresse=request.POST.get('adres','')
			for box in mybox:
				new_simn=int(new_simn)
				b=int(box.sim.number)
				if(b==new_simn):
					current_sim=box.sim
					current_box=box
					notexist=False
	
			if notexist:
				new_sim=Sim(number=new_simn, description=new_adresse)
				new_sim.save()
				new_box=Box(sim=new_sim,address=new_adresse)
				new_box.save()
				new_box.member.add(mymember)
			else:
				current_sim.description=new_adresse
				current_sim.save()
				current_box.sim=current_sim
				current_box.address=new_adresse
				current_box.save()
			return HttpResponseRedirect("/box/")
		else:
			if not request.user.is_authenticated():
				return HttpResponseRedirect("/login/")
			else:
				for boxu in Box.objects.filter(member=mymember):
    					box_list.append(boxu)
				t=get_template('box.html')
				html = t.render(RequestContext(request, {'vor':v,'username':user,'mybox_list':box_list}))
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

def commandev(request):
	user=request.user
	t=get_template('commande.html')
	html = t.render(RequestContext(request, {'username':user}))
	return HttpResponse(html)
	
def registerv(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_member=Member(member=new_user,name='Blank',surname='Blank',billingaddress='Blank')
			new_member.save()
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

def technology(request):
	user=request.user
	t=get_template('technology.html')
	html = t.render(RequestContext(request, {'username':user}))
	return HttpResponse(html)
	
def dev_team(request):
	user=request.user
	t=get_template('dev_team.html')
	html = t.render(RequestContext(request, {'username':user}))
	return HttpResponse(html)    
