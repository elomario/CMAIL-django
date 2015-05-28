from django.contrib import admin
from box.models import Box

#class InlineMember(admin.TabularInLine):
	#model = Member

class BoxAdmin(admin.ModelAdmin):
	list_display=('address','sim')
	filter_vertical=('member',)
	
# Register your models here.
admin.site.register(Box, BoxAdmin)


# Register your models here.
