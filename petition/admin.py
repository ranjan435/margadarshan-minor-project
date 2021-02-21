from django.contrib import admin
from .models import Petition
from django.contrib.gis import admin

# Register your models here.
admin.site.register(Petition)
# admin.site.register(LocationPost,admin.OSMGeoAdmin)