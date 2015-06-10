from django.db import models
from cmail import settings
from notification.models import Notification
# Create your models here.

class Photo(models.Model):
	TYPE_CHOICES=(
			('colis', 'colis'),
			('enveloppe', 'enveloppe'),
			('pub', 'pub'),
			('bordereau', 'bordereau'),
	)
	#type de photos 4 colis blabla
	image = models.ImageField(upload_to = 'static', blank=True)
	phototype = models.CharField(max_length = 9,choices = TYPE_CHOICES, blank = True)
	publication_date = models.DateTimeField('published on:', auto_now_add = True)
	notification=models.ForeignKey(Notification, null=True)
	
	
	
	
	def image_tag(self):
		return u'<img src="/%s" width="100" height="100" />' % self.image.url
	
	image_tag.allow_tags = True