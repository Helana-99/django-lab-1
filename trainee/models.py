from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return self.name
