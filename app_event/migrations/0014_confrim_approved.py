# Generated by Django 2.2.1 on 2019-07-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0013_remove_confrim_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='confrim',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
