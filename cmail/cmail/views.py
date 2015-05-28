from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.

def home(request):
	return render(request,'home.html')
