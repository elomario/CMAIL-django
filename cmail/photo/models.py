from django.db import models
# Create your models here.

class Photo(models.Model):
	TYPE_CHOICES=(
			('colis', 'colis'),
			('enveloppe', 'enveloppe'),
			('pub', 'pub'),
			('bordereau', 'bordereau'),
	)
	#type de photos 4 colis blabla
	phototype = models.CharField(max_length = 9,choices = TYPE_CHOICES, blank = True)
	publication_date = models.DateTimeField('published on:', auto_now_add = True)

class Image(models.Model):
	photo = models.ForeignKey(Photo)
	image = models.ImageField(upload_to = 'static')