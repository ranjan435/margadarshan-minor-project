# Generated by Django 3.0.2 on 2020-01-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20200123_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationmodel',
            name='destination',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='destinationmodel',
            name='source',
            field=models.CharField(max_length=100),
        ),
    ]
