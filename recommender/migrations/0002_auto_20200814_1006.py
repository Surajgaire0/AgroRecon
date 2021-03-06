# Generated by Django 3.0.7 on 2020-08-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant_recommend',
            name='coarse_tex_soils',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=10),
        ),
        migrations.AddField(
            model_name='plant_recommend',
            name='fine_tex_soils',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=10),
        ),
        migrations.AddField(
            model_name='plant_recommend',
            name='medium_tex_soils',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=10),
        ),
        migrations.AlterField(
            model_name='plant_recommend',
            name='drought_tolerance',
            field=models.CharField(choices=[('none', 'None'), ('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='Low', max_length=20),
        ),
        migrations.AlterField(
            model_name='plant_recommend',
            name='duration',
            field=models.CharField(blank=True, choices=[('perennial', 'Perennial'), ('annual', 'Annual'), ('biennial', 'Biennial')], default='annual', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='plant_recommend',
            name='growth_habit',
            field=models.CharField(blank=True, choices=[('shrub', 'Shrub'), ('forb/herb', 'Forb/Herb'), ('graminoid', 'Graminoid'), ('subshrub', 'Subshrub'), ('tree', 'Tree'), ('vine', 'Vine')], default='forb/herb', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='plant_recommend',
            name='shade_tolerance',
            field=models.CharField(choices=[('intolerant', 'Intolerant'), ('intermediate', 'Intermediate'), ('tolerant', 'Tolerant')], default='Intermediate', max_length=20),
        ),
    ]
