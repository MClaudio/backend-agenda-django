from django.db import models

# Create your models here.

class Persona(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

class Telefono(models.Model):
    persona_fk = models.ForeignKey(Persona, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=100)
    operadora = models.CharField(max_length=100)