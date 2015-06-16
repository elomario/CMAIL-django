from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Member(models.Model):
	member = models.OneToOneField(User)
	name = models.CharField(max_length = 20, blank = True)
	surname = models.CharField(max_length = 20, blank = True)
	billingaddress =  models.CharField(max_length = 45, blank = True)
	phone= PhoneNumberField(blank=True)
	def __str__(self):  
		return self.member.username
