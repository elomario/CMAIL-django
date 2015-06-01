from django.contrib import admin
from photo.models import Photo

class InlineImage(admin.TabularInline):
	model = image

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('publication_date','id','phototype','image')
	inlines=[InlineImage]
	
admin.site.register(Photo,PhotoAdmin)