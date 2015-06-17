from django.db import models
from box.models import Box
# Create your models here.

class Notification(models.Model):
	TRUE=0
	FALSE=1
	CHECKED_CHOICES=(
			(TRUE, 'true'),
			(FALSE, 'false'),
	)	
	title=models.CharField(max_length = 45, blank = True)
	description = models.CharField(max_length = 45, blank = True)
	box=models.ForeignKey(Box)
	checked=models.IntegerField(choices = CHECKED_CHOICES, default = '1')
	#sent is 0 not sent is 1
	sent=models.IntegerField(default='1')
	
	
	def __str__(self):  
			return self.title