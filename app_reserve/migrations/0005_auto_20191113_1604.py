# Generated by Django 2.2.1 on 2019-11-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reserve', '0004_auto_20191113_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='burn',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]