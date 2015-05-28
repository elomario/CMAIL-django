from django.db import models
# Create your models here.
class Photo(models.Model):
	TYPE_CHOICES=(
			('colis', 'colis'),
			('enveloppe', 'enveloppe'),
			('pub', 'pub'),
			('bordereau', 'bordereau'),
	)
	phototype = models.CharField(max_length = 9,choices = TYPE_CHOICES, blank = False)
	image = models.ImageField(upload_to='static')
	publication_date = models.DateTimeField('published on:', auto_now_add = True)
	
