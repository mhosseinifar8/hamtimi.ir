# Generated by Django 2.2.1 on 2019-09-19 10:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_event', '0031_event_possibilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Possibilities',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('بوفه', 'بوفه'), ('سرویس بهداشتی', 'سرویس بهداشتی'), ('دوش و کمد', 'دوش و کمد'), ('رختکن', 'رختکن'), ('پارکینگ', 'پارکینگ'), ('فروشگاه', 'فروشگاه'), ('تهویه هوا', 'تهویه هوا'), ('فضای سبز', 'فضای سبز'), ('ماساژ', 'ماساژ'), ('جایگاه تماشاچیان', 'جایگاه تماشاچیان'), ('توپ', 'توپ'), ('مربی', 'مربی')], max_length=100, null=True),
        ),
    ]