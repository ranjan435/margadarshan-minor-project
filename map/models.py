from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone

# Create your models here.
class DestinationModel(models.Model):
	source= models.CharField(max_length=100)
	destination = models.CharField(max_length=100)

	def __str__(self):
		return self.destination

class SensorModel(models.Model):
	temperature = models.CharField(max_length=20)
	humidity = models.CharField(max_length=20) 
	dust = models.CharField(max_length=20)
	date_posted=models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return str(self.id)

	class Meta:
		ordering=['-date_posted']


class VehicleModel(models.Model):
	vehicle_count=models.CharField(max_length=20,null=True)
	def __str__(self):
		return self.vehicle_count
	# class Meta:
	# 	ordering=['-id']
 	