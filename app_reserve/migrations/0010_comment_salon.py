# Generated by Django 2.2.1 on 2019-11-27 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_reserve', '0009_auto_20191126_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=150, null=True)),
                ('created_time', django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True)),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cm', to='app_reserve.Reserve')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
