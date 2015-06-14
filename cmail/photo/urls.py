from django.conf.urls import patterns, url
from photo import views

urlpatterns = patterns('',
	url(r'^upload/', views.upload_test, name='test upload'),
)
