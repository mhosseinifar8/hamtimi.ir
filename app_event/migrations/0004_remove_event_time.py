# Generated by Django 2.2.1 on 2019-06-27 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0003_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
    ]