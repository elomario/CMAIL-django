from django.conf.urls import patterns, url
from notification import views

urlpatterns = patterns('',
        url(r'^notification/', views.send_notificationv),
)

