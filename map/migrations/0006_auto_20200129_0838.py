# Generated by Django 3.0.2 on 2020-01-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20200129_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensormodel',
            name='dust',
            field=models.CharField(max_length=20),
        ),
    ]
