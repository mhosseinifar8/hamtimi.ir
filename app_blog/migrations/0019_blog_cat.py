# Generated by Django 2.2.1 on 2019-12-19 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0018_auto_20191127_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
