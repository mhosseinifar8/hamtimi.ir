# Generated by Django 2.2.1 on 2019-11-04 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0028_auto_20191104_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='resiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resiver', to=settings.AUTH_USER_MODEL),
        ),
    ]
