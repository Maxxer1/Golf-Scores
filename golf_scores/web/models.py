from django.db import models


class GolfCourse(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    par = models.IntegerField()

    def __str__(self):
        return self.name
