from django.db import models


# Create your models here.


class Clientes(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


class Meseros(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.dni}"


class Mesas(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.numero}"
