# Generated by Django 2.2.1 on 2019-06-27 08:11

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=django_jalali.db.models.jDateTimeField(null=True),
        ),
    ]