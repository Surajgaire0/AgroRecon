# Generated by Django 3.1 on 2020-10-21 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20201005_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='downvote',
        ),
    ]
