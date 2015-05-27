from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
	user = models.OneToOneField(User)
	box = models.ManyToManyField('box.Box', null = True, blank = True)
	def __str__(self):  
       	return self.user.username