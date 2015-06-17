from django.shortcuts import render
from photo.models import Photo
from box.models import Box
from sim.models import Sim
from django.http import HttpResponse, HttpResponseRedirect
from notification.models import Notification
from django.core.management import call_command

import subprocess

# Create your views here.
#commandes de tests
#curl --form "sim_id=12" --form "file_upload=@pathtoimage" c-mail.no-ip.org/upload

def upload_photo(request):
	if request.method == 'POST':
		sim_file= request.FILES['sim_id']
		f=sim_file.read()
		sim_id=int(f)
		#test if Sim with number=sim_id  exists
		if Sim.objects.filter(number = sim_id).count()==1:
			#Creating Photo object
			uploaded_photo = Photo(phototype= 'Blank', image = request.FILES['file_upload'])
			#Creating Notification object and save to DBB
			mySim=Sim.objects.get(number = sim_id)
			myBox=Box.objects.get(sim = mySim)
			if Notification.objects.filter(title__contains = uploaded_photo.image).count() > 1:
				i=0
				for notification in Notification.objects.filter(title__contains = uploaded_photo.image):
					i+=1			
				titleu=str(uploaded_photo.image) + str(i)
				myNotification = Notification(title = titleu, box=myBox)
			else:
				myNotification = Notification(title = uploaded_photo.image, box=myBox)
			#Traitement d'image
			myNotification.save()
			#Polishing Photo object and save to DBB
			uploaded_photo.notification=myNotification
			uploaded_photo.save()
			return HttpResponse("Image Uploaded owner of " + str(sim_id))
		else:
			return HttpResponse("ACCESS DENIED: Box Not Identified")
	else:
		return HttpResponse("GET Denied")

def upload_sim(request):
	if request.method == 'POST':
		#sim_id= request.POST['sim_id']
		sim_file= request.FILES['sim_id']
		#sim_file= request.FILES['text.txt']
		print(sim_file)
		f=sim_file.read()
		intsim_id=int(f)
		print(intsim_id)
		# +retrieve image name sent so intsim_id == first 2 bytes of data
		if Sim.objects.filter(number = intsim_id).count()==1:
			#create notif and photo objects with name of image already in static folder
			return HttpResponse("Got your post owner of " + str(intsim_id))
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
		notificationu=Notification.objects.get(title='testti')
		photou=Photo.objects.get(notification=notificationu)
		print(str(photou.image))

		#ls_fd = subprocess.call('static\pi_test_forme.exe ' + str(photou.image))
		ls_fd = subprocess.Popen('static\pi_test_forme.exe ' + str(photou.image),stdout=subprocess.PIPE).communicate()[0]
		#ls_fd = subprocess.call('static\pi_test_forme.exe static\image_2.jpg')
		print('done')
		out = ls_fd
		return HttpResponse("DO A POST " +  str(out))
