# Generated by Django 2.2.1 on 2019-10-07 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_blog', '0014_auto_20191007_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='REP_CM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100, null=True)),
                ('create_time', django_jalali.db.models.jDateField(auto_now_add=True, null=True)),
                ('rep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rep', to='app_blog.Comment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='rep',
        ),
    ]