from django.db import models


class Cliente(models.Model):
    monto = models.IntegerField()
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)


class Inversionista(models.Model):
    monto = models.IntegerField()
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
