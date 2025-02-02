from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class Professor(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)
    correu = models.CharField(max_length=100)
    curs = ArrayField(ArrayField(models.IntegerField()))
    rol = models.CharField(max_length=100)
    moduls = models.CharField(max_length=100)
