from django.db import models

class Almacenes(models.Model):
    IdAlmacen = models.AutoField(primary_key=True)
    NombreAlmacen = models.CharField(max_length=200)
    Ubicacion = models.CharField(max_length=100)
    IdEstatus = models.BooleanField(default=1)

class TiposProducto(models.Model):
    IdTipoProducto = models.AutoField(primary_key=True)
    TipoProducto = models.CharField(max_length=200)

class Productos(models.Model):
    IdProducto = models.AutoField(primary_key=True)
    NombreProducto = models.CharField(max_length=200)