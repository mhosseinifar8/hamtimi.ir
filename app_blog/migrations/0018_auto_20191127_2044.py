# Generated by Django 2.2.1 on 2019-11-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0017_remove_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
