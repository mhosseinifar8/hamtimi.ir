# Generated by Django 2.2.1 on 2019-10-27 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0034_auto_20191015_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='City',
            field=models.CharField(blank=True, choices=[('کرج', 'کرج'), ('تهران', 'تهران'), ('مشهد', 'مشهد'), ('اصفهان', 'اصفهان')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='Event_type',
            field=models.CharField(blank=True, choices=[('فوتبال', 'فوتبال'), ('تنیس', 'تنیس'), ('بسکتبال', 'بسکتبال'), ('والیبال', 'والیبال'), ('پینتبال', 'پینتبال'), ('بازی های کامپیوتری', 'بازی های کامپیوتری'), ('شطرنج', 'شطرنج'), ('دیگر', 'دیگر')], max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='gender',
            field=models.CharField(blank=True, choices=[('مرد', 'مرد'), ('زن', 'زن')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.CharField(blank=True, choices=[('البرز', 'البرز'), ('تهران', 'تهران'), ('خراسان شمالی', 'خراسان شمالی'), ('اصفهان', 'اصفهان')], max_length=30, null=True),
        ),
    ]
