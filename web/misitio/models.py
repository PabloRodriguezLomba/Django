from django.db import models

# Create your models here.
from django.db import models


class Cliente(models.Model):
    dni = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=150,blank=False,null=False)
    alta = models.DateTimeField('Fecha Alta',blank=False,null=False)
    direccion = models.CharField(max_length=150,blank=False,null=True)
    mobile = models.CharField(max_length=150,blank=False,null=True)

class Printer(models.Model):
    Modelo = models.CharField(max_length=150,blank=False,null=False)
    Precio = models.FloatField(blank=False,null=False)