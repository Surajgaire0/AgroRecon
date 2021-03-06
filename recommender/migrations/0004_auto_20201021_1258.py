# Generated by Django 3.1 on 2020-10-21 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0003_auto_20200904_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='max_ph',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(14)]),
        ),
        migrations.AlterField(
            model_name='recommend',
            name='min_ph',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(14)]),
        ),
    ]
