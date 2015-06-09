from django.conf.urls import patterns, include, url
from django.contrib import admin
from cmail import views

urlpatterns = (
	url(r'^admin/', include(admin.site.urls)),
	url(r'^technology/', views.technology),
	url(r'^devteam/', views.dev_team),
	url(r'^$', views.homev),
	url(r'^home/',views.homev),
    	url(r'^login/',views.loginv),
    	url(r'^logout/', views.logoutv),
	url(r'^register/',views.registerv),
	url(r'^account/',views.accountv),
    	url(r'^template/',views.templatev),
    	url(r'^box/',views.boxv),
    	url(r'', include('photo.urls')),
    	url(r'', include('notification.urls')),
	url(r'^mynotification/', include('notification.urls')),
)
