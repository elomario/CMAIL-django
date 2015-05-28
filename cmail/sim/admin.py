from django.contrib import admin
from sim.models import Sim

class SimAdmin(admin.ModelAdmin):
		list_display=('description', 'id')
# Register your models here.

admin.site.register(Sim, SimAdmin)