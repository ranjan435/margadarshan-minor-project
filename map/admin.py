from django.contrib import admin
from .models import DestinationModel,SensorModel,VehicleModel


# Register your models here.
admin.site.register(DestinationModel)
admin.site.register(SensorModel)
admin.site.register(VehicleModel)