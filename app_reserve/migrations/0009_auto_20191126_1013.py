# Generated by Django 2.2.1 on 2019-11-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reserve', '0008_reserve_salon_sport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]