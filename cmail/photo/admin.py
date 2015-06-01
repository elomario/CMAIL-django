from django.contrib import admin
from photo.models import Photo

#class InlinePhoto(GenericTabularInline):
#	model = Photo

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('publication_date','id','image_tag','phototype','notification','image',)
	#inlines=[InlinePhoto]
	
admin.site.register(Photo,PhotoAdmin)