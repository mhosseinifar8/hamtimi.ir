# Generated by Django 2.2.1 on 2019-11-04 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0024_remove_messages_pk_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]