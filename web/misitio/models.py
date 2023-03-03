from django.db import models

# Create your models here.
from django.db import models


class Cliente(models.Model):
    dni = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=150,blank=False,null=False)
    alta = models.DateTimeField('Fecha Alta',blank=False,null=False)
    direccion = models.CharField(max_length=150,blank=False,null=True)
    mobile = models.CharField(max_length=150,blank=False,null=True)

class Product(models.Model):
    nombre = models.CharField(max_length=150,primary_key=True)
    url = models.CharField(max_length=150,blank=False,null=False)
    precio = models.CharField(max_length=150,blank=False,null=False)
    stock = models.CharField(max_length=150,blank=False,null = False)
    Descripcion = models.CharField(max_length=500,blank=False,null=True)
