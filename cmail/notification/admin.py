from django.contrib import admin
from notification.models import Notification

class NotificationAdmin(admin.ModelAdmin):
	list_display=('title','description', 'box','checked','sent')

# Register your models here.
admin.site.register(Notification, NotificationAdmin)


# Register your models here.
