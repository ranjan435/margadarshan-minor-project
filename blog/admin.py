from django.contrib import admin
from .models import Post
from django.contrib.gis import admin

# Register your models here.
admin.site.register(Post)
# admin.site.register(LocationPost,admin.OSMGeoAdmin)