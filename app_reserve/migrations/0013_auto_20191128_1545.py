# Generated by Django 2.2.1 on 2019-11-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reserve', '0012_auto_20191128_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_salon',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment_salon',
            name='user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
