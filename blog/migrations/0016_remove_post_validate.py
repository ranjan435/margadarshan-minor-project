# Generated by Django 3.0.2 on 2020-01-27 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='validate',
        ),
    ]
