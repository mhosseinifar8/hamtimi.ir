# Generated by Django 2.2.1 on 2019-12-22 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_reserve', '0020_auto_20191221_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserve',
            name='time',
        ),
    ]
