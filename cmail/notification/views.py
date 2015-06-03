from django.shortcuts import render

# Create your views here.

def send_notification(request):
	if request.method == 'GET':
		for last_photo in Photo.all()
			myPhoto=last_photo
		#integrate matlab exec for image handling
		myPhoto.type="colis"