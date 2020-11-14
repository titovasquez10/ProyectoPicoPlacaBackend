from django.db import models

# Create your models here.

class Ciudades(models.Model):
    CiudadId = models.AutoField(primary_key=True)
    CiudadNombre = models.CharField(max_length=100)

class Picoplaca(models.Model):
    DigitoplacaId = models.AutoField(primary_key=True)
    DiaSemana = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)
    FechaEntrada = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
