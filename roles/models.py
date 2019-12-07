from django.db import models

class Roles(models.Model):
    IdRol = models.AutoField(primary_key=True)
    NombreRol = models.CharField(max_length=200)
    IdEstatus = models.BooleanField(default=1)

class Permisos(models.Model):
    IdPermiso = models.AutoField(primary_key=True)
    CampoId = models.CharField(max_length=200, default="")
    NombrePermiso = models.CharField(max_length=200)
    IdEstatus = models.BooleanField(default=1)

class PermisosAsignados(models.Model):
    IdPermisoAsignado = models.AutoField(primary_key=True)
    IdUsuario = models.IntegerField()
    IdPermiso = models.IntegerField()
    IdEstatus = models.BooleanField(default=1)