# Generated by Django 3.0.2 on 2020-01-20 17:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.FileField(blank=True, null=True, upload_to='gallery/')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]
