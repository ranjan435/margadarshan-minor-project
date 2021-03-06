# Generated by Django 3.0.2 on 2020-01-31 04:02

from django.conf import settings
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.spatial


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address_to', models.CharField(default='Pulchowk campus', max_length=20)),
                ('img', models.FileField(blank=True, default='gallery/construction.jpeg', null=True, upload_to='gallery/')),
                ('city', models.CharField(default='kathmandu', max_length=20)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(85.3178166, 27.6828417), srid=4326)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
