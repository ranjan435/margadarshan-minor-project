# Generated by Django 3.0.2 on 2020-01-29 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_sensormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensormodel',
            name='dust',
            field=models.FloatField(max_length=20),
        ),
    ]
