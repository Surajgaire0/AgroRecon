# Generated by Django 3.1 on 2020-11-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0005_auto_20201121_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='prediction',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
    ]