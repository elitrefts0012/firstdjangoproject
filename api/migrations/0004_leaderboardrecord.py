# Generated by Django 2.2.12 on 2020-08-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_box_box_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderBoardRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_username', models.CharField(max_length=20)),
                ('time_seconds', models.IntegerField()),
                ('time_minutes', models.IntegerField()),
            ],
        ),
    ]
