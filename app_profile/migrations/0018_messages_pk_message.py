# Generated by Django 2.2.1 on 2019-08-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0017_auto_20190818_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='pk_message',
            field=models.IntegerField(null=True),
        ),
    ]
