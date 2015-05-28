from django.contrib import admin
from member.models import Member

class MemberAdmin(admin.ModelAdmin):
	list_display=('member','id')
	
admin.site.register(Member,MemberAdmin)
# Register your models here.
