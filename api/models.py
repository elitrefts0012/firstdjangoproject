from django.db import models


class LeaderBoardRecord(models.Model):
    player_username = models.CharField(max_length=20)
    time_seconds = models.IntegerField()
    time_minutes = models.IntegerField()
    time_hundredths = models.IntegerField()


class Box(models.Model):
    horizontal_velocity = models.IntegerField()
    vertical_velocity = models.IntegerField()
    distance_top = models.IntegerField()
    distance_left = models.IntegerField()
    color = models.CharField(max_length=7)
    size = models.IntegerField()