# Generated by Django 2.2.12 on 2020-08-01 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_leaderboardrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboardrecord',
            name='time_hundredths',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
