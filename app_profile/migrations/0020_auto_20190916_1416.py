# Generated by Django 2.2.1 on 2019-09-16 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0019_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tell',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator('^[0][9][0-3][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$')]),
        ),
    ]
