# Generated by Django 3.0.2 on 2020-01-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_auto_20200130_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensormodel',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
