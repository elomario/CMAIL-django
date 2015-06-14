from django.shortcuts import render
from photo.models import Photo
from box.models import Box
from sim.models import Sim
from django.http import HttpResponse, HttpResponseRedirect
from notification.models import Notification
from django.core.management import call_command
#from StringIO import StringIO 

import subprocess

# Create your views here.
#commandes de tests
#curl -F "sim_id=12"  -F "image=Hearthstone_Screenshot_05-26-25_22.50.03.png" localhost:8000/upload/ > test.html

def upload_photo(request):
	if request.method == 'POST':
		sim_id= request.POST['sim_id']
		#test if Sim with number=sim_id  exists
		if Sim.objects.filter(number = sim_id).count()==1:
			#Creating Photo object
			uploaded_photo = Photo(phototype= 'Blank', image = request.FILES['file_upload'])
			#Creating Notification object and save to DBB
			mySim=Sim.objects.get(number = sim_id)
			myBox=Box.objects.get(sim = mySim)
			myNotification = Notification(title = 'image uploaded from arduino', box=myBox)
			#Traitement d'image
			myNotification.save()
			#Polishing Photo object and save to DBB
			uploaded_photo.notification=myNotification
			uploaded_photo.save()
			return HttpResponse("Image Uploaded and Notification Sent")
		else:
			return HttpResponse("ACCESS DENIED: Box Not Identified")
	else:
		return HttpResponse("GET Denied")
		
def upload_test(request):
	#sim_id=bytearray()
	if request.method == 'POST':
		sim_id=request.POST['sim_id']
		#byte=bytearray([str.encode('sim_id')])
		byte=str.encode(sim_id)
		print(byte)
		print(bytes(byte))
		#while request.POST['EOF'] != EOF
		#byte[i]=request.POST['bytearray']
		#image = PIL.Image.frombytes('L', (3, 3), data)
		#image.save('image.bmp')
		return HttpResponse("Image Uploaded and Notification Sent")
	else:
	#C:\Users\Elomario\Desktop\PI\Phase2\CMAIL-django\
		notificationu=Notification.objects.get(title='new enveloppe')
		photou=Photo.objects.get(notification=notificationu)
		print(str(photou.image))

		#ls_fd = subprocess.call('static\pi_test_forme.exe ' + str(photou.image))
		ls_fd = subprocess.Popen('static\pi_test_forme.exe ' + str(photou.image),stdout=subprocess.PIPE).communicate()[0]
		#ls_fd = subprocess.call('static\pi_test_forme.exe static\image_2.jpg')
		print('done')
		out = ls_fd
		return HttpResponse("DO A POST " +  str(out))