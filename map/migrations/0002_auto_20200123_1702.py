# Generated by Django 3.0.2 on 2020-01-23 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationmodel',
            name='destination',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='destinationmodel',
            name='source',
            field=models.CharField(max_length=40),
        ),
    ]
