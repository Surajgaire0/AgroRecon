# Generated by Django 3.1 on 2020-11-21 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_answer_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='answered_at',
            new_name='commented_at',
        ),
    ]