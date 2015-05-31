from django.db import models

# Create your models here.
class Sim(models.Model):
	number = models.CharField(max_length = 45, blank = True)
	description = models.CharField(max_length = 45, blank = True)
	def __str__(self):  
			return self.number