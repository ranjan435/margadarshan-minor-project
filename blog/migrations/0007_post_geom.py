# Generated by Django 3.0.2 on 2020-01-22 13:09

import django.contrib.gis.geos.point
from django.db import migrations
import location_field.models.spatial


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='geom',
            field=location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(27.6828417, 85.3178166), srid=4326),
        ),
    ]
