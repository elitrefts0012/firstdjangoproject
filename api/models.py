from django.db import models


class Box(models.Model):
    horizontal_velocity = models.IntegerField()
    vertical_velocity = models.IntegerField()
    distance_top = models.IntegerField()
    distance_left = models.IntegerField()
    color = models.CharField(max_length=7)
    size = models.IntegerField()