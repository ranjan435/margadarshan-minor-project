# Generated by Django 3.0.2 on 2020-01-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_reputation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='reputation',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
