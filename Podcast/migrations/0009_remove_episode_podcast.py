# Generated by Django 2.0.6 on 2018-06-13 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Podcast', '0008_auto_20180613_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='podcast',
        ),
    ]