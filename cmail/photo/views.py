from django.shortcuts import render
from photo.models import Photo
from box.models import Box
from sim.models import Sim
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
#commandes de tests
#curl -F "sim_id=12"  -F "image=Hearthstone_Screenshot_05-26-25_22.50.03.png" localhost:8000/upload/ > test.html

def upload_photo(request):
	if request.method == 'POST':
		sim_id= request.POST['sim_id']
		#test if Sim with number=sim_id  exists
		if Sim.objects.filter(number = sim_id).count()==1:
<<<<<<< HEAD
		#	#with the raw http post being: blabla
			uploaded_photo = Photo(phototype= 'Blank', image = request.POST['image'])
=======
			#with the raw http post being: blabla
			
			uploaded_photo = Photo(image = request.POST['image'])
>>>>>>> f3af9e9f03d2651f4e09f00c1c431490d54c8cf5
			if uploaded_photo.is_valid():
				uploaded_photo.save()
				return HttpResponse("Image Uploaded")
			else:
				return HttpResponse("Image Not Uploaded: Check type or File Integrity")
		else:
			return HttpResponse("ACCESS DENIED: Box Not Identified")
	else:
		return HttpResponse("GET Denied")
