# Generated by Django 2.0.6 on 2018-06-14 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Podcast', '0011_auto_20180614_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='Episode_Slug',
            new_name='slug',
        ),
    ]
