from django.db import models

# Create your models here.

class Vivienda(models.Model):
    numero           = models.PositiveSmallIntegerField(primary_key=True)
    nombres           = models.CharField(max_length=50)
    apellido_pat     = models.CharField(max_length=50)
    apellido_mat     = models.CharField(max_length=50)