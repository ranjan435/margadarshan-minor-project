from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

# Create your models here.
class Petition(gis_models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()
	address_to=models.CharField(default='Pulchowk campus',max_length=20)
	img=models.FileField(default='gallery/construction.jpeg',upload_to='gallery/',null=True,blank=True)
	city=models.CharField(max_length=20,default='kathmandu')
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	location=LocationField(based_fields=['pulchowk campus'],zoom=7,default=Point(85.3178166,27.6828417))

	class Meta:
		ordering=['-date_posted']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('petition-home')

	def total_upvotes(self):
		return self.upvotes.count()


