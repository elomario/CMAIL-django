from django.contrib import admin
from photo.models import Image, Photo

class InlineImage(admin.TabularInline):
	model = Image

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('publication_date','id','phototype','image')
	inlines=[InlineImage]
	
admin.site.register(Photo,PhotoAdmin)