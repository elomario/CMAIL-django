from django.db import models
from box.models import Box

from photo.models import Photo
# Create your models here.

class Notification(models.Model):
	title=models.CharField(max_length = 45, blank = True)
	description = models.CharField(max_length = 45, blank = True)
	box=models.ForeignKey(Box)
	photo = models.ForeignKey(Photo, null=True)
	def __str__(self):  
			return self.title