from django.db import models
from trainee.models import Trainee

class Tracking(models.Model):
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    progress = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.trainee.name} - {self.date}"
