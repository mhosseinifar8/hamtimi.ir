# Generated by Django 2.2.1 on 2019-07-03 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0012_confrim_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confrim',
            name='approved',
        ),
    ]
