# Generated by Django 2.2.1 on 2019-11-24 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reserve', '0007_reserve_salon_roof'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='salon_sport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
