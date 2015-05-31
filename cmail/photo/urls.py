from django.conf.urls import patterns, url
from photo import views

urlpatterns = patterns('',
	url(r'^upload/', views.upload_photo, name='photo upload'),
)