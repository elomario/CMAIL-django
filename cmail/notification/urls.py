from django.conf.urls import patterns, url
from notification import views

urlpatterns = patterns('',
        url(r'^mynotification/', views.show_notification),
)