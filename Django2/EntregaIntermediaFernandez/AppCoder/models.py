from pyexpat import model
from django.db import models

class Alimentos(models.Model):
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=30)
    rangoEdad = models.CharField(max_length=30)
    calidad =models.CharField(max_length=30)
    
class Accesorios(models.Model):
    nombre= models.CharField(max_length=30)
    tipo= models.CharField(max_length=30)
    material = models.CharField(max_length=30)
   

class Servicios(models.Model):
    tipo= models.CharField(max_length=30)
    horarios= models.IntegerField()
   

class Contacto(models.Model):
    sucursal = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email= models.EmailField()


