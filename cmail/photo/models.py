from django.db import models
# Create your models here.
class Phototype(models.Model):
	TYPE_CHOICES=(
			(1, 'colis'),
			(2, 'enveloppe'),
			(3, 'pub'),
			(4, 'bordereau'),
	)
	phototype = models.CharField(max_length = 9,choices = TYPE_CHOICES, blank = True)


class Photo(models.Model):
	image = models.ImageField(upload_to='static')
	publication_date = models.DateTimeField('published on:', auto_now_add = True)
	phototype=models.ForeignKey(Phototype)
	
