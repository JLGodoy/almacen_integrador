from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, AbstractUser,BaseUserManager


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class usuario(models.Model):
    username = models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 60)
    password = models.CharField(max_length = 30)
    is_staff = models.BooleanField(default = True)

class almacen(models.Model):
    nombre = models.CharField(max_length = 20)
    ubicacion = models.CharField(max_length = 20)
    estado = models.CharField(max_length = 20, blank = True)
    encargado = models.ForeignKey(User,null = True, blank = True, on_delete = models.CASCADE)
