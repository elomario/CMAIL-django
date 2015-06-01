from django.contrib import admin
from photo.models import Photo

#class InlinePhoto(GenericTabularInline):
#	model = Photo

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('publication_date','id','phototype','notification','image')
	#inlines=[InlinePhoto]
	
admin.site.register(Photo,PhotoAdmin)