# Generated by Django 2.2.12 on 2020-07-23 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200711_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='box',
            name='box_id',
        ),
    ]
