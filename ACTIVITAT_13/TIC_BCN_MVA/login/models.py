from django.db import models

# Create your models here.
class Person:
    id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True)
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100)

