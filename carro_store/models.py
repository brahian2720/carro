from django.db import models

# Create your models here.
class Marca (models.Model):
    name = models.CharField(max_length=255)

class Dueño (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cédula = models.IntegerField()
    nationality = models.CharField(max_length=255, null=True, blank=True)

class Car (models.Model):
    modelo = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    image_url = models.URLField(max_length=255, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class DueñoCar (models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)