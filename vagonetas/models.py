from django.db import models

# Create your models here.

class Pañales (models.Model):
    nombre = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__ (self):
        return f'Nombre: {self.nombre} - Tamaño: {self.tamaño} - Precio: {self.precio}'

class Accesorios (models.Model):
    nombre = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return f'Nombre:{self.nombre} - Producto: {self.producto} - Precio: {self.precio}'

class Indumentaria (models.Model):
    nombre = models.CharField(max_length=100)
    talle = models.CharField(max_length=10)
    precio = models.IntegerField()

    def __str__(self):
        return f'Nombre:{self.nombre} - Talle: {self.talle} - Precio: {self.precio}'

class Perfumeria (models.Model):
    nombre = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return f'Nombre:{self.nombre} - Tamaño: {self.tamaño} - Precio: {self.precio}'

