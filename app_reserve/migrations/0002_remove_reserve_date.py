# Generated by Django 2.2.1 on 2019-11-13 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_reserve', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='date',
        ),
    ]