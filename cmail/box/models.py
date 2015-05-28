from django.db import models
from member.models import Member
from sim.models import Sim
# Create your models here.
class Box(models.Model):
	address = models.CharField(max_length = 45, blank = True)
	sim = models.ForeignKey(Sim)
	member = models.ManyToManyField('member.Member', null = True, blank = True)
	def __str__(self):  
			return self.address