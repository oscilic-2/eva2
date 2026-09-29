from django.db import models
from . choices import modelos
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Chofer(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creado = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
class Micro(models.Model):
    patente = models.CharField(max_length=6)
    modelo = models.CharField(max_length=50, choices=[(modelo, modelo) for modelo in modelos], default='LO916')
    numero = models.IntegerField()
    creado = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.patente} - {self.modelo}"
class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creado = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre
class Mantenimiento(models.Model):
    micro = models.ForeignKey(
        Micro,
        on_delete=models.CASCADE,
        related_name="mantenimientos"
    )
    repuesto = models.ForeignKey(
        Repuesto,
        on_delete=models.CASCADE,
        related_name="mantenimientos"
    )
    fecha = models.DateField(default=timezone.now)
    costo = models.IntegerField()
    intervalo_dias = models.PositiveIntegerField(default=30)

    @property
    def proxima_fecha(self):
        return self.fecha + timezone.timedelta(days=self.intervalo_dias)

    def __str__(self):
        return f"Mantenimiento de {self.micro} con {self.repuesto} el {self.fecha}"