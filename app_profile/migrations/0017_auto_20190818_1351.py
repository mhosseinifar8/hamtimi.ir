# Generated by Django 2.2.1 on 2019-08-18 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0016_auto_20190818_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='resiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messages',
            name='sender',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
