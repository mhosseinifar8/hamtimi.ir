# Generated by Django 2.2.1 on 2019-11-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0040_auto_20191112_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='support',
            name='id_support',
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
    ]
