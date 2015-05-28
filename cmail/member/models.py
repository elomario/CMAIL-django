from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
	member = models.OneToOneField(User)
	def __str__(self):  
		return self.user.username