# Generated by Django 2.2.1 on 2019-07-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0018_auto_20190704_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confrim',
            name='user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
