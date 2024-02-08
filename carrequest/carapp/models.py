from django.db import models

# Create your models here.
class Car(models.Model):
    types=models.CharField(max_length=30)
    size=models.IntegerField()