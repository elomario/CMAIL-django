from django.conf.urls import patterns, url
from photo import views

urlpatterns = patterns('',
	url(r'^upload/', views.upload_photo, name='photoupload'),
	url(r'^upload2/', views.upload_sim, name='simupload'),
	url(r'^upload3/', views.upload_test, name='testupload'),
)
