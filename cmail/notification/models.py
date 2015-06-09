from django.db import models
from box.models import Box
# Create your models here.

class Notification(models.Model):
	title=models.CharField(max_length = 45, blank = True)
	description = models.CharField(max_length = 45, blank = True)
	box=models.ForeignKey(Box)
	
	
	
	def __str__(self):  
			return self.title