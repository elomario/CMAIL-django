from django.contrib import admin
from photo.models import Photo


class PhotoAdmin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)
	list_display = ('publication_date','image_tag','id','phototype','notification','image',)
	
	
admin.site.register(Photo,PhotoAdmin)