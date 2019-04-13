from django.db import models


class GolfCourse(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    par = models.IntegerField()

    def __str__(self):
        return self.name


class Score(models.Model):
    date = models.DateField()
    golf_course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE, related_name='golf_course')
    score = models.IntegerField()
    to_par = models.IntegerField(editable=False)

    def __str__(self):
        return f'{self.date} - {self.golf_course} - {self.score}'
