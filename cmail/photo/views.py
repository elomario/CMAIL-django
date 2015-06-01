from django.shortcuts import render
from photo.models import Photo
from box.models import Box
from sim.models import Sim
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def upload_photo(request):
	if request.method == 'POST':
		sim_id= request.POST['sim_id']
		#test if Sim with number=sim_id  exists
		if Sim.objects.filter(number = sim_id).count()==1:
			#with the raw http post being: blabla
			uploaded_photo = Photo(phototype= request.POST['phototype'], image = request.POST['image'])
			if uploaded_photo.is_valid():
				uploaded_photo.save()
				return HttpResponse("Image Uploaded")
			else:
				return HttpResponse("Image Not Uploaded: Check type or File Integrity")
		else:
			return HttpResponse("ACCESS DENIED: Box Not Identified")
	else:
		return HttpResponse("GET Denied")
